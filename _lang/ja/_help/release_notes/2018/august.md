---
nav_title: 8月
page_order: 6
noindex: true
page_type: update
description: "この記事には、2018 年 8 月のリリースノートが含まれています。"
---
# 2018 年 8 月

## iOS 12 通知グループ

最近のiOS 12リリースでは、アプリケーションの通知のグループ化（Android通知チャネルと同様）がサポートされています。[Brazeでは、メッセージコンポーザーを使用してiOSでこのグループ化機能を利用できます。]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#notification-groups)

## プッシュストーリーのトリガー

Push Story スライドでの特定のページクリックに基づいてユーザーをリターゲティングできるようになりました。「**インタラクト対象キャンペーン**」に追加のフィルターを使用してください。

## 匿名ユーザーからの S3 および Azure データイベント

Amazon S3 と Microsoft Azure にデータをエクスポートするお客様は、匿名ユーザーからのイベントを含めることができるようになりました。この機能は、新しく作成されたすべてのインテグレーションでデフォルトでオンになりますが、既存のすべてのインテグレーションではオフのままになります。質問がある場合は、アカウントマネージャーに連絡するか、[サポートチケットを開いてください][support]。

## ミックスパネルコホート統合

BrazeとMixpanelの両方のお客様は、[Mixpanelコホートをセグメントフィルターとして統合してBrazeに送信できるようになりました]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/#mixpanel-cohort-import)。1 回限りの手動エクスポートまたは 2 時間ごとの動的エクスポートを設定できます。更新された各ユーザーはデータポイントとしてカウントされますが、Mixpanelは前回の同期以降の変更のみを送信します。

[support]: {{site.baseurl}}/braze_support/