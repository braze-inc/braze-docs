---
nav_title: MyPostcard
article_title: MyPostcard
page_order: 1
description: "この参考記事では、CRMワークフローの追加チャネルとしてダイレクトメールを使用できるようにする、BrazeとMyPostcardのパートナーシップについて概説している。"
alias: /partners/mypostcard/
page_type: partner
search_tag: Partner

---

# MyPostcard

> [MyPostcard](https://www.mypostcard.com) は世界有数のポストカードアプリで、ダイレクトメールのキャンペーンを簡単に実行でき、シームレスで収益性の高い方法で顧客とつながることができます。 

MyPostcard と Braze の統合を使用すると、印刷物を簡単に顧客に送信できます。

## 前提条件

| 必要条件                      | 説明                                                                                                             |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| MyPostcard B2B アカウント           | この統合を利用するには、MyPostcardへの登録が必要である。                                          |
| B2B API キーと認証情報        | API キーと認証情報は、MyPostcard B2B 管理ツールで確認できる。                                         |
| 承認された MyPostcard B2B キャンペーン | この統合を利用するには、MyPostcard B2Bツールで印刷郵送キャンペーンを設定する必要がある。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース

ダイレクトメールキャンペーンを向上させるには、従来の大量郵送を超える方法を採用し、印刷物をワークフローにシームレスに統合することが重要です。このアプローチによって、メールマガジンをオプトアウトしている顧客や、メールがスパムとしてマークされている特定の顧客にアプローチすることができます。MyPostcardを使えば、Brazeから直接、印刷物の郵送キャンペーンを簡単に送ることができる。

- 専門知識がなくても、Brazeで直感的なワークフローを構築し、印刷メールを強力な新しいチャネルとして組み込む。
- いくつかの簡単なステップで、パーソナライズされた印刷物の可能性を引き出します。
- 専任チームによるパーソナライズされたサポートに裏打ちされた、わかりやすい導入のメリットを享受できる。

## 統合

MyPostcard と統合するには、[ログインするかサインアップ](https://www.mypostcard.com/b2b/admin/)して、[Braze Webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks) を使って MyPostcard を使用する最初のキャンペーンを作成します。

### ステップ1: BrazeのWebhookテンプレートを作成する

Brazeプラットフォームの**Templates**>**Webhook Templatesから**、今後のキャンペーンやCanvasで使用するMyPostcard Webhookテンプレートを作成する。

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/)使用している場合は、**エンゲージメント**>**テンプレート& メディア**>**Webhook テンプレートに**移動する。
{% endalert %}

単発のMyPostcard Webhookキャンペーンを作成したい場合、または既存のテンプレートを使用したい場合は、新規キャンペーン作成時にBrazeで**Webhookを**選択する。以下のフィールドに入力します。

| フィールド         | 説明                                               |
|---------------|-----------------------------------------------------------|
| **Webhook URL** | B2B 管理ツールに表示される Webhook URL。             |
| **リクエスト本文** | 生テキスト（B2B管理ツールにあるJSON形式）。        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### リクエストメソッドとヘッダー

MyPostcardでは、HTTPメソッドと以下のHTTPヘッダーをテンプレートに含める必要がある。

{% raw %}
<table>
  <thead>
    <tr>
      <th><strong>フィールド</strong></th>
      <th><strong>詳細</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>HTTPメソッド</strong></td>
      <td><code>POST</code></td>
    </tr>
    <tr>
      <td><strong>ユーザー名</strong></td>
      <td><code>{{ '&lt;username&gt;' }}</code></td>
    </tr>
    <tr>
      <td><strong>パスワード</strong></td>
      <td><code>{{ '&lt;password&gt;' }}</code></td>
    </tr>
    <tr>
      <td><strong>コンテンツタイプ</strong></td>
      <td><code>application/json</code></td>
    </tr>
  </tbody>
</table>
{% endraw %}
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Request body

B2B 管理ツールに表示されているリクエスト本文をコピーし、Liquid パーソナライゼーションタグを使用してプレースホルダにコンテンツを入力します。

![JSON 本文と Webhook 情報を示す [作成] タブ。]({% image_buster /assets/img/mypostcard/mypostcard_compose.jpg %})

### ステップ2: リクエストをプレビューする

次に、**Preview**パネルでリクエストをプレビューするか、**Test**タブに行き、そこでランダムユーザー、既存ユーザーを選択するか、カスタムユーザーを作成してWebhookをテストする。ページを離れる前にテンプレートを保存することをお忘れなく！

![Webhook Tabを異なるフィールドでテストし、実装を検証する。]({% image_buster /assets/img/mypostcard/mypostcard_test.jpg %})

{% alert important %}
ページを離れる前にテンプレートを保存することを忘れないこと！<br>更新されたWebhookテンプレートは、新しい[Webhookキャンペーンを]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)作成するときに、**保存されたWebhookテンプレート**リストで見つけることができる。
{% endalert %}

