const btnShow = document.getElementById("show-password");
const inputPassword = document.getElementById("password");
const inputPassword2 = document.getElementById("password-2");



function toggleShow(){
    if (inputPassword2) {
        if (inputPassword.type == "password") {
            inputPassword.type = "text";
            inputPassword2.type = "text";
            btnShow.style.filter = "saturate(5)"  
        } else {
            inputPassword.type = "password";
            inputPassword2.type = "password";
            btnShow.style.filter = "saturate(1)" 

        }
    } else {
        if (inputPassword.type == "password" ) {
            inputPassword.type = "text";
            btnShow.style.filter = "saturate(5)" 
        } else {
            inputPassword.type = "password";
            btnShow.style.filter = "saturate(1)" 
        }
        
    }
}


btnShow.addEventListener("click", toggleShow)