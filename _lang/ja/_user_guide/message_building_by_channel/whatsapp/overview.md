---
nav_title: WhatsAppの設定
article_title: WhatsAppの設定
alias: /partners/whatsapp/
description: "この記事では、Braze WhatsAppチャンネルを設定する方法について、前提条件や次のステップを含めて説明する。"
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

- **オプトイン・ポリシー：**WhatsAppは、顧客がメッセージングにオプトインすることを企業に求めている。
- **WhatsAppのコンテンツルール：**WhatsAppには守るべき[コンテンツルールが](https://www.whatsapp.com/legal/commerce-policy?l=en)いくつかある。
- **コンプライアンスだ：**適用されるすべてのBrazeおよびMetaの文書と、適用される[Metaのポリシーに](https://www.whatsapp.com/legal/?lang=en)従うこと。
- **24時間の会話制限：**企業が最初にテンプレート化されたメッセージを送信した後、あるいはユーザーがメッセージを送信した後、両者がメッセージをやり取りできる24時間のウィンドウが発生する。 
- **会話を始める：**ユーザーはいつでも会話を始めることができる。企業は、承認されたメッセージテンプレートによってのみ会話を開始することができる。
- **アカウントの制限：**Brazeの各ワークスペースには1つのWhatsApp Businessアカウント、サブスクリプショングループ、電話番号を保存できる。さらに、WhatsApp Businessアカウント1つにつき、[サードパーティとの統合は1つしか](https://developers.facebook.com/docs/whatsapp/embedded-signup/faq#faq_194614375799047)行えない。
<br><br>

| 必要条件| 説明|
| ---| --- |
| メタ・ビジネス・マネージャー・アカウント | このメッセージング・チャネルを活用するには、Meta Businessアカウントが必要である。 |
| WhatsApp ビジネスアカウント | このメッセージングチャネルを利用するにはWhatsApp Businessアカウントが必要である。 |
| WhatsAppの電話番号 | メッセージングチャンネルを利用するには、WhatsAppの[クラウドAPI](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers)または[オンプレミスAPIの](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers)要件を満たす電話番号を取得する必要がある。  | 
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ 1:WhatsAppメッセンジャーをBrazeに接続する

Brazeの**Partner Integrations**>**Technology Partnersで** **WhatsAppを**検索する。

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、「**統合」の**下に**テクノロジー・パートナーが**ある。
{% endalert %}

WhatsApp パートナーページで "**Begin Integration "**を選択。

![][1]

開封ウィンドウで、**次へ**を選択し、**統合開始**ボタンが表示されるまで続けます。ボタンを選択し、統合プロセスを開始する。

![BrazeとWhatsAppの接続方法。][7]

### ステップ2:WhatsAppのセットアップ

次に、Brazeセットアップのワークフローが表示される。ステップ・バイ・ステップのチュートリアルについては、[WhatsApp埋め込みサインアップを]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/)参照のこと。 

この流れの中で、あなたはこうなる：
1. MetaとWhatsApp Businessアカウントを作成または選択する。[WhatsApp表示名のガイドラインを](https://www.facebook.com/business/help/757569725593362)必ず確認すること。<br><br>あなたの会社には、すでに少なくとも1つの既存のMeta Businessアカウントがあると思われる。その場合、WhatsApp Businessアカウントを選択する。WhatsAppのユーザー権限とビジネス認証はMeta Businessアカウントで一元管理される。<br><br>
2. WhatsApp Businessプロフィールを作成する。
3. WhatsApp Business番号を確認する<br><br>

{% alert note %}
WhatsAppビジネスアカウント(WABA)は複数のビジネスソリューションプロバイダーと共有することはできない。Brazeのワークスペースごとに特定のWABAが必要になる。
{% endalert %}	

設定完了後、ユーザー専用のWhatsApp購読グループが作成される。

### ステップ 3:WhatsAppテンプレートを作成する

顧客との会話に使用できるのは、承認されたWhatsAppメッセージテンプレートのみである。WhatsAppテンプレートは[Meta Business Managerで](https://www.facebook.com/business/help/2055875911147364?id=2129163877102343)作成できる。BrazeがサポートするWhatsAppメッセージ機能の一覧は、[サポートされるWhatsApp機能を]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#supported-whatsapp-features)ご覧下さい。

1. **[テンプレート・マネージャーに](https://business.facebook.com/wa/manage/message-templates)移動する**<br>
Meta Business Managerで、**Account Toolsの**下にある**Message Templatesを**選択する。
次に、**Create Templatesを**選択する。<br><br>![][3]{: style="max-width:100%;"}<br><br>
2. **メッセージ設定**<br>
新しいメッセージ・テンプレート・コンポーザーで、メッセージのカテゴリーを選択し、テンプレートに名前を付け、サポートしたい言語を選択する。後で言語を削除したり追加したりすることもできる。<br><br> 
	利用可能なメッセージテンプレートのカテゴリーには以下のものがある：
	- マーケティングだ：キャンペーンや製品情報などを配信し、認知度とエンゲージメントを高める
	- ユーティリティだ：アカウント更新、注文更新、アラートなどを送信し、重要な情報を共有する
	- 認証を行う：顧客がアカウントにアクセスできるコードを送信する<br><br> 
	![][4]{: style="max-width:100%;"}<br><br>
3. **テンプレートを編集する**<br>
次に、メッセージ・テンプレートを作成するよう促される。<br><br>ここでは、テキストまたはメディアヘッダー、本文、メッセージフッター、ボタンを提供することができる。また、ヘッダーはテキストか画像タイプでなければならない。メッセージのプレビューが右側に表示される。<br><br>MetaはLiquidをサポートしていないが、BrazeでLiquidの変数に置き換えることができる変数をテンプレートすることができる。**変数の追加**ボタンを選択する。<br><br>![][5]{: style="max-width:100%;"}<br><br>テンプレートが完成したら、**Submitを**押す。 

#### テンプレート承認時間

メッセージテンプレートの承認状況は、Meta Business Managerの**メッセージテンプレートページ**、またはBrazeでキャンペーンやキャンバスを作成する際に確認できる。さらに、通知権限に応じてWhatsAppチームからメールで通知されることもある。 

{% alert note %}
承認されたテンプレートは、好きなだけキャンペーンやキャンバスに使用できる。また、好きなだけ多くのオプトイン・ユーザーに送ることができる。テンプレートの品質が低下しない限り、これは事実である。
{% endalert %}

### ステップ 4:WhatsAppキャンペーンを作成する

WhatsAppテンプレートが承認されたら、ダッシュボードに移動して[WhatsAppキャンバスやキャンペーンを]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/)作成できる。 

{% alert note %}
WhatsApp ビジネスアカウント作成後、Meta がメッセージ送信の上限を決定する。詳しくは[スループットを]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/10dlc/#throughput)ご覧いただきたい。
{% endalert %}

## 次のステップ

統合が完了したら、次の2つのMetaプロセスを完了させることをお勧めする：
- [ビジネス検証](https://www.facebook.com/business/help/2058515294227817?id=180505742745347)
	- 既存のメタ・ビジネス・マネージャーを使用している場合は、すでにビジネス認証を受けているかもしれない。 
- [公式ビジネスアカウント](https://www.facebook.com/business/help/604726921052590?ref=search_new_0)

また、[ユーザーの電話番号]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/)について読むことをお勧めします。組織でメッセージ[テンプレートを作成する必要があるユーザーを追加してください](https://www.facebook.com/business/help/2169003770027706?id=2190812977867143)。

### WhatsApp Cloud API ローカルストレージ

BrazeはWhatsAppの[クラウドAPIローカルストレージを](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/local-storage?content_id=ka6F9gESPqhQpm5)サポートしている。これを有効にするには、Brazeカスタマーサポートマネージャーに連絡すること。

[1]: {% image_buster /assets/img/whatsapp/whatsapp1.png %}
[2]: {% image_buster /assets/img/whatsapp/whatsapp10.png %}
[3]: {% image_buster /assets/img/whatsapp/whatsapp2.png %}
[4]: {% image_buster /assets/img/whatsapp/whatsapp3.png %}
[5]: {% image_buster /assets/img/whatsapp/whatsapp4.png %}
[6]: {% image_buster /assets/img/whatsapp/whatsapp5.png %}
[7]: {% image_buster /assets/img/whatsapp/instructions.png %} 
