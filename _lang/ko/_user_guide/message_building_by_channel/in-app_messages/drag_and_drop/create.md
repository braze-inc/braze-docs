---
nav_title: 인앱 메시지 만들기
article_title: "드래그 앤 드롭으로 인앱 메시지 만들기"
description: "이 참조 문서에서는 드래그 앤 드롭 편집기를 사용하여 인앱 메시지를 만드는 방법, 전제 조건, 창의적 세부 사항 등을 다룹니다."
alias: "/create_dnd_iam/"
page_order: 1
local_redirect: #set-message-level-styles, #add-a-custom-font, #drag-and-drop-in-app-message-components, #creative-details
  set-message-level-styles: '/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-level-styles'
  add-a-custom-font: '/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#custom-fonts'
  drag-and-drop-in-app-message-components: '/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components'
  creative-details: '/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#creative-details'
---

# 드래그 앤 드롭으로 인앱 메시지 만들기

> 드래그 앤 드롭 편집기를 사용하면 드래그 앤 드롭 편집 경험을 통해 캠페인 또는 캔버스에서 완전히 커스텀되고 개인화된 인앱 메시지를 만들 수 있습니다.

{% multi_lang_include video.html id="tbrgv_mU1zI" align="right" source="youtube" %}

기존 커스텀 HTML 템플릿이나 타사에서 생성한 템플릿을 사용하려면 드래그 앤 드롭 편집기에서 다시 생성해야 합니다.

Not sure whether your in-app message should be sent using a campaign or a [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/)? 캠페인은 단일의 간단한 메시징 캠페인에 적합하며, 캔버스는 여러 단계의 사용자 여정에 적합합니다. 메시지를 구축할 위치를 선택한 후, 드래그 앤 드롭 인앱 메시지를 만드는 단계로 들어가 보겠습니다.

## 전제 조건

### SDK 요구 사항

| 최소 소프트웨어 개발 키트 버전                                                          | 권장 SDK 버전                                                       |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| {::nomarkdown}{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}{:/} | {::nomarkdown}{% sdk_min_versions swift:6.5.0 android:26.0.0 web:4.8.1 %}{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% details 최소 SDK에 대한 추가 정보 %}

드래그 앤 드롭 편집기를 사용하여 생성된 메시지는 최소 SDK 버전의 사용자에게만 보낼 수 있습니다(위 표 참조). 사용자가 애플리케이션을 업데이트하지 않은 경우(즉, 이전 SDK 버전을 사용 중인 경우), 인앱 메시지를 받지 못합니다.

드래그 앤 드롭 편집기에서 사용할 수 있는 모든 기능을 활용하려면 SDK를 권장 SDK 버전으로 업데이트하세요. 이를 통해 다음과 같은 추가 기능을 활용할 수 있습니다:

- 메시지를 해제하지 않는 텍스트 링크
- 버튼 동작으로 푸시 프라이머 요청

다음은 이러한 기능에 대한 개별 최소 SDK(SDK) 요구 사항을 설명합니다.

