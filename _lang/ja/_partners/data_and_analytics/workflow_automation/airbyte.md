---
nav_title: Airbyte
article_title: Airbyte
description: "この参考記事では、BrazeとAirbyteの統合について取り上げている。Airbyte はデータウェアハウス、データレイク、データベースにデータを統合するのに役立つオープンソースのデータ統合エンジンであり、Airbyte から Braze にリアルタイムのイベントが転送されます。"
alias: /partners/airbyte/
page_type: partner
search_tag: Airbyte

---

# Airbyte

> [Airbyte](https://airbyte.com/) は、データウェアハウス、データレイク、データベースにデータを統合するのに役立つオープンソースのデータ統合エンジンです。

_この統合は Airbyte によって管理されます。_

## 統合について

BrazeとAirbyteの統合により、ユーザーはデータパイプラインを作成し、すべてのアプリケーションとデータベースを中央倉庫に接続することで、Brazeのデータを収集・分析することができる。中央ウェアハウスにデータが収集されると、データチームは好きなビジネスインテリジェンスツールを使って、Braze のデータを効率的に調査できます。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Airbyte Cloud アカウント | この統合を利用するには、[Airbyte Cloud](https://cloud.airbyte.io/workspaces)アカウントが必要である。 |
| Braze REST API キー | すべての権限を持つBraze REST APIキー。<br><br> これはBrazeのダッシュボードで**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | お客様のエンドポイントは、お客様のインスタンスのBraze URLに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

1. Airbyte Cloud アカウントで **[Sources] > [+ New Source] > [Set up the Source]** に移動します。
2. ソース名として「Braze」を入力し、ソースのドロップダウンから [**Braze**] を選択します。
3. エンドポイント URL、Braze REST API キー、および開始日を指定します。[**Set up Source**] をクリックします。

### 対応する同期モード

Airbyte の Braze ソースコネクターは、以下の[同期モード](https://docs.airbyte.com/cloud/core-concepts#connection-sync-modes)をサポートしています。
- **フル・リフレッシュ｜上書き**：ソースからすべてのレコードを同期し、デスティネーションのデータを上書きして置き換える。
- **Incremental Sync | Append**:ソースから新しいレコードを同期し、データを削除せずに宛先に追加する。

### サポートされるストリーム

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
レート制限はストリームによって異なる。詳しくは[料金制限表を]({{site.baseurl}}/api/api_limits/#rate-limits-by-request-type)参照のこと。
{% endalert %}
