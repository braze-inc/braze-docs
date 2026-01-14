---
nav_title: API利用アラート
article_title: API 使用状況アラート
description: "この記事では、予期せぬトラフィックをプロアクティブに検出できるAPI使用アラートの概要を説明する。"
page_order: 3.6
---

# API利用アラート

> API使用アラートは、API使用状況の重要な可視性を提供し、予期せぬトラフィックをプロアクティブに検出することを可能にする。これらのアラートを設定してキーAPIリクエスト量を追跡することで、リアルタイム通知を受け取り、マーケティングキャンペーンに影響が出る前に問題に対処することができる。

## API利用アラートについて

API使用アラートを使って、以下のカテゴリーのリクエスト量を監視することができる：

| APIカテゴリー | 詳細 |
|--------------|---------|
| REST APIエンドポイント | メッセージの送信、キャンペーンの作成、ユーザーのエクスポートなど、Brazeのバックエンドに対して行われたすべてのREST APIコールの使用状況をトラッキング追跡する。 |
| SDK APIリクエスト | アプリ内メッセージのトリガーやユーザーデータの同期など、クライアントアプリでBraze SDKから行われたAPIリクエストをトラッキング追跡。<br><br>_\*マンスリーアクティブユーザー - CY24-25を購入した顧客のみ利用可能。_ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## API使用アラートを作成する

API使用アラートを作成する：

1. **設定**＞**APIと識別子**＞**API使用アラートと**進み、新しいアラートを作成する。
2. アラートの名前を入力し、アラートさせたいREST APIエンドポイントとAPIキーを選択する。
3. 1つまたは複数のレスポンスコードを選択し、[アラートしきい値を](#api-usage-alert-thresholds)指定することで、アラート基準を定義する。
4. 終了したら、**イネーブルメントをオンに**切り替える。
    ![Track usersエンドポイントが1時間以内に100%増加した場合に通知を送信するAPI使用アラートの例。]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts1.png %})

## 警告のしきい値 {#api-usage-alert-thresholds}

アラート基準を定義する際、以下の閾値を調整することができる：

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
        アラートさせたい閾値ボリュームに至るまでの条件を定義する。以下がサポートされている：<br><br>
        <ul>
          <li><strong>増加</strong>または<strong>減少した</strong>：リクエストを前のタイムウィンドウと比較する。</li>
          <li><strong>パーセント増加</strong>または<strong>パーセント減少した</strong>：前回のタイムウィンドウに対するリクエストの変化率を比較する。</li>
          <li><strong>以上</strong>または<strong>以下</strong>である：時間ウィンドウ内のリクエストをカウントする。</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>しきい値量</td>
      <td>閾値条件と併用される。</td>
    </tr>
    <tr>
      <td>Within (範囲内)</td>
      <td>アラート評価の時間枠。</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## アラート通知の設定

メールアラート、Webhook アラート、またはその両方を設定できます。Webhookアラートは、Slackチャネルなどの外部プラットフォームにアラートを送信するようなユースケースで非常に役立つ。例として、Slackとのアラート統合に関する[ドキュメントで](https://www.braze.com/docs/user_guide/administrative/app_settings/company_settings/notification_preferences#slack-incoming-webhook-integration)、通知設定を参照できる。

![アラートの基準に達すると、選択したメールにメールが送信される。]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts2.png %})

### サンプルペイロード {#payload}

以下は、API Usage Alert Webhookのボディのペイロードのサンプルである。

```json
{
  "data": {
    "alert_name": "My First API Usage Alert",
    "alert_type": "API Usage Alert",
    "alert_criteria": [
    	"response_codes": ["201", "202", "203"],
    	"threshold_condition: "Increased by %",
    	"threshold_volume": 50,
    	"within": "1 day"
    	],
    "timeframe_start": 2025-03-20T15:35:00Z,
    "timeframe_end": 2025-03-20T16:35:00Z,
    "volume": 1500,
    "previous_timeframe_start": 2025-03-20T14:35:00Z,
    "previous_timeframe_end": 2025-03-20T15:35:00Z,
    "previous_volume": 1000
  },
  "text": "Your My First API Usage Alert alert has triggered. You can view your alert and usage here: <link>. Note that this alert will reset in 1 day, as each alert will only send one notification per 8 hours."
}
```

### アラート例

以下のシナリオで通知されるAPI使用アラート設定の方法をいくつか紹介する。

{% tabs local %}
{% tab api health %}
アラートを設定して、APIの全般的な健全性を監視することができる。例えば、APIエラーが前の時間から20％など急激に増加した場合に、このようなアラートを設定することができる。

| エンドポイント | APIキー | 応答コード | しきい値条件 | しきい値量 | Within (範囲内) |
| --- | --- | --- | --- | --- | --- |
| すべてのエンドポイント | すべての API キー | `4XX` と `5XX` | 10%増 | 10 | 1 時間 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab endpoint rate limit %}
ワークスペースが`/users/track` エンドポイントのレート制限に達するとアラートが表示される。この設定は、他のBrazeエンドポイントにも適用できる。

| エンドポイント | APIキー | 応答コード | しきい値条件 | しきい値量 | Within (範囲内) |
| --- | --- | --- | --- | --- | --- |
| `/users/track` | すべての API キー | `429` | 以上 | 100 | 1 時間 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab API-triggered campaigns %}
このアラート設定は、APIトリガーキャンペーンとキャンバスにエラーが発生したときに通知する。

| エンドポイント | APIキー | 応答コード | しきい値条件 | しきい値量 | Within (範囲内) |
| --- | --- | --- | --- | --- | --- |
| {::nomarkdown}<ul><li><code>/campaigns/trigger/send</code></li><li><code>/canvas/trigger/send</code></li><li><code>/messages/send</code></li></ul>{:/} | すべての API キー | `4XX` と `5XX` | 以上 | 1 | 1 時間 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab partner integrations %}
パートナー連携がBrazeへのデータ送信を停止した場合にアラートを出すには、以下のアラート設定を使用する。

| エンドポイント | APIキー | 応答コード | しきい値条件 | しきい値量 | Within (範囲内) |
| --- | --- | --- | --- | --- | --- |
| すべてのエンドポイント | パートナー連携に使用するAPIキー | すべての応答コード | 以下 | 0 | 1 日 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}
{% endtabs %}

## 考慮事項

- 各アクティブアラートは、8時間に一度だけメールまたはWebhook通知を送信する。これは、1つのアラートからの通知が多すぎるのを防ぐためである。アラートの通知が早すぎる場合は、ユースケースに合うようにアラート基準を編集することを検討する。
- ワークスペースごとに最大10個のアラートを設定できる。
