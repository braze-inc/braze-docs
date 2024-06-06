---
nav_title: 4月
page_order: 9
noindex: true
page_type: update
description: "この記事には、2017 年 4 月のリリースノートが含まれています。"
---

# 2017 年 4 月

## HTML ブラウザ内メッセージ

カスタム HTML やメールキャプチャ形式などのインタラクティブなブラウザ内メッセージタイプをサポートするようになったため、どこにいても顧客にリーチできます。[アプリ内メッセージの詳細をご覧ください][48]。

## 接続コンテンツを含むパーソナライズされたアプリ内メッセージ

{% raw %}{%connected_content%}{% endraw %}トリガーされるアプリ内メッセージにブロックを追加しました。これにより、API 経由でアクセス可能な情報をメッセージに直接挿入することで、高度なカスタマイズが可能になります。これで、プッシュ、メール、ウェブフックに加えて、アプリ内でコネクテッドコンテンツを使用できるようになりました。[コネクテッドコンテンツの詳細をご覧ください][34]。

## ニュースフィードカードのナビゲーションが改善されました

ニュースフィードカード作成の UI が改善され、キャンペーンのナビゲートや作成が容易になりました。[ニュースフィードカードの詳細をご覧ください][33]。

## iOS リッチ通知のプレビューが改善されました

iOSのプレビュー通知には、豊富な通知が表示されるようになりました。これにより、顧客に送信している内容をフォントサイズまで正確に把握できます。[iOS のリッチ通知の詳細をご覧ください][32]。

## プッシュ統計に「影響を受けたオープン」を追加

Brazeで提供される標準キャンペーンとキャンバス統計のリストに「影響を受けた開封数」を追加しました。これにより、影響を受けた開封数、直接開封数、合計開封数のキャンペーンの内訳がわかりやすくなりました。[インフルエンスオープンについて詳しくは][31]、こちらをご覧ください。

## 内部グループへのアップグレード

複数の内部グループを作成し、そのグループを SDK ロギング、REST API ロギング、またはメッセージコンテンツテストに使用するかどうかを示すプロパティを割り当てることができるようになりました。[イベントユーザーログの詳細をご覧ください][30]。

> 更新:[内部グループを使用してシードメールを送信することもできます]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/#seed-groups)。

## ウェブ URL の新しいオプション

プッシュメッセージ、アプリ内メッセージ、ブラウザ内メッセージ、ニュースフィードカード用のウェブ URL を外部のウェブブラウザで開くことができるようになりました。「アプリへのディープリンク」アクションは、HTTP/HTTPSディープリンクにも対応するようになりました。BranchやAppleのユニバーサルリンクなどのパートナーを使用する場合は、SDKのカスタマイズが必要になります。[ディープリンクの詳細をご覧ください][29]。

## 新しい「実行されたコンバージョン」イベントキャンバス

リターゲティングオプションを改善するために、新しい「実行されたコンバージョン」イベントと「キャンバスコントロール内」フィルターを追加しました。[リターゲティングフィルターの使用について詳しくは][28]、こちらをご覧ください。



[28]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#retargeting-campaigns
[29]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking
[30]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[31]: {{site.baseurl}}/user_guide/data_and_analytics/influenced_opens/#influenced-opens
[32]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#ios-10-rich-notifications
[33]: {{site.baseurl}}/user_guide/engagement_tools/news_feed/creating_a_news_feed_item/#news-feed-cards
[34]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
[48]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/
[98]:{{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#authentication-rules
