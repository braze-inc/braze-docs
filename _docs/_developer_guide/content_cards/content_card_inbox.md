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
import com.braze.ui.inappmessage.BrazeInAppMessageManager
import com.braze.BrazeActivityLifecycleCallbackListener
import com.braze.ui.inappmessage.listeners.IInAppMessageManagerListener
import com.braze.models.inappmessage.IInAppMessage
import com.braze.ui.inappmessage.InAppMessageOperation
import android.util.Log

```

!!step
lines-MainApplication.kt=17

#### 1. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

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
