---
nav_title: アクショナブル・ドット・ミー
article_title: アクショナブル・ドット・ミー
description: "この参考記事では、Brazeと独自のソフトウェアおよびプロセスであるactionable.meとのパートナーシップについて概説している。"
alias: /partners/actionableme/
page_type: partner
search_tag: Partner

---

# actionable.me

> [actionable.me][2]データおよびCRMエージェンシーであるMassive Rocketのチームによって構築された、CRMプログラムを実行するための標準化され、自動化されたアプローチであり、Brazeの顧客が迅速、一貫性、予測可能な価値を得られるように設計されたツールとプロセスを提供する。 

Brazeとactionable.me の統合により、Brazeの活用状況をモニターするサービスを展開することができる。ツールとプロセスを組み合わせることで、CRMのパフォーマンスを迅速にベンチマークし、新たな機会を特定し、より良いパフォーマンスを実現する方法を提案する。

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
| actionable.me アカウント | このパートナーシップを利用するには、actionable.me のアカウントが必要である。 |
| Braze REST API キー | 次のセクションに記載されている権限を持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント | [RESTエンドポイントのURL][1]。エンドポイントは、インスタンスのBraze URLに依存する。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

Brazeとactionable.me を統合するには、actionable.me プラットフォームを設定し、Braze APIキーをBrazeで作成し、actionable.me ダッシュボードで設定する必要がある。

### ステップ 1:BrazeのAPIキーを作成する

Brazeで、**Settings**>**API Keysに**移動する。**Create New API Keyを**選択し、以下のパーミッションが追加されていることを確認する：

- `campaigns.list`
- `campaigns.data_series`
- `campaigns.details`
- `sends.data_series`
- `segments.list`
- `segments.data_series`
- `segments.details`
- `events.list`
- `canvas.list`
- `canvas.data_series`
- `canvas.details`
- `canvas.data_summary`
- `kpi.mau.data_series`
- `kpi.dau.data_series`
- `kpi.new_users.data_series`
- `kpi.uninstalls.data_series`

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、**Developer Console**>**API Settingsから**APIキーを作成できる。
{% endalert %}

### ステップ2:actionable.me チームに情報を提供する

統合を完了するには、REST APIキーと[RESTエンドポイントURLを][1] actionable.me オペレーション・チームに提供する必要がある。actionable.me が接続を確立し、セットアップ完了後に連絡を取り、インサイトの共有を開始する。

![actionable.me 運営チームが設定するactionable.me 「プラットフォームの追加」ページ。][5]

## トラブルシューティング

actionable.me またはMassive Rocketチームまでご連絡を。[massiverocket.com][3]

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://actionable.me
[3]: mailto:info@massiverocket.com
[4]: {% image_buster /assets/img/actionableme/image1.png %}
[5]: {% image_buster /assets/img/actionableme/image2.png %}
