---
nav_title: "通知オプション"
article_title: Android 通知オプション
page_order: 2
page_type: reference
description: "このリファレンス記事では、いくつかのAndroid通知オプションと、それらをブレーズキャンペーン内で最適に使用する方法について説明します。"

platform: Android
channel:
  - Push

---

# 通知オプション

> メッセージを分類し、ユーザーの通知トレイにグループ化する場合は、Braze を使用してAndroid の通知チャネル機能を利用できます。

Android プッシュキャンペーンを作成し、**Notification Channel** ドロップダウンの**Compose** タブの最上部を探します。

![][28]{: style="max-width:60%;" }

ドロップダウンから通知チャネルを選択します。また、通知チャネル設定が誤動作した場合は、フォールバックチャネルを選択する必要があります。

ここにリストされている[Notification Channels]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/) がない場合は、Notification Channel ID を使用して追加できます。開発者に問い合わせて、通知チャネルID が何であるかを確認するか、必要に応じて新しいID を作成します。 

Notification ID をNotification Channel に追加するには、**Notification Channel** ドロップダウンメニューで**Manage Notification Channel** をクリックし、必要なフィールドに入力します。Notification Channels は、Braze プラットフォームで使用する前にアプリで定義する必要があります。

![][29]{: style="max-width:80%;" }


[28]: {% image_buster /assets/img_archive/notification_channel_dropdown.png %}
[29]: {% image_buster /assets/img_archive/notification_channels.png %}
