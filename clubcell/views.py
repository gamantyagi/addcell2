import json

from django.utils import timezone
from django.http import HttpResponse
from django.template.loader import render_to_string

from clubcell.models import events, clubcell, events, messages, typing_message, event_participants, posts, \
    event_wishlist, group_event, related_images, custom_input
from .General import General, GoTo
from django.contrib.auth.models import User
from .Constants import Paths, Pages, Alerts
from .Common import Rendering, GetData, InCSV
import os


class Entry:

    @staticmethod
    def login(request):
        # Return True if login succeed
        if General.login_by_request(request):
            return GoTo.redirect_to(Paths.HOMEPAGE)
        else:
            # alert will send to the user if submitted username or password is incorrect
            General.message_response(request, if_method='POST', alert=Alerts.LOGIN_FAILED_MESSAGE)
            return GoTo.render_page(request, Pages.LOGIN)

    @staticmethod
    def homepage(request):
        if request.user.is_authenticated:
            if GetData.is_user_having_club(request):
                return GoTo.redirect_to(Paths.CLUB_HOME)
            else:
                return GoTo.redirect_to(Paths.STUDENT_HOME)
        else:
            return GoTo.redirect_to(Paths.LOGIN)

    @staticmethod
    def signup(request):
        # Return True if registration succeed
        if not request.user.is_authenticated:
            if General.signup(request):
                return GoTo.landing_page()
            else:
                return GoTo.render_page(request, Pages.SIGNUP)
        else:
            # Landing page is root url of site
            return GoTo.landing_page()

    @staticmethod
    def logout(request):
        General.logout_user(request)
        return GoTo.landing_page()


