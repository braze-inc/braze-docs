---
nav_title: エアバイト
article_title:Airbyte
description:「この参考記事では、BrazeとAirbyteの統合について説明しています。Airbyteは、データウェアハウス、レイク、データベース内のデータを統合し、AirbyteからBrazeにリアルタイムのイベントを転送するのに役立つオープンソースのデータ統合エンジンです。「
alias: /partners/airbyte/
page_type: partner
search_tag:Airbyte

---

# Airbyte

> [Airbyteは](https://airbyte.com/)、データウェアハウス、レイク、データベース内のデータを統合するのに役立つオープンソースのデータ統合エンジンです。

BrazeとAirbyteの統合により、ユーザーはすべてのアプリケーションとデータベースを中央ウェアハウスに接続することで、Brazeデータを収集および分析するためのデータパイプラインを作成できます。中央ウェアハウスでデータが収集されると、データチームは好みのビジネスインテリジェンスツールを使用してBrazeデータを効果的に探索できます。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
|  | この統合を利用するには、[Airbyte Cloudアカウントが必要です](https://cloud.airbyte.io/workspaces)。 |
| Braze REST API キー | すべての権限を持つBraze REST APIキー。<br><br> これは Braze ダッシュボードの **\[設定] > \[**API キー**]** から作成できます。 |
| Braze REST エンドポイント | \[あなたの REST エンドポイント URL ][1]。エンドポイントは、インスタンスの Braze URL によって異なります。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

1. Airbyte Cloud アカウントで、\[**ソース] > \[+ 新規ソース] > \[ソースの設定**] に移動します。
2. ソース名として「Braze」と入力し、ソースドロップダウンから **Braze** を選択します。
3. エンドポイント URL、Braze REST API キー、および開始日を入力してください。「**ソースを設定**」をクリックします。

### サポート対象の同期モード

AirbyteのBrazeソースコネクタは、[以下の同期モードをサポートしています](https://docs.airbyte.com/cloud/core-concepts#connection-sync-modes)。
- **完全更新 | 上書き**:ソースのすべてのレコードを同期し、送信先データを上書きして置き換えます。
- **インクリメンタル同期 | 追加**:データを削除せずに、ソースから新しいレコードを同期し、送信先に追加します。

### 対応ストリーム

- [`campaigns`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f3b0b3ef-04fb-4a31-8570-e6ad88dacb18)
- [`campaigns_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c07b5ebd-0246-471e-b154-416d63ae28a1)
- [`canvases`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e6c150d7-fceb-4b10-91e2-a9ca4d5806d1)
- [`canvases_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0fd61e93-7edf-4d87-a8dc-052420aefb73)
- [`events`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#93ecd8a5-305d-4b72-ae33-2d74983255c1)
- [`events_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0bd1ab63-d1a5-4301-8d17-246cf24a178c)
- [`kpi_daily_new_users`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#07756c39-cfa0-40a0-8101-03f8791cec01)
- [`kpi_daily_active_users`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#90a64560-65aa-4f71-a8ef-1edf49321986)
- [`kpi_daily_app_uninstalls`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#59c4d592-3e77-42f8-8ff1-d5d250acbeae)
- [`cards`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9fa7a3bc-4a02-4de2-bc4c-8f111750665e)
- [`cards_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9cdc3b1e-641e-4d62-b9e8-42d04ee9d4d8)
- [`segments`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1349e6f4-3ce7-4e60-b3e9-951c99c0993f)
- [`segments_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#62d9d142-cdec-4aea-a287-c13efea7415e)

{% alert note %}
レート制限はストリームによって異なります。詳細については、[レート制限表をご覧ください](https://www.braze.com/docs/api/api_limits/#rate-limits-by-request-type)。
{% endalert %}