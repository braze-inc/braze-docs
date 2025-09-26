---
nav_title: API 트리거 전달
article_title: API 트리거 전달
page_order: 2
page_type: reference
description: "이 참조 문서에서는 API로 트리거된 캠페인을 예약하고 설정하는 방법을 설명합니다."
tool: Campaigns
platform: API

---

# API-트리거된 전달

> API-트리거 캠페인 또는 서버-트리거 캠페인은 더 고급 트랜잭션 사용 사례에 이상적입니다. Braze API로 트리거된 캠페인은 마케터가 Braze 대시보드 내에서 캠페인 카피, 다변량 테스트 및 재적격성 규칙을 관리하면서 자체 서버 및 시스템에서 해당 콘텐츠의 전달을 트리거할 수 있도록 합니다. API 요청으로 메시지를 트리거할 때 실시간으로 메시지에 템플릿화할 추가 데이터를 포함할 수도 있습니다.

## API로 시작된 캠페인 설정

API로 트리거된 캠페인을 설정하는 데에는 몇 가지 단계가 필요합니다. 먼저, 새로운 다중 채널 또는 단일 채널 캠페인(다변량 테스트 포함)을 만드세요.

{% alert note %}
API로 시작된 캠페인은 [API 캠페인]({{site.baseurl}}/developer_guide/rest_api/api_campaigns/#api-campaigns)과 다릅니다.
{% endalert %}

다음으로, 예약된 알림에 대해 일반적으로 수행하는 것과 동일한 방식으로 복사본 및 알림을 구성하고 **API-Triggered Delivery**를 선택합니다. 이 서버에서 이러한 캠페인을 트리거하는 방법에 대한 자세한 내용은 이 [API로 트리거된 캠페인 전송]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) 기사를 참조하세요.

![]({% image_buster /assets/img_archive/api_triggered_campaign_delivery.png %})

## API 요청에 포함된 템플릿 콘텐츠 사용

메시지를 트리거하는 것 외에도 `trigger_properties` 객체 내에서 메시지로 템플릿화할 콘텐츠를 API 요청에 포함할 수 있습니다. 이 콘텐츠는 메시지 본문에서 참조할 수 있습니다. 예를 들어, 다음을 포함할 수 있습니다:
``{% raw %} {{ api_trigger_properties.${ some_value_included_with_request }}} {% endraw %}``. 다음 소셜 알림 예제를 추가 컨텍스트로 참조하세요:

![앞서 언급한 트리거 속성은 메시지에 포함되어 사용자의 이름을 자동으로 채운 후 다음 텍스트를 추가합니다: "님이 당신의 사진을 좋아합니다!" Click here to see what they've been up to.".]({% image_buster /assets/img_archive/api_triggered_photo_social_example_1.png %}){: style="max-width:70%;"}

## API로 트리거된 캠페인의 재적격성

사용자가 API로 트리거된 캠페인을 받는 횟수는 재적격성 설정을 사용하여 제한할 수 있습니다. 이것은 사용자가 API 트리거가 몇 번 실행되든 상관없이 캠페인을 한 번만 또는 주어진 기간 내에 한 번만 받게 됨을 의미합니다.

예를 들어, 사용자가 최근에 본 항목에 대한 캠페인을 보내기 위해 API로 트리거된 캠페인을 사용한다고 가정해 보겠습니다. 이 경우, 캠페인이 하루에 최대 한 개의 메시지를 보내도록 제한할 수 있으며, 각 항목에 대해 API 트리거를 실행하는 동안 그들이 본 항목의 수에 관계없이 메시지를 보낼 수 있습니다. 반면, API로 트리거된 캠페인이 트랜잭션인 경우, 지연 시간을 0분으로 설정하여 사용자가 트랜잭션을 할 때마다 캠페인을 받을 수 있도록 해야 합니다.

![]({% image_buster /assets/img_archive/api_triggered_reeligible.png %})