class Club:

    @staticmethod
    def having_permission(request):
        if request.user.is_authenticated and request.user.details.having_club:
            return True
        return False

    @staticmethod
    def home(request):
        # This function is used for club dashboard
        if Club.having_permission(request):
            user = request.user
            GetData.distinct_messages(request)
            return GoTo.render_page(request, Pages.CLUB_HOME, {'user': request.user,
                                                               'alert_unseen': user.alerts.filter(seen=False).count,
                                                               'events_done': user.clubcell.events.filter(
                                                                   event_complete='D'),
                                                               'events_todo': user.clubcell.events.filter(
                                                                   event_complete='P'),
                                                               'messages': GetData.distinct_messages(
                                                                   request, 'all')})
        return GoTo.landing_page()

    @staticmethod
    def profile_view(request):
        if Club.having_permission(request):
            return GoTo.render_page(request, Pages.CLUB_PROFILE_VIEW,
                                    {'user': request.user,
                                     'events_done': request.user.clubcell.events.filter(event_complete='D')})
        return GoTo.landing_page()

    @staticmethod
    def my_cell(request):
        if Club.having_permission(request):
            user = request.user
            return GoTo.render_page(request, Pages.CLUB_MY_CELL, {'user': request.user,
                                                                  'alert_unseen': user.alerts.filter(seen=False).count,
                                                                  'messages': GetData.distinct_messages(request)})
        return GoTo.landing_page()

    @staticmethod
    def add_event(request):
        user = request.user
        return GoTo.render_page(request, Pages.ClUB_ADD_EVENT, {'user': request.user,
                                                                'alert_unseen': user.alerts.filter(seen=False).count,
                                                                'messages': GetData.distinct_messages(request),
                                                                'inbuilt_inputs': custom_input.objects.filter(club=None),
                                                                'custom_inputs': custom_input.objects.filter(club=user.clubcell)})

    @staticmethod
    def event_todo_main(request, event_uen):
        # this method is use to manipulate only any one event todo's
        if Club.having_permission(request):
            user = request.user
            event = events.objects.get(club=user.clubcell, event_uen=event_uen)
            return GoTo.render_page(request, Pages.EVENT_TODO_MAIN, {'event': event,
                                                                     'alert_unseen': user.alerts.filter(
                                                                         seen=False).count,
                                                                     'messages': GetData.distinct_messages(request)})
        # return Club.events_todo(request)

    @staticmethod
    def events_todo(request):
        if Club.having_permission(request):
            user = request.user
            return GoTo.render_page(request, Pages.EVENTS_TODO,
                                    {'events_todo': reversed(user.clubcell.events.filter(event_complete='P'))})
        return GoTo.landing_page()

    @staticmethod
    def event_done(request):
        if Club.having_permission(request):
            user = request.user
            return GoTo.render_page(request, Pages.EVENTS_DONE, {'user': request.user,
                                                                 'alert_unseen': user.alerts.filter(seen=False).count,
                                                                 'events_done': user.clubcell.events.filter(
                                                                     event_complete='D'),
                                                                 'messages': GetData.distinct_messages(request),
                                                                 'groups': group_event.objects.filter(
                                                                     club=user.clubcell, parent_group=None),
                                                                 'events_done': reversed(
                                                                     user.clubcell.events.filter(group_event=None))})
        return GoTo.landing_page()

    @staticmethod
    def update_profile(request):
        if Club.having_permission(request) and request.method == "POST":
            user = request.user

            username = request.POST['username'].lower().lstrip()
            first_name = (request.POST['first_name']).lower().lstrip()
            last_name = (request.POST['last_name']).lower().lstrip()
            email = request.POST['email'].lstrip()
            if username != '' and first_name != '' and last_name != '' and email != '':
                user.email, user.last_name, user.first_name, user.username = email, last_name, first_name, username
                user.save()
        return GoTo.redirect_to(Paths.CLUB_PROFILE_VIEW)

    @staticmethod
    def update_cell(request):
        if Club.having_permission(request) and request.method == "POST":
            user = request.user
            cell = clubcell.objects.get(PAN=user.details.PAN)
            cellname = request.POST['cellname'].lower().lstrip()
            offemail = (request.POST['offemail']).lower().lstrip()
            about = (request.POST['about']).lower().lstrip()
            tel = request.POST['tel'].lstrip()
            cell.off_email, cell.clubname, cell.tel, cell.about = offemail, cellname, tel, about
            cell.save()
        return GoTo.redirect_to(Paths.CLUB_PROFILE_VIEW)

    @staticmethod
    def members(request):
        if Club.having_permission(request):
            user = request.user
            return GoTo.render_page(request, Pages.CLUB_MEMBERS, {'user': request.user,
                                                                  'alert_unseen': user.alerts.filter(seen=False).count,
                                                                  'messages': GetData.distinct_messages(request),
                                                                  'teams': user.clubcell.team.all()})

    @staticmethod
    def posts(request):
        if Club.having_permission(request):
            user = request.user
            return GoTo.render_page(request, Pages.CLUB_POSTS, {'user': request.user,
                                                                'alert_unseen': user.alerts.filter(seen=False).count,
                                                                'messages': GetData.distinct_messages(request),
                                                                'posts': posts.objects.filter(user=user)})

    @staticmethod
    def addcells(request):
        if Club.having_permission(request):
            user = request.user
            return GoTo.render_page(request, Pages.CLUB_ADDCELLS, {'user': request.user,
                                                                   'alert_unseen': user.alerts.filter(seen=False).count,
                                                                   'messages': GetData.distinct_messages(request)})

    @staticmethod
    def trending(request):
        if Club.having_permission(request):
            user = request.user
            return GoTo.render_page(request, Pages.CLUB_TRENDING, {'user': request.user,
                                                                   'alert_unseen': user.alerts.filter(seen=False).count,
                                                                   'messages': GetData.distinct_messages(request)})


class Student:

    @staticmethod
    def home(request):  # explore option
        if request.user.is_authenticated:
            user = request.user
            return GoTo.render_page(request, Pages.STUDENT_HOME, {'user': user,
                                                                  'events_todo': events.objects.filter(
                                                                      event_complete='P'),
                                                                  'event_registered': GetData.registered_event(user)})

    @staticmethod
    def profile(request):
        if request.user.is_authenticated:
            user = request.user
            return GoTo.render_page(request, Pages.STUDENT_PROFILE, {'user': user,
                                                                     'events_participants': event_participants.objects.filter(
                                                                         user=user)})

    @staticmethod
    def posts(request):
        if request.user.is_authenticated:
            user = request.user
            return GoTo.render_page(request, Pages.STUDENT_POSTS, {'user': user,
                                                                   'posts': posts.objects.all()})

    @staticmethod
    def event_register_form(request, event_uen):
        if request.method == "GET" and request.user.is_authenticated:
            user = request.user
            event = events.objects.get(event_uen=event_uen)
            if event.registration and not event_participants.objects.filter(events=event, user=user).exists():
                inputs = []
                for inp in event.custom_inputs.all():
                    try:
                        inputs.append([inp, user.custom_input_value.get(input=inp).value])
                    except:
                        inputs.append([inp, ''])

                return GoTo.render_page(request, "studentcell/register_event.html", {'event': event,
                                                                                     'inputs': inputs})
            else:
                status = user.event_participants.get(events=event)
                if status.payment_done:
                    return HttpResponse("You already registered for this event, and verified.")
                else:
                    return HttpResponse(
                        'You already registered for this event, but payment is not done #%s' % status.cash_acceptor)


