---
nav_title: カスタムイベントの追跡
article_title: ウェブのカスタムイベントをトラッキングする
platform: Web
page_order: 2
page_type: reference
description: "この記事では、カスタム・イベントのトラッキング方法と、それらのイベントにWeb用のプロパティを追加する方法について説明する。"

---

# カスタムイベントのトラッキング

> Braze でカスタムイベントを記録することで、アプリの使用パターンに関する詳細を把握し、ダッシュボードでのアクションによってユーザーをセグメント化できます。

実装する前に、カスタムイベント、カスタム属性、購入イベントによって提供されるセグメンテーションオプションの例を、[ベストプラクティスで]({{site.baseurl}}/developer_guide/platform_wide/getting_started/analytics_overview/#best-practices)確認してほしい。また、[イベントの命名規則]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/)についてもよく理解しておくことをお勧めします。

```javascript
braze.logCustomEvent("YOUR-EVENT-NAME");
```

詳しくは [`logCustomEvent`][1]ドキュメントを参照のこと。

## プロパティ {#properties-events} の追加

オプションとして、カスタム・イベントにプロパティ・オブジェクトを渡すことで、カスタム・イベントに関するメタデータを追加することができる。

プロパティはキーと値のペアとして定義されています。キーは文字列で、値は`string` 、`numeric` 、`boolean` 、またはオブジェクトである。 [`Date`][2]オブジェクトである。

```javascript
braze.logCustomEvent("YOUR-EVENT-NAME", {
  you: "can", 
  pass: false, 
  orNumbers: 42,
  orDates: new Date(),
  or: ["any", "array", "here"],
  andEven: {
     deeply: ["nested", "json"]
  }
});
```

詳しくは[`logCustomEvent()` のドキュメントを][1]参照のこと。

[0]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[1]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent
[2]: http://www.w3schools.com/jsref/jsref_obj_date.asp
