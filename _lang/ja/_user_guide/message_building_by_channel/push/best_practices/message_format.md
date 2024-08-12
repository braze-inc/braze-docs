---
nav_title: メッセージ形式
article_title: プッシュメッセージと画像フォーマット
page_order: 5
page_type: reference
description: "この記事では、プッシュ通知のメッセージと画像の形式について説明します。"
channel: push

---

# プッシュメッセージと画像形式

> このリファレンス記事では、プッシュ通知のメッセージと画像の形式について説明します。

最良の結果を得るには、プッシュ メッセージを作成するときに、次の画像サイズとメッセージの長さのガイドラインを参照してください。画像の有無、ユーザーの端末の通知状態（iOS）や表示設定、端末のサイズなどにより多少の差異が生じる場合があります。疑問がある場合は、コピーを短く簡潔にしてください。

## iOSとAndroidのプッシュ

{% tabs local %}
{% tab Images %}

**画像タイプ** | **推奨画像サイズ** | **最大画像サイズ** | **ファイルタイプ**
--- | --- | --- | ---
(iOS) 2:1 *推奨* | 500 KB | 5 MB | PNG、JPEG、GIF
(Android) プッシュアイコン | 500 KB | 5 MB | PNG、JPEG
(Android) 拡張通知 | 500 KB | 5 MB | PNG、JPEG
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% endtab %}
{% tab Text %}

| メッセージ タイプ | 推奨メッセージの長さ (テキストのみ) | 推奨メッセージの長さ (リッチ)
--- | ---
(iOS) ロック画面 | 160 文字 | 130 文字
(iOS) 通知センター | 160 文字 | 130 文字
(iOS) バナーアラート | 80 文字 | 65 文字
(Android) ロック画面 | 49 文字 | N/A
(Android) Notification Drawer | 597 characters | N/A
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

iOS プッシュ通知では、切り捨てられることなく何文字まで使用できるか知りたいですか?[iOS の文字数カウントガイドライン]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count)をご覧ください。

{% endtab %}
{% tab Payload Size %}

**プラットフォーム** | **サイズ**
--- | ---
iOS 8 以前 | 0.256 KB
iOS 8以降 | 2 KB
Android (FCM) | 4 KB
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Image Example %}
{% subtabs %}
{% subtab iOS %}

![iOS push notification with text that reads: "Hi! This is an iOS Push with an image" with an emoji. There is a small image beside the text.]({% image_buster /assets/img_archive/braze_richpush1.png %}){: style="max-width:50%;"}
![iOS push notification on a hard push with the same text as the previous message with an expanded image preceding the text.]({% image_buster /assets/img_archive/braze_richpush2.png %}){: style="max-width:50%;"}

{% endsubtab %}
{% subtab Android %}

![Android push notification with a large image under the message text.]({% image_buster /assets/img_archive/android_push_img2.png %})

{% alert note %}
大きな画像通知は、少なくとも 600 x 300 ピクセルの画像を使用すると最適に表示されます。
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Text Example %}
{% subtabs %}
{% subtab iOS %}

![iOS push notification with text that reads: "Hi! This is an iOS Push".]({% image_buster /assets/img_archive/iOS_push_notification_small.png %})

{% endsubtab %}
{% subtab Android %}
![Android push notification displayed on the home screen.]({% image_buster /assets/img_archive/Push_Android_2.png %})
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Web プッシュ

{% tabs local %}
{% tab Images %}

| **ブラウザ** | **推奨アイコンサイズ**
| --- | ---
クローム | 192 x 192 ≥
Firefox | 192 x 192 ≥
Safari | 192 x 192 ≥ (macOS 13 以降の Safari 16 では、アイコンはキャンペーンごとに設定可能です)
オペラ | 192x192 ≥
{: .reset-td-br-1 .reset-td-br-2}

| **ブラウザ** | **プラットフォーム** | **大きな画像サイズ**
| --- | --- | ---
Chrome | Android | アスペクト比 2:1
Firefox | Android | N/A
Chrome | Windows | 2:1 aspect ratio
Edge | Windows | 2:1 aspect ratio
Firefox | Windows | N/A
Firefox | Windows | アスペクト比 2:1
Safari | macOS | N/A
Chrome | macOS | N/A
Firefox | macOS | N/A
Opera | macOS | N/A
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Text %}

| **ブラウザ** | **プラットフォーム** | **タイトルの最大長** | **メッセージ本文の最大長**
| --- | --- | --- | ---
Chrome | Android | 35 | 50
Firefox | Android | 35 | 50
Chrome | Windows | 50 | 120
エッジ | Windows | 50 | 120
Firefox | Windows | 54 | 200
Opera | Windows | 50 | 120
Chrome | macOS | 35 | 50
Safari | macOS | 38 | 84
Firefox | macOS | 38 | 42
オペラ | macOS | 38 | 42
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% endtab %}
{% endtabs %}


