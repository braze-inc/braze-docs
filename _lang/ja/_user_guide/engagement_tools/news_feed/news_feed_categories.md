---
nav_title: ニュースフィードのカテゴリ
page_order: 9

page_type: reference
description: "この参考記事では、ニュースフィードの複数のインスタンスをアプリケーションに統合できるようにするニュースフィードカテゴリについて説明します。"
tool: Dashboard
channel: news feed
hidden: true

---

# ニュースフィードのカテゴリ

{% alert note %}
ニュースフィードは非推奨になります。Braze では、News Feed ツールを使用するお客様は、コンテンツカードメッセージングチャネルに移動することを推奨しています。これは、より柔軟でカスタマイズ可能で、信頼性が高いチャネルです。詳しくは[マイグレーションガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)をご覧ください。
{% endalert %}

> ニュースフィードのカテゴリを使用すると、ニュースフィードの複数のインスタンスをアプリケーションに統合できます。特定のカテゴリのニュースフィードカードのみを表示するさまざまな期間内でフィードを統合することができます。

![Sweet Teeth - Buy candy in bulk!"というタイトルのニュースフィードアイテムのキャプション付きイメージカードプレビューが付いたニュースフィードパネルには、"Satisfy your sweet tooth and stop by our store. "というメッセージが添えられている！この広告に言及すると、最初のキャンディー 1 袋が 50% オフになります」というメッセージが添えられています。]ニュースフィードのカテゴリには、[ニュース]、[お知らせ]、[広告]、[ソーシャル] の 4 つのチェックボックスがあります。どのカテゴリも選択されていません。][1]

ニュースフィードを特定のカテゴリからのものとしてマークしても、エンド ユーザーには表示されません。デフォルトでは、特定のカテゴリを表示するようにアプリコードでフィードが特別に構成されていない限り、Braze のニュースフィードにはすべてのカテゴリのカードが表示されます。アプリコードの設定の詳細については、[ニュースフィードカテゴリの定義][2] を参照してください。

[1]: {% image_buster /assets/img_archive/Newsfeed_category.png %}
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/news_feed/defining_a_news_feed_category/
