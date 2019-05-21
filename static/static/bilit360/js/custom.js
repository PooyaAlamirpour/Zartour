$('.search__result .content .search__result__items .more__info__systemi').click(function(){
  $('.search__result .content .tab__option__systemi').slideToggle();
});

$('.search__result .content .search__result__items .more__info__charteri').click(function(){
  $('.search__result .content .tab__option__charteri').slideToggle();
});

$('.search__result .content .search__result__items__blite .more__info__charteri').click(function(){

  $('.search__result .content .tab__option__systemi').slideToggle();
});



var clock;

$(document).ready(function () {
  var clock;

  clock = $('.timer').FlipClock({
    clockFace: 'MinuteCounter',
    autoStart: false,
    callbacks: {
      stop: function () {
        $('.message').html('The clock has stopped!')
      }
    }
  });

  clock.setTime(2208);
  clock.setCountdown(true);
  clock.start();

});

var pkclock;

$(document).ready(function () {
  var pkclock;

  pkclock = $('.pkclock').FlipClock({
    clockFace: 'DailyCounter',
    language:'fa-ir',
    autoStart: false,
    callbacks: {
      stop: function () {
        $('.message').html('The clock has stopped!')
      }
    }
  });

  pkclock.setTime(22208);
  pkclock.setCountdown(true);
  pkclock.start();

});

$(document).ready(function () {

  $('.search__tour__timer').each(function () {
      var clocktt;

      clocktt = $(this).FlipClock({
          clockFace: 'HourCounter',
          autoStart: false,
          callbacks: {
              stop: function () {
                  $('.message').html('The clock has stopped!')
              }
          }
      });

      clocktt.setTime(22208);
      clocktt.setCountdown(true);
      clocktt.start();
  })
});


$('.slider').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  arrows: false,
  // autoplay: true,
  // autoplaySpeed: 2000,
  infinite: true,

  asNavFor: '.title__slider'

});
$('.title__slider').slick({
  slidesToShow: 4,
  slidesToScroll: 1,
  asNavFor: '.slider',
  dots: false,
  centerMode: true,
  focusOnSelect: true
});
$('.leatest__inner__tour .items').slick({
  slidesToShow: 4,
  slidesToScroll: 1,
  arrows: false,
  //  autoplay: true,
  //  autoplaySpeed: 2000,
  infinite: true,
  dots: true,
  rtl: true,
  responsive: [{
      breakpoint: 1024,
      settings: {
        slidesToShow: 3,

      }
    },
    {
      breakpoint: 768,
      settings: {
        slidesToShow: 2,

      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,

      }
    }
    // You can unslick at a given breakpoint now by adding:
    // settings: "unslick"
    // instead of a settings object
  ]
});

$('.leatest__hotel .items').slick({
  slidesToShow: 4,
  slidesToScroll: 1,
  arrows: false,
  //  autoplay: true,
  //  autoplaySpeed: 2000,
  infinite: true,
  dots: true,
  rtl: true,
  responsive: [{
      breakpoint: 1024,
      settings: {
        slidesToShow: 3,

      }
    },
    {
      breakpoint: 768,
      settings: {
        slidesToShow: 2,

      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,

      }
    }
    // You can unslick at a given breakpoint now by adding:
    // settings: "unslick"
    // instead of a settings object
  ]
});




$('.mobile__menu').click(function () {
  $('header .top__menu .menu nav ul').slideToggle();
});


///index calander
const calanderConfig={
  initialValueType: 'gregorian',
    "inline": false,
    "format": "l",
    "viewMode": "day",
    "initialValue": false,    
    "position": "auto",
    "altFormat": "unix",
    "altField": "#arrival_date",
    "onlyTimePicker": false,
    "onlySelectOnDate": false,
    "calendarType": "persian",
    "inputDelay": 800,
    "observer": true,
    "calendar": {
      "persian": {
        "locale": "fa",
        "showHint": true,
        "leapYearMode": "algorithmic"
      },
      "gregorian": {
        "locale": "en",
        "showHint": false
      }
    },
    "navigator": {
      "enabled": true,
      "scroll": {
        "enabled": true
      },
      "text": {
        "btnNextText": "<",
        "btnPrevText": ">"
      }
    },
    "toolbox": {
      "enabled": true,
      "calendarSwitch": {
        "enabled": false,
        "format": "MMMM"
      },
      "todayButton": {
        "enabled": true,
        "text": {
          "fa": "امروز",
          "en": "Today"
        }
      },
      "submitButton": {
        "enabled": true,
        "text": {
          "fa": "تایید",
          "en": "Submit"
        }
      },
      "text": {
        "btnToday": "امروز"
      }
    },
    "timePicker": {
      "enabled": false,
      "step": 1,
      "hour": {
        "enabled": false,
        "step": null
      },
      "minute": {
        "enabled": false,
        "step": null
      },
      "second": {
        "enabled": false,
        "step": null
      },
      "meridian": {
        "enabled": true
      }
    },
    "dayPicker": {
      "enabled": true,
      "titleFormat": "YYYY MMMM"
    },
    "monthPicker": {
      "enabled": true,
      "titleFormat": "YYYY"
    },
    "yearPicker": {
      "enabled": true,
      "titleFormat": "YYYY"
    },
    "responsive": true
  };

