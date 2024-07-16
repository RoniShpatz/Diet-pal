const mealList = document.querySelectorAll(".meal-item p span")
const mealBottonsList =  document.querySelectorAll(".meal-item span")
const inputMealList = document.querySelectorAll(".meal-item input")
const spanSubmitMeal = document.querySelectorAll(".span-submit")
const spanDeleteMeal = document.querySelectorAll(".span-delete")
const submitMeals = document.querySelector("#submit-meal")
const inputNewNameMeal = document.querySelector("#new-meal-name")
const iputNeaMealContent = document.querySelector("#nea-meal-content")
const formAddMeal = document.querySelector(".edit-meal")


isClicked = false
let meals = []


inputMealList.forEach(input => {
    input.style.display = "none"
})

spanSubmitMeal.forEach(span => {
    span.style.display = "none"
})

spanDeleteMeal.forEach(span => {
    span.style.display = "none"
})


mealList.forEach (meal => {
    meal.addEventListener("click", () => {
        const mealClassName = meal.className
        const spanMeal = document.querySelectorAll(`.meal-item p .${mealClassName}`)
        const inputName = document.querySelector(`.meal-name-${mealClassName}`)
        const inputContent = document.querySelector(`.meal-content-${mealClassName}`)
        const submitSpan = document.querySelector(`.meal-item .span-submit.${mealClassName}`)
        const deleteSpan = document.querySelector(`.meal-item .span-delete.${mealClassName}`)
        inputName.value = spanMeal[0].innerText
        inputContent.value = spanMeal[1].innerText
        if (!isClicked) {
            submitSpan.style.display = "inline-block"
            deleteSpan.style.display = "inline-block"
            inputName.style.display = "inline-block"
            inputContent.style.display ="inline-block"
            isClicked = true;
        } else {
            submitSpan.style.display = "none"
            deleteSpan.style.display = "none"
            inputName.style.display = "none"
            inputContent.style.display ="none"
            isClicked = false
        }
        submitSpan.addEventListener("click", () => {
            if (inputName.value && inputContent.value) {
                spanMeal[0].innerText = inputName.value
                spanMeal[1].innerText = inputContent.value
                submitSpan.style.display = "none"
                deleteSpan.style.display = "none"
                inputName.style.display = "none"
                inputContent.style.display ="none"
                isClicked = false
            }
        })
        deleteSpan.addEventListener("click", () => {
            const listItemMeal = document.querySelector(`ul .meal-item.${mealClassName}`)
            listItemMeal.remove()
            submitSpan.style.display = "none"
            deleteSpan.style.display = "none"
            inputName.style.display = "none"
            inputContent.style.display ="none"
            isClicked = false
        })
    })
})

function mealsObjects(arry) {
    let newMeals = []
   for (let i = 0; i < arry.length ; i+= 2) {
    let name = arry[i].innerText
    let content = arry[i + 1].innerText
    let newMeal = {name: name, content: content}
    newMeals.push(newMeal)
   } 
   return newMeals
}



submitMeals.addEventListener("click", (e) => {
    e.preventDefault()
    let newNameMeal = inputNewNameMeal.value
    let newContentMeal = iputNeaMealContent.value
    let newMeal = {name: newNameMeal, content: newContentMeal}
    
    meals.push(newMeal)
    // console.log(meals)
    if (newContentMeal && newContentMeal) {
        data = meals;
        dataJson = JSON.stringify(data);
        // console.log(dataJson);
        fetch("/meal_edited", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: dataJson
        })
        .then((r) => r.json())
        .then((data) => {
            console.log(data)
            meals = data
        })
        .catch((error) => console.error('Error:', error));
    } else {
        let para = document.createElement("p")
        para.classList.add("fill-in-form")
        para.innerText = "Fill in all form, and than press submit"
        formAddMeal.appendChild(para)
        setTimeout(() => {
            formAddMeal.removeChild(para)
            }, 2000)
    }
    inputNewNameMeal.value = ""
    iputNeaMealContent.value =""
    
})





