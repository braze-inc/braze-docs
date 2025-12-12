---
nav_title: WhatsAppのセットアップ
nav_title: WhatsAppのセットアップ
article_title: WhatsApp設定
alias: /partners/whatsapp/
description: "この記事では、Braze WhatsApp チャネルを設定する方法について、前提条件や推奨される次のステップを含めて説明します。"
page_type: partner
search_tag: Partner
page_order: 1
channel:
  - WhatsApp
search_rank: 2
---

# WhatsAppのセットアップ

> [WhatsApp](https://www.whatsapp.com/)Businessメッセージングは、世界中で利用されている人気のピアツーピアメッセージングプラットフォームで、ビジネス向けに会話ベースのメッセージングを提供している。	

## 前提条件

統合を進める前に以下を確認する：

- **オプトインポリシー:**WhatsApp は、顧客がメッセージングにオプトインすることを企業に義務付けています。
- **WhatsApp のコンテンツルール:**WhatsAppには守るべき[コンテンツルールが](https://www.whatsapp.com/legal/commerce-policy?l=en)いくつかある。
- **コンプライアンス:**適用されるすべての Braze および Meta の文書と、適用される [Meta のポリシー](https://www.whatsapp.com/legal/?lang=en)に従います。
- **24 時間の会話制限:**企業が最初にテンプレート化されたメッセージを送信した後、あるいはユーザーがメッセージを送信した後、両者がメッセージをやり取りできる24時間のウィンドウが発生する。 
- **会話を始める:**ユーザーはいつでも会話を始めることができる。企業は、承認されたメッセージテンプレートによってのみ会話を開始することができる。
<br><br>

| 必要条件| 説明|
| ---| --- |
| Facebook Business Manager アカウント | このメッセージングチャネルを活用するには、Meta Business アカウントが必要です。 |
| WhatsApp ビジネスアカウント | このメッセージングチャネルを利用するには、WhatsApp Business アカウントが必要です。 |
| WhatsAppの電話番号 | メッセージングチャネルを利用するには、WhatsApp の[クラウド API](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) または[オンプレミス API ](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers)の要件を満たす電話番号を取得する必要があります。  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ 1: WhatsApp Messenger を Braze に接続する

Braze の [**パートナー連携**] > [**テクノロジーパートナー**] に移動して、[**WhatsApp**] を検索します。

WhatsApp パートナーページで、[**統合を開始**] を選択します。

![パートナページをWhatsAppして、インテグレーションを開始します。]({% image_buster /assets/img/whatsapp/whatsapp1.png %}){: style="max-width:70%;"}

開いたウィンドウで [**次へ**] を選択し、[**統合を開始**] ボタンが表示されるまで続けます。ボタンを選択し、統合プロセスを開始します。

![BrazeをWhatsAppに接続するための指示。]({% image_buster /assets/img/whatsapp/instructions.png %}){: style="max-width:50%;"}

### ステップ 2: WhatsAppのセットアップ

次に、Brazeセットアップのワークフローが表示される。ステップバイステップのウォークスルーについては、[WhatsApp 埋め込みサインアップ]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/)を参照してください。 

このフローでは、次のようになります。
1. Meta と WhatsApp Business アカウントを作成または選択します。[WhatsApp の表示名のガイドライン](https://www.facebook.com/business/help/757569725593362)を必ず確認してください。<br><br>御社にはすでに少なくとも 1 つの既存の Meta Business アカウントがあると考えられます。その場合は、WhatsApp Business アカウントを配置したいアカウントを選択します。WhatsApp のユーザー権限とビジネス認証は Meta Business アカウントで一元管理されます。<br><br>
2. WhatsApp Business プロファイルを作成します。
3. WhatsApp Business 番号を確認します。<br><br>

設定が完了すると、ユーザー専用の WhatsApp 購読グループが作成されます。

### ステップ 3: WhatsAppテンプレートを作成する

承認された WhatsApp メッセージテンプレートのみを使用して、顧客との会話を開始できます。WhatsApp テンプレートは [Meta Business Manager](https://www.facebook.com/business/help/2055875911147364?id=2129163877102343) で作成できます。Braze でサポートされる WhatsApp メッセージ機能の一覧は、[サポートされる WhatsApp 機能]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#supported-whatsapp-features)を参照してください。

1. [**[テンプレートマネージャー](https://business.facebook.com/wa/manage/message-templates)**] に移動します。<br>
Meta Business Manager で、**Account Tools** の下にある [**メッセージテンプレート**] を選択します。
次に、[**テンプレートを作成**] を選択します。<br><br>![WhatsAppマネージャ。メッセージテンプレートの一覧が表示されます。]({% image_buster /assets/img/whatsapp/whatsapp2.png %}){: style="max-width:100%;"}<br><br>
2. **メッセージの設定**<br>
新しいメッセージ・テンプレート・コンポーザーで、メッセージのカテゴリーを選択し、テンプレートに名前を付け、サポートしたい言語を選択する。後で言語を削除したり追加したりすることもできる。<br><br> 
	利用可能なメッセージテンプレートのカテゴリーには以下のものがある：
	- マーケティング: キャンペーンや製品情報などを配信し、認知度とエンゲージメントを高める
	- ユーティリティ: アカウント更新、注文更新、アラートなどを送信し、重要な情報を共有する
	- 認証: 顧客がアカウントにアクセスできるようにするコードを送信する<br><br> 
	![マーケティング、ユーティリティ、認証のカテゴリを持つメッセージテンプレートコンポーザー。]({% image_buster /assets/img/whatsapp/whatsapp3.png %}){: style="max-width:100%;"}<br><br>
3. **テンプレートを編集する**<br>
次に、メッセージテンプレートを作成します。<br><br>テキストまたはメディアヘッダー、テキスト本文、メッセージフッタ、およびボタンを指定できます。現在、ビデオとドキュメントのヘッダーは使用できず、ヘッダーはテキストまたは画像のいずれかでなければなりません。追加したすべてのメディアは、確認処理の例として機能し、**はテンプレートメッセージに含まれていません**。Brazeで用紙を追加する必要があります。画面にメッセージのプレビューが表示されます。<br><br>Meta は Liquid をサポートしていませんが、後で Braze で Liquid 変数に置き換えることができる変数をテンプレート化することができます。[**\+ 変数を追加**] ボタンを選択します。<br><br>![テンプレート作成者]]({% image_buster /assets/img/whatsapp/whatsapp4.png %}){: style="max-width:100%;"}

テンプレートが完成したら、[**送信**] をクリックします。 

#### テンプレート承認時間

メッセージテンプレートの承認状況は、Meta Business Manager の**メッセージテンプレートページ**、または Braze でキャンペーンやキャンバスを作成する際に確認できます。さらに、通知権限に応じてWhatsAppチームからメールで通知されることもある。 

{% alert note %}
承認されたテンプレートは、好きなだけキャンペーンやキャンバスに使用できる。また、好きなだけ多くのオプトインユーザーに送ることができます。テンプレートの品質が低下しない限り、これは事実である。
{% endalert %}

### ステップ 4: WhatsAppキャンペーンを作成する

WhatsApp テンプレートが承認されたら、ダッシュボードに移動して [WhatsApp キャンバスやキャンペーン]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/)を作成できます。 

{% alert note %}
WhatsApp Business Account が作成されると、Meta によって初期のメッセージ制限が決定されます。詳しくは[スループットを]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/10dlc/#throughput)ご覧いただきたい。
{% endalert %}

## 次のステップ

統合が完了したら、次の 2 つの Meta プロセスを完了させることをお勧めします。
- [ビジネス検証](https://www.facebook.com/business/help/2058515294227817?id=180505742745347)
	- 既存の Meta Business Manager を使用している場合は、すでにビジネス検証を行っている可能性があります。 
- [公式ビジネスアカウント](https://www.facebook.com/business/help/604726921052590?ref=search_new_0)

[ユーザーの電話番号]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/)について読み、メッセージ[テンプレートを組織で作成](https://www.facebook.com/business/help/2169003770027706?id=2190812977867143)する必要があるユーザーを追加することをお勧めします。

### WhatsApp Cloud API ローカルストレージ

Braze は WhatsApp の [Cloud API ローカルストレージ](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/local-storage?content_id=ka6F9gESPqhQpm5)をサポートしています。これを有効にするには、Brazeカスタマーサポートマネージャーに連絡すること。

