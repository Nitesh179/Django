import { states } from './state.js'


var progressbar = 25;

// image showing function
let imgfile = document.getElementById('input-file');
$('#input-file').change(function () {
    $('#pic').attr('src', URL.createObjectURL(imgfile.files[0]));
})



// --------------------------------------regx methods -------------------------------------------

$.validator.addMethod("email_regx", function (value, element) {
    return this.optional(element) || /^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.[a-zA-Z.]{2,5}$/i.test(value);
}, "Please enter a valid email address.");

$.validator.addMethod("name_regx", function (value, element) {
    return this.optional(element) || /^[a-zA-Z ]*$/i.test(value);
}, "Please enter a valid Name.");

$.validator.addMethod("dob_regx", function (value, element) {
    return this.optional(element) || /^(2\d{2}[1-9]|2\d[1-9]0|[3-9]\d{3}|\d{2,}\d{3})\-(0\d|1[0-2]|[1-9])\-([0-2]\d|3[0-1]|[1-9])$/i.test(value);
}, "birth year son shoud be above 2000.");

$.validator.addMethod("contact_regx", function (value, element) {
    return this.optional(element) || /^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$/.test(value);
}, "phone number shoud be 10 digits");



var v = jQuery("#mainForm").validate({
    rules: {
        //  first page
        name: {
            required: true,
            minlength: 2,
            name_regx: true
        },
        dob: {
            required: true,
            dob_regx: true
        },
        email: {
            required: true,
            email_regx: true
        },
        contact: {
            contact_regx: true,
            required: true
        },
        maritialstatus: {
            required: true
        },
        gender: {
            required: true
        },
        //  second page

        state: {
            required: true,
        },
        city: {
            required: true,
        },
        zip: {
            required: true,
        },
        address: {
            required: true
        },
        //  third page

        bankname: {
            required: true,
            name_regx: true
        },
        branch: {
            required: true,
            name_regx: true
        },
        accountno: {
            required: true,
            minlength: 12
        },
        ifsc: {
            required: true
        },
        feedback: {
            required: true
        }
    },

    messages: {}

});

//   next buttons 

$("#next1").click(function () {
    if (v.form()) {
        progressbar += 25
        $(".frm").hide("fast");
        $("#sf2").show("slow");
        //   $('#form1').attr('style', 'display:none')
        //   $('#form2').attr('style', 'display:block')
        $('#progress').attr('style', `width:${progressbar}%`)
    }
});


$("#next2").click(function () {
    if (v.form()) {
        progressbar += 25
        $(".frm").hide("fast");
        $("#sf3").show("slow");
        $('#progress').attr('style', `width:${progressbar}%`)
    }
});
$("#next3").click(function () {

    if (v.form()) {
        progressbar += 25
        $(".frm").hide("fast");
        $("#sf4").show("slow");
        $('#progress').attr('style', `width:${progressbar}%`)
    }
});

//   Back buttons

$('#back1').click(function () {
    progressbar -= 25
    $(".frm").hide("fast");
    $("#sf1").show("slow");
    $('#progress').attr('style', `width:${progressbar}%`)
});

$('#back2').click(function () {
    progressbar -= 25
    $(".frm").hide("fast");
    $("#sf2").show("slow");
    $('#progress').attr('style', `width:${progressbar}%`)
});

$('#back3').click(function () {
    progressbar -= 25
    $(".frm").hide("fast");
    $("#sf3").show("slow");
    $('#progress').attr('style', `width:${progressbar}%`)
});

$('#perview,#percheck').click(function () {
    $(".m-form").hide("fast");
    $(".m-page").show("slow");
    getCookie();
})

$('#previewback').click(function () {
    $(".m-form").show("fast");
    $(".m-page").hide("slow");
})


// state and city choice : 

Object.keys(states).map((data, index) => {
    // return <option value={date} key={index}>{data}</option>
    $('#statechoice').append(new Option(data, data));
    // console.log(states.Assam)
})
// $('#statechoice').find(":selected").val();
$("#statechoice").change(function () {
    $("#citychoice").empty();
    var choice = ""
    choice = $(this).val()

    var ct = Object.entries(states).filter(data => {
        return data[0] == choice
    })

    //  console.log(ct[0][1])
    ct[0][1].map((city, index) => {
        $('#citychoice').append(new Option(city, city));
    })
})


 