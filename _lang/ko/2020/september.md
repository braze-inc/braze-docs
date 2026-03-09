---
nav_title: 9월
page_order: 4
noindex: true
page_type: update
description: "이 문서에는 2020년 9월의 릴리스 노트가 포함되어 있습니다."
---

# 9월

## 퍼널 보고

퍼널 리포팅은 고객이 [캠페인이나]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) [캔버스를]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) 수신한 후의 여정을 분석할 수 있는 시각적 보고서를 제공합니다.

## iOS 14 업그레이드 가이드

Apple의 새로운 iOS 14에서 발표된 변경 사항에 따라 Braze 관련 변경 사항과 Braze iOS SDK 통합에 필요한 조치 항목이 몇 가지 있습니다. 자세한 내용은 이 [업그레이드 가이드를]({{site.baseurl}}/ios_14/) 참조하세요.

## iOS 14용 IDFA 및 IDFV 변경 사항

iOS 14에서는 사용자가 광고 추적에 옵트인하고 앱과 광고 네트워크가 앱 방문 시 자신의 IDFA를 읽을 수 있도록 허용할지 여부를 결정해야 합니다. 따라서 Braze의 전략은 '공급업체 식별자'(예: IDFV)를 대신 사용하여 여러 기기에서 사용자를 계속 추적할 수 있도록 하는 것입니다. 자세한 내용은 [iOS 14 업그레이드 가이드]({{site.baseurl}}/ios_14/)를 참조하세요.

## 이메일 유효성 검사

이 새로운 이메일 구문 유효성 검사 프로세스는 Braze의 기존 프로세스를 업그레이드한 것입니다. 이 검사는 Braze로 업데이트하거나 가져온 이메일이 올바른지 확인하기 위한 검사입니다. 자세한 내용은 [이 가이드라인과 참고 사항]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation/)을 참조하세요.

## 커런츠의 무작위 버킷 사용자 이벤트

무작위 버킷 번호(예: RBN)는 워크스페이스 내에서 새 사용자가 생성될 때마다 발생합니다. 이 이벤트 기간 동안 각 신규 사용자에게는 무작위 버킷 번호가 할당되며, 이를 사용하여 균일하게 분포된 무작위 사용자 세그먼트를 생성할 수 있습니다. 이를 사용하여 다양한 임의의 버킷 번호 값을 그룹화하고 캠페인 및 캠페인 변형의 성과를 비교할 수 있습니다. 이 이벤트의 이용 가능 여부를 확인하려면 커런츠 [고객 행동 이벤트 용어집]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/)을 참조하세요.

## 캔버스 구성 요소 - 곧 출시됩니다!

Braze는 캔버스의 유연성과 기능을 향상시키는 데 도움이 되는 네 가지 새로운 캔버스 구성 요소를 추가했습니다. 이러한 새로운 구성 요소에는 다음이 포함됩니다: [의사 결정 분할 단계]({{site.baseurl}}/decision_split/), [지연 단계]({{site.baseurl}}/delay_step/), [메시징 단계]({{site.baseurl}}/message_step/) 및 [대상 그룹을 Facebook에 동기화합니다]({{site.baseurl}}/audience_sync_facebook/).
- **캔버스 의사 결정 분할, 지연 및 메시징 단계**<br>결정 분할을 사용하여 사용자가 정의된 쿼리와 일치하는지 여부에 따라 캔버스 브랜치를 만들 수 있습니다. 지연 단계를 사용하면 해당 메시지 없이도 캔버스에 독립형 지연을 추가할 수 있습니다. 메시징 단계를 사용하면 캔버스 흐름에서 원하는 위치에 독립형 메시지를 추가할 수 있습니다.
- **Facebook에 오디언스 동기화**<br>브랜드는 Braze 오디언스 동기화 기능을 Facebook에 사용하여 자체 Braze 통합의 사용자 데이터를 Facebook 맞춤 오디언스에 추가하여 행동 트리거, 세분화 등을 기반으로 광고를 게재할 수 있습니다. 사용자 데이터를 기반으로 Braze 캔버스에서 메시지(푸시, 이메일, SMS, 웹훅 등)를 트리거하는 데 일반적으로 사용하는 모든 기준을 이제 Facebook 커스텀 오디언스에서 해당 사용자에게 광고를 트리거하는 데 사용할 수 있습니다.

## SMS 인바운드 수신 이벤트

커런츠에 새로운 메시징 인게이지먼트 이벤트가 추가되었습니다. 이 이벤트는 사용자 중 한 명이 Braze SMS 구독 그룹 중 하나에 있는 전화번호로 SMS를 보낼 때 발생합니다. 자세한 내용은 커런츠 [메시징 및 인게이지먼트 이벤트 용어집]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/)에서 확인하세요.
