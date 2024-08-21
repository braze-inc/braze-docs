---
nav_title: 大きなセグメントをエクスポートする
article_title: 大きなセグメントをエクスポートする
page_order: 4

page_type: solution
description: "このヘルプ記事では、大規模なユーザーセグメントをエクスポートするためのいくつかの方法について説明する。"
tool: Segments
---

# 大きなセグメンテーションをエクスポートする

大規模なユーザーセグメントをエクスポートするには、いくつかの方法がある。50万人以上のユーザーを含むセグメンテーションの場合、この大きなセグメンテーションを小さなセグメンテーションに分割して、これらのユーザーを捕捉し、ダッシュボードからそれぞれの小さなセグメンテーションをエクスポートすることができる。 

また、[ランダムなバケット番号を使って]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/ab_testing_with_random_buckets/#step-1-segment-your-users-by-the-random-bucket-attribute)ユーザー群を複数のセグメンテーションに分け、エクスポート後にそれらを組み合わせることも検討できる。たとえば、セグメンテーションを2つの異なるセグメントに分割する必要がある場合、以下のフィルターを使って分割することができる：
- セグメント1:ランダムバケット番号が5000未満（0～4999を含む）
- セグメンテーション2：ランダムバケット番号が4999以上（5000～9999を含む）

また、以下のエンドポイントを活用して、特定のセグメントのユーザーデータをエクスポートすることもできる。これらのエンドポイントはデータ制限の対象となる。
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/)

まだ助けが必要か？[サポートチケットを]({{site.baseurl}}/braze_support/)開封する。

_最終更新日：2022年10月24日_
