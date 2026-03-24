{% multi_lang_include developer_guide/prerequisites/android.md %}

## Making an inbox with Content Cards for Android

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Content Card Inbox Android" %}

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
/* Framework tab spacing (Compose / RecyclerView tabs) */
.ab-nav.ab-nav-tabs {
  padding-left: 8px !important;
}
.ab-nav-tabs .coderow a.tab_toggle {
  padding: 10px 16px !important;
}
.ab-tab-pane {
  padding: 0 20px !important;
}
</style>

<div class="braze-tutorial-intro">
  <p>This tutorial walks you through building a custom Content Card inbox on Android with the Braze SDK. You can follow the <strong>Compose</strong> path with Jetpack Compose or the <strong>RecyclerView</strong> path with XML layouts and a <code>RecyclerView</code>. Each section introduces a concept, shows the code, and explains how the pieces connect. Select the tab that matches your UI framework.</p>
</div>

<div class="braze-learn-box">
  <h4>You will learn how to</h4>
  <ul>
    <li>Configure the Braze SDK in your <code>Application</code> class with <code>BrazeConfig</code></li>
    <li>Optionally enable verbose logging with <code>BrazeLogger.enableVerboseLogging()</code> during development</li>
    <li>Subscribe to Content Card updates and request a refresh</li>
    <li>Build an inbox list UI with Jetpack Compose or a <code>RecyclerView</code></li>
    <li>Render card titles and descriptions for common Content Card types</li>
    <li>Log impressions and clicks with <code>logImpression()</code> and <code>logClick()</code></li>
  </ul>
</div>

### Step 1: Configure the Braze SDK

In your `Application` class, build a `BrazeConfig` with your API key and SDK endpoint, then pass it to `Braze.configure()`. The SDK initializes once for the whole app process.

```kotlin
import android.app.Application
import com.braze.Braze
import com.braze.configuration.BrazeConfig

class ContentCardsApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Configure Braze with your SDK key & endpoint
        val config = BrazeConfig.Builder()
            .setApiKey("YOUR_API_KEY")
            .setCustomEndpoint("YOUR_API_ENDPOINT")
            .build()
        Braze.configure(this, config)
    }
}
```

`Braze.configure()` must run before you call other Braze APIs (for example, subscribing to Content Cards). Register this `Application` subclass in your `AndroidManifest.xml` if it is not already registered.

### Step 2: Enable debugging (optional)

To make troubleshooting easier while developing, turn on verbose Braze logging at the start of `onCreate()`:

```kotlin
import com.braze.support.BrazeLogger

// In onCreate(), before or after configure:
BrazeLogger.enableVerboseLogging()
```

Verbose logs appear in Logcat and include SDK network and sync details. Remove this call before you ship to production.

{% tabs %}
{% tab Compose %}

### Step 3: Subscribe to Content Card updates

