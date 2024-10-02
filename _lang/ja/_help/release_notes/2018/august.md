---
nav_title: 8月
page_order: 6
noindex: true
page_type: update
description: "この記事は、2018年8月のリリースノートを含んでいます。"
---
# 2018年8月

## iOS 12 通知群

最近のiOS 12 リリースでは、アプリ版の通知のグループ化(Android 通知チャンネルに似ています) がサポートされています。[Braze では、メッセージ作成画面を使用してこのグループ化機能をiOS で利用できます。]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#notification-groups)

## プッシュストーリートリガー中

プッシュストーリースライドのページクリックに基づいてs をリターゲティングする ユーザーできるようになりました。**Campaign**とのインタラクションには、追加のフィルターを使用します。

## 匿名ユーザーからのS3およびAzureデータイベント

Amazon S3 およびMicrosoft Azure にデータをエクスポートするお客様は、匿名ユーザーからのイベントを含めることができます。この機能は、新しく作成されたすべての統合で有効にデフォルトされますが、既存のすべての統合で無効のままになります。ご不明な点がございましたら、アカウントマネージャーまでお問い合わせいただくか、[サポートチケット][support]を開封してください。

## Mixpanelコホート統合

Braze とMixpanel の両方の顧客が統合できるようになり、[ Mixpanel コホートをSegment フィルター s]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/#mixpanel-cohort-import) としてBraze に送信します。1 回限りの手動エクスポートを設定するか、2 時間ごとにダイナミックなエクスポートを設定できます。それぞれの更新 d ユーザーはデータポイントとしてカウントされますが、ミックスパネルは前回の同期以降の変更のみを送信します。

[support]: {{site.baseurl}}/braze_support/