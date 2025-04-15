---
nav_title: Intelligence Suite
article_title: Intelligence Suite
page_order: 10
layout: dev_guide
search_rank: 12
guide_top_header: "Intelligence Suite"
guide_top_text: "Braze Intelligence Suite는 데이터 기반 인사이트로 의사 결정을 자동화하는 데 도움을 줍니다. 전달 시간부터 다변량 테스트까지, 브랜드는 이러한 도구와 기능을 사용하여 대규모로 최적화되는 동적 크로스채널 경험을 만들 수 있습니다. <br> <br> Intelligence Suite는 세 가지 주요 기능으로 구성되어 있습니다. 바로 Intelligent Timing, 인텔리전트 채널, 지능형 선택입니다."
description: "Braze Intelligence Suite는 데이터 기반 인사이트로 의사 결정을 자동화하는 데 도움을 줍니다. 전달 시간부터 다변량 테스트까지, 브랜드는 이러한 도구와 기능을 사용하여 대규모로 최적화되는 동적 크로스채널 경험을 만들 수 있습니다."

Tool:
  - Dashboard

guide_featured_title: "도구 및 기능"
guide_featured_list:
- name: Intelligent Timing
  link: /docs/user_guide/brazeai/intelligence/intelligent_timing/
  image: /assets/img/braze_icons/clock.svg
- name: 인텔리전트 채널
  link: /docs/user_guide/brazeai/intelligence/intelligent_channel/
  image: /assets/img/braze_icons/mail-04.svg
- name: 지능형 선택
  link: /docs/user_guide/brazeai/intelligence/intelligent_selection/
  image: /assets/img/braze_icons/hearts.svg

guide_menu_title: "Additional resources"
guide_menu_list:
- name: 지능 FAQ
  link: /docs/user_guide/brazeai/intelligence/faqs/
  image: /assets/img/braze_icons/annotation-question.svg


---

## 사용 사례

Intelligence Suite는 사용자 기록과 캠페인 및 캔버스 성과를 분석하는 강력한 기능을 제공하며, 참여, 시청률 및 전환을 증가시키기 위해 자동으로 조정합니다. 다양한 산업에서 이러한 기능이 어떻게 이점을 제공할 수 있는지에 대한 몇 가지 예를 보려면 아래의 사용 사례를 참조하세요.

### eCommerce

- **반짝 세일:** [인텔리전트 채널 필터]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/)를 사용하여 사용자 기록을 연구하고 푸시 알림에 더 잘 반응하는 사용자와 이메일에 더 잘 반응하는 사용자를 식별한 다음, 해당 사용자에게 푸시 알림과 이메일을 보냅니다. 선택적으로, 사용자가 선호하는 채널을 결정하기에 충분한 데이터가 없는 경우 특정 채널을 선택하세요.
- **홍보 배너:** [지능형 선택]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/)을 사용하여 반복 캠페인에서 다양한 홍보 배너의 성능을 분석한 다음, 가장 높은 클릭률을 생성하는 배너를 자동으로 선택하고 전송합니다.

### 여행

- **패키지 제공:** 지능형 선택을 사용하여 반복 캔버스에서 다양한 여행 패키지 제안을 테스트하고, 가장 성과가 좋은 배리언트로 캔버스 트래픽을 점진적으로 전환하여 더 높은 예약률을 유도하세요.
- **여행 상품:** 인텔리전트 채널 필터를 사용하여 사용자의 가장 활발한 채널(이메일 또는 SMS 등)을 통해 개인화된 여행 상품을 보내 메시징에 대한 참여 가능성을 극대화하세요.

### 엔터테인먼트

- **새로운 콘텐츠 홍보:** 사용자들이 메시징을 열 가능성이 가장 높을 때 [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/)을 사용하여 새로운 영화, 쇼, 음악 및 기타 유형의 콘텐츠에 대한 알림을 보내세요.
- **게임 내 구매:** 지능형 선택을 사용하여 인게임 구매를 위한 다양한 프로모션 메시지를 테스트하고 가장 높은 전환율을 생성하는 메시지를 자동으로 선택하세요.

### 퀵 서비스 레스토랑

SandwichEmperor는 패스트푸드 레스토랑에서 일한다고 가정해봅시다. 이 레스토랑은 새로운 한정 메뉴 아이템인 로열 로스트를 제공합니다. 캔버스에서 개인화된 프로모션을 보내기 위해 두 가지 Intelligence Suite 기능을 사용합니다.

#### 알림을 보낼 시기를 위해 Intelligent Timing을 사용하세요

Intelligent Timing을 사용하여 앱 및 각 메시징 채널에서 사용자의 과거 상호작용을 분석한 다음 각 사용자에게 Royal Roast를 홍보할 최적의 시간을 자동으로 선택할 것입니다. 일부 사용자는 오후에 프로모션을 받을 수 있고, 다른 사용자는 저녁에 받을 수 있습니다. 

사용자에게 분석할 과거 상호작용이 충분하지 않은 경우 대체 시간을 제공합니다: 모든 사용자 중 앱을 사용하는 가장 인기 있는 시간입니다.

![Intelligent Timing 전달 설정 메시지 단계.][1]

#### 지능형 선택을 사용하여 프로모션을 선택하세요

실제 프로모션 메시지의 경우, Royal Roast에 대해 세 가지 다른 메시지(푸시 알림, 이메일 및 SMS)를 테스트하기 위해 지능형 선택을 사용할 것입니다. 지능형 선택은 하루에 두 번 모든 프로모션 메시지의 성과를 분석한 후, 가장 성과가 좋은 메시지를 점진적으로 더 많이 보내고 다른 메시지는 덜 보냅니다.

지능형 선택이 최상의 성과를 내는 메시지를 결정하기에 충분한 데이터를 수집한 후, 향후 발송의 100%에 해당 메시지를 사용할 것입니다.

![캔버스의 A/B 테스트 섹션에서 지능형 선택이 활성화되었습니다.][3]

#### 캔버스 시작

Intelligent Timing과 지능형 선택을 모두 사용하여 Royal Roast 프로모션이 타이밍과 메시징에 최적화되도록 설정했습니다. 캔버스를 시작하고 우리의 전송이 사용자 선호에 맞게 조정되는 것을 지켜볼 수 있습니다.

[1]: {% image_buster /assets/img/intelligence_suite1.png %}
[3]: {% image_buster /assets/img/intelligent_selection_canvas.png %}
