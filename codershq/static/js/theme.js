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
