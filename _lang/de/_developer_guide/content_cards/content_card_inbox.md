---
nav_title: "Anleitung: Content-Card-Posteingänge"
article_title: "Anleitung: Einen Posteingang mit Content-Cards erstellen"
description: ""
page_order: 6
layout: scrolly
---

# Anleitung: Einen Posteingang mit Content-Cards erstellen

> Folgen Sie dem Beispielcode in diesem Tutorial, um einen Posteingang mit Braze Content-Cards zu erstellen.

{% sdktabs %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %}

## Erstellen eines Posteingangs mit Content-Cards für Android (Compose)

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md %}

{% scrolly %}

```kotlin file=MainApplication.kt
import android.app.Application
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
}
```

```kotlin file=ContentCardsInboxScreen.kt
import android.content.Intent
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
    var cards by remember { mutableStateOf<List<Card>>(emptyList()) }
    val loggedImpressions = remember { mutableSetOf<String>() }

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
}
```

!Schritt
Zeilen-MainApplication.kt=12

#### 1\. Enablement von Fehlersuchen (optional)

Um die Fehlerbehebung während der Entwicklung zu erleichtern, sollten Sie das Debugging aktivieren.

!Schritt
Zeilen-ContentCardsInboxScreen.kt=47-69

#### 2\. Eine UI-Ansicht erstellen

