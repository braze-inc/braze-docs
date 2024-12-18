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

実施にあたっては、まずカスタムイベントs、カスタム属性s、購買イベントが提供するセグメンテーション選択肢の事例を[ベストプラクティス]({{site.baseurl}}/developer_guide/platform_wide/getting_started/analytics_overview/#best-practices)で検討すること。また、[イベントの命名規則]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/)についてもよく理解しておくことをお勧めします。

```javascript
braze.logCustomEvent("YOUR-EVENT-NAME");
```

詳しくは [`logCustomEvent`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent)ドキュメントを参照のこと。

## プロパティ {#properties-events} の追加

カスタムイベントとともにプロパティオブジェクトを渡すことで、カスタムイベントに関するメタデータを追加することもできます。

プロパティはキーと値のペアとして定義されています。キーは文字列で、値は `string`、`numeric`、`boolean`、または [`Date`](http://www.w3schools.com/jsref/jsref_obj_date.asp) オブジェクトになります。

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

詳細については、[`logCustomEvent()` のドキュメント](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent)を参照してください。

