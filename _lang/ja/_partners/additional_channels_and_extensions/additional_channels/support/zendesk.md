---
nav_title: Zendesk
article_title: Zendesk
description: "このリファレンス記事では、Braze と Zendesk のパートナーシップについて説明します。Zendesk は人気の高いサポートスイートであり、この2つのプラットフォーム間でサポートデータを同期できる Braze Webhook を利用できます。"
alias: /partners/zendesk/
page_type: partner
search_tag: Partner

---

# Zendesk

> [Zendesk Support Suite](https://www.zendesk.com/support-suite/)（ZSS）は、Eメール、ウェブチャット、音声、ソーシャルメッセージングアプリを使ったオムニチャネルサポートを通じて、顧客との自然な会話を可能にする。Zendesk は対応の追跡と優先順位付けを重視する効率的なチケット発行システムを提供し、企業が顧客の履歴を一元的に把握できるようにしています。

Braze とZendesk のサーバー間統合により、以下を利用できます。 
- BrazeのWebhookを使用して、BrazeのユーザージャーニーでのメッセージエンゲージメントによるZendeskでのサポートチケット作成を自動化する。例えば、統合の実装とテストに成功した後、Brazeは、アプリ内のメッセージ "Enjoying our App?" に否定的な回答をしたユーザーからサポートチケットを作成し、サポートチームが顧客をフォローアップできるようにする。
- Zendesk でのアクティビティによる Braze でのユーザープロファイルの更新など、双方向ユースケースをサポートするための Zendesk Webhook。例えば、チケットが解決した後、Brazeのユーザープロファイルにイベントを記録する。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Zendeskアカウント | このパートナーシップを活用するには、[Zendesk 管理者アカウント](https://`<your-zendesk-instance>`.zendesk.com/agent/admin)が必要です。 |
| Zendesk APIトークン | Braze から Zendesk チケットエンドポイントにリクエストを送信するには、Zendesk API トークン ](https://support.zendesk.com/hc/en-us/articles/226022787-Generating-a-new-API-token-) が必要です。 |
| 共通識別子（推奨） | BrazeとZendesk間で[共通の識別子を](#common-identifier)使用することを推奨する。 |
| BrazeのAPIキー | ZendeskからBrazeエンドポイントにリクエストを送信するには、Braze APIキーが必要である。使用するAPIキーが、Zendesk webhookが使用するBrazeエンドポイントに対して正しい権限を持っていることを確認する。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## BrazeとZendeskの統合

### ステップ1:BrazeのWebhookを作成する

ウェブフックを作成する：

- **キャンペーン:**Brazeダッシュボードの**Campaigns**ページに行く。[**キャンペーンを作成**] をクリックし、[**Webhook**] を選択します。
- **キャンバス:**新しいキャンバスまたは既存のキャンバスから、キャンバスビルダーでフルステップまたはメッセージステップを作成します。次に、[**メッセージ**] をクリックし、メッセージオプションから [**Webhook**] を選択します。

Webhookに以下のフィールドを記入する：
- **Webhook URL**: `<your-zendesk-instance>.zendesk.com/api/v2/tickets.json`
- **リクエスト本文**:Raw Text

その他のユースケースは、[Zendesk support API](https://developer.zendesk.com/rest_api/docs/support/introduction) を使用して対処できます。これにより、Webhook URL の末尾の `/api/v2/` エンドポイントが変更されます。

#### リクエストヘッダーとメソッド

Zendeskは認証のためのHTTPヘッダーとHTTPメソッドを要求する。**設定]**タブで、<email_address> を Zendesk 管理者のメールアドレスに、<api_token> を Zendesk API トークンに置き換える。

- **HTTPメソッド**：POST
- **リクエストヘッダー**:
  - **Authorization**:ベーシック {% raw %} `{{ '<email_address>/token:<api_token>' | base64_encode }}` {% endraw %}
  - **Content-Type**: application/json

![]({% image_buster /assets/img_archive/zendesk_step1.gif %}){: style="max-width:70%;"}

#### Request body

Webhookペイロードで、タイプ、サブジェクト、ステータスなどのチケットの詳細を定義する。チケットの詳細は拡張可能であり、[Zendesk ticket API](https://developer.zendesk.com/rest_api/docs/support/tickets#create-ticket) に基づいてカスタマイズされます。以下の例を参考に、ペイロードを構成し、希望するフィールドを入力する。

{% raw %}
```json
{% assign ticket_type = 'question/incident/task/problem' %} << Choose one >>
{% assign ticket_subject = '' %}
{% capture ticket_body %}
<< Your message here >>
{% endcapture %}
{% assign ticket_subject_tag = '' %}
{% assign ticket_status = 'New' %}

{
"ticket": {
"requester_id": "{{${user_id}}}", 
"requester": { "name": "{{${first_name}}} {{${last_name}}}", "email": "{{${email_address}}}", "phone": "{{${phone_number}}}"},
"type": "{{ ticket_type }}",
"subject":  "{{ticket_subject}}",
"comment":  { "body": "{{ticket_body}}" },
"priority": "urgent",
"status": "{{ ticket_status }}"
  }
}
```
{% endraw %}

### ステップ2:リクエストをプレビューする

テキストがBrazeタグであれば、自動的にハイライトされる。

**Preview**パネルでリクエストをプレビューするか、**Test**タブに移動して、ランダムなユーザーか既存のユーザーを選択するか、Webhookをテストするために自分でカスタマイズする。

最後に、Zendesk側でチケットが作成されているかどうかを確認する。

## 共通識別子

Braze と Zendesk の間に共通の識別子がある場合は、それを `requester_id` として使用することをお勧めします。これにより、2つのユーザーセットを統一できます。それ以外の場合は、名前、メールアドレス、電話番号などの一連の識別属性を渡すことをお勧めします。

## ZendeskとBrazeの統合

### ステップ1:ウェブフックを作成する

1. [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb) で、サイドバーにある [**Apps and integrations**] クリックし、**[Webhooks] > [Webhooks]** を選択します。<br><br>
2. [**Create webhook**] をクリックします。<br><br>
3. [**Trigger**] または [**Automation**] を選択し、[**Next**] をクリックします。<br>![]({% image_buster /assets/img_archive/zendesk2.png %}){: style="max-width:70%;"}<br><br>
4. Webhook に以下の情報を指定します。
- ウェブフックの名前と説明を入力する。
- Webhookが使用するBrazeエンドポイントURLを入力する。{% raw %}この例では`https://{{instance_url}}/users/track` を使用する。{% endraw %}
- ウェブフックのリクエスト・メソッドとしてPOSTを選択し、リクエスト・フォーマットをJSONに設定する。
- Webhook にベアラートークン認証方式を選択し、[Braze API キー]({{site.baseurl}}/api/basics/#creating-and-managing-rest-api-keys)を入力します。
  - 使用する API キーに、Webhook が使用する Braze エンドポイントに対して[正しい権限]({{site.baseurl}}/api/basics/#rest-api-key-permissions)があることを確認します。<br><br>
5. (推奨）Webhookをテストし、正しく動作していることを確認する。<br><br>
6. トリガーとオートメーションのウェブフックについては、セットアップを終了する前に、ウェブフックをトリガーまたはオートメーションに接続する必要がある。Webhookのトリガーを作成する例については、次のステップを参照のこと。トリガーが作成されたら、このページに戻り、[**設定完了**] を選択します。

### ステップ2: トリガーまたはオートメーションを作成する

[Zendesk の指示に従って](https://support.zendesk.com/hc/en-us/articles/4408839108378#topic_bwm_1tv_dpb)、Webhook をトリガーまたはオートメーションに接続する。

以下の例では、サポートケースのステータスが "Solved"（解決済み）または "Closed"（クローズ済み）に変更されたときに、Webhookを呼び出すトリガーを使用している。 

1. **Admin Center** で、サイドバーにある [**Objects and rules**] をクリックし、**[Business rules] > [Triggers]** を選択します。<br><br>
2. ［**トリガーを追加**] を選択します。<br><br>
3. トリガーに名前を付け、カテゴリーを選択する。<br><br>
4. [**条件の追加**] を選択して、Webhook をトリガーする条件を設定します。たとえば、「Status category changed to closed」や「Status category changed to solved」などです。![]({% image_buster /assets/img_archive/zendesk1.png %}){: style="max-width:70%;"}<br><br>
5. [**アクションの追加**] を選択し、[**アクティブな webhook に通知**] を選択し、前のステップで作成した Webhook をドロップダウンから選択します。<br><br>
6. Brazeのエンドポイントに適合するようにJSON本体を定義し、Zendeskの変数プレースホルダを使用して、関連するフィールドに動的に入力する。<br>![]({% image_buster /assets/img_archive/zendesk3.png %}){: style="max-width:70%;"}<br><br>
7. [**作成**] を選択します。<br><br>
8. Webhook に戻り、[**Finish setup**] をクリックします。


