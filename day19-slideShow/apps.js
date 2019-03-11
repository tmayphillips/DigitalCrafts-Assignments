let imgDiv = document.getElementById('imgDiv')
let desc = "`<img src='${item.url}' />`"
let images = [
{
  "url" : "1.png"
  },
  {"url" : "2.png"
  },
  {"url" : "3.png"
}]

/*images.map(function(item){
  images.forEach(function() {
    setInterval(function(){
      let result = eval(desc)
      imgDiv.innerHTML = result
      },2000)
    })
  })*/

images.map(function(item){
images.forEach(function() {
  setInterval(function(){
    let result = eval(desc)
    imgDiv.innerHTML = result
  },2000)
})
})
