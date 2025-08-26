---
nav_title: Exporting large segments
article_title: Exporting Large Segments
page_order: 4

page_type: solution
description: "This help article walks you through several methods on exporting large user segments."
tool: Segments
---

# Exporting large segments

There are several methods to export a large user segment. For segments that contain over 500,000 users, you can breakdown this larger segment into smaller segments to capture these users, and export each of the smaller segments from the Braze dashboard. 

You can also consider using [random bucket numbers]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/ab_testing_with_random_buckets/#step-1-segment-your-users-by-the-random-bucket-attribute) to break your user base into multiple segments, and then combine them after export. For example, if you need to break up your segment into two different segments, you can do so with the following filters:
- Segment 1: Random bucket number is less than 5000 (includes 0-4999)
- Segment 2: Random bucket number is more than 4999 (includes 5000-9999)

You can also leverage the following endpoints to export user data for a specific segment. Note that these endpoints are subject to data limits.
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/)

Still need help? Open a [support ticket]({{site.baseurl}}/braze_support/).

_Last updated on October 24, 2022_
