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
    
});
let isMealFormClick = false;
mealForms.forEach(form => {
    form.style.display = "none"
})

mealPara.forEach(para => {
    para.addEventListener("click", () => {
    const number = para.classList[1]
    const form = document.getElementsByClassName(`f-${number}`)
    const spanArray  = document.querySelectorAll(`.p-${number} span`)
    const spanTime = spanArray[0].innerText
    const spanContent = spanArray[1].innerText

    if (!isMealFormClick) {
        form[0].style.display = "inline"
        const inputArray = document.querySelectorAll(`.f-${number} input`)
        inputArray[0].value = spanTime
        inputArray[1].value = spanContent
      
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
        // console.log(weightInput)
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
        const h3Spans = document.querySelectorAll(`.h3-${number} span`)
        const workName = h3Spans[0].innerText
        const time = h3Spans[1].innerText
        // console.log(workName, time)
        if (!isWorkoutClicked) {
            workouttH3Input[0].style.display = "inline-block";
            const formInput = document.querySelectorAll(`.f-work-${number} input`) 
            formInput[0].value = workName
            formInput[1].value = time
            // console.log(formInput)
            isWorkoutClicked = true;
        } else {
            workouttH3Input[0].style.display = "none";
            isWorkoutClicked = false;
        }
    });
});

const addMeal = document.querySelector(".profile-add-new p") 
const addMealForm = document.getElementsByClassName("add-form-meal")

addMealForm[0].style.display = "none"
let isAddMealForm = false

addMeal.addEventListener("click", () => {
    if (!isAddMealForm) {
        addMealForm[0].style.display = "inline"
         isAddMealForm = true
    } else {
        addMealForm[0].style.display = "none"
        isAddMealForm = false
    }
})

const weightDisplay = document.querySelectorAll(".profile-weight-display h3")
const addWeight = document.getElementsByClassName("profile-add-new-weight")

addWeight[0].style.display = "none"

// console.log(weightDisplay)
if(weightDisplay.length == 0) {
    addWeight[0].style.display = "block"   
}

const addNewWeight = document.querySelector(".profile-add-new-weight p")
const addNewWeightForm = document.querySelector(".add-form-weight")

addNewWeightForm.style.display = "none"
let isAddNewWeight = false

addNewWeight.addEventListener("click", () => {
 if (!isAddNewWeight) {
    addNewWeightForm.style.display = "inline"
    isAddNewWeight = true
 } else {
    addNewWeightForm.style.display = "none"
    isAddNewWeight = false
 }
})

const addNewWorkOut = document.querySelector(".profile-add-new-workout")

addNewWorkOut.style.display = "none"

if (workouttH3.length == 0) {
addNewWorkOut.style.display = "inline"
}

const addNewWorkoutP = document.querySelector(".profile-add-new-workout p")
const addNewWorkOutForm = document.querySelector(".add-form-workout")

addNewWorkOutForm.style.display = "none"
let isAddWorkout = false

addNewWorkoutP.addEventListener("click", () => {
    if (!isAddWorkout) {
        addNewWorkOutForm.style.display = "inline"
        isAddWorkout = true
    } else {
        addNewWorkOutForm.style.display = "none"
        isAddWorkout = false  
    }
})

const favMeals = document.querySelectorAll(".profile-fav-meals")
const addMealInput = document.getElementById("profile-meal-input")


favMeals.forEach(option => {
    option.addEventListener("change", () => {
        addMealInput.value = option.value
    
    })
});