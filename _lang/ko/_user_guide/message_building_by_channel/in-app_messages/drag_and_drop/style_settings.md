---
nav_title: 스타일 설정
article_title: "인앱 메시지 스타일 설정"
description: "이 참고 문서에서는 드래그 앤 드롭 편집기로 인앱 메시지를 만들 때 사용할 수 있는 스타일링 옵션에 대해 설명합니다."
page_order: 3
---

# 인앱 메시지 스타일 설정

> 드래그 앤 드롭 편집 환경은 두 섹션으로 나뉩니다: **구축** 및 **미리보기 & 테스트**. 이 문서에서는 에디터의 **구축** 탭에서 작업할 때 알아야 할 사항을 다루며 이미 [인앱 메시지를 만들었다고]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/) 가정합니다.

!"["메시지 스타일" 탭.]({% image_buster /assets/img_archive/dnd_iam_message_styles.png %}){: style="float:right;max-width:25%;margin-left:15px;max-width:30%"}

## 메시지 수준 스타일

**메시지 스타일** 탭에서 인앱 메시지의 모든 관련 블록에 적용될 특정 스타일을 설정할 수 있습니다. 예를 들어 메시징에 포함된 모든 텍스트의 글꼴이나 모든 링크의 색상을 커스텀할 수 있습니다.

이 섹션의 스타일은 특정 블록에 대해 재정의하는 경우를 제외하고 메시징의 모든 곳에서 사용됩니다. 메시징에 [여러 페이지가]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page) 있는 경우 표시 유형 및 최대 너비를 제외한 개별 페이지에 대한 메시지 수준 스타일을 재정의할 수도 있습니다.

보다 쉬운 디자인 경험을 위해 블록 수준에서 스타일을 커스텀하기 전에 메시지 수준 스타일을 설정하는 것이 좋습니다.

언제든지 **메시지 스타일** 탭으로 돌아가려면 다음과 같이 하세요:

- 개별 블록 속성에서 닫기 X 버튼을 클릭합니다.
- 메시지 컨테이너, 메시지 닫기 X 버튼 또는 편집기 배경을 선택합니다.

### 커스텀 글꼴

다음 파일 형식의 글꼴을 사용할 수 있습니다: `.ttf`, `.woff`, `.otf`, `.woff2`. 자세한 내용은 [자산 파일을]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/html_in-app_messages#asset-files) 참조하세요.

커스텀 글꼴에는 일부 스타일링 옵션을 사용할 수 없으므로 글꼴 모음에 여러 가지 변형을 추가할 수 있습니다. 현재 URL을 통한 글꼴 추가는 지원하지 않습니다.

커스텀 글꼴을 추가하려면 다음과 같이 하세요:

1. **메시지 스타일** 탭의 **콘텐츠** 섹션으로 이동합니다.
2. **커스텀 글꼴 추가를** 클릭합니다.
3. 미디어 라이브러리를 사용하여 글꼴을 업로드합니다. 

{% alert note %}
메시지 수준 글꼴은 현재 메시지와 중복된 메시지에만 적용되며 향후 템플릿에는 적용되지 않습니다.
{% endalert %}

## 메시지 구성 요소

프로모션 인앱 메시지가 생성되는 과정을 보여주는 GIF입니다.]({% image_buster /assets/img_archive/dnd_iam_create.gif %})

드래그 앤 드롭 편집기는 인앱 메시지 작성에 **행과** **블록이라는** 두 가지 주요 구성 요소를 사용합니다. 모든 블록은 일렬로 배치해야 합니다.

### 닫기 x 버튼

모달 및 전체 화면 인앱 메시지의 경우 메시지 오른쪽 상단에 <i class="fa-solid fa-xmark"></i> 으로 표시되는 닫기 버튼을 커스텀할 수 있습니다. 커스텀 옵션에는 버튼 위치, 크기, 채우기 색상, 배경색, 테두리 스타일, 테두리 반경 등이 있습니다.

버튼 크기, 채우기 색상, 배경색, 테두리 스타일, 테두리 반경 등 인앱 메시지에서 닫기 X 버튼을 커스텀할 수 있는 옵션입니다.]({% image_buster /assets/img_archive/close_x_button.png %}){: style="max-width:40%"}

### 스팬 스타일링

