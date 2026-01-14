---
nav_title: 인앱 메시지 생성하기
article_title: "드래그 앤 드롭으로 인앱 메시지 만들기"
description: "이 참조 문서에서는 드래그 앤 드롭 편집기를 사용하여 인앱 메시지를 만드는 방법, 전제 조건, 크리에이티브 세부 사항 등을 다룹니다."
alias: "/create_dnd_iam/"
page_order: 1
local_redirect: #set-message-level-styles, #add-a-custom-font, #drag-and-drop-in-app-message-components, #creative-details
  set-message-level-styles: '/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-level-styles'
  add-a-custom-font: '/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#custom-fonts'
  drag-and-drop-in-app-message-components: '/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components'
  creative-details: '/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#creative-details'
---

# 드래그 앤 드롭으로 인앱 메시지 만들기

> 드래그 앤 드롭 편집기를 사용하면 캠페인이나 캔버스에서 드래그 앤 드롭 편집 경험을 통해 완전히 커스텀되고 개인화된 인앱 메시지를 만들 수 있습니다.


{% multi_lang_include video.html id="j94omgo73o" align="right" source="wistia" %}

기존 커스텀 HTML 템플릿이나 타사에서 만든 템플릿을 사용하려면 드래그 앤 드롭 편집기에서 다시 만들어야 합니다.

인앱 메시지를 캠페인으로 보내야 할지 [캔버스로]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/) 보내야 할지 잘 모르시겠어요? 캠페인은 단일의 간단한 메시징 캠페인에 적합하며, 캔버스는 여러 단계의 사용자 여정에 적합합니다. 메시지를 구축할 위치를 선택한 후에는 드래그 앤 드롭 인앱 메시지를 만드는 단계를 자세히 살펴보겠습니다.

## 전제 조건

### 소프트웨어 개발 키트 요구 사항

| 최소 소프트웨어 개발 키트 버전                                                          | 권장 소프트웨어 개발 키트 버전                                                       |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| {::nomarkdown}{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}{:/} | {::nomarkdown}{% sdk_min_versions swift:6.5.0 android:26.0.0 web:4.8.1 %}{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% details More information on minimum SDKs %}

드래그 앤 드롭 편집기를 사용하여 만든 메시지는 최소 소프트웨어 개발 키트 버전을 사용하는 사용자에게만 보낼 수 있습니다(위 표 참조). 사용자가 애플리케이션을 업데이트하지 않은 경우(즉, 이전 소프트웨어 개발 키트 버전을 사용 중인 경우) 인앱 메시지를 받지 못합니다.

드래그 앤 드롭 편집기에서 사용할 수 있는 모든 기능을 활용하려면 SDK를 권장 SDK 버전으로 업데이트하세요. 이를 통해 다음과 같은 추가 기능을 활용할 수 있습니다:

- 메시지를 해제하지 않는 텍스트 링크
- 푸시 프라이머 요청 버튼 동작

다음은 이러한 기능에 대한 개별 최소 소프트웨어 개발 키트 요구 사항을 간략하게 설명합니다:

| 텍스트 링크*                                                         | 푸시 프라이머 요청하기                                                           |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| {::nomarkdown}{% sdk_min_versions swift:6.2.0 android:26.0.0 %}{:/} | {::nomarkdown}{% sdk_min_versions web:4.8.1 swift:6.5.0 android:26.0.0 %}{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

\*인앱 메시지에 URL로 리디렉션되는 링크를 포함하고 최종 사용자가 지정된 최소 소프트웨어 개발 키트 버전이 아닌 경우 링크를 선택하면 메시지가 닫히고 사용자가 메시지로 돌아가 양식을 제출할 수 없습니다.

{% enddetails %}

### 추가 전제 조건

- 웹 소프트웨어 개발 키트의 경우 초기화 옵션을 [`allowUserSuppliedJavascript`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) 을 `true` 으로 설정해야 합니다. `enableHtmlInAppMessages` 옵션도 이러한 메시징을 사용할 수 있지만 더 이상 사용되지 않으므로 `allowUserSuppliedJavascript` 으로 업데이트해야 합니다.
- Google 태그 매니저를 사용하는 경우 GTM 구성에서 "HTML 인앱 메시지 허용"을 인에이블먼트해야 합니다.

## 1단계: 인앱 메시지 만들기

새 인앱 메시지 또는 캔버스 단계를 만든 다음 **드래그 앤 드롭 편집기를** 선택하여 메시징 경험을 만듭니다.

## 2단계: 템플릿 선택

드래그 앤 드롭 편집기를 편집 환경으로 선택한 후 선택할 수 있습니다:

- 빈 모달 템플릿으로 시작하기
- Braze 드래그 앤 드롭 인앱 메시지 템플릿 사용
- 저장된 드래그 앤 드롭 인앱 메시지 템플릿을 선택합니다.

**메시지 구축을** 선택하여 드래그 앤 드롭 편집기에서 인앱 메시지 디자인을 시작합니다.

기본, 배경 이미지, 전화번호 캡처 또는 빈 템플릿을 선택할 수 있는 Braze 템플릿 섹션입니다.]({% image_buster /assets/img_archive/dnd_iam_select_template.png %})