Für Jetpack Compose verwenden Sie ein [`LazyColumn`](<https://developer.android.com/develop/ui/compose/lists#lazy>) um Content-Cards in einer scrollbaren Liste anzuzeigen.

!Schritt
Zeilen-ContentCardsInboxScreen.kt=25-37

#### 3\. Updates für Content-Cards abonnieren

Verwenden Sie eine [`DisposableEffect`](<https://developer.android.com/develop/ui/compose/side-effects#disposableeffect>) um den Lebenszyklus des Abos zu verwalten und eine ordnungsgemäße Bereinigung sicherzustellen, wenn das Composable die Komposition verlässt.

!Schritt
Zeilen-ContentCardsInboxScreen.kt=84-95

#### 4\. Erstellen Sie ein angepasstes UI für den Posteingang

Mit den [Attributen für](<https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html>) Content-Cards wie `title`, `description` und `url` können Sie Content-Cards erstellen, die Ihren spezifischen UI-Anforderungen entsprechen. In diesem Fall erstellen wir einen Posteingang mit den Composables `Card` und `Column` von Jetpack Compose.

!Schritt
Zeilen-ContentCardsInboxScreen.kt=57,62

#### 5\. Tracking von Impressionen und Klicks

Sie können Impressionen und Klicks protokollieren, indem Sie die [`logImpressions`](<https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html>) und [`logClick`](<https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html>) die für Content-Cards verfügbar sind.

Impressionen sollten nur einmal protokolliert werden, wenn der Nutzer:innen eine Karte ansieht. Verwenden Sie `LaunchedEffect`, um Impressionen zu protokollieren, wenn eine Karte sichtbar wird. Beachten Sie, dass Sie möglicherweise den Lebenszyklus Ihrer App sowie den Anwendungsfall berücksichtigen müssen, um sicherzustellen, dass Impressionen korrekt protokolliert werden.

{% endscrolly %}

## Erstellen eines Posteingangs mit Content-Cards für Android (RecyclerView)

{% scrolly %}

```kotlin file=MainApplication.kt
import android.app.Application
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
}
```

```kotlin file=ContentCardInboxActivity.kt
import android.content.Intent
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
    private val cards = mutableListOf<Card>()
    private var subscriber: IEventSubscriber<ContentCardsUpdatedEvent>? = null
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
}
```

```xml file=content_card_inbox.xml
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

!Schritt
Zeilen-MainApplication.kt=12

#### 1\. Enablement von Fehlersuchen (optional)

Um die Fehlerbehebung während der Entwicklung zu erleichtern, sollten Sie das Debugging aktivieren.

!Schritt
lines-content_card_inbox.xml=1-24

#### 2\. Eine UI-Ansicht erstellen

In diesem Lernprogramm verwenden wir die Android [`RecyclerView`](<https://developer.android.com/develop/ui/views/layout/recyclerview>) zur Anzeige von Content-Cards, aber wir empfehlen, ein UI mit Klassen und Komponenten zu erstellen, das Ihrem Anwendungsfall entspricht. Braze stellt das UI standardmäßig zur Verfügung, aber in diesem Tutorial erfahren Sie, wie Sie eine angepasste Ansicht erstellen, um das Aussehen und Verhalten anzupassen.

!Schritt
Zeilen-ContentCardInboxActivity.kt=29-35,40-42,44

#### 3\. Updates für Content-Cards abonnieren

Verwenden Sie [`subscribeToContentCardsUpdates`](<https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-content-cards-updates.html?query=abstract%20fun%20subscribeToContentCardsUpdates(subscriber:%20IEventSubscriber%3CContentCardsUpdatedEvent%3E)>) um zuzulassen, dass Ihr UI reagiert, wenn neue Content-Cards verfügbar sind. Hier werden Abonnent:innen im Rahmen der Aktivitäts-Lebenszyklus-Haken registriert und entfernt.

!Schritt
Zeilen-ContentCardInboxActivity.kt=73-84

#### 4\. Erstellen Sie ein angepasstes UI für den Posteingang

Mit den [Content-Card-Attributen](<https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html>) wie `title`, `description` und `url` können Sie Content-Cards erstellen, die Ihren spezifischen UI-Anforderungen entsprechen. In diesem Fall bauen wir einen Posteingang mit dem nativen Android `RecyclerView` auf.

!Schritt
Zeilen-ContentCardInboxActivity.kt=90,93

#### 5\. Tracking von Impressionen und Klicks

Sie können Impressionen und Klicks protokollieren, indem Sie die [`logImpressions`](<https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html>) und [`logClick`](<https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html>) die für Content-Cards verfügbar sind.

Impressionen sollten nur einmal protokolliert werden, wenn der Nutzer:innen eine Karte ansieht. Hier verwenden wir einen naiven Mechanismus zum Schutz vor doppelten Protokollen mit einem Flag pro Karte. Beachten Sie, dass Sie möglicherweise den Lebenszyklus Ihrer App sowie den Anwendungsfall berücksichtigen müssen, um sicherzustellen, dass Impressionen korrekt protokolliert werden.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} Sie müssen auch [In-App-Nachrichten für Swift aktivieren]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=swift#swift_enabling-in-app-messages).

## Erstellen eines Posteingangs mit Content-Cards für Swift

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md %}

{% scrolly %}

```swift file=AppDelegate.swift
import SwiftUI
import BrazeKit
import BrazeUI

class AppDelegate: UIResponder, UIApplicationDelegate {
    static var braze: Braze!

    func application(
      _ application: UIApplication,
      didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {

        // Braze configuration with your SDK API key and endpoint
        let configuration = Braze.Configuration(apiKey: "YOUR_API_ENDPOINT", endpoint: "YOUR_API_KEY")
        configuration.logger.level = .debug

        // Initialize Braze SDK instance
        AppDelegate.braze = Braze(configuration: configuration)

        return true
    }
}

struct InboxViewControllerRepresentable: UIViewControllerRepresentable {
    func makeUIViewController(context: Context) -> UINavigationController {
        let vc = BrazeInboxViewController(style: .plain)
        return UINavigationController(rootViewController: vc)
    }
    func updateUIViewController(_ uiViewController: UINavigationController, context: Context) {}
}

struct ContentView: View {
    var body: some View {
        NavigationView {
                InboxViewControllerRepresentable()
            .navigationTitle("Message Inbox")
        }
    }
}

```

```swift file=SampleApp.swift
import SwiftUI

@main
struct SampleApp: App {
    @UIApplicationDelegateAdaptor(AppDelegate.self) var delegate

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
```

```swift file=BrazeInboxView.swift
import SwiftUI
import UIKit
import BrazeKit

class BrazeInboxViewController: UITableViewController {
    private var cards: [Braze.ContentCard] = []
    private var subscription: Any?
    private var loggedImpressions = Set<String>()

    override func viewDidLoad() {
        super.viewDidLoad()
        tableView.register(UITableViewCell.self, forCellReuseIdentifier: "CardCell")
        tableView.rowHeight = 100

        subscription = AppDelegate.braze.contentCards.subscribeToUpdates { [weak self] updatedCards in
            self?.cards = updatedCards
            self?.tableView.reloadData()
        }

        AppDelegate.braze.contentCards.requestRefresh()
    }

    override func numberOfSections(in tableView: UITableView) -> Int { 1 }

    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        cards.count
    }

    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let card = cards[indexPath.row]
        let cell = tableView.dequeueReusableCell(withIdentifier: "CardCell", for: indexPath)

        // Work with the content card's title and description
        cell.textLabel?.numberOfLines = 2
        cell.textLabel?.text = [card.title, card.description].compactMap { $0 }.joined(separator: "\n")
        
        return cell
    }

    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        let card = cards[indexPath.row]
        card.logClick(using: AppDelegate.braze)
        if let url = card.clickAction?.url {
            UIApplication.shared.open(url, options: [:], completionHandler: nil)
        }
        tableView.deselectRow(at: indexPath, animated: true)
    }
    
    override func tableView(_ tableView: UITableView,
                            willDisplay cell: UITableViewCell,
                            forRowAt indexPath: IndexPath) {
        let card = cards[indexPath.row]
        if !loggedImpressions.contains(card.id) {
            card.logImpression(using: AppDelegate.braze)
        }
    }
}
```

!Schritt
Zeilen-AppDelegate.swift=15

#### 1\. Enablement von Fehlersuchen (optional)

Um die Fehlerbehebung während der Entwicklung zu erleichtern, sollten Sie das Debugging aktivieren.

!Schritt
Zeilen-BrazeInboxView.swift=5

#### 2\. Eine UI-Ansicht erstellen

In diesem Tutorial verwenden wir die Swift [`UITableViewController`](https://developer.apple.com/documentation/uikit/uitableviewcontroller)aber wir empfehlen, ein UI mit Klassen und Komponenten zu erstellen, das Ihrem Anwendungsfall entspricht.

!Schritt
Zeilen-BrazeInboxView.swift=15-20

#### 3\. Updates für Content-Cards abonnieren

Abonnieren Sie den Content-Cards-Listener, um die neuesten Updates zu erhalten, und rufen Sie dann `requestRefresh()` auf, um die neuesten Content-Cards für diesen Nutzer:in anzufragen.

!Schritt
Zeilen-BrazeInboxView.swift=34-35

#### 4\. Erstellen Sie ein angepasstes UI für den Posteingang

Die Verwendung der Content-Card [`attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard) wie `title`, `description` und `imageUrl` können Sie Content-Cards erstellen, die Ihren speziellen UI-Anforderungen entsprechen. In diesem Fall bauen wir einen Posteingang mit den nativen Tabellen-APIs von Swift auf.

