---
nav_title: WhatsAppセットアップ
article_title: WhatsAppセットアップ
alias: /partners/whatsapp/
description: "この記事では、Braze WhatsAppチャネルの設定方法と、前提条件と推奨される次のステップについて説明します。"
page_type: partner
search_tag: Partner
page_order: 0
channel:
  - WhatsApp
search_rank: 2
---

# WhatsAppのセットアップ

> [ワッツアップ](https://www.whatsapp.com/) ビジネスメッセージングは、世界中で使用されている人気のあるピアツーピアメッセージングプラットフォームであり、企業に会話ベースのメッセージングを提供します。	

## 前提 条件

統合を続行する前に、次の点を確認してください。

- **オプトインポリシー:**WhatsAppでは、企業に顧客にメッセージングをオプトインしてもらう必要があります。
- **WhatsAppコンテンツルール:**WhatsAppには、従う必要のある [いくつかのコンテンツルール](https://www.whatsapp.com/legal/commerce-policy?l=en) があります。
- **コンプライアンス：**該当するすべてのBrazeおよびMetaのドキュメント、および該当する [Metaポリシー](https://www.whatsapp.com/legal/?lang=en)を遵守します。
- **24時間の会話制限:**企業が最初のテンプレート メッセージを送信するか、ユーザーがメッセージを送信した後、24 時間のウィンドウが発生し、2 つの当事者がメッセージをやり取りできます。 
- **会話の開始:**ユーザーはいつでも会話を開始できます。ビジネスは、承認されたメッセージテンプレートを介してのみ会話を開始できます。
- **アカウントの制限:**各Brazeワークスペースは、1つのWhatsApp Businessアカウント、サブスクリプショングループ、電話番号を保持できます。さらに、各WhatsApp Businessアカウントは [、1つのサードパーティ統合](https://developers.facebook.com/docs/whatsapp/embedded-signup/faq#faq_194614375799047)しか保持できません。
<br><br>

|要件|説明|
| ---| --- |
|Metaビジネスマネージャアカウント |このメッセージングチャネルを利用するには、Metaビジネスアカウントが必要です。|
|WhatsApp Businessアカウント |このメッセージングチャネルを利用するには、WhatsApp Businessアカウントが必要です。|
|WhatsAppの電話番号 |メッセージングチャネルを使用するための [WhatsAppの要件を満たす](https://developers.facebook.com/docs/whatsapp/phone-numbers/) 電話番号を取得する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ 1:WhatsApp MessengerをBrazeに接続する

Brazeで、[ **Partner Integrations** ]>[ **Technology Partners** ]に移動し、 **WhatsApp**を検索します。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、[**統合]** の下に **[テクノロジ パートナー]** があります。
{% endalert %}

WhatsAppパートナーページで、[ **Facebookでログイン** ]を選択して統合プロセスを開始します。

![][1]{: style="max-width:70%;"}

会社にすでに少なくとも1つのMetaビジネスアカウントをお持ちである可能性があります。その場合は、WhatsApp Businessアカウントを存続させたいものを選択してください。WhatsAppのユーザー権限とビジネス認証は、Meta Businessアカウントで一元管理されます。

### ステップ 2:WhatsAppのセットアップ
次に、Brazeのセットアップワークフローが表示されます。このフローでは、次のことを行います。
1\.MetaアカウントとWhatsApp Businessアカウントを作成または選択します。[WhatsAppの表示名のガイドライン](https://www.facebook.com/business/help/757569725593362)を必ず確認してください。
2\.WhatsApp Businessのプロフィールを作成します。
3\.WhatsApp Business 番号を検証する<br><br>

	![][2]{: style="max-width:100%;"}

{% alert note %}
WhatsAppビジネスアカウント(WABA)は、複数のビジネスソリューションプロバイダーと共有することはできません。Brazeワークスペースごとに特定のWABAが必要です。
{% endalert %}	

セットアップが完了すると、ユーザー専用のWhatsAppサブスクリプショングループが作成されます。

### ステップ 3:WhatsAppテンプレートを作成する

承認されたWhatsAppメッセージテンプレートのみを使用して、顧客との会話を開始できます。WhatsAppテンプレートは、 [Metaビジネスマネージャー](https://www.facebook.com/business/help/2055875911147364?id=2129163877102343)で作成できます。BrazeがサポートするWhatsAppメッセージング機能のリストについては、 [サポートされているWhatsApp機能]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#supported-whatsapp-features)をご覧ください。

1. **[テンプレートマネージャー](https://business.facebook.com/wa/manage/message-templates)に移動します**<br>
Metaビジネスマネージャの **[アカウントツール**]で、[ **メッセージテンプレート**]を選択します。
次に、 **[テンプレートの作成**] を選択します。<br><br>![][3]{: style="max-width:100%;"}<br><br>
2. **メッセージ設定**<br>
新しいメッセージテンプレートコンポーザーで、メッセージのカテゴリを選択し、テンプレートに名前を付けて、サポートする言語を選択します。言語は後で削除または追加できます。<br><br> 
	使用可能なメッセージテンプレートのカテゴリには、次のものがあります。
	- マーケティングプロモーションオファーや製品発表などを送信して、認知度とエンゲージメントを高める
	- 効用：アカウントの更新、注文の更新、アラートなどを送信して、重要な情報を共有します
	- 認証顧客が自分のアカウントにアクセスできるようにするコードを送信する<br><br> 
	![][4]{: style="max-width:100%;"}<br><br>
3. **テンプレートの編集**<br>
次に、メッセージテンプレートを作成するように求められます。<br><br>ここでは、テキストまたはメディアのヘッダー、テキスト本文、メッセージフッター、およびボタンを指定できます。ビデオとドキュメントのヘッダーは現在使用できず、ヘッダーはテキストまたは画像のいずれかのタイプである必要があります。メッセージのプレビューが右側に表示されます。<br><br>MetaはLiquidをサポートしていませんが、後でBraze for Liquid変数で置き換えることができる変数をテンプレート化できます。これを行うには、 **[+ 変数の追加** ] ボタンを選択します。<br><br>![][5]{: style="max-width:100%;"}<br><br>テンプレートが完成したら、[ **送信**]を押します。 

#### テンプレートの承認時間

メッセージテンプレートの承認ステータスは、Metaビジネスマネージャの **[メッセージテンプレート** ]ページ、またはBrazeでキャンペーンやキャンバスを作成するときに確認できます。さらに、通知権限に応じて、WhatsAppチームから電子メールで通知を受け取ることができます。 

{% alert note %}
承認済みテンプレートは、必要な数のキャンペーンやキャンバスで使用できます。また、オプトインしたユーザー数だけ送信することもできます。これは、テンプレートの品質が低下しない限り当てはまります。
{% endalert %}

### ステップ 4: WhatsAppキャンペーンを作成する

WhatsAppテンプレートが承認されたら、ダッシュボードに移動してWhatsApp [キャンバスまたはキャンペーン]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/)を構築できます。 

{% alert note %}
WhatsAppビジネスアカウントが作成されると、Metaが開始メッセージの制限を決定します。詳細については、「 [スループット]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/10dlc/#throughput)」を参照してください。
{% endalert %}

## 次のステップ:

統合が完了したら、次の 2 つの Meta プロセスを完了することをお勧めします。
- [ビジネス認証](https://www.facebook.com/business/help/2058515294227817?id=180505742745347)
	\- 既存のMetaビジネスマネージャをご利用いただいている場合は、すでにビジネス認証を取得している可能性があります。
- [公式ビジネスアカウント](https://www.facebook.com/business/help/604726921052590?ref=search_new_0)

また、 [ユーザーの電話番号]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/) について読み、 [組織でメッセージテンプレート](https://www.facebook.com/business/help/2169003770027706?id=2190812977867143)を作成するためにアクセスする必要があるユーザーを追加することをお勧めします。


[1]: {% image_buster /assets/img/whatsapp/whatsapp1.png %}
[2]: {% image_buster /assets/img/whatsapp/whatsapp10.png %}
[3]: {% image_buster /assets/img/whatsapp/whatsapp2.png %}
[4]: {% image_buster /assets/img/whatsapp/whatsapp3.png %}
[5]: {% image_buster /assets/img/whatsapp/whatsapp4.png %}
[6]: {% image_buster /assets/img/whatsapp/whatsapp5.png %} 
