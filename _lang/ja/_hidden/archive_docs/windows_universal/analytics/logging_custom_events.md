---
nav_title: カスタムイベントのトラッキング
article_title: Windows Universalのカスタムイベントのトラッキング
platform: Windows Universal
page_order: 2
description: "このリファレンス記事では、Windowsユニバーサルプラットフォームでカスタムイベントを追跡する方法について説明します。"
hidden: true
---

# カスタムイベントのトラッキング
{% multi_lang_include archive/windows_deprecation.md %}

Brazeでカスタムイベントを記録することで、アプリの使用パターンについて詳しく知ることができ、ダッシュボード上の行動によってユーザーをセグメント化することができます。また、[イベントの命名規則を]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/)よく理解されることをお勧めします。

すべてのイベントは、IAppboyで公開されているプロパティである`EventLogger` 。`EventLogger` への参照を得るには、`Appboy.SharedInstance.EventLogger` を呼び出す。以下のメソッドを使用して、重要なユーザーアクションやカスタムイベントを追跡できます：

```csharp
bool LogCustomEvent(string YOUR_EVENT_NAME)
```
