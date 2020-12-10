//links to a page that shows the user about meditation(will temporarily use home until the page is created)
var modal;
function linker_meditation()
{
    modal = document.getElementById('modal-meditation');
    modal.style.display = "block";
}
window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }
function link_breathing_article(){
  location.href="https://mindworks.org/blog/breathing-techniques-meditation/";
}
function link_relaxing_article(){
  location.href="https://www.healthline.com/health/mental-health/meditation-positions";
}