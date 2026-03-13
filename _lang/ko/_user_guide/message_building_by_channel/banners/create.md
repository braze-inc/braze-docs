---
nav_title: 배너 만들기
article_title: 배너 만들기
page_order: 1
description: "이 참조 문서에서는 Braze 캠페인과 캔버스를 사용하여 배너를 만들고, 구성하고, 설정하고, 전송하는 방법을 다룹니다."
tool:
  - Campaigns
channel:
  - banners
---

# 배너 만들기

> Braze에서 캠페인과 캔버스를 구축할 때 배너를 만드는 방법을 배우십시오. 자세한 내용은 [배너 정보를]({{site.baseurl}}/user_guide/message_building_by_channel/banners) 참조하세요.

{% alert important %}
캔버스에서 배너 메시지를 만드는 것은 초기 액세스 단계에 있습니다. 이 얼리 액세스에 참여하려면 고객 성공 매니저에게 문의하세요.
{% endalert %}

## 필수 조건

배너를 시작하기 전에 개발 팀이 [앱 또는 웹사이트에 배치 설정]({{site.baseurl}}/developer_guide/banners/creating_placements/)을 해야 합니다. 그동안 배너 캠페인을 초안으로 작성할 수 있지만, 배치가 구성될 때까지 캠페인을 시작할 수 없습니다.

## 배너 메시지 만들기

{% multi_lang_include banners/creating_placements.md section="user" %}

### 2단계: 메시지를 작성할 위치 선택

메시지를 캠페인으로 보내야 할지 캔버스로 보내야 할지 잘 모르시겠어요? 캠페인은 단일, 타겟팅된 메시징 캠페인에 더 적합하고, 캔버스는 다단계 사용자 여정에 더 적합합니다.

{% tabs %}
{% tab Campaign %}

1. **메시징** > **캠페인**으로 이동하여 **캠페인 만들기**를 선택합니다.
2. **배너를** 선택합니다.
3. 캠페인의 이름을 명확하고 의미 있는 것으로 정하세요.
4. 필요에 따라 [팀과]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) [태그를]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) 추가하세요. 태그를 사용하면 캠페인을 더 쉽게 찾고 보고서를 작성할 수 있습니다. 예를 들어 보고서 작성기를 사용할 때 관련 태그를 기준으로 필터링할 수 있습니다.
5. 이전에 생성한 게재 위치를 선택하여 캠페인과 연결합니다.
6. 필요에 따라 이형 상품을 추가합니다. 각 메시지마다 다른 메시지 유형과 레이아웃을 선택할 수 있습니다. 변형에 대한 자세한 내용은 [다변량 및 A/B 테스트를]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing) 참조하세요.
7. 배너 캠페인의 시작 날짜와 시간을 선택합니다. 기본적으로 배너는 무기한으로 지속됩니다. **종료 시간을** 선택하고 종료 날짜와 시간을 지정하여 이를 변경할 수 있습니다.

