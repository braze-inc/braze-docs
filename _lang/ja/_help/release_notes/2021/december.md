---
nav_title: 12 月
page_order: 0
noindex: true
page_type: update
description: "この記事には、2021 年 12 月のリリース ノートが含まれています。"
alias: "/help/release_notes/2022/january/"
---
# 2021年12月発売

## セグメントエンドポイント別にユーザーをエクスポートするための更新

2021 年 12 月以降、 [セグメント別にユーザーをエクスポート]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)エンドポイントで次の変更が有効になります。

1. この API 要求の `fields_to_export` フィールドは必須です。すべてのフィールドをデフォルトにするオプションは削除されます。
2. 、`purchases`、 `campaigns_received`の`canvases_received`フィールドに`custom_events`は、過去 90 日間のデータのみが含まれます。

## Currents メッセージ エンゲージメント イベントの新しいプロパティ

選択した [メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/)に新しいプロパティが追加されました。このアップデートは、以下の Currents メッセージ エンゲージメント イベントと、それらを使用するすべてのパートナーに適用されます。

- `LINK_ID`に を追加します`LINK_ALIAS`。
  - Eメールクリック(すべての宛先)
- 追加 `USER_AGENT` 先:
  - メール開封
  - メールクリック
  - メールをスパムとしてマーク
- 追加 `MACHINE_OPEN` 先:
  - メール開封

## 新しいLiquidパーソナライゼーションタグ

デバイスでフォアグラウンドプッシュを有効にしているユーザーのターゲット設定を、以下のLiquidタグでサポートするようになりました。

{% raw %}
- `{{most_recently_used_device.${foreground_push_enabled}}}`
- `{{targeted_device.${foreground_push_enabled}}}`
{% endraw %}

詳細については、「 [サポートされているパーソナライゼーションタグ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)」を参照してください。

## Webhook について

Webhook は強力で柔軟なツールですが、少し混乱を招く可能性があります。Webhookとは何か、Brazeでどのように使用できるのか疑問に思っている場合は、 [Webhookについて]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/)に関する新しい記事をご覧ください。

## Amazon パーソナライズ

Amazon Personalize は、独自の終日 Amazon 機械学習レコメンデーションシステムを持っているようなものです。Amazon Personalize は、20 年以上にわたるレコメンデーションの経験に基づいて、リアルタイムでパーソナライズされた製品とコンテンツのレコメンデーションとターゲットを絞ったマーケティングプロモーションを強化することで、顧客エンゲージメントを向上させることができます。 

詳細については、Amazon Personalize の新しい記事にアクセスして、Amazon [Personalize]({{site.baseurl}}/partners/message_personalization/dynamic_content/amazon_personalize/amazon_personalize/) が提供するユースケース、Amazon Personalize が扱うデータ、サービスの設定方法、Braze との統合方法を理解してください。

## Brazeの新しいパートナーシップ

### Yotpo – eコマース

[Yotpo]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/yotpo/)とBrazeの統合により、Braze内の電子メールやその他のコミュニケーションチャネル内の製品に、星評価、トップレビュー、視覚的なユーザー生成コンテンツを動的に取得して表示できます。また、顧客レベルのロイヤルティデータをメールやその他のコミュニケーション方法に含めて、よりパーソナライズされたインタラクションを作成し、売上とロイヤルティを高めることもできます。

### Zeotap – 顧客データプラットフォーム

[Zeotap]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/zeotap/) と Braze の統合により、Zeotap の顧客セグメントを同期して Zeotap のユーザーデータを Braze のユーザーアカウントにマッピングすることで、キャンペーンの規模とリーチを拡張できます。その後、このデータに基づいて行動し、パーソナライズされたターゲットエクスペリエンスをユーザーに提供できます。