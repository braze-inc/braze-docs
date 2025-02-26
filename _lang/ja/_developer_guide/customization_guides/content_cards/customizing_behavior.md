---
nav_title: カードの動作のカスタマイズ
article_title: コンテンツカードの動作のカスタマイズ
page_order: 2
description: "この実装ガイドでは、コンテンツカードの動作の変更、ペイロードへのキーと値のペアなどの追加、一般的なカスタマイズのレシピについて説明します。"
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# コンテンツカードの動作のカスタマイズ

> この実装ガイドでは、コンテンツカードの動作の変更、ペイロードへのキーと値のペアなどの追加、一般的なカスタマイズのレシピについて説明します。コンテンツカードのカスタマイズオプションのタイプの基本的な概要については[カスタマイズの概要]({{site.baseurl}}/developer_guide/customization_guides/customization_overview)を参照してください。 

## キーと値のペア

Braze では、キーと値のペアを使用して、コンテンツカードを介して追加のデータペイロードをユーザーデバイスに送信することができます。これらは、内部指標の追跡、アプリコンテンツの更新、プロパティのカスタマイズに役立ちます。\[ダッシュボードを使用してキーと値のペアを追加する][9]。 
 
{% alert note %}
ネストされた JSON 値をキーと値のペアとして送信することは推奨しません。その代わりに、送信する前に JSON を平坦化します。
{% endalert %}

{% tabs %}
{% tab Android %}

キーと値のペアは、`extras`として<a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/#-2118252107%2FProperties%2F-1725759721" target="_blank">`card`</a>オブジェクトに格納されます 。これらは、カードと一緒にデータを送信し、アプリケーションでさらに処理するために使用します。<a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/extras.html" target="_blank">`card.extras`</a>を呼び出して、これらの値にアクセスします。

{% endtab %}
{% tab iOS %}

キーと値のペアは、`extras`として<a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard" target="_blank">`card`</a>オブジェクトに格納されます 。これらは、カードと一緒にデータを送信し、アプリケーションでさらに処理するために使用します。<a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct/extras" target="_blank">`card.extras`</a>を呼び出して、これらの値にアクセスします。

{% endtab %}
{% tab Web %}

キーと値のペアは、`extras`として<a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html" target="_blank">`card`</a>オブジェクトに格納されます 。これらは、カードと一緒にデータを送信し、アプリケーションでさらに処理するために使用します。`card.extras`を呼び出して、これらの値にアクセスします。

{% endtab %}
{% endtabs %}

{% alert tip %}
マーケターが Braze ダッシュボードに入力するキーと値のペアは、開発者がアプリのロジックに組み込むキーと値のペアと正確に一致しなければならないため、マーケティングチームと開発チームが、どのキーと値のペアを使用するか (たとえば、`feed_type = brand_homepage`) について確実に調整することが重要です。
{% endalert %}

## 補足コンテンツとしてのコンテンツカード

![][1]{: style="float:right;max-width:25%;margin-left:15px;border:0;"}

コンテンツカードを既存のフィードにシームレスにブレンドし、複数のフィードからのデータを同時に読み込むことができます。これにより、Braze コンテンツカードと既存のフィードコンテンツとの一貫性のある、調和のとれたエクスペリエンスが生まれます。

右の例は、ローカルデータと Braze コンテンツカードを使ったハイブリッドなアイテムリストを持つフィードを示しています。これによって、コンテンツカードは既存のコンテンツと区別がつかなくなります。

### API トリガーのキーと値のペア

\[API-triggered campaigns][7] は、カードの値が外部要因に依存してユーザーに表示するコンテンツを決定する場合に採用するとよい戦略である。たとえば、補足的なコンテンツを表示するには、Liquid を使用してキーと値のペアを設定します。なお、`class_type`はセットアップ時に知っておく必要があります。

![補足コンテンツカードのユースケースのキーと値のペア。この例では、"tile_id"、"tile_deeplink"、"tile_title "のようなカードの異なる側面がLiquidを使って設定されている。][2]{: style="max-width:60%;"}

## インタラクティブコンテンツとしてのコンテンツカード
![画面左下に50%のプロモーションを示すインタラクティブなコンテンツカードが表示されている。クリックすると、カートにプロモーションが適用されます。][4]{: style="border:0;"}{: style="float:right;max-width:45%;border:0;margin-left:15px;"} 

