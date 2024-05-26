---
nav_title: ロケーショントラッキング
article_title: Windows ユニバーサルのロケーショントラッキング
platform: Windows Universal
page_order: 6
description: "この参考記事では、Windows ユニバーサルアプリに位置追跡を追加する方法について説明します。"
tool: Location
hidden: true
---

# ロケーショントラッキング
{% multi_lang_include archive/windows_deprecation.md %}

1. `Package.appxmanifest``location`ファイル内でがチェックされていることを確認します。
2. 自動位置追跡を無効にする場合は、`<DisableLocationCollection>false</DisableLocationCollection>``true`でに設定します`AppboyConfiguration.xml`。
