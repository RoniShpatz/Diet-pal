const weightForm = document.querySelector(".weight-form")
const submitBtn = document.querySelector("#weight-submit-btn")
const resetBtn = document.querySelector("#weight-reset-btn")
const inputNum = document.querySelector("#weight-num")
const checkWeight = document.querySelectorAll(".kg-lb")

const dropDownMeals = document.querySelector("#fav-meals")
const textMeal = document.querySelector("#iput-meal")
const resetMeal = document.querySelector("#meals-reset-btn")
const submitMeal = document.querySelector("#meals-submit-btn")
const timeNow = document.querySelector("#now-time")
const inputTimeDiv = document.querySelector(".input-time")
const changeTime = document.querySelector("#submit-watch")
const resetTime = document.querySelector("#reset-watch")
const inputTime = document.querySelector("#timeInput")
const mealForm = document.querySelector(".meals-form")
// weight script

function getSelectorValue() {
    let value = "";
    checkWeight.forEach(input => {
        if(input.checked) {
            value = input.value;
        }
    }); return value;
}

weightForm.addEventListener("submit", (e) => {
    let weight = inputNum.value
    let measurement = getSelectorValue()
    e.preventDefault()
    if (weight && measurement) {
        data = {
            weight: weight,
            measurement: measurement
        }
        dataJson = JSON.stringify(data)
        fetch("/weight", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: dataJson
        })
        .then((r)=> r.json()) 
        .then((data) => console.log(data))
       
    } else { 
        let para = document.createElement("p")
        para.classList.add("fill-in-form")
        para.innerText = "Fill in all form, and than press submit"
        weightForm.appendChild(para)
        setTimeout(() => {
            weightForm.removeChild(para)
            }, 2000)
        
    }
    inputNum.value = "";
}  )

// meals script
const isStart = false

dropDownMeals.addEventListener("change", () => {
    let mealChosen = dropDownMeals.value
    if (mealChosen != "add new meal") {
        textMeal.innerHTML = mealChosen
    }
})

resetMeal.addEventListener("click", () => {
    textMeal.innerHTML = ""
})

function getTime() {
    const now = new Date();
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0');
    const day = String(now.getDate()).padStart(2, '0');
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    return `${hours} : ${minutes}`;
}

function getDate(){
    const now = new Date();
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0');
    const day = String(now.getDate()).padStart(2, '0');
    return `${day}/ ${month} / ${year}`
}

function formatTime(input) {
    let value = input.value.replace(/[^0-9]/g, '');
    if (value.length >= 3) {
        value = value.slice(0, 2) + ':' + value.slice(2, 4);
    }
    input.value = value;
}

timeNow.innerHTML = getTime();
inputTimeDiv.style.display = "none"
let isWatchShow = false;

timeNow.addEventListener("click", () => {
    if (isWatchShow) {
        inputTimeDiv.style.display = "none"
        isWatchShow = false
    } else {
        inputTimeDiv.style.display = "inline-block";
        isWatchShow = true
    }
})

changeTime.addEventListener("click", () => {
    if (inputTime.value) {
        let newTime = inputTime.value
        timeNow.innerHTML = newTime
        inputTimeDiv.style.display = "none"
        isWatchShow = false
    }
})

resetTime.addEventListener("click", () => {
    timeNow.innerHTML = getTime()
    inputTime.value = "00:00"
    inputTimeDiv.style.display = "none"

})

submitMeal.addEventListener("click", (e) => {
    let newMeal = textMeal.value
    e.preventDefault()
    e.preventDefault()
    if (newMeal) {
        data = {
           meal : newMeal,
           time:  timeNow.innerHTML,
           date: getDate()
        }
        dataJson = JSON.stringify(data)
        console.log(dataJson)
        fetch("/meals", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: dataJson
        })
        .then((r)=> r.json()) 
        .then((data) => console.log(data))
       
    } else { 
        let para = document.createElement("p")
        para.classList.add("fill-in-form")
        para.innerText = "Fill in all form, and than press submit"
        mealForm .appendChild(para)
        setTimeout(() => {
            mealForm .removeChild(para)
            }, 2000)
        
    }
    textMeal.innerHTML = ""
}  )

// water script

const waterQuantity = document.querySelectorAll(".water-size")
const sbmitWater = document.querySelector("#add-water")
const waterForm = document.querySelector(".water-form")
// console.log(waterQuantity)

function getWaterValue() {
    let value = "";
    waterQuantity.forEach(input => {
        if(input.checked) {
            value = input.value;
        }
    }); return value;
}


sbmitWater.addEventListener("click", (e) => {
    let quantity = getWaterValue() 
    let time = getTime()
    e.preventDefault()
    if (time && quantity) {
        data = {
           quantity : quantity,
           time:  timeNow.innerHTML,
           date: getDate()
        }
        dataJson = JSON.stringify(data)
        console.log(dataJson)
        fetch("/water", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: dataJson
        })
        .then((r)=> r.json()) 
        .then((data) => console.log(data))
       
    } else { 
        let para = document.createElement("p")
        para.classList.add("fill-in-form")
        para.innerText = "Fill in all form, and than press submit"
        waterForm.appendChild(para)
        setTimeout(() => {
            waterForm.removeChild(para)
            }, 2000)
        
    }
}  )

// workout script

const chooseWorkout = document.querySelectorAll(".choose-workout")
const wokoutForm = document.querySelector(".wokout-form")
const costumInput = document.querySelector("#add-custom-workout")
const workoutSubmit = document.querySelector("#add-workout")

function getWokoutValue() {
    let value = "";
    chooseWorkout.forEach(input => {
        if(input.checked) {
            value = input.value;
        }
    }); return value;
}


workoutSubmit.addEventListener("click", (e) => {
    let workout = getWokoutValue()
    if (!workout) {
        workout = costumInput.value
    } 
    let time = getTime()
    e.preventDefault()
    if (time && workout) {
        data = {
           workout_type : workout,
           time:  timeNow.innerHTML,
           date: getDate()
        }
        dataJson = JSON.stringify(data)
        console.log(dataJson)
        fetch("/workout", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: dataJson
        })
        .then((r)=> r.json()) 
        .then((data) => console.log(data))
       
    } else { 
        let para = document.createElement("p")
        para.classList.add("fill-in-form")
        para.innerText = "Fill in all form, and than press submit"
        wokoutForm.appendChild(para)
        setTimeout(() => {
            wokoutForm.removeChild(para)
            }, 2000)
        
    }
    costumInput.value = ""
}  )