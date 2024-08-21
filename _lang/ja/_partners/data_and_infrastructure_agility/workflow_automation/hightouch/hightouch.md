---
nav_title: Hightouch
article_title: Hightouch
description: "この参考記事では、BrazeとHightouchのパートナーシップについて概説している。Hightouchは、顧客データを倉庫からビジネスツールに同期させるプラットフォームである。"
page_type: partner
search_tag: Partner

---

# Hightouch

> [Hightouchは][1]、最新のデータ統合プラットフォームであり、倉庫やデータレイクから任意のアプリケーションに顧客、製品、または独自のデータを同期させることができる。

BrazeとHightouchの統合により、データウェアハウスからの最新の顧客データを使って、Braze上でより良いキャンペーンを構築することができる。顧客データを自動的にBrazeに同期させることで、データの整合性を心配する必要がなくなり、ワールドクラスの顧客体験の構築に集中することができる。 

この統合により、[ユーザーコホートをBrazeにインポート]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/hightouch/)し、倉庫にしか存在しないデータに基づいてターゲットを絞ったキャンペーンを送信することもできる。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| ハイタッチアカウント | このパートナーシップを利用するには、ハイタッチ・アカウントが必要である。
| Braze REST API キー | `users.track` および`users.export.ids` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント  | RESTエンドポイントのURL。エンドポイントは、[インスタンスのBraze URLに][2]依存する。<br><br>Hightouchは、Brazeインスタンスのクラスタ名を要求する。例えば、Brazeのエンドポイントが`https://rest.iad-01.braze.com` の場合、必要なのは`iad-01` だけである。|
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

* ユーザーとアカウントに関するデータをBrazeに同期し、超パーソナライズされたキャンペーンを構築する。
* Brazeセグメントをウェアハウスからの新鮮なデータで自動的に更新する。
* 他の顧客接点からのデータをBrazeに取り込むことで、より良い体験を提供する。
* ユーザーのコホートをBrazeにインポートし、ターゲットを絞ったキャンペーンやキャンバスを送信できる。 

## 統合

### ステップ1:ハイタッチ・ブレイズの目的地を作る

1. ハイタッチ・プラットフォームの**宛先**セクションで、**宛先の追加を**クリックする。
2. 利用可能な目的地のリストから**Brazeを**選択する。
3. Braze RESTエンドポイント（"https://rest. "を除く）とBraze REST API Keyを入力する。<br><br>![][3]

### ステップ2:オブジェクトとイベントの同期

ハイタッチは、ユーザー・オブジェクトとイベントの両方への同期をサポートしている。

| 目的地 | 説明 | 対応モード |
|---|---|---|
| オブジェクト | 同期先のユーザーや組織などのオブジェクトにレコードを同期する。| アップサートまたはアップデート |
| イベント | これは多くの場合、トラック・コールの形式である。 | サーキット・イベントまたはサーキット購入 |

{% alert note %}
同期がBrazeのデータポイント消費にどのように影響するかについての詳細は、[Hightouchを](https://hightouch.com/docs/destinations/braze#syncing-and-data-point-consumption)参照のこと。
{% endalert %}

#### Brazeオブジェクトを同期する

Hightouchオブジェクト（ユーザーフィールド）を同等のBrazeデフォルトまたはカスタムフィールドに同期できる。また、レコードマッチングを実行して、2つのプラットフォーム間でデータを統一することもできる。

#### Brazeのイベントを同期する

ハイタッチでは、イベントや購買データを追跡し、Brazeと同期させることができる。Hightouchでは、トラッキングデータの設定や存在しないユーザー動作の定義など、同期動作に影響を与えるいくつかのオプションを設定できる。

{% alert important %}
オブジェクトとイベントの同期に関する詳しい説明は、[Hightouchのドキュメントを](https://hightouch.io/docs/destinations/braze/)参照されたい。
{% endalert %}



## 統合デモ

<div class="video-container">
    <iframe width="560" height="315" src="https://drive.google.com/file/d/1KQdCwZzV88hXMx7AMWgh8izqkldtNv5p/preview" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

[1]: https://hightouch.io
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: {% image_buster /assets/img/hightouch/hightouch_braze_setup.png %}
[4]: https://hightouch.io/docs/destinations/braze/

