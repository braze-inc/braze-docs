---
nav_title: イベント
article_title: イベント
page_order: 0
page_type: reference
description: "この記事では、Braze のさまざまなイベント (標準イベント、購入イベント、カスタムイベント) とその目的について説明します。"
---

# イベント 

> このページでは、Braze のさまざまなイベントとその目的について説明します。

Brazeは、いくつかの異なるイベントタイプを使用して、ユーザーの行動とブランドとの関わりについて包括的に理解しています。各タイプのイベントにはそれぞれの目的があります。

- [標準イベント](#standard-events): アプリやサイトに対するユーザーエンゲージメントの基本的な情報を提供します。
- [購入イベント](#purchase-events): ユーザーの購入行動を把握し、収益を追跡するうえで重要です。 
- [カスタムイベント](#custom-events): アプリやビジネスに固有のユーザー行動について、より深いインサイトを提供します。

これらのさまざまなタイプのイベントを追跡することで、ユーザーについての理解を深めることができます。その結果、マーケティング戦略が充実し、アプリの最適化に役立ち、よりパーソナライズされたユーザーエクスペリエンスを提供できます。詳しく見ていきましょう。

## 標準イベント

Braze の標準イベントは、ユーザーがアプリ内で実行できる定義済みのアクションであり、Braze SDK を連携すると Braze により自動的に追跡されます。標準イベントの例をいくつか示します。

- アプリ起動
- [購入](#purchase-events)
- セッション開始
- セッション終了
- プッシュ通知のクリック
- メールの開封

マーケターはこれらの標準イベントを使用して、ユーザーの行動やアプリへのエンゲージメントを把握できます。たとえば、ユーザーがアプリを起動する頻度や、購入が何回行われているかを確認できます。この情報は、ターゲットを絞ったマーケティングキャンペーンを作成する場合に貴重です。

標準イベントは Braze によって自動的に追跡されますが、購入イベント、カスタムイベント、およびカスタム属性は特定のニーズと目標に基づいて開発チームが設定する必要があることに注意してください。

## 購入イベント

購入イベントは、ユーザーによる購入を記録して追跡する方法です。これは標準イベントの一種であり、Braze SDK を連携するとデフォルトで利用可能になります。そのため、購入イベントを使用して購入を追跡すると、Braze から直接、さまざまな収入源にわたる経時的な収益を監視できます。

購入イベントには、購入に関する以下の重要な情報が記録されます。

- 製品 ID (通常は製品名またはカテゴリ)
- 通貨
- 価格
- 数量

このデータを使用して、生涯価値、購入頻度、特定の購入などに基づいてユーザーのセグメンテーションができます。

Braze は複数通貨での購入もサポートしています。米ドル以外の通貨で購入が記録された場合、購入が記録された日の為替レートに基づいて、Braze ダッシュボードに米ドル単位で表示されます。

詳細については、独立した「[購入イベント]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/)」の記事を参照してください。

{% details Example implementation %}

実際に購入イベントを実装するには、Braze SDK とアプリを統合する必要があるため、技術的な知識が必要になります。オンボーディングの一環として、カスタマーサクセスマネージャーがチームにこのプロセスを説明しますが、一般的なステップは次のとおりです。

1. **Braze SDK と連携する:**イベントをログに記録する前に、Braze SDK をアプリに統合する必要があります。
2. **購入イベントをログに記録する:**SDK と連携すると、ユーザーがアプリ内で購入を行うたびに購入イベントをログに記録できます。これは通常、購入が完了したときに呼び出される関数またはメソッドで行われます。

Swift を使用して iOS アプリに購入イベントを記録する方法の例を以下に示します。

```swift
Appboy.sharedInstance()?.logPurchase("product_name", inCurrency: "USD", atPrice: NSDecimalNumber(string: "1.99"), withQuantity: 1)
```

この例では、"product_name" は購入した製品の名前、"USD" は購入の通貨、" 1.99" は製品の価格、"1" は購入数量です。

{:start="3"}
3. **Braze ダッシュボードで購入イベントを確認する:**購入イベントが記録されると、Braze ダッシュボードに表示できます。このデータを使用して、収益の分析、ユーザーのセグメンテーションなどができます。

具体的な実装は、プラットフォーム (iOS、Android、Web) やアプリの特定の要件によって異なる場合があることに注意してください。 

{% enddetails %}

## カスタムイベント

カスタムイベントは、アプリまたはサイトの内部で追跡しようとする特定のアクションに基づいて定義するイベントです。Braze は自動的にはトラッキングしません。Braze SDK 実装でこれらのイベントを手動で設定する必要があります。カスタムイベントは、ユーザーがゲーム内のレベルをクリアした、プロフィール情報を更新したなど、何でもかまいません。

Swift を使用して iOS アプリのカスタムイベントを記録する方法の例を以下に示します。

```swift
Appboy.sharedInstance()?.logCustomEvent("completed_level")
```

この例では、"completed_level" は、ユーザーがゲームのレベルを完了したときにログに記録されるカスタムイベントの名前です。そのカスタムイベントは Braze のユーザープロファイルに記録され、キャンペーンのトリガーやメッセージングのパーソナライゼーションに使用できます。

詳細については、独立した「[カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)」の記事を参照してください。

{% details Example implementation %}

購入イベントと同様に、カスタムイベントには追加の設定が必要です。Braze でカスタムイベントを実装する一般的なステップは次のとおりです。

1. **Braze SDK と連携する:**イベントをログに記録する前に、Braze SDK をアプリに連携する必要があります。
2. **カスタムイベントを定義する:**カスタムイベントとして追跡するアプリ内のアクションを決めます。これは、ユーザーがゲーム内のレベルをクリアした、プロフィールを更新した、特定タイプの購入を行ったなど、アプリにとって意味のあるアクションであれば何でもかまいません。
3. **カスタムイベントをログに記録する:**カスタムイベントを定義したら、アプリのコードでログに記録できます。これは通常、アクションが発生したときに呼び出される関数またはメソッドで行われます。

Swift を使用して iOS アプリのカスタムイベントを記録する方法の例を以下に示します。

```swift
Appboy.sharedInstance()?.logCustomEvent("updated_profile")
```

この例題では、"updated_profile" は、ユーザー 更新がプロファイルを取得したときに記録されるカスタムイベントの名前です。

{:start="4"}
4. **プロパティをカスタムイベントに追加する (オプション):**カスタムイベントに関する詳細情報を収集する場合は、プロパティを追加できます。これは、イベントをログに記録するときにプロパティのディクショナリを渡すことで行われます。

Swift を使用して iOS アプリのカスタムイベントをプロパティとともにログに記録する方法の例を以下に示します。

```swift
let properties: [AnyHashable: Any] = ["Property Name": "Property Value"]
Appboy.sharedInstance()?.logCustomEvent("updated_profile", withProperties: properties)
```

この例のカスタムイベントには、名前が「Property Name」で値「Property Value」を持つプロパティがあります。

{:start="5"}
5. **Braze ダッシュボードでカスタムイベントを確認する:**カスタムイベントが記録されると、Braze ダッシュボードに表示できます。このデータを使用して、ユーザー行動の分析、ユーザーのセグメンテーションなどができます。

{% enddetails %}

<!--

### Using custom events instead of purchase events to track purchases

You might prefer to use custom events to track purchases if you need to capture more specific or additional information about the purchase that the standard purchase event doesn't cover. Here's what you can do with custom events that you can't accomplish with purchase events:

- **Custom definitions:** Custom events can be defined based on any significant action within your app. This level of customization is not available with standard purchase events, which are predefined and specifically designed to track purchases.
- **Additional properties:** You can log additional properties to custom events that provide more context about the event. For example, you could log a custom event when a user makes a purchase and include properties such as the product category or the payment method. This is not possible with standard purchase events, which have a fixed schema that only tracks the product name, currency, price, and quantity.
- **Event frequency:** Custom events allow you to track the frequency of specific actions. With purchase events, you can only track the occurrence of purchases, not other types of actions.

#### Use case 1

Let's say you have an eCommerce app, and you want to track the purchase itself and the product category. The standard purchase event in Braze does not capture this level of detail, so you could use a custom event instead.

Here's an example of how you might do this in an iOS app using Swift:

```swift
let properties: [AnyHashable: Any] = ["Product Category": "Electronics"]
Appboy.sharedInstance()?.logCustomEvent("Purchase", withProperties: properties)
```

In this example, "Purchase" is the name of the custom event, and the properties dictionary contains additional information about the event. In this case, the product category is "Electronics". Now you can segment your users based on the product categories they purchase from.

#### Use case 2

Consider a fitness app where users can purchase personal training sessions or premium workout plans. In this case, you might want to track these purchases as custom events to capture additional details about the purchase.

Here's an example of how you might do this in an iOS app using Swift:

```swift
let properties: [AnyHashable: Any] = ["Workout Plan": "10 Sessions Personal Training"]
Appboy.sharedInstance()?.logCustomEvent("Purchase", withProperties: properties)
```

In this example, "Purchase" is the name of the custom event, and the properties dictionary contains additional information about the event. In this case, the workout plan is "10 Sessions Personal Training". Now you can segment your users based on the types of workout plans they purchase.

-->


