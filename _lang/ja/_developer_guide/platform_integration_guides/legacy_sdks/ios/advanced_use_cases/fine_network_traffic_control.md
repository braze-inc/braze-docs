---
nav_title: きめ細かなネットワークトラフィック制御
article_title: iOS 向けのきめ細かなネットワークトラフィック制御
platform: iOS
page_order: 1
description: "この記事では、iOS アプリケーションのきめ細かなネットワーク トラフィック制御の実装について説明します。"

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# きめ細かなネットワークトラフィック制御

## リクエスト処理ポリシー

Braze では、ユーザーに対し、以下のプロトコルを使用してネットワーク トラフィックを制御するオプションが提供されます。

### 自動リクエスト処理

***`ABKRequestProcessingPolicy` 列挙値: `ABKAutomaticRequestProcessing`***

- これが**デフォルトのリクエストポリシー**値です。
- Braze SDK では、以下を含むすべてのサーバー通信が自動的に処理されます。
    - カスタムイベントと属性データの Braze サーバーへのフラッシュ
    - コンテンツカードとジオフェンスの更新
    - 新しいアプリ内メッセージのリクエスト
- アプリ内メッセージなどの Braze 機能にユーザー向けデータが必要である場合に、即時サーバーリクエストが実行されます。
- サーバーの負荷を最小限に抑えるため、Braze では新規ユーザーデータの定期フラッシュが数秒ごとに実行されます。

データは、次の方法を使用して、いつでも手動で Braze サーバーにフラッシュできます。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] flushDataAndProcessRequestQueue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.flushDataAndProcessRequestQueue()
```

{% endtab %}
{% endtabs %}

### 手動リクエスト処理

***`ABKRequestProcessingPolicy` 列挙値: `ABKManualRequestProcessing`***

- このプロトコルは、次の点を除いて自動リクエスト処理と同じです。
    - カスタム属性とカスタムイベントデータが、ユーザーセッションを通じてサーバーに自動でフラッシュされません。
- Braze で、アプリ内メッセージのリクエスト、アプリ内メッセージの Liquid テンプレート、ジオフェンス、位置情報の追跡などの内部機能に対する自動ネットワークリクエストが実行されます。詳細については、[`Appboy.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h) で `ABKRequestProcessingPolicy` の宣言を参照してください。これらの内部リクエストが実行されると、リクエストのタイプによっては、ローカルに保存されたカスタム属性とカスタムイベントデータが Braze サーバーにフラッシュされる場合があります。

データは、次の方法を使用して、いつでも手動で Braze サーバーにフラッシュできます。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] flushDataAndProcessRequestQueue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.flushDataAndProcessRequestQueue()
```

{% endtab %}
{% endtabs %}

## リクエスト処理ポリシーの設定

### 起動時のリクエストポリシーの設定

これらのポリシーは、アプリの起動時に [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24) メソッドから設定できます。`appboyOptions` ディクショナリで、次のコードスニペットに示すように `ABKRequestProcessingPolicyOptionKey` を設定します。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
NSDictionary *appboyOptions = @{
  // Other entries
  ABKRequestProcessingPolicyOptionKey : @(ABKAutomaticRequestProcessing)
};
```

{% endtab %}
{% tab swift %}

```swift
let appboyOptions: [AnyHashable: Any] = [
  // Other entries
  ABKRequestProcessingPolicyOptionKey: ABKRequestProcessingPolicy.automaticRequestProcessing.rawValue
]
```

{% endtab %}
{% endtabs %}

### 実行時のリクエストポリシーの設定

リクエスト処理ポリシーは、`requestProcessingPolicy` プロパティを `Appboy` で使用することで実行時に設定することもできます。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Sets the request processing policy to automatic (the default value)
[Appboy sharedInstance].requestProcessingPolicy = ABKAutomaticRequestProcessing;
```

{% endtab %}
{% tab swift %}

```swift
// Sets the request processing policy to automatic (the default value)
Appboy.sharedInstance()?.requestProcessingPolicy = ABKRequestProcessingPolicy.automaticRequestProcessing
```

{% endtab %}
{% endtabs %}

## 実行中のサーバー通信の手動シャットダウン

「実行中」のサーバー通信を停止する必要がある場合は、次のメソッドを呼び出す必要があります。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] shutdownServerCommunication];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.shutdownServerCommunication();
```

{% endtab %}
{% endtabs %}

このメソッドを呼び出した後、リクエスト処理モードを自動にリセットする必要があります。そのため、OS がバックグラウンドタスクなどの停止を強制している場合にのみ、これを呼び出すことをお勧めします。

