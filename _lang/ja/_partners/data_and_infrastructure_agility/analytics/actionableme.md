---
nav_title: actionable.me
article_title: actionable.me
description:「この参考記事では、Brazeと、Brazeへの投資をすぐに最大限に活用できる独自のソフトウェアおよびプロセスであるactionable.meとのパートナーシップについて概説しています。「
alias: /partners/actionableme/
page_type: partner
search_tag:Partner

---

# actionable.me

> [actionable.meは][2]、データおよびCRMエージェンシーであるMassive Rocketのチームによって構築され、CRMプログラムを実行するための標準化された自動化されたアプローチであり、Brazeの顧客が迅速かつ一貫して、予測どおりに価値を提供できるように設計されたツールとプロセスを提供します。 

Brazeとactionable.meの統合により、Brazeの利用の進捗状況を監視するサービスをデプロイすることができます。ツールとプロセスを組み合わせることで、CRM パフォーマンスを迅速にベンチマークし、新しい機会を特定し、パフォーマンスを向上させる方法に関する推奨事項を提供します。

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
| アクション可能な.me アカウント | このパートナーシップを利用するには、Actionable.meアカウントが必要です。 |
| Braze REST API キー | 次のセクションに記載されている権限を持つ Braze REST API キー。<br><br> これは Braze ダッシュボードの **\[設定] > \[**API キー**]** から作成できます。 |
| Braze REST エンドポイント | [あなたの REST エンドポイント URL][1]。エンドポイントは、インスタンスの Braze URL によって異なります。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

Brazeとactionable.meを統合するには、actionable.meプラットフォームを設定する必要があります。また、BrazeでBrazeのAPI キーを作成し、actionable.meダッシュボードで設定する必要があります。

### ステップ1:Braze API キーを作成する

Braze で、\[**設定] > \[**API キー**]** に移動します。\[**新しい API キーを作成**] を選択し、次の権限が追加されていることを確認します。

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
[古いナビゲーションを使用している場合は]({{site.baseurl}}/navigation)、**開発者コンソール** > API **設定から API** キーを作成できます。
{% endalert %}

### ステップ2:actionable.meチームに情報を提供してください

統合を完了するには、REST API キー[とRESTエンドポイントのURLをactionable.me運用チームに提供する必要があります][1]。その後、actionable.meが接続を確立し、セットアップが完了した後に連絡を取り、インサイトの共有を開始できるよう連絡します。

![actionable.me運用チームが設定するactionable.meの「プラットフォーム追加」ページ。][5]

## トラブルシューティング

[その他のサポートについては、actionable.meまたはMassive Rocketチームにお問い合わせください。info@massiverocket.com][3]

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://actionable.me
[3]: mailto:info@massiverocket.com
[4]: {% image_buster /assets/img/actionableme/image1.png %}
[5]: {% image_buster /assets/img/actionableme/image2.png %}
