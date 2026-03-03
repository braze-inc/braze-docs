---
nav_title: データソースを接続する
article_title: データソースを接続する
page_order: 1
description: "顧客データソースをBrazeAI Decisioning Studio Proに接続し、パーソナライズされたAIデシジョニングを行う方法を学ぶ。"
---

# データソースを接続する

> BrazeAI Decisioning Studio™ Proのエージェントは、効果的な意思決定を行うために、顧客のコンテキストを完全に理解する必要がある。この記事では、顧客データソースをDecisioning Studio Proに接続する方法を説明する。

{% alert tip %}
AIデシジョニング・サービス・チームは、最適なパフォーマンスを実現するためのデータ接続の設定をサポートする。
{% endalert %}

## サポートされている統合パターン

Decisioning Studio Proは、顧客データを接続するための複数の統合パターンをサポートしている：

| 統合パターン | 最適な用途 | セットアップの複雑さ |
|---------------------|----------|------------------|
| **Braze データプラットフォーム** | Brazeをすでにご利用の顧客 | 低 |
| **Brazeクラウドデータインジェスト（CDI）** | 外部データウェアハウスとの接続 | 中 |
| **クラウドストレージ（GCS、AWS、Azure）** | 他のプラットフォームからの直接データエクスポート | 中 |
| **CEP統合** | SFMC、Klaviyoデータ拡張機能 | 中 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## 顧客データの種類

以下の顧客データ資産は、エージェントがより効果的にパーソナライズするのに役立つ：

| データタイプ | 説明 | 例 |
|-----------|-------------|----------|
| **顧客プロファイル** | 静的属性とゆっくり変化する属性 | 顧客年数、地域、獲得チャネル、満足度、生涯価値推定値。 |
| **顧客行動** | アクティビティとエンゲージメントのパターン | アカウントログイン、デバイスの種類、顧客サービスとのやり取り、製品の使用状況 |
| **取引履歴** | 購買およびコンバージョンデータ | 購入商品、取引金額、支払方法、購入チャネル |
| **マーケティング・エンゲージメント** | レスポンシブ対応 | メール開封／クリック、SMSエンゲージメント、Webおよびモバイルアクティビティ、アンケートレスポンス |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert tip %}
顧客に関する情報が多ければ多いほど、エージェントのパフォーマンスは向上する。あなたのビジネスにとって特に重要なインサイトに関するデータを含めることを検討する（例えば、AIがロイヤルティ顧客に対してどのように異なる扱いをするか確認したい？ロイヤルティのステータスが顧客データに入っていることを確認する）。
{% endalert %}

## プラットフォーム別にデータを接続する

{% tabs %}
{% tab Braze %}

### Brazeを通じて顧客データを送信する

BrazeAI Decisioning Studioは、すでにBrazeデータプラットフォームに送信しているすべてのデータを使用できる。

現在ユーザープロファイルやカスタム属性に保存されていない、Decisioning Studioで使用したい顧客データがある場合は、[Braze Cloud Data Ingestionを]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)使用して他のソースからデータを取り込むことを推奨します。

CDIは直接の統合をサポートしている：

- Snowflake
- レッドシフト
- ビッグクエリ
- Databricks
- Microsoft Fabric
- AWS S3

サポートされているデータソースの全リストは、[クラウドデータ・インジェストーションを]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)参照のこと。

Braze Data Platformに送信するデータにご納得いただけましたら、AIデシジョニングサービスチームにご連絡いただき、ユーザープロファイルのどのフィールドまたはカスタム属性をAIデシジョニングに使用するかをご相談ください。

このプロセスを合理化するために、Decisioning Studioで使用すべき顧客の行動を最もよく表していると思われるBrazeユーザープロファイル属性のリストを作成する（[使用可能なフィールドのリストを]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/#fields-to-export)参照）。サービス・チームは、どのフィールドがAIデシジョニングに最も適しているかを決定するためのディスカバリー・セッションの実施も支援できる。

