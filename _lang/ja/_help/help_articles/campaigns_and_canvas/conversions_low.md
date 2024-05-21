---
nav_title: キャンペーンまたはキャンバスのコンバージョン率が低い
article_title: キャンペーンまたはキャンバスのコンバージョン率が低い
page_order: 4

page_type: solution
description: "このヘルプ記事では、コンバージョン率が予想よりも低いキャンペーンやキャンバスのトラブルシューティングについて説明します。"
tool:
- Canvas
- Campaigns
---

# キャンペーンまたはキャンバスのコンバージョン率が低い

コンバージョンは、キャンペーンの作成時に定義したメッセージ内でユーザーがアクションを実行したときに発生します。

コンバージョン率は、以前のキャンペーンや予想と比較した場合、期待したほど高くない可能性があります。コンバージョンは扱いにくいビジネスですが、プラットフォームのいくつかのシンプルな機能、つまりイベントトラッキングとコンバージョン期限に依存しています。

その理由をすばやく解決するには、イベントトラッキングとコンバージョンの期限を確認することをおすすめします。

## イベントトラッキング

キャンペーンがセッション開始またはカスタムイベントをトリガーする場合、このイベントまたはセッションがメッセージをトリガーするのに十分な頻度で発生していることを確認する必要があります。[概要][1] (セッションデータ用) [またはカスタムイベントページで次のデータを確認してください][2]。

![カスタムイベント数の統計を含むカスタムイベントページ] [43]

## 変換期限

キャンペーンごとに選択するコンバージョンイベントごとに、[期限] [44] を設定します。つまり、コンバージョンが各キャンペーンでカウントされるためには、コンバージョンが発生するまでの時間制限を設定していることになります。

キャンペーンの指標を理解するために、[コンバージョンの計算] [45] に関する情報を確認しておいてください。Canvasでのユーザーコンバージョンについては、[Canvas FAQを参照してください]({{site.baseurl}}/user_guide/engagement_tools/canvas/faqs/#how-are-user-conversions-tracked-in-a-canvas)。 

まだ助けが必要ですか？[サポートチケットを開きます]({{site.baseurl}}/braze_support/)。

_最終更新日は2021年5月6日です_

[1]: {{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting
[43]: {% image_buster /assets/img_archive/trouble5.png %}
[44]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#step-2-add-conversion-events
[45]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-tracking-rule