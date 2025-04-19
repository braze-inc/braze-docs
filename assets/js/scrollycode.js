document.addEventListener("DOMContentLoaded", () => {
  // Process each scrolly block independently.
  const scrollyBlocks = document.querySelectorAll(".scrolly-code-block");

  scrollyBlocks.forEach((block) => {
    // Get narrative steps, tab buttons, and code panels within this block.
    const id = block.getAttribute("id");
    const steps = [...block.querySelectorAll(".scrolly-step")];
    const tabButtons = [
      ...block.querySelectorAll(".scrolly-tab-selector button"),
    ];
    const codeBlocks = [...block.querySelectorAll(".code-blocks pre")];

    let currentIndex = 0; // active narrative step index for this block

    // Helper: Return the currently active <pre> element.
    function getActiveCodeBlock() {
      return (
        codeBlocks.find((pre) => pre.style.display !== "none") || codeBlocks[0]
      );
    }

    // Build code spans and update highlights in the active code block.
    function highlightLines(linesToHighlight = []) {
      const activePre = getActiveCodeBlock();
      if (!activePre) return;
      const codeElem = activePre.querySelector("code");
      if (!codeElem) return;
      const rawCode = codeElem.dataset.fullCode?.trim() || "";
      if (!rawCode) return;
      const rawLines = rawCode.split("\n");

      const fragment = document.createDocumentFragment();
      // Detect language from the active pre element (default to "javascript")
      const langMatch = activePre.className.match(/language-(\w+)/);
      const lang = langMatch ? langMatch[1] : "javascript";

      rawLines.forEach((line, i) => {
        const lineEl = document.createElement("span");
        lineEl.innerHTML = hljs.highlight(line || " ", {
          language: lang,
        }).value;
        lineEl.classList.add("code-line");
        if (linesToHighlight.includes(i + 1)) {
          lineEl.dataset.highlight = "true";
        } else {
          delete lineEl.dataset.highlight;
        }
        fragment.appendChild(lineEl);
      });
      codeElem.innerHTML = "";
      codeElem.appendChild(fragment);
      updateHighlightOverlay();
    }

    // Create or update overlays for highlighted lines.
    function updateHighlightOverlay() {
      const activePre = getActiveCodeBlock();
      if (!activePre) return;
      const codeElem = activePre.querySelector("code");
      if (!codeElem) return;
      // Remove any existing overlays.
      activePre
        .querySelectorAll(".highlight-overlay")
        .forEach((el) => el.remove());
      const highlightedLines = Array.from(
        codeElem.querySelectorAll(".code-line[data-highlight='true']")
      );
      if (highlightedLines.length === 0) return;

      const containerRect = activePre.getBoundingClientRect();
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
        overlay.style.top = groupTop + "px";
        overlay.style.height = newHeight + "px";
        overlay.style.opacity = "0";
        activePre.appendChild(overlay);
        requestAnimationFrame(() => {
          overlay.style.opacity = "1";
        });
      });
    }

    // Parse a range string like "1-3,5" into an array of line numbers.
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
      return Array.from(result).sort((a, b) => a - b);
    }

    // Activate a narrative step by index.
    // Each step is expected to have a data attribute in the form:
    // data-lines-<filekey>="<range>" (e.g. data-lines-index-js="1-3").
    function activateStep(index) {
      if (index < 0 || index >= steps.length) return;
      currentIndex = index;
      steps.forEach((step, i) => {
        step.setAttribute("data-active", i === index ? "true" : "false");
      });
      const currentStep = steps[index];
      // Look for a data attribute starting with "data-lines-"
      let activeFile = null;
      for (const attr of currentStep.attributes) {
        if (attr.name.startsWith("data-lines-")) {
          activeFile = attr.name.replace("data-lines-", "");
          break;
        }
      }
      if (!activeFile) return;
      // Activate the corresponding tab in this block.
      tabButtons.forEach((btn) => {
        btn.classList.toggle(
          "scrolly-active-tab",
          btn.dataset.file === activeFile
        );
      });
      codeBlocks.forEach((pre) => {
        pre.style.display = pre.dataset.file === activeFile ? "" : "none";
      });
      const rangeStr =
        currentStep.getAttribute(`data-lines-${activeFile}`) || "";
      const highlightList = parseLineRange(rangeStr);
      highlightLines(highlightList);
    }

    // Determine the closest narrative step based on scroll position.
    function getClosestStep() {
      // workaround to make sure the first step is selected while scrolling back up
      if (stepsContainer.scrollTop < 5) return 0;
      // workaround to make sure the last step is selected while scrolling down
      if (
        stepsContainer.scrollTop >
        stepsContainer.scrollHeight - stepsContainer.clientHeight - 5
      )
        return steps.length - 1;
      const style = getComputedStyle(stepsContainer);
      const paddingBottom = parseFloat(style.paddingBottom) || 0;
      const effectiveHeight = stepsContainer.clientHeight + paddingBottom;
      const centerY = stepsContainer.scrollTop + effectiveHeight * 0.5;
      let closestIdx = currentIndex;
      let minDistance = Infinity;
      steps.forEach((step, i) => {
        // Use offsetTop relative to the scroll container.
        const mid = step.offsetTop + step.offsetHeight / 2;
        const distance = Math.abs(mid - centerY);
        if (distance < minDistance) {
          minDistance = distance;
          closestIdx = i;
        }
      });
      return closestIdx;
    }

    // Get the scrollable steps container.
    const stepsContainer = block.querySelector(".scrolly-text");
    // Attach scroll event to the steps container instead of the window.
    stepsContainer.addEventListener("scroll", () => {
      const idx = getClosestStep();
      if (idx !== currentIndex) {
        activateStep(idx);
      }
    });

    // Clicking on a narrative step activates it.
    steps.forEach((step, i) => {
      step.addEventListener("click", () => {
        step.scrollIntoView({ behavior: "smooth", block: "center" });
        activateStep(i);
      });
    });

    // Clicking on a tab manually overrides the current narrative selection.
    tabButtons.forEach((btn) => {
      btn.addEventListener("click", () => {
        const fileKey = btn.dataset.file;
        tabButtons.forEach((b) => {
          b.classList.toggle("scrolly-active-tab", b.dataset.file === fileKey);
        });
        codeBlocks.forEach((pre) => {
          pre.style.display = pre.dataset.file === fileKey ? "" : "none";
        });
        // When a tab is clicked manually, clear any highlights.
        highlightLines([]);
      });
    });

    // IntersectionObserver to handle blocks that are initially hidden.
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            // When the block becomes visible, re-activate its current step.
            activateStep(currentIndex);
          }
        });
      },
      { threshold: 0.1 }
    );
    observer.observe(block);

    // Initialize this block after a short delay.
    setTimeout(() => {
      activateStep(0);
    }, 100);
  });
});
