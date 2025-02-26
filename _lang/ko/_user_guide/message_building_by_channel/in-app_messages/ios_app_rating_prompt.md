---
nav_title: iOS용 인앱 평가 프롬프트
article_title: iOS용 인앱 평가 프롬프트
page_order: 6
description: "이 문서에서는 Braze를 사용하여 사용자에게 앱 검토를 요청하는 방법과 그 의미에 대해 설명합니다."
channel:
  - in-app messages

---

# iOS용 인앱 평가 프롬프트

> 이 문서에서는 Braze를 사용하여 사용자에게 앱 검토를 요청하는 방법과 그 의미에 대해 설명합니다. 효과적인 앱 평점 캠페인을 만드는 방법에 대한 팁은 [고객 앱 평점의 해야 할 일과 하지 말아야 할 일을](https://www.braze.com/resources/articles/the-dos-and-donts-of-customer-app-ratings) 확인하세요.

Apple은 iOS 10.3에 도입된 기본 프롬프트를 통해 사용자가 앱 자체에서 앱을 평가할 수 있는 기능을 제공합니다. iOS에서 인앱 메시지를 사용하여 사용자에게 앱 등급을 요청하려면 Apple에서 사용자 지정 검토 메시지를 허용하지 않으므로 기본 메시지를 사용해야 합니다( [앱 스토어 검토 가이드라인](https://developer.apple.com/app-store/review/guidelines/#code-of-conduct) 5.6.1절 참조).

Apple 가이드라인에 따라 앱 리뷰 프롬프트는 1년에 최대 3회까지 사용자에게 표시될 수 있으므로 모든 앱 리뷰 캠페인은 [사용량 제한조치]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/)를 활용해야 합니다. 또한 사용자는 앱 설정에서 앱 리뷰 메시지를 완전히 표시하지 않도록 선택할 수도 있습니다. App Store 평가에 대한 자세한 내용은 Apple의 [평가, 리뷰 및 응답에](https://developer.apple.com/app-store/ratings-and-reviews/) 대한 문서를 참조하세요.

## Braze를 사용하여 사용자에게 앱 리뷰 요청하기

Apple은 기본 프롬프트를 사용하도록 요구하지만, Braze 캠페인을 활용하여 사용자에게 적절한 순간에 앱을 평가하고 검토하도록 요청할 수 있습니다. 두 가지 주요 접근 방식을 사용할 수 있습니다.

### 접근 방식 1: 앱 스토어에 딥링킹

이 접근 방식을 사용하면 사용자가 앱 스토어를 방문하여 리뷰를 추가하도록 유도할 수 있습니다. 이렇게 하려면 앱 스토어에 [딥링크로]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) 연결되는 인앱 메시지 캠페인을 생성하세요.

![두 개의 모바일 화면을 나란히 배치합니다. 첫 번째는 앱 스토어에서 앱에 대한 평가를 요청하는 인앱 메시지입니다. 두 번째는 해당 앱의 iOS 앱 스토어 페이지입니다.][1]

### 접근 방식 2: 소프트 프라이밍

사용자가 앱을 떠나지 않도록 하려면 먼저 별도의 인앱 메시지로 사용자에게 메시지를 전달할 수 있습니다. 프라이밍은 기본 App Store 리뷰 프롬프트를 보내기 전에 사용자에게 권한을 요청하는 방법입니다. 이렇게 하려면 인앱 메시지 캠페인을 생성하고 클릭 시 `requestReview` 메서드를 호출하는 커스텀 딥링크를 추가합니다. 

자세한 단계는 [커스텀 앱 스토어 검토 프롬프트]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/custom_app_store_review_prompt/)를 참조하세요.

![두 개의 인앱 메시지를 나란히 표시합니다. 첫 번째는 앱을 평가할 시간이 있는지 물어봄으로써 사용자가 앱을 평가하도록 유도합니다. 두 번째는 기본 iOS 앱 스토어 리뷰 메시지로, 사용자가 앱을 평가하기 위해 선택할 수 있는 별 5개 등급을 표시합니다.][2]

사용자는 기본 App Store 리뷰 프롬프트를 통해 평점을 제출하며, 앱에서 나가지 않고도 리뷰를 작성하고 제출할 수 있습니다.

### 고려 사항

소프트 프라이머의 대안으로, 이전에 표시되었던 Braze 소프트 프라이머 메시지 없이 iOS 앱 등급 프롬프트를 바로 표시할 수도 있습니다. 이 방법의 장점은 사용자가 앱 리뷰 메시지를 선택 해제하면 앱을 평가하려고 해도 평가하라는 메시지가 표시되지 않는 불편한 사용자 환경이 발생하지 않는다는 것입니다.

{% alert important %}
기본 iOS 앱 평점 메시지를 모방하는 사용자 지정 HTML 인앱 메시지는 Apple의 가이드라인에 위배되므로 만들지 마세요.
{% endalert %}

[1]: {% image_buster /assets/img_archive/app_store_app_review.png %}
[2]: {% image_buster /assets/img_archive/prime_app_review.png %}