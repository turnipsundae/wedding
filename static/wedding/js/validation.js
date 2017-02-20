// Wait for the DOM to be ready
$(function() {
  // Initialize form validation on the registration form.
  // It has the name attribute "registration"
  $("form[name='rsvp_form']").validate({
    // Specify validation rules
    rules: {
      // The key name on the left side is the name attribute
      // of an input field. Validation rules are defined
      // on the right side
      first_name: "required",
      email: {
        required: true,
        // Specify that email should be validated
        // by the built-in "email" rule
        email: true
      },
      attendingRadios: {
        required: true,
      }
    },
    // Specify validation error messages
    messages: {
      firstname: "Please enter your firstname",      
      email: "Please enter a valid email address",
      attendingRadios: "Please let us know if you are attending"
    },
    
    highlight: function (element) {
            $(element).closest('.control-group').removeClass('success').addClass('error');
    },
    errorPlacement: function (error, element) {
      if (element.attr('type') == 'radio') {
        error.insertAfter(element.closest('radio'));
      } else {
        error.insertAfter(element);
      }
    },
    errorElement: 'label',
    errorClass: 'has-error',
    // Make sure the form is submitted to the destination defined
    // in the "action" attribute of the form when valid
    submitHandler: function(form) {
      form.submit();
    }
  });
});
