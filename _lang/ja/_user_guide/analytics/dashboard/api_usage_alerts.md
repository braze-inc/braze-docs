---
nav_title: API使用アラート
article_title: API 使用状況アラート
description: "この記事では、予期しないトラフィックを事前に検出できるAPI使用量アラートの概要を説明する。"
page_order: 3.6
---

# API使用アラート

> API使用状況アラートは、APIの使用状況を可視化する重要な手段であり、予期せぬトラフィックを事前に検知することを可能にする。これらのアラートを設定して主要なAPIリクエスト量をトラッキングすれば、リアルタイムで通知を受け取ることができ、問題がマーケティングキャンペーンに影響を与える前に解決できる。

## API使用に関する警告について

API使用量アラートを使って、以下のカテゴリのリクエスト量を監視できる：

| APIカテゴリ | 詳細 |
|--------------|---------|
| REST API エンドポイント | Brazeのバックエンドに対して行われたすべてのREST API呼び出しの使用状況をトラッキングする。例えば、メッセージ送信、キャンペーン作成、ユーザーエクスポートなどである。 |
| SDK APIリクエスト | Braze SDKからクライアントアプリに対して行われるAPIリクエストを追跡する。例えば、アプリ内メッセージのトリガーやユーザーデータの同期などだ。<br><br>_\*「月間アクティブユーザー – CY 24-25」を購入した顧客のみが利用可能である。_ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## API使用量アラートの作成

API使用量アラートを作成するには：

1. **設定**＞**APIと識別子**＞**API使用量アラート**に移動し、新しいアラートを作成する。
2. アラートの名前を入力し、通知を受け取りたいREST APIエンドポイントとAPI キーを選択する。
3. アラート基準を定義するには、一つ以上の応答コードを選択し、[アラート閾](#api-usage-alert-thresholds)値を指定する。
4. 終わったら、**アラートを**イネーブルメントする。
    ![API使用アラートの例として、ユーザートラッキングエンドポイントが1時間以内に100％増加した場合に通知を送信するものがある。]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts1.png %})

## 警報閾値 {#api-usage-alert-thresholds}

アラート基準を定義する際には、以下のしきい値を調整できる：

<table>
  <thead>
    <tr>
      <th>フィールド</th>
      <th>説明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>しきい値条件</td>
      <td>
        通知を受けたいしきい値のボリュームに至るまでの条件を定義する。以下のものがサポートされている：<br><br>
        <ul>
          <li><strong>増加したか</strong>、<strong>減少したか</strong>：リクエストを前回の時間枠と比較する。</li>
          <li><strong>パーセントで増加したか</strong>、<strong>パーセントで減少したか</strong>：リクエストの割合の変化を、前回の時間枠と比較する。</li>
          <li><strong>以上</strong>、または<strong>以下</strong>：時間枠内のリクエストを数える。</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>しきい値量</td>
      <td>しきい値条件と組み合わせて使用される。</td>
    </tr>
    <tr>
      <td>Within (範囲内)</td>
      <td>アラート評価の時間枠。</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## アラート通知の設定

メールアラート、Webhook アラート、またはその両方を設定できます。Webhookアラートは、Slackチャネルなどの外部プラットフォームへアラートを送信するといったユースケースにおいて非常に有用である。例えば、通知設定に関するアラートとSlackの連携方法については、当社の[ドキュメントを](https://www.braze.com/docs/user_guide/administrative/app_settings/company_settings/notification_preferences#slack-incoming-webhook-integration)参照のこと。

![アラートの条件が満たされた場合、選択したメールアドレスにメールが送信される。]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts2.png %})

### サンプルペイロード {#payload}

以下は、API使用アラートWebhookの本文に対するサンプルペイロードである。

```json
{
  "data": {
    "alert_name": "My First API Usage Alert",
    "alert_type": "API Usage Alert",
    "alert_criteria": {
    	"response_codes": ["201", "202", "203"],
    	"threshold_condition": "Increased by %",
    	"threshold_volume": 50,
    	"within": "1 day"
    },
    "timeframe_start": "2025-03-20T15:35:00Z",
    "timeframe_end": "2025-03-20T16:35:00Z",
    "volume": 1500,
    "previous_timeframe_start": "2025-03-20T14:35:00Z",
    "previous_timeframe_end": "2025-03-20T15:35:00Z",
    "previous_volume": 1000
  },
  "text": "Your My First API Usage Alert alert has triggered. You can view your alert and usage here: <link>. Note that this alert will reset in 1 day, as each alert will only send one notification per 8 hours."
}
```

### 例のアラート

API使用量アラートの設定を以下のシナリオで通知されるように設定する方法をいくつか示す。

{% tabs local %}
{% tab api health %}
APIの全体的な状態を監視するためのアラートを設定できる。例えば、APIエラーが前時間比で20％増加するなど、急激に増加した際にこれらのアラートを設定できる。

| エンドポイント | APIキー | 応答コード | しきい値条件 | しきい値量 | Within (範囲内) |
| --- | --- | --- | --- | --- | --- |
| すべてのエンドポイント | すべての API キー | `4XX` と `5XX` | 10％増加した | 10 | 1 時間 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab endpoint rate limit %}
ワークスペースがエンド`/users/track`ポイントのレート制限に達した際に通知を受け取る。この設定は他のBrazeエンドポイントにも適用できる。

| エンドポイント | APIキー | 応答コード | しきい値条件 | しきい値量 | Within (範囲内) |
| --- | --- | --- | --- | --- | --- |
| `/users/track` | すべての API キー | `429` | 以上 | 100 | 1 時間 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab API-triggered campaigns %}
このアラート設定は、APIによってトリガーされたキャンペーンやキャンバスでエラーが発生した際に通知する。その中には優先度の高いものも含まれる。

| エンドポイント | APIキー | 応答コード | しきい値条件 | しきい値量 | Within (範囲内) |
| --- | --- | --- | --- | --- | --- |
| {::nomarkdown}<ul><li><code>/campaigns/trigger/send</code></li><li><code>/canvas/trigger/send</code></li><li><code>/messages/send</code></li></ul>{:/} | すべての API キー | `4XX` と `5XX` | 以上 | 1 | 1 時間 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab partner integrations %}
以下のアラート設定を使用すると、パートナー連携がBrazeへのデータ送信を停止した際に通知を受け取れる。

| エンドポイント | APIキー | 応答コード | しきい値条件 | しきい値量 | Within (範囲内) |
| --- | --- | --- | --- | --- | --- |
| すべてのエンドポイント | パートナー連携に使用するAPI キー | すべての応答コード | 以下 | 0 | 1 日 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}
{% endtabs %}

## 考慮事項

- 各アクティブなアラートは、8時間に1回だけメールまたはWebhook通知を送信する。これは単一のアラートから通知が過剰に発生するのを防ぐためだ。アラートが早すぎる場合は、ユースケースに合わせてアラートの条件を編集することを検討せよ。
- 各ワークスペースにつき最大10個のアラートを設定できる。
