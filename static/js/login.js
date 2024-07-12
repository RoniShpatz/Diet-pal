const btnShow = document.getElementById("show-password");
const inputPassword = document.getElementById("password");
const inputPassword2 = document.getElementById("password-2");



function toggleShow(){
    if (inputPassword2) {
        if (inputPassword.type == "password") {
            inputPassword.type = "text";
            inputPassword2.type = "text";  
        } else {
            inputPassword.type = "password";
            inputPassword2.type = "password";  
        }
    } else {
        if (inputPassword.type == "password" ) {
            inputPassword.type = "text";
        } else {
            inputPassword.type = "password";
        }
        
    }
}


btnShow.addEventListener("click", toggleShow)