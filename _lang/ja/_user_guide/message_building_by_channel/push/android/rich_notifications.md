---
nav_title: "Android リッチ通知"
article_title: Android 向けリッチ通知
page_order: 3
page_layout: tutorial
description: "このチュートリアルでは、Braze キャンペーン用に Android リッチ通知を設定する方法について説明します。"
platform: Android
channel:
  - Push
tool:
  - Campaigns
  
---

# Android のリッチ通知

> リッチ通知を使用すると、コピーだけでなく追加のコンテンツを追加することで、プッシュ通知をさらにカスタマイズできます。Android の通知では、以前からプッシュ通知に「拡張通知画像」と呼ばれる画像が含まれていました。

## 要件

- 拡張通知ビューは、Jelly Bean (Android 4.1) 以降を使用しているデバイスでのみ利用できることに注意してください。ユーザーのデバイスがこれらのシステムで実行されていない場合、通知画像は表示されません。
- Android 拡張通知画像は 2:1 の比率である必要がありますが、サイズ制限はありません。
- Android では、標準の通知ビューに別の画像を設定することもできます。<br>推奨画像サイズ:小サイズは 512x256、中サイズは 1024x512、大サイズは 2048x1024 です。
- 現在、Android リッチ通知では、JPEG、PNG、GIF などのまだサポートされていない画像形式を含む静的画像のみが許可されています。
- プッシュ通知にアクション ボタンを追加すると、表示可能な画像領域に影響する場合がありますので注意してください。ダッシュボードのプレビューとライブデバイスでテストして、結果が期待どおりであることを確認します。

{% alert note %}
Braze ではリッチ プッシュの設定方法についての手順が提供されていますが、リッチ プッシュ通知の実際のレンダリングは、デバイスのアスペクト比、Android のバージョン、OEM 固有の制約などの外部要因によって異なる場合があります。リッチ プッシュ通知が意図したとおりに表示されるかどうかを確認するために、複数の Android デバイスへの送信テストを実行することをお勧めします。
{% endalert %}

## Androidのリッチ通知を設定する

### ステップ 1:キャンペーンを作成する

Android 用のプッシュ通知を作成するための [キャンペーンを作成する][3] 手順に従います。リッチ コンテンツを含まないプッシュ通知を設定する場合も、同じコンポーザーを使用します。

### ステップ 2:キャプションを追加する

通知内の画像の前に表示する **概要テキスト/画像キャプション** を追加します。

![][9]

### ステップ 3:メディアを追加

メッセージの作成画面の **「拡張通知画像」** フィールドに画像を追加します。画像はダッシュボードから直接アップロードすることも、他の場所でホストされているコンテンツ URL を指定してアップロードすることもできます。

サポートされている画像の詳細については、 [画像仕様]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#push)をご覧ください。

![][8]

### ステップ 4: キャンペーンの作成を続ける

リッチ通知コンテンツがダッシュボードにアップロードされたら、 [キャンペーンのスケジュール設定を][6]続行できます。

[3]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
[6]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/
[8]: {% image_buster /assets/img_archive/android_rich_image.png %}
[9]: {% image_buster /assets/img_archive/android_rich_summarytext.png %}
