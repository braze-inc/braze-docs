---
nav_title: Hightouch
article_title: Hightouch
description: "このリファレンス記事では、Braze と Hightouchのパートナーシップについて説明します。Hightouch は、ウェアハウスの顧客データをカスタムツールと同期するプラットフォームです。"
page_type: partner
search_tag: Partner

---

# Hightouch

> [Hightouch](https://hightouch.io) は最新のデータ統合プラットフォームであり、IT チームやエンジニアリングチームの支援を必要とせずに、ウェアハウスやデータレイクからお客様が選択したアプリに、顧客データ、製品データ、または独自のデータを同期できます。

Braze と Hightouch の統合により、データウェアハウスの最新の顧客データを使用して、Braze でより優れたキャンペーンを作成できます。顧客データを Braze に自動的に同期させることで、データの整合性を心配する必要がなくなり、世界レベルのカスタマーエクスペリエンスの構築に集中して取り組むことができます。 

この統合により、[ユーザーコホートをBrazeにインポート]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/hightouch/hightouch_cohort_import/)し、倉庫にしか存在しないデータに基づいてターゲットを絞ったキャンペーンを送信することもできる。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Hightouch アカウント | このパートナーシップを活用するには、Hightouch アカウントが必要です。
| Braze REST API キー | `users.track` および `users.export.ids` の権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント  | REST エンドポイントのURL。エンドポイントはインスタンスの [Braze URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) に応じて異なります。<br><br>Hightouch には、Braze インスタンスが配置されているクラスターの名前が必要です。例えば、Brazeのエンドポイントが`https://rest.iad-01.braze.com` の場合、必要なのは`iad-01` だけである。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース

* ユーザーとアカウントに関するデータをBrazeに同期し、超パーソナライズされたキャンペーンを構築する。
* Braze セグメントをウェアハウスからの最新データで自動的に更新する。
* 他の顧客接点からのデータをBrazeに取り込むことで、より良い体験を提供する。
* ユーザーのコホートをBrazeにインポートし、ターゲットを絞ったキャンペーンやキャンバスを送信できる。 

## 統合

### ステップ1:Hightouch Braze 宛先を作成する

1. Hightouch プラットフォームの [**Destinations**] セクションで [**Add destination**] をクリックします。
2. 利用可能な目的地のリストから**Brazeを**選択する。
3. Braze REST エンドポイント (「https://rest」を除く) と Braze REST API キーを指定します。<br><br>![]({% image_buster /assets/img/hightouch/hightouch_braze_setup.png %})

### ステップ 2:オブジェクトとイベントの同期

Hightouch では、ユーザーオブジェクトとイベントの両方の同期がサポートされています。

| 目的地 | 説明 | サポートされているモード |
|---|---|---|
| オブジェクト | 宛先のユーザーや組織などのオブジェクトにレコードを同期します。| アップサートまたはアップデート |
| イベント | レコードをイベントとして宛先に同期します。これは多くの場合、トラックコールの形式です。 | イベントまたは購入の追跡 |

{% alert note %}
同期がデータポイントの記録方法にどのように影響するかについては、[Hightouchを](https://hightouch.com/docs/destinations/braze#syncing-and-data-point-consumption)参照のこと。
{% endalert %}

#### Brazeオブジェクトを同期する

Hightouchオブジェクト（ユーザーフィールド）を同等のBrazeデフォルトまたはカスタムフィールドに同期できる。2つのプラットフォーム間でデータを統合するためにレコードマッチングを実行することもできます。

#### Brazeのイベントを同期する

Hightouch では、イベントデータと購入データを追跡し、これらのデータを Braze に同期できます。Hightouchでは、トラッキングデータの設定や存在しないユーザー動作の定義など、同期動作に影響を与えるいくつかのオプションを設定できる。

{% alert important %}
オブジェクトとイベントの同期に関する詳細な手順については、[Hightouch のドキュメント](https://hightouch.io/docs/destinations/braze/)を参照してください。
{% endalert %}



## 統合デモ

<div class="video-container">
    <iframe width="560" height="315" src="https://drive.google.com/file/d/1KQdCwZzV88hXMx7AMWgh8izqkldtNv5p/preview" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


