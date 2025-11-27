---
nav_title: 位置情報の追跡
article_title: Windows Universalの位置情報の追跡
platform: Windows Universal
page_order: 6
description: "このリファレンス記事では、Windows Universal アプリに位置情報の追跡を追加する方法について説明します。"
tool: Location
hidden: true
---

# 位置情報の追跡
{% multi_lang_include archive/windows_deprecation.md %}

1. `Package.appxmanifest` ファイル内で `location` がオンになっていることを確認します。
2. 自動位置情報の追跡をオフにするには、`AppboyConfiguration.xml` で `<DisableLocationCollection>false</DisableLocationCollection>` を `true` に設定します。
