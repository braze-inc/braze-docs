---
nav_title: キャンペーンやキャンバスのコンバージョンが低い
article_title: キャンペーンやキャンバスのコンバージョンが低い
page_order: 4

page_type: solution
description: "このヘルプ記事では、期待したコンバージョン率よりも低いキャンペーンやキャンバスのトラブルシューティングについて説明する。"
tool:
- Canvas
- Campaigns
---

# キャンペーンやキャンバスのコンバージョンが低い。

コンバージョンは、キャンペーン作成時に定義したメッセージ内でユーザーがアクションを実行したときに発生する。

以前のキャンペーンや予想と比較すると、コンバージョンが思ったほど高くないかもしれない。コンバージョンは厄介なビジネスだが、私たちのプラットフォームのいくつかのシンプルな機能、すなわちトラッキング、コンバージョン期限に依存している。

その理由を素早くトラブルシューティングするには、イベントトラッキングとコンバージョン期限をチェックすることをお勧めする。

## トラッキング、 追跡

キャンペーンがセッション開始またはカスタムイベントをトリガーするとき、このイベントまたはセッションがメッセージをトリガーするのに十分な頻度で起こっていることを確認したい。[概要][1]（セッションデータ用）または[カスタムイベントページで][2]このデータを確認する：

![カスタムイベントカウントの統計があるカスタムイベントページ。][43]

## コンバージョンの期限

キャンペーンごとに選択したコンバージョンイベントごとに、\[期限][44] を設定する。これは、コンバージョンがそれぞれのキャンペーンにカウントされるために、そのコンバージョンが発生しなければならない制限時間を設定していることを意味する。

キャンペーン指標を理解するために、\[コンバージョンの計算][45] ]に関する情報を確認したことを確認する。キャンバスのユーザーコンバージョンについては、[キャンバスFAQを]({{site.baseurl}}/user_guide/engagement_tools/canvas/faqs/#how-are-user-conversions-tracked-in-a-canvas)参照のこと。 

まだ助けが必要か？[サポートチケットを]({{site.baseurl}}/braze_support/)開封する。

_最終更新日：2021年5月6日_

[1]: {{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting
[43]: {% image_buster /assets/img_archive/trouble5.png %}
[44]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#step-2-add-conversion-events
[45]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-tracking-rule