---
nav_title: "Androidリッチ通知"
article_title: Android向けリッチ通知
page_order: 3
page_layout: tutorial
description: "このチュートリアルでは、BrazeキャンペーンにAndroidリッチ通知を設定する方法を説明する。"
platform: Android
channel:
  - Push
tool:
  - Campaigns
  
---

# アンドロイドのリッチ通知

> リッチ通知では、コピーだけでなく追加のコンテンツを追加することで、プッシュ通知をよりカスタマイズすることができる。Androidの通知機能には、以前からプッシュ通知に画像が含まれており、「拡張通知画像」と呼ばれている。

## 要件

- クイックプッシュキャンペーンを作成する際、Androidのリッチ通知は利用できない。
- 拡張通知ビューは、Jelly Bean（Android 4.1）以降の端末でのみ利用できる。ユーザーのデバイスがこれらのシステムで動作していない場合、通知画像は表示されない。
- Androidの拡張通知画像は2:1の比率でなければならないが、サイズ制限はない。
- Androidでは、標準の通知ビューに別の画像を設定することもできる。これらは推奨サイズの画像である： 
  - 小さい：512x256
  - ミディアムだ：1024x512 
  - 大きい：2048x1024
- 現在、Androidのリッチ通知では、JPEGやPNGなどの静止画像しか使えない。GIFやその他の画像フォーマットはまだサポートされていない。
- プッシュ通知にアクションボタンを追加すると、表示可能な画像の領域に影響を与える可能性がある。ダッシュボードのプレビューと実機でテストし、結果が期待通りであることを確認する。

{% alert note %}
Brazeはリッチプッシュの設定方法を提供しているが、リッチプッシュ通知の実際のレンダリングは、デバイスの縦横比、Androidのバージョン、OEM固有の制約などの外部要因によって異なる可能性がある。リッチプッシュ通知が意図したとおりに表示されることを確認するために、複数のAndroidデバイスに送信テストを行うことをお勧めする。
{% endalert %}

## アンドロイドのリッチ通知を設定する

### ステップ 1:キャンペーンを作成する

Android用のプッシュ通知を作成するための[キャンペーンを作成][3]するためのステップに従う。リッチコンテンツを含まないプッシュ通知の設定には、同じコンポーザーを使うことになる。

### ステップ 2:キャプションを追加する

通知の画像の前に表示したい**要約テキスト／画像キャプションを**追加する。

![][9]

### ステップ 3:メディアを追加する

メッセージのコンポーザーにある**Expanded Notification Image**フィールドに画像を追加する。画像は、ダッシュボードから直接アップロードすることも、他の場所でホストされているコンテンツURLを指定してアップロードすることもできる。

対応画像の詳細については、[画像仕様を]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#push)参照のこと。

![][8]

### ステップ 4:キャンペーンの作成を続ける

リッチ通知コンテンツがダッシュボードにアップロードされた後、[キャンペーンのスケジューリングを][6]続けることができる。

[3]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
[6]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/
[8]: {% image_buster /assets/img_archive/android_rich_image.png %}
[9]: {% image_buster /assets/img_archive/android_rich_summarytext.png %}
