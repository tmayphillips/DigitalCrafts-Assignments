let items = ''

function palindrome() {
  var word = document.getElementById("palindrome").elements[0].value
  if (word.toLowerCase() == word.toLowerCase().split('').reverse().join('')) {
  var result = "a palindrome!"
} else {
  var result = "not palindrome!"
}
document.getElementById('palindrome_output').innerHTML = word + " is " + result
}

function duplicates() {

var textarea = document.getElementById('duplicates').value;
var arr = textarea.split('\n');

let x = (arr) => arr.filter((v,i) => arr.indexOf(v) === i);
results = x(arr);

document.getElementById("duplicates_output").innerHTML = results;
items = results;
}

function itemIncluded() {
  var text = document.getElementById("itemIncluded").elements[0].value;
  var arrayIncludes = (items.indexOf(text) > -1)
  if (arrayIncludes == true)  {
    document.getElementById("itemIncluded_output").innerHTML = "Yes it is";
  } else if (arrayIncludes == false){
    document.getElementById("itemIncluded_output").innerHTML = "No it is not";
}
}

function largestSmallest() {
  var textarea = document.getElementById('largestSmallest').value;
  var arr = textarea.split('\n')
  let maxNumber = arr[0]
  let minNumber = arr[0]
  for(let index = 0; index < arr.length; index++) {
    console.log(arr[index])
    if (parseFloat(arr[index]) > maxNumber) {
      maxNumber = parseFloat(arr[index])
    }
    if (parseFloat(arr[index]) < minNumber) {
      minNumber = parseFloat(arr[index])
    }
  }
  document.getElementById("smallest_output").innerHTML = minNumber + " is the smallest."
  document.getElementById("largest_output").innerHTML = maxNumber + " is the largest."
}

function fizzBuzz() {
  var number = document.getElementById("fizzBuzz").elements[0].value
  if (number % 3 == 0 && number % 5 == 0) {
    document.getElementById("fizzBuzz_output").innerHTML = "FIZZ BUZZ"
  } else if (number % 3 == 0) {
    document.getElementById("fizzBuzz_output").innerHTML = "FIZZ"
  } else if (number % 5 == 0) {
    document.getElementById("fizzBuzz_output").innerHTML = "BUZZ"
  } else {
    document.getElementById("fizzBuzz_output").innerHTML = "Maybe next time"
  }
}

function evenOdd() {
  var number = document.getElementById("evenOdd").elements[0].value
  if (number % 2 == 0) {
    document.getElementById("evenOdd_output").innerHTML = "Even"
  } else {
    document.getElementById("evenOdd_output").innerHTML = "Odd"
  }
  }

function ascendDescend() {
    var textarea = document.getElementById('ascendDescend').value;
    var arr = textarea.split('\n')
    arr.sort(function(a, b){return b-a});
    document.getElementById("descend_output").innerHTML = arr
    arr.sort(function(a, b){return a-b});
    document.getElementById("ascend_output").innerHTML = arr
      }


function BankAccount () {
  this.userName = ""
  this.firstName = ""
  this.middleName = ""
  this.lastName = ""
  this.accountType = ""
  this.balance = ""
  this.status = ""
}

let users = []
function Open(){
//  var userName
  //document.getElementById("firstName").value = userName
  let userName = new BankAccount()
  userName.firstName = document.getElementById("firstName").value
  userName.middleName = document.getElementById("middleName").value
  userName.lastName = document.getElementById("lastName").value
  userName.accountType = document.getElementById("accountType").value
  userName.userName = userName.firstName + userName.middleName + userName.lastName + userName.accountType

  userName.balance = parseFloat(document.getElementById("openDeposit").value)

if (users.length < 1){
  users.push(userName)
  console.log("creating user");
} else {
  found = false
  for(let i = 0; i < users.length; i++) {
    console.log("starting loop");
    if (users[i].userName == userName.userName) {
      console.log("already exists")
      found = true
  }
}
  if(found == false && userName.balance > 100) {
    users.push(userName)
    console.log("creating user");
  } // need else statement
}
  console.log(userName);
  console.log(users);
}


 function Transfer() {
  let firstName = document.getElementById("firstName").value
  let middleName = document.getElementById("middleName").value
  let lastName = document.getElementById("lastName").value
  let accountTypeFrom = document.getElementById("transferFrom").value
  let accountTypeTo = document.getElementById("transferTo").value
  let transferAmount = document.getElementById("transferAmount").value
  let userNameFrom = firstName + middleName + lastName + accountTypeFrom
  let userNameTo = firstName + middleName + lastName + accountTypeTo

  let foundFrom = false
  let foundTo = false
    for(let i = 0; i < users.length; i++) {
      console.log("starting loop");
      if (users[i].userName == userNameFrom) {
        console.log("Found From");
        foundFrom = true
    }
      if (users[i].userName == userNameTo) {
        console.log("Found To");
        foundTo = true
      }
    }
    if(foundFrom == true && foundTo == true) {
      console.log("both are true");
      for(let i = 0; i < users.length; i++) {
        if (users[i].userName == userNameFrom) {
          console.log("transfering from");
          users[i].balance -= parseFloat(transferAmount)
        }
        if (users[i].userName == userNameTo) {
          console.log("transfering to");
          users[i].balance += parseFloat(transferAmount)
        }
      }
    }
    console.log(users);
}
