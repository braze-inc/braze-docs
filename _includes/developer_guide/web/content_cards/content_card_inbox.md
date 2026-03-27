{% multi_lang_include developer_guide/prerequisites/web.md %}

However, no additional setup is required.

## Making an inbox with Content Cards for Web

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Content Card Inbox Web" %}

<style>
/* Standard code blocks: light mode, no line numbers */
.highlight {
  background: #ffffff !important;
  border: 1px solid #e2e8f0 !important;
  border-radius: 8px !important;
  box-shadow: 0 1px 4px rgba(0,0,0,0.06) !important;
  overflow: hidden !important;
}
.highlight pre,
.highlight .rouge-code,
.highlight .rouge-code pre {
  background: #ffffff !important;
}
.highlight .rouge-table,
.highlight .rouge-table tbody,
.highlight .rouge-table tr {
  display: block !important;
  width: 100% !important;
}
.highlight .rouge-table td.rouge-code {
  display: block !important;
  width: 100% !important;
}
.highlight td.gl,
.highlight td.gutter,
.highlight .rouge-table td.gl,
.highlight .rouge-table td.gutter,
.highlight .gutter,
.highlight .lineno {
  display: none !important;
  width: 0 !important;
  height: 0 !important;
  overflow: hidden !important;
  padding: 0 !important;
  font-size: 0 !important;
  visibility: hidden !important;
}
.highlight code.hljs,
.highlight pre code.hljs {
  background: #ffffff !important;
  color: #1B2536 !important;
  padding: 16px !important;
}
.highlight .hljs-keyword { color: #0969da !important; font-weight: 600; }
.highlight .hljs-string { color: #0a3069 !important; }
.highlight .hljs-comment { color: #6e7781 !important; font-style: italic; }
.highlight .hljs-function,
.highlight .hljs-title { color: #8250df !important; }
.highlight .hljs-number,
.highlight .hljs-literal { color: #0550ae !important; }
.highlight .hljs-built_in { color: #0550ae !important; }
.highlight .hljs-attr,
.highlight .hljs-attribute { color: #0550ae !important; }
.highlight .hljs-tag,
.highlight .hljs-name { color: #116329 !important; }
.highlight .hljs-params { color: #1B2536 !important; }
.highlight .hljs-meta { color: #0550ae !important; }
.braze-tutorial-intro {
  font-size: 17px;
  line-height: 1.7;
  color: #404756;
  margin-bottom: 28px;
}
.braze-learn-box {
  background: #f0f8ff;
  border: 1px solid #d4e8f7;
  border-left: 4px solid #00B3E6;
  border-radius: 8px;
  padding: 20px 24px;
  margin: 0 0 36px;
}
.braze-learn-box h4 {
  margin: 0 0 12px !important;
  font-size: 15px !important;
  font-weight: 700 !important;
  color: #1B2536 !important;
}
.braze-learn-box ul {
  margin: 0 !important;
  padding-left: 20px !important;
  list-style-type: disc !important;
}
.braze-learn-box li {
  margin: 6px 0 !important;
  font-size: 14px !important;
  color: #3A506B !important;
  line-height: 1.55 !important;
}
.braze-tutorial-sandbox {
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  overflow: hidden;
  margin: 28px 0;
  box-shadow: 0 1px 4px rgba(0,0,0,0.07);
}
.braze-tutorial-sandbox-top {
  background: #f5f7f9;
  display: flex;
  align-items: center;
  padding: 0 4px;
  border-bottom: 1px solid #e2e8f0;
}
.braze-tutorial-tab {
  padding: 9px 14px;
  color: #6b7280;
  font-size: 13px;
  font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
  cursor: pointer;
  border: none;
  background: transparent;
  border-bottom: 2px solid transparent;
  transition: color 0.15s, border-color 0.15s, background 0.15s;
  outline: none;
}
.braze-tutorial-tab:hover {
  color: #1B2536;
}
.braze-tutorial-tab:focus-visible {
  outline: 2px solid #00B3E6;
  outline-offset: -2px;
  border-radius: 4px;
}
.braze-tutorial-tab.active {
  color: #1B2536;
  font-weight: 500;
  border-bottom-color: #00B3E6;
  background: rgba(0, 179, 230, 0.06);
}
.braze-tutorial-sandbox-body {
  display: flex;
  min-height: 200px;
}
@media (max-width: 840px) {
  .braze-tutorial-sandbox-body {
    flex-direction: column;
  }
  .braze-tutorial-preview {
    border-left: none !important;
    border-top: 1px solid #e2e8f0;
  }
}
.braze-tutorial-editor {
  flex: 1.2;
  min-width: 0;
  background: #ffffff;
  overflow: auto;
  max-height: 440px;
  border-right: 1px solid #e2e8f0;
}
.braze-tutorial-panel {
  display: none;
}
.braze-tutorial-panel.active {
  display: block;
}
.braze-tutorial-editor pre {
  margin: 0 !important;
  padding: 16px !important;
  background: #ffffff !important;
  border: none !important;
  border-radius: 0 !important;
  white-space: pre !important;
  overflow-x: auto !important;
}
.braze-tutorial-editor code {
  font-size: 13px !important;
  line-height: 1.65 !important;
  background: transparent !important;
  padding: 0 !important;
  color: #1B2536 !important;
}
.braze-tutorial-editor .hljs {
  background: #ffffff !important;
  color: #1B2536 !important;
}
.braze-tutorial-editor .hljs-keyword {
  color: #0969da !important;
  font-weight: 600;
}
.braze-tutorial-editor .hljs-string {
  color: #0a3069 !important;
}
.braze-tutorial-editor .hljs-comment {
  color: #6e7781 !important;
  font-style: italic;
}
.braze-tutorial-editor .hljs-function,
.braze-tutorial-editor .hljs-title {
  color: #8250df !important;
}
.braze-tutorial-editor .hljs-number,
.braze-tutorial-editor .hljs-literal {
  color: #0550ae !important;
}
.braze-tutorial-editor .hljs-built_in {
  color: #0550ae !important;
}
.braze-tutorial-editor .hljs-attr,
.braze-tutorial-editor .hljs-attribute {
  color: #0550ae !important;
}
.braze-tutorial-editor .hljs-tag,
.braze-tutorial-editor .hljs-name {
  color: #116329 !important;
}
.braze-tutorial-editor .hljs-params {
  color: #1B2536 !important;
}
.braze-tutorial-editor .hljs-meta {
  color: #0550ae !important;
}
.braze-tutorial-preview {
  flex: 1;
  min-width: 0;
  border-left: 1px solid #e2e8f0;
  background: #fff;
  display: flex;
  flex-direction: column;
}
.braze-tutorial-preview-bar {
  padding: 8px 16px;
  background: #f5f7f9;
  border-bottom: 1px solid #e2e8f0;
  font-size: 12px;
  color: #6b7280;
  font-weight: 500;
  letter-spacing: 0.03em;
}
.braze-tutorial-iframe {
  flex: 1;
  width: 100%;
  min-height: 300px;
  border: none;
  display: block;
}
</style>

<div class="braze-tutorial-intro">
  <p>This tutorial walks you through building a custom Content Card inbox in a web app with the Braze Web SDK. Each step adds one idea: initialization, markup, subscriptions, rendering, analytics, and control groups. At the end, you can review the full sample with a live-style preview.</p>
</div>

<div class="braze-learn-box">
  <h4>You will learn how to</h4>
  <ul>
    <li>Initialize the Braze Web SDK and open a session</li>
    <li>Build an inbox container in HTML for your card list</li>
    <li>Subscribe to Content Card updates and refresh the feed</li>
    <li>Render cards from Content Card attributes into the DOM</li>
    <li>Log clicks with <code>logContentCardClick</code></li>
    <li>Log impressions once per card using <code>IntersectionObserver</code></li>
    <li>Omit control-group cards from the inbox UI</li>
  </ul>
</div>

### Step 1: Initialize the SDK

Import the SDK, call `braze.initialize()` with your API key and SDK endpoint, then call `openSession()` so Braze can associate activity with the current user. While you're developing, you can turn on `enableLogging` to send SDK diagnostics to the browser console. You can also assign `window.braze` if you want to call SDK methods from the developer console.

```javascript
import * as braze from "@braze/web-sdk";

// Uncomment this if you'd like to run braze web SDK methods in the console
// window.braze = braze;

// initialize the Braze SDK
braze.initialize("YOUR_API_KEY", {
  baseUrl: "YOUR_API_ENDPOINT",
  enableLogging: true,
});
braze.openSession();
```

Replace `YOUR_API_KEY` and `YOUR_API_ENDPOINT` with the values from your Braze dashboard. Remove `enableLogging` before you ship to production.

### Step 2: Build the inbox container

Add a page (or view) that includes a heading and a single element the script can target—here, a `div` with `id="cards-list"`. Use `aria-live="polite"` so assistive technologies can announce when new cards arrive. Style `.card-item` rows so titles, body text, and optional images match your product.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style>
      body {
        font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial,
          sans-serif;
        margin: 0;
      }
      main {
        max-width: 720px;
        margin: 0 auto;
        padding: 16px;
      }
      h1 {
        margin: 0 0 12px;
        font-size: 24px;
      }
      .card-item {
        border-bottom: 1px solid #eee;
        padding: 12px 0;
        cursor: pointer;
      }
      .card-item h3 {
        margin: 0 0 6px;
        font-size: 16px;
      }
      .card-item p {
        margin: 0;
        color: #444;
      }
      .card-item img {
        max-width: 100%;
        height: auto;
      }
    </style>
  </head>
  <body>
    <main id="app">
      <h1>Message Inbox</h1>
      <div id="cards-list" aria-live="polite"></div>
    </main>

    <script type="module" src="/src/main.js"></script>
  </body>
</html>
```

Point `src` at wherever you bundle `main.js` in your project. The script in the following steps reads `#cards-list` and injects one `<article class="card-item">` per card.

### Step 3: Subscribe to Content Card updates

Register `subscribeToContentCardsUpdates()` before you request a refresh so you don't miss the first payload. The callback receives an updates object; read `updates.cards` (or an empty array) and pass it to your render function. Call [`requestContentCardsRefresh()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestcontentcardsrefresh) after the subscription is in place. Alternatively, register the subscriber before `openSession()` if you want an automatic refresh when the session starts.

```javascript
braze.subscribeToContentCardsUpdates((updates) => {
  const cards = updates.cards || [];
  renderCards(cards);
});

braze.requestContentCardsRefresh();
```

Define `renderCards` and any helper functions above this block in your module so they're ready when the callback runs.

### Step 4: Render cards into the inbox

Grab the list node, keep maps for impression de-duplication and card lookup, define the observer helpers, and rebuild the list whenever the SDK sends new data. For each non-control card, create an `<article>`, set `dataset.cardId`, and fill in `title`, `description`, and an optional image from [`ClassicCard`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html) fields. Clear the container on each render so you don't duplicate rows. Step 6 focuses on how visibility ties into impression logging.

```javascript
// --- DOM refs ---
const listEl = document.getElementById("cards-list");

// --- State for impression de-duping & lookup ---
const loggedImpressions = new Set();
const idToCard = new Map();
let observer = null;

// Utility: clean observer between renders
function resetObserver() {
  if (observer) observer.disconnect();
  observer = new IntersectionObserver(onIntersect, { threshold: 0.6 });
}

// Intersection callback: logs impression once when ≥60% visible
function onIntersect(entries) {
  entries.forEach((entry) => {
    if (!entry.isIntersecting) return;

    const id = entry.target.dataset.cardId;
    if (!id || loggedImpressions.has(id)) return;

    const card = idToCard.get(id);
    if (!card) return;

    // Log a single-card impression and stop observing this element
    braze.logContentCardImpressions([card]);
    loggedImpressions.add(id);
    observer.unobserve(entry.target);
  });
}

// Renders cards into the DOM, sets up click + visibility tracking
function renderCards(cards) {
  // Rebuild lookup and observer each render
  idToCard.clear();
  resetObserver();

  listEl.textContent = ""; // clear list

  cards.forEach((card) => {
    // Skip control-group cards in UI; (optional) you could log impressions for them elsewhere
    if (card.isControl) return;

    idToCard.set(card.id, card);

    const item = document.createElement("article");
    item.className = "card-item";
    item.dataset.cardId = card.id;

    const h3 = document.createElement("h3");
    h3.textContent = card.title || "";

    const p = document.createElement("p");
    p.textContent = card.description || "";

    let img = undefined;
    if (card.imageUrl) {
      img = document.createElement("img");
      img.src = card.imageUrl;
      item.append(img);
    }

    const children = [h3, p];
    if (img) {
      children.push(img);
    }
    item.append(...children);

    // Click tracking + action
    item.addEventListener("click", (e) => {
      braze.logContentCardClick(card);
      if (card.url) {
        // any url-handling logic for your use case
      }
    });

    listEl.appendChild(item);
    observer.observe(item);
  });
}
```

`resetObserver`, `onIntersect`, and the control-group guard work together with click and impression logging—the next steps break those down.

### Step 5: Handle card clicks

When someone selects a row, call [`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick) with the card instance Braze gave you. If the card carries a `url`, run your own navigation or deep-link handling after logging.

```javascript
item.addEventListener("click", (e) => {
  braze.logContentCardClick(card);
  if (card.url) {
    // any url-handling logic for your use case
  }
});
```

Logging the click records engagement in Braze even when you handle routing yourself.

### Step 6: Track impressions (IntersectionObserver)

`resetObserver` and `onIntersect` from Step 4 create an `IntersectionObserver` with a 60% visibility threshold. When a row crosses that threshold, the callback resolves the Braze card with `idToCard`, calls [`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions) once, records the id in `loggedImpressions`, and calls `unobserve` on that element. `resetObserver()` runs at the start of each `renderCards` pass so you don't watch detached nodes.

Inside `renderCards`, register each new row with the observer:

```javascript
    listEl.appendChild(item);
    observer.observe(item);
```

Tune the threshold and when you log to match your layout, scroll containers, and product rules.

### Step 7: Filter control group cards

Users assigned to a Content Card control group still receive a card object with `isControl` set to `true`. Skip rendering those rows in your inbox so the user doesn't see placeholder content. If your experiment design requires it, you can still log impressions for control cards elsewhere.

```javascript
if (card.isControl) return;
```

You can also log dismissals with [`logCardDismissal`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcarddismissal) when the user removes a card from the list.

### Putting it all together

This sample combines initialization, the inbox markup, subscriptions, rendering, clicks, impressions, and control-group handling. The preview shows a web app shell with a Message Inbox and mock cards (the editor shows the real SDK code you run in your app).

<div class="braze-tutorial-sandbox">
  <div class="braze-tutorial-sandbox-top">
    <button class="braze-tutorial-tab active" role="tab" aria-selected="true" data-tab-index="0" data-sandbox="sandbox-web-inbox-full">main.js</button>
    <button class="braze-tutorial-tab" role="tab" aria-selected="false" data-tab-index="1" data-sandbox="sandbox-web-inbox-full">index.html</button>
  </div>
  <div class="braze-tutorial-sandbox-body">
    <div class="braze-tutorial-editor" id="sandbox-web-inbox-full">
      <div class="braze-tutorial-panel active">
        <pre><code class="language-javascript">import * as braze from "@braze/web-sdk";

// Uncomment this if you'd like to run braze web SDK methods in the console
// window.braze = braze;

// initialize the Braze SDK
braze.initialize("YOUR_API_KEY", {
  baseUrl: "YOUR_API_ENDPOINT",
  enableLogging: true,
});
braze.openSession();

// --- DOM refs ---
const listEl = document.getElementById("cards-list");

// --- State for impression de-duping & lookup ---
const loggedImpressions = new Set();
const idToCard = new Map();
let observer = null;

// Utility: clean observer between renders
function resetObserver() {
  if (observer) observer.disconnect();
  observer = new IntersectionObserver(onIntersect, { threshold: 0.6 });
}

// Intersection callback: logs impression once when ≥60% visible
function onIntersect(entries) {
  entries.forEach((entry) => {
    if (!entry.isIntersecting) return;

    const id = entry.target.dataset.cardId;
    if (!id || loggedImpressions.has(id)) return;

    const card = idToCard.get(id);
    if (!card) return;

    // Log a single-card impression and stop observing this element
    braze.logContentCardImpressions([card]);
    loggedImpressions.add(id);
    observer.unobserve(entry.target);
  });
}

// Renders cards into the DOM, sets up click + visibility tracking
function renderCards(cards) {
  // Rebuild lookup and observer each render
  idToCard.clear();
  resetObserver();

  listEl.textContent = ""; // clear list

  cards.forEach((card) => {
    // Skip control-group cards in UI; (optional) you could log impressions for them elsewhere
    if (card.isControl) return;

    idToCard.set(card.id, card);

    const item = document.createElement("article");
    item.className = "card-item";
    item.dataset.cardId = card.id;

    const h3 = document.createElement("h3");
    h3.textContent = card.title || "";

    const p = document.createElement("p");
    p.textContent = card.description || "";

    let img = undefined;
    if (card.imageUrl) {
      img = document.createElement("img");
      img.src = card.imageUrl;
      item.append(img);
    }

    const children = [h3, p];
    if (img) {
      children.push(img);
    }
    item.append(...children);

    // Click tracking + action
    item.addEventListener("click", (e) => {
      braze.logContentCardClick(card);
      if (card.url) {
        // any url-handling logic for your use case
      }
    });

    listEl.appendChild(item);
    observer.observe(item);
  });
}

// Subscribe to updates *then* ask for a refresh
braze.subscribeToContentCardsUpdates((updates) => {
  const cards = updates.cards || [];
  renderCards(cards);
});

braze.requestContentCardsRefresh();</code></pre>
      </div>
      <div class="braze-tutorial-panel">
        <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;meta charset="utf-8" /&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1" /&gt;
    &lt;style&gt;
      body {
        font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial,
          sans-serif;
        margin: 0;
      }
      main {
        max-width: 720px;
        margin: 0 auto;
        padding: 16px;
      }
      h1 {
        margin: 0 0 12px;
        font-size: 24px;
      }
      .card-item {
        border-bottom: 1px solid #eee;
        padding: 12px 0;
        cursor: pointer;
      }
      .card-item h3 {
        margin: 0 0 6px;
        font-size: 16px;
      }
      .card-item p {
        margin: 0;
        color: #444;
      }
      .card-item img {
        max-width: 100%;
        height: auto;
      }
    &lt;/style&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;main id="app"&gt;
      &lt;h1&gt;Message Inbox&lt;/h1&gt;
      &lt;div id="cards-list" aria-live="polite"&gt;&lt;/div&gt;
    &lt;/main&gt;

    &lt;script type="module" src="/src/main.js"&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;</code></pre>
      </div>
    </div>
    <div class="braze-tutorial-preview">
      <div class="braze-tutorial-preview-bar">Result</div>
      <iframe id="braze-preview-web-inbox-full" class="braze-tutorial-iframe" title="Content Card inbox preview"></iframe>
    </div>
  </div>
</div>

The `enableLogging` flag is optional. It helps during development; remove it for production builds.

### Next steps

- [About Content Cards]({{site.baseurl}}/developer_guide/content_cards/) — card types, use cases, and how feeds sync.
- [Logging analytics for Content Cards]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/) — impressions, clicks, dismissals, and custom handling.
- [Web SDK reference](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html) — full API documentation for Content Card methods.

{% raw %}
<script>
(function() {
  function initBrazeTutorial() {
    document.querySelectorAll('.braze-tutorial-tab').forEach(function(tab) {
      tab.addEventListener('click', function() {
        var sandboxId = this.getAttribute('data-sandbox');
        if (!sandboxId) return;
        var editor = document.getElementById(sandboxId);
        if (!editor) return;
        var tabIndex = parseInt(this.getAttribute('data-tab-index'), 10);
        var allTabs = this.parentElement.querySelectorAll('.braze-tutorial-tab');
        var allPanels = editor.querySelectorAll('.braze-tutorial-panel');
        allTabs.forEach(function(t, i) {
          var isActive = i === tabIndex;
          t.classList.toggle('active', isActive);
          t.setAttribute('aria-selected', isActive ? 'true' : 'false');
        });
        allPanels.forEach(function(p, i) {
          p.classList.toggle('active', i === tabIndex);
        });
      });
    });

    document.querySelectorAll('.highlight td.gl, .highlight td.gutter, .highlight .gutter, .highlight .lineno, td.gl, td.gutter').forEach(function(el) {
      el.remove();
    });

    if (typeof hljs !== 'undefined') {
      document.querySelectorAll('.braze-tutorial-editor code').forEach(function(block) {
        hljs.highlightElement(block);
      });
    }

    var sharedStyles = '* { box-sizing: border-box; margin: 0; padding: 0; }' +
      'body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #f8f9fa; color: #1B2536; }' +
      '.app-nav { background: #1B2536; color: #fff; padding: 10px 20px; display: flex; align-items: center; }' +
      '.app-nav-brand { font-weight: 700; font-size: 15px; }' +
      '.app-nav-links { margin-left: auto; display: flex; gap: 18px; }' +
      '.app-nav-links a { color: rgba(255,255,255,0.75); text-decoration: none; font-size: 13px; }' +
      '.app-content { padding: 20px; max-width: 720px; margin: 0 auto; }' +
      'h2.page-title { font-size: 20px; font-weight: 700; margin-bottom: 14px; }' +
      '.card-item { border-bottom: 1px solid #eee; padding: 12px 0; cursor: pointer; }' +
      '.card-item h3 { margin: 0 0 6px; font-size: 16px; font-weight: 700; }' +
      '.card-item p { margin: 0; color: #444; font-size: 14px; line-height: 1.5; }';

    var navBar = '<div class="app-nav">' +
      '<span class="app-nav-brand">MyApp</span>' +
      '<nav class="app-nav-links">' +
      '<a href="javascript:void(0)">Home</a><a href="javascript:void(0)">Products</a><a href="javascript:void(0)">About</a>' +
      '</nav></div>';

    var cardArticle = function(title, desc) {
      return '<article class="card-item">' +
        '<h3>' + title + '</h3>' +
        '<p>' + desc + '</p>' +
        '</article>';
    };

    var inboxFullPreview = '<!DOCTYPE html><html><head><meta charset="utf-8"/><style>' + sharedStyles +
      '</style></head><body>' +
      navBar +
      '<div class="app-content">' +
      '<h2 class="page-title">Message Inbox</h2>' +
      cardArticle('Welcome to Braze!', 'Thanks for installing our app. Check out these features.') +
      cardArticle('Flash Sale This Weekend', 'Save up to 40% on select items. Shop the sale before it ends!') +
      cardArticle('New Feature: Dark Mode', 'Try our new dark mode for a better experience at night.') +
      cardArticle('Weekly Newsletter', 'Read this week\'s top stories and updates from our team.') +
      '</div></body></html>';

    var previews = {
      'braze-preview-web-inbox-full': inboxFullPreview
    };

    function forcePopulatePreviews() {
      Object.keys(previews).forEach(function(id) {
        var iframe = document.getElementById(id);
        if (iframe) {
          iframe.srcdoc = previews[id];
        }
      });
    }

    forcePopulatePreviews();
    setTimeout(forcePopulatePreviews, 300);
    setTimeout(forcePopulatePreviews, 1000);

    document.querySelectorAll('.tab_toggle, .sdk-tab_toggle').forEach(function(toggle) {
      toggle.addEventListener('click', function() {
        setTimeout(forcePopulatePreviews, 150);
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initBrazeTutorial);
  } else {
    initBrazeTutorial();
  }
})();
</script>
{% endraw %}
