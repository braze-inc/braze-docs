---
nav_title: WhatsAppコネクター
article_title: 独自のWhatsAppコネクターを持ち込む
page_order: 0
description: "このリファレンス記事では、設定が独自のWhatsApp コネクターを起動するためのステップ-by-ステップのウォークスルーを提供します。これにより、Infobip WhatsApp ビジネスマネージャへのBrazeなアクセスが可能になります。"
page_type: reference
channel:
  - WhatsApp
---

# 独自のWhatsAppコネクターを持ち込む

> BYO (Bring Your Own) WhatsApp コネクターは、Infobip WhatsApp ビジネスマネージャ(WABA) へのBrazeの接続を可能にするBraze とInfobip の間の提携を提供します。これにより、セグメンテーション、パーソナライゼーション、およびキャンペーン オーケストレーションにBrazeを使用しながら、インフォビップで直接的にメッセージング費用を管理および支払うことができます。Braze は、送信メッセージ、受信メッセージの処理、WhatsAppの流れ、分析など、WhatsApp チャネルが提供するすべての機能を維持します。

## 要件 

| 要件 | 説明 |
| --- | --- |
| Infobip アカウント | BYO WhatsAppコネクターを使用するには、Infobip アカウントが必要です。
| メールクレジット | WhatsAppを送信すると、Braze メッセージングクレジットを消費します。 |
| WhatsApp要求事項 | すべての[WhatsApp要件]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/#prerequisites)を完了します。 |
| 電話番号 | 便宜上、[Infobip](https://www.infobip.com/docs/numbers/getting-started)を通じて電話番号を取得することをお勧めします。 |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

## セットアップ 

BYO WhatsApp コネクターを設定する前に、WhatsApp 取引先の以前の送信がInfobip で行われていないことを確認します。

### 対応事例

- WhatsAppの取引先と電話番号が以前に取引先に接続されたことがない
- WhatsApp企業取引先は、ネイティブインテグレーションを介してBrazeに直接的に接続されます。
    - [WhatsApp電話番号マイグレーション]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/phone_number_migration/)のステップsに従って、電話番号を一度に1つずつ新しいWhatsApp法人取引先にマイグレーションします。
- WhatsApp 法人取引先がBraze およびInfobip から別のソリューションプロバイダーに接続されている
    - [WhatsApp電話番号マイグレーション]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/phone_number_migration/)のステップsに従って、電話番号を一度に1つずつ新しいWhatsApp法人取引先にマイグレーションします。

## ステップ 1: Infobip アカウント情報の取得 {#step-1}

1. インフォビップで、WhatsAppの法人取引先で使用する取引先を特定します。 
2. **Developer Tools**> **API Keys**に移動し、**Create API Key**を選択します。

!["API キー" 作成日が"16/12/2025"有効期限が"16/12/36"のページを作成します。]({% image_buster /assets/img/whatsapp/byo_connector/create_api_key.png %})

{: start="3"}
3\.「Braze - My Workspace Name - My WABA Name」など、キーに意味のある名前を付けます。
4. トークンの期限切れの問題を回避するために、遠い将来の有効期限日を追加します。
    \- 新しいAPI キーを生成するメモを作成し、有効期限日までにWABA を再接続します。
5. 以下のスコープを選択します。
- `Message:send`
- `Whatsapp:manage`
- `Whatsapp:message:send`
- `Account-management:manage`
- `Subscriptions:manage`
- `Metrics:manage`
6. キーを作成したら、API キーをコピーします。
    - キーは、作成後、限られた時間のみコピーできます。今後別のWhatsApp 取引先に接続する必要がある場合は、これらのステップs を繰り返して新しい鍵を作成できます。

![Braze Example API Key" 6 つのスコープが追加されました。]({% image_buster /assets/img/whatsapp/byo_connector/api_key.png %})

{: start="7"}
7. アカウントAPI ベースURL をコピーします。

![" API キー s" API 基本URL が強調表示されたページ。]({% image_buster /assets/img/whatsapp/byo_connector/api_base_url.png %})

## ステップ 2:埋め込みサインアップの開始

1. Brazeで、**Partner Integrations**> **Technology Partners**> **WhatsApp**に移動します。
2. **BYO Connector - Infobip**タブを選択します。

![WhatsAppテクノロジーパートナーページ。]({% image_buster /assets/img/whatsapp/byo_connector/byo_tab_tech_parners.png %})

{: start="3"}
3\.[ステップ1](#step-1)からAPI キーと基本URLを入力します。
4. [**接続**] を選択します。
5. 次の考慮事項に従い、[埋め込みサインアップワークフロー]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/#whatsapp-embedded-signup-workflow) を実行します。
- 別のビジネス・ソリューション・プロバイダーが使用する同じビジネス・ポートフォリオを選択することはできません。
- 別のビジネスソリューションプロバイダが使用する電話番号は選択できません。
- 既存のWAB を選択せずに、新しいWABA を作成する必要があります。

{% alert note %}
確認コードを受信するには、Infobip ダッシュボード > **Analyze** > **Logs** に移動し、受信SMS メッセージからコードを取得します。  
{% endalert %}

![確認コードを含む受信SMSメッセージを示すメッセージログ。]({% image_buster /assets/img/whatsapp/byo_connector/verification_code.png %})

設定が完了すると、電話番号がサブスクリプショングループとしてWhatsApp事業グループに表示されます。WhatsApp ビジネスグループには、接続先のInfobip アカウント名とAPI ベースURL が含まれます。ネイティブ統合で接続されたアカウントには、Infobip アカウント名はありません。

{% alert note %}
WhatsApp 取引先を1 つのInfobip アカウントに接続します。追加の電話番号またはサブスクリプショングループを接続するたびに、WhatsAppビジネスアカウントがすでにInfobipアカウントに接続されている場合は、既存のアカウントのAPI 認証情報sを再入力する必要があります。
{% endalert %}

## ステップ 3:メッセージの送信

次のようなネイティブ統合送信プロセスに従います。
- [ユーザー s のサブスクリプショングループへのサブスクライブ]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/)
- [WhatsAppメッセージを作成する]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/)

## セットアップのトラブルシューティング

### WhatsAppの取引先ID を取得できませんでした

WhatsAppの法人取引先が別のBraze ワークスペースに接続されていないことを確認します。

### WhatsAppの法人取引先ID をInfobip と共有できませんでした

1. WhatsApp取引先がBrazeまたは他の取引先に接続されていないことを確認します。
2. WhatsApp取引先の電話番号が別のInfobipアカウントに接続されていないことを確認します。インポートされた番号については、Infobip で番号を検索し、**Cancel number** を選択します。

!["Cancel number"ボタン(Infobip 番号の場合)。]({% image_buster /assets/img/whatsapp/byo_connector/cancel_number.png %})

## 考慮事項 


Braze のすべての機能がサポートされていますが、これらのユースケースは現在サポートされていません。

| ユースケース | 理由 |
| --- | --- |
| Braze およびInfobip での受信メッセージの処理 | これにより、どちらかのシステムでトリガーされているロジックトレーニングが、重複して矛盾する可能性のあるメッセージスレッドを生成するのを防ぎます。 |
| Brazeとインフォビップからのメール送信 | Braze に接続されているWhatsApp 法人取引先の場合、すべての送信はBraze から行われます。 |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation” }

