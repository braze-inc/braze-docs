---
nav_title: 누락된 푸시 알림
article_title: 누락된 푸시 알림
page_order: 3

page_type: solution
description: "이 도움말 문서에서는 사용자가 푸시 알림을 받지 못하는 경우 수행할 수 있는 문제 해결 단계를 안내합니다."
channel: push
---
# 누락된 푸시 알림

푸시 알림으로 인해 전달에 어려움을 겪고 계신가요? 이 문제를 해결하기 위해 취할 수 있는 여러 단계가 있습니다.

* [푸시 구독 상태](#push-subscription-status)
* [세그먼트](#segment)
* [푸시 알림 캡](#push-notification-caps)
* [요금 제한](#rate-limits)
* [대조군 상태](#control-group-status)

### 푸시 구독 상태

**사용자 프로필** 섹션의 [참여][1] 탭에서 **사용자** 프로필을 확인하여 테스트 중인 워크스페이스에 대해 푸시 등록이 되어 있는지 확인하세요. 여러 앱에 등록되어 있는 경우 **푸시 등록 대상** 필드에 해당 앱이 나열됩니다:

![푸시 등록 대상][2]

Braze 내보내기 엔드포인트를 사용하여 사용자 프로필을 내보낼 수도 있습니다:
- [식별자별 사용자][12]
- [세그먼트별 사용자][13]

두 엔드포인트 모두 기기별 푸시 인에이블먼트 정보가 포함된 푸시 토큰 객체를 반환합니다.

### 세그먼트

타겟팅하는 세그먼트에 속하는지 확인하세요(테스트가 아닌 라이브 캠페인인 경우). **고객 프로필**에 사용자가 현재 속해 있는 세그먼트 목록이 표시됩니다. 세분화는 실시간으로 업데이트되므로 계속 변화하는 변수라는 점을 기억하세요.

![세그먼트 목록][3]

### 푸시 알림 캡

글로벌 주파수 한도를 확인하세요. 워크스페이스에 글로벌 최대 게재빈도 설정이 적용되어 있고 지정된 기간 동안 푸시 알림 한도에 이미 도달했기 때문에 푸시 알림을 받지 못했을 수 있습니다.

대시보드에서 [글로벌 최대 게재빈도 설정][4]을 확인하여 이 작업을 수행할 수 있습니다. 캠페인이 빈도 제한 규칙을 준수하도록 설정된 경우, 이러한 설정의 영향을 받는 사용자가 다수 발생할 수 있습니다.

![캠페인 세부 정보][5]

### 요금 제한

캠페인 또는 캔버스에 사용량 제한이 설정되어 있는 경우 이 한도를 초과하여 메시징 수신이 중단될 수 있습니다. 자세한 내용은 [요금 제한][9]]을 참조하세요.

### 대조군 상태

단일 채널 캠페인이거나 캔버스에 대조 그룹이 있는 경우 대조 그룹에 속할 수 있습니다.

  1. 대조군이 있는지 확인하려면 [배리언트 배포][6]]를 확인하세요.
  2. 그렇다면 [캠페인 대조군][7]에 [세그먼트 내보내기]에 대한 세그먼트 필터링을 생성하고 사용자 ID가 이 목록에 있는지 확인합니다.

### 유효한 푸시 토큰
푸시 토큰은 발신자가 푸시 알림으로 특정 기기를 타겟팅할 때 사용하는 식별자입니다. 따라서 기기에 유효한 푸시 토큰이 없는 경우 푸시 알림을 보낼 방법이 없습니다. 

### 푸시 알림 유형

올바른 유형의 푸시 알림을 사용하고 있는지 확인하세요. 예를 들어, FireTV를 타겟팅하려는 경우 Android 푸시 캠페인이 아닌 Kindle 푸시 알림을 사용합니다. Braze 워크플로우를 이해하는 방법에 대한 자세한 내용은 다음 문서를 참조하세요.
- [Apple 푸시 알림][10]
- [Firebase Cloud Messaging][11]

아직도 도움이 필요하신가요? [지원 티켓]({{site.baseurl}}/braze_support/)을 여세요.

_마지막 업데이트: 2021년 1월 21일_

[1]: {{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab
[2]: {% image_buster /assets/img_archive/trouble1.png %}
[3]: {% image_buster /assets/img_archive/trouble2.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#freq-cap-feat-over
[5]: {% image_buster /assets/img_archive/trouble3.png %}
[6]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#step-5-distribute-users-among-your-variants
[7]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#in-campaign-control-group-filter
[8]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/segment_data_to_csv/#exporting-to-csv
[9]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/troubleshooting/
[11]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/troubleshooting
[12]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier
[13]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_segment