인앱 메시지 내 텍스트에 스팬 스타일을 추가하면 다양한 텍스트 색상, 글꼴, 크기를 사용할 수 있어 메시지 모양을 더욱 맞춤화할 수 있습니다. 스팬 스타일링은 주요 정보에 주의를 집중시키고 전반적인 메시지 명확성을 개선하여 사용자의 참여도를 높이고 시각적으로 매력적인 경험을 제공합니다.

!"[인앱 메시지에서 텍스트를 강조 표시할 때 표시되는 옵션입니다. 작은 페인트 브러시 아이콘은 스팬으로 스타일을 지정할 수 있음을 나타냅니다.]({% image_buster /assets/img_archive/span_1.png %}){: style="max-width:40%"}

최종 사용자가 글꼴 패밀리, 글꼴 무게, 글꼴 크기, 글자 간격 및 텍스트 색상을 커스텀할 수 있는 '스팬 속성' 사이드 패널입니다.]({% image_buster /assets/img_archive/span_2.png %}){: style="max-width:40%"}

### 행

행은 셀을 사용하여 메시지 섹션의 가로 구성을 정의하는 구조적 단위입니다.

인앱 메시지에 추가할 수 있는 행입니다.]({% image_buster /assets/img_archive/dnd_iam_rows.png %}){: style="max-width:40%"}

행을 선택하면 **열 커스텀** 섹션에서 필요한 열 개수를 추가하거나 제거하여 서로 다른 콘텐츠 요소를 나란히 배치할 수 있습니다. 

기존 열의 크기를 슬라이드하여 조정할 수도 있습니다.

!"열 커스텀" 섹션에서 열 조정하기.]({% image_buster /assets/img_archive/dnd_iam_column_customization.gif %}){: style="max-width:40%"}

행과 열 속성의 서식을 지정하기 전에 행 내부의 블록에 서식을 지정하는 것이 좋습니다. 간격과 정렬을 조정할 수 있는 곳이 많으므로 기초부터 시작하면 진행하면서 편집하기가 더 쉬워집니다.

### 블록

콘텐츠 블록은 메시징에 사용할 수 있는 다양한 유형의 콘텐츠를 나타냅니다. 기존 행 세그먼트 안으로 드래그하면 셀 너비에 맞게 자동으로 조정됩니다.

{% alert tip %}
블록을 추가하기 전에 메시지 컨테이너, 글꼴, 색상 및 기타 커스텀하려는 모든 항목에 대해 [메시지 수준 스타일을](#set-message-level-styles) 설정하세요. 그런 다음 필요에 따라 개별 블록을 커스텀할 수 있습니다. **닫기 버튼은** 메시지 상단에 유지되므로 사용자는 항상 메시지를 취소할 수 있습니다.
{% endalert %}

상자를 드래그 앤 드롭하여 선택합니다.]({% image_buster /assets/img_archive/dnd_iam_editor_blocks.png %}){: style="max-width:40%"}

모든 블록에는 패딩을 세밀하게 제어하는 등의 설정이 있습니다. 오른쪽 패널은 선택한 콘텐츠 요소의 스타일링 패널로 자동 전환됩니다. 자세한 내용은 [편집기 블록 속성을]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/drag_and_drop_editor_blocks/?sdktab=in-app%20messages#inappmessages_properties) 참조하세요.

인앱 메시지를 구축할 때 툴바에서 모바일, 태블릿 또는 데스크톱 보기를 선택하여 인앱 메시지가 사용자 그룹에 어떻게 표시될지 미리 볼 수 있습니다. 이렇게 하면 콘텐츠의 반응성이 보장되며, 그 과정에서 필요한 조정을 수행할 수 있습니다.

## 크리에이티브 세부 정보

### 큰 화면에서 전체 화면으로 보기 {#fullscreen}

태블릿 또는 데스크톱 브라우저에서는 전체 화면 인앱 메시지가 앱 화면 중앙에 표시됩니다. 전체 화면 메시지의 최대 너비에 대한 모든 편집 사항은 태블릿 및 데스크톱 기기에만 적용됩니다. 

\![전체화면 인앱 메시지 예시.]({% image_buster /assets/img_archive/dnd_iam_fullscreen_example.png %}){: style="border:none"}

### 배경 이미지 추가하기

**메시지 스타일** 탭에서 메시지 배경에 이미지를 추가할 수 있습니다. 

1. 캔버스 영역에서 배경 컨테이너를 선택합니다. 메시징의 스크롤 가능한 섹션입니다.
2. **메시지 스타일** 탭에서 **배경 이미지를** 켭니다.
3. 미디어 라이브러리에서 이미지를 추가하거나 이미지가 호스팅되는 URL을 입력합니다.

