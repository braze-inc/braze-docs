---
nav_title: ランダムバケット番号
article_title: ランダムバケット番号
page_order: 2
page_type: reference
description: "この記事では、ランダムバケット番号の概念と、それを使用してバリアントとコントロールグループを作成する方法について説明します。"
page_type: reference
tool:
  - Campaign
  - Canvas

---

# ランダムバケット番号

> この記事では、ランダムバケット番号の概念と、それを使用してバリアントとコントロールグループを作成する方法について説明します。

## 概要

Braze でユーザープロファイルを作成すると、そのユーザーには0から9999までのランダムなバケット番号が自動的に割り当てられます。ランダムバケット番号は、ランダムユーザーの均一に分散したセグメントを作成するために使用できるユーザー属性です。これらのセグメントを活用して、ユーザーのグループに対する複数のキャンペーンまたはキャンバスの効果を長期的にテストできます。

ランダムなバケット番号は、キャンペーンやキャンバスを受信しないユーザーのグループであるグローバルコントロールグループでも使用されます。Braze はランダムなバケット番号の複数の範囲をランダムに選択し、選択されたバケットのユーザーを含めます。グローバルコントロールグループを設定していて、ランダムなバケット番号を他の用途に使用したい場合は、[注意すべきこと]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#things-to-watch-for)を確認してください。

### ランダムなバケット番号を使用する場合

複数のキャンペーンやキャンバスの効果を長期的にテストする場合は、ランダムなバケット番号を使用してユーザーをセグメント化できます。

### 他のものを使用する場合

1つのキャンペーンまたは1つのキャンバス内でテストするユーザーをセグメント化する場合は、代わりにキャンペーンの [AB テスト]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/)を使用してください。キャンバスでは、ジャーニーレベルのテスト用に異なる[バリアント]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#adding-a-variant)を作成したり、ステップレベルのテスト用に[実験パス]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/)を使用することもできます。

## ランダムなバケット番号を使用してセグメントを作成する

[セグメントを作成]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/)するときは、`Random Bucket #` フィルターを追加します。フィルターラベルが**統計サンプリング ID** に変わります。その後、セグメントに含める番号または番号の範囲を指定できます。

![][1]

![][2]

3つの異なるバリアントのテストを実行し、コントロールグループも含める場合は、これらのタイプのセグメントを使用することもできます。3つのバリアントとコントロールグループで同じサイズのセグメントを作成するための次のサンプルプランを考えます。

- バケット番号0～2499はコントロールセグメントに対応する
- バケット番号2500から4999は、バリアント1を受け取るセグメントに対応する
- バケット番号5000から7499は、バリアント2を受け取るセグメントに対応する
- バケット番号7500～9999は、バリアント3を受け取るセグメントに対応する

必要なセグメントの数や各セグメント内のユーザーの分布によって、プランが異なる場合があります。

コントロールグループを含むランダムバケット番号セグメントごとに、[[分析トラッキング]({{site.baseurl}}/user_guide/data_and_analytics/tracking/segment_analytics_tracking)] をオンにします。コントロールグループに関連してバリアントの成功を評価する場合、[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_custom_event_data)ページに移動し、各セグメントが特定のカスタムイベントを完了した頻度を表示できます。


[1]: {% image_buster /assets/img_archive/random_buckets_filter.png %}
[2]: {% image_buster /assets/img_archive/random_buckets_filterexample.png %}
