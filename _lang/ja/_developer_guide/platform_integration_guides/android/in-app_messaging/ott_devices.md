---
nav_title: OTT と TV での表示
article_title: Android および FireOS 用の OTT および TV での表示
page_order: 5
platform: 
  - Android
  - FireOS
description: "このリファレンス記事では、Android または FireOS アプリケーションのアプリ内メッセージ OTT 表示情報について説明します。"
channel:
  - in-app messages

---

# OTT と TV での表示

> Braze Android SDK は、Android TV やFire Stick などの OTT デバイスでのアプリ内メッセージの表示をネイティブでサポートしています。

## 主な違い

ネイティブデバイスと OTT デバイスでは、標準のアプリ内メッセージの表示にいくつかの重要な違いがあります。

OTT デバイスの場合:

* スライドアップなどのタッチモードを必要とするアプリ内メッセージは、OTT で無効になります。
* 閉じるボタンなど、現在選択されている項目またはフォーカスされている項目がハイライト表示されます。
* ボタン上ではなく、アプリ内メッセージ自体の本文をクリックすることはサポートされていません。

