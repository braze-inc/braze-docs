---
nav_title: 모범 사례
article_title: WhatsApp 모범 사례
page_order: 9
description: "이 문서에서는 WhatsApp 메시징 채널을 사용할 때의 권장 모범 사례를 설명하며, 높은 전화 품질 등급을 유지하고 차단 및 신고 비율을 낮추는 방법을 포함합니다."
page_type: reference
channel:
  - WhatsApp
 
---
# WhatsApp 모범 사례

> WhatsApp 메시지를 보내기 전에 높은 전화 품질 등급을 유지하고 차단 및 신고를 피하며 사용자에게 옵트인 및 옵트아웃하는 방법에 대한 권장 모범 사례를 참조하십시오.

## 높은 전화 품질 등급 유지 

WhatsApp은 사용자가 귀하의 메시지를 수신할 때 취하는 행동(예: 귀하의 비즈니스를 차단하거나 신고하는 것)을 기반으로 [전화 품질 등급](https://www.facebook.com/business/help/896873687365001)을 결정합니다. 높은 품질 등급을 유지하는 것이 중요합니다. 낮은 품질 등급이 일정 시간 동안 개선되지 않으면 메시징 한도가 감소할 수 있습니다.

WhatsApp에서 사용자에게 처음 메시지를 보낼 때 이러한 옵션이 메시지 스레드 내에 표시됩니다.

\![차단 또는 비즈니스를 신고할 수 있는 옵션이 있는 WhatsApp 메시지 스레드]({% image_buster /assets/img/whatsapp/whatsapp_block_report.png %}){: style="max-width:30%;"}

{% alert note %}
차단 및 신고에 대한 메트릭을 보려면 WhatsApp 관리자에서 [인사이트 탭](https://www.facebook.com/business/help/683499390267496)이 켜져 있는지 확인하십시오.
{% endalert %}

차단 및 신고 비율을 낮추기 위해 Braze는 높은 전화 품질 등급과 안정적인 메시징 한도를 유지하기 위한 다음의 모범 사례를 제안합니다. 

### WhatsApp 옵트인 요구 사항 및 가이드라인 준수

WhatsApp에서 사용자와 소통을 시작하기 전에 모든 사용자가 WhatsApp 메시지를 수신하는 데 적극적으로 동의했는지 확인하십시오. 사용자에게 옵트인 요청 시, 사용자는 귀하의 비즈니스로부터 WhatsApp을 통해 메시지를 수신하는 데 동의하고 있다는 것을 명확히 알려야 합니다.

{% alert note %}
옵트인 요구 사항 및 유용한 팁에 대한 정보는 [WhatsApp에 대한 옵트인 받기](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/)를 참조하십시오.
{% endalert %}

### 메시징 모범 사례 준수

- 사용자가 메시지가 귀하로부터 온 것임을 인식할 수 있도록 채널 이름이 귀하의 브랜드를 반영하도록 하십시오. 스팸이 아닙니다.
- 사용자의 옵트인 동의를 수집한 후 확인 메시지를 전송하세요.
- 적절한 시간에 메시지를 전송하세요.

### 고객에게 옵트아웃 옵션을 제공하세요.

옵트아웃은 전화 품질 평가에 영향을 미치지 않으므로 사용자가 WhatsApp 통신 수신을 차단하거나 신고하는 것보다 옵트아웃하는 것이 더 좋습니다.

제안된 모범 사례는 사용자가 수신하는 첫 번째 메시지의 바닥글에 옵트아웃 방법에 대한 지침을 제공하는 것입니다. 예를 들어, 사용자가 옵트아웃 트리거 단어로 응답하여 WhatsApp 채널에서 구독 취소할 수 있다고 명시할 수 있습니다. 향후 캠페인에서도 정기적으로 옵트아웃 바닥글을 포함할 수 있습니다. 이 설정 방법을 배우려면 [옵트인 및 옵트아웃]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/)을 참조하세요.
 
\![채널에서 구독 취소를 위해 STOP으로 응답하라는 바닥글이 있는 WhatsApp 메시지]({% image_buster /assets/img/whatsapp/whatsapp_unsubscribe.png %}){: style="max-width:35%;"}.