대시보드의 **템플릿** 섹션에서 모든 템플릿에 액세스할 수도 있습니다.

## 3단계: 추가 페이지 추가(선택 사항) {#multi-page}

인앱 메시지에 페이지를 추가하면 온보딩 흐름이나 환영 여정과 같은 순차적인 흐름을 통해 사용자를 안내할 수 있습니다. **구축** 탭의 **페이지** 섹션에서 페이지를 관리할 수 있습니다.

세 페이지로 구성된 헬스케어 회사의 인앱 메시지입니다.]({% image_buster /assets/img_archive/dnd_iam_mockup.png %})

{% tabs %}
{% tab Adding pages %}

인앱 메시지는 기본값으로 한 페이지로 시작됩니다. 새 페이지를 추가하려면

1. **페이지 추가를** 선택합니다.
2. 커스텀 또는 Braze에서 제공하는 템플릿 목록에서 선택합니다.
3. 페이지의 이름을 의미 있는 이름으로 지정합니다. 이렇게 하면 페이지를 서로 연결할 때 도움이 됩니다.

{% alert tip %}
인앱 메시지당 최대 10페이지까지 추가할 수 있습니다.
{% endalert %}

기존 페이지를 복제하려면

1. 목록에서 페이지 위로 마우스를 가져가 <i class="fas fa-ellipsis-vertical"></i> 을 선택하면 더 많은 옵션이 열립니다.
2. **복제를** 선택합니다.
3. 페이지의 이름을 의미 있는 이름으로 지정합니다. 이렇게 하면 페이지를 서로 연결할 때 도움이 됩니다.

{% endtab %}
{% tab Deleting or renaming pages %}

페이지를 삭제하거나 이름을 변경하려면

1. 목록에서 페이지 위로 마우스를 가져가 <i class="fas fa-ellipsis-vertical"></i> 을 선택하면 더 많은 옵션이 열립니다.
2. **이름 바꾸기** 또는 **삭제를** 선택합니다.

{% endtab %}
{% endtabs %}

### 3a단계: 페이지를 서로 연결

여러 페이지로 구성된 인앱 메시지는 순차적으로 표시되므로 사용자는 탭하거나 클릭하여 흐름의 다음 페이지로 이동하여 메시지와 상호 작용할 수 있습니다.

페이지를 서로 연결하려면:

1. 시작 페이지를 선택합니다.
2. 캔버스에서 버튼 또는 이미지 요소를 선택합니다.
3. **클릭 시 동작을** **페이지로 이동으로** 설정합니다.
4. 시작 페이지에서 연결하려는 페이지를 선택합니다.
5. 모든 페이지가 연결될 때까지 계속 진행합니다.

\![사용자가 인앱 메시지의 2페이지로 이동하기 위해 기본 실행 버튼을 편집하고 있습니다.]({% image_buster/assets/img_archive/dnd_iam_multipage.gif %})

페이지가 다른 페이지에 링크되어 있지 않으면 메시지를 실행할 수 없습니다.

{% alert note %}
사용자는 언제든지 닫기 X 버튼을 선택하여 메시지를 종료할 수 있습니다. 이 버튼은 제거할 수 없습니다.
{% endalert %}

## 4단계: 인앱 메시지 구축 및 디자인하기

여기에서 브랜드의 시그니처 스타일을 입고 런웨이를 활보하는 메시지를 전달할 수 있습니다. 편집기 블록과 스타일 설정을 조합하여 인앱 메시지를 커스터마이즈하고 디자인할 수 있습니다.

- 사용 가능한 편집기 블록 및 해당 속성 목록은 [편집기 블록을]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/) 참조하세요.
- 메시징의 모양과 느낌을 커스터마이징하는 데 도움이 필요하면 [스타일 설정을]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/) 확인하세요.
- 오른쪽에서 왼쪽으로 메시지를 작성하는 모범 사례는 [오른쪽에서 왼쪽으로 메시지 작성하기를]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) 참조하세요.

## 5단계: 인앱 메시지 테스트하기

**미리보기 & 테스트** 섹션에서는 여러 기기에서 인앱 메시지를 미리 보고 기기에 테스트 메시지를 보낼 수 있습니다. 여기에서 드래그 앤 드롭 인앱 메시지 캠페인을 위해 모든 플랫폼에 걸쳐 세부 사항을 조정할 수 있습니다. 

