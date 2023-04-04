// disable the browser's form resubmission confirmation
if (window.history.replaceState) {
  window.history.replaceState(null, null, window.location.href);
}
