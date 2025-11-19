---
nav_title: API トリガー配信
article_title: API トリガー配信
page_order: 2
page_type: reference
description: "このリファレンス記事では、API トリガーキャンペーンのスケジュールと設定方法について説明します。"
tool: Campaigns
platform: API

---

# API トリガー配信

> API トリガーキャンペーンまたはサーバートリガーキャンペーンは、より高度なトランザクションユースケースに最適です。Braze API によってトリガーされるキャンペーンでは、マーケターはキャンペーンのコピー、多変量テスト、再適格性ルールを Braze ダッシュボード内で管理しながら、自社のサーバーやシステムからそのコンテンツを配信できます。メッセージをトリガーする API リクエストには、メッセージにリアルタイムでテンプレート化する追加データを含めることもできます。

## API を利用したキャンペーンの設定

API トリガーによるキャンペーンの設定には、いくつかのステップが必要です。まず、新しいマルチチャネルまたはシングルチャネルキャンペーンを作成します (多変量テストあり)。

{% alert note %}
API を利用したキャンペーンは、[API キャンペーン]({{site.baseurl}}/developer_guide/rest_api/api_campaigns/#api-campaigns)とは異なります。
{% endalert %}

次に、通常の予約通知と同じようにコピーと通知を設定し、**API トリガー配信**を選択します。サーバーからこれらのキャンペーンをトリガーする方法については、こちらの [API トリガーキャンペーン送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)記事をご覧ください。

![]({% image_buster /assets/img_archive/api_triggered_campaign_delivery.png %})

## API リクエストに含まれるテンプレート化されたコンテンツを使用する

メッセージのトリガーに加えて、API リクエストを含むコンテンツを`trigger_properties`オブジェクト内にテンプレート化することもできます。この内容はメッセージの本文で参照できます。たとえば、次のものを含めることができます。
``{% raw %} {{ api_trigger_properties.${ some_value_included_with_request }}} {% endraw %}``。追加のコンテキストについては、次のソーシャル通知の例を参照してください。

![前述のトリガープロパティは、メッセージに含まれ、ユーザーの名前と次のテキストを自動入力します。「あなたの写真にいいねしました。彼らが何をしていたかを見るにはここをクリック」]({% image_buster /assets/img_archive/api_triggered_photo_social_example_1.png %}){: style="max-width:70%;"}

## API トリガーキャンペーンで再利用可能

ユーザーが API トリガーキャンペーンを受け取る回数は、再資格設定を使用して制限できます。つまり、API トリガーが何回起動されたかにかかわらず、ユーザーは 1 回のみ、または特定の期間中に 1 回キャンペーンを受け取ることになります。

たとえば、API トリガーのキャンペーンを使用して、ユーザーが最近閲覧したアイテムに関するキャンペーンを送信しているとします。この場合、各アイテムの API トリガーを起動している間、閲覧したアイテムの数に関係なく、1 日 1 回までメッセージを送信するようにキャンペーンを制限できます。一方、API トリガーのキャンペーンがトランザクションベースの場合、遅延時間を 0 分に設定することで、ユーザーがトランザクションを実行するたびにキャンペーンを受け取るようにできます。

![]({% image_buster /assets/img_archive/api_triggered_reeligible.png %})


