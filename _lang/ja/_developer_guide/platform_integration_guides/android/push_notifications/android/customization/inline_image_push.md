---
nav_title: インライン画像プッシュ
article_title: Android 向けインライン画像プッシュ
platform: Android
page_order: 5.9
description: "このリファレンス記事では、Android アプリにインライン画像プッシュを実装する方法について説明します。"
channel:
  - push

---

# インライン画像プッシュ

![]({% image_buster /assets/img/android/push/inline_image_push_android_1.png %}){: style="float:right;max-width:30%;margin-left:15px;border: 0;"}

> インライン画像プッシュを使用して Android プッシュ通知内で大きな画像を表示します。この設計により、ユーザーは画像を拡大するために手動でプッシュを拡大する必要がなくなります。 

この機能を使用するために、追加の統合や SDK の変更は必要となりません。最小バージョン要件を満たしていないデバイスまたは SDK では、代わりに標準の大画像プッシュ通知が表示されます。

## 使用要件

- この通知タイプには Braze Android SDK v10.0.0+ と Android M+ デバイスが必要です。 
- サポートされていないデバイスや SDK は、標準の大画像プッシュ通知にフォールバックします。
- 通常の Android プッシュ通知とは異なり、インライン画像プッシュ画像の縦横比は 3:2 です。

{% alert note %}
Android 12 を実行しているデバイスでは、カスタムプッシュ通知スタイルの変更によりレンダリングが異なります。
{% endalert %}

## ダッシュボードのセットアップ

Android プッシュメッセージを作成する場合、この機能は [**通知タイプ**] ドロップダウンで使用できます。

![「通知タイプ」ドロップダウン (標準のプッシュプレビューの上) の場所を示すプッシュキャンペーンエディター。]({% image_buster /assets/img/android/push/android_inline_image_notification_type.png %})
