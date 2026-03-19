---
nav_title: データソースを接続する
article_title: データソースを接続する
page_order: 1
description: "顧客データソースをBrazeAI Decisioning Studio Proに接続し、パーソナライズされたAI意思決定を行う方法を学ぶ。"
---

# データソースを接続する

> BrazeAI Decisioning Studio™ Proエージェントは、効果的な意思決定を行うために顧客の状況を完全に理解する必要がある。この記事では、顧客データソースをDecisioning Studio Proに接続する方法を説明する。

{% alert tip %}
AI意思決定サービスチームは、最適なパフォーマンスを実現するためのデータ接続設定を支援する。
{% endalert %}

## サポートされている統合パターン

Decisioning Studio Proは、顧客データを接続するための複数の統合パターンをサポートしている。

| 統合パターン | 最適な用途 | 設定の複雑さ |
|---------------------|----------|------------------|
| **Braze データプラットフォーム** | 既にBrazeを利用している顧客 | 低 |
| **Braze Cloud データ取り込み (CDI)** | 外部データウェアハウスを接続する | 中 |
| **クラウドストレージ（GCS、AWS、Azure）** | 他のプラットフォームからの直接データエクスポート | 中 |
| **CEP統合** | SFMC、Klaviyoデータ拡張機能 | 中 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## 顧客データの種類

以下の顧客データ資産は、エージェントがより効果的にパーソナライゼーションを行うのに役立つ：

| データタイプ | 説明 | 例 |
|-----------|-------------|----------|
| **顧客プロファイル** | 静的でゆっくりと変化する属性 | 顧客歴年数、地域、獲得チャネル、満足度レベル、生涯価値の推定値 |
| **顧客行動** | 活動とエンゲージメントのパターン | アカウントのログイン、デバイスの種類、顧客サービスとのやり取り、製品の使用状況 |
| **取引履歴** | 購入とコンバージョンデータ | 購入した商品、取引金額、支払い方法、購入チャネル |
| **マーケティングエンゲージメント** | 通信への応答 | メール開封率／クリック率、SMSエンゲージメント、Webとモバイルの活動、アンケート回答 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert tip %}
エージェントが顧客について持っている情報が多ければ多いほど、彼らのパフォーマンスは向上する。自社にとって特に重要なインサイトに関するデータを検討して含めること（例えば、AIがロイヤルティ顧客をどのように差別的に扱うかを確認したいか？）。顧客データにロイヤルティステータスが含まれていることを確認せよ。
{% endalert %}

## プラットフォームごとにデータを接続する

{% tabs %}
{% tab Braze %}

### 顧客データをBraze経由で送信する

BrazeAI Decisioning Studioは、既にBrazeデータプラットフォームに送信している全てのデータを利用できる。

ユーザープロファイルやカスタム属性に現在保存されていない顧客データをDecisioning Studioで使用したい場合、推奨される方法は[Braze Cloud Data]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) [Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)を使用して他のソースからデータをインジェストすることだ。

CDIは以下との直接連携をサポートする：

- Snowflake
- 赤方偏移
- BigQuery
- Databricks
- Microsoft Fabric
- AWS S3

サポートされているデータソースの完全なリストについては、[クラウドデータ取り込みを]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)参照せよ。

Brazeデータプラットフォームに送信するデータに問題がなければ、AI意思決定サービスチームに連絡し、ユーザープロファイルやカスタム属性のどのフィールドをAI意思決定に使用すべきか相談する。

このプロセスを効率化するため、顧客行動を最も適切に表すと考えるBrazeユーザープロファイル属性のリストを作成する。このリストはDecisioning Studioで使用すべき属性である（[利用可能なフィールドのリスト]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/#fields-to-export)を参照）。サービスチームは、どのフィールドがAI意思決定に最も適しているかを判断するためのディスカバリーセッションの実施も支援できる。

データを送信するその他の方法には以下がある：

- SDK経由でBrazeカスタムイベントを送信する
- RESTエンド[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)ポイントを使用したイベント送信

これらのパターンはより多くの開発作業を必要とするが、現在のBrazeの設定によっては好ましい場合もある。AI意思決定サービスチームに問い合わせて、学習することだ。

{% endtab %}
{% tab SFMC %}

### 顧客データをSFMC経由で送信する

Salesforce Marketing Cloudの統合については：

1. 顧客データ用にSFMCデータ拡張機能を設定する
2. Decisioning Studioが要求する適切な権限で、API統合用のSFMCインストール済みパッケージを設定する。
3. データ拡張は毎日更新されるようにする。Decisioning Studioは利用可能な最新の増分データを取得するからだ。

拡張機能IDとAPI キーをAI意思決定サービスチームに提供せよ。彼らは顧客データの取り込みにおける次のステップを支援する。

{% endtab %}
{% tab Klaviyo %}

### 顧客データをKlaviyo経由で送信する

Klaviyoの統合については：

1. 顧客プロファイルデータがKlaviyoプロファイルで利用可能であることを確認する
2. プロファイルへの完全なアクセス権を持つプライベートAPI キーを生成する
3. API キーをAI意思決定サービスチームに提供せよ

API キーの設定に関する詳細は、[Klaviyoのドキュメント](https://help.klaviyo.com/hc/en-us/articles/115005237908)を参照せよ。

{% endtab %}
{% tab Cloud Storage %}

### その他のクラウドソリューション（Google Cloud Storage、Azure、AWS）

顧客データが現在Braze、SFMC、またはKlaviyoに保存されていない場合、次に取るべき最善のステップは、Brazeが管理するGoogle Cloud Storageバケットへの自動エクスポートを設定することだ。AWSやAzureへのエクスポートもサポートできる（ただしGCSが望ましい）。これらのプラットフォームでは、各クラウドプラットフォームの内部クラウドストレージへエクスポートすれば、Brazeがそのデータを取得できる。

これが可能かどうかを判断するには、使用しているマーテクプラットフォームのドキュメントを参照せよ。以下に例を示します。

- mParticleは[Google Cloud Storageとのネイティブ統合](https://www.mparticle.com/integration/google-cloud-storage/)を提供する。
- [Twilio Segment](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [トレジャーデータ](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [アドビ エクスペリエンス プラットフォーム](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

これが可能であれば、顧客データをエクスポートするためのGCSバケットを提供できる。そのバケットはDecisioning Studioに隔離されている。

{% endtab %}
{% endtabs %}

## ベストプラクティス

- **説明的な列名**：顧客データには、明確で説明的な列名をつけるべきだ。理想的には、データディクショナリを提供すべきだ。
- **増分更新**：増分ファイルは、顧客履歴全体のスナップショットを毎日取るよりも好ましい。
- **一貫した識別子**：各レコードには、すべてのデータ資産で一貫した固有の顧客識別子を含めなければならない。
- **タイムスタンプを含める**：記録には正確なアトリビューションとエージェントのトレーニングのために、関連するタイムスタンプが付与されるべきだ。

## カスタム統合

他の選択肢や完全にカスタムのデータパイプラインも可能だ。これらは、貴社のチームによる追加のサービス作業や開発作業が必要となる可能性がある。実現可能で最適な方法を判断するには、AI意思決定サービスチームと連携せよ。

{% alert important %}
このガイドでは、最も一般的な統合パターンを説明する。情報セキュリティ部門は引き続き全ての接続ポイントを審査する必要がある。ソリューションコンサルタントは実装に関する助言を提供できる。
{% endalert %}

## 次のステップ

データソースを接続したら、オーケストレーションの設定に進む：

- [オーケストレーションを設定する]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/set_up_orchestration/)

