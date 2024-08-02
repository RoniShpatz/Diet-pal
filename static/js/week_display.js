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


const dayForms = document.querySelectorAll(".week-day-form")

const dayToday = new Date();
let day = dayToday.getDate();
let month = dayToday.getMonth() + 1;
let year = dayToday.getFullYear();

day = day < 10 ? `0${day}`: day;
month = month < 10 ? `0${month}`: month;

let currentDate = `${day}/ ${month}/ ${year}`

dayForms.forEach(form => {
    if (form[1].innerText == currentDate) {
       form[0].style.color = "#81B214"
       form[1].style.color = "#81B214"
      form.style.border = "dotted 4px #FC0"
      form.style.borderRadius = "10px"
      form[0].style.textShadow = "2px 4px 3px rgba(0,0,0,0.3);";
    }
})