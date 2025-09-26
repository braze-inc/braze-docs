---
nav_title: "リッチプッシュ通知の作成"
article_title: "Androidのリッチプッシュ通知の作成"
page_order: 3
page_layout: tutorial
description: "このチュートリアルでは、BrazeキャンペーンにAndroidリッチ通知を設定する方法を説明する。"
platform: Android
channel:
  - Push
tool:
  - Campaigns
  
---

# Androidのリッチプッシュ通知の作成

> リッチ通知では、コピーだけでなく追加のコンテンツを追加することで、プッシュ通知をよりカスタマイズすることができる。Androidの通知機能には、以前からプッシュ通知に画像が含まれており、「拡張通知画像」と呼ばれている。

## 前提条件

Android のリッチプッシュ通知を作成する前に、次の点に注意してください。

- クイックプッシュキャンペーンを作成する際、Androidのリッチ通知は利用できない。
- Androidの拡張通知画像は2:1の比率でなければならないが、サイズ制限はない。
- Androidでは、標準の通知ビューに別の画像を設定することもできる。これらは推奨サイズの画像である： 
  - **小:**512x256
  - **中:**1024x512 
  - **大:**2048x1024
- 現在、Androidのリッチ通知では、JPEGやPNGなどの静止画像しか使えない。GIFやその他の画像フォーマットはまだサポートされていない。
- プッシュ通知にアクションボタンを追加すると、表示可能な画像の領域に影響を与える可能性がある。ダッシュボードプレビューとライブデバイスを使用してテストし、結果が期待どおりであることを確認します。

{% alert note %}
Brazeはリッチプッシュの設定方法を提供しているが、リッチプッシュ通知の実際のレンダリングは、デバイスの縦横比、Androidのバージョン、OEM固有の制約などの外部要因によって異なる可能性がある。リッチプッシュ通知が意図したとおりに表示されることを確認するために、複数のAndroidデバイスに送信テストを行うことをお勧めする。
{% endalert %}

## Android のリッチプッシュ通知の設定

### ステップ1:プッシュキャンペーンを作成する

Android用のプッシュ通知を作成するための[キャンペーンを作成]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message)するためのステップに従う。リッチコンテンツを含まないプッシュ通知の設定には、同じコンポーザーを使うことになる。

### ステップ 2: キャプションを追加する

通知の画像の前に表示する **要約テキスト / 画像キャプション**を追加します。

![画像を追加したり、画像URLを入力したりできる拡張通知画像セクション。]({% image_buster /assets/img_archive/android_rich_summarytext.png %})

### ステップ 3:メディアを追加する

メッセージのコンポーザーにある**Expanded Notification Image**フィールドに画像を追加する。画像は、ダッシュボードから直接アップロードすることも、他の場所でホストされているコンテンツ URL を指定してアップロードすることもできます。

サポートしている画像の詳細については、「[画像の仕様]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#push)」を参照してください。

![ユーザーが iOS のプッシュ通知を受け取る。タイトルは「Hi there」、テキストは「Thanks for joining out loyalty program!」である。]({% image_buster /assets/img_archive/android_rich_image.png %})

### ステップ4:キャンペーンの作成を続ける

リッチプッシュ通知がダッシュボードにアップロードされたら、[キャンペーンのスケジューリング]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/)を続行できます。

