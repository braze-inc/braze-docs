---
nav_title: サイレントプッシュ通知
article_title: Android のサイレントプッシュ通知
platform: Android
page_order: 3
description: "この記事では、Android アプリケーションにサイレントプッシュ通知を実装する方法について説明します。"
channel:
  - push

---

# Android用のサイレントプッシュ通知

> サイレント通知を使用すると、重要なイベントが発生したときにバックグラウンドでアプリに通知できます。たとえば、新しいインスタントメッセージを配信したり、雑誌の新刊を公開したり、ニュース速報アラートを送信したりするほか、ユーザーのお気に入りのテレビ番組の最新エピソードをダウンロードしてオフラインで視聴する準備ができたため、それを知らせる場合などです。サイレント通知は、バックグラウンドでの取得間の遅延が許容できないような、散発的だが即時に必要なコンテンツに適しています。

## サイレント・プッシュ通知を設定する

サイレント通知は Braze[Messaging API]({{site.baseurl}}/api/endpoints/messaging/) を通じて利用できます。これらを利用するには、[Android push object]({{site.baseurl}}/api/objects_filters/messaging/android_object/) 内で`send_to_sync` フラグを`true` に設定し、`title` または`alert` フィールドが設定されていないことを確認する必要があります。これは、`send_to_sync`-とともに使用するとエラーが発生するためですが、オブジェクト内にデータ`extras`

{% alert tip %}
[プッシュ通知メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message//?tab=android#step-4-compose-your-push-message)を作成すると、1つのスペースだけでメッセージを送信することで、サイレントAndroidプッシュ通知を送信できます。これは、プッシュ通知の送信に推奨される方法である**not** ですが、場合によっては役立つことがあります。
{% endalert %}

