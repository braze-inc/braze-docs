---
nav_title: サイレントプッシュ通知
article_title: FireOS のサイレントプッシュ通知
platform: FireOS
page_order: 3

page_type: reference
description: "このリファレンス記事では、サイレント FireOS プッシュ通知を送信する方法と、サイレントプッシュ通知を使用するのが望ましい状況のユースケースについて説明します。"
channel: push

---

# サイレントプッシュ通知

> サイレント通知を使用すると、重要なイベントが発生したときにバックグラウンドでアプリに通知できます。たとえば、新しいインスタントメッセージを配信したり、雑誌の新刊を公開したり、ニュース速報アラートを送信したりするほか、ユーザーのお気に入りのテレビ番組の最新エピソードをダウンロードしてオフラインで視聴する準備ができたため、それを知らせる場合などです。サイレント通知は、バックグラウンドでの取得間の遅延が許容できないような、散発的だが即時に必要なコンテンツに適しています。

サイレント通知は Braze[Messaging API]({{site.baseurl}}/api/endpoints/messaging/) を通じて利用できます。サイレント通知を利用するには、[Android プッシュオブジェクト]({{site.baseurl}}/api/objects_filters/messaging/android_object/)内で `send_to_sync` フラグを `true` に設定します。また、`title` または `alert` フィールドを `send_to_sync` とともに使用するとエラーが発生するため、それらが設定されていないことを確認する必要があります。ただし、データ `extras` をオブジェクト内に含めることはできます。

サイレント通知はダッシュボード内でも利用できます。サイレント通知を送信するには、図に示すように、通知のタイトルと本文のフィールドが空白であることを確認します。

![]({% image_buster /assets/img_archive/SilentPushExample.png %} "サイレントプッシュ通知の例 -- Android")

