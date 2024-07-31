---
nav_title: 4月
page_order: 9
noindex: true
page_type: update
description: "この記事には2017年4月のリリースノートが含まれている。"
---

# 2017年4月

## HTMLブラウザ内メッセージ

カスタムHTMLやメールキャプチャ形式を含むインタラクティブなインブラウザメッセージタイプをサポートし、顧客がどこにいてもメッセージを届けることができるようになった。[アプリ内メッセージについて][48]学習する。

## コネクテッドコンテンツでパーソナライズされたアプリ内メッセージ

アプリ内メッセージのトリガーに{% raw %} {%connected_content%} {% endraw %} ブロックを追加した。これにより、API経由でアクセス可能なあらゆる情報をメッセージに直接挿入することで、リッチパーソナライゼーションを追加できる。これで、プッシュ、メール、Webhookに加えて、アプリ内でコネクテッドコンテンツを使用できるようになった。[コネクテッド・コンテンツについて][34]もっと知る。

## ニュースフィードカードのナビゲーションが改善された。

ニュースフィードカードを作成するためのUIを改善し、より簡単に操作してキャンペーンを作成できるようになった。[ニュースフィード・カードについて][33]もっと知る。

## iOSのリッチプッシュ通知のプレビューが改善された。

iOSのプレビュー通知では、リッチプッシュ通知が表示されるようになり、顧客に送信する内容をフォントサイズまで正確に把握できるようになった。[iOSのリッチプッシュ通知について][32]学習する。

## プッシュ統計に「影響を受けた開封」を追加

Brazeで提供される標準的なキャンペーンとキャンバスの統計リストに「Influenced Opens」を追加し、キャンペーンのInfluenced、Direct、Total Opensの内訳を簡単に知ることができるようになった。[インフルエンス・オープンについて][31]もっと知る。

## 内部グループへのアップグレード

複数の内部グループを作成し、グループをSDKロギング、REST APIロギング、またはメッセージコンテンツテストのいずれに使用するかを示すプロパティを割り当てることができるようになった。[イベント・ユーザー・ログについて][30]学習する。

> 更新だ：内部グループは、[シードメールの送信にも]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/#seed-groups)使用できる。

## Web URLの新しいオプション

プッシュメッセージ、アプリ内メッセージ、ブラウザ内メッセージ、ニュースフィードカードについて、外部WebブラウザでWeb URLを開封するオプションが追加された。アプリへのディープリンク」アクションは、HTTP/HTTPSディープリンクにも対応するようになった。BranchやAppleのUniversal Linksのようなパートナーを使う場合は、SDKのカスタマイズが必要になる。[ディープリンクについて][29]もっと学習しよう。

## 新しい "パフォーマンス・コンバージョン "イベント キャンバス

リターゲティングオプションを改善するために、新しい "Performed Conversion "イベントと "In Canvas Control "フィルターを追加した。[リターゲティングフィルターの][28]使用について詳しく学習する。



[28]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#retargeting-campaigns
[29]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking
[30]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[31]: {{site.baseurl}}/user_guide/data_and_analytics/influenced_opens/#influenced-opens
[32]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#ios-10-rich-notifications
[33]: {{site.baseurl}}/user_guide/engagement_tools/news_feed/creating_a_news_feed_item/#news-feed-cards
[34]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
[48]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/
[98]:{{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#authentication-rules
