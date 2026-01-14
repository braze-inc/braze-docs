---
nav_title: ジャスパー
article_title: ジャスパー
description: "Brazeとジャスパーの融合について概説した。"
alias: /partners/jasper/
page_type: partner
search_tag: Partner
---

# ジャスパー 

> [Jasper](https://www.jasper.ai/)は、ブログ、広告、ソーシャルメディアを含む様々なチャネルにまたがって、ブランドが高品質のオンブランドコンテンツを創造し、管理し、規模を拡大できるようにする、AIを駆使したコンテンツプラットフォームです。

_この統合はJasperによって維持されています。_

## 概要

ジャスパーとBrazeインテグレーションにより、コンテンツ作成とキャンペーン実行を合理化できます。ジャスパーでは、マーケティングチームが高品質でオンブランドのコピーを数分で作成できます。Brazeは、これらの情報を最適な時期に適切なオーディエンスに配信することを促進する。この統合により、シームレスなワークフローが促進され、手作業の労力が削減され、より強力なエンゲージメント成果がもたらされます。

この統合を使用する利点は、次のとおりです。

- **高速キャンペーン実行:**数週間ではなく、数分でキャンペーンsを起動します。
- **一貫したブランドの声:**ジャスパーテンプレートsを使用して、生成された複製がブランドガイドラインに厳密に準拠していることを確認します。
- **ターゲットコンテンツ生成:**オーディエンス Segment、スタイルガイド、独自のナレッジアイテムで高度にカスタマイズされたメッセージングを作成します。
- **ダイナミックパーソナライゼーション:**Braze内のスケーラブルなパーソナライゼーションには、{% raw %}```{{${first_name}}}```{% endraw %} のようなリキッドプレースホルダを使用します。
- **エラー低減:**自動化されたワークフローは、コピー/ペーストエラーを最小化し、手動ステップを削減します。

## 前提条件

| 必要条件   | 説明  |
| ------------------- | ---------------- |
| ジャスパーアカウント      | このパートナーシップを活用するにはJasperアカウントが必要です。 |
| Braze REST API キー  | 次の権限を持つBraze REST API キー。<br>  <br>`templates.email.create`<br> `templates.email.update`<br>`content_blocks.create`<br>`content_blocks.update`<br><br>このキーは、**Settings > API Keys** にナビゲートすることで、Braze ダッシュボードで生成できます。  |
| Braze RESTエンドポイント | RESTエンドポイントのURL。具体的なエンドポイントは、インスタンスのBraze URL によって異なります。[Braze API の基本を参照してください。詳細は、エンドポイント]({{site.baseurl}}/api/basics#endpoints) ドキュメントを参照してください。 |
{: .reset-td-br-1 .rest-td-br-2 role=“presentation” }

## 統合方法

ジャスパーでコンテンツを生成し、Braze テンプレートs を更新するには、次の2 つの方法があります。

1. Jasper API を直接使用する
2. Jasper Studio を使用して、Braze対応のカスタムアプリを作成する

{% tabs %}
{% tab Jasper API %}

## メソッド: Jasper API を直接使用する

このメソッドは、Jasper およびBraze での手動設定をバイパスして、Braze でメール HTML テンプレートs をプログラムで作成および更新する場合にアイデアです。

### ステップ 1: ジャスパーのセットアップ

1. [Getting Started](https://developers.jasper.ai/docs/getting-started-1)の手順に従ってJasper API キーを生成します。
2. テンプレート ID が`skl_BC53D8AC5B4B47E8BE557EBB706E9B47` のBraze HTML メール テンプレートs の生成に最適化されたJasper のビルド済みテンプレートを使用します。
3. 以下のフィールドs の値を収集します。これは、Braze HTML メール テンプレートのコンテンツを生成するリクエストを実行するために必要です。

| フィールド | 説明 |
| --- | --- |
| `emailObjective`| メールの目標を明確に定義する。 |
| `ctaLink`| 通話先アクションのURL。 |
| `unsubscribeLink`| マーケティング メール s に必要。 |
| `brandColor`| 16 進数形式のブランドのプライマリカラー(`#4dfa8a` など)。 |
{: .reset-td-br-1 .rest-td-br-2 role=“presentation” }

**任意項目**

| フィールド | 説明 |
| --- | --- |
|`toneId` | ブランドボイス |
| `audienceId`| オーディエンスセグメンテーション |
| `styleId`| スタイルガイド |
| `knowledgeIds` | コンテンツコンテキストの拡張。最大3 つのID を追加できます。 |
{: .reset-td-br-1 .rest-td-br-2 role=“presentation” }

{: start="4"}
4. Jasper API を使用してテンプレートを実行し、出力を生成します。これにより、`subject`、`preheader`、および`body`(HTML内容)を含むJSON 有料読み込むが生成されます。

{% subtabs %}
{% subtab Sample request %}

### サンプルリクエスト

{% raw %}
```json
curl --location 'https://api.jasper.ai/v1/templates/skl_BC53D8AC5B4B47E8BE557EBB706E9B47/run?toneId=ton_811696974b3c4db4b3ac0041685c3b7c&knowledgeIds=kno_0a62fc17529e4fe69a71f30b6f0e88a7&audienceId=aud_0199117a690a7cc98481f8700916e2a6' \
--header 'Content-Type: application/json' \
--header 'x-api-key: ••••••' \
--data '{
  "inputs": {
    "emailObjective": "Announce a webinar and highlight Jasper + Braze integration benefits. Use {{${firstname}}} in the subject and body. Body length ~400 words. Include CTA buttons for registration and footer with unsubscribe link. Apply brand color to buttons and links.",
    "ctaLink": "https://yourbrand.com/register",
    "unsubscribeLink": "{{${unsubscribe_link}}}",
    "brandColor":"#4dfa8a"
  },
  "options": {
    "outputCount": 1,
    "outputLanguage": "English",
    "inputLanguage": "English",
    "languageFormality": "less"
  }
}'
```
{% endraw %}

{% endsubtab %}
{% subtab Sample output %}

### 出力例
```
{
  "subject": "GlowUp Serum is Here! Limited-Time 20% Off!",
  "preheader": "GlowUp Serum is here with a 20% launch discount for 7 days only!",
  "body": "<html> ... </html>"
}
```
{% endsubtab %}
{% endsubtabs %}

### ステップ 2:Brazeの設定

ステップ1 でJasper によって生成された`subject`、`preheader`、および`body` を使用して、[ にBraze REST API へのPOST リクエストを行い、新しいメール テンプレート]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/) を作成します。Braze REST API キーに`templates.email.create` および`templates.email.update` 権限があることを確認します。

### メール テンプレートを作成するためのBraze APIリクエストの例

```json
curl --location --request POST 'https://rest.iad-03.braze.com/templates/email/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <YOUR_BRAZE_API_KEY>' \
--data '{
  "template_name": "email_template_jasperapi_20231104T142300Z",
  "subject": "GlowUp Serum is Here! Limited-Time 20% Off!",
  "preheader": "GlowUp Serum is here with a 20% launch discount for 7 days only!",
  "body": "<html> ... </html>"
}'
```
{% endtab %}
{% tab Jasper Studio %}

## メソッド: Jasper Studio でBraze対応のカスタムアプリを作成する

Jasper Studio は、IT サポートを必要とせずにカスタマイズされたAI アプリを構築できるJasper 内のno-コード プラットフォームです。Braze API 用に特別にフォーマットされたJSON ストラクチャを生成するカスタムアプリをデザインしたり、Braze メッセージに手動で追加できるコンテンツを生成したりできます。

1. Jasperのホーム画面で、**アプリを作成**を選択します。
2. 作成するアプリを指定します。たとえば、**Braze HTMLメールテンプレート**または**コンテンツブロックテンプレート**などです。
3. Jasperが生成する入力プロンプトフィールドを変更します。HTML メール テンプレートの場合、件名行、プリヘッダー、HTML本文、タグs、インラインCSS切り替え、テンプレートの名前の入力フォームを含めることができます。
4. 一貫したパーソナライゼーションとダイナミックな内容のためのリキッドのベストプラクティスに関するガイダンスと知識を統合する。
5. コンテンツ生成のために、Large Language Model (LLM) に提供されている手順を絞り込みます。
6. Braze給与読み込むs 用にフォーマットされた自動化されたJSON 出力を含めることができる、目的の出力のサンプルを提供します。
7. 以下を生成してエクスポートします。
- **ダイレクトコピー/貼り付け:**内容をコピーしてBraze プラットフォームに貼り付けることができます。
- **JSON 出力:**JSON 出力を生成します。この有料読み込むは、`curl` またはミドルウェアを介してBraze エンドポイントを直接呼び出すか、メールオペレーションワークフローに統合するために使用できます。

![Jasper Braze カスタムアプリ。]({% image_buster /assets/img/jasper/jasper_custom_app.png %})

{% subtabs %}
{% subtab Sample JSON output (custom app) %}

## JSON 出力の例(カスタムアプリ)

{% raw %}
```json
{
  "template_name": "email_webinar_2025",
  "subject": "Join Our Webinar, {{${firstname}}}!",
  "preheader": "Unlock the potential of seamless integration.",
  "body": "<html> ... </html>",
  "tags": ["jasperapi"],
  "should_inline_css": true
}
```
{% endraw %}

{% endsubtab %}
{% subtab Sample Braze API request (using custom app output) %}

## Braze API リクエストの例(カスタムアプリアウトプットを使用)

{% raw %}
```json
curl --location --request POST 'https://rest.iad-03.braze.com/templates/email/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <YOUR_BRAZE_API_KEY>' \
--data '{
  "template_name": "email_template_jasperapi_20231104T142300Z",
  "subject": "GlowUp Serum is Here! Limited-Time 20% Off!",
  "preheader": "GlowUp Serum is here with a 20% launch discount for 7 days only!",
  "body": "<html> ... </html>"
}'
```
{% endraw %}

{% endsubtab %}
{% endsubtabs %}

または、マーケターの場合は、カスタムアプリを作成してブランドガイドラインに合わせ、HTMLやコピーアンドペーストなしでコンテンツを生成し、Braze テンプレートsを使用してスタイルを設定することもできます。

{% endtab %}
{% endtabs %}

{% alert note %}
その他のサポートについては、[Jasper API ドキュメント](https://developers.jasper.ai/reference/gettemplate-1)および[Jasper Studio ヘルプセンター](https://help.jasper.ai/hc/en-us/articles/36783295610395-Jasper-Studio)を参照してください。
{% endalert %}
