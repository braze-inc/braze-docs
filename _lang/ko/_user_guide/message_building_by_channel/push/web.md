---
nav_title: "웹 푸시"
article_title: 웹 푸시 알림
page_order: 8.5
page_type: reference
description: "이 참조 페이지에서는 웹 푸시 알림에 대해 간략하게 설명하고, 웹 푸시 알림을 만드는 데 필요한 단계로 연결되는 링크를 제공합니다."
platform: Web
channel:
  - push

---

# 웹 푸시

> Braze에서 웹 푸시 알림에 대해 알아보고 나만의 웹 푸시 알림을 만들기 위한 리소스를 찾아보세요.

웹 푸시는 웹 애플리케이션 사용자와 소통할 수 있는 또 다른 좋은 방법입니다. [지원되는 브라우저에서](#supported-browsers) 웹사이트를 방문하는 고객은 웹 페이지 로드 여부와 관계없이 웹 애플리케이션에서 웹 푸시를 수신하도록 옵트인할 수 있습니다.

## 개요

웹 푸시 알림은 긴급하고 실행 가능한 업데이트를 전달하여 빠른 전환을 유도합니다. 웹 푸시를 사용하면 다음이 가능합니다.

- 가격 하락과 같이 중요한 데이터가 변경되면 바로 메시지 트리거
- 간단한 클릭 유도 실행 버튼으로 웹사이트 방문을 유도
- 제품 및 고객 정보로 푸시를 개인화하여 메시지 관련성을 높입니다.

웹 푸시는 앱 푸시 알림이 휴대폰에서 작동하는 방식과 동일하게 작동합니다. For more information on composing a web push, check out [Creating a push notification]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message).

![Web push example with the same push message displayed on a laptop and phone.]({% image_buster /assets/img_archive/Macbook_Push.png %}){: style="border:none"}

## 잠재적 사용 사례

다음은 일반적인 웹 푸시 메시지 사용 사례의 몇 가지 예입니다.

| 사용 사례 | 설명 |
| --- | --- | 
| 무료 평가판 | 웹사이트의 신규 방문자가 무료 평가판에 등록하도록 유도하세요. 사용자에게 특별한 경험을 할 수 있는 기회를 제공함으로써 유료 고객으로 전환할 가능성을 높일 수 있습니다. |
| 앱 다운로드 | 웹 사용자를 모바일 앱으로 유도하여 제품에서 더 많은 가치를 얻을 수 있도록 하세요. 개인화를 활용하여 현재 인게이지먼트 패턴에 따라 앱의 혜택을 강조하는 것도 고려해 보세요. |
| 할인 및 세일 | 시간에 민감한 이벤트 및 프로모션에 대한 고객 인지도를 높입니다. 웹 푸시를 포함한 여러 채널에 메시지를 전달하여 브랜드 프로모션에 대한 인지도를 높일 수 있습니다. |
| 장바구니 포기 | 거래를 완료하지 않은 사용자에게 자동 리마인더를 전송하여 결제 흐름으로 돌아오도록 유도합니다. <br><br>Braze에서 실시한 연구에 따르면 웹 푸시가 이메일보다 53%, 모바일 푸시보다 23% 더 효과적이어서 수신자가 다시 돌아와 구매를 완료하도록 유도하는 데 더 큰 영향을 미칩니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 웹 푸시 사용을 위한 전제 조건

Braze를 사용하여 푸시 메시지를 생성하고 전송하려면 먼저 개발자와 협력하여 웹사이트에 푸시를 통합해야 합니다. For detailed steps, refer to our [Web push integration guide]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web).

### 푸시 권한

모든 브랜드는 웹 푸시 알림을 웹사이트에 통합하여 사용할 수 있습니다. 웹 브라우저가 열려 있는 한 현재 웹 방문자와 이전 웹 방문자 모두에게 알림을 보낼 수 있지만, 기존 모바일 앱 푸시와 마찬가지로 ]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-permission)방문자가 알림을 받으려면 옵트인해야]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-permission)합니다.

{% alert tip %}
[푸시 프라이머]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)라고도 하는 인브라우저 메시지를 사용하여 사용자가 웹 푸시를 옵트인하도록 유도하는 것이 좋습니다.
{% endalert %}

## 지원되는 브라우저

웹 푸시 알림을 지원하는 브라우저는 다음과 같습니다. 그러나 비공개 브라우징 창은 현재 웹 푸시를 지원하지 않습니다.

- Chrome(및 Android 모바일용 Chrome)
- Safari
- 파이어폭스(및 안드로이드 모바일용 파이어폭스)
- Opera
- Edge

푸시 프로토콜 표준 및 브라우저 지원에 대한 자세한 내용은 사용 중인 브라우저에 따른 리소스를 검토할 수 있습니다.

- [Safari(데스크톱)](https://developer.apple.com/notifications/safari-push-notifications/)
- [Safari (mobile)]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=safari)
- [Mozilla Firefox](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility)
- [Microsoft Edge](https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/how-to/push)


