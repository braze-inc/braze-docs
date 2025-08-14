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

キャンペーンがセッション開始またはカスタムイベントをトリガーするとき、このイベントまたはセッションがメッセージをトリガーするのに十分な頻度で発生していることを確認したい。このデータを[概要]({{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/)（セッションデータの場合）または[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting)ページで確認してください。

![カスタムイベント数の統計を含む [カスタムイベント] ページ。]({% image_buster /assets/img_archive/trouble5.png %})

## コンバージョンの期限

キャンペーンごとに選択したコンバージョンイベントごとに、[期限]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#step-2-add-conversion-events)設定します。つまり、コンバージョンが各キャンペーンでカウントされるための発生時間の制限を設定します。

キャンペーンの指標を理解するために、[コンバージョンの計算に関する]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-tracking-rule)情報を確認しておくこと。キャンバスのユーザーコンバージョンについては、[キャンバスに関する FAQ]({{site.baseurl}}/user_guide/engagement_tools/canvas/faqs/#how-are-user-conversions-tracked-in-a-canvas) を参照してください。 

サポートが必要な場合は、[サポートチケット]({{site.baseurl}}/braze_support/)を登録してください。

_最終更新日：2021年5月6日_

