$(document).ready(function () {


    var stateName, cityId;


//   var regex = /^(.+?)(\d+)$/i;
//   var cloneIndex = $("#personForm").length;

// function clone(){
//   console.log("inBox");
//     $("#personForm").clone()
//         .appendTo("#mainContainer")
//         .attr("id", "personForm" +  cloneIndex)
//         .find("*")
//         .each(function() {
//             var id = this.id || "";
//             var match = id.match(regex) || [];
//             if (match.length == 3) {
//                 this.id = match[1] + (cloneIndex);
//             }
//         })
//         // .on('click', 'button.clone', clone)
//         .on('click', 'removeMember', remove);
//     cloneIndex++;
// }

// function remove(){
//     $(this).parents(".needs-validation").remove();
// }

// $("#addMember").on("click", clone);


    // $("#addMember").on("click",function(){
    //   console.log("inBox");
    //   var clone = $("#personForm").clone().appendTo("#mainContainer").attr("id","personForm" + numPerson);
    // });

    // $("#removeMember").on("click",function(){
    //   console.log("removeBox");
    //   $(this).parentsUntil("form").remove()
    // });
    //
    $(".State").select2(
        {
            theme: 'bootstrap4',
            placeholder: 'State',
            width: 'style',
        }
    );
    // $(".City").select2(
    //     {
    //         theme: 'bootstrap4',
    //         tags: true,
    //         placeholder: 'City',
    //         width: 'style',
    //     }
    // );
    $("#marudharMe").select2(
        {
            theme: 'bootstrap4',
            placeholder: 'Marudhar Me',
            width: 'style',
        }
    );
    $("#personBloodGroup").select2(
        {
            theme: 'bootstrap4',
            placeholder: 'Blood Group',
            width: 'style',
        }
    );
    $("#personGender").select2(
        {
            theme: 'bootstrap4',
            placeholder: 'Sex',
            width: 'style',
        }
    );
    $('#qualificationClass').prepend('<option value="None">None</option>').select2(
        {
            theme: 'bootstrap4',
            placeholder: 'Class',
            width: 'style',
            allowClear: true
        }
    )
    $('#qualificationType').prepend('<option value="None">None</option>').select2(
        {
            theme: 'bootstrap4',
            placeholder: 'Qualification',
            width: 'style',
            allowClear: true
        }
    )
    $('#occupation').select2(
        {
            theme: 'bootstrap4',
            placeholder: 'Occupation',
            width: 'style',
            allowClear: true
        }
    )
    $('#maritalStatus').select2(
        {
            theme: 'bootstrap4',
            placeholder: 'Marital Status',
            width: 'style',
        }
    )


    $("#addMember").on("click", function () {
        if ($("#personForm").hasClass("submitted")) {
            console.log("Ready to add a new person");
        }
    });


    $('#qualificationType').on('change', function () {
        var selection = $(this).val();
        console.log(selection)
        switch (selection) {
            case "None":
                $("#qualificationClass").prop("disabled", true);
                $("#qualificationClass").val("").trigger('change');
                $("#qualificationYear").prop("disabled", true);
                $("#qualificationYear").val('');
                $("#qualificationName").prop("disabled", true);
                $("#qualificationName").val('');
                $("#qualificationState").prop("disabled", true);
                $("#qualificationState").val('').trigger('change');
                $("#qualificationCity").prop("disabled", true);
                $("#qualificationCity").val('');
                break;

            default:
                $("#qualificationClass").prop("disabled", false);
                $("#qualificationYear").prop("disabled", false);
                $("#qualificationName").prop("disabled", false);
                $("#qualificationState").prop("disabled", false);
                $("#qualificationCity").prop("disabled", false);
        }
    });


    $('#occupation').on('change', function () {
        var selection = $(this).val();
        switch (selection) {
            case "Student":
                $("#occupationPhoneNumber").prop("disabled", true);
                $("#occupationPhoneNumber").val('');
                $("#occupationName").prop("disabled", true);
                $("#occupationName").val('');
                $("#occupationType").prop("disabled", true);
                $("#occupationType").val('');
                $("#occupationAddress").prop("disabled", true);
                $("#occupationAddress").val('');
                $("#officeState").prop("disabled", true);
                $("#officeState").val('').trigger('change');
                $("#officeCity").prop("disabled", true);
                $("#officeCity").val('');
                $("#officeArea").prop("disabled", true);
                $("#officeArea").val('');
                $("#officePincode").prop("disabled", true);
                $("#officePincode").val('');
                break;

            case "Self Employee":
                $("#occupationPhoneNumber").prop("disabled", true);
                $("#occupationPhoneNumber").val('');
                $("#occupationName").prop("disabled", true);
                $("#occupationName").val('');
                $("#occupationType").prop("disabled", true);
                $("#occupationType").val('');
                $("#occupationAddress").prop("disabled", true);
                $("#occupationAddress").val('');
                $("#officeState").prop("disabled", true);
                $("#officeState").val('').trigger('change');
                $("#officeCity").prop("disabled", true);
                $("#officeCity").val('');
                $("#officeArea").prop("disabled", true);
                $("#officeArea").val('');
                $("#officePincode").prop("disabled", true);
                $("#officePincode").val('');
                break;

            // case "Professional":
            //     console.log("Professional");
            //     $("#occupationNameDiv").removeClass("col-sm-9 col-md-9 col-lg-9 col-xl-9")
            //     $("#occupationNameDiv").addClass("col-sm-6 col-md-6 col-lg-6 col-xl-6")
            //     $('#occupationType').prop("hidden", false);
            //     break;

            default:
                console.log("default");
                $("#occupationPhoneNumber").prop("disabled", false);
                $("#occupationName").prop("disabled", false);
                $("#occupationType").prop("disabled", false);
                $("#occupationAddress").prop("disabled", false);
                $("#officeState").prop("disabled", false);
                $("#officeCity").prop("disabled", false);
                $("#officePincode").prop("disabled", false);
                $("#officeArea").prop("disabled", false);
            // $("#occupationNameDiv").removeClass("col-sm-6 col-md-6 col-lg-6 col-xl-6")
            // $("#occupationNameDiv").addClass("col-sm-9 col-md-9 col-lg-9 col-xl-9")
            // $('#occupationType').prop("hidden", true);
        }
    });

    var forms = document.querySelectorAll('.needs-validation');
    Array.prototype.slice.call(forms)
        .forEach(function (form) {
            form.addEventListener('submit', function (event) {
                if (!form.checkValidity()) {
                    event.preventDefault()
                    event.stopPropagation()
                }
                form.classList.add('was-validated')
            }, false)
        });


    $('#bod').on('focus', function () {
        $(this).attr({type: 'date'});
    })

    $("#qualificationType").change(function () {
        const url = $("#personForm").attr("data-qualification-url");
        const TypeId = $(this).val();
        if (TypeId !== "None") {
            $.ajax({
                url: url,
                data: {
                    'TypeId': TypeId
                },
                success: function (data) {
                    $("#qualificationClass").html(data);
                    // $("#homeCity").prepend("<option value='' hidden selected='selected'>City</option>");
                }
            });
        }
    });



    // $("#homeCity").change(function () {
    //     const url = $("#familyForm").attr("data-area-url");
    //     cityId = $(this).val();
    //     stateName = $("#homeState option:selected").html()
    //     console.log(stateName)
    //     console.log(url)
    //     $.ajax({
    //         url: url,
    //         data: {
    //             'state_id': stateName,
    //             'cityId': cityId
    //         },
    //     });
    // });


});


