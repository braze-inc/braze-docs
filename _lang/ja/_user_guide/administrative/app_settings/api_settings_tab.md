---
nav_title: API キー
article_title: API キー
page_order: 3
page_type: reference
description: "このリファレンス記事では、ワークスペースの API ID を表示する [API キー] ページについて説明します。"

---

# API キー

> [**API キー**] ページには、ワークスペースの API ID が表示されます。**サービス**に関する最初のセクションには、Braze API のさまざまな用途 ([ユーザーデータ][3]、[メッセージング][4]、[メール同期][5]、および[エクスポート][6]) に関する関連記事の一覧があります。

[**API キー**] ページはさらに次のセクションに分かれています。

- REST API キー
- 識別
- 追加の API 識別子

[**API キー**] ページは [**設定**] の下にあります。

{% alert note %}
古いナビゲーションを使用している場合、このページは [**API 設定**] と呼ばれ、[**設定**] > [**設定の管理**] にあります。
{% endalert %}

### REST API キー

このセクションには、ワークスペース REST API キーが表示されます。これは、ワークスペースのデータへのアクセスを可能にする一意の識別子です。Braze API へのリクエストのそれぞれに、REST API キーが必要です。API キーの作成と使用の詳細については、「[REST API キーの概要]({{site.baseurl}}/api/api_key/)」を参照してください。

#### API IP の許可リスト

さらなるセキュリティ強化のため、特定の REST API キーに対する REST API リクエストが許可されている IP アドレスおよびサブネットのリストを指定できます。これは、許可リストまたはホワイトリストと呼ばれます。特定の IP アドレスやサブネットを許可するには、新規の REST API キーの作成時に [**IP をホワイトリストに追加**] セクションにそれらを追加します。 

![新規 API キー作成時の API の [IP をホワイトリストに追加] セクション][26]

何も指定しない場合、すべての IP アドレスからリクエストを送信できます。

{% alert tip %}
Braze to Braze webhook を作成し、許可リストを使用する場合は、[ホワイトリストに追加する IP]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-whitelisting) のリストを確認してください。
{% endalert %}

### 識別

このセクションには、Braze API へのリクエストで特定のアプリを参照するために使用される識別子のリストがあります。アプリケーション識別子の詳細については、「[アプリ識別子の API キー]({{site.baseurl}}/api/identifier_types/)」を参照してください。

### 追加の API 識別子

弊社の API と連携する目的で、Braze 外部の API からアクセスしようとする任意のセグメント、キャンペーン、コンテンツカードなどに関連する識別子を検索できます。すべてのメッセージは [UTF-8][12] エンコーディングに従う必要があります。いずれかを選択すると、ドロップダウンメニューの下に識別子が表示されます。

詳細については、「[API 識別子のタイプ]({{site.baseurl}}/api/identifier_types/)」を参照してください。

[3]: {{site.baseurl}}/api/endpoints/user_data/
[4]: {{site.baseurl}}/api/endpoints/messaging/
[5]: {{site.baseurl}}/api/endpoints/email/
[6]: {{site.baseurl}}/api/endpoints/export/
[12]: https://en.wikipedia.org/wiki/UTF-8 "Wikipedia: UTF-8"
[26]: {% image_buster /assets/img_archive/api-key-ip-whitelisting.png %}
