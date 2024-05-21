---
nav_title: 8 月
page_order: 5
noindex: true
page_type: update
description: "この記事には、2017 年 8 月のリリース ノートが含まれています。"
---

# 2017年8月号

## プッシュアクションボタンに更新

[プッシュ アクション ボタン][70]のサポートを REST API メッセージング エンドポイントに追加しました。

## Liquidテンプレートへの更新

以下に基づいて [メッセージをパーソナライズ][69] できるようになりました。
\- 送信先のデバイス
\- デバイスID、
-キャリア
\- IDFAの、
-モデル
\- OS、および
-プラットホーム

## API トリガー Canvas

キャンペーンの既存のエンドポイントと一致するAPIエンドポイント(送信、スケジュール、更新、削除)を介して [キャンバス][68] をトリガーできるようになり、マーケティングをさらに自動化および最適化できるようになりました。

## Web プッシュ・アクション・ボタン

Chrome 版ウェブ SDK にプッシュ アクション ボタンのサポートが追加され、ユーザーが状況に応じた選択肢を提供して忙しい生活を簡素化することで、エンゲージメントを高めることができます。[プッシュ通知のベストプラクティス][66]をご確認ください。

## 新しい API エンドポイント

新しい API エンドポイント、 /email/hard_bounces, that lets you pull hard bounces by email address or in a given date range, and /messages/scheduled_broadcasts, that lets you pull the next time that scheduled campaigns and scheduled-entry Canvases will begin. These new endpoints allow you for further customization and optimization of your campaigns. Learn more about our [API エンドポイントを公開しました][65]。

## ジオフェンス

ジオフェンスという新機能が追加され、顧客が定義された地域に出入りしたときにリアルタイムでメッセージをトリガーし、顧客とのパーソナライズされた関連性の高いコミュニケーションを可能にします。[詳しくは、ロケーションマーケティング][64]についての記事をご覧ください。

## メールエディターの更新

新しいメールエディターに動的オートコンプリート機能が追加され、Liquidを使用する際に顧客の実際のカスタム属性やイベントをオートコンプリートできるようになり、作業が楽になりました。[詳しくは、Academy][63] のメールに関するおすすめの方法をご覧ください。

## 日付フィルターの更新

「なし」の日付フィルターを追加したので、メッセージを受け取ったり、やり取りしたりしたことのない顧客をターゲットにすることができ、クリーンな顧客リストを作成し、メールの配信可能性を確保できます。[詳しくは、フィルター][62]についての記事をご覧ください。

## キャンバスに更新

各キャンバスのバリエーションの上部にパーセンテージを追加し、どのバリエーションのパフォーマンスが優れているかが一目でわかるようにしました。[詳しくは、Canvas][61] についての記事をご覧ください。

## インテリジェント選択機能付きキャンバス

Canvas にインテリジェント選択機能が追加され、より効率的に Canvas をテストできるようになりました。[Intelligence Suite][60]の詳細をご覧ください。

## メールの表示名を更新する

メールの表示名に特殊な UTF-8 文字のサポートが追加されたため、顧客向けにさらにパーソナライズされたメールを作成できます。[詳しくは、メールのおすすめの方法][67]をご覧ください。

## エンゲージメントレポートのCSV集計

選択したキャンペーンやキャンバスの数に関係なく、すべてのキャンペーンとすべてのキャンバスの統合データを 2 つの別々のファイルで受信できるようになり、必要なときに必要なすべてのデータを取得できるようになりました。[エンゲージメントレポート][59]の詳細をご覧ください。

> [2017 年 9 月のリリース ノート]({{site.baseurl}}/help/release_notes/2017/september/)に記載されているように、特定の期間のデータを集計したり、エクスポートを定期的に実行するようにスケジュールしたりできるようになりました。


[59]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/
[60]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/
[61]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/
[62]: {{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#segmentation-filters
[63]: {{site.baseurl}}/help/troubleshooting_guide/troubleshooting_guide/#email
[64]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/locations_and_geofences/
[65]: {{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api
[66]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
[67]: {{site.baseurl}}/help/troubleshooting_guide/troubleshooting_guide/#email
[68]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/
[69]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/personalized_messaging/#personalized-messaging
[70]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_action_buttons/#how-to-use-action-buttons
[98]:{{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#authentication-rules
