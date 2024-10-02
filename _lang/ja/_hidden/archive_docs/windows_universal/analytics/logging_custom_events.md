---
nav_title: カスタムイベントの追跡
article_title: Windows Universal のカスタムイベントの追跡
platform: Windows Universal
page_order: 2
description: "このリファレンス記事では、Windows ユニバーサルプラットフォームでカスタムイベントを追跡する方法について説明します。"
hidden: true
---

# カスタムイベントのトラッキング
{% multi_lang_include archive/windows_deprecation.md %}

Braze でカスタムイベントを記録することで、アプリの使用パターンに関する詳細を把握し、ダッシュボードでのアクションによってユーザーをセグメント化できます。また、[イベントの命名規則]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/)についてもよく理解しておくことをお勧めします。

すべてのイベントは、`EventLogger` を使用してログに記録されます。これは、IAppboy で公開されるプロパティです。`EventLogger` への参照を取得するには、`Appboy.SharedInstance.EventLogger` を呼び出します。以下の方法で、大切なユーザー アクションs とカスタムイベントs をトラッキングできます。

```csharp
bool LogCustomEvent(string YOUR_EVENT_NAME)
```
