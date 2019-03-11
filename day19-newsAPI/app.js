let listUL = document.getElementById('listUL')
let desc = "`<li class='noBullets'><h3>${item.title||''}</h3><h4>${item.author||''}</h4><p>${item.description||''}</p><a href='${item.url||''}'><img id='imageSize' src = '${item.urlToImage}' alt='blank image' /></a><p>${item.publishedAt||''}</p></li>`"

let article = news.articles.map(function(item) {
  return eval(desc)
})
listUL.innerHTML = article.join('')
