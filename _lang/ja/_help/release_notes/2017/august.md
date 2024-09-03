---
nav_title: 8月
page_order: 5
noindex: true
page_type: update
description: "この記事には2017年8月のリリースノートが含まれている。"
---

# 2017年8月

## アクションボタンを押すためのアップデート

REST APIメッセージングエンドポイントに[プッシュアクションボタンの][70]サポートを追加した。

## リキッドテンプレートの更新

[メッセージのパーソナライズが][69]可能になった：
- 送信先のデバイス、
- デバイスID、
- キャリアだ、
- IDFAである、
- モデルだ、
- OS、そして
- プラットフォーム

## APIトリガー・キャンバス

キャンペーン用の既存のエンドポイントと一致するAPIエンドポイント（送信、スケジュール、更新、削除）を介して[キャンバスを][68]トリガーできるようになったので、マーケティングの自動化と最適化をさらに進めることができる。

## ウェブ・プッシュ・アクション・ボタン

Chrome用のウェブSDKにプッシュアクションボタンのサポートが追加され、ユーザーの多忙な生活を簡素化するコンテキストに応じた選択肢を与えることで、エンゲージメントを高めることができる。[プッシュ通知のベストプラクティスを][66]チェックしよう。

## 新しいAPIエンドポイント

新しいAPIエンドポイントを公開した。/email/hard_bouncesは、メールアドレス別または指定された日付範囲のハードバウンスを引き出すことができ、/messages/scheduled_broadcastsは、スケジュールされたキャンペーンとスケジュールされたエントリーのキャンバスが開始される次の時間を引き出すことができる。これらの新しいエンドポイントは、キャンペーンのさらなるカスタマイズと最適化を可能にする。[APIエンドポイントについて][65]もっと知る。

## ジオフェンス

ジオフェンスという新機能が追加され、顧客が定義された地理的エリアに出入りしたときにリアルタイムでメッセージをトリガーすることができるようになり、顧客とのパーソナライズされた適切なコミュニケーションが可能になった。[ロケーション・マーケティングについて][64]もっと知る。

## Eメールエディターの更新

新しいメールエディタにダイナミックオートコンプリートを追加した。[アカデミーの][63]Eメールのベストプラクティスについてもっと知る。

## 日付フィルターの更新

一度もメッセージを受信したことがない、または一度もやりとりしたことがない顧客をターゲットにできるよう、「一度も」日付フィルタを追加。[フィルターについて][62]もっと知る。

## キャンバスへの更新

各キャンバスのバリアントの上部にパーセンテージが追加され、どのバリアントがより良いパフォーマンスをしているかが一目でわかるようになった。[キャンバスについて][61]もっと知る。

## インテリジェント・セレクションのキャンバス

キャンバスにはインテリジェント・セレクションが追加され、より効率的にキャンバスをテストできるようになった。[インテリジェンス・スイートの][60]詳細はこちら。

## 電子メールの表示名を更新

電子メールの表示名に特殊なUTF-8文字をサポートするようになったので、顧客によりパーソナライズされた電子メールを作成できるようになった。[Eメールのベストプラクティスについて][67]もっと知る。

## エンゲージメント・レポートCSV集計

キャンペーンやキャンバスの数に関係なく、すべてのキャンペーンとキャンバスの統合データを2つのファイルに分けて受け取ることができる。[エンゲージメント・レポートの][59]詳細はこちら。

> [2017年9月のリリースノートで]({{site.baseurl}}/help/release_notes/2017/september/)述べたように、特定の期間のデータを集計したり、定期的にエクスポートを実行するようにスケジュールしたりできるようになった。


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
