---
nav_title: メッセージフォーマット
article_title: プッシュメッセージとイメージの形式
page_order: 5
page_type: reference
description: "この記事では、プッシュ通知のメッセージ形式と画像形式について説明します。"
channel: push

---

# プッシュ通知メッセージと画像の形式

> このリファレンス記事では、プッシュ通知のメッセージ形式と画像形式について説明します。

最適な結果を得るには、プッシュメッセージを作成するときに、以下の画像サイズとメッセージ長のガイドラインを参照してください。"画像の有無、ユーザーの機器の通知ステート(iOS)やディスプレイ設定、機器の大きさによって、多少のばらつきがある場合があります。迷ったときには、文章を簡潔にまとめます。

## iOSとAndroidプッシュ

{% tabs local %}
{% tab Images %}

**画像タイプ** | **推奨画像サイズ** | **最大画像サイズ** | **ファイルの種類**
--- | --- | --- | ---
(iOS) 2:1 *推奨* | 500 KB | 5 MB | PNG、JPEG、GIF
(Android)プッシュアイコン | 500 KB | 5 MB | PNG、JPEG
(Android) 拡張通知 | 500 KB | 5 MB | PNG、JPEG
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endtab %}
{% tab Text %}

| メッセージタイプ | 推奨メッセージ長 (テキストのみ) | 推奨メッセージ長 (リッチ)
--- | ---
(iOS)ロック画面 | 160文字 | 130文字
(iOS) 通知センター | 160文字 | 130文字
(iOS)バナーアラート | 80文字 | 65 文字
(Android)ロックスクリーン | 49文字 | 該当なし
(Android)通知ドロアー | 597文字 | 該当なし
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

iOS プッシュ通知で、切り詰められずに使用できる文字数が不明の場合は、[iOS文字数ガイドライン]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count)を確認してください。

{% endtab %}
{% tab Payload Size %}

**プラットフォーム** | **サイズ**
--- | ---
iOS 8以前 | 0.256 KB
ポストiOS 8 | 2 KB
Android(FCM) | 4 KB
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Image Example %}
{% subtabs %}
{% subtab iOS %}

![読み上げる文字を含むiOSプッシュ通知:「こんにちは。これは、画像を含む iOS プッシュ通知です」と絵文字があります。テキストの横に小さな画像があります。(]({% image_buster /assets/img_archive/braze_richpush1.png %})){: style="max-width:50%;"}
長押しで表示される iOS プッシュ通知。前のメッセージと同じテキストを持ち、画像がテキストの前に拡大表示されています。()![

{% endsubtab %}
{% subtab Android %}

![メッセージテキストの下に大きな画像がある Android のプッシュ通知。]({% image_buster /assets/img_archive/android_push_img2.png %})()

{% alert note %}
大画像の通知は、600x300 ピクセル以上の画像を使用すると最も良く表示されます。
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Text Example %}
{% subtabs %}
{% subtab iOS %}

![読み上げる文字を含むiOSプッシュ通知:「こんにちは。これは iOS プッシュ通知です。」(]({% image_buster /assets/img_archive/iOS_push_notification_small.png %}))

{% endsubtab %}
{% subtab Android %}
ホーム画面に表示されるAndroid プッシュ通知(![)
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Web プッシュ

{% tabs local %}
{% tab Images %}

| **ブラウザー** | **推奨アイコンサイズ**
| --- | ---
Chrome | 192 x 192 ≥
Firefox | 192 x 192 ≥
Safari | 192 x 192 ≥ (MacOS 13 以降 のSafari 16 では、キャンペーンごとにアイコンを設定可能)
Opera | 192x192 ≥
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

| **ブラウザー** | **プラットフォーム** | **大きな画像のサイズ**
| --- | --- | ---
Chrome | Android | アスペクト比2:1
Firefox | Android | 該当なし
Chrome | Windows | アスペクト比2:1
Edge | Windows | アスペクト比2:1
Firefox | Windows | 該当なし
Firefox | Windows | アスペクト比2:1
Safari | macOS | 該当なし
Chrome | macOS | 該当なし
Firefox | macOS | 該当なし
Opera | macOS | 該当なし
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Text %}

| **ブラウザー** | **プラットフォーム** | **タイトルの最大長**  | **メッセージ本文の最大長**
| --- | --- | --- | ---
Chrome | Android | 35 | 50
Firefox | Android | 35 | 50
Chrome | Windows | 50 | 120
Edge | Windows | 50 | 120
Firefox | Windows | 54 | 200
Opera | Windows | 50 | 120
Chrome | macOS | 35 | 50
Safari | macOS | 38 | 84
Firefox | macOS | 38 | 42
Opera | macOS | 38 | 42
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endtab %}
{% endtabs %}


