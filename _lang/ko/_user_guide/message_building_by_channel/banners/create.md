---
nav_title: 배너 만들기
article_title: 배너 만들기
page_order: 1
description: "이 참조 문서에서는 Braze 캠페인과 캔버스를 사용하여 배너를 만들고, 작성하고, 구성하고, 전송하는 방법에 대해 설명합니다."
tool:
  - Campaigns
channel:
  - banners
---

# 배너 만들기

> Braze에서 캠페인과 캔버스를 구축할 때 배너를 만드는 방법을 알아보세요. 자세한 내용은 [배너 정보를]({{site.baseurl}}/user_guide/message_building_by_channel/banners) 참조하세요.

{% alert important %}
캔버스에서 배너 메시지를 만드는 기능은 얼리 액세스 중입니다. 이 얼리 액세스에 참여하려면 고객 성공 매니저에게 문의하세요.
{% endalert %}

## 필수 조건

배너를 시작하려면 먼저 개발자가 [앱이나 웹사이트에 배치를 설정해야]({{site.baseurl}}/developer_guide/banners/creating_placements/) 합니다. 그 동안에도 배너 캠페인 초안을 작성할 수 있지만 게재 위치가 구성될 때까지 캠페인을 시작할 수 없습니다.

## 배너 메시지 만들기

{% multi_lang_include banners/creating_placements.md section="user" %}

### 2단계: 메시지를 작성할 위치 선택

