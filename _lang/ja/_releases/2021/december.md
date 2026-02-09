---
nav_title: 12月
page_order: 0
noindex: true
page_type: update
description: "この記事には、2021年12月のリリースノートが含まれている。"
alias: "/help/release_notes/2022/january/"
---
# 2021年12月

## セグメント・エンドポイントごとにユーザーをエクスポートするように更新

2021年12月より、[セグメント別ユーザー・エクスポート・エンドポイントについて]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)、以下の変更が適用される：

1. このAPIリクエストの`fields_to_export` フィールドは必須となる。すべてのフィールドをデフォルトにするオプションは削除される。
2. `custom_events`、`purchases`、`campaigns_received`、`canvases_received` のフィールドには、過去90日間のデータのみが含まれます。

## カレントのメッセージ・エンゲージメント・イベントの新しいプロパティ

一部の[メッセージ・エンゲージメント・イベントに]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/)新しいプロパティが追加された。この更新は、以下の Currents メッセージエンゲージメントイベントと、それらを使用するすべてのパートナーに適用されます。

- `LINK_ID`、`LINK_ALIAS` を以下に追加します。
  - メールクリック(すべての送信先)
- `USER_AGENT` を以下に追加します。
  - メール開封
  - メールのクリック
  - 迷惑メールとしてマークする
- `MACHINE_OPEN` を以下に追加します。
  - メール開封

## 新流動パーソナライゼーション タグ

次の Liquid タグを使用して、デバイスでフォアグラウンドプッシュが有効になっているユーザーへのターゲット設定をサポートします。

{% raw %}
- `{{most_recently_used_device.${foreground_push_enabled}}}`
- `{{targeted_device.${foreground_push_enabled}}}`
{% endraw %}

詳細については、[サポートされるパーソナライゼーション タグs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)を参照してください。

## ウェブフックについて

Webhookは強力で柔軟なツールだが、少しわかりにくいかもしれない。どのようなwebhookがあり、どのようにBrazeでそれらを使用できるか気になる場合は、[webhookについて]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/)の新しい記事をご覧ください。

## Amazon Personalize

Amazon Personalizeは、Amazonの機械学習によるレコメンデーションシステムを一日中利用できるようなものだ。20年以上にわたるレコメンデーションの経験に基づき、Amazon Personalizeは、リアルタイムでパーソナライズされた商品やコンテンツのレコメンデーション、およびターゲットを絞ったマーケティングプロモーションを可能にすることで、顧客エンゲージメントを向上させることができる。 

さらに詳しく知りたい方は、[Amazon Personalizeの]({{site.baseurl}}/partners/message_personalization/dynamic_content/personalized_recommendations/amazon_personalize)新しい記事を参照し、Amazon Personalizeが提供するユースケース、Amazon Personalizeが扱うデータ、サービスの設定方法、Brazeとの統合方法について理解しよう。

## 新しいBrazeのパートナーシップ

### Yotpo - eコマース

[Yotpo]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/yotpo/) と Braze の統合により、Braze 内のメールや他の通信チャネル内で、製品の星の評価、トップレビュー、視覚的なユーザー生成コンテンツを動的に取得して表示できます。また、顧客レベルのロイヤルティデータをメールやその他のコミュニケーション手段に組み込むこで、よりパーソナライズされたインタラクションを実現し、売上とロイヤルティを高めることができます。

### Zeotap - 顧客データプラットフォーム

[Zeotap]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/zeotap/) と Braze の統合により、Zeotap の顧客セグメントを同期して Zeotap のユーザーデータを Braze のユーザーアカウントにマッピングすることで、キャンペーンの規模と範囲を拡張できます。そして、このデータに基づいて行動し、ユーザーにパーソナライズされたターゲット体験を提供することができる。