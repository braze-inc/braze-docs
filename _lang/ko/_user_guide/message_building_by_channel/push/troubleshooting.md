---
nav_title: 문제 해결
article_title: 푸시 문제 해결
page_order: 23
page_type: reference
description: "이 페이지에는 푸시 메시징 채널과 관련된 다양한 문제에 대한 문제 해결 단계가 포함되어 있습니다."
channel: push
---

# 푸시 문제 해결

> 이 페이지에서는 푸시 메시징 채널에서 발생할 수 있는 다양한 문제를 해결하는 데 도움이 됩니다.

## 누락된 푸시 알림

푸시 알림으로 인해 전달에 어려움을 겪고 계신가요? 이 문제를 해결하기 위해 취할 수 있는 여러 단계가 있습니다.

- [푸시 구독 상태](#push-subscription-status)
- [세그먼트](#segment)
- [푸시 알림 캡](#push-notification-caps)
- [요금 제한](#rate-limits)
- [대조군 상태](#control-group-status)
- [유효한 푸시 토큰](#valid-push-token)
- [푸시 알림 유형](#push-notification-type)
- [현재 앱](#current-app)

#### 푸시 구독 상태

푸시는 구독하거나 옵트인한 사용자에게만 보낼 수 있습니다. **사용자 프로필** 섹션의 [참여]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) 탭에서 사용자 프로필을 확인하여 테스트 중인 워크스페이스에 대해 푸시 등록이 되어 있는지 확인합니다. 여러 앱에 등록되어 있는 경우 **푸시 등록 대상** 필드에 해당 앱이 나열됩니다:

![푸시 등록]({% image_buster /assets/img_archive/trouble1.png %})

Braze 내보내기 엔드포인트를 사용하여 사용자 프로필을 내보낼 수도 있습니다:
- [식별자별 사용자]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)
- [세그먼트별 사용자]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)

두 엔드포인트 모두 기기별 푸시 인에이블먼트 정보가 포함된 푸시 토큰 객체를 반환합니다.

#### 세그먼트

타겟팅하는 세그먼트에 속하는지 확인하세요(테스트가 아닌 라이브 캠페인인 경우). **고객 프로필**에 사용자가 현재 속해 있는 세그먼트 목록이 표시됩니다. 세분화는 실시간으로 업데이트되므로 계속 변화하는 변수라는 점을 기억하세요.

![세그먼트 목록]({% image_buster /assets/img_archive/trouble2.png %})

세그먼트를 만들 때 사용자 **조회를** 사용하여 사용자가 세그먼트의 일부인지 확인할 수도 있습니다.

![검색 필드가 있는 사용자 조회 섹션]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

#### 푸시 알림 캡

글로벌 주파수 한도를 확인하세요. 워크스페이스에 글로벌 최대 게재빈도 설정이 적용되어 있고 지정된 기간 동안 푸시 알림 한도에 이미 도달했기 때문에 푸시 알림을 받지 못했을 수 있습니다.

대시보드에서 [글로벌 주파수 제한을]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#freq-cap-feat-over) 확인하여 이를 수행할 수 있습니다. 캠페인이 빈도 제한 규칙을 준수하도록 설정된 경우, 이러한 설정의 영향을 받는 사용자가 다수 발생할 수 있습니다.

![캠페인 세부 정보]({% image_buster /assets/img_archive/trouble3.png %})

#### 요금 제한

캠페인 또는 캔버스에 사용량 제한이 설정되어 있는 경우 이 한도를 초과하여 메시징 수신이 중단될 수 있습니다. 자세한 내용은 [요금 제한을]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting) 참조하세요.

#### 대조군 상태

단일 채널 캠페인이거나 캔버스에 대조 그룹이 있는 경우 대조 그룹에 속할 수 있습니다.

  1. [이형 상품 분포를]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#step-5-distribute-users-among-your-variants) 확인하여 대조 그룹이 있는지 확인합니다.
  2. 그렇다면 [캠페인 관리 그룹에서]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#in-campaign-control-group-filter) 세그먼트 필터링을 생성한 다음 [세그먼트를 내보내고]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/segment_data_to_csv/#exporting-to-csv) 사용자 ID가 이 목록에 있는지 확인하세요.

#### 유효한 푸시 토큰
푸시 토큰은 발신자가 푸시 알림으로 특정 기기를 타겟팅할 때 사용하는 식별자입니다. 따라서 기기에 유효한 푸시 토큰이 없는 경우 푸시 알림을 보낼 방법이 없습니다. 

#### 푸시 알림 유형

올바른 유형의 푸시 알림을 사용하고 있는지 확인하세요. 예를 들어, FireTV를 타겟팅하려는 경우 Android 푸시 캠페인이 아닌 Kindle 푸시 알림을 사용합니다. 마찬가지로 안드로이드를 타겟팅하려면 iOS 푸시 캠페인이 아닌 안드로이드 푸시 알림을 사용하세요. Braze 워크플로우를 이해하는 방법에 대한 자세한 내용은 다음 문서를 참조하세요.
- [Apple 푸시 알림]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=swift)
- [파이어베이스 클라우드 메시징]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android)

#### 현재 앱

내부 사용자를 대상으로 푸시 전송을 테스트할 때는 푸시 알림을 받으려는 사용자가 현재 관련 앱에 로그인되어 있는지 확인하세요. 이로 인해 사용자가 푸시를 받지 못하거나 세그먼트화되지 않은 것으로 판단되는 푸시를 받을 수 있습니다.

아직도 도움이 필요하신가요? [지원 티켓]({{site.baseurl}}/braze_support/)을 여세요.

