document.addEventListener("DOMContentLoaded", () => {
  // Process each scrolly block independently.
  const scrollyBlocks = document.querySelectorAll(".scrolly-code-block");

  scrollyBlocks.forEach((block) => {
    // Within each block, get its own steps and code container.
    const steps = [...block.querySelectorAll(".scrolly-step")];
    const codeContainer = block.querySelector(".code-animate");
    if (!codeContainer) {
      console.warn("Missing code container in scrolly block", block);
      return;
    }
    const codeBlock = codeContainer.querySelector("code");
    const rawCode = codeBlock?.dataset?.fullCode?.trim() || "";

    if (!rawCode) {
      console.warn(
        "Missing full code in data-full-code attribute in block",
        block
      );
      return;
    }

    const rawLines = rawCode.split("\n");
    let currentIndex = -1;

    // Build the code block – each line is a <span> with a "code-line" class.
    function highlightLines(linesToHighlight = []) {
      const fragment = document.createDocumentFragment();
      rawLines.forEach((line, i) => {
        const lineEl = document.createElement("span");
        lineEl.innerHTML = hljs.highlight(line || " ", {
          language: "javascript",
        }).value;
        lineEl.classList.add("code-line");
        // Mark highlighted lines.
        if (linesToHighlight.includes(i + 1)) {
          lineEl.dataset.highlight = "true";
        } else {
          delete lineEl.dataset.highlight;
        }
        fragment.appendChild(lineEl);
      });
      codeBlock.innerHTML = "";
      codeBlock.appendChild(fragment);
      updateHighlightOverlay();
    }

    // Create or update overlay(s) for highlighted lines.
    function updateHighlightOverlay() {
      // Remove existing overlays.
      codeContainer
        .querySelectorAll(".highlight-overlay")
        .forEach((el) => el.remove());
      const highlightedLines = [
        ...codeBlock.querySelectorAll(".code-line[data-highlight='true']"),
      ];
      if (highlightedLines.length === 0) return;

      const containerRect = codeContainer.getBoundingClientRect();

      // Group contiguous highlighted lines.
      let groups = [];
      let currentGroup = [highlightedLines[0]];
      for (let i = 1; i < highlightedLines.length; i++) {
        const prevRect = highlightedLines[i - 1].getBoundingClientRect();
        const currRect = highlightedLines[i].getBoundingClientRect();
        if (Math.abs(currRect.top - prevRect.bottom) < 2) {
          currentGroup.push(highlightedLines[i]);
        } else {
          groups.push(currentGroup);
          currentGroup = [highlightedLines[i]];
        }
      }
      groups.push(currentGroup);

      groups.forEach((group) => {
        let groupTop = Infinity,
          groupBottom = -Infinity;
        group.forEach((line) => {
          const rect = line.getBoundingClientRect();
          const relTop = rect.top - containerRect.top;
          const relBottom = rect.bottom - containerRect.top;
          if (relTop < groupTop) groupTop = relTop;
          if (relBottom > groupBottom) groupBottom = relBottom;
        });
        const newHeight = groupBottom - groupTop;
        const overlay = document.createElement("div");
        overlay.className = "highlight-overlay";
        // Set initial values with opacity 0.
        overlay.style.top = groupTop + "px";
        overlay.style.height = newHeight + "px";
        overlay.style.opacity = "0";
        codeContainer.appendChild(overlay);
        // Force a reflow and then update to trigger the transition.
        requestAnimationFrame(() => {
          overlay.style.opacity = "1";
        });
      });
    }

    function parseLineRange(rangeStr) {
      const parts = rangeStr.split(",").map((p) => p.trim());
      const result = new Set();
      for (let part of parts) {
        if (part.includes("-")) {
          const [start, end] = part.split("-").map(Number);
          for (let i = start; i <= end; i++) result.add(i);
        } else {
          result.add(Number(part));
        }
      }
      return [...result].sort((a, b) => a - b);
    }

    function activate(index) {
      if (index === currentIndex || index < 0 || index >= steps.length) return;
      steps.forEach((el, i) =>
        el.setAttribute("data-active", i === index ? "true" : "false")
      );
      const lines = steps[index].dataset.lines || "";
      const highlightList = parseLineRange(lines);
      highlightLines(highlightList);
      currentIndex = index;
    }

    function getClosestStep() {
      if (window.scrollY < 50) return 0;
      const centerY = window.scrollY + window.innerHeight / 2;
      let closestIdx = -1;
      let minDistance = Infinity;
      steps.forEach((step, i) => {
        const rect = step.getBoundingClientRect();
        const mid = rect.top + window.scrollY + rect.height / 2;
        const distance = Math.abs(mid - centerY);
        if (distance < minDistance) {
          minDistance = distance;
          closestIdx = i;
        }
      });
      return closestIdx;
    }

    // Attach scroll event for this block.
    window.addEventListener("scroll", () => {
      const index = getClosestStep();
      if (index !== -1) activate(index);
    });

    // Allow clicking on a narrative step to activate it.
    steps.forEach((el, i) => {
      el.dataset.index = i;
      el.addEventListener("click", () => {
        el.scrollIntoView({ behavior: "smooth", block: "center" });
        activate(i);
      });
    });

    // Expose updateHighlightOverlay to the block so it can be called externally.
    block.updateHighlightOverlay = updateHighlightOverlay;

    // Initialize this block.
    setTimeout(() => activate(0), 100);

    // Needed so that the highlight overlay shows up if a scrolly block is initially rendered out of view (ie. behind anohter tab)
    const observer = new IntersectionObserver(
      (entries, observer) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            updateHighlightOverlay();
          }
        });
      },
      { threshold: 0.1 }
    );
    observer.observe(block);
  });
});
