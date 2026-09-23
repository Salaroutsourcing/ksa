/* Small, synchronous preference loader avoids a theme flash. No network requests. */
(() => {
  try {
    const theme = localStorage.getItem("sk-theme");
    if (theme === "light" || theme === "dark")
      document.documentElement.dataset.theme = theme;
    if (localStorage.getItem("sk-motion") === "paused")
      document.documentElement.dataset.motion = "paused";
  } catch (_) {
    /* Preferences are optional when storage is unavailable. */
  }
})();
