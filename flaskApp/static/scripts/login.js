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

function showPwd() {
    var pwdfield = document.getElementById("pwdField")
    var icon = document.getElementById("icon")
    if(pwdfield.type === "password") {
        icon.className = "";
        icon.className = "fas fa-eye icon";
        pwdfield.type = "text";
    } else {
        icon.className = "";
        icon.className = "fas fa-eye-slash icon";
        pwdfield.type = "password";
    }
}
