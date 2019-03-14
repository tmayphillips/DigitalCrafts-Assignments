let database = firebase.database()
let users = []
let stores = []
let myUserId = ""

let storeTextBox = document.getElementById('storeName')
let signInUser = document.getElementById('signInUser')
let signUpUser = document.getElementById('signUpUser')

database.ref("stores")
.on("child_added",function(snapshot){
  let store = new Store(snapshot.key,snapshot.val().name)
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

submitButton.addEventListener('click',function(){
      let storeName = storeTextBox.value
      let storesRef = database.ref("stores")
      let storeRef =storesRef.push({
        name: storeName
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
  myUserId = firebase.auth().currentUser.uid;
  console.log(myUserId);
})

function userName(emailAddress,password) {
  let usersRef = database.ref("users")
  let userRef = usersRef.push({
    name: emailAddress,
    password: password
  })
  userRef.child("stores").set({
    any: ''
  })
}

firebase.auth().signOut().then(function() {
  // Sign-out successful.
}).catch(function(error) {
  // An error happened.
});

function displayStores() {
  let storeLI = stores.map((store) => {
    return `<li>
        ${store.name}
        <button onclick="deleteStore('${store.key}')">Delete</button>
        </li>`
  })
  storesUL.innerHTML = storeLI.join("")
}

function deleteStore(key) {
  database.ref("stores").child(key).remove()
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
        // [END_EXCLUDE]


        function sendEmailVerification() {
        // [START sendemailverification]
        firebase.auth().currentUser.sendEmailVerification().then(function() {
          // Email Verification sent!
          // [START_EXCLUDE]
          alert('Email Verification Sent!');
          // [END_EXCLUDE]
        });
        // [END sendemailverification]
      }
    })

    firebase.auth().signInWithEmailAndPassword(email, password).catch(function(error) {
  // Handle Errors here.
  var errorCode = error.code;
  var errorMessage = error.message;
  // ...
});
