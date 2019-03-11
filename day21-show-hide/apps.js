let body = $("body")
let btnHide = $("<button>")
let btnShow = $("<button>")
let div = $("<div>")
let title = $("<h1>")
let img = $("<img>")
btnHide.html("Hide")
btnShow.html("Show")
title.append("Div Show and Hide")
img.attr("src",'image.jpeg')
div.append(btnHide)
div.append(title)
div.append(img)
body.append(div)

btnHide.click(function(){
  $("div").hide(1000);
  $(btnHide.hide())
  body.append(btnShow)
  $(btnShow.show())
  })

btnShow.click(function(){
  $("div").show(1000);
  $(btnHide.show())
  $(btnShow.hide())
})