!Schritt
Zeilen-BrazeInboxView.swift=8,43,49-56

#### 5\. Tracking von Impressionen und Klicks

Sie können Impressionen und Klicks protokollieren, indem Sie die [`logClick(using:)`](<https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/logclick(using:)/>) und [`logImpression(using:)`](<https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/logimpression(using:)/>) Methoden, die für eine Content-Card verfügbar sind.

Außerdem können Sie [`logDismissed(using:)`](<https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/logdismissed(using:)/>) für Entlassungen verwenden.

Impressionen sollten nur einmal protokolliert werden, wenn sie von einem Nutzer:innen angesehen werden. Hier wird ein naiver Mechanismus verwendet, der eine `Set` und `willDisplay` verwendet. Beachten Sie, dass Sie möglicherweise den UI-Lebenszyklus Ihrer App sowie den Anwendungsfall berücksichtigen müssen, um sicherzustellen, dass Impressionen korrekt protokolliert werden.

{% endscrolly %}
{% endsdktab %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} Es ist jedoch keine zusätzliche Einrichtung erforderlich.

## Erstellen eines Posteingangs mit Content-Cards für das Internet

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md %}

{% scrolly %}

```js file=main.js
import * as braze from "@braze/web-sdk";

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

braze.requestContentCardsRefresh();
```

```html file=index.html
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

!Schritt
Zeilen-main.js=3-4,9

#### 1\. Enablement von Fehlersuchen (optional)

Um die Fehlerbehebung während der Entwicklung zu erleichtern, sollten Sie das Debugging aktivieren. Optional können Sie die Methoden des Braze Web SDK auch in der Konsole ausführen.

!Schritt
Zeilen-index.html=1-44

#### 2\. Erstellen Sie die UI

Erstellen Sie ein UI für die Seite des Posteingangs. Hier erstellen wir eine einfache HTML-Seite, die eine `div` mit der ID `cards-list` enthält. Dieser wird als Targeting-Container für die Darstellung von Content-Cards verwendet.

!Schritt
Zeilen-main.js=96-99,101

#### 3\. Updates für Content-Cards abonnieren

Abonnieren Sie den Content-Cards-Listener, um die neuesten Updates zu erhalten, und rufen Sie dann [`requestContentCardsRefresh()`](<https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestcontentcardsrefresh>) auf, um die neuesten Content-Cards für diesen Nutzer:innen anzufordern. Alternativ können Sie den Abonnent:in auch vor `openSession()` aufrufen, um eine automatische Aktualisierung bei Sitzungsbeginn zu erhalten. 

!Schritt
Zeilen-main.js=64,67,70-74

#### 4\. Erstellen Sie die Elemente für den Posteingang

Mit den [Content-Card-Attributen](<https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html>) wie `title`, `description` und `url` können Sie Content-Cards anzeigen, die Ihren spezifischen UI-Anforderungen entsprechen.

!Schritt
Zeilen-main.js=22-25,28-43,84,91

#### 5\. Tracking von Impressionen und Klicks

Sie können Impressionen und Klicks protokollieren, indem Sie die [`logContentCardImpressions`](<https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions>) und [`logContentCardClick`](<https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick>) die für Content-Cards verfügbar sind.

Außerdem können Sie [`logCardDismissal`](<https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcarddismissal>) für Entlassungen verwenden.

Impressionen sollten nur einmal protokolliert werden, wenn sie von einem Nutzer:innen angesehen werden. Hier verhindert ein `IntersectionObserver` plus ein `Set` mit dem Schlüssel `card.id` doppelte Protokolle. Beachten Sie, dass Sie möglicherweise den UI-Lebenszyklus Ihrer App sowie den Anwendungsfall berücksichtigen müssen, um sicherzustellen, dass Impressionen korrekt protokolliert werden.

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}
