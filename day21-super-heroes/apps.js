let btnSearch = document.getElementById('btnSearch')
let searchTerm = ""
btnSearch = addEventListener('click', function(){
  searchTerm = document.getElementById('searchTerm').value

let searchURL = "http://www.omdbapi.com/?s=" + searchTerm + "&apikey=202cf207"
let mainTitle  = document.getElementById('mainTitle')
let movieTitles = document.getElementById('movieTitles')
let title = document.getElementById('title')
let poster = document.getElementById('poster')
let year = document.getElementById('year')
let rating = document.getElementById('rating')
let released = document.getElementById('released')
mainTitle.innerHTML = searchTerm + " Movies"
let request = new XMLHttpRequest()
request.open("GET",searchURL)
request.send()
request.onload = function(){
  if (request.status != 200) {
    console.log("server not found");
  } else {
    let moviesResponse = JSON.parse(request.responseText)
    let listResponse = moviesResponse.Search.map(function(titles) {
      return `<li>${titles.Title}<a href='#' onclick = 'getMoreInfo("${titles.imdbID}")'><img src = '${titles.Poster}' /></a></li>`
    })
movieTitles.innerHTML = listResponse.join('')

}
}
})

function getMoreInfo (imdbID) {
  console.log(imdbID);
  let requestedURL = 'http://www.omdbapi.com/?i='+imdbID+'&apikey=202cf207'
  let request = new XMLHttpRequest()
  request.open("GET",requestedURL)
  request.send()
  request.onload = function(){
    if (request.status != 200) {
      console.log("server not found");
    } else {
  let moviesResponse = JSON.parse(request.responseText)
  swalAlert(moviesResponse)
}
}


// Courtesy of Richard Lorenzini //
function swalAlert(i) {
  swal({
    text: JSON.stringify(i, null, 4),
    title: `${i.Title}`,
    text: `Year: ${i.Year}
    Rating: ${i.Rated}
    Released: ${i.Released}
    Director: ${i.Director}
    Writer: ${i.Writer}
    Cast: ${i.Actors}
    Plot: ${i.Plot}`,
    icon: `${i.Poster}`
  })
}