캠페인을 보내기 전에 항상 인앱 메시지를 테스트하여 사용자 관점에서 최종 메시지가 어떻게 보일지 시각화하는 것이 중요합니다.

### 사용자로서 메시지 미리보기

{% alert warning %}
콘텐츠 테스트 그룹 또는 개별 사용자에게 테스트를 보내려면 보내기 전에 테스트 기기에서 푸시를 인에이블먼트해야 합니다.
{% endalert %}

**미리보기 & 테스트** 탭에서 사용자가 된 것처럼 메시지를 미리 볼 수 있습니다. 특정 사용자, 임의의 사용자를 선택하거나 커스텀 사용자를 만들 수 있습니다:

- **무작위 사용자:** Braze는 데이터베이스에서 무작위로 사용자를 선택하고 해당 사용자의 속성 또는 이벤트 정보를 기반으로 인앱 메시지를 미리 보여줍니다.
- **사용자를 선택합니다:** 이메일 주소 또는 `external_id` 을 기반으로 특정 사용자를 선택할 수 있습니다. 인앱 메시지는 해당 사용자의 속성 및 이벤트 정보를 기반으로 미리 볼 수 있습니다.
- **커스텀 사용자:** 사용자를 커스텀할 수 있습니다. Braze는 사용 가능한 모든 속성과 이벤트에 대한 입력을 제공합니다. 미리 보기 이메일에 보고 싶은 정보를 입력합니다.

### 테스트 체크리스트

인앱 메시지를 테스트할 때 다음 질문을 고려하세요:

- 다른 기기에서 메시지를 테스트해 보셨나요?
- 이미지와 미디어가 예상대로 표시되고 작동하나요?
- Liquid가 예상대로 작동하나요? Liquid가 정보를 반환하지 않는 경우의 기본 속성 값을 고려하셨나요?
- 카피가 명확하고 간결하며 정확한가요?
- 버튼이 사용자가 어디로 이동해야 하는지 안내하나요?

## 자주 묻는 질문

#### 본문 클릭이 분석 페이지에 표시되지 않는 이유는 무엇인가요?

드래그 앤 드롭 편집기로 작성한 인앱 메시지에 대해서는 본문 클릭이 자동으로 수집되지 않습니다. 자세한 내용은 [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog#3310) 및 [Android용]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog#1100) 소프트웨어 개발 키트 체인지로그를 참조하세요.

#### 버튼 클릭을 기준으로 세그먼트를 세분화할 수 있나요?

예, 메시지에서 최대 2개의 버튼에 대해 버튼 클릭을 기준으로 메시지 세그먼트를 세분화할 수 있습니다. 이렇게 하려면 버튼에 대한 **보고 식별자를** "0" 및 "1"로 설정하면 각각 "클릭한 인앱 메시지 버튼 1" 및 "클릭한 인앱 메시지 버튼 2" 세분화 필터에 해당합니다.

값이 "0"인 '보고용 식별자' 필드입니다.]({% image_buster /assets/img/identifier_for_reporting.png %}){: style="max-width:50%;"}

#### 커스텀 HTML 또는 JavaScript를 사용하여 인앱 메시지를 사용자 지정하거나 기존 HTML 메시지를 에디터로 전송할 수 있나요?

기존 HTML 메시지를 편집기로 직접 전송할 수는 없지만 원시 HTML, CSS 및 JavaScript를 커스텀 코드 블록에 삽입할 수 있습니다. 커스텀 코드 블록을 사용하여 타사 동영상을 임베드하고 연결된 콘텐츠 또는 조건문과 같은 Liquid를 진행할 수 있습니다.

#### 슬라이드업 인앱 메시지는 어떻게 만들 수 있나요?

현재 에디터는 모달 및 전체 화면 메시징으로만 제한되어 있습니다. **메시지 스타일** 패널의 **메시지 컨테이너** 섹션에서 표시 유형 간에 전환할 수 있습니다.

#### 캠페인 또는 캔버스 내에서 인앱 메시지를 구축한 후 템플릿으로 저장할 수 있나요?

예. 향후 캠페인 또는 캔버스 단계에서 재사용하려는 인앱 메시지는 에디터를 종료한 후 사용할 수 있는 **템플릿으로** 저장 버튼을 사용하여 커스텀 템플릿으로 저장할 수 있습니다. 템플릿으로 저장하려면 먼저 캠페인을 시작하거나 초안으로 저장해야 합니다.

\![제품 둘러보기를 위한 인앱 메시지 미리보기입니다.]({% image_buster /assets/img_archive/dnd_iam_save_as_template.png %})

**템플릿** > **인앱 메시지 템플릿으로** 이동하여 인앱 메시지 템플릿을 생성하고 저장할 수도 있습니다.
