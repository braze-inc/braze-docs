---
nav_title: 선택
article_title: 선택
page_order: 5
description: "이 참조 문서에서는 카탈로그를 사용하여 Braze 캠페인에서 데이터를 참조하기 위해 선택 항목을 생성하고 사용하는 방법을 다룹니다."
---

# 선택

> 선택 항목은 캠페인에서 각 사용자에게 메시지를 개인화하는 데 사용할 수 있는 데이터 그룹입니다. 선택을 사용할 때, 본질적으로 카탈로그의 특정 열을 기반으로 커스텀 필터를 설정하는 것입니다. 여기에는 브랜드, 크기, 위치, 추가된 날짜 등을 위한 필터가 포함될 수 있습니다. 이것은 항목이 먼저 충족해야 하는 기준을 정의할 수 있도록 함으로써 사용자에게 표시하는 내용을 제어할 수 있게 해줍니다.<br><br>This page covers how to create and use selections with your catalogs.

After creating a [catalog]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/), you can further reference your catalog data by incorporating selections in your Braze campaigns or recommendations.

![예제 카탈로그의 선택 섹션.]({% image_buster /assets/img_archive/catalog_selections1.png %})

## 알아야 할 사항

- 카탈로그당 최대 30개의 선택 항목을 만들 수 있습니다.
- 선택당 최대 10개의 필터를 추가할 수 있습니다.
- 선택은 Braze 카탈로그 데이터에서 추천을 세분화하는 데 좋습니다. If you're looking for inspiration, check out [About item recommendations]({{site.baseurl}}/user_guide/brazeai/recommendations/) for example use cases.

## 선택 만들기

선택을 만들려면 다음을 수행하십시오.

1. **카탈로그**로 이동하여 목록에서 카탈로그를 선택하십시오.
2. **선택** 탭을 선택하고 **선택 만들기**를 클릭합니다.
3. 선택 항목에 이름과 선택적 설명을 지정하십시오.
4. **필터 필드**에서 필터링할 카탈로그 열을 선택합니다. 1,000자 이상의 문자열 필드는 필터에 선택할 수 없습니다.
5. 필터 기준을 정의하려면 관련 연산자(예: "같음" 또는 "같지 않음") 및 속성을 선택하세요.
6. **정렬 유형** 섹션에서 결과가 정렬되는 방식을 결정합니다. 기본값으로, 결과는 특정한 순서 없이 반환됩니다. 특정 필드로 정렬을 지정하려면 **정렬 순서 무작위화**를 끄고 **정렬 필드** 및 **정렬 순서**(오름차순 또는 내림차순)을 지정하십시오.
7. **결과 제한** 섹션에 결과를 입력하세요(최대 50개).
8. **선택 만들기**.

### 테스트 및 미리보기

선택을 만든 후, **미리보기 사용자** 섹션을 사용하여 선택이 무작위 사용자 또는 특정 사용자에게 반환할 내용을 볼 수 있습니다. 개인화를 사용하는 선택의 경우, 사용자를 선택한 후에만 미리보기를 볼 수 있습니다.

### Liquid 선택 결과

카탈로그에서 커스텀 속성 및 커스텀 이벤트와 같은 Liquid을(를) 사용하는 경우 선택한 각 사용자에 대해 반환되는 결과가 다를 수 있습니다. 

{% alert note %}
연결된 콘텐츠 Liquid는 이러한 필터 설정에서 지원되지 않습니다.
{% endalert %}

![속성이 Liquid 커스텀 속성으로 설정된 카탈로그 선택을 위한 필터 설정.]({% image_buster /assets/img_archive/catalog_selections7.png %})

## 메시징에서 선택 사용

선택을 만든 후, Liquid을 사용하여 해당 카탈로그에서 필터링된 항목을 삽입하여 메시지를 개인화하세요. 메시지 작성기에서 찾을 수 있는 개인화 창에서 Braze가 Liquid를 생성하도록 할 수 있습니다.

