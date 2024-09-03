---
nav_title: Airbyte
article_title: Airbyte
description: "この参考記事では、BrazeとAirbyteの統合について取り上げている。Airbyteはオープンソースのデータ統合エンジンで、データウェアハウス、レイク、データベース内のデータを統合し、AirbyteからBrazeにリアルタイムイベントを転送するのに役立つ。"
alias: /partners/airbyte/
page_type: partner
search_tag: Airbyte

---

# Airbyte

> [Airbyteは](https://airbyte.com/)オープンソースのデータ統合エンジンで、データウェアハウス、レイク、データベース内のデータの統合を支援する。

BrazeとAirbyteの統合により、ユーザーはデータパイプラインを作成し、すべてのアプリケーションとデータベースを中央倉庫に接続することで、Brazeのデータを収集・分析することができる。セントラルウェアハウスにデータが収集された後、データチームは好みのビジネスインテリジェンスツールを使ってBrazeのデータを効率的に探索することができる。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| エアバイトクラウドアカウント | この統合を利用するには、[Airbyte Cloud](https://cloud.airbyte.io/workspaces)アカウントが必要である。 |
| Braze REST API キー | すべての権限を持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント | \[あなたのRESTエンドポイントURL][1].エンドポイントは、インスタンスのBraze URLに依存する。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

1. Airbyte Cloudアカウントで、**Sources > + New Source > Set up Sourceに**移動する。
2. ソース名に "Braze "と入力し、ソースのドロップダウンから**Brazeを**選択する。
3. エンドポイントURL、Braze REST APIキー、開始日を入力する。**ソースの設定を**クリックする。

### 対応する同期モード

AirbyteのBrazeソースコネクターは、以下の[シンクモードを](https://docs.airbyte.com/cloud/core-concepts#connection-sync-modes)サポートしている：
- **フル・リフレッシュ｜上書き**：ソースからすべてのレコードを同期し、デスティネーションのデータを上書きして置き換える。
- **インクリメンタル同期｜アペンド**：ソースから新しいレコードを同期し、データを削除せずにデスティネーションに追加する。

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
レート制限はストリームによって異なる。詳しくは[料金制限表を](https://www.braze.com/docs/api/api_limits/#rate-limits-by-request-type)参照のこと。
{% endalert %}