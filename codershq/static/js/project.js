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
      $("#issuesGrid").append(
        `<div class="col-lg-4 col-md-6">
          <div class="ud-single-issue">
              <div class="ud-issue-content">
                  <span class="ud-blog-date">${date_str}</span>
                  <h3 class="ud-issue-title"><a class="ud-issue-span" href="${issue.html_url}">${issue.title}</a></h3>
                  <span class="ud-issue-author">${issue.user.login}</span>
              </div>
          </div>
      </div>`
      );
    }
  });
  $("#issuesCount").append(
    `<a href='https://github.com/Coders-HQ/CodersHQ/issues?q=is%3Aopen+is%3Aissue'>
      <span class='issues-span'>${issueCount} issues.</span>
      </a>`
  );
}
