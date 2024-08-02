const divWeight = document.querySelectorAll(".week-weight")

divWeight.forEach(div => {
    const para = div.querySelector('p')
    if (para == null) {
        const paraNull = document.createElement('p')
        paraNull.innerText = "No Weigth Yet"
        div.appendChild(paraNull)
    }
})

const divWorkout = document.querySelectorAll(".week-workout")

divWorkout.forEach(div => {
    const para = div.querySelector('p')
    if (para == null) {
        const paraNull = document.createElement('p')
        paraNull.innerText = "No Workout Yet"
        div.appendChild(paraNull)
    }
})