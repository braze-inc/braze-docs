---
nav_title: actionable.me
article_title: actionable.me
description: "このリファレンス記事では、Braze と actionable.me のパートナーシップについて説明します。actionable.me は、Braze への投資を今すぐ最大限に引き出すことができる専用ソフトウェアおよびプロセスです。"
alias: /partners/actionableme/
page_type: partner
search_tag: Partner

---

# actionable.me

> [actionable.me](https://actionable.me) は、データおよび CRM エージェンシーである Massive Rocket のチームによって開発された、CRM プログラムを実行するための標準化および自動化されたアプローチです。Braze のお客様に、迅速かつ一貫性があり予測可能な方法で価値を実現するためのツールとプロセスを提供します。 

_この統合は actionable.me によって管理されます。_

## 統合について

Braze と actionable.me の統合により、Braze の使用状況を監視するためのサービスをデプロイできます。ツールとプロセスを組み合わせることで、CRM のパフォーマンスが迅速にベンチマークされ、新しい機会が特定され、パフォーマンスの向上に関する推奨事項が提供されます。

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
| actionable.me アカウント | このパートナーシップを活用するには、actionable.me アカウントが必要です。 |
| Braze REST API キー | 次のセクションに記載されている権限を持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze REST エンドポイント | [あなたのRESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。お客様のエンドポイントは、お客様のインスタンスのBraze URLに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

Braze とactionable.me を統合するには、actionable.me プラットフォームを設定し、Braze API キーを Braze で作成して actionable.me ダッシュボードで設定する必要があります。

### ステップ1:BrazeのAPIキーを作成する

Braze で [**設定**] > [**API キー**] の順に移動します。[**新しい API キーを作成**] を選択し、次の権限が追加されていることを確認します。

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

### ステップ2:actionable.me チームに情報を提供する

統合を完了するには、REST API キーと [REST エンドポイント URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) を actionable.me オペレーションチームに提供する必要があります。その後 actionable.me が接続を確立し、設定完了後に連絡を取り、インサイトの共有を開始します。

![actionable.me 運営チームが設定するactionable.me 「プラットフォームの追加」ページ。]({% image_buster /assets/img/actionableme/image2.png %})

## トラブルシューティング

その他のサポートについては、actionable.me またはMassive Rocket チーム ([info@massiverocket.com](mailto:info@massiverocket.com)) にお問い合わせください。