| 텍스트 링크*                                                         | 푸시 프라이머 요청                                                           |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| {::nomarkdown}{% sdk_min_versions swift:6.2.0 android:26.0.0 %}{:/} | {::nomarkdown}{% sdk_min_versions web:4.8.1 swift:6.5.0 android:26.0.0 %}{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

\*인앱 메시지에 URL로 리디렉션되는 링크를 포함하면 최종 사용자가 지정된 최소 SDK 버전이 아닐 경우, 링크를 선택하면 메시지가 닫히고 사용자는 양식을 제출하기 위해 메시지로 돌아갈 수 없습니다.

{% enddetails %}

### 추가 전제 조건

- 웹 SDK의 초기화 옵션 [`allowUserSuppliedJavascript`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions)를 `true`로 설정해야 합니다. `enableHtmlInAppMessages` 옵션은 이러한 메시지가 작동하도록 허용하지만 더 이상 사용되지 않으며 `allowUserSuppliedJavascript`로 업데이트해야 합니다.
- Google Tag Manager를 사용하고 있다면 GTM 구성에서 "In-App 메시지에 HTML 허용"을 활성화해야 합니다.

## 1단계: 인앱 메시지를 생성하세요

새 인앱 메시지 또는 캔버스 단계를 생성한 다음, **드래그 앤 드롭 편집기**를 편집 환경으로 선택하세요.

## 2단계: 템플릿을 선택하세요

드래그 앤 드롭 편집기를 편집 환경으로 선택한 후 다음을 선택할 수 있습니다.

- 빈 모달 템플릿으로 시작
- Braze 드래그 앤 드롭 인앱 메시지 템플릿을 사용하세요
- 저장된 드래그 앤 드롭 인앱 메시지 템플릿을 선택하십시오

드래그 앤 드롭 편집기에서 인앱 메시지를 디자인하기 시작하려면 **구축 메시지**를 선택하세요.

![브레이즈 템플릿 섹션에서는 기본 템플릿, 배경 이미지, 전화번호 캡처 또는 빈 템플릿을 선택할 수 있습니다.]({% image_buster /assets/img_archive/dnd_iam_select_template.png %}){: style="max-width:75%"}

템플릿의 **템플릿** 섹션에서 모든 템플릿에 액세스할 수 있습니다.

## 3단계: 추가 페이지 추가 (선택 사항) {#multi-page}

인앱 메시지에 페이지를 추가하면 온보딩 흐름이나 환영 여정과 같은 순차적 흐름을 통해 사용자를 안내할 수 있습니다. **페이지** 섹션의 **구축** 탭에서 페이지를 관리할 수 있습니다.

![헬스케어 회사의 세 페이지로 구성된 인앱 메시지.]({% image_buster /assets/img_archive/dnd_iam_mockup.png %})

{% tabs %}
{% tab 페이지 추가 %}

인앱 메시지는 기본적으로 한 페이지로 시작합니다. 새 페이지를 추가하려면:

1. **페이지 추가** 선택.
2. 커스텀 또는 Braze에서 제공한 템플릿 목록에서 선택하십시오.
3. 페이지에 의미 있는 이름을 지정하세요. 이것은 페이지를 연결할 때 도움이 될 것입니다.

{% alert tip %}
인앱 메시지당 최대 10페이지를 추가할 수 있습니다.
{% endalert %}

기존 페이지를 복제하려면,

1. 목록에서 페이지 위로 마우스를 가져가고 <i class="fas fa-ellipsis-vertical"></i>을 선택하여 더 많은 옵션을 엽니다.
2. **중복** 선택.
3. 페이지에 의미 있는 이름을 지정하세요. 이것은 페이지를 연결할 때 도움이 될 것입니다.

{% endtab %}
{% tab 페이지 삭제 또는 이름 변경 %}

페이지를 삭제하거나 이름을 바꾸려면:

1. 목록에서 페이지 위로 마우스를 가져가고 <i class="fas fa-ellipsis-vertical"></i>을 선택하여 더 많은 옵션을 엽니다.
2. **이름 바꾸기** 또는 **삭제**를 선택하십시오.

{% endtab %}
{% endtabs %}

### 3a 단계: 페이지를 연결합니다

다중 페이지 인앱 메시지는 순차적이므로 사용자가 메시지를 탭하거나 클릭하여 흐름의 다음 페이지로 이동합니다.

페이지를 연결하려면:

1. 시작 페이지를 선택하세요.
2. 캔버스에서 버튼 또는 이미지 요소를 선택하십시오.
3. **클릭 시 동작**을(를) **페이지로 이동**으로 설정합니다.
4. 시작 페이지에서 연결할 페이지를 선택하세요.
5. 모든 페이지가 연결될 때까지 계속하십시오.

![사용자가 인앱 메시지의 페이지 2로 이동하기 위해 기본 실행 버튼을 편집하고 있습니다.]({% image_buster/assets/img_archive/dnd_iam_multipage.gif %})

페이지가 다른 페이지와 연결되지 않은 경우, 메시지를 실행할 수 없습니다.

{% alert note %}
사용자는 언제든지 메시지를 종료하기 위해 닫기 X 버튼을 선택할 수 있습니다. 이 버튼은 제거할 수 없습니다.
{% endalert %}

## 4단계: 인앱 메시지를 빌드하고 디자인

여기에서 귀하의 메시지가 귀하의 브랜드 시그니처 스타일로 차려입고 런웨이를 활보합니다. 편집기 블록과 스타일 설정의 조합을 사용하여 인앱 메시지를 사용자 정의하고 디자인할 수 있습니다.

- 사용 가능한 편집기 블록 및 해당 속성 목록은 [편집기 블록]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/)을 참조하십시오.
- 메시지의 모양과 느낌을 사용자 정의하는 데 도움이 필요하면 [스타일 설정]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/)을 확인하세요.
- For best practices creating right-to-left messages, refer to [Creating right-to-left messages]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

## 5단계: 인앱 메시지를 테스트하세요

**미리보기 및 테스트** 섹션에서는 다양한 기기에서 인앱 메시지를 미리 보고 기기로 테스트 메시지를 보낼 수 있습니다. 여기에서 드래그 앤 드롭 인앱 메시지 캠페인에 대한 세부 정보가 모든 플랫폼에서 일치하도록 할 수 있습니다. 

