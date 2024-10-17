---
nav_title: 4月
page_order: 9
noindex: true
page_type: update
description: "この記事には2017年4月のリリースノートが含まれている。"
---

# 2017年4月

## HTMLブラウザ内メッセージ

カスタム HTML およびメールキャプチャ形式を含むインタラクティブなブラウザ内メッセージタイプがサポートされるようになりました。これにより、どこにいても顧客にリーチできます。[アプリ内メッセージ s][48] について詳しく説明します。

## 接続されたコンテンツでパーソナライズされたアプリ内メッセージ

トリガーされたアプリ内メッセージに {% raw %} {%connected_content%} {% endraw %} ブロックを追加しました。これにより、API 経由でアクセス可能な情報をメッセージに直接挿入して、豊富なパーソナライゼーションを追加できます。プッシュ、メール、Webhook に加えて、アプリ内でコネクテッドコンテンツを使用できるようになりました。[Connected Content][34]について詳しく説明します。

## ニュースフィードカードのナビゲーションを改善

ニュースフィードカードを作成するためのUIを改善し、ナビゲートとキャンペーンの作成をより簡単にした。[ニュースフィードカードについて][33]もっと知る。

## iOSリッチ通知のプレビューを改善

iOSのプレビュー通知では、リッチな通知が表示されるようになり、顧客に送信している内容をフォントサイズまで正確に把握できるようになった。詳細については、[iOS リッチプッシュ通知][32]を参照してください。

## プッシュ統計に「Influenced Opens」を追加

「"Influenced Opens"」をBrazeで提供されているスタンダードキャンペーンとキャンバス統計の一覧に追加しました。これにより、「Influenced」、「Direct」、および「Total Opens」のキャンペーンの内訳がわかりやすくなります。詳細については、[誘発された開封数][31]を参照してください。

## 内部グループへのアップグレード

複数の内部グループを作成し、SDKロギング、REST APIロギング、またはメッセージコンテンツテストのためにグループを使用するかどうかを示すプロパティを割り当てることができるようになった。[イベントユーザーログ][30]について詳しく説明します。

> 更新:内部グループを使用して、[シードメールs]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/#seed-groups)を送信することもできます。

## ウェブURLの新しいオプション

プッシュメッセージ、アプリ内メッセージ、ブラウザ内メッセージ、ニュースフィードカードについて、外部ウェブブラウザでウェブURLを開くオプションが追加された。「アプリにディープリンクする」アクションと HTTP/HTTPS ディープリンクとの互換性も確保されました。Branch や Apple のユニバーサルリンクなどのパートナーを使用する場合は、SDK のカスタマイズが必要になります。詳細については、[ディープリンク][29]を参照してください。

## 新しい「コンバージョンを実行」イベントキャンバス

新しい「コンバージョンを実行」イベントと「キャンバス内コントロール」フィルターを追加し、リターゲティングを改善しました。[リターゲティングフィルター][28]の使用に関する詳細をご確認ください。



[28]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#retargeting-campaigns
[29]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking
[30]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[31]: {{site.baseurl}}/user_guide/data_and_analytics/influenced_opens/#influenced-opens
[32]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#ios-10-rich-notifications
[33]: {{site.baseurl}}/user_guide/engagement_tools/news_feed/creating_a_news_feed_item/#news-feed-cards
[34]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
[48]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/
[98]:{{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#authentication-rules