Use a [`DisposableEffect`](https://developer.android.com/develop/ui/compose/side-effects#disposableeffect) so you subscribe when the composable enters composition and remove the subscription when it leaves. Call `subscribeToContentCardsUpdates()` with an `IEventSubscriber` that updates your local list, then call `requestContentCardsRefresh(false)` to fetch cards.

```kotlin
DisposableEffect(Unit) {
    val subscriber = IEventSubscriber<ContentCardsUpdatedEvent> { event ->
        cards = event.allCards.filter { !it.isControl }
    }

    Braze.getInstance(context).subscribeToContentCardsUpdates(subscriber)
    Braze.getInstance(context).requestContentCardsRefresh(false)

    onDispose {
        Braze.getInstance(context)
            .removeSingleSubscription(subscriber, ContentCardsUpdatedEvent::class.java)
    }
}
```

Filtering with `!it.isControl` skips control cards so they do not appear in your custom UI. `removeSingleSubscription()` in `onDispose` prevents leaks when the screen is destroyed.

### Step 4: Build the inbox UI

Use a [`LazyColumn`](https://developer.android.com/develop/ui/compose/lists#lazy) inside a `Column` for a scrollable inbox. Add a header `Text` for the screen title, then list each card with `items()` and a stable `key` from `card.id`.

```kotlin
Column(modifier = Modifier.fillMaxSize()) {
    Text(
        text = "Message Inbox",
        fontSize = 20.sp,
        fontWeight = FontWeight.Bold,
        modifier = Modifier.padding(start = 16.dp, end = 16.dp, top = 12.dp, bottom = 8.dp)
    )

    LazyColumn(
        modifier = Modifier
            .fillMaxSize()
            .padding(horizontal = 16.dp)
    ) {
        items(cards, key = { it.id }) { card ->
            ContentCardItem(
                card = card,
                onImpression = {
                    if (!loggedImpressions.contains(card.id)) {
                        card.logImpression()
                        loggedImpressions.add(card.id)
                    }
                },
                onClick = {
                    card.logClick()
                    card.url?.let {
                        context.startActivity(Intent(Intent.ACTION_VIEW, Uri.parse(it)))
                    }
                }
            )
        }
    }
}
```

`remember { mutableStateOf<List<Card>>(emptyList()) }` holds the card list at the composable level, and `remember { mutableSetOf<String>() }` tracks which card IDs already logged an impression.

### Step 5: Create a Content Card item

Define a `ContentCardItem` composable that reads `title` and `description` from [`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) subtypes (`CaptionedImageCard`, `ShortNewsCard`, `TextAnnouncementCard`). Use Material3 `Card` and `Column` for layout, and `Modifier.clickable` to handle taps.

```kotlin
@Composable
fun ContentCardItem(
    card: Card,
    onImpression: () -> Unit,
    onClick: () -> Unit
) {
    // Log impression when the card becomes visible
    LaunchedEffect(card.id) {
        onImpression()
    }

    val title = when (card) {
        is CaptionedImageCard -> card.title
        is ShortNewsCard -> card.title
        is TextAnnouncementCard -> card.title
        else -> null
    }
    val description = when (card) {
        is CaptionedImageCard -> card.description
        is ShortNewsCard -> card.description
        is TextAnnouncementCard -> card.description
        else -> null
    }

    Card(
        modifier = Modifier
            .fillMaxWidth()
            .padding(vertical = 4.dp)
            .clickable { onClick() }
    ) {
        Column(modifier = Modifier.padding(16.dp)) {
            title?.let {
                Text(
                    text = it,
                    fontWeight = FontWeight.Bold,
                    fontSize = 16.sp
                )
            }
            description?.let {
                Spacer(modifier = Modifier.height(4.dp))
                Text(
                    text = it,
                    fontSize = 14.sp
                )
            }
        }
    }
}
```

Extend the `when` branches if you support additional card types. The composable stays presentation-focused; navigation and analytics stay in the parent via lambdas.

### Step 6: Track impressions and clicks

Log impressions with [`logImpression()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html) and clicks with [`logClick()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html). `LaunchedEffect(card.id)` runs when each item enters composition so you can treat that as the visibility signal for impressions, while the `items` callback deduplicates with `loggedImpressions`.

```kotlin
// Inside ContentCardItem — fires when the card enters composition
LaunchedEffect(card.id) {
    onImpression()
}

// In the LazyColumn items { } block — guard so each card logs at most once
onImpression = {
    if (!loggedImpressions.contains(card.id)) {
        card.logImpression()
        loggedImpressions.add(card.id)
    }
},
onClick = {
    card.logClick()
    card.url?.let {
        context.startActivity(Intent(Intent.ACTION_VIEW, Uri.parse(it)))
    }
}
```

Impression semantics depend on your product and view lifecycle. If users scroll quickly, consider stricter visibility detection (for example, `LazyListState` and item visibility) instead of composition alone.


### Putting it all together

The sandbox lists `MainApplication.kt` and `ContentCardsInboxScreen.kt`. The preview is a static phone mockup of the inbox, not a running Android UI.

<div class="braze-tutorial-sandbox">
  <div class="braze-tutorial-sandbox-top">
    <button class="braze-tutorial-tab active" role="tab" aria-selected="true" data-tab-index="0" data-sandbox="sandbox-android-compose-full">MainApplication.kt</button>
    <button class="braze-tutorial-tab" role="tab" aria-selected="false" data-tab-index="1" data-sandbox="sandbox-android-compose-full">ContentCardsInboxScreen.kt</button>
  </div>
  <div class="braze-tutorial-sandbox-body">
    <div class="braze-tutorial-editor" id="sandbox-android-compose-full">
      <div class="braze-tutorial-panel active">
        <pre><code class="language-kotlin">import android.app.Application
import com.braze.Braze
import com.braze.support.BrazeLogger
import com.braze.configuration.BrazeConfig
import android.util.Log

class ContentCardsApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Turn on verbose Braze logging
        BrazeLogger.enableVerboseLogging()

        // Configure Braze with your SDK key & endpoint
        val config = BrazeConfig.Builder()
            .setApiKey("YOUR_API_KEY")
            .setCustomEndpoint("YOUR_API_ENDPOINT")
            .build()
        Braze.configure(this, config)
    }
}</code></pre>
      </div>
      <div class="braze-tutorial-panel">
        <pre><code class="language-kotlin">import android.content.Intent
import android.net.Uri
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.braze.Braze
import com.braze.events.ContentCardsUpdatedEvent
import com.braze.events.IEventSubscriber
import com.braze.models.cards.*

@Composable
fun ContentCardInboxScreen() {
    val context = LocalContext.current
    var cards by remember { mutableStateOf&lt;List&lt;Card&gt;&gt;(emptyList()) }
    val loggedImpressions = remember { mutableSetOf&lt;String&gt;() }

    DisposableEffect(Unit) {
        val subscriber = IEventSubscriber&lt;ContentCardsUpdatedEvent&gt; { event ->
            cards = event.allCards.filter { !it.isControl }
        }

        Braze.getInstance(context).subscribeToContentCardsUpdates(subscriber)
        Braze.getInstance(context).requestContentCardsRefresh(false)

        onDispose {
            Braze.getInstance(context)
                .removeSingleSubscription(subscriber, ContentCardsUpdatedEvent::class.java)
        }
    }

    Column(modifier = Modifier.fillMaxSize()) {
        Text(
            text = "Message Inbox",
            fontSize = 20.sp,
            fontWeight = FontWeight.Bold,
            modifier = Modifier.padding(start = 16.dp, end = 16.dp, top = 12.dp, bottom = 8.dp)
        )

        LazyColumn(
            modifier = Modifier
                .fillMaxSize()
                .padding(horizontal = 16.dp)
        ) {
            items(cards, key = { it.id }) { card ->
                ContentCardItem(
                    card = card,
                    onImpression = {
                        if (!loggedImpressions.contains(card.id)) {
                            card.logImpression()
                            loggedImpressions.add(card.id)
                        }
                    },
                    onClick = {
                        card.logClick()
                        card.url?.let {
                            context.startActivity(Intent(Intent.ACTION_VIEW, Uri.parse(it)))
                        }
                    }
                )
            }
        }
    }
}

@Composable
fun ContentCardItem(
    card: Card,
    onImpression: () -> Unit,
    onClick: () -> Unit
) {
    // Log impression when the card becomes visible
    LaunchedEffect(card.id) {
        onImpression()
    }

    val title = when (card) {
        is CaptionedImageCard -> card.title
        is ShortNewsCard -> card.title
        is TextAnnouncementCard -> card.title
        else -> null
    }
    val description = when (card) {
        is CaptionedImageCard -> card.description
        is ShortNewsCard -> card.description
        is TextAnnouncementCard -> card.description
        else -> null
    }

    Card(
        modifier = Modifier
            .fillMaxWidth()
            .padding(vertical = 4.dp)
            .clickable { onClick() }
    ) {
        Column(modifier = Modifier.padding(16.dp)) {
            title?.let {
                Text(
                    text = it,
                    fontWeight = FontWeight.Bold,
                    fontSize = 16.sp
                )
            }
            description?.let {
                Spacer(modifier = Modifier.height(4.dp))
                Text(
                    text = it,
                    fontSize = 14.sp
                )
            }
        }
    }
}</code></pre>
      </div>
    </div>
    <div class="braze-tutorial-preview">
      <div class="braze-tutorial-preview-bar">Result</div>
      <iframe id="braze-preview-android-compose-full" class="braze-tutorial-iframe" title="Jetpack Compose Content Card inbox preview"></iframe>
    </div>
  </div>
</div>

`BrazeLogger.enableVerboseLogging()` in `MainApplication.kt` is optional. Remove it before you deploy to production.

{% endtab %}
{% tab RecyclerView %}

### Step 3: Create the XML layout

Use a vertical `LinearLayout` with a header `TextView` and a [`RecyclerView`](https://developer.android.com/develop/ui/views/layout/recyclerview). The recycler uses `layout_weight` so it fills the space below the header.

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
        android:orientation="vertical"
        android:layout_width="match_parent"
        android:layout_height="match_parent">

        <TextView
            android:id="@+id/inboxHeader"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="Message Inbox"
            android:textStyle="bold"
            android:textSize="20sp"
            android:paddingStart="16dp"
            android:paddingEnd="16dp"
            android:paddingTop="12dp"
            android:paddingBottom="8dp" />

        <androidx.recyclerview.widget.RecyclerView
            android:id="@+id/contentCardsRecyclerView"
            android:layout_width="match_parent"
            android:layout_height="0dp"
            android:layout_weight="1" />
    </LinearLayout>
```

Inflate this layout in your activity with `setContentView(R.layout.content_card_inbox)`.

### Step 4: Subscribe to Content Card updates

Create an `IEventSubscriber<ContentCardsUpdatedEvent>` that updates a `MutableList<Card>` on the main thread and notifies the adapter. Register the subscriber in `onStart()` and remove it in `onStop()` with `removeSingleSubscription()` so you do not leak the activity.

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    setContentView(R.layout.content_card_inbox)

    recyclerView = findViewById(R.id.contentCardsRecyclerView)
    recyclerView.layoutManager = LinearLayoutManager(this)
    recyclerView.adapter = adapter

    // Prepare the subscriber (attach/detach in onStart/onStop)
    subscriber = IEventSubscriber { event ->
        runOnUiThread {
            cards.clear()
            cards.addAll(event.allCards.filter { !it.isControl })
            adapter.notifyDataSetChanged()
        }
    }
}

override fun onStart() {
    super.onStart()
    subscriber?.let {
        Braze.getInstance(this).subscribeToContentCardsUpdates(it)
    }
    // Fetch fresh cards
    Braze.getInstance(this).requestContentCardsRefresh(false)
}

override fun onStop() {
    // Avoid leaks by removing the subscription when not visible
    Braze.getInstance(this)
        .removeSingleSubscription(subscriber, ContentCardsUpdatedEvent::class.java)
    super.onStop()
}
```

`requestContentCardsRefresh(false)` runs each time the activity becomes visible so the list stays up to date.

### Step 5: Build the RecyclerView adapter

Subclass `RecyclerView.Adapter` with a `ViewHolder` that holds title and description `TextView`s. This example inflates `android.R.layout.simple_list_item_2` for a quick two-line row; you can replace it with a custom layout when you polish the design.

```kotlin
inner class ContentCardAdapter :
    RecyclerView.Adapter<ContentCardAdapter.CardViewHolder>() {

    inner class CardViewHolder(v: View) : RecyclerView.ViewHolder(v) {
        val title: TextView = v.findViewById(android.R.id.text1)
        val description: TextView = v.findViewById(android.R.id.text2)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): CardViewHolder {
        val view = LayoutInflater.from(parent.context)
            .inflate(android.R.layout.simple_list_item_2, parent, false)
        return CardViewHolder(view)
    }

    override fun getItemCount() = cards.size

    override fun onBindViewHolder(holder: CardViewHolder, position: Int) {
        val card = cards[position]

        val title = when (card) {
            is CaptionedImageCard -> card.title
            is ShortNewsCard -> card.title
            is TextAnnouncementCard -> card.title
            else -> null
        }
        val description = when (card) {
            is CaptionedImageCard -> card.description
            is ShortNewsCard -> card.description
            is TextAnnouncementCard -> card.description
            else -> null
        }

        holder.title.text = title.orEmpty()
        holder.description.text = description.orEmpty()

        // Naive impression guard: only log the first time we bind a not-yet-viewed card.
        if (!card.viewed) card.logImpression()

        holder.itemView.setOnClickListener {
            card.logClick()
            card.url?.let { startActivity(Intent(Intent.ACTION_VIEW, Uri.parse(it))) }
        }
    }
}
```

Declare `adapter` as a property on the activity (for example, `private val adapter = ContentCardAdapter()`) so `onCreate` can assign it to the `RecyclerView`.

### Step 6: Track impressions and clicks

In `onBindViewHolder`, call [`logImpression()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html) when the card has not been marked viewed, and [`logClick()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html) inside `setOnClickListener` before opening a URL.

```kotlin
        // Naive impression guard: only log the first time we bind a not-yet-viewed card.
        if (!card.viewed) card.logImpression()

        holder.itemView.setOnClickListener {
            card.logClick()
            card.url?.let { startActivity(Intent(Intent.ACTION_VIEW, Uri.parse(it))) }
        }
```

Binding-based impressions are a simple starting point. For stricter “visible on screen” rules, combine `RecyclerView` scroll listeners or view attachment callbacks with your analytics policy.


### Putting it all together

The sandbox lists `MainApplication.kt`, `ContentCardInboxActivity.kt`, and `content_card_inbox.xml`. The preview is a static phone mockup of the inbox.

<div class="braze-tutorial-sandbox">
  <div class="braze-tutorial-sandbox-top">
    <button class="braze-tutorial-tab active" role="tab" aria-selected="true" data-tab-index="0" data-sandbox="sandbox-android-rv-full">MainApplication.kt</button>
    <button class="braze-tutorial-tab" role="tab" aria-selected="false" data-tab-index="1" data-sandbox="sandbox-android-rv-full">ContentCardInboxActivity.kt</button>
    <button class="braze-tutorial-tab" role="tab" aria-selected="false" data-tab-index="2" data-sandbox="sandbox-android-rv-full">content_card_inbox.xml</button>
  </div>
  <div class="braze-tutorial-sandbox-body">
    <div class="braze-tutorial-editor" id="sandbox-android-rv-full">
      <div class="braze-tutorial-panel active">
        <pre><code class="language-kotlin">import android.app.Application
import com.braze.Braze
import com.braze.support.BrazeLogger
import com.braze.configuration.BrazeConfig
import android.util.Log

class ContentCardsApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Turn on verbose Braze logging
        BrazeLogger.enableVerboseLogging()

        // Configure Braze with your SDK key & endpoint
        val config = BrazeConfig.Builder()
            .setApiKey("YOUR_API_KEY")
            .setCustomEndpoint("YOUR_API_ENDPOINT")
            .build()
        Braze.configure(this, config)
    }
}</code></pre>
      </div>
      <div class="braze-tutorial-panel">
        <pre><code class="language-kotlin">import android.content.Intent
import android.net.Uri
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import android.view.*
import android.widget.TextView
import com.braze.Braze
import com.braze.events.ContentCardsUpdatedEvent
import com.braze.events.IEventSubscriber
import com.braze.models.cards.*

class ContentCardsActivity : ComponentActivity() {
    private val cards = mutableListOf&lt;Card&gt;()
    private var subscriber: IEventSubscriber&lt;ContentCardsUpdatedEvent&gt;? = null
    private lateinit var recyclerView: RecyclerView
    private val adapter = ContentCardAdapter()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.content_card_inbox)

        recyclerView = findViewById(R.id.contentCardsRecyclerView)
        recyclerView.layoutManager = LinearLayoutManager(this)
        recyclerView.adapter = adapter

        // Prepare the subscriber (attach/detach in onStart/onStop)
        subscriber = IEventSubscriber { event ->
            runOnUiThread {
                cards.clear()
                cards.addAll(event.allCards.filter { !it.isControl })
                adapter.notifyDataSetChanged()
            }
        }
    }

    override fun onStart() {
        super.onStart()
        subscriber?.let {
            Braze.getInstance(this).subscribeToContentCardsUpdates(it)
        }
        // Fetch fresh cards
        Braze.getInstance(this).requestContentCardsRefresh(false)
    }

    override fun onStop() {
        // Avoid leaks by removing the subscription when not visible
        Braze.getInstance(this)
            .removeSingleSubscription(subscriber, ContentCardsUpdatedEvent::class.java)
        super.onStop()
    }

    inner class ContentCardAdapter :
        RecyclerView.Adapter&lt;ContentCardAdapter.CardViewHolder&gt;() {

        inner class CardViewHolder(v: View) : RecyclerView.ViewHolder(v) {
            val title: TextView = v.findViewById(android.R.id.text1)
            val description: TextView = v.findViewById(android.R.id.text2)
        }

        override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): CardViewHolder {
            val view = LayoutInflater.from(parent.context)
                .inflate(android.R.layout.simple_list_item_2, parent, false)
            return CardViewHolder(view)
        }

        override fun getItemCount() = cards.size

        override fun onBindViewHolder(holder: CardViewHolder, position: Int) {
            val card = cards[position]

            val title = when (card) {
                is CaptionedImageCard -> card.title
                is ShortNewsCard -> card.title
                is TextAnnouncementCard -> card.title
                else -> null
            }
            val description = when (card) {
                is CaptionedImageCard -> card.description
                is ShortNewsCard -> card.description
                is TextAnnouncementCard -> card.description
                else -> null
            }

            holder.title.text = title.orEmpty()
            holder.description.text = description.orEmpty()

            // Naive impression guard: only log the first time we bind a not-yet-viewed card.
            if (!card.viewed) card.logImpression()

            holder.itemView.setOnClickListener {
                card.logClick()
                card.url?.let { startActivity(Intent(Intent.ACTION_VIEW, Uri.parse(it))) }
            }
        }
    }
}</code></pre>
      </div>
      <div class="braze-tutorial-panel">
        <pre><code class="language-xml">&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
        android:orientation="vertical"
        android:layout_width="match_parent"
        android:layout_height="match_parent"&gt;

        &lt;TextView
            android:id="@+id/inboxHeader"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="Message Inbox"
            android:textStyle="bold"
            android:textSize="20sp"
            android:paddingStart="16dp"
            android:paddingEnd="16dp"
            android:paddingTop="12dp"
            android:paddingBottom="8dp" /&gt;

        &lt;androidx.recyclerview.widget.RecyclerView
            android:id="@+id/contentCardsRecyclerView"
            android:layout_width="match_parent"
            android:layout_height="0dp"
            android:layout_weight="1" /&gt;
    &lt;/LinearLayout&gt;</code></pre>
      </div>
    </div>
    <div class="braze-tutorial-preview">
      <div class="braze-tutorial-preview-bar">Result</div>
      <iframe id="braze-preview-android-rv-full" class="braze-tutorial-iframe" title="RecyclerView Content Card inbox preview"></iframe>
    </div>
  </div>
</div>

`BrazeLogger.enableVerboseLogging()` in `MainApplication.kt` is optional. Remove it before you deploy to production.

{% endtab %}
{% endtabs %}

### Next steps

- [About Content Cards]({{site.baseurl}}/developer_guide/content_cards/) — how Content Cards work across channels and use cases.
- [Customizing Content Cards]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/) — feed, UI, and click handling options.
- [Android SDK reference](https://braze-inc.github.io/braze-android-sdk/kdoc/) — full API documentation for Content Cards.

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

    var phoneStyles = '* { box-sizing: border-box; margin: 0; padding: 0; }' +
      'body { font-family: Roboto, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; background: #f5f7f9; padding: 12px; }' +
      '.phone { max-width: 300px; margin: 0 auto; border-radius: 28px; overflow: hidden; border: 3px solid #1B2536; box-shadow: 0 8px 30px rgba(0,0,0,0.12); }' +
      '.phone-status { background: #1B2536; color: rgba(255,255,255,0.7); padding: 4px 20px; font-size: 10px; display: flex; justify-content: space-between; }' +
      '.phone-header { background: #fff; color: #1B2536; padding: 14px 16px; font-weight: 700; font-size: 17px; border-bottom: 1px solid #e2e8f0; }' +
      '.phone-body { background: #f1f5f9; padding: 12px 12px 20px; min-height: 320px; }' +
      '.ccard { background: #fff; border-radius: 10px; padding: 14px 16px; margin-bottom: 10px; box-shadow: 0 1px 3px rgba(0,0,0,0.08), 0 1px 2px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; }' +
      '.ccard-title { font-weight: 700; font-size: 15px; color: #1B2536; margin-bottom: 6px; line-height: 1.3; }' +
      '.ccard-desc { font-size: 13px; color: #64748b; line-height: 1.45; }' +
      '.ccard-link { margin-top: 10px; font-size: 12px; }' +
      '.ccard-link a { color: #00B3E6; font-weight: 600; text-decoration: none; }';

    function inboxCard(title, desc, showLink) {
      var link = showLink
        ? '<div class="ccard-link"><a href="javascript:void(0)">View details</a></div>'
        : '';
      return '<div class="ccard"><div class="ccard-title">' + title + '</div><div class="ccard-desc">' + desc + '</div>' + link + '</div>';
    }

    var inboxPreview = '<!DOCTYPE html><html><head><style>' + phoneStyles + '</style></head><body>' +
      '<div class="phone">' +
      '<div class="phone-status"><span>9:41</span><span>LTE</span></div>' +
      '<div class="phone-header">Message Inbox</div>' +
      '<div class="phone-body">' +
      inboxCard('Welcome to Braze!', 'Thanks for installing our app.', true) +
      inboxCard('Flash Sale This Weekend', 'Save up to 40% on select items.', true) +
      inboxCard('New Feature: Dark Mode', 'Try our new dark mode setting.', true) +
      '</div></div></body></html>';

    var previews = {
      'braze-preview-android-compose-full': inboxPreview,
      'braze-preview-android-rv-full': inboxPreview
    };

    function forcePopulatePreviews() {
      var allPopulated = true;
      Object.keys(previews).forEach(function(id) {
        var iframe = document.getElementById(id);
        if (iframe) {
          iframe.srcdoc = previews[id];
        } else {
          allPopulated = false;
        }
      });
      return allPopulated;
    }

    forcePopulatePreviews();

    var pollCount = 0;
    var pollInterval = setInterval(function() {
      forcePopulatePreviews();
      pollCount++;
      if (pollCount >= 30) {
        clearInterval(pollInterval);
      }
    }, 500);

    document.addEventListener('click', function(e) {
      var target = e.target;
      if (!(target instanceof Element) && target && target.parentElement) {
        target = target.parentElement;
      }
      if (!(target instanceof Element)) {
        return;
      }
      if (target.classList.contains('tab_toggle') ||
          target.classList.contains('sdk-tab_toggle') ||
          target.classList.contains('sdk-tab_toggle_only') ||
          target.closest('.ab-nav-tabs') ||
          target.closest('.sdk-ab-nav-tabs') ||
          target.closest('.braze-tutorial-tab')) {
        setTimeout(forcePopulatePreviews, 100);
        setTimeout(forcePopulatePreviews, 300);
        setTimeout(forcePopulatePreviews, 600);
      }
    }, true);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initBrazeTutorial);
  } else {
    initBrazeTutorial();
  }
})();
</script>
{% endraw %}
