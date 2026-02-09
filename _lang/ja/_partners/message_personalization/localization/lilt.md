---
nav_title: LILT
article_title: LILT
description: "この参考記事では、BrazeとLILTのパートナーシップについて概説している。"
alias: /partners/lilt/
page_type: partner
search_tag: Partner
---

# LILT

> [LILTは](https://lilt.com/)、企業の翻訳とコンテンツ作成のための完全なAIソリューションである。LILTは、AIエージェントと完全に自動化されたワークフローにより、グローバル企業のコンテンツ、製品、コミュニケーション、サポート業務の拡張と最適化を可能にする。

_この統合はLILTによって維持されている。_

## この統合について

LILT Braze Connectorは、AIスピードとエンタープライズグレードの品質でHTMLメールテンプレートの翻訳を可能にする。ブランドに合わせたインスタント翻訳や品質保証されたベリファイド翻訳を依頼し、Brazeで直接LILTから多言語メールコンテンツを受け取る。 

## ユースケース

LILTのBrazeインテグレーションは、翻訳プロセスをオートメーション化し、高速化することで、グローバルマーケティングチームは、ブランドの一貫性を保ちながら、迅速に多言語キャンペーンを開始することができる。

### 合理化されたグローバルキャンペーンの開始

手作業による翻訳のハンドオフによる遅延なしに、複数の地域で同時にマーケターキャンペーンを開始する。

- **シナリオ:**あなたの会社は10カ国で新製品を発売する。
- **ソリューション:**マーケティングチームがBrazeで英語のメールテンプレートを完成させ、`LILT: Ready` のタグを付けると、LILTコネクターが自動的にコンテンツを取り込む。ドメインに特化した言語スペシャリストが、品質保証のためにLILTプラットフォームでAI翻訳プロンプトをレビューし、Connectorが翻訳されたバージョンをBrazeにプッシュバックする。
- **メリットだ：**グローバルキャンペーンの市場投入までの時間を数日から数時間に短縮し、すべての顧客が最適なタイミングで新製品発表を受け取ることができる。

### ブランドに合わせたローカライゼーションを即座に行う

LILTのAIを使えば、一刻を争うコミュニケーションのために、即座に、オンブランドの翻訳を行うことができる。

- **シナリオ:**フラッシュセール、期間限定オファー、緊急サービス停止などのメールを、5つの地域に即座に配信しなければならない。
- **ソリューション:**メールテンプレートに`LILT: Instant` のタグを付ける。LILTは、あなたの会社に特有のAIと言語資産（用語集やスタイルガイドなど）を使用して、数分以内に高品質でブランド一貫性のある翻訳を生成する。
- **メリットだ：**一刻を争うマーケティングに不可欠な、ブランドの声や品質を犠牲にすることなく、ハイパーレスポンシブでリアルタイムなコミュニケーションを可能にする。

## 前提条件

| 前提条件       | 説明 |                        
|-----------------------|-----------------|
| LILTのアカウント   | このパートナーシップを利用するには、LILTアカウントが必要である。  |
| Braze REST API キー  | 以下の権限を持つBraze REST APIキー：<br>- `templates.email.create`<br>- `templates.email.update`<br>- `templates.email.info`<br>- `templates.email.list`<br>- `templates.translations.source.get`<br>- `templates.translations.update`<br>- `templates.translations.get`<br>-`templates.translations.all.get`<br><br> ダッシュボードの**「設定」**>「**APIキー**」からこのキーを作成する。 |
| Braze RESTエンドポイント | [あなたのRESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントはインスタンスの Braze URL に応じて異なります。  |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}


## 統合

### ステップ 1: LILTブレイズコネクターを設定する

1. LILTにログインし、**Connect**>**New Connector**>**Brazeと**進む。
	
![LILTのコネクターをBrazeする。]({% image_buster /assets/img/lilt/image_1_select_connector.png %})

{: start="2"}
2\.Brazeコンテンツに必要なローカライゼーションワークフローを選択する。

![LILTのBrazeワークフロー。]({% image_buster /assets/img/lilt/image_2_select_workflow.png %})	

{: start="3"}
3\.必要な設定の詳細を入力し、確認する：
- APIキー
- Braze RESTエンドポイント

![完全なAPI認証情報。]({% image_buster /assets/img/lilt/image_3_api_creds.png %})	

{: start="4"}
4. **Verifyを**選択してセットアップをテストする。接続が確認されたら、設定を保存する。

### ステップ 2:Brazeのワークスペースを準備する

1. Brazeワークスペース設定で多言語機能を有効にする。

![Brazeでローカライゼーションを設定する。]({% image_buster /assets/img/lilt/image_4_lilt_locales.png %})	

{: start="2"}
2\.LILTワークフロー用にBrazeで以下のタグを作成する： 
- `LILT: Ready`
- `LILT: In progress`
- `LILT: Sent to LILT`
- `LILT: Delivered`
- `LILT: Needs Attention`
- `LILT: Instant`

![BrazeでLILTタグを設定する。]({% image_buster /assets/img/lilt/image_5_lilt_tags.png %})	

{: start="3"}
### ステップ 3:コンテンツを翻訳のためにLILTに送る 

1. LILT Braze Connectorを設定した後、Brazeメールテンプレート内でLiquid翻訳タグを使用して、翻訳対象のコンテンツを識別する。 
- 例:  {% raw %}`{% translation id_0 %}`こんにちは、 `{{first_name}}!{% endtranslation %}`{% endraw %}
2. 希望するワークフローを示すテンプレートタグを更新して、翻訳を開始する： 
- 検証された翻訳には`LILT: Ready` を選ぶ
- `LILT: Instant` 、ブランドに合ったインスタント翻訳を選択する。
3. LILTのBrazeコネクタは、タグ付けされたコンテンツをLILTに取り込むために、あらかじめ設定されたタイミングで動作する。Brazeのコンテンツタグが自動的に更新され、プロジェクトの段階が反映されるため、翻訳の進捗状況を把握できる。 
	
![翻訳タグ付きBrazeメールテンプレート。]({% image_buster /assets/img/lilt/image_6_braze_template.png %})	