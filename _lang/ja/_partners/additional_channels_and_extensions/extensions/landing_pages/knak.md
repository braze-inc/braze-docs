---
nav_title: Knak
article_title: Knak
alias: /partners/knak/
description: "この参考記事では、Brazeとキャンペーン作成プラットフォームであるKnakのパートナーシップについて概説している。Knakは、数日または数週間ではなく、数分または数時間で完全なレスポンシブメールを作成し、すぐに使えるBrazeテンプレートとしてエクスポートすることを可能にする。"
page_type: partner
search_tag: Knak

---

# Knak

> [Knak](https://knak.com/) は、企業のマーケティングチームが社内で使用するために構築された、初のキャンペーン作成プラットフォームです。ドラッグ・アンド・ドロップのプラットフォームは、コーディングや外部の手を借りることなく、誰でも数分で美しく、ブランドのあるEメールやランディングページを作成することができる。

_この統合は Knak によって管理されます。_

## 統合について

BrazeとKnakの統合により、何日も何週間もかかることなく、数分から数時間で完全なレスポンシブメールを作成し、すぐに使えるBrazeテンプレートとしてエクスポートできる。Knakは、Brazeで管理するキャンペーンのメール作成をレベルアップしたいマーケティング担当者のために作られたもので、外部エージェンシーやハンドコーディングを必要としない。 

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Knak アカウント | このパートナーシップを活用するには、Knak アカウントが必要です。 |
| Braze REST API キー | 完全な**テンプレート**権限を持つBraze REST API キー。<br><br>これはBrazeのダッシュボードで**設定** > **APIキー**から作成できます。 |
| Braze REST エンドポイント | [あなたのRESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。お客様のエンドポイントは、お客様のインスタンスのBraze URLに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース

Knak は、コーディングや外部からの支援を必要とせずに、メール作成をレベルアップしたいマーケターを対象に構築されました。こんな人には最適だ：
- 現在、Eメールにシンプルなテンプレートを使用しているが、さらにレベルアップしたい
- Braze のメールの作成を外部の組織や開発者に頼っている。
- アセット制作のクリエイティブ・コントロールを取り戻し、市場投入までの時間を大幅に短縮したい。

## 統合

### ステップ1:統合を設定する

Knak で **[Integrations] > [Platforms] > [+ Add New Integration]** に移動します。

![統合追加のボタン]({% image_buster /assets/img/knak/integration-setup-step-2-add-new-integration.png %})

次に、**Braze**プラットフォームを選択し、Braze APIキーとRESTエンドポイントを提供する。[**Create New Integration**] をクリックして統合を完了します。 

![新しい統合を作成する]({% image_buster /assets/img/knak/integration-setup-step-4-add-api-key.png %})

### ステップ2: Knakテンプレートを同期する

Knak で、Braze に同期するメールを見つけて [**Publish**] を選択し、次に [**Sync**] を選択します。

![Knak 統合2]({% image_buster /assets/img/knak/integration-post-step-1-sync.png %})

次にメール名を確認し、[**Sync**] をクリックします。

![Knak 統合2]({% image_buster /assets/img/knak/integration-post-step-2-asset-name.png %})

## 統合を利用する

アップロードした Knak メールは、Braze の**[エンゲージメント] > [テンプレートとメディア]** にあります。見た目がよく、ブランドらしく、完全にレスポンシブです。クリエイティビティを存分に発揮してください。


