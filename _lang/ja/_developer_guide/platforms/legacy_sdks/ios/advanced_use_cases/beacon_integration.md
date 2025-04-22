---
nav_title: ビーコンの統合
article_title: iOS 向けビーコン統合
platform: iOS
page_order: 4
description: "この記事では、Infillion Beacons for iOS を使用したカスタムイベントのログ記録について説明します。"

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# ビーコンの統合

ここでは、特定の種類のビーコンを Braze と統合して、セグメンテーションとメッセージングを可能にする方法について説明します。

## インフィリオンビーコン

Infillionビーコンを設定し、アプリに統合すると、訪問の開始や終了、ビーコンの表示などのカスタムイベントをログに記録できます。これらのイベントのプロパティ (場所の名前、滞在時間など) をログに記録することもできます。

ユーザーが場所に入ったときにカスタムイベントをログに記録するには、次のコードを `didBeginVisit` メソッドに入力します。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] logCustomEvent:@"Entered %@", visit.place.name];
[[Appboy sharedInstance] flushDataAndProcessRequestQueue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logCustomEvent("Entered %@", visit.place.name)
Appboy.sharedInstance()?.flushDataAndProcessRequestQueue()
```

{% endtab %}
{% endtabs %}

`flushDataAndProcessRequestQueue` は、アプリがバックグラウンドで実行されている場合でもイベントが必ずログに記録されることを確認します。これと同じプロセスを、場所から離れる行動についても実装できます。これにより、ユーザーが新しい場所を入力するたびに固有のカスタムイベントが作成され、増分されることに注意してください。50 個を超える場所を作成する予定の場合は、一般的な「入力された場所」カスタムイベントを 1 つ作成し、イベントプロパティとして場所名を含めることをお勧めします。
