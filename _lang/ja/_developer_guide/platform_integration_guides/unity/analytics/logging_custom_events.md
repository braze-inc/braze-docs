---
nav_title: カスタムイベントの追跡
article_title: Unityのカスタムイベントのトラッキング
platform: 
  - Unity
  - iOS
  - Android
page_order: 1
description: "この参考記事では、Unity プラットフォームでカスタムイベントを記録する方法について説明します。"

---

# カスタムイベントのトラッキング

> Braze でカスタムイベントを記録することで、アプリの使用パターンに関する詳細を把握し、ダッシュボードでのアクションによってユーザーをセグメント化できます。

実施にあたっては、まずカスタムイベントs、カスタム属性s、購買イベントが提供するセグメンテーション選択肢の事例を[ベストプラクティス][4]で検討すること。また、[イベントの命名規則]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/)についてもよく理解しておくことをお勧めします。

```csharp
AppboyBinding.LogCustomEvent("event name");
```

Braze では、イベントプロパティの `Dictionary` を渡すことによる、カスタムイベントに関するメタデータの追加もサポートしています。

```csharp
AppboyBinding.LogCustomEvent("event name", properties(Dictionary<string, object>));
```

## REST API

また、REST APIを使用してイベントを記録することもできます。詳細については、[ユーザー API][5] のドキュメントを参照してください。

[4]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#best-practices
[5]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
