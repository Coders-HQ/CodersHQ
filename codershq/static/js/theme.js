// Change theme when page loads
document.addEventListener("DOMContentLoaded", function () {
  if (theme == "dark") {
    $("#darkLogo").addClass("hiddenSvg");
    $("body").addClass("theme-dark");
    $("#lightLogo").removeClass("hiddenSvg");
  } else {
    $("#darkLogo").removeClass("hiddenSvg");
    $("body").addClass("theme-light");
    $("#lightLogo").addClass("hiddenSvg");
  }
});

$(function () {
  var current = location.pathname;
  $(".nav-link").each(function () {
    var $this = $(this);
    // if the current path is like this link, make it active
    if ($this.attr("href").indexOf(current) !== -1 && current.length > 1) {
      $this.addClass("active");
    } else if ($this.attr("id") === "homeLink" && current === "/") {
      $this.addClass("active");
    }
  });
});
