---
nav_title: 9월
page_order: 3
noindex: true
page_type: update
description: "이 문서에는 2021년 9월의 릴리스 노트가 포함되어 있습니다."
---

# 2021년 9월

## iOS 15

### Apple MPP 

Apple의 MPP(메일 개인정보 보호)는 9월 중순에 출시되는 iOS 15, iPadOS 15, macOS 몬터레이 및 watchOS 8의 Apple Mail 앱 사용자가 사용할 수 있는 개인정보 보호 업데이트입니다. MPP에 옵트인한 사용자의 경우 이제 이메일이 프록시 서버를 사용하여 미리 로드되어 이미지를 캐싱하고 [열람 추적]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#open-tracking-pixel)과 같은 측정기준에 추적 픽셀을 활용하는 기능을 방해하게 됩니다. 이메일 전달 가능성 측정기준과 관련된 MPP 및 문제, 이러한 측정기준을 기반으로 트리거되는 기존 캠페인 및 캔버스와 관련된 문제에 대해 자세히 알아보려면 [설명서]({{site.baseurl}}/user_guide/message_building_by_channel/email/apple_mail/mpp/)를 참조하세요.

### 푸시 기능

iOS 15에는 사용자가 하루 종일 집중하고 자주 방해받지 않도록 도와주는 새로운 알림 기능이 도입되었습니다. [중단 수준 및 관련성 점수]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/)를 포함한 새로운 기능을 지원하게 되어 매우 기쁩니다.

## 연락처 카드

연락처 카드는 비즈니스 및 연락처 정보를 전송하기 위한 표준화된 파일 형식으로 주소록이나 연락처 목록으로 쉽게 가져올 수 있습니다. 이제 SMS 및 MMS 메시지에 대한 연락처 카드를 업로드하고 만들 수 있습니다. 기본 제공 연락처 카드 생성기에서 연락처 카드를 만드는 방법에 대해 자세히 알아보려면 [설명서]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/contact_card/)를 참조하세요.

## 기본 콘텐츠 카드 사용자 지정

`ABKContentCardsTableViewController`를 확장하여 모든 UI 요소와 콘텐츠 카드 동작을 커스텀하여 나만의 콘텐츠 카드 인터페이스를 만들 수 있습니다. 콘텐츠 카드 피드를 커스텀하는 방법에 대한 자세한 내용은 [설명서]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style/)를 참조하세요. 

## API 사용량 제한

[사용량 제한]({{site.baseurl}}/api/basics/#api-limits/)은 2021년 9월 16일 이후에 가입한 모든 고객에게 적용됩니다. 

## Android 및 FireOS 개발자 가이드 업데이트

Android 및 FireOS 개발자 가이드가 한 곳으로 통합되었습니다. FireOS 전용 문서는 이 [새로운 Android 섹션]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android)에서 확인할 수 있습니다.

## 퍼널 및 리텐션 보고서 업데이트

이제 SMS 캠페인에 [퍼널 보고서]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) 와 [리텐션 보고서를]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/) 사용할 수 있습니다.