앱 내 메시지를 항상 테스트하는 것이 중요합니다. 캠페인을 보내기 전에 사용자의 관점에서 최종 메시지가 어떻게 보일지를 시각화하는 데 도움이 됩니다.

### 사용자로서 메시지 미리보기

{% alert warning %}
테스트를 콘텐츠 테스트 그룹 또는 개별 사용자에게 보내려면, 푸시가 전송 전에 테스트 기기에서 활성화되어 있어야 합니다.
{% endalert %}

메시지를 사용자인 것처럼 **미리보기 및 테스트** 탭에서 미리 볼 수 있습니다. 특정 사용자, 무작위 사용자 또는 커스텀 사용자를 선택할 수 있습니다.

- **무작위 사용자:** Braze는 데이터베이스에서 사용자를 무작위로 선택하고 속성 또는 이벤트 정보를 기반으로 인앱 메시지를 미리 봅니다.
- **사용자 선택:** 특정 사용자를 이메일 주소 또는 `external_id`를 기준으로 선택할 수 있습니다. 인앱 메시지는 해당 사용자의 속성과 이벤트 정보를 기반으로 미리보기 됩니다.
- **커스텀 사용자:** 사용자를 사용자 정의할 수 있습니다. Braze는 사용 가능한 모든 속성과 이벤트에 대한 입력을 제공합니다. 미리보기 이메일에서 보고 싶은 정보를 입력하세요.

### 테스트 체크리스트

다음 질문을 고려하면서 인앱 메시지를 테스트하세요:

- 다양한 기기에서 메시지를 테스트해 보셨나요?
- 이미지와 미디어가 예상대로 표시되고 작동합니까?
- Liquid 기능이 예상대로 작동합니까? Liquid가 정보를 반환하지 않는 경우 기본 속성 값을 고려했습니까?
- 귀하의 카피가 명확하고 간결하며 정확합니까?
- 당신의 버튼이 사용자가 가야 할 곳으로 안내합니까?

## 자주 묻는 질문

#### 내 분석 페이지에 본문 클릭이 나타나지 않는 이유는 무엇입니까?

본문 클릭은 드래그 앤 드롭 편집기로 생성된 인앱 메시지에 대해 자동으로 수집되지 않습니다. 자세한 내용은 [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog#3310) 및 [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog#1100)용 SDK 체인지로그를 참조하세요.

#### 버튼 클릭을 기준으로 세그먼트할 수 있나요?

네, 메시지에서 최대 두 개의 버튼 클릭을 기준으로 세그먼트할 수 있습니다. 이를 위해 버튼의 **보고용 식별자**를 "0" 및 "1"로 설정하면 각각 "인앱 메시지 버튼 1 클릭" 및 "인앱 메시지 버튼 2 클릭" 세분화 필터에 해당합니다.

#### 내 인앱 메시지를 커스텀 HTML 또는 JavaScript를 사용하여 커스터마이징하거나 기존 HTML 메시지를 편집기로 전송할 수 있습니까?

기존 HTML 메시지를 편집기로 직접 전송할 수는 없지만, 커스텀 코드 블록에 원시 HTML, CSS 및 JavaScript를 삽입할 수 있습니다. 커스텀 코드 블록을 사용하여 타사 비디오 및 연결된 콘텐츠 또는 조건문과 같은 고급 Liquid를 포함할 수 있습니다.

#### 슬라이드업 인앱 메시지를 어떻게 만들 수 있나요?

현재 편집기는 모달 및 전체 화면 메시지로만 제한됩니다. **메시지 컨테이너** 섹션의 **메시지 스타일** 패널에서 디스플레이 유형을 전환할 수 있습니다.

#### 내 캠페인 또는 캔버스 내에서 구축한 인앱 메시지를 템플릿으로 저장할 수 있나요?

네. 향후 캠페인 또는 캔버스 단계에서 다시 사용하려는 모든 인앱 메시지의 경우, 편집기를 종료한 후 사용할 수 있는 **템플릿으로 저장** 버튼을 사용하여 커스텀 템플릿으로 저장할 수 있습니다. 템플릿으로 저장하기 전에 먼저 캠페인을 시작하거나 초안으로 저장해야 합니다.

![텍스트 업데이트를 위한 가입을 위한 인앱 메시지 미리보기.]({% image_buster /assets/img_archive/dnd_iam_save_as_template.png %})

**탬플릿** > **인앱 메시지 템플릿**으로 이동하여 인앱 메시지 템플릿을 생성하고 저장할 수도 있습니다.
