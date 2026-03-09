---
nav_title: リッチプッシュ通知の作成
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

# Androidのための豊かなプッシュ通知sの作成

> リッチ通知では、コピーだけでなく追加のコンテンツを追加することで、プッシュ通知をよりカスタマイズすることができる。Androidの通知機能には、以前からプッシュ通知に画像が含まれており、「拡張通知画像」と呼ばれている。

## 前提条件

Android のリッチプッシュ通知を作成する前に、次の点に注意してください。

- Android拡張通知 "画像sは2:1の比率でなければなりませんが、サイズ制限はありません。
- Androidでは、標準の通知ビューに別の画像を設定することもできる。これらは推奨サイズの画像である： 
  - **小:**512x256
  - **中:**1024x512 
  - **大:**2048x1024
- 現在、Androidのリッチ通知では、JPEGやPNGなどの静止画像しか使えない。GIFやその他の画像フォーマットはまだサポートされていない。
- プッシュ通知にアクションボタンを追加すると、表示可能な画像の領域に影響を与える可能性がある。ダッシュボードプレビューとライブデバイスを使用してテストし、結果が期待どおりであることを確認します。
- "画像をレンダリングするには、Braze Android SDKを有効にする必要があります。

{% alert note %}
Brazeはリッチプッシュの設定方法を提供しているが、リッチプッシュ通知の実際のレンダリングは、デバイスの縦横比、Androidのバージョン、OEM固有の制約などの外部要因によって異なる可能性がある。リッチプッシュ通知が意図したとおりに表示されることを確認するために、複数のAndroidデバイスに送信テストを行うことをお勧めする。
{% endalert %}

## Android のリッチプッシュ通知の設定

### ステップ1:プッシュキャンペーンを作成する

Android用のプッシュ通知を作成するための[キャンペーンを作成]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message)するためのステップに従う。リッチコンテンツを含まないプッシュ通知の設定には、同じコンポーザーを使うことになる。

### ステップ 2: キャプションを追加する

通知の"画像の前に表示する**Summary Text**を追加します。

![ペットフードアプリからのリッチプッシュ通知では、サマリーテキスト付きのスポットのために、より多くの食べ物を注文する時期であることを示す、ドッグと呼ばれた。]({% image_buster /assets/img_archive/android_rich_summarytext.png %})

### ステップ 3:メディアを追加する

メッセージの作成者の**Android通知"画像**フィールドに"画像を追加します。画像は、ダッシュボードから直接アップロードすることも、他の場所でホストされているコンテンツ URL を指定してアップロードすることもできます。

サポートしている画像の詳細については、「[画像の仕様]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#push)」を参照してください。

!["画像を追加したり、"画像のURL を入力したりできるAndroid 通知 "画像欄です。]({% image_buster /assets/img_archive/android_rich_image.png %})

### ステップ 4: キャンペーンの作成を続ける

リッチプッシュ通知がダッシュボードにアップロードされたら、[キャンペーンのスケジューリング]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/)を続行できます。