データ送信のオプションには他にも以下のものがある：

- SDK経由でBrazeカスタムイベントを送信する
- RESTエンドポイント([`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track))

これらのパターンは、より多くの開発労力を必要とするが、現在のBrazeの構成によっては好ましい場合もある。詳しくは、AI意思決定サービス・チームにお問い合わせいただきたい。

{% endtab %}
{% tab SFMC %}

### SFMCを通じて顧客データを送信する。

セールスフォース・マーケティングクラウドとの統合のため：

1. 顧客データ用にSFMC Data Extensionを設定する。
2. Decisioning Studioが必要とする適切な権限で、API統合用のSFMCインストールパッケージを設定する。
3. デシジョニング・スタジオは利用可能な最新のインクリメンタルデータからプルするため、データエクステンションが毎日更新されるようにする。

拡張機能IDとAPIキーをAI Decisioning Servicesチームに提供する。顧客データを取り込むための次のステップをサポートしてくれる。

{% endtab %}
{% tab Klaviyo %}

### Klaviyoを通じて顧客データを送信する

Klaviyoとの統合のために：

1. 顧客プロファイルデータがKlaviyoプロファイルで利用可能であることを確認する。
2. プロファイルにフルアクセスできる秘密APIキーを生成する
3. API キーを AI Decisioning Services チームに提供する。

APIキーの設定の詳細については、[Klaviyoドキュメントを](https://help.klaviyo.com/hc/en-us/articles/115005237908)参照のこと。

{% endtab %}
{% tab Cloud Storage %}

### その他のクラウドソリューション（Google Cloud Storage、Azure、AWS）

顧客データが現在Braze、SFMC、またはKlaviyoに保存されていない場合、次の最良のステップは、BrazeがコントロールするGoogle Cloud Storageバケットに直接自動エクスポートを設定することである。AWSやAzureへのエクスポートもサポートできる（GCSが望ましいが）。これらのプラットフォームでは、それらのクラウドプラットフォームの内部クラウドストレージにエクスポートし、Brazeはそのデータを引き出すことができる。

これが可能かどうかを判断するには、マーテク・プラットフォームのドキュメントを参照すること。以下に例を示します。

- mParticleは、[Google Cloud Storageとのネイティブな統合を](https://www.mparticle.com/integration/google-cloud-storage/)提供している。
- [Twilio Segment](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [トレジャーデータ](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [アドビ・エクスペリエンス・プラットフォーム](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

これが可能であれば、顧客データをエクスポートするGCSバケットを提供し、Decisioning Studioに隔離することができる。

{% endtab %}
{% endtabs %}

## ベストプラクティス

- **説明的なカラム名**：顧客データは、明確で説明的なカラム名を持つべきである。理想的には、データ辞書が提供されるべきである。
- **インクリメンタル更新**だ：顧客履歴全体を毎日スナップショットするよりも、増分ファイルの方が望ましい。
- **一貫した識別子**：各レコードには、すべてのデータ資産で一貫性のある一意の顧客識別子が含まれていなければならない。
- **タイムスタンプを含む**：正確なアトリビューションとエージェントのトレーニングのために、記録には関連するタイムスタンプが必要である。

## 顧客統合

その他のオプションや完全な顧客データパイプラインも可能である。これらの作業には、追加サービス作業や開発作業が必要になる場合がある。何が実現可能で最適かを判断するには、AI意思決定サービスチームと連携する。

{% alert important %}
このガイドでは、最も一般的な統合パターンについて説明する。情報セキュリティーは、すべての接続ポイントを審査する必要があり、ソリューション・コンサルタントが導入に関するアドバイスを提供する。
{% endalert %}

## 次のステップ

データソースを接続したら、オーケストレーションの設定に進む：

- [オーケストレーションの設定]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/set_up_orchestration/)

