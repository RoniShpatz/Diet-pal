const inputTime = document.querySelectorAll(".edit-time-meal")
const timeMeal = document.querySelectorAll(".meal-time")
const mealPara = document.querySelectorAll(".profile-meal-p")
const mealForms = document.querySelectorAll(".form-meal")


function formatTime(input) {
    let value = input.value.replace(/[^0-9]/g, '');
    if (value.length >= 3) {
        value = value.slice(0, 2) + ':' + value.slice(2, 4);
    }
    input.value = value;
}

inputTime.forEach(input => {
    input.addEventListener('input', () => formatTime(input));
    formatTime(input);
});
let isMealFormClick = false;
mealForms.forEach(form => {
    form.style.display = "none"
})

mealPara.forEach(para => {
    para.addEventListener("click", () => {
    const number = para.classList[1]
    const form = document.getElementsByClassName(`f-${number}`)
    if (!isMealFormClick) {
        form[0].style.display = "inline"
        isMealFormClick = true
    } else {
        form[0].style.display = "none"
        isMealFormClick = false
    }
    })
})

const waterH3 = document.querySelectorAll(".h3-water")
const waterInput = document.querySelectorAll(".water-form")

let isWaterClicked = false

waterInput.forEach(input => {
    input.style.display = "none"
})

waterH3.forEach(h3 => {
    h3.addEventListener("click", () => {
       if (!isWaterClicked ) {
        waterInput.forEach(input => {
            input.style.display = "inline-block"
        })
        isWaterClicked  = true
       } else {
        waterInput.forEach(input => {
            input.style.display = "none" 
        })
        isWaterClicked  = false
       }
    })
})

const weightH3 = document.querySelectorAll(".weight-h3")
const weightForm = document. querySelectorAll(".weight-from")

let isWeightClicked = false

weightForm.forEach(form => {
    form.style.display = "none"
})

weightH3.forEach(h3 => {
    h3.addEventListener("click", () => {
        let number = h3.classList[1]
        const weightInput = document.getElementsByClassName(`f-weight-${number}`)
        console.log(weightInput)
        if (!isWeightClicked) {
            weightInput[0].style.display = "inline-block"
            isWeightClicked = true
        } else {
            weightInput[0].style.display = "none"
            isWeightClicked = false 
        }
    })
})

const workouttH3 = document.querySelectorAll(".workout-h3")
const workoutForm = document. querySelectorAll(".form-workout")

workoutForm.forEach(form => {
    form.style.display = "none"
})
let isWorkoutClicked = false;

workouttH3.forEach(h3 => {
    h3.addEventListener("click", () => {
        let number = h3.classList[1];
        const workouttH3Input = document.getElementsByClassName(`f-work-${number}`);
       
        if (!isWorkoutClicked) {
            workouttH3Input[0].style.display = "inline-block";
            isWorkoutClicked = true;
        } else {
            workouttH3Input[0].style.display = "none";
            isWorkoutClicked = false;
        }
    });
});