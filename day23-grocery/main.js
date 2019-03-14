let database = firebase.database()
let users = []
let stores = []
let items = []
let myUserId = ''
let storeTitle = ''
let storeTextBox = document.getElementById('storeName')
let signInUser = document.getElementById('signInUser')
let signUpUser = document.getElementById('signUpUser')
let signOut = document.getElementById('signOut')

database.ref("stores")
.on("child_added",function(snapshot){
  let store = new Store(snapshot.key,snapshot.val().name,snapshot.val().userID)
  stores.push(store)
  displayStores()
})

database.ref("stores")
.on("child_removed",function(snapshot){
    stores = stores.filter((store) => {
      return store.key != snapshot.key
    })
    displayStores()
})

database.ref("items")
.on("child_added",function(snapshot){
  let item = new Item(snapshot.key,snapshot.val().userID,snapshot.val().store,snapshot.val().name,snapshot.val().qty)
  items.push(item)
  displayItems()
})

database.ref("items")
.on("child_removed",function(snapshot){
    items = items.filter((item) => {
      return item.key != snapshot.key
    })
    displayItems()
})

signOut.addEventListener('click',function(){
  firebase.auth().signOut().then(function() {
    document.getElementById("storesUL").style.display = "none";
    document.getElementById("itemBox").style.display = "none";
    document.getElementById("itemForm").style.display = "none";
    location.reload().then(function(){}).catch(function(error) {
  });
})
})

submitButton.addEventListener('click',function(){
      let storeName = storeTextBox.value
      let storesRef = database.ref("stores")
      let storeRef =storesRef.push({
        name: storeName,
        userID: checking()
      })
})

signUpUser.addEventListener('click',function() {
  let emailAddress = document.getElementById('emailAddress').value
  let password = document.getElementById('password').value
  userName(emailAddress,password)
  firebase.auth().createUserWithEmailAndPassword(emailAddress,password)
})

signInUser.addEventListener('click',function() {
  let emailAddress = document.getElementById('emailAddress').value
  let password = document.getElementById('password').value
  firebase.auth().signInWithEmailAndPassword(emailAddress,password)
  checking()
})

function userName(emailAddress,password) {
  let usersRef = database.ref("users")
  let userRef = usersRef.push({
    name: emailAddress,
    password: password
  })
}


startDispalyStores.addEventListener('click',function() {
  displayStores()
})

function displayStores() {
  document.getElementById("storesUL").style.display = "block";
  let storeLI = stores.map((store) => {
    if (store.userID == checking()) {
      return `<li>
          ${store.name}
          <button onclick="openForm('${store.name}')">Add Items</button>
          <button onclick="displayItems('${store.name}')">View</button>
          <button onclick="deleteStore('${store.key}','${store.name}')">Delete</button>
          </li>`
    } else {
    }
  })
  storesUL.innerHTML = storeLI.join("")
}

function displayItems(storeNameForItems) {
  let itemLI = items.map((item) => {
    document.getElementById("itemBox").style.display = "block";
    if (item.userID == checking() && item.store == storeNameForItems) {
      itemsTitle.innerHTML = item.store + "   " + `<button onclick="removeItemBox()">Close</button>`

      return `<li>
          ${item.name} - ${item.qty}
          <button onclick="deleteItem('${item.key}')">Delete</button>
          </li>`
    } else {
    }
  })

  itemsUL.innerHTML = itemLI.join("")
}

function removeItemBox() {
  document.getElementById("itemBox").style.display = "none";
}
function deleteStore(storeKey,storeNameForItems) {
      database.ref("stores").child(storeKey).remove()
      items.map((item) => {
          if (item.userID == checking() && item.store == storeNameForItems) {
            console.log("trying to delete");
            database.ref("items").child(item.key).remove()
          }
})
}

function deleteItem(key) {
      database.ref("items").child(key).remove()
      displayItems()
}

firebase.auth().createUserWithEmailAndPassword(email, password).catch(function(error) {
        // Handle Errors here.
        var errorCode = error.code;
        var errorMessage = error.message;
        // [START_EXCLUDE]
        if (errorCode == 'auth/weak-password') {
          alert('The password is too weak.');
        } else {
          alert(errorMessage);
        }
        console.log(error);


function sendEmailVerification() {
    firebase.auth().currentUser.sendEmailVerification().then(function() {
        alert('Email Verification Sent!');
        });
      }
    })

firebase.auth().signInWithEmailAndPassword(email, password).catch(function(error) {
  var errorCode = error.code;
  var errorMessage = error.message;
});

firebase.auth().onAuthStateChanged(function(user) {
 window.user = user; // user is undefined if no user signed in
});

function checking() {
var user = firebase.auth().currentUser;
var name, email, photoUrl, uid, emailVerified;
if (user != null) {
  name = user.displayName;
  email = user.email;
  photoUrl = user.photoURL;
  emailVerified = user.emailVerified;
  myUserId = user.uid;  // The user's ID, unique to the Firebase project. Do NOT use
                   // this value to authenticate with your backend server, if
                   // you have one. Use User.getToken() instead.
  return myUserId

} else {
}}

function openForm(storeNameForItems) {
  document.getElementById("itemForm").style.display = "block";
  storeTitle = storeNameForItems
}

function closeForm() {
  document.getElementById("itemForm").style.display = "none";
}

function logItems() {
  let item = document.getElementById('item').value
  let qty = document.getElementById('qty').value
  let itemsRef = database.ref("items")
  let itemRef = itemsRef.push({
    userID: myUserId,
    store: storeTitle,
    name: item,
    qty: qty
  })
  //document.getElementById("myForm").reset()
}
