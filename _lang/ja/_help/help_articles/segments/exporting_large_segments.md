---
nav_title: 大きなセグメントをエクスポートする
article_title: 大きなセグメントをエクスポートする
page_order: 4

page_type: solution
description: "このヘルプ記事では、大きなユーザーセグメントのエクスポート方法について説明します。"
tool: Segments
---

# 大きなセグメントをエクスポートする

大きなユーザーセグメントをエクスポートするには、いくつかの方法があります。含まれるユーザー数が500,000を超える大きなセグメントについては、小さなセグメントに分割してこれらのユーザーをキャプチャし、小さなセグメントをそれぞれ Braze ダッシュボードからエクスポートできます。 

また、[ランダムバケット番号]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/ab_testing_with_random_buckets/#step-1-segment-your-users-by-the-random-bucket-attribute)を使用してユーザー群を複数のセグメントに分割し、エクスポート後に組み合わせることもできます。例えば、セグメントを2つの異なるセグメントに分割する必要がある場合は、次のフィルターを使用できます。
- セグメント1: ランダムバケット番号が5000未満 (0 ～ 4999を含む)
- セグメント2: ランダムバケット番号が5000以上 (5000 ～ 9999を含む)

また、次のエンドポイントを利用して、特定のセグメントのユーザーデータをエクスポートすることもできます。これらのエンドポイントはデータ制限の対象となるのでご注意ください。
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/)

サポートが必要な場合は、[サポートチケット]({{site.baseurl}}/braze_support/)を登録してください。

_最終更新日2022年10月24日_
