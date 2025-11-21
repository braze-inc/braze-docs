---
nav_title: API 트리거 전달
article_title: API 트리거 전달
page_order: 2
page_type: reference
description: "이 참조 문서에서는 API 트리거 캠페인을 예약하고 설정하는 방법에 대해 설명합니다."
tool: Campaigns
platform: API

---

# API 트리거 전달

> API 트리거 캠페인 또는 서버 트리거 캠페인은 보다 고급 트랜잭션 사용 사례에 이상적입니다. API 트리거 캠페인을 통해 마케터는 Braze 대시보드 내에서 캠페인 카피, 다변량 테스트, 재자격 규칙을 관리하는 동시에 자체 서버와 시스템에서 해당 콘텐츠의 전달을 트리거할 수 있습니다. 메시지를 트리거하는 API 요청에는 메시지에 실시간으로 템플릿화할 추가 데이터가 포함될 수도 있습니다.

## API 트리거 캠페인 설정하기

API 트리거 캠페인 설정은 몇 단계만 거치면 됩니다. 먼저 새로운 멀티채널 또는 단일 채널 캠페인을 생성합니다(다변량 테스트 포함).

{% alert note %}
API 트리거 캠페인은 일반 [API 캠페인과]({{site.baseurl}}/developer_guide/rest_api/api_campaigns/#api-campaigns) 다릅니다.
{% endalert %}

그런 다음 예약된 알림과 동일한 방식으로 사본 및 알림을 구성하고 **API 트리거 전달을** 선택합니다. 서버에서 이러한 캠페인을 트리거하는 방법에 대한 자세한 내용은 [API 트리거 캠페인 전송]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) 문서를 참조하세요.

\![]({% image_buster /assets/img_archive/api_triggered_campaign_delivery.png %})

## API 요청에 포함된 템플릿 콘텐츠 사용

메시지를 트리거하는 것 외에도 `trigger_properties` 객체 내의 메시지에 템플릿을 지정할 API 요청과 함께 콘텐츠를 포함할 수도 있습니다. 이 콘텐츠는 메시지 본문에서 참조할 수 있습니다. 예를 들어 다음을 포함할 수 있습니다:
``{% raw %} {{ api_trigger_properties.${ some_value_included_with_request }}} {% endraw %}``. 자세한 내용은 다음 소셜 알림 예시를 참조하세요:

앞서 언급한 트리거 속성이 메시지에 포함되어 사용자 이름을 자동으로 채우고 그 뒤에 "좋아요를 누른 사진!"이라는 텍스트가 표시됩니다. 그들이 무엇을 하고 있는지 보려면 여기를 클릭하세요.".]({% image_buster /assets/img_archive/api_triggered_photo_social_example_1.png %}){: style="max-width:70%;"}

## API 트리거 캠페인을 통한 재자격 부여

재자격 설정을 사용하여 사용자가 API 트리거 캠페인을 수신하는 횟수를 제한할 수 있습니다. 즉, 사용자는 API 트리거가 몇 번 실행되든 상관없이 지정된 기간에 한 번 또는 한 번만 캠페인을 수신하게 됩니다.

예를 들어 API 트리거 캠페인을 사용하여 사용자가 최근에 본 항목에 대한 캠페인을 보낸다고 가정해 보겠습니다. 이 경우 각 항목에 대해 API 트리거를 실행하는 동안 조회한 항목 수에 관계없이 하루에 최대 한 개의 메시지만 보내도록 캠페인을 제한할 수 있습니다. 반면 API 트리거 캠페인이 트랜잭션인 경우 지연 시간을 0분으로 설정하여 사용자가 트랜잭션을 수행할 때마다 캠페인을 수신할 수 있도록 해야 합니다.

\![]({% image_buster /assets/img_archive/api_triggered_reeligible.png %})


