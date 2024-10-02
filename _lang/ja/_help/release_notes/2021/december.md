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
2. `custom_events` 、`purchases` 、`campaigns_received` 、`canvases_received` のフィールドには、過去90日間のデータのみが含まれる。

## カレントのメッセージ・エンゲージメント・イベントの新しいプロパティ

一部の[メッセージ・エンゲージメント・イベントに]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/)新しいプロパティが追加された。このアップデートは、以下のCurrentsメッセージエンゲージメントイベントと、それらを使用するすべてのパートナーに適用される：

- `LINK_ID`,`LINK_ALIAS` を加える：
  - Eメールクリック（すべての宛先）
- `USER_AGENT` ：
  - Eメールオープン
  - Eメールクリック
  - 迷惑メールとしてマークする
- `MACHINE_OPEN` ：
  - Eメールオープン

## 新リキッド名入れタグ

以下のリキッドタグで、フォアグラウンドプッシュを有効にしているユーザーをターゲットにできるようになった：

{% raw %}
- `{{most_recently_used_device.${foreground_push_enabled}}}`
- `{{targeted_device.${foreground_push_enabled}}}`
{% endraw %}

詳しくは、[サポートされるパーソナライズタグを]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)参照のこと。

## ウェブフックについて

Webhookは強力で柔軟なツールだが、少しわかりにくいかもしれない。Webhookとは何なのか、Brazeでどのように使えるのか気になる方は、[Webhookについての]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/)新しい記事をチェックしよう。

## Amazon Personalize

Amazon Personalizeは、Amazonの機械学習によるレコメンデーションシステムを一日中利用できるようなものだ。20年以上にわたるレコメンデーションの経験に基づき、Amazon Personalizeは、リアルタイムでパーソナライズされた商品やコンテンツのレコメンデーション、およびターゲットを絞ったマーケティングプロモーションを可能にすることで、顧客エンゲージメントを向上させることができる。 

さらに詳しく知りたい方は、[Amazon Personalizeの]({{site.baseurl}}/partners/message_personalization/dynamic_content/amazon_personalize/amazon_personalize/)新しい記事を参照し、Amazon Personalizeが提供するユースケース、Amazon Personalizeが扱うデータ、サービスの設定方法、Brazeとの統合方法について理解しよう。

## 新しいブレイズ・パートナーシップ

### Yotpo - Eコマース

[Yotpoと]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/yotpo/)Brazeの統合により、Braze内のEメールやその他のコミュニケーションチャンネルで、製品に関する星評価、トップレビュー、視覚的なユーザー生成コンテンツを動的に取得し、表示することができる。また、顧客レベルのロイヤルティデータをEメールやその他のコミュニケーション手段に含めることで、よりパーソナライズされたインタラクションを実現し、売上とロイヤルティを高めることができる。

### Zeotap - 顧客データプラットフォーム

[Zeotapと]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/zeotap/)Brazeの統合により、Zeotap顧客セグメントを同期してZeotapユーザーデータをBrazeユーザーアカウントにマッピングすることで、キャンペーンの規模とリーチを拡大することができる。そして、このデータに基づいて行動し、ユーザーにパーソナライズされたターゲット体験を提供することができる。