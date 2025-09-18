---
nav_title: 재고 있음
article_title: 재고 있음
page_order: 2
page_type: reference
description: "이 문서에서는 Braze 캔버스 템플릿을 사용하여 품목의 재입고 시 사용자에게 개인화된 메시지로 알림으로써 구매를 유도하는 방법에 대해 설명합니다."
tool: Canvas
---

# 재입고

> 품절 템플릿을 사용하여 이전에 품절되었지만 현재 구매 가능한 품목을 보거나 관심을 표명한 사용자를 대상으로 메시지를 작성할 수 있습니다. 이렇게 하면 제품이 재입고되는 중요한 순간에 사용자의 참여를 유도하여 원하는 제품을 구매할 수 있습니다.

이 문서에서는 사용자 라이프사이클의 전환 단계를 위해 설계된 **재고** 있음 템플릿의 사용 사례를 안내합니다. 완료되면 상품이 재입고되면 사용자에게 푸시(웹 또는 모바일), SMS 또는 이메일로 최대 2개의 알림을 전송하는 캔버스를 만들 수 있습니다.

## 필수 조건

이 템플릿을 성공적으로 사용하려면 다음이 필요합니다:

- 상품에 대한 정보가 포함된 [카탈로그]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog) 
- 사용자에게 메시지를 보내려는 품목에 대해 [품절 알림을]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/back_in_stock_notifications/#how-back-in-stock-notifications-work) 설정해야 합니다.

## 필요에 맞게 템플릿 조정하기

슬랙스, 청바지, 큐롯 및 기타 여러 종류의 바지를 전문으로 판매하는 소비자 직거래 의류 소매업체인 PantsLabyrinth에서 일한다고 가정해 보겠습니다. 재고 입고 템플릿을 사용하여 인기 청바지인 클래식 스트레이트 레그의 재고가 다시 입고되면 다양한 채널에서 고객에게 알릴 수 있습니다.

캔버스를 만들기 전에 스트레이트 레그 팬츠 재고에 대한 정보가 포함된 [카탈로그를 설정하고]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog) 클래식 스트레이트 레그 청바지에 대한 [품절 알림을 설정했습니다]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/back_in_stock_notifications/#setting-up-back-in-stock-notifications). 사용자가 앱에서 클래식 스트레이트 레그 청바지에 좋아요를 누르는 사용자 지정 이벤트를 수행한 후 알림을 구독하도록 만들었습니다.

재고가 있는 템플릿에 액세스하려면 새 캔버스를 만들 때 **캔버스 템플릿 사용** > **브레이즈 템플릿을** 선택합니다. 그런 다음 **재고 있음** 옆의 **템플릿 적용을** 선택합니다. 이제 템플릿을 검토하여 필요에 맞게 조정할 수 있습니다.

### 1단계: 세부 정보 설정

목표를 반영하도록 캔버스 세부 사항을 조정해 보겠습니다.

1. 템플릿 이름 옆의 **편집을** 선택합니다.

![캔버스의 현재 제목과 설명입니다.]({% image_buster /assets/img/canvas_templates/back_in_stock_old_name_description.png %}){: style="max-width:45%;"}

{:start="2"}
2\. 캔버스 이름을 업데이트하여 클래식 스트레이트 레그 제품이 재입고되면 해당 캔버스가 타겟팅 사용자용임을 명시합니다.
3\. 설명을 업데이트하여 이 캔버스에 개인화된 메시지가 포함되어 있음을 설명합니다.
4\. **프로모션** 태그 아래에 중첩된 **재고** 있음 태그를 추가하여 캔버스 홈 페이지에서 필터링할 수 있도록 합니다. 

!["Set Up Canvas Details" step with a Canvas name of "Back in Stock - Classic Straight Leg" and a brief Canvas description.]({% image_buster /assets/img/canvas_templates/back_in_stock_1.png %})

### 2단계: 전환 이벤트 할당

**기본 전환 이벤트 - A를** **특정 구매로** 변경하고 제품 이름으로 **클래식 스트레이트 레그를** 선택합니다.

!["Assign Conversion Events" section for the conversion event type of purchasing the Classic Straight Leg product with a conversion deadline of 7 days.]({% image_buster /assets/img/canvas_templates/back_in_stock_2.png %})

### 3단계: 참가 일정 맞춤 설정

입력 일정을 **액션 기반으로** 유지하여 사용자가 템플릿에서 이미 **재고 소진 이벤트 수행으로** 설정된 액션을 수행할 때 캔버스에 입력하도록 하겠습니다.

이 단계에서 두 가지를 조정하겠습니다:

1. '스트레이트 레그 팬츠'로 명명된 클래식 스트레이트 레그 청바지에 대한 정보가 포함된 카탈로그를 선택하세요. 

