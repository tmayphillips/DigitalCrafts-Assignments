var btnContainer = document.getElementById("myBtnContainer");
var btns = btnContainer.getElementsByClassName("btn");
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  })
}


let menuListUL = document.getElementById('menuListUL')
startersBtn = document.getElementById('starters')
entreesBtn = document.getElementById('entrees')
dessertsBtn = document.getElementById('desserts')
allBtn = document.getElementById('all')


let menuItem = dishes.map(function(item) {
  return `<li class="row">
          <img class = "col" src = '${item.imageURL}'></img>
          <div class = "col-6">
          <h3>${item.title}</h3>
          <p>${item.description}</p>
          </div>
          <p class = "col">${item.price}</p>
          </li>`
})
menuListUL.innerHTML = menuItem.join('')


startersBtn.addEventListener('click',() => {
let starters = dishes.filter(item => item.course === 'Starters')
let menuItem = starters.map(function(item) {
  return `<li class="row">
          <img class = "col" src = '${item.imageURL}'></img>
          <div class = "col-6">
          <h3>${item.title}</h3>
          <p>${item.description}</p>
          </div>
          <p class = "col">${item.price}</p>
          </li>`

})
menuListUL.innerHTML = menuItem.join('')
})

entreesBtn.addEventListener('click',() => {
let entrees = dishes.filter(item => item.course === 'Entrees')
let menuItem = entrees.map(function(item) {
  return `<li class="row">
          <img class = "col" src = '${item.imageURL}'></img>
          <div class = "col-6">
          <h3>${item.title}</h3>
          <p>${item.description}</p>
          </div>
          <p class = "col">${item.price}</p>
          </li>`

})
menuListUL.innerHTML = menuItem.join('')
})

dessertsBtn.addEventListener('click',() => {
let desserts = dishes.filter(item => item.course === 'Desserts')
let menuItem = desserts.map(function(item) {
  return `<li class="row">
          <img class = "col" src = '${item.imageURL}'></img>
          <div class = "col-6">
          <h3>${item.title}</h3>
          <p>${item.description}</p>
          </div>
          <p class = "col">${item.price}</p>
          </li>`

})
menuListUL.innerHTML = menuItem.join('')
})

allBtn.addEventListener('click',() => {
let menuItem = dishes.map(function(item) {
  return `<li class="row">
          <img class = "col" src = '${item.imageURL}'></img>
          <div class = "col-6">
          <h3>${item.title}</h3>
          <p>${item.description}</p>
          </div>
          <p class = "col">${item.price}</p>
          </li>`
})
menuListUL.innerHTML = menuItem.join('')
})