메시지를 캠페인으로 보내야 할지 캔버스로 보내야 할지 잘 모르시겠어요? 캠페인은 단일 타겟팅 메시징 캠페인에 더 적합하며, 캔버스는 다단계 사용자 여정에 더 적합합니다.

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
캠페인의 모든 메시지가 비슷하거나 콘텐츠가 동일한 경우, 변형을 추가하기 전에 메시지를 작성하세요. 그런 다음 **배리언트 추가** 드롭다운에서 **배리언트에서 복사를** 선택할 수 있습니다.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. 캔버스 작성기를 사용하여 [캔버스를 만듭니다]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
2. 캔버스를 설정한 후 캔버스 빌더에서 메시지 단계를 추가합니다. 단계에 명확하고 의미 있는 이름을 붙이세요.
3. 메시징 채널로 **배너를** 선택합니다.
4. 배너의 배치를 선택합니다.
5. 배너의 우선순위를 설정합니다. 배너 [우선순위는]({{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority) 배너가 동일한 위치를 공유하는 경우 배너가 표시되는 순서를 결정합니다.
6. 배너의 만료일을 설정합니다. 이는 단계를 사용할 수 있게 된 후 일정 시간이 지난 후 또는 특정 날짜와 시간이 될 수 있습니다.

{% endtab %}
{% endtabs %}

### 3단계: 배너 작성 {#compose-a-banner}

배너를 작성하려면 다음을 선택할 수 있습니다:

- 빈 템플릿으로 시작하기
- Braze 배너 템플릿 사용
- 저장된 배너 템플릿을 선택합니다.

![빈 배너 또는 템플릿을 선택할 수 있는 옵션입니다.]({% image_buster /assets/img/banners/choose_banner_composer.png %})

#### 3.1 단계: 배너 스타일 지정

블록과 행을 캔버스 영역으로 끌어다 놓아 메시지 작성을 시작할 수 있습니다.

메시지의 배경 속성, 테두리 설정 등을 사용자 지정하려면 **스타일을** 선택합니다. 특정 블록 또는 행에 대해서만 스타일을 사용자 지정하려면 해당 블록 또는 행을 선택하여 변경합니다.

![배너 작성기의 스타일 패널.]({% image_buster /assets/img/banners/banner_card_styles.png %})

#### 3.2 단계: 클릭 시 동작 정의(선택 사항)

사용자가 배너의 링크를 클릭하면 앱 내부로 더 깊이 이동하거나 다른 웹페이지로 리디렉션하도록 선택할 수 있습니다. 또한 [커스텀 속성 또는 이벤트를 기록하도록]({{site.baseurl}}/developer_guide/analytics/) 선택하면 사용자가 배너를 클릭할 때 사용자 프로필이 커스텀 데이터로 업데이트됩니다.

{% alert important %}
{::nomarkdown}
특정 요소(예: 배너의 버튼, 링크 또는 이미지)에 고유한 클릭 동작이 있는 경우 클릭 동작을 재정의할 수 있습니다. 예를 들어 다음과 같은 클릭 동작이 있다고 가정해 보겠습니다:<br><ul><li>배너에는 웹사이트의 홈페이지로 리디렉션되는 클릭 시 동작이 있습니다.</li><li>배너의 이미지에는 클릭 시 웹사이트의 제품 페이지로 리디렉션되는 동작이 있습니다.</li></ul>사용자가 이미지를 클릭하면 제품 페이지로 리디렉션됩니다. 하지만 배너에서 주변 영역을 클릭하면 홈페이지로 리디렉션됩니다.
{:/}
{% endalert %}

#### Step 3.3: 커스텀 속성 추가(선택 사항) {#custom-properties}

배너에 커스텀 속성을 추가하여 문자열이나 JSON 오브젝트와 같은 구조화된 메타데이터를 첨부할 수 있습니다. 이러한 속성은 배너가 표시되는 방식에는 영향을 미치지 않지만 [Braze 소프트웨어 개발 키트를 통해 액세스하여]({{site.baseurl}}/developer_guide/banners/placements/) 앱의 동작이나 모양을 수정할 수 있습니다. 예를 들어, 다음과 같이 할 수 있습니다:

- 타사 분석 또는 통합을 위한 메타데이터를 전송하세요.
- `timestamp` 또는 JSON 객체와 같은 메타데이터를 사용하여 조건 로직을 트리거하세요.
- `ratio` 또는 `format` 과 같은 포함된 메타데이터를 기반으로 배너의 동작을 제어합니다.

커스텀 속성을 추가하려면 **설정** > **속성** > **속성 추가를** 선택합니다.

![배너 캠페인에 첫 번째 커스텀 속성을 추가하는 옵션이 표시된 속성 페이지입니다.]({% image_buster /assets/img/banners/add_property.png %})

추가하려는 각 속성에 대해 다음을 입력합니다:

| 필드 | 설명 | 예시 |
|-------|-------------|---------|
| 속성정보 유형 | 속성의 데이터 유형입니다. 지원되는 유형에는 문자열, 부울, 숫자, 타임스탬프, 이미지 URL, JSON 객체 등이 있습니다. | 문자열 |
| 속성정보 키 | 속성의 고유 식별자입니다. 이 키는 소프트웨어 개발 키트에서 속성에 액세스하는 데 사용됩니다. | `color` |
| 값 | 속성에 할당된 값입니다. 선택한 속성 유형과 일치해야 합니다. | `#FF0000` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

완료했으면 **완료**를 선택합니다.

![색상 키와 값이 #FF0000 인 문자열 속성이 있는 속성 페이지입니다.]({% image_buster /assets/img/banners/example_property.png %})

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

#### 오디언스 선택하기

1. **타겟 오디언스에서** 세그먼트 또는 필터를 선택하여 오디언스의 범위를 좁힙니다. 대략적인 세그먼트 모집단의 미리보기가 자동으로 표시됩니다. 정확한 세그먼트 멤버십은 메시지가 전송되기 전에 계산됩니다.

{% multi_lang_include target_audiences.md %}

{:start="2"}
2\. **전환 할당에서** 최대 30일의 기간으로 전환 이벤트를 정의하여 사용자가 캠페인을 수신한 후 특정 액션을 수행하는 빈도를 추적하여 해당 액션을 전환으로 계산할 수 있습니다.

{% multi_lang_include target_audiences.md %}

#### 전환 이벤트 선택

Braze를 사용하면 캠페인 수신 후 사용자가 특정 액션을 얼마나 자주 수행하는지 [전환 이벤트를]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) 추적할 수 있습니다. 사용자가 지정된 작업을 수행하면 최대 30일 동안 전환이 카운트되도록 허용하는 옵션이 있습니다.

{% endtab %}

{% tab Canvas %}

아직 완료하지 않았다면 캔버스 구성 요소의 나머지 섹션을 완료하세요. 나머지 캔버스를 구축하고, [다변량 테스트]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) 및 [지능형 선택을]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) 구현하는 방법 등에 대한 자세한 내용은 캔버스 설명서의 캔버스 [구축]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) 단계를 참조하세요.

{% endtab %}
{% endtabs %}

### 5단계: 메시지 테스트(선택 사항)

{% multi_lang_include banners/testing.md page="campaigns" %}

### 6단계: 검토 및 배포

캠페인 또는 캔버스 구축을 완료한 후에는 세부 사항을 검토하고 [테스트한]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) 다음 준비가 되면 전송하세요.
