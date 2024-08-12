---
nav_title: カスタムイベントの追跡
article_title: Unity のカスタムイベントの追跡
platform: 
  - Unity
  - iOS
  - Android
page_order: 1
description: "このリファレンス記事では、Unity プラットフォームでカスタムイベントをログに記録する方法について説明します。"

---

# カスタムイベントのトラッキング

> Braze でカスタムイベントを記録することで、アプリの使用パターンに関する詳細を把握し、ダッシュボードでのアクションによってユーザーをセグメント化できます。

実装前に、[ベストプラクティス][4]記事のカスタムイベント、カスタム属性、および購入イベントで提供されるセグメンテーションオプションの例を確認してください。また、[イベントの命名規則]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/)についてもよく理解しておくことをお勧めします。

```csharp
AppboyBinding.LogCustomEvent("event name");
```

Brazeは、イベントプロパティを渡す `Dictionary` ことで、カスタムイベントに関するメタデータを追加することもできます。

```csharp
AppboyBinding.LogCustomEvent("event name", properties(Dictionary<string, object>));
```

## REST API

REST APIを使用してイベントを記録することもできます。詳細については、[ユーザー API][5] のドキュメントを参照してください。

[4]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#best-practices
[5]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
