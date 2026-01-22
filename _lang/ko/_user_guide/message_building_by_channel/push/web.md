---
nav_title: "웹 푸시"
article_title: 웹 푸시 알림
page_order: 8.5
page_type: reference
description: "이 참조 페이지는 웹 푸시 알림에 대해 간략하게 설명하고, 이를 생성하기 위한 필요한 단계로 연결됩니다."
platform: Web
channel:
  - push

---

# 웹 푸시

> Braze에서 웹 푸시 알림에 대해 배우고, 자신만의 알림을 생성하기 위한 리소스를 찾으세요.

웹 푸시는 웹 애플리케이션 사용자와 소통하는 또 다른 훌륭한 방법입니다. [지원되는 브라우저](#supported-browsers)에서 귀하의 웹사이트를 방문하는 고객은 웹 페이지가 로드되었는지 여부에 관계없이 귀하의 웹 애플리케이션에서 웹 푸시를 수신하도록 선택할 수 있습니다.

## 개요

웹 푸시 알림은 긴급하고 실행 가능한 업데이트를 제공하여 빠른 전환을 유도합니다. 웹 푸시를 사용하면 다음을 수행할 수 있습니다:

- 중요한 데이터가 변경될 때 메시지를 즉시 전송합니다. 예를 들어 가격이 하락할 때.
- 간단한 클릭 유도 버튼으로 사람들을 귀하의 웹사이트로 다시 유도합니다.
- 제품 및 고객 정보를 사용하여 푸시를 개인화하여 메시지를 관련성 있게 만듭니다.

웹 푸시는 귀하의 전화에서 앱 푸시 알림이 작동하는 방식과 동일하게 작동합니다. 웹 푸시 작성에 대한 자세한 정보는 [푸시 알림 만들기]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message)를 확인하세요.

\![노트북과 전화에서 동일한 푸시 메시지가 표시된 웹 푸시 예시.]({% image_buster /assets/img_archive/Macbook_Push.png %}){: style="border:none"}

## 잠재적 사용 사례

여기 일반적인 웹 푸시 메시지 사용 사례의 몇 가지 예가 있습니다.

| 사용 사례 | 설명 |
| --- | --- | 
| 무료 체험 | 웹사이트의 새로운 방문자에게 무료 체험에 가입하도록 권장하세요. 사용자에게 특별한 점을 경험할 기회를 제공함으로써, 그들이 유료 고객이 될 가능성을 높일 수 있습니다. |
| 앱 다운로드 | 웹 사용자를 모바일 앱으로 유도하여 제품에서 더 많은 가치를 얻도록 도와주세요. 개인화를 활용하여 현재의 참여 패턴에 따라 앱의 이점을 강조하는 것을 고려하세요. |
| 할인 및 세일 | 시간에 민감한 이벤트와 프로모션에 대한 고객 인식을 높이세요. 웹 푸시를 포함한 여러 채널을 통해 메시지를 전달하여 브랜드 프로모션에 대한 인식을 높이세요. |
| 장바구니 포기 | 거래를 완료하지 않은 사용자에게 자동 알림을 보내어 체크아웃 흐름으로 다시 유도하세요. <br><br>Braze에서 실시한 연구에 따르면, 웹 푸시는 이메일보다 53% 더 효과적이며, 모바일 푸시보다 23% 더 영향력이 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 웹 푸시를 사용하기 위한 전제 조건

Braze를 사용하여 푸시 메시지를 생성하고 보내기 전에, 개발자와 협력하여 웹사이트에 푸시를 통합해야 합니다. 자세한 단계는 [웹 푸시 통합 가이드]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)를 참조하세요.

### 푸시 권한

모든 브랜드는 웹사이트에서 웹 푸시 알림을 통합하고 사용할 수 있습니다. 알림은 현재 및 이전 웹 방문자에게 도달할 수 있으며, 웹 브라우저가 열려 있는 한 가능합니다. 그러나 방문자는 [알림 수신에 동의해야 합니다]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-permission)—전통적인 모바일 앱 푸시와 마찬가지로.

{% alert tip %}
웹 푸시에 대한 동의를 유도하기 위해 브라우저 내 메시지를 사용하는 것을 고려하세요. 이는 [푸시 프라이머]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)로도 알려져 있습니다.
{% endalert %}

## 지원되는 브라우저

다음 브라우저는 웹 푸시 알림을 지원합니다. 그러나 개인 브라우징 창은 현재 웹 푸시를 지원하지 않습니다.

- Chrome (및 Chrome for Android 모바일)
- Safari
- Firefox (및 Firefox for Android 모바일)
- Opera
- Edge

푸시 프로토콜 표준 및 브라우저 지원에 대한 자세한 정보는 사용 중인 브라우저를 기반으로 한 리소스를 검토할 수 있습니다:

- [사파리 (데스크탑)](https://developer.apple.com/notifications/safari-push-notifications/)
- [사파리 (모바일)]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=safari)
- [모질라 파이어폭스](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility)
- [마이크로소프트 엣지](https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/how-to/push)


