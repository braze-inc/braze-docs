---
nav_title: メッセージフォーマット
article_title: プッシュメッセージとイメージの形式
page_order: 5
page_type: reference
description: "ここでは、プッシュ通知の電文と\"画像形式について説明します。"
channel: push

---

# プッシュメッセージと"画像形式

> このリファレンス記事では、プッシュ通知のメッセージフォーマットと"画像フォーマットについて説明します。

最良の結果を得るには、プッシュメッセージを作成する際に以下の"画像容量とメッセージ長の目安を参照してください。"画像の有無、ユーザーの機器の通知ステート(iOS)やディスプレイ設定、機器の大きさによって、多少のばらつきがある場合があります。疑問がある場合は、コピーを短くして甘くしてください。

## iOSとAndroidプッシュ

{% tabs ローカル %}
{% tab 画像 %}

**画像タイプ** | **推奨画像サイズ** | **最大画像サイズ** | **ファイルの種類**
--- | --- | --- | ---
(iOS) 2:1 *推奨* | 500 KB | 5 MB | PNG、JPEG、GIF
(Android)プッシュアイコン | 500 KB | 5 MB | PNG、JPEG
(Android) 拡張通知 | 500 KB | 5 MB | PNG、JPEG
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% endtab %}
{% tab テキスト %}

| メッセージタイプ | 推奨メッセージ長(テキストのみ) | 推奨メッセージ長(リッチ)
--- | ---
(iOS)ロック画面 | 160文字 | 130文字
(iOS) 通知センター | 160文字 | 130文字
(iOS)バナーアラート | 80文字 | 65 文字
(Android)ロックスクリーン | 49文字 | 該当なし
(Android)通知ドロアー | 597文字 | 該当なし
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

iOS プッシュ通知では、切り捨てられずに何文字使用できるかがわかりますか?[iOS文字数ガイドライン]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count)を確認してください。

{% endtab %}
{% tab 給与読み込む規模 %}

**プラットフォーム** | **サイズ**
--- | ---
iOS 8以前 | 0.256 KB
ポストiOS 8 | 2 KB
Android(FCM) | 4 KB
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab 画像例 %}
{% subtabs %}
{% subtab iOS %}

![読み上げる文字を含むiOSプッシュ通知:"こんにちは!これは、"画像" と絵文字を持つiOS プッシュです。テキストの横に小さな"画像があります。]({% image_buster /assets/img_archive/braze_richpush1.png %}){: style="max-width:50%;"}
![iOS プッシュ通知を、テキストの前に拡張"画像がある前のメッセージと同じテキストでハードプッシュする。]({% image_buster /assets/img_archive/braze_richpush2.png %}){: style="max-width:50%;"}

{% endsubtab %}
{% subtab Android %}

![メッセージtext.]({% image_buster /assets/img_archive/android_push_img2.png %})の下に大きな"画像を持つAndroid プッシュ通知

{% alert note %}
600x300ピクセル以上の"画像を使用する場合、大"画像 通知のディスプレイが最適です。
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab テキストの例 %}
{% subtabs %}
{% subtab iOS %}

![読み上げる文字を含むiOSプッシュ通知:"こんにちは!これはiOS Push".]({% image_buster /assets/img_archive/iOS_push_notification_small.png %})です。

{% endsubtab %}
{% subtab Android %}
![ホーム画面に表示されるAndroid プッシュ通知]({% image_buster /assets/img_archive/Push_Android_2.png %})
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Web プッシュ

{% tabs ローカル %}
{% tab 画像 %}

| **ブラウザ** | **推奨アイコンサイズ**
| --- | ---
クロム | 192 x 192 ≥
Firefox | 192 x 192 ≥
サファリ | 192 x 192 ≧(アイコンは、macOS 13+ のSafari 16 でキャンペーンごとに設定可能)
オペラ | 192x192 ≥
{: .reset-td-br-1 .reset-td-br-2}

| **ブラウザ** | **プラットフォーム** | **大きな画像サイズ**
| --- | --- | ---
クロム | Android | アスペクト比2:1
Firefox | Android | 該当なし
クロム | Windows | アスペクト比2:1
エッジ | Windows | アスペクト比2:1
Firefox | Windows | 該当なし
Firefox | Windows | アスペクト比2:1
サファリ | macOS | 該当なし
クロム | macOS | 該当なし
Firefox | macOS | 該当なし
オペラ | macOS | 該当なし
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab テキスト %}

| **ブラウザ** | **プラットフォーム** | **タイトルの最大長**  | **メッセージ本文の最大長**
| --- | --- | --- | ---
クロム | Android | 35 | 50
Firefox | Android | 35 | 50
クロム | Windows | 50 | 120
エッジ | Windows | 50 | 120
Firefox | Windows | 54 | 200
オペラ | Windows | 50 | 120
クロム | macOS | 35 | 50
サファリ | macOS | 38 | 84
Firefox | macOS | 38 | 42
オペラ | macOS | 38 | 42
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% endtab %}
{% endtabs %}


