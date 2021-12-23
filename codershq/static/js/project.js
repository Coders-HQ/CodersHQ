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

/* Caching GitHub API (Caches results for 10 minutes) */

var localCache = {
  /**
   * timeout for cache in millis
   * @type {number}
   */
  timeout: 900000,
  /**
   * @type {{_: number, data: {}}}
   **/
  data: {},
  remove: function (url) {
    delete localCache.data[url];
  },
  exist: function (url) {
    return (
      !!localCache.data[url] &&
      new Date().getTime() - localCache.data[url]._ < localCache.timeout
    );
  },
  get: function (url) {
    console.log("Getting in cache for url" + url);
    return localCache.data[url].data;
  },
  set: function (url, cachedData, callback) {
    localCache.remove(url);
    localCache.data[url] = {
      _: new Date().getTime(),
      data: cachedData,
    };
    if ($.isFunction(callback)) callback(cachedData);
  },
};

$.ajaxPrefilter(function (options, originalOptions, jqXHR) {
  if (options.cache) {
    var complete = originalOptions.complete || $.noop,
      url = originalOptions.url;
    //remove jQuery cache as we have our own localCache
    options.cache = false;
    options.beforeSend = function () {
      if (localCache.exist(url)) {
        complete(localCache.get(url));
        return false;
      }
      return true;
    };
    options.complete = function (data, textStatus) {
      localCache.set(url, data, complete);
    };
  }
});

$(function () {
  var url =
    "https://api.github.com/repos/Coders-HQ/CodersHQ/issues?state=open&issue";
  $(document).ready(function (e) {
    $.ajax({
      url: url,
      data: {
        test: "value",
      },
      cache: true,
      complete: fetchIssues,
    });
  });
});

var imageLocation = document.getElementById("imageLocation").value;

function fetchIssues(data) {
  var allIssues = data.responseJSON;
  var issueCount = 0;
  //console.log(returndata);
  $.each(allIssues, function (i, issue) {
    if (!issue.pull_request) {
      issueCount += 1;
      var date = new Date(issue.created_at);
      date.toDateString();
      var month = date.getMonth() + 1;
      var day = date.getDate();
      var year = date.getFullYear();
      date_str = month + "/" + day + "/" + year;
      //style="color: #${issue.labels.color}"
      var labels = issue.labels.flatMap((x) => x);
      $("#issuesGrid").append(
        `<div class="ud-single-issue">
              <a href="${issue.html_url}" target='_blank'>
              <div class="ud-issue-content">
                  <div class="ud-issue-upper-part">
                    <img
                    src="${imageLocation}"
                    alt="Coders HQ Logo"
                    class="ud-issue-chq-logo"
                    />
                    <div class="ud-issue-repo-name">Coders-HQ/CodersHQ</div>
                  </div>
                  <div class="ud-issue-labels" id="udLabels-${issueCount}">
                  </div>
                  <h3 class="ud-issue-title"><span class="ud-issue-span">${
                    issue.title.length < 50
                      ? issue.title
                      : issue.title.substring(0, 40) + "..."
                  }</span></h3>
              </div>
              </a>
          </div>`
      );
      //console.log(issueCount);
      console.log(issue.labels.length);
      let labelCount = 0;
      if (issue.labels.length > 0) {
        labels.forEach((label) => {
          labelCount += 1;
          if (labelCount <= 3) {
            $("#udLabels-" + issueCount).append(
              `<div class="ud-issue-single-label" style="background-color: #${
                label.color
              }">${
                label.name.length < 5
                  ? label.name
                  : label.name.substring(0, 5) + "..."
              }</div>`
            );
          } else {
            return;
          }
        });
      } else {
        $("#udLabels-" + issueCount).append(
          `<div class="ud-issue-single-label" style="background-color: #232323">Unlabled</div>`
        );
      }
    }
  });
  $("#issuesCount").append(
    `<a target='_blank' href='https://github.com/Coders-HQ/CodersHQ/issues?q=is%3Aopen+is%3Aissue'>
      <span class='issues-span'>${issueCount} open issues</span>
      </a>`
  );
}
