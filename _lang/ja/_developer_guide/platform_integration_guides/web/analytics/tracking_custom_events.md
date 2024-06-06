---
nav_title: カスタムイベントの追跡
article_title: Web 用カスタムイベントのトラッキング
platform: Web
page_order: 2
page_type: reference
description: "この記事では、Web 用にカスタムイベントを追跡し、それらのイベントにプロパティを追加する方法について説明します。"

---

# カスタムイベントのトラッキング

> Braze でカスタムイベントを記録することで、アプリの使用パターンに関する詳細を把握し、ダッシュボードでのアクションによってユーザーをセグメント化できます。

実装前に、[ベストプラクティス][0]記事のカスタムイベント、カスタム属性、および購入イベントで提供されるセグメンテーションオプションの例を確認してください。また、[イベントの命名規則]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/)についてもよく理解しておくことをお勧めします。

```javascript
braze.logCustomEvent("YOUR-EVENT-NAME");
```

詳細については、[`logCustomEvent`][1]ドキュメントを参照してください。

## プロパティ {#properties-events} の追加

オプションで、カスタムイベントにプロパティオブジェクトを渡すことで、カスタムイベントに関するメタデータを追加できます。

プロパティはキーと値のペアとして定義されています。キーは文字列で`string`、値は、、`numeric``boolean`、[`Date`][2]またはオブジェクトです。

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

詳細については、[`logCustomEvent()`ドキュメントを参照してください][1]。

[0]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[1]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent
[2]: http://www.w3schools.com/jsref/jsref_obj_date.asp
