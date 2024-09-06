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

> メッセージを分類してユーザーの通知トレイにグループ分けしたい場合は、Brazeを通じてAndroidの通知チャンネル機能を利用できる。

Androidプッシュ・キャンペーンを作成し、**\[メール送信]**タブの一番上にある\[**通知チャンネル**]ドロップダウンを探す。

![][28]{: style="max-width:60%;" }

ドロップダウンから通知チャンネルを選択する。また、通知チャンネル設定が誤動作した場合の予備チャンネルを選択する必要がある。

ここに[通知チャンネルが]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/)ない場合は、通知チャンネルIDを使って追加できる。開発者に連絡し、通知チャネルIDを確認するか、必要に応じて新しいIDを作成する。 

通知チャネルに通知IDを追加するには、**通知チャネルの**ドロップダウンメニューで**通知チャネルを管理を**クリックし、必要なフィールドに記入する。通知チャンネルは、Brazeプラットフォームで使用する前に、アプリ上で定義する必要がある。

![][29]{: style="max-width:80%;" }


[28]: {% image_buster /assets/img_archive/notification_channel_dropdown.png %}
[29]: {% image_buster /assets/img_archive/notification_channels.png %}