コンテンツカードを活用して、ユーザーのための動的でインタラクティブな体験を作成できます。右の例では、コンテンツカードのポップアップがチェックアウト時に表示され、ユーザーに最新のプロモーションを提供しています。このようなカードをうまく配置することで、ユーザーを特定のアクションに「後押し」することができます。 

このユースケースのキーと値のペアには、希望する割引額として設定された`discount_percentage`と、`coupon_code` として設定された`class_type`が含まれます。これらのキーと値のペアによって、チェックアウト画面でタイプ別のコンテンツカードをフィルタリングして表示することができます。キーと値のペアを使用して複数のフィードを管理する方法については、\[デフォルトのコンテンツカードフィードのカスタマイズ][3] を参照してください。
<br>
<br>

![][5]{: style="max-width:80%;"} 

## コンテンツカードバッジ

![Brazeのサンプルアプリ「Swifty」が表示されたiPhoneのホーム画面には、赤いバッジで数字の「7」が表示されている。][8]{: style="max-width:35%;float:right;margin-left:15px;border:none;"}

バッジは小さなアイコンで、ユーザーの注意を引くのに最適です。バッジを使って新しいコンテンツカードの内容をユーザーに知らせることで、ユーザーをアプリに呼び戻し、セッションを増やすことができます。

### コンテンツカードの未読数をバッジで表示する

コンテンツカードの未読数をバッジとしてアプリのアイコンに表示できます。 

{% tabs %}
{% tab Android %}

未読カードの数は、以下を呼び出していつでもリクエストできます。

{% subtabs %}
{% subtab Java %}

```java
Braze.getInstance(context).getContentCardUnviewedCount();
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
Braze.getInstance(context).contentCardUnviewedCount
```

{% endsubtab %}
{% endsubtabs %}

この情報を使って、未読コンテンツカードの数を示すバッジを表示することができます。詳細については、<a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/get-content-card-unviewed-count.html" target="_blank">SDK リファレンスドキュメント</a>を参照してください。


{% endtab %}
{% tab iOS %}

次のサンプルでは、`braze.contentCards` を使用して未読コンテンツカードの数をリクエストして表示しています。アプリが閉じられ、ユーザーのセッションが終了した後、このコードはカード・カウントをリクエストし、`viewed` プロパティに基づいてカードの数をフィルタリングする。

{% subtabs %}
{% subtab Swift %}

```swift
func applicationDidEnterBackground(_ application: UIApplication)
```

このメソッド内で、次のコードを実装します。これにより、ユーザーが特定のセッション中にカードを閲覧している間にバッジカウントがアクティブに更新されます。

```swift
let unreadCards = AppDelegate.braze?.contentCards.cards.filter { $0.viewed == false }
UIApplication.shared.applicationIconBadgeNumber = unreadCards?.count ?? 0
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
(void)applicationDidEnterBackground:(UIApplication *)application
```

このメソッド内で、次のコードを実装します。これにより、ユーザーが特定のセッション中にカードを閲覧している間にバッジカウントがアクティブに更新されます。

```objc
NSInteger unreadCardCount = 0;
for (BRZContentCardRaw *card in AppDelegate.braze.contentCards.cards) {
  if (card.viewed == NO) {
    unreadCardCount += 1;
  }
}
[UIApplication sharedApplication].applicationIconBadgeNumber = unreadCardCount;
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

未読カードの数は、以下を呼び出していつでもリクエストできます。

```javascript
braze.getCachedContentCards().getUnviewedCardCount();
```

この情報を使って、未読コンテンツカードの数を示すバッジを表示することができます。詳細については、<a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.contentcards.html" target="_blank">SDK リファレンスドキュメント</a>を参照してください。

{% endtab %}
{% endtabs %}


[1]: {% image_buster /assets/img/cc_implementation/supplementary.png %}
[2]: {% image_buster /assets/img/cc_implementation/supplementary_content.png %}
[3]: {{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds
[4]: {% image_buster /assets/img/cc_implementation/discount2.png %}
[5]: {% image_buster /assets/img/cc_implementation/discount.png %}
[6]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/#content-cards
[7]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/
[8]: {% image_buster /assets/img/cc_implementation/ios-unread-badge.png %}
[9]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create#step-4-configure-additional-settings-optional
