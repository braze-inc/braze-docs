---
nav_title: Salesforce Sales Cloud
article_title: Salesforce Sales Cloud を使ってリードを管理する
page_order: 3
page_type: reference
description: "Braze の Webhook を使用して、Salesforce sobjects/Lead エンドポイントを通して Salesforce Sales Cloud でリードを作成および更新する方法を学びます。"
---

# Salesforce Sales Cloud を使ってリードを管理する

> [Salesforce](https://www.salesforce.com/) は、リードジェネレーション、オポチュニティ追跡、アカウント管理など、企業が営業プロセス全体を管理できるように設計された、世界有数のクラウドベースのカスタマーリレーションシップマネジメント (CRM) プラットフォームです。<br><br>このページでは、Braze Webhook を使用して、コミュニティから投稿された統合を通じて Salesforce Sales Cloud でリードを作成および更新する方法を紹介します。

{% alert important %}
これはコミュニティから提出された統合であり、Braze は直接サポートしていません。Brazeでは、Braze が提供する公式の Webhook テンプレートのみをサポートします。
{% endalert %}

## 仕組み

Braze と Salesforce Sales Cloud の統合は、 Braze の Webhook を使用して、Salesforce [sobjects/Lead](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_lead.html) エンドポイントを通して Salesforce Sales Cloud でリードを作成および更新します。

Braze は現在、以下のユースケース向けに Salesforce Sales Cloud との2つの統合を提供しています。
1. [Salesforce Sales Cloud でリードを作成する](#creating-lead)
2. [Salesforce Sales Cloud でリードを更新する](#updating-lead)

{% alert note %}
この統合は、純粋にリード獲得と育成の一環として Braze からのデータで Salesforce を更新するためのものです。Salesforce から Braze にデータを同期するには、[B2B データモデル]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_data_models/)を確認するか、[テクノロジパートナー]({{site.baseurl}}/partners/home/)の1つにお問い合わせください。
{% endalert %}

## 前提条件

この統合には、Salesforce のドキュメントにあるステップに従って、Salesforce Sales Cloud で接続されたアプリを作成する必要があります。[OAuth 2.0クライアント認証情報フロー用に接続アプリを設定する](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5)。

接続されたアプリに必要な OAuth 設定を構成するときは、次のものを除き、すべての OAuth 設定をデフォルトの値と選択のままにします。
1. [**デバイスの有効化**] フローを選択します。**Callback URLは**デフォルトでプレースホルダーになるので、空白のままでも構わない。
2. 選択した**OAuth スコープ**に対して、**[API 経由でユーザーデータを管理する (api)]** を追加します。
3. [**クライアント認証情報を有効化**] フローを選択します。

## Salesforce Sales Cloud でリードを作成する{#creating-lead}

カスタマーエンゲージメントプラットフォームとして、Brazeはランディングページのフォーム入力などのユーザーフローに基づいて新しいリードを生成することができる。その場合、Braze Salesforce Sales Cloud の Webhook を使って、Salesforce で対応するリードを作成することができます。

### ステップ1:`client_id` および `client_secret` を収集する

1. Salesforce で、[**プラットフォームツール**] > [**アプリ**] > [**アプリマネージャー**] と進みます。
2. 新しく作成した Braze アプリを見つけ、[**表示**] を選択します。
3. **消費者キーと秘密（Consumer Key and Secret）**]で、[**消費者詳細の管理（Manage Consumer Details）**]を選択する。
4. 表示されたページで、**消費者キー**と**消費者シークレット**をメモします。**消費者キーは**あなたの`client_id` であり、**消費者シークレットは**あなたの`client_secret` である。

### ステップ2:Webhook テンプレートのセットアップ

テンプレートを使って、Brazeプラットフォーム全体でこのWebhookをすばやく再利用できる。 

1. Brazeの「**Templates**」から「**Webhook Templates**」を選択し、**「+ Create Webhook Template**」を選択する。
2. テンプレートの名前を指定します ("Salesforce Sales Cloud > Create Lead"など)。
3. **Compose**タブで、以下の詳細を入力する：

#### Webhook作成 

| フィールド | 詳細 |
| --- | --- |
| Webhook URL | {% raw %}`https://[insert_instance_name].my.salesforce.com/services/data/v60.0/sobjects/Lead/`{% endraw %} |
| HTTP メソッド | `POST` |
| リクエスト本文 | JSON キーと値のペア |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

#### 本文プロパティのキー値

Braze から Salesforce にマップするキーと値のペアごとに、[**+新しい本文プロパティの追加**] を選択します。どんなフィールドでもマッピングできるので、以下の表はほんの一例に過ぎない。

| キー | 値 |
| --- | --- |
| ファーストネーム | {% raw %}`{{${first_name}}}`{% endraw %} |
| ラストネーム | {% raw %}`{{${last_name}}}`{% endraw %} |
| email | {% raw %}`{{${email_address}}}`{% endraw %} |
| 会社 | {% raw %}`{{custom_attribute.${company}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

#### リクエストヘッダー

次の各リクエストヘッダーに対して [**+新しいヘッダーの追加**] を選択します。

| キー | 値 |
| --- | --- |
| 許可 | {% raw %}`{% connected_content https://[insert_instance_name].my.salesforce.com/services/oauth2/token     :method post     :body client_id=[insert_client_id]&client_secret=[insert_client_secret]&grant_type=client_credentials     :save result %}Bearer {{result.access_token}}`{% endraw %} |
| コンテンツタイプ | `application/json` |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

{: start="4" }
4\.[**テンプレートの保存**] を選択します。

![リードを作成するための記入済みWebhook テンプレート。]({% image_buster /assets/img/b2b/create_lead_webhook.png %}){: style="max-width:70%;"}
 
## Salesforce Sales Cloud でリードを更新する{#updating-lead}

Salesforce でリードを更新する Braze Salesforce Sales Cloud webhook を設定するには、Salesforce Sales Cloud と Braze の間に共通の識別子が必要です。以下の例では、Salesforce `lead_id` を Braze `external_id` として使用していますが、`user_alias` を使用することでもこれを実現できます。これの詳細については、[B2B データ]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_data_models)を参照してください。

この例では、リードが一定のリードしきい値を超えた後、リードのリードステージを「MQL」 (マーケティング適格リード) に更新する方法を具体的に示しています。これは、私たちの[B2B リードスコアリングワークフロー]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/lead_scoring/)のユースケースの核となる部分です。

