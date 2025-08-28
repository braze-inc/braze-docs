---
nav_title: 8月
page_order: 5
noindex: true
page_type: update
description: "この記事には2017年8月のリリースノートが含まれている。"
---

# 2017年8月

## プッシュアクションボタンsへのアップデート

REST API メッセージングエンドポイントに[プッシュアクションボタン]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_action_buttons/#how-to-use-action-buttons)のサポートを追加しました。

## リキッドテンプレーティングへのアップデート

[メッセージのパーソナライズが]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)可能になった：
- 送信先のデバイス、
- デバイス ID、
- 通信事業者、
- IDFA、
- モデル、
- OS、
- プラットフォーム

## API トリガーキャンバス

キャンペーン用の既存のエンドポイントと一致するAPIエンドポイント（送信、スケジュール、更新、削除）を介して[キャンバスを]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)トリガーできるようになったので、マーケティングの自動化と最適化をさらに進めることができる。

## Web プッシュアクションボタンs

Chrome用のウェブSDKにプッシュアクションボタンのサポートが追加され、ユーザーの多忙な生活を簡素化するコンテキストに応じた選択肢を与えることで、エンゲージメントを高めることができる。[プッシュ通知のベストプラクティス]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/)を確認してください。

## 新しいAPIエンドポイント

新しい API エンドポイント /email/hard_bounces を公開しました。これにより、メールアドレスまたは特定の日付範囲でハードバウンスを取得できます。また、/messages/scheduled_broadcasts を使用すると、スケジュールされたキャンペーンとスケジュールされたエントリキャンバスが次に開始される時刻を取得できます。これらの新しいエンドポイントは、キャンペーンのさらなるカスタマイズと最適化を可能にする。詳細については、[API エンドポイントs]({{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api) を参照してください。

## ジオフェンス

ジオフェンスという新しい機能を追加しました。これにより、顧客が定義済みの地理的エリアに出入りするときにリアルタイムでメッセージをトリガーし、顧客とのパーソナライズされた関連性の高いコミュニケーションが可能になります。[ロケーション・マーケティングについて]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/locations_and_geofences/)もっと知る。

## Eメールエディターの更新

新しいメールエディタにダイナミックオートコンプリート機能を追加しました。これにより、Liquid を使用する際に顧客の実際のカスタム属性とイベントをオートコンプリートできるようになり、作業が楽になります。[メールのベストプラクティス]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices)について詳しく説明します。

## 日付フィルターの更新

「まったく該当しない」日付フィルターを追加しました。これにより、メッセージを一度も受信または操作したことのない顧客をターゲットにでき、クリーンな顧客リストを保持して、メールの配信到達性を確保できます。フィルターについて[詳しく知る]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#segmentation-filters)。

## キャンバスへの更新

各キャンバスのバリアントの上部にパーセンテージが追加され、どのバリアントがより良いパフォーマンスをしているかが一目でわかるようになった。キャンバスについて詳しくは、[こちら]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)をご覧ください。

## インテリジェントセレクションを使用したキャンバス

キャンバスにインテリジェントセレクションが追加され、キャンバスをより効率的にテストできるようになりました。詳細については、[Intelligence Suite]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) を参照してください。

## メールディスプレイの名前へのアップデート

電子メールの表示名に特殊なUTF-8文字をサポートするようになったので、顧客によりパーソナライズされた電子メールを作成できるようになった。[メールのベストプラクティス]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices)について詳しく説明します。

## エンゲージメント・レポートCSV集計

選択されているキャンペーンやキャンバスの数に関係なく、すべてのキャンペーンとすべてのキャンバスの統合データを2つの別々のファイルで受け取ることができるため、必要なときに必要なすべてのデータを入手できるようになりました。[エンゲージメント・レポートの]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/)詳細はこちら。

> [2017年9月のリリースノート]({{site.baseurl}}/help/release_notes/2017/september/)に記載されているように、特定の期間のデータを集計したり、定期的なエクスポートの実行をスケジュールしたりできるようになりました。


