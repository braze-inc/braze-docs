---
nav_title: 8月
page_order: 5
noindex: true
page_type: update
description: "この記事には2017年8月のリリースノートが含まれている。"
---

# 2017年8月

## プッシュアクションボタンsへのアップデート

REST API メッセージングエンドポイントに[プッシュアクションボタン][70]のサポートを追加しました。

## リキッドテンプレーティングへのアップデート

[メッセージのパーソナライズが][69]可能になった：
- 送信先のデバイス、
- デバイス ID、
- 通信事業者、
- IDFA、
- モデル、
- OS、
- プラットフォーム

## API トリガーキャンバス

キャンペーン用の既存のエンドポイントと一致するAPIエンドポイント（送信、スケジュール、更新、削除）を介して[キャンバスを][68]トリガーできるようになったので、マーケティングの自動化と最適化をさらに進めることができる。

## Web プッシュアクションボタンs

Chrome用のウェブSDKにプッシュアクションボタンのサポートが追加され、ユーザーの多忙な生活を簡素化するコンテキストに応じた選択肢を与えることで、エンゲージメントを高めることができる。[プッシュ通知のベストプラクティス][66]を確認してください。

## 新しいAPIエンドポイント

新しい API エンドポイント /email/hard_bounces を公開しました。これにより、メールアドレスまたは特定の日付範囲でハードバウンスを取得できます。また、/messages/scheduled_broadcasts を使用すると、スケジュールされたキャンペーンとスケジュールされたエントリキャンバスが次に開始される時刻を取得できます。これらの新しいエンドポイントは、キャンペーンのさらなるカスタマイズと最適化を可能にする。詳細については、[API エンドポイントs][65] を参照してください。

## ジオフェンス

ジオフェンスという新しい機能を追加しました。これにより、顧客が定義済みの地理的エリアに出入りするときにリアルタイムでメッセージをトリガーし、顧客とのパーソナライズされた関連性の高いコミュニケーションが可能になります。[ロケーション・マーケティングについて][64]もっと知る。

## Eメールエディターの更新

新しいメールエディタにダイナミックオートコンプリート機能を追加しました。これにより、Liquid を使用する際に顧客の実際のカスタム属性とイベントをオートコンプリートできるようになり、作業が楽になります。メール のベストプラクティスの詳細については、[Academy][63] を参照してください。

## 日付フィルターの更新

「まったく該当しない」日付フィルターを追加しました。これにより、メッセージを一度も受信または操作したことのない顧客をターゲットにでき、クリーンな顧客リストを保持して、メールの配信到達性を確保できます。フィルターについて[詳しく知る][62]。

## キャンバスへの更新

各キャンバスのバリアントの上部にパーセンテージが追加され、どのバリアントがより良いパフォーマンスをしているかが一目でわかるようになった。キャンバスについて詳しくは、[こちら][61]をご覧ください。

## インテリジェントセレクションを使用したキャンバス

キャンバスにインテリジェントセレクションが追加され、キャンバスをより効率的にテストできるようになりました。詳細については、[Intelligence Suite][60] を参照してください。

## メールディスプレイの名前へのアップデート

電子メールの表示名に特殊なUTF-8文字をサポートするようになったので、顧客によりパーソナライズされた電子メールを作成できるようになった。[メールのベストプラクティス][67]について詳しく説明します。

## エンゲージメント・レポートCSV集計

選択されているキャンペーンやキャンバスの数に関係なく、すべてのキャンペーンとすべてのキャンバスの統合データを2つの別々のファイルで受け取ることができるため、必要なときに必要なすべてのデータを入手できるようになりました。[エンゲージメント・レポートの][59]詳細はこちら。

> [2017年9月のリリースノート]({{site.baseurl}}/help/release_notes/2017/september/)に記載されているように、特定の期間のデータを集計したり、定期的なエクスポートの実行をスケジュールしたりできるようになりました。


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
