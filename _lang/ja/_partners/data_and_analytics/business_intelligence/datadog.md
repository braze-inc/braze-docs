---
nav_title: Datadog
article_title: "Datadog"
description: "この参考記事では、BrazeとDatadogとの提携について概説している。Datadogは、クラウドスケールのアプリケーション向けの観測可能なサービスで、SaaSベースのデータ分析プラットフォームを通じて、サーバー、データベース、ツール、サービスの監視を提供する。"
alias: /partners/datadog/
page_type: partner
search_tag: Partner


---

# Datadog

> [Datadog](https://www.datadoghq.com/) は、クラウド規模のアプリケーション向けオブザーバビリティサービスであり、SaaS ベースのデータ分析プラットフォームでサーバー、データベース、ツール、およびサービスを監視する機能を提供します。

Braze と Datadog の統合により、お客様は Datadog で Braze データを収集し、送信するデータに関するアラートを作成できます。例えば、毎週のニュースレター・キャンペーンで送信されるメッセージの量が異常に少なかったり、通常は1日に数通しか送信しないキャンバス・ステップが数千通を送信し始めたりした場合に、モニターを設定してアラートを出す。 

## 前提条件 

| 必要条件 | 説明 |
|---|---|
| Datadogアカウント | このパートナーシップを活用するには、Datadog アカウントが必要です。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ1:Datadogのキーを生成する

Datadog で [API キー](https://docs.datadoghq.com/account_management/api-app-keys/#api-keys)を作成する必要があります。APIキーを追加するには、「**Organization Settings（組織設定）」>「** **API Keys（APIキー）」>「** **New Key（新規キー）**」の順に移動する。

### ステップ2:Braze にキーを追加する

Braze ダッシュボードで [**パートナー連携**] > [**テクノロジーパートナー**] に移動し、[**Datadog**] を探します。Datadog パートナーページで Datadog API キーを指定します。これで、Braze がDatadog にデータを送信するための接続が作成されます。

## Braze のイベント

接続が統合されると、Brazeは以下のイベントをDatadogに送信する：

- `braze.messaging.sent` - 送信回数

これらの各イベントには、Datadogタグの形でメタデータが付与され、以下のような情報が得られる：

- `app_group_id`
- `app_group_name`
- `campaign_id` /`campaign_name` (利用可能な場合)
- `canvas_id` /`canvas_name` /`canvas_step_id` /`canvas_step_name` (利用可能な場合)

これらのイベントとタグは、Datadog**Metrics Explorer**ページで監視できる。これらのメトリクスは、DataDogに[ディストリビューションとして](https://docs.datadoghq.com/metrics/distributions/)記録される。指標の性質と、DataDog の集約とロールアップの不正確さを考慮して、Braze では、送信中に発生する可能性のある断続的なネットワークエラーやその他の DataDog API エラーの場合は再試行されません。つまり、これら指標の数値が、Braze ダッシュボードや Currents で表示される数値とは若干異なる可能性があります。

![]({% image_buster /assets/img/datadog.png %})

