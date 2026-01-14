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
    let isProgrammaticScroll = false;

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
      scrollCodeToHighlight();
    }

    function scrollCodeToHighlight() {
      const activePre = getActiveCodeBlock();
      if (!activePre) return;

      // Find the first highlighted line
      const firstHl = activePre.querySelector(
        '.code-line[data-highlight="true"]'
      );
      if (!firstHl) return;

      // Compute its offset *inside* the pre
      const hlOffset = firstHl.offsetTop;
      const hlHeight = firstHl.clientHeight;
      const containerHt = activePre.clientHeight;

      // Target so that the highlighted line sits vertically centered
      const scrollTo = hlOffset - containerHt / 2 + hlHeight / 2;

      activePre.scrollTo({
        top: scrollTo,
        behavior: "smooth",
      });
    }

    // Create or update overlays for highlighted lines.
    function updateHighlightOverlay() {
      const activePre = getActiveCodeBlock();
      if (!activePre) return;

      // ensure <pre> is positioning context
      if (getComputedStyle(activePre).position === "static") {
        activePre.style.position = "relative";
      }

      // clear old overlays…
      activePre
        .querySelectorAll(".highlight-overlay")
        .forEach((el) => el.remove());

      const codeElem = activePre.querySelector("code");
      if (!codeElem) return;

      // pull out all the highlighted code-line spans
      const highlighted = Array.from(
        codeElem.querySelectorAll('.code-line[data-highlight="true"]')
      );
      if (!highlighted.length) return;

      // group contiguous runs…
      const groups = [];
      let run = [highlighted[0]];
      for (let i = 1; i < highlighted.length; i++) {
        const prev = highlighted[i - 1],
          curr = highlighted[i];
        if (
          Math.abs(curr.offsetTop - (prev.offsetTop + prev.offsetHeight)) < 2
        ) {
          run.push(curr);
        } else {
          groups.push(run);
          run = [curr];
        }
      }
      groups.push(run);

      // compute the pre's top padding:
      const preStyle = getComputedStyle(activePre);
      const prePaddingTop = parseFloat(preStyle.paddingTop) || 0;

      // for each group, position one overlay
      groups.forEach((group) => {
        const first = group[0];
        const last = group[group.length - 1];

        // original offsetTop is relative to the code element;
        // now we add the pre's top padding so it aligns under the spans
        const top = first.offsetTop + prePaddingTop;
        const height = last.offsetTop + last.offsetHeight - first.offsetTop;

        const overlay = document.createElement("div");
        overlay.className = "highlight-overlay";
        overlay.style.top = `${top}px`;
        overlay.style.height = `${height}px`;
        overlay.style.width = codeElem.scrollWidth + "px";
        activePre.appendChild(overlay);
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

    const PREFERRED_TOP_OFFSET = 100;
    // Determine the closest narrative step based on scroll position.
    function getClosestStep() {
      // 1) If we’re within 1px of the bottom, immediately return the last real step
      const scrollBottom =
        stepsContainer.scrollTop + stepsContainer.clientHeight;
      if (scrollBottom >= stepsContainer.scrollHeight - 1) {
        // find the index of the last *non-rating* step
        const normalSteps = steps.filter(
          (s) => !s.classList.contains("rating-step")
        );
        return steps.indexOf(normalSteps[normalSteps.length - 1]);
      }

      // 2) Otherwise, fall back to your existing “20px from top” midpoint logic:
      const containerRect = stepsContainer.getBoundingClientRect();
      const referenceY = containerRect.top + PREFERRED_TOP_OFFSET;

      let closestIdx = currentIndex;
      let minDistance = Infinity;

      steps.forEach((step, i) => {
        if (step.classList.contains("rating-step")) return;
        const stepRect = step.getBoundingClientRect();
        const stepMidY = stepRect.top + stepRect.height / 2;
        const distance = Math.abs(stepMidY - referenceY);
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
      if (isProgrammaticScroll) return;
      const idx = getClosestStep();
      if (idx !== currentIndex) {
        activateStep(idx);
      }
    });

    const normalSteps = steps.filter(
      (s) => !s.classList.contains("rating-step")
    );
    const lastStep = normalSteps[normalSteps.length - 1];
    const ratingStep = block.querySelector(".rating-step");

    // Compute & apply the adaptive bottom buffer:
    function updateBottomBuffer() {
      const containerH = stepsContainer.clientHeight;
      const ratingH = ratingStep.clientHeight;
      const lastStepH = lastStep.clientHeight;

      const buffer = Math.max(
        0,
        containerH - ratingH - lastStepH - PREFERRED_TOP_OFFSET
      );
      stepsContainer.style.paddingBottom = `${buffer}px`;
    }

    updateBottomBuffer();
    window.addEventListener("resize", updateBottomBuffer);

    steps.forEach((step, i) => {
      step.addEventListener("click", () => {
        if (step.classList.contains("rating-step")) return;

        isProgrammaticScroll = true;

        // ─── Compute “rawTarget” via bounding rectangles ───
        // 1) Where is the container on screen?
        const containerRect = stepsContainer.getBoundingClientRect();
        // 2) Where is this step on screen?
        const stepRect = step.getBoundingClientRect();
        // 3) How many pixels between step.top and container.top?
        const distanceToContainerTop = stepRect.top - containerRect.top;
        // 4) Subtract PREFERRED_TOP_OFFSET so the step ends up that many px down
        const rawTarget =
          stepsContainer.scrollTop +
          distanceToContainerTop -
          PREFERRED_TOP_OFFSET;

        // ─── Clamp to [0, maxScroll] ───
        const maxScroll =
          stepsContainer.scrollHeight - stepsContainer.clientHeight;
        const targetScroll = Math.max(0, Math.min(rawTarget, maxScroll));

        // ─── Smooth-scroll the container ───
        stepsContainer.scrollTo({
          top: targetScroll,
          behavior: "smooth",
        });

        // ─── Immediately activate/highlight this step ───
        activateStep(i);

        // ─── Re-enable normal scroll logic after the animation ───
        setTimeout(() => {
          isProgrammaticScroll = false;
        }, 400);
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

    const codeContainer = block.querySelector(".scrolly-code .code-animate");
    codeContainer.addEventListener("scroll", updateHighlightOverlay);

    // IntersectionObserver to handle blocks that are initially hidden.
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            // When the block becomes visible, re-activate its current step.
            updateBottomBuffer();
            activateStep(currentIndex);
          }
        });
      },
      { threshold: 0.1 }
    );
    observer.observe(block);

    // === rating prompt handler ===
    const stars = Array.from(ratingStep.querySelectorAll(".star"));
    stars.forEach((star, idx) => {
      star.addEventListener("click", () => {
        const rating = 5 - idx;

        // 1) Log to Braze
        if (window.braze?.logCustomEvent) {
          braze.logCustomEvent("Tutorial Rating", {
            tutorial: feedback_site,
            rating,
          });
          braze.requestImmediateDataFlush();
        }

        // 2) Send to feedback.js's network request
        var submit_data = {
          Helpful:
            rating === 5
              ? "Very Helpful"
              : rating === 4
              ? "Helpful"
              : rating === 3
              ? "Somewhat Helpful"
              : rating === 2
              ? "Unhelpful"
              : "Very Unhelpful",
          URL: feedback_site,
          "Article Title": feedback_article_title,
          "Nav Title": feedback_nav_title,
          Params: window.location.search,
          Language: page_language,
        };
        console.log("Sending feedback data:", submit_data);
        $.ajax({
          url: "https://c9616da7-4322-4bed-9b51-917c1874fb31.trayapp.io/feedback",
          method: "GET",
          dataType: "json",
          data: submit_data,
        });

        // 3) Update UI
        stars.forEach((s, i) => {
          s.classList.toggle("selected", i < rating);
        });
        ratingStep.classList.add("rated");

        // 4) disable further clicks
        stars.forEach((s) => (s.style.pointerEvents = "none"));
      });
    });

    // Initialize this block after a short delay.
    setTimeout(() => {
      activateStep(0);
    }, 100);
  });
});
