---
nav_title: Datadog
article_title: "Datadog"
description: "この参考記事では、BrazeとDatadogとの提携について概説している。Datadogは、クラウドスケールのアプリケーション向けの観測可能なサービスで、SaaSベースのデータ分析プラットフォームを通じて、サーバー、データベース、ツール、サービスの監視を提供する。"
alias: /partners/datadog/
page_type: partner
search_tag: Partner


---

# Datadog

> [Datadogは](https://www.datadoghq.com/)、クラウドスケールのアプリケーションのための観測可能なサービスで、SaaSベースのデータ分析プラットフォームを通じて、サーバー、データベース、ツール、サービスの監視を提供する。

BrazeとDatadogの統合により、顧客はDatadogでBrazeのデータを収集し、当社が送信するデータに対してアラートを作成することができる。例えば、毎週のニュースレター・キャンペーンで送信されるメッセージの量が異常に少なかったり、通常は1日に数通しか送信しないキャンバス・ステップが数千通を送信し始めたりした場合に、モニターを設定してアラートを出す。 

## 前提条件 

| 必要条件 | 説明 |
|---|---|
| Datadogアカウント | このパートナーシップを利用するには、Datadogアカウントが必要である。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:Datadogのキーを生成する

Datadogでは、[APIキーを](https://docs.datadoghq.com/account_management/api-app-keys/#api-keys)作成する必要がある。APIキーを追加するには、「**Organization Settings（組織設定）」>「** **API Keys（APIキー）」>「** **New Key（新規キー）**」の順に移動する。

### ステップ2:ブレーズにキーを追加する

Brazeのダッシュボードで、**Partner Integrations**>**Technology Partnersと**進み、**Datadogを**検索する。Datadog パートナーページで、Datadog API キーを入力する。これで、BrazeがDatadogにデータを送信するための接続が作成される。

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、「**統合」の**下に**テクノロジー・パートナーが**ある。
{% endalert %}

## ブレイズのイベント

接続が統合されると、Brazeは以下のイベントをDatadogに送信する：

- `braze.messaging.sent` - 送信回数

これらの各イベントには、Datadogタグの形でメタデータが付与され、以下のような情報が得られる：

- `app_group_id`
- `app_group_name`
- `campaign_id` /`campaign_name` (利用可能な場合)
- `canvas_id` /`canvas_name` /`canvas_step_id` /`canvas_step_name` (利用可能な場合)

これらのイベントとタグは、Datadog**Metrics Explorer**ページで監視できる。これらのメトリクスは、DataDogに[ディストリビューションとして](https://docs.datadoghq.com/metrics/distributions/)記録される。Brazeは、メトリクスの性質とDataDogの集計およびロールアップの不正確さを考慮し、送信中に発生する可能性のある断続的なネットワークエラーやその他のDataDog APIエラーを再試行しない。つまり、これらの数値は、BrazeのダッシュボードやCurrentsで表示される数値とは若干異なる可能性がある。

![][1]

[1]: {% image_buster /assets/img/datadog.png %}
