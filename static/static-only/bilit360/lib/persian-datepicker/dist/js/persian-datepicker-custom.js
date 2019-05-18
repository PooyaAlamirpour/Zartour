(function (jQuery) {

    var current_calendar = "persian";//gregorian
    var calendar_separator = "/";
    var calendar_format = "YYYY-MM-DD";

    if ((typeof  fmt) !== "undefined") {
        if (fmt.indexOf('-') != -1)
            calendar_separator = "-";
        calendar_format = fmt.toUpperCase();
    }

    //var calendar_persian_format = "DD" + calendar_separator + "MM" + calendar_separator + "YYYY";
    var year_index = 0;
    var month_index = 0;
    var day_index = 0;
    var calendar_split = calendar_format.split(calendar_separator);


    for (var i = 0; i < calendar_split.length; i++) {
        if (calendar_split[i].toUpperCase() == "DD")
            day_index = i;
        else if (calendar_split[i].toUpperCase() == "MM")
            month_index = i;
        else if (calendar_split[i].toUpperCase() == "YYYY")
            year_index = i;
    }

    function switchCalendar(current) {
        var state = (current == "persian") ? true : false;
        jQuery('.calendar-switch input').bootstrapSwitch('state', state)
    }

    var customTemplate = "\n<div id=\"plotId\" class=\"datepicker-plot-area {{cssClass}}\">\n" +
        "{{#navigator.enabled}}\n<div data-navigator class=\"datepicker-navigator\">\n" +
        "<div class=\"pwt-btn pwt-btn-next\">{{navigator.text.btnNextText}}</div>\n" +
        " <div class=\"pwt-btn pwt-btn-switch\">{{navigator.switch.text}}</div>\n" +
        "<div class=\"pwt-btn pwt-btn-prev\">{{navigator.text.btnPrevText}}</div>\n</div>\n" +
        "  {{/navigator.enabled}}\n<div class=\"datepicker-grid-view\">\n{{#days.enabled}}\n" +
        " {{#days.viewMode}}\n<div class=\"datepicker-day-view\" >\n" +
        "<div class=\"month-grid-box\">\n<div class=\"header\">\n" +
        "<div class=\"title\"></div>\n<div class=\"header-row\">\n" +
        "{{#weekdays.list}}\n<div class=\"header-row-cell\">{{.}}</div>\n" +
        "{{/weekdays.list}}\n</div>\n</div>\n" +
        "<table cellspacing=\"0\" class=\"table-days\">\n<tbody>\n" +
        "{{#days.list}}\n\n<tr>\n" +
        "{{#.}}\n{{#enabled}}\n" +
        "<td data-date=\"{{dataDate}}\" data-unix=\"{{dataUnix}}\" >\n" +
        "<span  class=\"{{#otherMonth}}other-month{{/otherMonth}}\">{{title}}</span>\n" +
        "{{#altCalendarShowHint}}\n" +
        " <i  class=\"alter-calendar-day\">{{alterCalTitle}}</i>\n" +
        " {{/altCalendarShowHint}}\n</td>\n{{/enabled}}\n{{^enabled}}\n" +
        "<td data-date=\"{{dataDate}}\" data-unix=\"{{dataUnix}}\" class=\"disabled\">\n" +
        "<span class=\"{{#otherMonth}}other-month{{/otherMonth}}\">{{title}}</span>\n" +
        "{{#altCalendarShowHint}}\n<i  class=\"alter-calendar-day\">{{alterCalTitle}}</i>\n{{/altCalendarShowHint}}\n</td>\n" +
        "{{/enabled}}\n\n{{/.}}\n</tr>\n" +
        "{{/days.list}}\n                    </tbody>\n                </table>\n            </div>\n        </div>\n        {{/days.viewMode}}\n    " +
        "{{/days.enabled}}\n    \n    {{#month.enabled}}\n        {{#month.viewMode}}\n            <div class=\"datepicker-month-view\">\n                " +
        "{{#month.list}}\n                    {{#enabled}}               \n                        " +
        "<div data-month=\"{{dataMonth}}\" class=\"month-item {{#selected}}selected{{/selected}}\">{{title}}</small></div>\n                   " +
        " {{/enabled}}\n                    {{^enabled}}               \n                        " +
        "<div data-month=\"{{dataMonth}}\" class=\"month-item month-item-disable {{#selected}}selected{{/selected}}\">{{title}}</small></div>\n                    " +
        "{{/enabled}}\n                {{/month.list}}\n            </div>\n        {{/month.viewMode}}\n    {{/month.enabled}}\n    \n    {{#year.enabled }}\n       " +
        " {{#year.viewMode }}\n            <div class=\"datepicker-year-view\" >\n                {{#year.list}}\n                    {{#enabled}}\n                    " +
        "    <div data-year=\"{{dataYear}}\" class=\"year-item {{#selected}}selected{{/selected}}\">{{title}}</div>\n                    {{/enabled}}\n                 " +
        "   {{^enabled}}\n                        <div data-year=\"{{dataYear}}\" class=\"year-item year-item-disable {{#selected}}selected{{/selected}}\">{{title}}</div>\n                    " +
        "{{/enabled}}                    \n                {{/year.list}}\n            </div>\n        {{/year.viewMode }}\n    {{/year.enabled }}\n    \n    </div>\n    {{#time}}\n   " +
        " {{#enabled}}\n    <div class=\"datepicker-time-view\">\n        {{#hour.enabled}}\n            <div class=\"hour time-segment\" data-time-key=\"hour\">\n              " +
        "  <div class=\"up-btn\" data-time-key=\"hour\">\u25B2</div>\n                <input value=\"{{hour.title}}\" type=\"text\" placeholder=\"hour\" class=\"hour-input\">\n               " +
        " <div class=\"down-btn\" data-time-key=\"hour\">\u25BC</div>                    \n            </div>       \n            <div class=\"divider\">\n                <span>:</span>\n    " +
        "        </div>\n        {{/hour.enabled}}\n        {{#minute.enabled}}\n            <div class=\"minute time-segment\" data-time-key=\"minute\" >\n             " +
        "   <div class=\"up-btn\" data-time-key=\"minute\">\u25B2</div>\n                <input disabled value=\"{{minute.title}}\" type=\"text\" placeholder=\"minute\" class=\"minute-input\">\n   " +
        "             <div class=\"down-btn\" data-time-key=\"minute\">\u25BC</div>\n            </div>        \n            <div class=\"divider second-divider\">\n               " +
        " <span>:</span>\n            </div>\n        {{/minute.enabled}}\n        {{#second.enabled}}\n            <div class=\"second time-segment\" data-time-key=\"second\"  >\n     " +
        "           <div class=\"up-btn\" data-time-key=\"second\" >\u25B2</div>\n              " +
        "  <input disabled value=\"{{second.title}}\"  type=\"text\" placeholder=\"second\" class=\"second-input\">\n          " +
        "      <div class=\"down-btn\" data-time-key=\"second\" >\u25BC</div>\n            </div>\n           " +
        " <div class=\"divider meridian-divider\"></div>\n            <div class=\"divider meridian-divider\"></div>\n      " +
        "  {{/second.enabled}}\n        {{#meridian.enabled}}\n            <div class=\"meridian time-segment\" data-time-key=\"meridian\" >\n    " +
        "            <div class=\"up-btn\" data-time-key=\"meridian\">\u25B2</div>\n              " +
        "  <input disabled value=\"{{meridian.title}}\" type=\"text\" class=\"meridian-input\">\n          " +
        "      <div class=\"down-btn\" data-time-key=\"meridian\">\u25BC</div>\n            </div>\n      " +
        "  {{/meridian.enabled}}\n    </div>\n    {{/enabled}}\n    {{/time}}\n    \n    {{#toolbox}}\n    {{#enabled}}\n    " +
        "<div class=\"toolbox\">\n        {{#toolbox.submitButton.enabled}}\n            <div class=\"pwt-btn-submit\">{{submitButtonText}}</div>\n  " +
        "      {{/toolbox.submitButton.enabled}}        \n        {{#toolbox.todayButton.enabled}}\n           " +
        " <div class=\"pwt-btn-today\">{{todayButtonText}}</div>\n    " +
        "    {{/toolbox.todayButton.enabled}}        \n        {{#toolbox.calendarSwitch.enabled}}\n          " +
        "  <div class=\"pwt-btn-calendar\"><div class='calendar-switch-overlay'></div><div class='calendar-switch'><input type=\"checkbox\" ></div></div>\n" +
        "{{/toolbox.calendarSwitch.enabled}}\n</div>\n" +
        " {{/enabled}}\n    {{^enabled}}\n        {{#onlyTimePicker}}\n        <div class=\"toolbox\">\n            <div class=\"pwt-btn-exit\">{{text.btnExit}}</div>\n    " +
        "    </div>\n        {{/onlyTimePicker}}\n    {{/enabled}}\n    {{/toolbox}}\n</div>\n " +
        "<script> jQuery(\".calendar-switch input\").bootstrapSwitch({\n" +
        "                    size: 'mini',\n" +
        "                    onText : \"Gregorian\",\n" +
        "                    offText : \"شمسی\",\n" +
        "                    onSwitchChange: function (event, state) {\n" +
        "                         " +
        "                        \n" +
        "                    }\n" +
        "                });</script>";
    jQuery.fn.datepicker = function (options) {
        //.datepicker("option", "minDate", selectedDate);
        //.datepicker("option", "maxDate", selectedDate);
        //.advancedDatepicker( 'setDate', d );
        if (options == "getDate") {
            var get_current_date = jQuery(this).val();
            if (get_current_date == "" || get_current_date == undefined)
                return 0;
            else
                return new Date(get_current_date);
        } else {
            var defaults = {
                autoClose: true,
                template: customTemplate,
                initialValue: false,
                observer: true,
                minDate: "today",
                toolbox: {
                    calendarSwitch: {
                        onSwitch: function onSwitch(datepickerObject) {
                            current_calendar = datepickerObject.options.calendar_;
                            switchCalendar(current_calendar);
                        }
                    },
                    onToday: function (datepickerObject) {
                        switchCalendar(current_calendar);
                    }
                },
                calendar: {
                    persian: {
                        locale: 'fa'
                    },
                    gregorian: {
                        showHint: true
                    }
                },
                navigator: {
                    onNext: function (datepickerObject) {
                        switchCalendar(current_calendar);
                    },
                    onPrev: function (datepickerObject) {
                        switchCalendar(current_calendar);
                    },
                    onSwitch: function (datepickerObject) {
                        switchCalendar(current_calendar);
                    }
                },
                onShow: function onShow(datepickerObject) {

                },
                onSelect: function (unixDate) {
                    switchCalendar(current_calendar);
                },
                onSwitch: function (datepickerObject) {

                },
                altFieldFormatter: function (unixDate) {
                    var alt_format = moment(unixDate).format(calendar_format);
                    return alt_format;
                }
            };
            options = jQuery.extend(defaults, options);
            if (options.format == undefined)
                options.format = "YYYY-MM-DD";
            options.format = options.format.toUpperCase();
            console.log(options.format);
            return this.each(function () {

                var element = jQuery(this);
                var altField = element.clone();
                altField.attr("type", "hidden");
                altField.attr("class", element.attr("name") + "_alt_field");
                element.after(altField);
                element.addClass("input-" + element.attr("name"));
                element.removeAttr("name");
                //altField.removeAttr("name");
                altField.removeAttr("disabled");
                altField.removeAttr("placeholder");




                options.altField = element.next();
                options.calendarType = current_calendar;
                options.initialValueType = 'persian';
                options.initialValue = false;
				options.format = "YYYY-MM-DD";
                var travel_date_picker = element.persianDatepicker(options);
                if (element.val() != "" && element.val() != undefined) {
                    var current_date = element.val().split(calendar_separator);
                    var current_date_timestamp = new Date(current_date[year_index], current_date[month_index] - 1, current_date[day_index]).getTime();

                    travel_date_picker.setDate(current_date_timestamp);
                }
            });
        }
    };
})(jQuery);