const calanderForeignConfig={
  initialValueType: 'gregorian',
    "inline": false,
    "format": "l",
    "viewMode": "day",
    "initialValue": false,
    "position": "auto",
    "altFormat": "unix",
    "altField": "#arrival_foreign_date",
    "onlyTimePicker": false,
    "onlySelectOnDate": false,
    "calendarType": "persian",
    "inputDelay": 800,
    "observer": true,
    "calendar": {
      "persian": {
        "locale": "fa",
        "showHint": true,
        "leapYearMode": "algorithmic"
      },
      "gregorian": {
        "locale": "en",
        "showHint": false
      }
    },
    "navigator": {
      "enabled": true,
      "scroll": {
        "enabled": true
      },
      "text": {
        "btnNextText": "<",
        "btnPrevText": ">"
      }
    },
    "toolbox": {
      "enabled": true,
      "calendarSwitch": {
        "enabled": false,
        "format": "MMMM"
      },
      "todayButton": {
        "enabled": true,
        "text": {
          "fa": "امروز",
          "en": "Today"
        }
      },
      "submitButton": {
        "enabled": true,
        "text": {
          "fa": "تایید",
          "en": "Submit"
        }
      },
      "text": {
        "btnToday": "امروز"
      }
    },
    "timePicker": {
      "enabled": false,
      "step": 1,
      "hour": {
        "enabled": false,
        "step": null
      },
      "minute": {
        "enabled": false,
        "step": null
      },
      "second": {
        "enabled": false,
        "step": null
      },
      "meridian": {
        "enabled": true
      }
    },
    "dayPicker": {
      "enabled": true,
      "titleFormat": "YYYY MMMM"
    },
    "monthPicker": {
      "enabled": true,
      "titleFormat": "YYYY"
    },
    "yearPicker": {
      "enabled": true,
      "titleFormat": "YYYY"
    },
    "responsive": true
  };

const calanderConfig_return={
  initialValueType: 'gregorian',
    "inline": false,
    "format": "l",
    "viewMode": "day",
    "initialValue": false,
    "position": "auto",
    "altFormat": "unix",
    "altField": "#return_date",
    "onlyTimePicker": false,
    "onlySelectOnDate": false,
    "calendarType": "persian",
    "inputDelay": 800,
    "observer": true,
    "calendar": {
      "persian": {
        "locale": "fa",
        "showHint": true,
        "leapYearMode": "algorithmic"
      },
      "gregorian": {
        "locale": "en",
        "showHint": false
      }
    },
    "navigator": {
      "enabled": true,
      "scroll": {
        "enabled": true
      },
      "text": {
        "btnNextText": "<",
        "btnPrevText": ">"
      }
    },
    "toolbox": {
      "enabled": true,
      "calendarSwitch": {
        "enabled": false,
        "format": "MMMM"
      },
      "todayButton": {
        "enabled": true,
        "text": {
          "fa": "امروز",
          "en": "Today"
        }
      },
      "submitButton": {
        "enabled": true,
        "text": {
          "fa": "تایید",
          "en": "Submit"
        }
      },
      "text": {
        "btnToday": "امروز"
      }
    },
    "timePicker": {
      "enabled": false,
      "step": 1,
      "hour": {
        "enabled": false,
        "step": null
      },
      "minute": {
        "enabled": false,
        "step": null
      },
      "second": {
        "enabled": false,
        "step": null
      },
      "meridian": {
        "enabled": true
      }
    },
    "dayPicker": {
      "enabled": true,
      "titleFormat": "YYYY MMMM"
    },
    "monthPicker": {
      "enabled": true,
      "titleFormat": "YYYY"
    },
    "yearPicker": {
      "enabled": true,
      "titleFormat": "YYYY"
    },
    "responsive": true
  };

const calanderForeignConfig_return={
  initialValueType: 'gregorian',
    "inline": false,
    "format": "l",
    "viewMode": "day",
    "initialValue": false,
    "position": "auto",
    "altFormat": "unix",
    "altField": "#return_foreign_date",
    "onlyTimePicker": false,
    "onlySelectOnDate": false,
    "calendarType": "persian",
    "inputDelay": 800,
    "observer": true,
    "calendar": {
      "persian": {
        "locale": "fa",
        "showHint": true,
        "leapYearMode": "algorithmic"
      },
      "gregorian": {
        "locale": "en",
        "showHint": false
      }
    },
    "navigator": {
      "enabled": true,
      "scroll": {
        "enabled": true
      },
      "text": {
        "btnNextText": "<",
        "btnPrevText": ">"
      }
    },
    "toolbox": {
      "enabled": true,
      "calendarSwitch": {
        "enabled": false,
        "format": "MMMM"
      },
      "todayButton": {
        "enabled": true,
        "text": {
          "fa": "امروز",
          "en": "Today"
        }
      },
      "submitButton": {
        "enabled": true,
        "text": {
          "fa": "تایید",
          "en": "Submit"
        }
      },
      "text": {
        "btnToday": "امروز"
      }
    },
    "timePicker": {
      "enabled": false,
      "step": 1,
      "hour": {
        "enabled": false,
        "step": null
      },
      "minute": {
        "enabled": false,
        "step": null
      },
      "second": {
        "enabled": false,
        "step": null
      },
      "meridian": {
        "enabled": true
      }
    },
    "dayPicker": {
      "enabled": true,
      "titleFormat": "YYYY MMMM"
    },
    "monthPicker": {
      "enabled": true,
      "titleFormat": "YYYY"
    },
    "yearPicker": {
      "enabled": true,
      "titleFormat": "YYYY"
    },
    "responsive": true
  };

$("#arrived__time").persianDatepicker(calanderConfig);
$("#arrived_foreign_time").persianDatepicker(calanderForeignConfig);
$("#return__time").persianDatepicker(calanderConfig_return);
$("#return_foreign_time").persianDatepicker(calanderForeignConfig_return);