class CommonMethod:

    @staticmethod
    def view_event_detail(request, event_uen):
        user = request.user
        event = events.objects.get(event_uen=event_uen)
        return GoTo.render_page(request, Pages.CLUB_EVENT_DETAIL, {'user': user,
                                                                   'event': event,
                                                                   'event_images': related_images.objects.filter(
                                                                       event=event, type="collapse"),
                                                                   'event_registered': GetData.registered_event(user),
                                                                   'event_query': event.event_query.filter(replied=None)
                                                                   })


class Message:

    @staticmethod
    def chat(request, chat_to):
        if request.user.is_authenticated:
            user = request.user
            chat_to_user = User.objects.get(username=chat_to)
            try:
                event_to = request.GET['e']
                event_to_model = events.objects.get(event_uen=event_to)
            except:
                event_to = ''

            chats_count = (messages.objects.filter(user=chat_to_user, second_user=user).union(
                messages.objects.filter(user=user, second_user=chat_to_user))).order_by('date_and_time').count()

            chats = (messages.objects.filter(user=chat_to_user, second_user=user).union(
                messages.objects.filter(user=user, second_user=chat_to_user))).order_by('date_and_time')[::-1][0:100][
                    ::-1]
            return GoTo.render_page(request, Pages.CHAT_PANEL, {'chat_to': chat_to_user,
                                                                'user': user,
                                                                'chats': chats,
                                                                'chats_count': chats_count,
                                                                'event_to': event_to
                                                                })

    @staticmethod
    def get_new_message(request, chat_to):
        if request.user.is_authenticated and request.is_ajax():
            user = request.user
            gpk = request.POST['element']
            result_copy = request.POST['result_copy']
            txt_len = int(request.POST['text'])
            chat_to_user = User.objects.get(username=chat_to)
            # now we will get if second user is typing or not and set if we are also typing
            second_typing = GetData.typing_message(txt_len, user, chat_to_user)
            chats = (messages.objects.filter(user=chat_to_user, second_user=user).union(
                messages.objects.filter(user=user, second_user=chat_to_user))).order_by('date_and_time')
            last = chats.latest('date_and_time')
            if last.user == chat_to_user and last.seen == False:
                last.seen = True
                last.save()
            if last.pk == int(gpk):
                return HttpResponse(json.dumps("%dt" % second_typing), content_type="application/json")
            elif last.pk != int(gpk) and int(gpk) < last.pk and last.user != user:
                html = render_to_string('common/new_msg_box.html', {'user': user,
                                                                    'chat_to': chat_to_user,
                                                                    'message': last
                                                                    },
                                        request=request)
                dict_data = {'result': 1, 'html': html, 'id': last.pk}
                return HttpResponse(json.dumps(dict_data), content_type="application/json")
            else:
                # return HttpResponse(json.dumps("-1"), content_type="application/json")
                return HttpResponse(json.dumps("-1"), content_type="application/json")
        else:
            return HttpResponse(json.dumps("unknown"), content_type="application/json")

    @staticmethod
    def post_new_message(request):
        if request.user.is_authenticated and request.method == "POST" and request.is_ajax():
            user = request.user
            chat_to = request.POST['second_user']
            chat_to_user = User.objects.get(username=chat_to)
            message_sent = request.POST['message']
            message_sent = message_sent.lstrip()
            if message_sent != '':
                e = request.POST['event_to']
                try:
                    event = events.objects.get(event_uen=e)
                except:
                    event = None
                now = timezone.now()
                new_msg = messages(user=user, second_user=chat_to_user, message_in=message_sent, date_and_time=now,
                                   event=event)
                new_msg.save()
                new_msg = messages.objects.get(user=user, second_user=chat_to_user, message_in=message_sent,
                                               date_and_time=now)

                html = render_to_string('common/new_msg_box.html', {'user': user,
                                                                    'chat_to': chat_to_user,
                                                                    'message': new_msg
                                                                    },
                                        request=request)
                return HttpResponse(html)
            return HttpResponse('')
