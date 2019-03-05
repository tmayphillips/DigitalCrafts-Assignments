let btnAddTask = document.getElementById("btnAddTask")


btnAddTask.addEventListener('click', function() {

  let taskList = document.getElementById("tasks")
  let taskInput = document.getElementById("addTask").value
  let liElement = document.createElement("li")

  liElement.className = "list-group-item list-group-item-info d-flex justify-content-between align-items-center"
  liElement.id = taskInput
  let inputElement = document.createElement("input")
  inputElement.type = "checkbox"
  inputElement.className = "slider round"


  liElement.appendChild(inputElement)
  taskList.appendChild(liElement)
  liElement.appendChild(document.createTextNode(taskInput))
  let spanElement = document.createElement("span")
  liElement.appendChild(spanElement)
  let spanButton = spanElement.appendChild(document.createElement("button"))
  spanButton.appendChild(document.createTextNode("Remove"))
  spanButton.appendChild(document.createElement("type"))
  spanButton.type = "button"
  spanButton.className = "btn btn-danger"
  spanButton.addEventListener('click', function () {
  	let span = this.parentNode;
    let li = span.parentNode;
    let ul = li.parentNode
    ul.removeChild(li);
  })

inputElement.addEventListener("change", function () {
    if (this.checked) {
    let remove = this.parentNode
    remove.parentNode.removeChild(remove)
    let completed = document.getElementById("completedTasks").appendChild(remove)
    completed.className = "list-group-item list-group-item-danger d-flex justify-content-between align-items-center"
  } else {
    let remove = this.parentNode
    remove.parentNode.removeChild(remove)
    let completed = document.getElementById("tasks").appendChild(remove)
    completed.className = "list-group-item list-group-item-info d-flex justify-content-between align-items-center"
  }
})
})