{% alert tip %}
특정 블록을 선택하는 데 문제가 있는 경우 블록의 인라인 도구 모음에서 위쪽 화살표를 사용하여 각 상위 블록으로 초점을 이동할 수 있습니다.
{% endalert %}

### Liquid 추가하기

Liquid 개인화를 추가하는 아이콘입니다.]({% image_buster /assets/img_archive/dnd_iam_liquid.png %}){: style="float:right;max-width:25%;margin-left:15px"}

인앱 메시지에 [Liquid를]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) 추가하려면 편집기 도구 모음에서 <i class="fa-solid fa-circle-plus"></i> **개인화 추가를** 선택합니다. 여기에서 기본 속성, 기기 속성, 커스텀 속성 등 다양한 개인화 유형을 추가할 수 있습니다.

그런 다음 생성된 Liquid 스니펫을 가져와 메시징에 삽입합니다. 인앱 메시지를 디자인하고 구축한 후 ** & 테스트** 미리보기로 이동하여 메시지를 미리 봅니다.

### AI 카피라이터 사용

인앱 메시지에서 텍스트 블록을 선택한 경우, 다음을 클릭합니다. <i class="fa-solid fa-wand-magic-sparkles" title="AI 카피라이터"></i> 를 클릭하여 [AI 카피라이팅 도]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/)우미를 실행합니다. AI 카피라이팅 어시스턴트는 간단한 제품 이름이나 설명을 OpenAI의 GPT3 카피 생성 도구에 전달하여 메시징을 위한 인간과 유사한 마케팅 카피를 생성합니다.

{% alert tip %}
아이콘을 클릭하기 전에 블록 내부의 텍스트를 강조 표시하여 몇 번의 클릭만으로 저장할 수 있습니다. 강조 표시된 텍스트가 도구에 추가되고 복사본이 즉시 생성됩니다.
{% endalert %}

\![AI 카피라이터의 GIF.]({% image_buster /assets/img_archive/dnd_iam_ai_copywriter.gif %})

### 스타일을 기본값으로 재설정하기

기본값 스타일에서 변경한 속성은 주황색 점으로 표시됩니다. 특정 속성을 기본값 스타일로 재설정하려면 필드 위에 마우스를 갖다 대고 **기본값으로 재설정을** 선택합니다.

텍스트 크기를 기본값으로 재설정하는 주황색 점입니다.]({% image_buster /assets/img_archive/dnd_iam_reset_styles.gif %}){: style="max-width:45%"}

선택한 요소의 모든 스타일을 초기화할 수도 있습니다. <i class="fas fa-paintbrush" title="스타일 복사 또는 붙여넣기 버튼("></i> 을 선택하고 **기본값 스타일로 재설정을** 선택하여 모든 **스타일을** 재설정할 수도 있습니다.

### 스타일 복사 및 붙여넣기

요소의 스타일을 변경한 후 해당 스타일을 복사하여 다른 요소에 붙여넣을 수 있습니다. 스타일을 붙여넣을 때 해당 요소와 관련된 속성만 적용됩니다.

스타일 복사 옵션이 있는 드롭다운 메뉴입니다.]({% image_buster /assets/img_archive/dnd_iam_copypaste_styles.png %}){: style="float:right;margin-left:15px;max-width:35%"}

1. 요소를 선택한 상태에서 다음을 선택합니다. <i class="fas fa-paintbrush" title="스타일 복사 또는 붙여넣기"></i> 을 선택합니다(예: 버튼을 선택한 경우 "버튼 속성" 옆).
2. **스타일 복사를** 클릭하고 복사한 스타일을 적용할 요소를 선택합니다.
3. 선택 <i class="fas fa-paintbrush" title="스타일 복사 또는 붙여넣기"></i> 을 다시 선택하고 **스타일 붙여넣기를** 선택합니다.

#### 키보드 단축키

키보드 단축키를 사용하여 스타일을 복사하여 붙여넣을 수도 있습니다:

| 액션       | Mac                                            | Windows                                           |
| ------------ | ---------------------------------------------- | ------------------------------------------------- |
| 스타일 복사  | <kbd>⌘</kbd> + <kbd>Shift</kbd> + <kbd>c</kbd> | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>c</kbd> |
| 스타일 붙여넣기 | <kbd>⌘</kbd> + <kbd>Shift</kbd> + <kbd>v</kbd> | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>v</kbd> |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
