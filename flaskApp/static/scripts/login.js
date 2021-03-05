const emailField = document.querySelector("#emailField");

emailField.addEventListener('blur', function() {
    isValidEmail = emailField.checkValidity();
    emailHelp = document.querySelector('.emailHelp')
    if(!isValidEmail) {
        emailHelp.style.display = "block";
    } else if(isValidEmail) {
        emailHelp.style.display = "none";
    }
});
