---
nav_title: Eppo
article_title: Eppo
description: "EppoとBrazeの統合方法を学習する。"
alias: /partners/eppo/
page_type: partner
search_tag: Partner
---

# Eppo

> [Eppo](https://www.geteppo.com/) は、チームが A/B テストを実行し、大規模に機能を管理し、データ駆動型の意思決定に AI 駆動のインサイトを活用できるようにする次世代の実験プラットフォームです。

*この統合は、Eppo によって管理されます。*

Braze と Eppoの統合により、BrazeでABテストを設定し、Eppoで結果を分析することで、インサイトを明らかにし、メッセージパフォーマンスを収益やリテンションなどの長期的なビジネス指標に結びつけることができる。

## 前提条件

| 必要条件                        | 説明                                                                         |
|------------------------------------|-------------------------------------------------------------------------------------|
| Eppo アカウント                       | このパートナーシップを利用するには、Eppo アカウントが必要である。                   |
| Currents または Snowflake のデータ共有 | Eppoが実験データを解析するには、CurrentsまたはSnowflakeデータ共有が必要である。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ 1: Braze で Currents または Snowflake データ共有を設定する

Eppo はデータウェアハウスで直接実験を分析します。統合を有効にするには、Braze メッセージエンゲージメントのデータが、Eppo に接続されたデータウェアハウスで利用可能でなければなりません。Currents を使用して Braze からキャンペーンデータをエクスポートしたり、[Snowflake データ共有]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake)を使用して Snowflake インスタンスで Braze データにアクセスしたりできます。

### ステップ2: Brazeキャンペーンまたはキャンバスで実験を設定する。

キャンペーンやキャンバスでは、ネイティブの AB テスト機能を使うことができます。詳しくは、[多変量テストと AB テスト](https://www.braze.com/docs/user_guide/engagement_tools/testing/multivariant_testing#what-are-multivariate-and-ab-testing)を参照してください。

### ステップ 3: Eppo を設定して Braze の実験を測定する

EppoでBrazeデータを使用して実験を実行するには、Brazeからエクスポートされたユーザーレベルのメッセージイベントデータに基づいて、データウェアハウスに[割り当てテーブルを](https://docs.geteppo.com/data-management/definitions/assignment-sql/)作成する。キャンバス実験とキャンペーン実験は、異なるメタデータに依存しているため、別々のテーブルを使用することを推奨します。

{% tabs local %}
{% tab キャンバス実験 %}
キャンバスの実験では、割り当ては以下のいずれかで作成できます。

- キャンバスエントリーレベル (`users.canvas.Entry`)
- キャンバス実験ステップ (`users.canvas.experimentstep.SplitEntry`)

このようなケースでは、`canvas_name`、`experiment_step_id`、`canvas_variation_name`、`experiment_split_id` のようなフィールドが、実験名とバリエーションを定義するために使用されます。

{% endtab %}

{% tab キャンペーン実験 %}
キャンペーン実験では、送信イベント (プッシュ、メール、SMS など) を使って、ユーザーがいつ実験に参加したかを判断します。`campaign_name`、`message_variation_name`、および `time` は、割り当てテーブルに入力するために使用されます。

{% endtab %}
{% endtabs %}

メッセージ固有のメトリクス (クリックや開封など) をトラッキングするには、ユーザー ID とキャンペーン名またはキャンバス名を結合した `combined_id` を作成することによって**セカンダリエンティティ**を含めます。この `combined_id` は、ファクトテーブルでも使用され、メトリクスを正しい実験とバリエーションに合わせます。

Eppo は、これらの割り当てとファクトテーブルを使用して結果を分析します。Eppo で**プロトコル**を設定して、将来の実験の設定を標準化することをお勧めします。詳細については、[Eppo のドキュメント](https://docs.geteppo.com/guides/marketing/integrating-with-braze/)を参照してください。

## サポート

Braze Currents、Snowflakeデータ共有、多変量キャンペーンの設定に関するご質問は、Brazeカスタマーサクセスマネージャーまでお問い合わせください。

Braze実験を測定するためのEppoの設定に関するサポートについては、Eppoのサポートチームに問い合わせること。
