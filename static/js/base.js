const logoBtn = document.getElementById("logo-menu")
const listPopUp = document.getElementById("logo-popup")

var isOpen = false

logoBtn.addEventListener("click", () => {
    if (isOpen) {
        listPopUp.style.display = "none"
        isOpen = false 
    } else {
    listPopUp.style.display = "block"
    isOpen = true;
    }
})