---
nav_title: 8月
page_order: 6
noindex: true
page_type: update
description: "この記事には2018年8月のリリースノートが含まれている。"
---
# 2018年8月

## iOS 12の通知グループ

最近リリースされたiOS 12では、アプリケーションのグループ化通知（Androidの通知チャネルに似ている）がサポートされている。[Brazeでは、メッセージ作成画面を使って、このグループ化機能をiOSで利用することができる。]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#notification-groups)

## プッシュストーリーのトリガー

プッシュストーリースライドの特定のページクリックに基づいてユーザー群をリターゲティングすることができるようになった。**Interacted with Campaignの**追加フィルターを使用する。

## 匿名ユーザーからのS3およびAzureデータイベント

Amazon S3とMicrosoft Azureにデータをエクスポートする顧客は、匿名ユーザーのイベントを含めることができるようになった。この機能は、新規に作成されたすべての統合ではデフォルトでオンになるが、既存のすべての統合ではオフのままである。ご質問がある場合は、アカウントマネージャーに連絡するか、[サポートチケットを][support]開封する。

## Mixpanel Cohortsの統合

BrazeとMixpanelの両方の顧客が、[Mixpanelコホートを]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/#mixpanel-cohort-import)統合し、[セグメントフィルターとしてBrazeに送信]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/#mixpanel-cohort-import)できるようになった。一度だけ手動でエクスポートするか、2時間ごとにダイナミックなエクスポートを設定することができる。更新されたユーザーはそれぞれデータポイントとしてカウントされるが、Mixpanelは最後の同期以降の変更のみを送信する。

[support]: {{site.baseurl}}/braze_support/