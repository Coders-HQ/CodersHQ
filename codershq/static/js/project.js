var theme = window.localStorage.getItem("preferredTheme");

/* Project specific Javascript goes here. */
(function () {
  $('[data-toggle="tooltip"]').tooltip();
});

var tooltipTriggerList = [].slice.call(
  document.querySelectorAll('[data-bs-toggle="tooltip"]')
);
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl);
});

var tooltipTriggerList = [].slice.call(
  document.querySelectorAll('[data-bs-toggle="tooltip"]')
);
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl);
});

var urlToGetAllOpenBugs =
  "https://api.github.com/repos/Coders-HQ/CodersHQ/issues?state=open&";

/* $(document).ready(function () {
  $.getJSON(urlToGetAllOpenBugs, function (allIssues) {
    console.log(allIssues);
    $("#issuesCount").append(allIssues.length + " issues.");
    $.each(allIssues, function (i, issue) {
      $("#issuesGrid").append('<div class="col-lg-4 col-md-6">');
      $("#issuesGrid").append('<div class="ud-single-blog">');
      $("#issuesGrid").append('<div class="ud-blog-image">');
      $("#issuesGrid").append('<a href="#">');
      $("#issuesGrid").append(
        '<img src="assets/images/blog/blog-01.jpg" alt="blog" />'
      );
      $("#issuesGrid").append("</a>");
      $("#issuesGrid").append("</div>");
      $("#issuesGrid").append('<div class="ud-blog-content">');
      $("#issuesGrid").append(
        '<span class="ud-blog-date">' + issue.created_at + "</span>"
      );
      $("#issuesGrid").append('<h3 class="ud-blog-title">');
      $("#issuesGrid").append('<a href="#">');
      $("#issuesGrid").append(issue.title);
      $("#issuesGrid").append("</a>");
      $("#issuesGrid").append("</h3>");
      $("#issuesGrid").append('<p class="ud-blog-desc">');
      $("#issuesGrid").append(
        "Lorem Ipsum is simply dummy text of the printing and"
      );
      $("#issuesGrid").append("typesetting industry.");
      $("#issuesGrid").append("</p>");
      $("#issuesGrid").append("</div>");
      $("#issuesGrid").append("</div>");
      $("#issuesGrid").append("</div>");
    });
  });
}); */

$(document).ready(function () {
  var html = "";
  $("#issuesGrid").html("");
  $.ajax({
    url: urlToGetAllOpenBugs,
    dataType: "jsonp",
    success: function (allIssues) {
      //console.log(returndata);
      $("#issuesCount").append(
        "<a href='https://github.com/Coders-HQ/CodersHQ/issues'><span class='issues-span'>" +
          allIssues.data.length +
          " issues.</span></a>"
      );
      $.each(allIssues.data, function (i, issue) {
        var date = new Date(issue.created_at);
        date.toDateString();
        var month = date.getMonth() + 1;
        var day = date.getDate();
        var year = date.getFullYear();
        date_str = month + "/" + day + "/" + year;
        $("#issuesGrid").append(
          '<div class="col-lg-4 col-md-6"><div class="ud-single-issue">' +
            '<div class="ud-issue-content">' +
            '<span class="ud-blog-date">' +
            date_str +
            "</span>" +
            '<h3 class="ud-issue-title">' +
            '<a href="' +
            issue.html_url +
            '">' +
            issue.title +
            '</a></h3><p class="ud-issue-desc">' +
            issue.user.login +
            "</p></div></div></div></div>"
        );
      });
    },
  });
  return false;
}); // close repo click handler