### ステップ1:`client_id` および `client_secret` を収集する

1. Salesforce で、[**プラットフォームツール**] > [**アプリ**] > [**アプリマネージャー**] と進みます。
2. 新しく作成した Braze アプリを見つけ、[**表示**] を選択します。
3. **消費者キーと秘密（Consumer Key and Secret）**]で、[**消費者詳細の管理（Manage Consumer Details）**]を選択する。
4. 表示されたページで、**消費者キー**と**消費者シークレット**をメモします。
    - **消費者キーは**あなたの`client_id` であり、**消費者シークレットは**あなたの`client_secret` である。

### ステップ2:Webhook テンプレートのセットアップ

1. Brazeの「**Templates**」から「**Webhook Templates**」を選択し、**「+ Create Webhook Template**」を選択する。
2. テンプレートの名前を指定します ("Salesforce Sales Cloud > Update Lead to MQL"など)。
3. **Compose**タブで、以下の詳細を入力する：

#### Webhook作成 

| フィールド | 詳細 |
| --- | --- |
|Webhook URL | {% raw %}`https://[insert_instance_name].my.salesforce.com/services/data/v60.0/sobjects/Lead/{{${user_id}}}`{% endraw %} |
| HTTP メソッド | `PATCH` |
| リクエスト本文 | JSON キーと値のペア |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

#### 本文プロパティのキー値

次のキーと値のペアに対して、「**＋新しいボディ・プロパティを追加**」を選択する。なお、`Lead_Stage__c` は名前の例です。SalesforceでMQLを追跡するために使用するカスタムフィールドの名前が異なる場合があるので、両者が一致していることを確認すること。

| キー | 値 |
| --- | --- |
| `Lead_Stage__c` | `MQL` |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

#### リクエストヘッダー

次の各リクエストヘッダーに対して [**+新しいヘッダーの追加**] を選択します。

| キー | 値 |
| --- | --- |
| 許可 | {% raw %}`{% connected_content https://[insert_instance_name].my.salesforce.com/services/oauth2/token     :method post     :body client_id=[insert_client_id]&client_secret=[insert_client_secret]&grant_type=client_credentials     :save result %}Bearer {{result.access_token}}`{% endraw %} |
| コンテンツタイプ | `application/json` |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

{: start="4"}
4\.[**テンプレートの保存**] を選択します。