{% alert tip %}
캠페인의 모든 메시지가 비슷하거나 콘텐츠가 동일한 경우, 변형을 추가하기 전에 메시지를 작성하세요. 그런 다음 **변형에서 복사**를 **변형 추가** 드롭다운에서 선택할 수 있습니다.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. 캔버스 작성기를 사용하여 [캔버스를 만듭니다]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
2. 캔버스를 설정한 후, 캔버스 빌더에서 메시지 단계를 추가하십시오. 단계에 명확하고 의미 있는 이름을 붙이세요.
3. 메시징 채널로 **배너**를 선택하십시오.
4. 배너의 배치를 선택하십시오.
5. 배너의 우선 순위를 설정하십시오. 배너 [우선순위는]({{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority) 배너가 동일한 위치를 공유하는 경우 배너가 표시되는 순서를 결정합니다.
6. 배너의 만료를 설정하십시오. 이는 단계가 사용 가능해진 후 일정 시간 후 또는 특정 날짜와 시간에 설정할 수 있습니다.

{% endtab %}
{% endtabs %}

### 3단계: 배너 작성 {#compose-a-banner}

배너를 구성하려면 다음 중 하나를 선택할 수 있습니다:

- 빈 템플릿으로 시작하기
- Braze 배너 템플릿 사용하기
- 저장된 배너 템플릿 선택하기

![빈 배너 또는 템플릿을 선택하는 옵션.]({% image_buster /assets/img/banners/choose_banner_composer.png %})

#### 3.1 단계: 배너 스타일 지정

블록과 행을 캔버스 영역으로 끌어다 놓아 메시지 작성을 시작할 수 있습니다.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

메시지의 배경 속성, 테두리 설정 등을 사용자 지정하려면 **스타일을** 선택합니다. 특정 블록 또는 행에 대해서만 스타일을 사용자 지정하려면 해당 블록 또는 행을 선택하여 변경합니다.

![배너 작성기의 스타일 패널.]({% image_buster /assets/img/banners/banner_card_styles.png %})

#### 3.2 단계: 클릭 동작 정의 (선택 사항)

사용자가 배너의 링크를 클릭하면 앱 내부로 더 깊이 이동하거나 다른 웹페이지로 리디렉션하도록 선택할 수 있습니다. 추가적으로, [사용자 정의 속성 또는 이벤트]({{site.baseurl}}/developer_guide/analytics/)을 기록하도록 선택할 수 있으며, 이는 사용자가 배너를 클릭할 때 사용자 프로필을 사용자 정의 데이터로 업데이트합니다.

{% alert important %}
{::nomarkdown}
특정 요소(예: 배너의 버튼, 링크 또는 이미지)에 고유한 클릭 동작이 있는 경우 클릭 동작을 재정의할 수 있습니다. 예를 들어 다음과 같은 클릭 동작이 있다고 가정해 보겠습니다:<br><ul><li>배너에는 웹사이트의 홈페이지로 리디렉션되는 클릭 시 동작이 있습니다.</li><li>배너의 이미지에는 클릭 시 웹사이트의 제품 페이지로 리디렉션되는 동작이 있습니다.</li></ul>사용자가 이미지를 클릭하면 제품 페이지로 리디렉션됩니다. 그러나 배너의 주변 영역을 클릭하면 홈페이지로 리디렉션됩니다.
{:/}
{% endalert %}

#### Step 3.3: 사용자 정의 속성 추가 (선택 사항) {#custom-properties}

배너에 사용자 정의 속성을 추가하여 문자열 또는 JSON 객체와 같은 구조화된 메타데이터를 첨부할 수 있습니다. 이 속성은 배너의 표시 방식에 영향을 미치지 않지만 [Braze SDK를 통해 접근할 수]({{site.baseurl}}/developer_guide/banners/placements/) 있어 앱의 동작이나 외관을 수정할 수 있습니다. 예를 들어, 다음과 같이 할 수 있습니다:

- 타사 분석 또는 통합을 위한 메타데이터 전송.
- 조건 로직을 트리거하기 위해 `timestamp` 또는 JSON 객체와 같은 메타데이터 사용.
- 포함된 메타데이터에 따라 배너의 동작을 제어합니다. 예: `ratio` 또는 `format`.

사용자 정의 속성을 추가하려면 **설정** > **속성** > **속성 추가**를 선택합니다.

![배너 캠페인에 첫 번째 사용자 정의 속성을 추가하는 옵션을 보여주는 속성 페이지.]({% image_buster /assets/img/banners/add_property.png %})

추가하려는 각 속성에 대해 다음을 작성하십시오:

| 필드 | 설명 | 예시 |
|-------|-------------|---------|
| 속성 유형 | 속성의 데이터 유형입니다. 지원되는 유형에는 문자열, 부울, 숫자, 타임스탬프, 이미지 URL 및 JSON 객체가 포함됩니다. | 문자열 |
| 속성 키 | 속성의 고유 식별자입니다. 이 키는 SDK에서 속성에 접근하는 데 사용됩니다. | `color` |
| 값 | 속성에 할당된 값입니다. 선택한 속성 유형과 일치해야 합니다. | `#FF0000` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

완료했으면 **완료**를 선택합니다.

![색상 키와 #FF0000 값이 있는 문자열 속성을 가진 속성 페이지입니다.]({% image_buster /assets/img/banners/example_property.png %})

### 4단계: 나머지 캠페인 또는 캔버스 구축하기

{% tabs %}
{% tab Campaign %}

#### 배너 우선순위 설정(선택 사항)

배너 [우선순위는]({{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority) 배너가 동일한 위치를 공유하는 경우 배너가 표시되는 순서를 결정합니다. 우선순위를 수동으로 설정하려면:

1. **정확한 우선순위 설정을** 선택합니다.
2. 캠페인을 드래그 앤 드롭하여 올바른 우선순위로 정렬할 수 있습니다.
3. **정렬 적용을** 선택합니다.

{% alert tip %}
동일한 게재 위치 ID를 사용하는 배너 캠페인이 여러 개 있는 경우 드래그 앤 드롭 우선순위 정렬기를 사용하여 정확한 우선순위를 정의하는 것이 좋습니다.
{% endalert %}

#### 대상을 선택하세요

1. **대상 오디언스**에서 세그먼트 또는 필터를 선택하여 대상을 좁힙니다. 세그먼트 인구의 대략적인 미리보기를 자동으로 받습니다. 정확한 세그먼트 구성원 자격은 메시지가 전송되기 전에 계산됩니다.

{% multi_lang_include target_audiences.md %}

{:start="2"}
2\. **전환 할당**에서 캠페인을 받은 후 사용자가 특정 작업을 수행하는 빈도를 추적하려면 최대 30일의 기간 내에 전환 이벤트를 정의하여 해당 작업을 전환으로 계산합니다.

{% multi_lang_include target_audiences.md %}

#### 전환 이벤트 선택

Braze는 캠페인을 받은 후 사용자가 특정 작업을 수행하는 빈도인 [전환 이벤트]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/)를 추적할 수 있게 해줍니다. 사용자가 지정된 작업을 수행할 경우 전환이 계산되는 최대 30일의 기간을 허용할 수 있는 옵션이 있습니다.

{% endtab %}

{% tab Canvas %}

아직 완료하지 않았다면 캔버스 구성 요소의 나머지 섹션을 완료하세요. Canvas의 나머지를 구축하는 방법, [다변량 테스트]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) 및 [지능형 선택]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) 구현 방법에 대한 자세한 내용은 Canvas 설명서의 [Canvas 구축]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) 단계를 참조하세요.

{% endtab %}
{% endtabs %}

### 5단계: 메시지 테스트(선택 사항)

{% multi_lang_include banners/testing.md page="campaigns" %}

### 6단계: 검토 및 배포

캠페인 또는 Canvas 구축을 마친 후, 세부 정보를 검토하고, [테스트]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/)한 다음 준비가 되면 전송하세요.
