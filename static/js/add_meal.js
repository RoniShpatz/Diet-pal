let meals = [];


document.addEventListener("DOMContentLoaded", () => {
    meals = meals_favorites;  
    createMealList()
});

function updateList(name, content, count) {
    mealContainer.innerHTML = '';
    if (count < 0 || count >= meals.length){
        return
    } else {
        const oldKey = Object.keys(meals[count])[0];
        if (oldKey) {
            delete meals[count][oldKey]
        }
        meals[count][name] = content;
    }
}

function deleteItemFormList(count) {
    mealContainer.innerHTML = '';
    if (count < 0 || count >= meals.length){
        return
    
    } else {
        meals.splice(count, 1);
    }
}

function updateFlask(arry) {
    const updateMeal = arry
    if (updateMeal) {
        data = updateMeal
        dataJson = JSON.stringify(data)
        console.log(dataJson)
        fetch("/meal_edited", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: dataJson
        })
        .then((r) => r.json())
        .then((data) => console.log(data))
    } else {
        console.log("no update meal")
    }
}


const mealContainer = document.querySelector("#list-of-melas");

function createItemMeal(key, content) {
    const listItem = document.createElement("li");
    const paraNameItem = document.createElement("p");
    paraNameItem.innerText = key + ":";
    paraNameItem.classList.add("para-name")

    const inputName = document.createElement("input")
    inputName.classList.add("input-name")
    inputName.value = key
    

    const contentParaItem = document.createElement("p");
    contentParaItem.innerText = content;
    contentParaItem.classList.add("para-content")

    const inputcontent = document.createElement("input");
    inputcontent.classList.add("input-content")
    inputcontent.value = content

    const divSpan = document.createElement("div")
    divSpan.classList.add("spans-div")

    const deleteSpanItem = document.createElement("span");
    deleteSpanItem.innerHTML = "&#10005;";
    deleteSpanItem.classList.add("delet-item") 

    const submitSpanItem = document.createElement("span");
    submitSpanItem.innerHTML = "&#10004;";
    submitSpanItem.classList.add("submit-item")

    divSpan.appendChild(submitSpanItem)
    divSpan.appendChild(deleteSpanItem)

    listItem.appendChild(paraNameItem);
    listItem.appendChild(contentParaItem);
    listItem.appendChild(inputName );
    listItem.appendChild(inputcontent );
    listItem.appendChild(divSpan);
    
    return listItem;
}

let isInputDisplay = false

function createMealList() {
    let count = 0
    meals.forEach(meal=> {
        for (let key in meal) {
            const newlistItem = createItemMeal(key, meal[key]);
            newlistItem.classList.add("item");
            newlistItem.classList.add(`list-${count}`)
            mealContainer.appendChild(newlistItem);
        }
       
        const inputName = document.querySelector(`.list-${count} .input-name`)
        const inputContent =document.querySelector(`.list-${count} .input-content`)
        const deleteItem = document.querySelector(`.list-${count} .delet-item`)
        const submitItem = document.querySelector(`.list-${count} .submit-item`)
        const paraName = document.querySelector(`.list-${count} .para-name`)
        const paraContent = document.querySelector(`.list-${count} .para-content`)
        const number = count
        inputName.style.display= "none"
        inputContent.style.display= "none"
        if(paraName) {
            paraName.addEventListener("click", () => {
                if (!isInputDisplay) {
                    inputName.style.display= "inline-block"
                    inputContent.style.display= "inline-block"
                    isInputDisplay = true;
                } else {
                    inputName.style.display= "none"
                    inputContent.style.display= "none"
                    isInputDisplay = false
                }
            })
        }
        if (paraContent) {
            paraContent.addEventListener("click", () => {
                if (!isInputDisplay) {
                    inputName.style.display= "inline-block"
                    inputContent.style.display= "inline-block"
                    isInputDisplay = true;
                } else {
                    inputName.style.display= "none"
                    inputContent.style.display= "none"
                    isInputDisplay = false
                }  
            })
        }
        if (deleteItem) {
            deleteItem.addEventListener("click", () => {
                deleteItemFormList(number)
                createMealList()
                updateFlask(meals)
                console.log(meals);
            })
        }
        if (submitItem) {
            submitItem.addEventListener("click", () => {
                console.log(number)
                if (inputName.value && inputContent.value) {
                    let name = inputName.value;
                    let content = inputContent.value;
                    updateList(name, content, number);
                    createMealList()
                    updateFlask(meals)
                    console.log(meals);
                }
            })
        }
        count += 1   
    });
}

const addBtn = document.querySelector("#submit-meal")
const inputNewName = document.querySelector("#new-meal-name")
const inputNewContent = document.querySelector("#input-new-content")
const resetBtn = document.querySelector("#reset-mael")

addBtn.addEventListener("click", (e) => {
    e.preventDefault()
    const name = inputNewName.value
    const content = inputNewContent.value
    const newMeal = {}
    newMeal[name] = content
    if (name && content) {
        meals.push(newMeal)
        mealContainer.innerHTML = '';
        createMealList()
        updateFlask(meals)
        inputNewName.value = ""
        inputNewContent.value = ""
    } else {
        let para = document.createElement("p")
        para.classList.add("fill-in-form")
        para.innerText = "Fill in all form, and than press submit"
        const divContainer = document.querySelector(".edit-meal-div")
        divContainer.appendChild(para)
        setTimeout(() => {
            divContainer.removeChild(para)
            }, 2000)
    }
    
    console.log(meals)
})

resetBtn.addEventListener("click", (e) => {
    e.preventDefault()
        inputNewName.value = ""
        inputNewContent.value = ""
})