![リードを更新するための記入済みWebhook テンプレート。]({% image_buster /assets/img/b2b/update_lead_webhook.png %}){: style="max-width:70%;"}

## 運用ワークフローでこれらのWebhookを使用する

次のように、テンプレートを Braze の運用ワークフローにすばやく追加できます。

1. Salesforce でリードを作成する[新規ユーザーキャンペーン](#new-lead)の一部
2. MQL のしきい値を超えたユーザーを「MQL」に更新し、同じ情報で Salesforce Sales Cloud を更新する[リードスコアリングキャンバス](#lead-scoring)の一部

### 新規リードキャンペーン {#new-lead}

ユーザがメールアドレスを提供したときに Salesforce でリードを作成するには、「リードの更新」Webhook テンプレートを使用するキャンペーンを作成し、ユーザがメールアドレスを追加したとき（たとえば、Web フォームに入力したとき）にトリガーする。

![アクションベースで、「メールアドレスを追加」というトリガー アクションのキャンペーンを作成する手順2。]({% image_buster /assets/img/b2b/salesforce_create_campaign.png %}){: style="max-width:70%;"}

### マーケティング適格リード（MQL）の閾値を超えるためのリードスコアリングキャンバス {#lead-scoring}

このWebhookは[リードスコアリングの]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/lead_scoring/#lead-handoff)ユースケースで取り上げているが、リードスコアリングキャンバス内でMQLをチェックし、Salesforceを直接更新することもできる（Webhookキャンペーンを別途作成するのとは対照的）： 

ユーザー更新に後続ステップを追加し、ユーザーが定義したMQLしきい値を超えたかどうかをチェックする。もしユーザーがしきい値を超えた場合、そのユーザーのステータスを「MQL」に更新し、その後、この Webhook テンプレートを使用して同じ「MQL」ステータスで Salesforce を更新します。Salesforce は、定義されたリードルーティングルールを使用して、このリードを適切な営業チームにルーティングすることで、残りの処理を行います。  

#### MQLしきい値を通過したユーザーをチェックするキャンバスステップを追加する 

1. 2つのグループを持つ**オーディエンスパスの**ステップを追加する：「MQL しきい値」と「その他のユーザー」。
2. 「MQL しきい値」グループで、現在ステータスが「MQL」ではないが (例えば、`lead_stage` が「リード」に等しい)、定義したしきい値を超えるリードスコア (例えば、`lead_score` が 50以上) を持っているユーザーを探します。存在する場合は次のステップに進み、存在しない場合は終了します。

!["MQL Threshold" オーディエンスパスグループ。`lead_stage` が"Lead" と等しく、`lead_score` が"50" 以上の場合はフィルター s です。]({% image_buster /assets/img/b2b/salesforce_check_mql.png %}){: style="max-width:70%;"}

{: start="3" }
3\.ユーザーの`lead_stage` 属性値を "MQL "に更新する**ユーザー更新**ステップを追加する。

![`lead_stage`属性を更新する"MQLへの更新"ユーザ更新 ステップは"MQL"の値を持ちます。]({% image_buster /assets/img/b2b/salesforce_update_mql.png %}){: style="max-width:70%;"}

{: start="4" }
4\.新しいMQLステージでSalesforceを更新するWebhookステップを追加する。

![「Salesforce のアップデート」Webhook ステップに詳細が入力されます。]({% image_buster /assets/img/b2b/salesforce_webhook.png %}){: style="max-width:70%;"}

これでキャンバスフローは、MQLのしきい値を超えたユーザーを更新する！

![ユーザーがMQL しきい値を超えているかどうかを確認し、ユーザーが合格した場合はSalesforce を更新するキャンバスユーザー 更新 ステップ。]({% image_buster /assets/img/b2b/salesforce_canvas.png %}){: style="max-width:50%;"}

## トラブルシューティング

これらのワークフローは、Salesforce 内でのデバッグ機能が限られているため、Webhook に障害が発生した理由やエラーが発生したかどうかを調べるには、Braze [メッセージアクティビティログ]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab#message-activity-log)を参照することをおすすめします。

例えば、oAuthトークンの取得に使用された無効なURLによるエラーは、`https://[insert_instance_name].my.salesforce.com/services/oauth2/token is not a valid URL` と表示される。

![URL が有効なURL ではないことを示すエラー レスポンスボディ。]({% image_buster /assets/img/b2b/error_message_invalid_url.png %})

