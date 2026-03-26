---
nav_title: 재입고
article_title: 재고 있음
page_order: 2
page_type: reference
description: "이 문서에서는 Braze Canvas 템플릿을 사용하여 사용자가 품목이 재고에 들어왔을 때 개인화된 메시지로 구매를 유도하는 방법을 설명합니다."
tool: Canvas
---

# 재입고

> 재고가 다시 들어온 템플릿을 사용하여 이전에 품목을 본 적이 있거나 관심을 표현한 사용자에게 메시지를 생성합니다. 이 품목은 품절되었지만 이제 구매할 수 있습니다. 이는 사용자가 제품이 다시 이용 가능해질 때 중요한 순간에 참여하여 원하는 제품을 얻을 수 있도록 도와줍니다.

이 문서에서는 사용자 생애 주기의 전환 단계에 맞춰 설계된 **재고 복구** 템플릿의 사용 사례를 안내합니다. 작업이 완료되면 품목이 재고에 들어올 때 사용자에게 푸시(웹 또는 모바일), SMS 또는 이메일을 보내고 최대 두 번의 알림을 보내는 Canvas를 생성하게 됩니다.

## 필수 조건

이 템플릿을 성공적으로 사용하려면 다음이 필요합니다:

- 귀하의 품목에 대한 정보가 포함된 [카탈로그]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog)
- 사용자에게 메시지를 보내고자 하는 품목에 대해 [재고 복구 알림]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/#how-back-in-stock-notifications-work)을 설정해야 합니다.

## 필요에 맞게 템플릿 조정하기

우리는 바지, 청바지, 큘롯 및 기타 여러 종류의 바지를 전문으로 하는 직접 소비자 의류 소매업체인 PantsLabyrinth에서 일하고 있다고 가정해 보겠습니다. 우리는 재고가 다시 들어올 때 인기 있는 청바지인 Classic Straight Leg에 대해 다양한 채널에서 고객에게 알리기 위해 재고 복구 템플릿을 사용할 수 있습니다.

Canvas를 만들기 전에 [카탈로그 설정]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog)을 통해 우리의 스트레이트 레그 바지 재고에 대한 정보를 포함하고 [재고 복구 알림 설정]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/#setting-up-back-in-stock-notifications)을 Classic Straight Leg 청바지에 대해 설정했습니다. 사용자가 앱에서 Classic Straight Leg 청바지를 즐겨찾기하는 사용자 정의 이벤트를 수행한 후 알림을 구독하도록 설정했습니다.

재고 복구 템플릿에 접근하려면 새 Canvas를 만들 때 **Canvas 템플릿 사용** > **Braze 템플릿**을 선택합니다. 그런 다음 **재고 복구** 옆에서 **템플릿 적용**을 선택합니다. 이제 템플릿을 검토하여 필요에 맞게 조정할 수 있습니다.

### 1단계: 세부 정보 설정

목표를 반영하도록 캔버스 세부 사항을 조정해 보겠습니다.

1. 템플릿 이름 옆의 **편집을** 선택합니다.

![Canvas의 현재 제목 및 설명.]({% image_buster /assets/img/canvas_templates/back_in_stock_old_name_description.png %}){: style="max-width:45%;"}

{:start="2"}
2\. Canvas 이름을 업데이트하여 Canvas가 우리의 제품 Classic Straight Leg가 재고에 들어올 때 사용자를 타겟팅하기 위한 것임을 명시합니다.
3\. 설명을 업데이트하여 이 캔버스에 개인화된 메시지가 포함되어 있음을 설명합니다.
4\. 태그 **재고 복구**를 추가하여 태그 **프로모션** 아래에 중첩되도록 하여 Canvas 홈 페이지에서 필터링할 수 있도록 합니다. 

!["Canvas 세부정보 설정" 단계에서 "재고 복구 - Classic Straight Leg"라는 Canvas 이름과 간단한 Canvas 설명을 설정합니다.]({% image_buster /assets/img/canvas_templates/back_in_stock_1.png %})

### 2단계: 전환 이벤트 할당

**주요 전환 이벤트 - A**를 **특정 구매하기**로 변경하고 제품 이름으로 **Classic Straight Leg**을 선택합니다.

!["전환 이벤트 할당" 섹션에서 Classic Straight Leg 제품 구매의 전환 이벤트 유형과 7일의 전환 마감일을 설정합니다.]({% image_buster /assets/img/canvas_templates/back_in_stock_2.png %})

### 3단계: 참가 일정 맞춤 설정

사용자가 작업을 수행할 때 Canvas에 들어올 수 있도록 **작업 기반**으로 진입 일정을 유지합시다. 템플릿은 이미 **재고 복구 이벤트 수행**로 설정되어 있습니다.

이 단계에 두 가지 조정을 하겠습니다:

1. 우리의 클래식 스트레이트 레그 청바지에 대한 정보가 포함된 카탈로그를 선택합니다. 이 청바지는 "스트레이트 레그 팬츠"라고 명명했습니다. 

