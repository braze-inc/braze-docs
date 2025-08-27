---
nav_title: 4월
page_order: 9
noindex: true
page_type: update
description: "이 문서에는 2020년 4월 릴리스 노트가 포함되어 있습니다."
---
# 2020년 4월

## Movable Ink 파트너십

Movable Ink는 Braze 고객에게 푸시, 인앱 메시지 및 콘텐츠 카드 캠페인에서 카운트다운 타이머, 설문 조사 및 긁기와 같은 지능형 크리에이티브 기능을 사용할 수 있는 기능을 제공합니다. Movable Ink와 Braze는 데이터 중심의 동적 메시지에 대한 보다 균형 잡힌 접근 방식을 제공하여 사용자에게 중요한 것들에 대한 실시간 요소를 제공합니다.

귀하의 캠페인에 [Movable Ink]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/movable_ink/) 통합을 시작하세요!

## Intelligent Timing

캠페인을 예약할 때, [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/)(이전의 Intelligent Delivery)를 사용하여 각 사용자가 참여할 가능성이 가장 높은 시간에 메시지를 전달할 수 있습니다. 이 시간은 Braze가 결정합니다.

이 기능에 대한 업데이트는 다음을 포함합니다:
- **방해금지 시간에 대한 설명**: 방해금지 시간 기능은 동일하게 유지되지만, UI는 명확성을 위해 조정되었습니다.
- **미리보기 차트 추가**: 이제 Intelligent Timing을 사용하여 하루 중 각 시간에 메시지를 받을 사용자의 수와 최적의 시간을 계산할 수 있는 충분한 데이터를 가진 사용자의 비율을 확인할 수 있는 차트를 생성할 수 있습니다.
- **커스텀 대체 추가**: 이제 사용자가 최적의 시간을 계산하기에 충분한 인게이지먼트 데이터가 부족할 때 메시지를 보낼 현지 시간을 선택할 수 있습니다.

## Facebook 오디언스 내보내기

Braze는 Braze 세그먼트 페이지에서 사용자를 수동으로 내보내 Facebook 커스텀 오디언스를 생성할 수 있는 기능을 제공합니다. 이것은 일회성 정적 오디언스 내보내기이며 새 [Facebook 커스텀 오디언스]({{site.baseurl}}/partners/facebook/)만 생성됩니다.

현재 모든 클러스터에서 사용할 수 있는 새로운 Braze Facebook 오디언스 내보내기 프로세스가 있으며, 간단한 통합 단계로 프로세스를 간소화합니다. 더 이상 OAuth 리디렉션 URI를 화이트리스트에 추가하여 커스텀 오디언스를 전송하거나 Facebook 앱 설정 내에서 통합할 필요가 없습니다.

{% alert important %}
모든 클라이언트는 현재 Facebook 커스텀 오디언스를 사용하고 있으며, 새로운 단계로 Braze 세그먼트를 다시 통합해야 합니다.
{% endalert%}


## 콘텐츠 블록 및 이메일 템플릿 API 업데이트

[template/email/list]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) 및 [content_block/list]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) API 엔드포인트가 새로운 `tags` 필드를 포함하도록 업데이트되었습니다. 이 필드는 현재 블록 또는 이메일 템플릿에 적용되는 모든 태그를 배열로 나열합니다.

## 개인화된 from-address

Braze 내에서 이메일 메시지를 작성할 때, 이제 이메일 작성의 **보내기 정보** 섹션에서 메시지의 발신 주소를 개인화할 수 있습니다. 당사의 지원되는 [개인화 태그]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)를 사용할 수 있습니다

![맞춤 설정된 주소]({% image_buster /assets/img/personalized-from-name.png %}){: style="max-width:80%"}

