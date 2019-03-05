let photoList = document.getElementById("photoList")
let btnAddPhoto = document.getElementById("btnAddPhoto")

//let photos = ["1.png","2.png","3.png"]
//let index = 0


btnAddPhoto.addEventListener('click', function() {
// create image html element
  let imgElement = document.createElement("img")
  let photoName = photoNameTextBox.value
  //imgElement.src = photos[index]
  imgElement.src = photoName
  imgElement.className = "photo"
  let deleteBtn = document.createElement("button")
  deleteBtn.innerHTML = "Remove"

let photoDiv = document.createElement("div")
photoDiv.appendChild(imgElement)
photoDiv.appendChild(deleteBtn)

photoList.appendChild(photoDiv)

  //index += 1



})
