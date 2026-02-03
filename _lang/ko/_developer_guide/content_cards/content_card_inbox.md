---
nav_title: "Tutorial: 콘텐츠 카드 받은편지함"
article_title: "Tutorial: 콘텐츠 카드로 받은편지함 만들기"
description: ""
page_order: 6
layout: scrolly
---

# Tutorial: 콘텐츠 카드로 받은편지함 만들기

> 이 튜토리얼의 샘플 코드를 따라 Braze 콘텐츠 카드로 받은편지함을 구축하세요.

{% sdktabs %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %}

## Android용 콘텐츠 카드로 받은편지함 만들기(작성)

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

!!단계
lines-MainApplication.kt=12

#### 1\. 디버깅 활성화(선택 사항)

개발 중 문제 해결을 쉽게 하기 위해 디버깅을 활성화하는 것을 고려하세요.

!!단계
lines-ContentCardsInboxScreen.kt=47-69

#### 2\. UI 보기 구축

제트팩 컴포지션의 경우 [`LazyColumn`](<https://developer.android.com/develop/ui/compose/lists#lazy>) 를 사용하여 콘텐츠 카드를 스크롤 가능한 목록으로 표시합니다.

!!단계
라인-ContentCardsInboxScreen.kt=25-37

#### 3\. 콘텐츠 카드 업데이트 가입하기

를 사용하여 [`DisposableEffect`](<https://developer.android.com/develop/ui/compose/side-effects#disposableeffect>) 를 사용하여 구독 라이프사이클을 관리하여 컴포저블이 컴포저블을 떠날 때 적절한 정리가 이루어지도록 합니다.

!!단계
라인-ContentCardsInboxScreen.kt=84-95

#### 4\. 커스텀 받은편지함 UI 구축하기

`title`, `description`, `url` 와 같은 콘텐츠 카드 [속성을](<https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html>) 사용하여 특정 UI 요구 사항에 맞는 콘텐츠 카드를 구축할 수 있습니다. 이 경우 Jetpack Compose의 `Card` 및 `Column` 컴포저블을 사용하여 받은편지함을 구축합니다.

!!단계
lines-ContentCardsInboxScreen.kt=57,62

#### 5\. 노출 횟수 및 클릭 수 추적

노출 횟수와 클릭 수를 기록할 수 있습니다. [`logImpressions`](<https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html>) 및 [`logClick`](<https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html>) 메서드를 사용하여 노출과 클릭을 기록할 수 있습니다.

노출 횟수는 사용자가 카드를 볼 때 한 번만 기록해야 합니다. `LaunchedEffect` 을 사용하여 카드가 표시될 때 노출 횟수를 기록합니다. 노출 횟수가 올바르게 기록되도록 하려면 앱의 뷰 라이프사이클과 사용 사례를 고려해야 할 수 있습니다.

{% endscrolly %}

## Android용 콘텐츠 카드로 받은편지함 만들기(RecyclerView)

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

!!단계
lines-MainApplication.kt=12

#### 1\. 디버깅 활성화(선택 사항)

개발 중 문제 해결을 쉽게 하기 위해 디버깅을 활성화하는 것을 고려하세요.

!!단계
lines-content_card_inbox.xml=1-24

#### 2\. UI 보기 구축

이 튜토리얼에서는 Android의 [`RecyclerView`](<https://developer.android.com/develop/ui/views/layout/recyclerview>) 를 사용하여 콘텐츠 카드를 표시하지만, 사용 사례에 맞는 클래스와 컴포넌트로 UI를 구축하는 것이 좋습니다. Braze는 기본값으로 UI를 제공하지만 이 튜토리얼에서는 모양과 동작을 사용자 지정할 수 있는 커스텀 보기를 만드는 방법을 안내합니다.

!!단계
lines-ContentCardInboxActivity.kt=29-35,40-42,44

#### 3\. 콘텐츠 카드 업데이트 가입하기

를 사용하여 [`subscribeToContentCardsUpdates`](<https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-content-cards-updates.html?query=abstract%20fun%20subscribeToContentCardsUpdates(subscriber:%20IEventSubscriber%3CContentCardsUpdatedEvent%3E)>) 를 사용하여 새 콘텐츠 카드를 사용할 수 있을 때 UI가 응답하도록 합니다. 여기에서 가입자는 활동 라이프사이클 후크 내에서 등록 및 제거됩니다.

!!단계
라인-ContentCardInboxActivity.kt=73-84

#### 4\. 커스텀 받은편지함 UI 구축하기

`title`, `description`, `url` 와 같은 콘텐츠 카드 [속성을](<https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html>) 사용하면 특정 UI 요구 사항에 맞게 콘텐츠 카드를 구축할 수 있습니다. 이 경우, Android의 기본 `RecyclerView` 을 사용하여 받은편지함을 구축합니다.

!!단계
lines-ContentCardInboxActivity.kt=90,93

#### 5\. 노출 횟수 및 클릭 수 추적

노출 횟수와 클릭 수를 기록할 수 있습니다. [`logImpressions`](<https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html>) 및 [`logClick`](<https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html>) 메서드를 사용하여 노출과 클릭을 기록할 수 있습니다.

노출 횟수는 사용자가 카드를 볼 때 한 번만 기록해야 합니다. 여기서는 카드별 플래그를 사용하여 중복 로그를 방지하는 순진한 메커니즘을 사용합니다. 노출 횟수가 올바르게 기록되도록 하려면 앱의 뷰 라이프사이클과 사용 사례를 고려해야 할 수 있습니다.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} 또한 [Swift에 대한 인앱 메시지를 인에이블먼트해야]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=swift#swift_enabling-in-app-messages) 합니다.

## Swift용 콘텐츠 카드로 받은편지함 만들기

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

!!단계
lines-AppDelegate.swift=15

#### 1\. 디버깅 활성화(선택 사항)

개발 중 문제 해결을 쉽게 하기 위해 디버깅을 활성화하는 것을 고려하세요.

!!단계
lines-BrazeInboxView.swift=5

#### 2\. UI 뷰 구축

이 튜토리얼에서는 Swift의 [`UITableViewController`](https://developer.apple.com/documentation/uikit/uitableviewcontroller)를 사용하지만, 사용 사례에 맞는 클래스와 컴포넌트로 UI를 구축하는 것이 좋습니다.

!!단계
라인-BrazeInboxView.swift=15-20

#### 3\. 콘텐츠 카드 업데이트 가입하기

콘텐츠 카드 리스너에 가입하여 최신 업데이트를 받은 다음 `requestRefresh()` 으로 전화하여 해당 사용자의 최신 콘텐츠 카드를 요청하세요.

!!단계
라인-BrazeInboxView.swift=34-35

#### 4\. 커스텀 받은편지함 UI 구축하기

콘텐츠 카드 사용 [`attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard)`title` , `description`, `imageUrl` 와 같은 콘텐츠 카드를 사용하면 특정 UI 요구 사항에 맞게 콘텐츠 카드를 구축할 수 있습니다. 이 경우 Swift의 기본 테이블 API를 사용하여 받은편지함을 구축하고 있습니다.

!!단계
lines-BrazeInboxView.swift=8,43,49-56

#### 5\. 노출 횟수 및 클릭 수 추적

노출 횟수와 클릭 수를 기록할 수 있습니다. [`logClick(using:)`](<https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/logclick(using:)/>) 및 [`logImpression(using:)`](<https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/logimpression(using:)/>) 메서드를 사용하여 콘텐츠 카드에 대한 노출과 클릭을 기록할 수 있습니다.

또한 [`logDismissed(using:)`](<https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/logdismissed(using:)/>) 를 사용할 수도 있습니다.

노출 횟수는 사용자가 볼 때 한 번만 기록해야 합니다. 여기서는 `Set` 및 `willDisplay` 을 사용하는 순진한 메커니즘을 사용하여 이를 달성합니다. 노출 횟수가 올바르게 기록되도록 하려면 앱의 UI 라이프사이클과 사용 사례를 고려해야 할 수 있습니다.

{% endscrolly %}
{% endsdktab %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} 그러나 추가 설정은 필요하지 않습니다.

## 웹용 콘텐츠 카드로 받은편지함 만들기

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

!!단계
lines-main.js=3-4,9

#### 1\. 디버깅 활성화(선택 사항)

개발 중 문제 해결을 쉽게 하기 위해 디버깅을 활성화하는 것을 고려하세요. 선택적으로 콘솔에서 Braze 웹 소프트웨어 개발 키트 메서드를 실행할 수도 있습니다.

!!단계
라인-index.html=1-44

#### 2\. UI 구축

받은편지함 페이지의 UI를 만듭니다. 여기서는 ID가 `cards-list` 인 `div` 을 포함하는 기본 HTML 페이지를 구축합니다. 콘텐츠 카드 렌더링의 타겟팅 컨테이너로 사용됩니다.

!!단계
lines-main.js=96-99,101

#### 3\. 콘텐츠 카드 업데이트 가입하기

콘텐츠 카드 리스너에 가입하여 최신 업데이트를 받은 다음, 해당 사용자의 최신 콘텐츠 카드를 요청하려면 [`requestContentCardsRefresh()`](<https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestcontentcardsrefresh>) 을 호출하여 해당 사용자에 대한 최신 콘텐츠 카드를 요청하세요. 또는 가입자에게 `openSession()` 으로 전화하여 세션 시작 시 자동으로 새로고침되도록 요청하세요. 

!!단계
lines-main.js=64,67,70-74

#### 4\. 받은편지함 요소 구축하기

`title`, `description`, `url` 와 같은 콘텐츠 카드 [속성을](<https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html>) 사용하면 특정 UI 요구 사항에 맞게 콘텐츠 카드를 표시할 수 있습니다.

!!단계
라인-main.js=22-25,28-43,84,91

#### 5\. 노출 횟수 및 클릭 수 추적

노출 횟수와 클릭 수를 기록할 수 있습니다. [`logContentCardImpressions`](<https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions>) 및 [`logContentCardClick`](<https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick>) 메서드를 사용하여 노출과 클릭을 기록할 수 있습니다.

또한 [`logCardDismissal`](<https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcarddismissal>) 를 사용할 수도 있습니다.

노출 횟수는 사용자가 볼 때 한 번만 기록해야 합니다. 여기서 `IntersectionObserver` + `Set` + `card.id` 키는 중복 로그를 방지합니다. 노출 횟수가 올바르게 기록되도록 하려면 앱의 UI 라이프사이클과 사용 사례를 고려해야 할 수 있습니다.

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}