1. In any message composers that support personalization, select <i class="fa-solid fa-circle-plus" style="color: #12aec5;" title="Add personalization"></i> to open the personalization window.
2. **개인화 유형**의 경우 **카탈로그 항목**을 선택하십시오.
3. 카탈로그 이름을 선택하세요.
4. **항목 선택 방법**에서 **선택 사용**을 선택합니다.
4. 목록에서 선택 항목을 선택하십시오.
5. **표시할 정보**에 대해 카탈로그에서 각 항목에 포함할 필드를 선택하십시오.
6. Select the **Copy** icon and paste the Liquid wherever it needs to go in your message.

![다음 선택 항목이 있는 개인화 모달 추가: "개인화 유형"에 대한 "카탈로그 항목", "카탈로그 이름"에 대한 "게임", "선택 유형"에 대한 "선택", "선택"에 대한 "game_selection", "표시할 정보"에 대한 "title" 및 "description_en".]({% image_buster /assets/img_archive/catalog_selections6.png %}){: style="max-width:70%;"}

## 사용 사례

예를 들어, 귀하가 식사 전달 서비스을 운영하고 있으며 가장 최근에 본 음식 카테고리를 기반으로 특정 식사 선호도를 가진 사용자에게 개인화된 메시지를 보내고 싶다고 가정해 보겠습니다. 

식사 이름, 가격, 이미지 및 식사 카테고리에 대한 식사 배달 서비스의 정보를 포함한 카탈로그를 사용하여 사용자가 가장 최근에 본 카테고리를 기반으로 세 가지 식사를 추천하는 선택을 만들 수 있습니다.

![식사 전달 서비스에 대한 선택의 예는 두 가지 필터가 있습니다. 하나는 제품 유형을 식사로 식별하고, 다른 하나는 카테고리를 가장 최근에 본 것으로 식별합니다. 선택은 세 가지 결과가 반환되는 순서를 무작위로 설정합니다.]({% image_buster /assets/img_archive/catalog_selections2.png %}){: style="max-width:90%;"}

캠페인에서 이 카탈로그와 선택 항목을 사용하려면 캠페인 작성의 메시지 구성 섹션에서 **개인화 추가** 모달을 사용하십시오. 이 예에서 식사 전달 서비스 정보가 포함된 카탈로그와 가장 최근에 본 카테고리를 기반으로 한 식사 추천 선택을 선택했습니다. 이를 통해 식사 이름과 가격을 표시할 수 있습니다. 메시지를 더욱 구축하려면 선택 항목을 사용하여 첫 번째 추천 식사의 이미지를 추가할 수도 있습니다.

!["이 고평가된 식사를 사랑하게 될 것입니다!"라는 헤더가 있는 콘텐츠 카드와 메시지 구성 섹션에서 "recommendations_be_recent_category" 선택.]({% image_buster /assets/img_archive/catalog_selections3.png %}){: style="max-width:90%;"}

예를 들어, 사용자가 최근에 본 카테고리가 "치킨"인 경우입니다. 설정된 개인화 및 콘텐츠 카드 캠페인을 사용하여 이 사용자에게 닭고기가 포함된 세 가지 식사 추천을 보낼 수 있습니다.

![숯불에 구운 레몬 치킨 이미지와 사용자가 가장 최근에 본 카테고리를 기반으로 한 세 가지 식사 추천 목록이 있는 콘텐츠 카드.]({% image_buster /assets/img_archive/catalog_selections4.png %}){: style="max-width:90%;"}

동일한 개인화를 사용하여 가장 최근에 본 카테고리가 "소고기"인 사용자에게 세 가지 식사 추천을 보낼 수도 있습니다.

![소고기 스트로가노프 이미지와 사용자가 가장 최근에 본 카테고리를 기반으로 한 두 가지 식사 추천 목록이 있는 콘텐츠 카드.]({% image_buster /assets/img_archive/catalog_selections5.png %}){: style="max-width:90%;"}


