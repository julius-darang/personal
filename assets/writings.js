(() => {
  const initializeFilters = () => {
    const buttons = [...document.querySelectorAll("[data-writing-filter]")];
    const cards = [...document.querySelectorAll("[data-writing-card]")];
    const status = document.querySelector("[data-filter-status]");
    const empty = document.querySelector("[data-filter-empty]");

    if (!buttons.length || !cards.length) return;

    const applyFilter = (filter) => {
      let visible = 0;

      cards.forEach((card) => {
        const topics = (card.dataset.topics || "").split(" ");
        const isVisible = filter === "all" || topics.includes(filter);
        card.hidden = !isVisible;
        if (isVisible) visible += 1;
      });

      buttons.forEach((button) => {
        const isActive = button.dataset.writingFilter === filter;
        button.classList.toggle("active", isActive);
        button.setAttribute("aria-pressed", String(isActive));
      });

      if (status) {
        const topic = filter === "all" ? "all topics" : filter.replace("-", " ");
        status.textContent = `Showing ${visible} ${visible === 1 ? "writing" : "writings"} in ${topic}`;
      }
      if (empty) empty.hidden = visible !== 0;
    };

    buttons.forEach((button) => {
      button.addEventListener("click", () => applyFilter(button.dataset.writingFilter || "all"));
    });

    applyFilter("all");
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initializeFilters, { once: true });
  } else {
    initializeFilters();
  }
})();
