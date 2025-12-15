---
nav_title: 桶剣道
article_title: "桶剣道"
description: "OkendoとBrazeの統合方法を学習する。"
page_type: partner
search_tag: Partner
alias: /partners/okendo/
---

# 桶剣道

> [オケンドは](https://okendo.io/)、アドボカシーの育成、クチコミの拡大、生涯価値の最大化のためのツールを提供する統合カスタマーマーケティングプラットフォームであり、より迅速で効率的な成長のために顧客を動員する。

*この統合はオケンドによって維持されている。*

## 統合について

BrazeとOkendoの統合は、レビュー、ロイヤルティ、紹介、アンケート、クイズなど、Okendoのプラットフォームの複数の製品にまたがって機能する。Okendoはカスタムイベントとユーザー属性をBrazeに送信し、パーソナライズされたメッセージやトリガーメッセージに利用できる。  

## 前提条件

| 必要条件            | 説明                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| 桶胴口座         | このパートナーシップを利用するには、オケンドのアカウントが必要だ。        |
| Braze REST API キー     | `users.track` 権限を持つ Braze REST API キー。これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze REST エンドポイント    | [あなたのRESTエンドポイントURL]({{site.baseurl}}/api/basics/#endpoints)。エンドポイントはインスタンスの Braze URL に応じて異なります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ 1: オケンドでBraze Connectorを設定する

1. Okendoの**設定**>**Integrations**>**Email& SMS**>**Brazeに**アクセスする。
2. **インテグレーション**設定にAPIエンドポイントとAPIキーを追加する。

### ステップ 2:識別子を設定する

`external_id` フィールドは、各イベントに関連するユーザーを識別するために使用される。フィールドをShopifyカスタマーIDに関連付けるには、**Brazeユーザー識別にShopifyカスタマーIDを使用するを**トグルする。そうでない場合は、各ユーザーのメール・アドレスに関連付けるためにオフに切り替える。

## Okendoのイベントと属性をBrazeに同期させる

### カスタムイベント

{% alert note %}
イベントデータのサンプルについては、[オケンドのドキュメントを](https://support.okendo.io/en/articles/10396885-getting-started-with-braze-and-okendo#h_679a212e3c)参照のこと。
{% endalert %}

#### イベント・レビュー

- オケンドーのレビューが作成された
- 桶狭間のレビュー依頼

#### 紹介イベント

- 桶狭間の紹介状を送る
- オケンド紹介にオプトインする
- オケンド紹介状
- 紹介クーポンを受け取る
- 桶胴紹介クーポンを利用する
- 桶狭間の紹介は却下された

#### ロイヤルティ・イベント

- 桶胴ロイヤリティに加入
- 桶胴ロイヤリティポイント付与
- 桶胴ロイヤリティ・ポイント還元率
- 桶胴ロイヤリティ・ティア変更
- オケンド・ロイヤルティ・ポイント Adjusted

#### アンケートイベント

- 提出されたオケンド調査

#### クイズイベント

- 投稿されたオケンドー・クイズ

### カスタム属性

Okendoは、ユーザープロファイルのデータをBrazeのカスタム属性として送信し、オーディエンスセグメントの作成に利用できる。例としては次のようなものがあります:

- 年齢、誕生日、肌のタイプ、髪の色など、アンケートやレビュー投稿時に尋ねられるプロファイルの質問
- _平均レビュー評価や_ _平均レビュー感情などの_レビュー指標
- _ポイント残高や_ _VIPティアなどの_ロイヤルティ指標
- _紹介成功_数や_紹介総収入などの_紹介指標  
- アンケートから収集したNPSスコア

## オケンドーの製品でBrazeを使う

Okendoの製品によっては、BrazeとOkendoを併用するために追加のステップを踏む必要がある。詳細は以下の記事を参照のこと：

- [Brazeとレビューを統合する](https://support.okendo.io/en/articles/10509722-integrating-reviews-with-braze#h_09c4575b39)
- [ロイヤルティとBrazeの統合](https://support.okendo.io/en/articles/10509615-integrating-loyalty-with-braze#h_47129ea105)
- [Brazeと紹介を統合する](https://support.okendo.io/en/articles/10509748-build-a-canvas-in-braze-to-trigger-referral-emails#h_32fb5ba542)
- [アンケートをBrazeと統合する](https://support.okendo.io/en/articles/11546662-integrating-surveys-with-braze)
- [Brazeとクイズを統合する](https://support.okendo.io/en/articles/10509739-build-a-canvas-in-braze-to-send-quiz-recommendations#h_53748cb121)

{% alert note %}
統合の設定については、オケンドのサポート・チームに問い合わせを。
{% endalert %}
