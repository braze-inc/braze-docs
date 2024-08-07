---
nav_title: カスタムイベントの追跡
article_title: Windows Universalのカスタムイベントのトラッキング
platform: Windows Universal
page_order: 2
description: "この記事では、Windows Universalプラットフォームでカスタムイベントを追跡する方法について説明します。"
hidden: true
---

# カスタムイベントのトラッキング
{% multi_lang_include archive/windows_deprecation.md %}

Braze でカスタムイベントを記録することで、アプリの使用パターンに関する詳細を把握し、ダッシュボードでのアクションによってユーザーをセグメント化できます。また、[イベントの命名規則]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/)についてもよく理解しておくことをお勧めします。

すべてのイベントは、IAppboyで公開されているプロパティである`EventLogger`を使用してログに記録されます。参照を取得するには`EventLogger`、`Appboy.SharedInstance.EventLogger`を呼び出します。次の方法を使用して、重要なユーザーアクションとカスタムイベントを追跡できます:

```csharp
bool LogCustomEvent(string YOUR_EVENT_NAME)
```
