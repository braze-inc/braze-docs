---
nav_title: キャンペーンまたはキャンバスの低コンバージョン
article_title: キャンペーンまたはキャンバスの低コンバージョン
page_order: 4

page_type: solution
description: "このヘルプ記事では、期待したコンバージョン率より低いキャンペーンやキャンバスのトラブルシューティングについて説明する。"
tool:
- Canvas
- Campaigns
---

# キャンペーンまたはキャンバスのコンバージョンが低い

コンバージョンは、キャンペーン作成時に定義したメッセージ内でユーザーがアクションを実行したときに発生する。

以前のキャンペーンや期待と比較すると、コンバージョンが期待したほど高くならない可能性があります。コンバージョンは扱いにくい数値ですが、イベントトラッキングとコンバージョン期限という、Braze のプラットフォームにおけるいくつかのシンプルな機能に依存しています。

その理由を素早くトラブルシューティングするには、イベントトラッキングとコンバージョンの期限をチェックすることをお勧めする。

## イベントトラッキング

キャンペーンがセッション開始またはカスタムイベントをトリガーするとき、このイベントまたはセッションがメッセージをトリガーするのに十分な頻度で発生していることを確認したい。[概要][1](セッション情報の場合)または[カスタムイベント][2]ページでこのデータを確認します。

![カスタムイベント数の統計を含む [カスタムイベント] ページ。][43]

## コンバージョンの期限

キャンペーンごとに選択したコンバージョンイベントごとに、[期限][44] を設定する。つまり、コンバージョンが各キャンペーンでカウントされるための発生時間の制限を設定します。

キャンペーン指標を理解するために、[コンバージョンの計算][45] に関する情報を確認しておきます。キャンバスのユーザーコンバージョンについては、[キャンバスに関する FAQ]({{site.baseurl}}/user_guide/engagement_tools/canvas/faqs/#how-are-user-conversions-tracked-in-a-canvas) を参照してください。 

サポートが必要な場合は、[サポートチケット]({{site.baseurl}}/braze_support/)を登録してください。

_最終更新日：2021年5月6日_

[1]: {{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting
[43]: {% image_buster /assets/img_archive/trouble5.png %}
[44]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#step-2-add-conversion-events
[45]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-tracking-rule