!["Entry Schedule" step for an action-based Canvas.]({% image_buster /assets/img/canvas_templates/back_in_stock_3.png %})

{: start="2"}
2\. **시작 시간(필수)** 을 원하는 시작 날짜와 시간으로 설정합니다.

!["Entry Window" section with a start time of January 2, 2025 at 12 am.]({% image_buster /assets/img/canvas_templates/back_in_stock_4.png %})

### 4단계: 타겟 오디언스 선택

타겟 고객을 클래식 스트레이트 레그 청바지를 구매할 가능성이 높다고 생각되는 사용자로 정의합니다.

1. 앱이나 웹사이트에서 클래식 스트레이트 레그 청바지를 즐겨찾은 사용자로 구성된 타겟 세그먼트인 '즐겨찾는 - 클래식 스트레이트 레그 청바지'를 선택합니다.
2. '청바지'를 "0" 번 이상 구매한 사용자를 포함하려면 필터를 선택합니다.

!["Target Audience" step with the segment of "Favorited - Classic Straight Leg Jeans".]({% image_buster /assets/img/canvas_templates/back_in_stock_5.png %})

{: start="3"}
3\. 사용자가 캔버스의 최대 지속 시간이 지난 후 캔버스에 다시 들어갈 수 있도록 항목 컨트롤을 조정하여 사용자가 동시에 같은 단계를 트리거할 가능성을 방지합니다.

!["Entry Controls" section with a checkbox for allowing users to re-enter this Canvas with a maximum duration of the Canvas.]({% image_buster /assets/img/canvas_templates/back_in_stock_6.png %})

{: start="4"}
4\. 클래식 스트레이트 레그 청바지에 싫어요를 누르는 사용자 지정 이벤트를 수행한 사용자를 제거하도록 종료 기준을 조정합니다.

!["Exit Criteria" section with a exception for users that perform the custom event of "Unfavorited".]({% image_buster /assets/img/canvas_templates/back_in_stock_7.png %})

### 5단계: 전송 설정을 선택하세요

기본 구독 설정을 유지하여 구독하거나 메시지 또는 알림 수신을 선택한 사용자에게만 전송하고 다른 설정(빈도 제한, 조용한 시간, 시드 그룹)은 건너뜁니다.

!["Send Settings" step targeting users who are subscribed or opted in.]({% image_buster /assets/img/canvas_templates/back_in_stock_8.png %})

### 6단계: 캔버스 사용자 지정

이제 사용자에게 전송할 채널과 콘텐츠를 사용자 지정하여 캔버스를 구축하겠습니다. 네 가지 템플릿 채널(모바일 및 웹 푸시, SMS, 이메일)을 모두 사용하고 있으며 [지능형 채널]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/) 필터를 사용하고 있으므로 추가하거나 제거할 필요가 없습니다.

{% alert tip %}
[캔버스 항목 속성을]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) 사용하여 참조하는 제품에 따라 캔버스의 메시지를 사용자 지정할 수 있습니다.
{% endalert %}

각 메시지 단계를 진행하여 콘텐츠를 업데이트하는 것으로 사용자 지정 작업을 시작하겠습니다.

1. `!!YOURCATALOGHERE!!` 을 카탈로그 이름("Straight_Leg_Pants")으로 바꿉니다.
2. `[0]` 을 클래식 스트레이트 레그 청바지의 색인 번호인 "9"로 대체합니다(해당 청바지는 `items` 카탈로그의 10번째 항목이므로 "9"입니다). (Liquid에서 배열은 영 인덱싱되므로 첫 번째 항목은 `1` 이 아닌 `0` 입니다.)
3. 나머지 모든 메시지 단계에 대해 1단계와 2단계를 반복합니다:
    - 하루 지연 후 전송되는 '제품 내 메시지 및 이메일' 메시지
    - 구매를 하지 않은 사용자에게 보내는 '푸시+이메일 알림' 메시지
4. **구매** 작업 그룹을 선택하여 작업 경로 단계를 업데이트합니다. 그런 다음 **특정 구매를** 선택하고 제품에 대해 클래식 스트레이트 레그 청바지를 선택합니다.

![Mobile Push Canvas step with a message notifying users that a product is back in stock.]({% image_buster /assets/img/canvas_templates/back_in_stock_9.png %})

### 7단계: 캔버스 테스트 및 실행

캔버스를 테스트하고 검토하여 예상대로 작동하는지 확인한 후 **캔버스 시작을** 선택하여 캔버스를 실행합니다. 이제 클래식 스트레이트 레그 청바지를 좋아하고 메시지 채널을 구독한 사용자들은 재입고 시 알림을 받게 됩니다!

{% alert tip %}
캔버스 출시 전후에 고려해야 할 사항은 [출시 전/후 체크리스트를]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) 확인하세요.
{% endalert %}

