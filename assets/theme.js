(() => {
  const storageKey = "julius-theme";
  const root = document.documentElement;

  const readStoredTheme = () => {
    try {
      const theme = localStorage.getItem(storageKey);
      return theme === "light" || theme === "dark" ? theme : null;
    } catch {
      return null;
    }
  };

  const applyTheme = (theme, persist = false) => {
    root.dataset.theme = theme;
    if (persist) {
      try {
        localStorage.setItem(storageKey, theme);
      } catch {
        // The preference still applies for this visit when storage is unavailable.
      }
    }
  };

  const currentTheme = readStoredTheme() || "dark";
  root.classList.add("js");
  applyTheme(currentTheme);

  const updateToggle = (toggle, theme) => {
    const nextTheme = theme === "dark" ? "light" : "dark";
    toggle.setAttribute("aria-label", `Switch to ${nextTheme} theme`);
    toggle.setAttribute("title", `Switch to ${nextTheme} theme`);
    toggle.setAttribute("aria-pressed", String(theme === "light"));
  };

  const initializeToggle = () => {
    const toggle = document.querySelector("[data-theme-toggle]");
    if (!toggle) return;

    const theme = root.dataset.theme === "light" ? "light" : "dark";
    updateToggle(toggle, theme);
    toggle.addEventListener("click", () => {
      const nextTheme = root.dataset.theme === "light" ? "dark" : "light";
      applyTheme(nextTheme, true);
      updateToggle(toggle, nextTheme);
    });
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initializeToggle, { once: true });
  } else {
    initializeToggle();
  }
})();
