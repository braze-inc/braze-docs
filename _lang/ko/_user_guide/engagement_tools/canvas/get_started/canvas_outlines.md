---
nav_title: 캔버스 개요
article_title: 캔버스 개요
page_order: 3
page_type: reference
description: "이 참고 문서에서는 네 가지 유용한 캔버스 사용 사례를 다룹니다."
tool: Canvas

---

# 캔버스 윤곽선

[![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/page/courses){: style="float:right;width:120px;border:0;" class="noimgborder"}

> 이 문서에서는 [지연]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) 및 [메시지]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) 단계를 조합하여 캔버스를 사용하여 타겟팅된 개인화된 메시징을 수행하는 방법을 보여주는 몇 가지 예를 중점적으로 설명합니다.

Braze 학습은 일반적인 캔버스 개요를 다루는 여러 전용 캔버스 강좌도 제공합니다. 동영상, 강의, 대화형 연습을 통해 기술 용어와 개념에 대한 유용한 인사이트를 얻을 수 있습니다. 
- [캔버스 플로우로 고객 여정 만들기](https://learning.braze.com/create-customer-journeys-with-canvas-flow)
- [신규 로열티 회원 온보딩](https://learning.braze.com/new-loyalty-member-onboarding)
- [휴면 사용자](https://learning.braze.com/lapsing-users)
- [유기한 장바구니 사용자 여정 구축하기](https://learning.braze.com/build-an-abandoned-cart-user-journey)

{% alert important %}
2023년 2월 28일부터 오리지널 캔버스 경험 환경에서는 더 이상 캔버스를 생성하거나 복제할 수 없습니다. Braze는 원래 캔버스 경험을 사용하는 고객이 캔버스 플로우로 이동할 것을 권장합니다. 향상된 편집 경험을 통해 캔버스를 더 잘 구축하고 관리할 수 있습니다. [캔버스를 캔버스 플로우에 복제하는 방법]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/)에 대해 자세히 알아보세요.
{% endalert %}

### 온보딩

레스토랑에서 온보드 사용자가 첫 예약을 할 수 있도록 지원하고자 한다고 가정해 보겠습니다. 이 캔버스는 온보딩을 위한 것이므로 모든 신규 고객의 세션이 시작될 때 캔버스를 시작하는 것이 가장 이상적입니다. 다이닝 고객에게 빠르고 효과적으로 다가가려면 SMS 메시지 채널을 사용하면 됩니다.

![]({% image_buster /assets/img_archive/canvas_outline_onboarding.png %}){: style="max-width:90%;"}

### 업셀

효과적인 캔버스를 제작하고 전송하여 구독을 상향 판매하도록 장려할 수도 있습니다. 예를 들어 무료 버전의 앱을 사용 중인 활성 사용자를 업그레이드하려는 경우, 고객이 '3시간 스트리밍' 사용자 지정 이벤트에 도달하면 트리거되도록 액션 기반 캔버스를 만들 수 있습니다. 메시지 단계를 사용하여 이러한 고객에게 프리미엄 구독에 가입하라는 메시지를 표시할 수 있습니다.

![]({% image_buster /assets/img_archive/canvas_outline_upsell.png %}){: style="max-width:90%;"}

### 버려진 카트

리테일 비즈니스는 종종 고객에게 불완전한 구매를 상기시켜야 하는 상황에 처할 수 있습니다. 실행 기반 캔버스를 사용하면 등록된 모든 고객에게 유기한 장바구니에 있는 품목을 구매하도록 알림을 보낼 수 있습니다. 지연 시간을 달리하여 고객이 메시지를 얼마나 잘 받아들일지 테스트할 수도 있습니다.

![]({% image_buster /assets/img_archive/canvas_outline_cart.png %}){: style="max-width:90%;"}

### 고객 리소스

캔버스를 사용하여 고객에게 리소스를 교육할 수 있습니다. 예를 들어, 항공사 비즈니스의 경우 3일 후 여행을 예약한 고객에게 항공편 정보와 관련 공항 FAQ가 포함된 이메일을 매주 예약하여 예약을 유도하는 캔버스를 만들 수 있습니다.

![]({% image_buster /assets/img_archive/canvas_outline_resource.png %}){: style="max-width:90%;"}
