---
nav_title: 4月
page_order: 9
noindex: true
page_type: update
description: "この記事には2017年4月のリリースノートが含まれている。"
---

# 2017年4月

## HTMLブラウザ内メッセージ

カスタムHTMLやEメール・キャプチャ・フォーマットを含む、インタラクティブなインブラウザ・メッセージ・タイプをサポートするようになった。[アプリ内メッセージについて][48]もっと知る。

## 接続されたコンテンツでパーソナライズされたアプリ内メッセージ

アプリ内メッセージのトリガーに{% raw %} {%connected_content%} {% endraw %} ブロックが追加され、API経由でアクセス可能なあらゆる情報をメッセージに直接挿入することで、リッチなパーソナライゼーションを追加できるようになった。これで、プッシュ、Eメール、ウェブフックに加えて、アプリ内でコネクテッド・コンテンツを使うことができる。[コネクテッド・コンテンツについて][34]もっと知る。

## ニュースフィードカードのナビゲーションを改善

ニュースフィードカードを作成するためのUIを改善し、ナビゲートとキャンペーンの作成をより簡単にした。[ニュースフィードカードについて][33]もっと知る。

## iOSリッチ通知のプレビューを改善

iOSのプレビュー通知では、リッチな通知が表示されるようになり、顧客に送信している内容をフォントサイズまで正確に把握できるようになった。[iOSのリッチ通知について][32]もっと知る。

## プッシュ統計に「Influenced Opens」を追加

Brazeで提供される標準的なキャンペーンとキャンバスの統計リストに「Influenced Opens」が追加され、キャンペーンのInfluenced、Direct、Total Opensの内訳を簡単に知ることができるようになった。[インフルエンス・オープンについて][31]もっと知る。

## 内部グループへのアップグレード

複数の内部グループを作成し、SDKロギング、REST APIロギング、またはメッセージコンテンツテストのためにグループを使用するかどうかを示すプロパティを割り当てることができるようになった。[イベント・ユーザー・ログについて][30]もっと知る。

> 更新された：内部グループは、[シードメールの送信にも]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/#seed-groups)使用できる。

## ウェブURLの新しいオプション

プッシュメッセージ、アプリ内メッセージ、ブラウザ内メッセージ、ニュースフィードカードについて、外部ウェブブラウザでウェブURLを開くオプションが追加された。アプリへのディープリンク」アクションは、HTTP/HTTPSディープリンクにも対応するようになった。BranchやAppleのUniversal Linksのようなパートナーを使う場合は、SDKのカスタマイズが必要になる。[ディープリンクについて][29]もっと知る。

## 新しい "Performed Conversion "イベント・キャンバス

新しい "Performed Conversion "イベントと "In Canvas Control "フィルターを追加し、リターゲティングオプションを改善した。[リターゲティング・フィルターの][28]使い方についてもっと知る。



[28]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#retargeting-campaigns
[29]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking
[30]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[31]: {{site.baseurl}}/user_guide/data_and_analytics/influenced_opens/#influenced-opens
[32]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#ios-10-rich-notifications
[33]: {{site.baseurl}}/user_guide/engagement_tools/news_feed/creating_a_news_feed_item/#news-feed-cards
[34]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
[48]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/
[98]:{{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#authentication-rules