!["액션 기반 캔버스의 '입력 일정' 단계.]({% image_buster /assets/img/canvas_templates/back_in_stock_3.png %})

{: start="2"}
2\. 원하는 시작 날짜와 시간으로 **시작 시간 (필수)**를 설정합니다.

!["시작 시간이 2025년 1월 2일 오전 12시로 설정된 '참가 기간' 섹션입니다.]({% image_buster /assets/img/canvas_templates/back_in_stock_4.png %})

### 4단계: 타겟 오디언스 선택

우리의 목표 청중을 클래식 스트레이트 레그 청바지를 구매할 가능성이 더 높은 사용자로 정의하겠습니다.

1. 우리의 목표 세그먼트인 "즐겨찾기 - 클래식 스트레이트 레그 청바지"를 선택합니다. 이 세그먼트는 앱이나 웹사이트에서 클래식 스트레이트 레그 청바지를 즐겨찾기한 사용자로 구성됩니다.
2. "청바지"를 "0"회 이상 구매한 사용자를 포함하는 필터를 선택합니다.

!["타겟 오디언스" 단계에서 "즐겨찾기 - 클래식 스트레이트 레그 청바지" 세그먼트를 사용합니다.]({% image_buster /assets/img/canvas_templates/back_in_stock_5.png %})

{: start="3"}
3\. 사용자가 캔버스의 최대 지속 시간 후에 캔버스에 다시 들어갈 수 있도록 진입 제어를 조정하여 사용자가 동일한 단계를 동시에 트리거할 가능성을 방지합니다.

!["진입 제어" 섹션에서 사용자가 이 캔버스에 다시 들어갈 수 있도록 하는 체크박스를 추가합니다. 캔버스의 최대 지속 시간이 있습니다.]({% image_buster /assets/img/canvas_templates/back_in_stock_6.png %})

{: start="4"}
4\. 사용자가 클래식 스트레이트 레그 청바지를 즐겨찾기 해제하는 사용자 정의 이벤트를 수행한 경우 사용자를 제거하도록 종료 기준을 조정합니다.

!["종료 기준" 섹션에서 "즐겨찾기 해제" 사용자 정의 이벤트를 수행하는 사용자에 대한 예외를 추가합니다.]({% image_buster /assets/img/canvas_templates/back_in_stock_7.png %})

### 5단계: 전송 설정을 선택하세요

기본 구독 설정을 유지하여 구독하거나 메시지 또는 알림 수신을 선택한 사용자에게만 전송하고 다른 설정(빈도 제한, 조용한 시간, 시드 그룹)은 건너뜁니다.

!["전송 설정" 단계에서 구독하거나 선택한 사용자를 타겟팅합니다.]({% image_buster /assets/img/canvas_templates/back_in_stock_8.png %})

### Step 6: 캔버스 사용자 지정

이제 사용자에게 전송할 채널과 콘텐츠를 사용자 지정하여 캔버스를 구축하겠습니다. 모바일 및 웹 푸시, SMS, 이메일의 네 가지 템플릿 채널을 모두 사용하고 [인텔리전트 채널]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/) 필터를 사용하고 있으므로 추가하거나 제거할 필요가 없습니다.

{% alert tip %}
어떤 제품을 참조하는지에 따라 캔버스의 메시지를 사용자 정의하기 위해 [캔버스 진입 속성]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/)를 사용할 수 있습니다.
{% endalert %}

각 메시지 단계를 통해 내용을 업데이트하여 사용자 정의를 시작하겠습니다.

1. `!!YOURCATALOGHERE!!`을(를) 우리의 카탈로그 이름 (“Straight_Leg_Pants”).로 교체합니다.
2. `[0]`을(를) 클래식 스트레이트 레그 청바지의 인덱스 번호로 교체합니다. 이 번호는 "9"입니다. 왜냐하면 청바지가 카탈로그의 `items` 배열에서 열 번째 항목이기 때문입니다. (배열은 Liquid에서 0부터 시작하므로 첫 번째 항목은 `0`이고 `1`가 아닙니다.)
3. 모든 나머지 메시지 단계에 대해 1단계와 2단계를 반복합니다. 포함된 항목은 다음과 같습니다:
    - 하루 지연 후에 전송되는 "제품 내 메시지 & 이메일" 메시지
    - 구매를 하지 않은 사용자에게 전송되는 "푸시+이메일 알림" 메시지
4. **구매** 작업 그룹을 선택하여 작업 경로 단계를 업데이트합니다. 그런 다음 **특정 구매하기**를 선택하고 제품으로 클래식 스트레이트 레그 청바지를 선택합니다.

![모바일 푸시 캔버스 단계에서 제품이 재고에 다시 들어왔음을 알리는 메시지를 사용자에게 보냅니다.]({% image_buster /assets/img/canvas_templates/back_in_stock_9.png %})

### 7단계: 캔버스 테스트 및 실행

캔버스를 테스트하고 검토하여 예상대로 작동하는지 확인한 후 **캔버스 시작을** 선택하여 캔버스를 실행합니다. 이제 클래식 스트레이트 레그 청바지를 즐겨찾기하고 메시징 채널에 구독한 사용자에게 재고가 다시 들어왔을 때 알림이 전송됩니다!

{% alert tip %}
캔버스 출시 전후에 고려해야 할 사항은 [출시 전/후 체크리스트를]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) 확인하세요.
{% endalert %}

