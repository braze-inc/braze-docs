---
nav_title: 9月
page_order: 3
noindex: true
page_type: update
description: "この記事には2021年9月のリリースノートが含まれている。"
---

# 2021年9月

## iOS 15

### Apple Mail のプライバシー保護 

Apple のメールプライバシー保護 (MPP) は、9月中旬にリリースされた iOS 15、iPadOS 15、macOS Monterey、watchOS 8の Apple Mail アプリのユーザーに提供されるプライバシーアップデートです。MPP にオプトインしたユーザーの場合、メールはプロキシサーバーを使用してプリロードされ、画像がキャッシュされ、[開封の追跡]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#open-tracking-pixel)などの指標のトラッキングピクセルをトラッキングできなくなります。MPP およびメール配信可能性メトリクスに関する問題、およびこれらのメトリクスに基づいてトリガーされる既存のキャンペーンとキャンバスに関する問題については、[ドキュメント]({{site.baseurl}}/user_guide/message_building_by_channel/email/apple_mail/mpp/) を参照してください。

### プッシュ機能

iOS 15では新しい通知機能が導入され、ユーザーは1日を通して集中力を保ち、頻繁な作業の中断を避けることができます。[中断レベルや関連性スコアなど]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/)、これらの新機能のサポートを提供できることをうれしく思う。

## 連絡先カード

連絡先カードは、アドレス帳や連絡先一覧に簡単にインポートできるビジネス情報や連絡先情報を送信するための標準化されたファイル形式です。SMSやMMSメッセージに連絡先カードをアップロードして作成できるようになった。組み込みの連絡先カードジェネレーターで連絡先カードを構築する方法の詳細については、[こちら]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/contact_card/)のドキュメントを参照してください。

## デフォルト・コンテンツ・カードのカスタマイズ

`ABKContentCardsTableViewController` を拡張してすべての UI 要素とコンテンツカードの動作をカスタマイズすることで、独自のコンテンツカードインターフェイスを作成できます。コンテンツカードフィードのカスタマイズ方法の詳細については、[ドキュメント]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style/) をご覧ください。 

## API レート制限

[料金制限は]({{site.baseurl}}/api/basics/#api-limits/)2021年9月16日以降に搭乗するすべての顧客に適用される。 

## AndroidとFireOSの開発者向けガイドを更新

AndroidとFireOSの開発者ガイドは1つの場所に統合された。この[新しいAndroidセクション]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android) では、専用のFireOS アーティクルを使用できます。

## ファネルとリテンションレポートの更新

[ファネルレポート]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/)と[保持レポート]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/)がSMSキャンペーンで利用可能になりました。
