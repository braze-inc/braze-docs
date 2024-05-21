---
nav_title: 大規模セグメントのエクスポート
article_title: 大規模セグメントのエクスポート
page_order: 4

page_type: solution
description: "このヘルプ記事では、大規模なユーザーセグメントをエクスポートするいくつかの方法について説明します。"
tool: Segments
---

# 大規模セグメントのエクスポート

大規模なユーザーセグメントをエクスポートするには、いくつかの方法があります。500,000人以上のユーザーを含むセグメントでは、この大きなセグメントを小さなセグメントに分割してこれらのユーザーを獲得し、小さなセグメントをそれぞれBrazeダッシュボードからエクスポートできます。 

また、[ランダムなバケット番号を使用してユーザーベースを複数のセグメントに分割し]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/ab_testing_with_random_buckets/#step-1-segment-your-users-by-the-random-bucket-attribute)、エクスポート後にそれらを組み合わせることも検討できます。たとえば、セグメントを 2 つの異なるセグメントに分割する必要がある場合は、次のフィルターを使用できます。
-セグメント 1:ランダムバケット番号が 5000 未満 (0 ～ 4999 を含む)
-セグメント 2:ランダムバケット番号が4999を超えています（5000〜9999を含む）

次のエンドポイントを利用して、特定のセグメントのユーザーデータをエクスポートすることもできます。これらのエンドポイントはデータ制限の対象となることに注意してください。
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/)

まだ助けが必要ですか？[サポートチケットを開きます]({{site.baseurl}}/braze_support/)。

_2022年10月24日に最終更新されました_
