

// In order to get the quotes you can call the getStockQuote function as shown below:

// getStockQuote(pass in the symbol of the stock)

// available symbols are below:
// APLE
// AMAZ
// ALBAB
// GOOG
// FB

let quotes = {
  "APLE":{name : "Apple", price : 0},
  "AMAZ":{name : "Amazon", price :0},
  "ALBAB":{name : "Ali Baba", price :0},
  "GOOG":{name : "Google", price :0},
  "FB":{name : "Facebook", price :0}
}

function getStockQuote(symbol) {

  let stock = quotes[symbol]
  stock.price = getRandomInt(100,500)
  return quotes[symbol]
}

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min
}


btnStock = addEventListener('click', function(){
window.setInterval(function(){
  let symbolID = document.getElementById('symbol').value
  let btnStock = document.getElementById('btnStock')
  let stockName = document.getElementById('stockName')
  let stockPrice = document.getElementById('stockPrice')
  let stockQuote = getStockQuote(symbolID)
  stockName.innerHTML = stockQuote.name
  stockPrice.innerHTML = `$${stockQuote.price}`
},2000)
})
