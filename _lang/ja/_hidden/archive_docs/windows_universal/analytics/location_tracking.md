---
nav_title: 位置情報の追跡
article_title: Windowsユニバーサルの位置情報トラッキング
platform: Windows Universal
page_order: 6
description: "このリファレンス記事では、Windowsユニバーサルアプリに位置情報トラッキングを追加する方法を説明する。"
tool: Location
hidden: true
---

# 位置情報の追跡
{% multi_lang_include archive/windows_deprecation.md %}

1. `Package.appxmanifest` 、`location` がチェックされていることを確認する。
2. 自動位置追跡をオフにしたい場合は、`AppboyConfiguration.xml` で`<DisableLocationCollection>false</DisableLocationCollection>` を`true` に設定する。
