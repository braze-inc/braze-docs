---
nav_title: "Tutorial: Content Card Inboxes"
article_title: "Tutorial: Making an Inbox with Content Cards"
description: ""
page_order: 1
layout: scrolly
---

# Tutorial: Making an Inbox with Content Cards

> Follow along with the sample code in this tutorial to build an inbox with Braze content cards.

{% sdktabs %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %}

## Making an Inbox with Content Cards for Android

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

!!step
lines-MainApplication.kt=12

#### 1. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

!!step
lines-content_card_inbox.xml=1-24

#### 2. Create the UI View

We're using Android's `RecyclerView` to display Content Cards in this tutorial, but we recommend building a UI with classes and components that suit your use case(s). Braze provides UI by default, but here we create a custom view to have full control over the appearance and behavior.

!!step
lines-ContentCardInboxActivity.kt=29-35,40-42,44

#### 3. Subscribe to & Refresh Content Cards

Use [`subscribeToContentCardsUpdates`](<https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-content-cards-updates.html?query=abstract%20fun%20subscribeToContentCardsUpdates(subscriber:%20IEventSubscriber%3CContentCardsUpdatedEvent%3E)>) to allow your UI to respond when new content cards are available. Here, subscribers are registered and removed within the activity lifecycle hooks.

!!step
lines-ContentCardInboxActivity.kt=73-84
#### 4. Build a Custom Inbox UI

Using the content card [attributes](<https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html>) such as `title`, `description`, and `url` allows you to build content cards to match your specific UI requirements. In this case, we're building an inbox with Android's native `RecyclerView`.

!!step
lines-ContentCardInboxActivity.kt=90,93
#### 5. Track Impressions & Clicks

You can log impressions and clicks using the [`logImpressions`](<https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html>) and [`logClick`](<https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html>) methods available for content cards.

Impressions should only be logged once when a card is viewed by the user. Here, we use a naive machanism to guard agaisnt duplicate logs with a per-card flag. Note that you may need to think through the view lifecycle of your app, as well as use case, so ensure impressions are logged correctly.


{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} You'll also need to [enable in-app messages for Swift]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=swift#swift_enabling-in-app-messages).

## Making an Inbox with Content Cards for Swift

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

!!step
lines-AppDelegate.swift=15

#### 1. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

!!step
lines-BrazeInboxView.swift=5

#### 2. Create the UI View

We're using Swift's [`UITableViewController`](https://developer.apple.com/documentation/uikit/uitableviewcontroller) in this tutorial, but we recommend building a UI with classes and components that suit your use case(s).

!!step
lines-BrazeInboxView.swift=15-20

#### 3. Subscribe to & refresh Content Cards

Subscribe to the content cards listener to receive the latest updates, and then call `requestRefresh()` to request the latest content cards for that user.

!!step
lines-BrazeInboxView.swift=34-35

#### 4. Build a custom inbox UI

Using the content card [`attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard) such as `title`, `description`, and `imageUrl` allows you to build content cards to match your specific UI requirements. In this case, we're building an inbox with Swift's native table APIs.

!!step
lines-BrazeInboxView.swift=8,43,49-56

#### 5. Track impressions and clicks

You can log impressions and clicks using the [`logClick(using:)`](<https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/logclick(using:)/>) and [`logImpression(using:)`](<https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/logimpression(using:)/>) methods available for a content card.

Additionally, you can use [`LogDimissed(using:)`](<https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/logdismissed(using:)/>) for dimissals.

Impressions should only be logged once when viewed by the user. Here, a naive mechanism using a `Set` and `willDisplay` is used to achieve this. Note that you may need to think through the UI lifecycle of your app, as well as use case, to ensure impressions are logged correctly.

{% endscrolly %}
{% endsdktab %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} However, no additional setup is required.

## Making an Inbox with Content Cards for Web

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md %}

{% scrolly %}

```js file=index.js
import * as braze from "@braze/web-sdk";
```

!!step
lines-index.js=6

#### 1. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}
