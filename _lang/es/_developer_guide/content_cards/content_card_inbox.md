---
nav_title: "Tutorial: Buzones de entrada de tarjetas de contenido"
article_title: "Tutorial: Crear un buzón de entrada con tarjetas de contenido"
description: ""
page_order: 6
layout: scrolly
---

# Tutorial: Crear un buzón de entrada con tarjetas de contenido

> Sigue el código de ejemplo de este tutorial para crear un buzón de entrada con tarjetas de contenido Braze.

{% sdktabs %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %}

## Crear un buzón de entrada con tarjetas de contenido para Android (Componer)

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

Paso
líneas-MainApplication.kt=12

#### 1\. Habilitar la depuración (opcional)

Para facilitar la solución de problemas durante el desarrollo, considera la posibilidad de habilitar la depuración.

Paso
líneas-ContentCardsInboxScreen.kt=47-69

#### 2\. Construye una vista de IU

Para Jetpack Compose, utiliza un [`LazyColumn`](<https://developer.android.com/develop/ui/compose/lists#lazy>) para mostrar las tarjetas de contenido en una lista desplegable.

Paso
líneas-ContentCardsInboxScreen.kt=25-37

#### 3\. Suscribirse a las actualizaciones de la tarjeta de contenido

Utiliza un [`DisposableEffect`](<https://developer.android.com/develop/ui/compose/side-effects#disposableeffect>) para gestionar el ciclo de vida de la suscripción, garantizando una limpieza adecuada cuando el compositor abandona la composición.

Paso
líneas-ContentCardsInboxScreen.kt=84-95

#### 4\. Construye una interfaz de usuario de buzón de entrada personalizada

Utilizar los [atributos](<https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html>) de las tarjetas de contenido como `title`, `description` y `url` te permite crear tarjetas de contenido que se ajusten a tus requisitos específicos de interfaz de usuario. En este caso, estamos construyendo un buzón de entrada con los componibles `Card` y `Column` de Jetpack Compose.

Paso
líneas-ContentCardsInboxScreen.kt=57,62

#### 5\. Seguimiento de impresiones y clics

Puedes registrar las impresiones y los clics con el botón [`logImpressions`](<https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html>) y [`logClick`](<https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html>) disponibles para las tarjetas de contenido.

Las impresiones sólo deben registrarse una vez cuando el usuario ve una tarjeta. Utiliza `LaunchedEffect` para registrar las impresiones cuando una tarjeta se hace visible. Ten en cuenta que puede que tengas que considerar el ciclo de vida de la vista de tu aplicación, así como el caso de uso, para asegurarte de que las impresiones se registran correctamente.

{% endscrolly %}

## Crear un buzón de entrada con tarjetas de contenido para Android (RecyclerView)

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

Paso
líneas-MainApplication.kt=12

#### 1\. Habilitar la depuración (opcional)

Para facilitar la solución de problemas durante el desarrollo, considera la posibilidad de habilitar la depuración.

Paso
lines-content_card_inbox.xml=1-24

#### 2\. Construye una vista de IU

En este tutorial, utilizamos la función de Android [`RecyclerView`](<https://developer.android.com/develop/ui/views/layout/recyclerview>) para mostrar tarjetas de contenido, pero te recomendamos que construyas una interfaz de usuario con clases y componentes que se adapten a tu caso de uso. Braze proporciona la interfaz de usuario de forma predeterminada, pero este tutorial te guía para crear una vista personalizada para personalizar la apariencia y el comportamiento.

Paso
líneas-ContentCardInboxActivity.kt=29-35,40-42,44

#### 3\. Suscribirse a las actualizaciones de la tarjeta de contenido

Utiliza [`subscribeToContentCardsUpdates`](<https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-content-cards-updates.html?query=abstract%20fun%20subscribeToContentCardsUpdates(subscriber:%20IEventSubscriber%3CContentCardsUpdatedEvent%3E)>) para que tu interfaz de usuario responda cuando haya nuevas tarjetas de contenido disponibles. Aquí, los suscriptores se registran y eliminan dentro de los ganchos del ciclo de vida de la actividad.

Paso
líneas-ContentCardInboxActivity.kt=73-84

#### 4\. Construye una interfaz de usuario de buzón de entrada personalizada

El uso de los [atributos](<https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html>) de las tarjetas de contenido como `title`, `description` y `url` te permite crear tarjetas de contenido que se ajusten a tus requisitos específicos de interfaz de usuario. En este caso, estamos construyendo un buzón de entrada con el nativo de Android `RecyclerView`.

Paso
líneas-ContentCardInboxActivity.kt=90,93

#### 5\. Seguimiento de impresiones y clics

Puedes registrar las impresiones y los clics con el botón [`logImpressions`](<https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html>) y [`logClick`](<https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html>) disponibles para las tarjetas de contenido.

Las impresiones sólo deben registrarse una vez cuando el usuario ve una tarjeta. Aquí utilizamos un mecanismo ingenuo para evitar los registros duplicados con una bandera por tarjeta. Ten en cuenta que puede que tengas que considerar el ciclo de vida de la vista de tu aplicación, así como el caso de uso, para asegurarte de que las impresiones se registran correctamente.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} También tendrás que [habilitar los mensajes dentro de la aplicación para Swift]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=swift#swift_enabling-in-app-messages).

## Crear un buzón de entrada con tarjetas de contenido para Swift

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

Paso
líneas-AppDelegate.swift=15

#### 1\. Habilitar la depuración (opcional)

Para facilitar la solución de problemas durante el desarrollo, considera la posibilidad de habilitar la depuración.

Paso
líneas-BrazeInboxView.swift=5

#### 2\. Construye una vista de IU

En este tutorial, utilizamos Swift's [`UITableViewController`](https://developer.apple.com/documentation/uikit/uitableviewcontroller)pero te recomendamos que construyas una interfaz de usuario con clases y componentes que se adapten a tu caso de uso.

Paso
líneas-BrazeInboxView.swift=15-20

#### 3\. Suscribirse a las actualizaciones de la tarjeta de contenido

Suscríbete a la escucha de tarjetas de contenido para recibir las últimas actualizaciones y, a continuación, llama a `requestRefresh()` para solicitar las últimas tarjetas de contenido para ese usuario.

Paso
líneas-BrazeInboxView.swift=34-35

#### 4\. Construye una interfaz de usuario de buzón de entrada personalizada

Utilizar la tarjeta de contenido [`attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard) como `title`, `description` y `imageUrl` te permite crear tarjetas de contenido que se adapten a tus requisitos específicos de interfaz de usuario. En este caso, estamos construyendo un buzón de entrada con las API nativas de tablas de Swift.

Paso
líneas-BrazeInboxView.swift=8,43,49-56

#### 5\. Seguimiento de impresiones y clics

Puedes registrar las impresiones y los clics con el botón [`logClick(using:)`](<https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/logclick(using:)/>) y [`logImpression(using:)`](<https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/logimpression(using:)/>) disponibles para una tarjeta de contenido.

Además, puedes utilizar [`logDismissed(using:)`](<https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/logdismissed(using:)/>) para los despidos.

Las impresiones sólo deben registrarse una vez cuando las vea el usuario. Para ello se utiliza un mecanismo ingenuo que utiliza `Set` y `willDisplay`. Ten en cuenta que puede que tengas que considerar el ciclo de vida de la interfaz de usuario de tu aplicación, así como el caso de uso, para asegurarte de que las impresiones se registran correctamente.

{% endscrolly %}
{% endsdktab %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} Sin embargo, no es necesaria ninguna configuración adicional.

## Crear un buzón de entrada con tarjetas de contenido para Web

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

Paso
líneas-main.js=3-4,9

#### 1\. Habilitar la depuración (opcional)

Para facilitar la solución de problemas durante el desarrollo, considera la posibilidad de habilitar la depuración. Opcionalmente, también puedes ejecutar métodos del SDK Web de Braze en la consola.

Paso
líneas-index.html=1-44

#### 2\. Construye la IU

Crea una interfaz de usuario para la página del buzón de entrada. Aquí estamos construyendo una página HTML básica, que incluye un `div` con el ID `cards-list`. Se utiliza como contenedor de destino para la representación de las tarjetas de contenido.

Paso
líneas-main.js=96-99,101

#### 3\. Suscribirse a las actualizaciones de la tarjeta de contenido

Suscríbete a la escucha de Tarjetas de contenido para recibir las últimas actualizaciones y, a continuación, llama a [`requestContentCardsRefresh()`](<https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestcontentcardsrefresh>) para solicitar las últimas Tarjetas de contenido para ese usuario. Alternativamente, llama al suscriptor antes de `openSession()` para que se actualice automáticamente al iniciar la sesión. 

Paso
líneas-main.js=64,67,70-74

#### 4\. Construye los elementos del buzón de entrada

El uso de los [atributos](<https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html>) de las tarjetas de contenido como `title`, `description` y `url` te permite mostrar tarjetas de contenido que se ajusten a tus requisitos específicos de interfaz de usuario.

Paso
líneas-main.js=22-25,28-43,84,91

#### 5\. Seguimiento de impresiones y clics

Puedes registrar las impresiones y los clics con el botón [`logContentCardImpressions`](<https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions>) y [`logContentCardClick`](<https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick>) disponibles para las tarjetas de contenido.

Además, puedes utilizar [`logCardDismissal`](<https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcarddismissal>) para los despidos.

Las impresiones sólo deben registrarse una vez cuando las vea el usuario. Aquí, un `IntersectionObserver` más un `Set` con clave `card.id` evita los registros duplicados. Ten en cuenta que puede que tengas que considerar el ciclo de vida de la interfaz de usuario de tu aplicación, así como el caso de uso, para asegurarte de que las impresiones se registran correctamente.

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}
