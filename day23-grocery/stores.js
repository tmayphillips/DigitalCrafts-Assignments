class Store {
  constructor(key,name,userID) {
    this.key = key
    this.name = name
    this.userID = userID
  }
}

class User {
  contructor(key,name,password) {
    this.key = key
    this.name = name
    this.password = password
  }
}

class Item {
  constructor(key,userID,store,name,qty){
  this.key = key
  this.userID = userID
  this.store = store
  this.name = name
  this.qty = qty
  }
}
