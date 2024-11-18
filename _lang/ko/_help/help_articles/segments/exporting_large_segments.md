---
nav_title: 대형 세그먼트 내보내기
article_title: 대형 세그먼트 내보내기
page_order: 4

page_type: solution
description: "이 도움말 문서는 대규모 사용자 세그먼트를 내보내는 여러 방법을 안내합니다."
tool: Segments
---

# 대형 세그먼트 내보내기

큰 사용자 세그먼트를 내보내는 여러 가지 방법이 있습니다. 세그먼트에 500,000명 이상의 사용자가 포함된 경우, 이 더 큰 세그먼트를 더 작은 세그먼트로 분할하여 이러한 사용자를 캡처하고 각 더 작은 세그먼트를 Braze 대시보드에서 내보낼 수 있습니다. 

또한 [무작위 버킷 번호]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/ab_testing_with_random_buckets/#step-1-segment-your-users-by-the-random-bucket-attribute)를 사용하여 사용자 기반을 여러 세그먼트로 나눈 다음 내보낸 후 결합하는 것을 고려할 수 있습니다. 예를 들어, 세그먼트를 두 개의 다른 세그먼트로 나누어야 하는 경우 다음 필터를 사용하여 수행할 수 있습니다:
- 세그먼트 1: 무작위 버킷 번호는 5000보다 작습니다 (0-4999 포함)
- 세그먼트 2: 무작위 버킷 번호는 4999보다 큽니다 (5000-9999 포함)

다음 엔드포인트를 활용하여 특정 세그먼트의 사용자 데이터를 내보낼 수도 있습니다. 이러한 엔드포인트는 데이터 제한을 받을 수 있습니다.
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/)

아직도 도움이 필요하신가요? [지원 티켓]({{site.baseurl}}/braze_support/)을 여세요.

_마지막 업데이트 날짜: 2022년 10월 24일_
