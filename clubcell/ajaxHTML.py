# this file only contain html variables.

CUSTOM_USER_INPUT = '''
{% for inp in custom_inputs %}
                            <div class="form-check col-4" data-toggle="tooltip" title="Hint: {{inp.input_reference}}, Type: {{inp.get_input_type_display}}, Entry: {{inp.required|yesno:'required,optional'}}">
                              <label class="form-check-label">
                                <input type="checkbox" class="form-check-input" value="{{inp.input_name}}:-{{inp.pk}}">{{inp.input_name}}
                              </label>
                            </div>
                            {% empty %}
                                <b>No Custom inputs created yet in your club.</b>
                          {% endfor %}
'''

