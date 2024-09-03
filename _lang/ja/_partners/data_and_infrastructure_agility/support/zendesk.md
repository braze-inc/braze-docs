---
nav_title: Zendesk
article_title: Zendesk
description: "この参考記事では、Brazeと人気のサポートスイートであるZendeskのパートナーシップについて概説しており、2つのプラットフォーム間でサポートデータを同期できるBrazeのウェブフックを利用できる。"
alias: /partners/zendesk/
page_type: partner
search_tag: Partner

---

# Zendesk

> [Zendesk Support Suite](https://www.zendesk.com/support-suite/)（ZSS）は、Eメール、ウェブチャット、音声、ソーシャルメッセージングアプリを使ったオムニチャネルサポートを通じて、顧客との自然な会話を可能にする。Zendeskは、相互作用の追跡と優先順位付けを重視する合理化された発券システムを提供し、企業は顧客に関する統一された履歴ビューを持つことができる。

BrazeとZendeskのサーバー間統合を利用することができる： 
- BrazeのWebhookを使用して、BrazeのユーザージャーニーでのメッセージエンゲージメントによるZendeskでのサポートチケット作成を自動化する。例えば、統合の実装とテストに成功した後、Brazeは、アプリ内のメッセージ "Enjoying our App?" に否定的な回答をしたユーザーからサポートチケットを作成し、サポートチームが顧客をフォローアップできるようにする。
- ZendeskのWebhookにより、ZendeskのアクティビティによってBrazeのユーザープロファイルを更新するような双方向のユースケースをサポートする。例えば、チケットが解決した後、Brazeのユーザープロファイルにイベントを記録する。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Zendeskアカウント | このパートナーシップを利用するには、[Zendeskの管理者アカウントが](https://`<your-zendesk-instance>`.zendesk.com/agent/admin)必要である。 |
| Zendesk APIトークン | BrazeからZendeskチケットエンドポイントにリクエストを送信するには、Zendesk[APIトーク][2]ンが必要である。 |
| 共通識別子（推奨） | BrazeとZendesk間で[共通の識別子を](#common-identifier)使用することを推奨する。 |
| BrazeのAPIキー | ZendeskからBrazeエンドポイントにリクエストを送信するには、Braze APIキーが必要である。使用するAPIキーが、Zendesk webhookが使用するBrazeエンドポイントに対して正しい権限を持っていることを確認する。 |
{: .reset-td-br-1 .reset-td-br-2}

## BrazeとZendeskの統合

### ステップ1:BrazeのWebhookを作成する

ウェブフックを作成する：

- **キャンペーン**Brazeダッシュボードの**Campaigns**ページに行く。**Create Campaignを**クリックし、**Webhookを**選択する。
- **キャンバス:**新規または既存のキャンバスから、キャンバスビルダーでフルステップまたはメッセージステップを作成する。次に、**Messagesを**クリックし、メッセージ・オプションから**Webhookを**選択する。

Webhookに以下のフィールドを入力する：
- **ウェブフックのURL**： `<your-zendesk-instance>.zendesk.com/api/v2/tickets.json`
- **リクエスト・ボディ**Raw Text

その他のユースケースは、\[Zendesk support APIs][4], Webhook URL の末尾の`/api/v2/` エンドポイントを適宜変更する。

#### リクエスト・ヘッダとメソッド

Zendesk は HTTP ヘッダによる認証と HTTP メソッドを要求する。**設定]**タブで、<email_address> を Zendesk 管理者のメールアドレスに、<api_token> を Zendesk API トークンに置き換える。

- **HTTPメソッド**：POST
- **ヘッダーを要求する**：
  - **認可する**：ベーシック {% raw %} `{{ '<email_address>/token:<api_token>' | base64_encode }}` {% endraw %}
  - **Content-Type**: application/json

![][3]{: style="max-width:70%;"}

#### Request body

Webhookペイロードで、タイプ、サブジェクト、ステータスなどのチケットの詳細を定義する。チケットの詳細は、\[Zendesk ticket API][6].以下の例を参考に、ペイロードを構成し、希望するフィールドを入力する。

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

入力したテキストがBrazeタグに該当する場合、自動的にハイライト表示される。

**Preview**パネルでリクエストをプレビューするか、**Test**タブに移動して、ランダムなユーザーか既存のユーザーを選択するか、Webhookをテストするために自分でカスタマイズする。

最後に、Zendesk側でチケットが作成されているかどうかを確認する。

## 共通識別子

BrazeとZendeskで共通の識別子がある場合は、これを`requester_id` 。これは、2組のユーザーを統一するのに役立つだろう。また、そうでない場合は、名前、Eメールアドレス、電話番号などの識別属性を渡すことを推奨する。

## ZendeskとBrazeの統合

### ステップ1:ウェブフックを作成する

1. [Admin Centerで](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb)、サイドバーの**Apps and integrationsを**クリックし、**Webhooks > Webhooksを**選択する。<br><br>
2. **Create webhookを**クリックする。<br><br>
3. **Trigger**または**Automationを**選択し、**Nextを**クリックする。<br>![][9]{: style="max-width:70%;"}<br><br>
4. ウェブフックに以下の情報を記入する：
- ウェブフックの名前と説明を入力する。
- Webhookが使用するBrazeエンドポイントURLを入力する。{% raw %}この例では`https://{{instance_url}}/users/track` を使用する。{% endraw %}
- ウェブフックのリクエスト・メソッドとしてPOSTを選択し、リクエスト・フォーマットをJSONに設定する。
- Webhookのベアラートークン認証方法を選択し、[Braze APIキーを](https://www.braze.com/docs/api/basics/#creating-and-managing-rest-api-keys)入力する。
  - 使用するAPIキーが、Webhookが使用するBrazeエンドポイントに対して[正しい権限を持って](https://www.braze.com/docs/api/basics/#rest-api-key-permissions)いることを確認する。<br><br>
5. (推奨）ウェブフックが正しく動作しているかテストする。<br><br>
6. トリガーとオートメーションのウェブフックについては、セットアップを終了する前に、ウェブフックをトリガーまたはオートメーションに接続する必要がある。Webhookのトリガーを作成する例については、次のステップを参照のこと。トリガーが作成されたら、このページに戻り、**Finish setupを**クリックする。

### ステップ2:トリガーまたはオートメーションを作成する

[Zendesk の指示に従って](https://support.zendesk.com/hc/en-us/articles/4408839108378#topic_bwm_1tv_dpb)、Webhook をトリガーまたはオートメーションに接続する。

以下の例では、サポートケースのステータスが "Solved"（解決済み）または "Closed"（クローズ済み）に変更されたときに、Webhookを呼び出すトリガーを使用している。 

1. **Admin Centerで**、サイドバーの**Objects and rulesを**クリックし、**Business rules > Triggersを**選択する。<br><br>
2. **Add triggerを**クリックする。<br><br>
3. トリガーに名前を付け、カテゴリーを選択する。<br><br>
4. **Add conditionを**クリックして、ウェブフックをトリガーする条件を設定する。例えば、「ステータスのカテゴリーがクローズに変更されました」や「ステータスのカテゴリーが解決済みに変更されました」などである。![][8]{: style="max-width:70%;"}<br><br>
5. **Add actionを**クリックし、**Notify active webhookを**選択し、前のステップで作成したwebhookをドロップダウンから選択する。<br><br>
6. Brazeのエンドポイントに適合するようにJSON本体を定義し、Zendeskの変数プレースホルダを使用して、関連するフィールドに動的に入力する。<br>![][10]{: style="max-width:70%;"}<br><br>
7. \[**作成**] をクリックします。<br><br>
8. Webhookに戻り、**Finish setupを**クリックする。

[1]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
[2]: https://support.zendesk.com/hc/en-us/articles/226022787-Generating-a-new-API-token-\
[3]: {% image_buster /assets/img_archive/zendesk_step1.gif %}
[4]: https://developer.zendesk.com/rest_api/docs/support/introduction
[5]: {% image_buster /assets/img_archive/zendesk_step2.png %}
[6]: https://developer.zendesk.com/rest_api/docs/support/tickets#create-ticket
[7]: {% image_buster /assets/img_archive/zdfinal.gif %}

[8]: {% image_buster /assets/img_archive/zendesk1.png %}
[9]: {% image_buster /assets/img_archive/zendesk2.png %}
[10]: {% image_buster /assets/img_archive/zendesk3.png %}
