---
nav_title: "通知オプション"
article_title: Androidの通知オプション
page_order: 2
page_type: reference
description: "この参考記事では、いくつかのAndroid通知オプションと、Brazeのキャンペーンでそれらを最適に使用する方法について説明する。"

platform: Android
channel:
  - Push

---

# 通知オプション

> これらは、Brazeで利用可能なAndroid特有のプッシュ通知オプションの一部である。

## サイレント通知

[プッシュ通知メッセージを作成する]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/?tab=android#step-4-compose-your-push-message)際、Android プッシュメッセージはタイトルなしでは送信**できません**。ただし、代わりに1つのスペースを入力できます。メッセージにスペースが1つしか含まれていない場合、無音のプッシュ通知として送信されることを覚えておいてほしい。詳しくは、[サイレント・プッシュ]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android)通知を参照のこと。

## 通知グループ

メッセージを分類してユーザーの通知トレイにグループ分けしたい場合は、Brazeを通じてAndroidの通知チャンネル機能を利用できる。

まず、Androidプッシュ通知キャンペーンを作成し、[**メール作成]**タブの一番上にある[**通知チャネル**]ドロップダウンを探す。

![]({% image_buster /assets/img_archive/notification_channel_dropdown.png %}){: style="max-width:60%;"}

ドロップダウンから通知チャンネルを選択する。また、[通知チャネル] 設定で不具合が生じた場合に備えて、フォールバックチャネルを選択する必要があります。

ここに[通知チャンネルが]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/)ない場合は、通知チャンネルIDを使って追加できる。社内の開発者に連絡し、通知チャネル ID を確認するか、必要に応じて新しい ID を作成します。 

通知 ID を通知チャネル に追加するには、[**通知チャネル**] ドロップダウンメニューの [**通知チャネルを管理**] をクリックし、必須フィールドに入力します。通知チャネルを Braze プラットフォームで使用するには、アプリ上で通知チャネルを定義する必要があります。

![]({% image_buster /assets/img_archive/notification_channels.png %}){: style="max-width:80%;" }


