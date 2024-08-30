---
nav_title: ナック
article_title: ナック
alias: /partners/knak/
description: "この参考記事では、Brazeとキャンペーン作成プラットフォームであるKnakのパートナーシップについて概説している。Knakは、数日または数週間ではなく、数分または数時間で完全なレスポンシブメールを作成し、すぐに使えるBrazeテンプレートとしてエクスポートすることを可能にする。"
page_type: partner
search_tag: Knak

---

# ナック

> [Knakは][1]、企業のマーケティングチームが社内で使用するために構築された初のキャンペーン作成プラットフォームである。ドラッグ・アンド・ドロップのプラットフォームは、コーディングや外部の手を借りることなく、誰でも数分で美しく、ブランドのあるEメールやランディングページを作成することができる。

BrazeとKnakの統合により、何日も何週間もかかることなく、数分から数時間で完全なレスポンシブメールを作成し、すぐに使えるBrazeテンプレートとしてエクスポートできる。Knakは、Brazeで管理するキャンペーンのメール作成をレベルアップしたいマーケティング担当者のために作られたもので、外部エージェンシーやハンドコーディングを必要としない。 

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| クナックアカウント | このパートナーシップを利用するには、Knakアカウントが必要だ。 |
| Braze REST API キー | 完全な**テンプレート**権限を持つBraze REST APIキー。<br><br>これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント | [RESTエンドポイントのURL][2]。エンドポイントは、インスタンスのBraze URLに依存する。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

Knakは、メール作成のレベルアップを望むマーケティング担当者のために開発された。こんな人には最適だ：
- 現在、Eメールにシンプルなテンプレートを使用しているが、さらにレベルアップしたい
- Braze用のEメールを外部の代理店や開発者に依存する
- アセット制作のクリエイティブ・コントロールを取り戻し、市場投入までの時間を大幅に短縮したい。

## 統合

### ステップ1:統合を設定する

Knakで、**Integrations > Platforms > + Add New Integrationに**移動する。

![統合ボタンを追加する][5]

次に、**Braze**プラットフォームを選択し、Braze APIキーとRESTエンドポイントを提供する。**Create New Integrationを**クリックして統合を完了する。 

![新しい統合を作成する][6]

### ステップ2:Knakテンプレートを同期する

Knakで、Brazeに同期したいEメールを探し、**Publish**、**Syncの**順に選択する。

![クナック統合 1][8]

次に、Eメール名を確認し、**同期を**クリックする。

![クナック統合2][9]

## 統合を利用する

アップロードしたKnakのメールは、Brazeの**Engagement > Templates & Mediaで**確認できる。美しく、ブランドらしく、完全なレスポンシブである。唯一の限界は、あなた自身の創造力だ！

[1]: https://knak.com/
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[5]: {% image_buster /assets/img/knak/integration-setup-step-2-add-new-integration.png %}
[6]: {% image_buster /assets/img/knak/integration-setup-step-4-add-api-key.png %}
[8]: {% image_buster /assets/img/knak/integration-post-step-1-sync.png %}
[9]: {% image_buster /assets/img/knak/integration-post-step-2-asset-name.png %}