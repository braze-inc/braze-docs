---
nav_title: 大規模セグメントのエクスポート
article_title: 大規模セグメントのエクスポート
page_order: 4

page_type: solution
description: "このヘルプ記事では、大規模なユーザー Segmentのエクスポート方法について説明します。"
tool: Segments
---

# ラージSegmentのエクスポート

大きなユーザー Segmentをエクスポートするには、いくつかの方法があります。Segment s に500,000 ユーザー s 以上が含まれている場合、この大きなSegmentを小さなSegments に分解して、これらのユーザーs をキャプチャし、それぞれの小さなSegments をBraze ダッシュボードからエクスポートできます。 

また、[乱数バケット番号]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/ab_testing_with_random_buckets/#step-1-segment-your-users-by-the-random-bucket-attribute)を使用してユーザー群を複数のSegments に分割し、エクスポート後に組み合わせることもできます。たとえば、Segmentを2 つのSegments に分割する必要がある場合は、次のフィルターs を使用して分割できます。
- セグメント1:ランダムバケット番号が5000 未満(0 ～4999 を含む)
- セグメント2:ランダムバケット番号が4999 を超えています(5000 ～ 9999 を含む)

また、次のエンドポイントs を利用して、指定したSegmentのユーザーデータをエクスポートすることもできます。なお、これらのエンドポイントsはデータリミットの対象となります。
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/)

それでも助けが必要ですか?[サポートチケット]({{site.baseurl}}/braze_support/)を開きます。

_2022更新10月24日昨日d_
