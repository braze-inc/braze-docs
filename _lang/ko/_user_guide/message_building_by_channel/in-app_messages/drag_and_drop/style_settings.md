---
nav_title: 스타일 설정
article_title: "인앱 메시지 스타일 설정"
description: "이 참조 문서에서는 드래그 앤 드롭 편집기를 사용하여 인앱 메시지를 만들 때 사용할 수 있는 스타일링 옵션을 다룹니다."
page_order: 3
---

# 인앱 메시지 스타일 설정

> 드래그 앤 드롭 편집 경험은 두 섹션으로 나뉩니다: **빌드**와 **미리보기 및 테스트**. 이 문서에서는 편집기의 **빌드** 탭에서 작업하는 데 필요한 내용을 다루며, 이미 [인앱 메시지를 생성]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/)한 것으로 가정합니다.

!["Message styles" tab.]({% image_buster /assets/img_archive/dnd_iam_message_styles.png %}){: style="float:right;max-width:25%;margin-left:15px;max-width:30%"}

## 메시지 수준 스타일

관련된 모든 블록에 적용할 특정 스타일을 인앱 메시지의 **메시지 스타일** 탭에서 설정할 수 있습니다. 예를 들어, 메시지의 모든 텍스트의 글꼴이나 모든 링크의 색상을 커스텀할 수 있습니다.

이 섹션의 스타일은 특정 블록에 대해 재정의하지 않는 한 메시지 전반에서 사용됩니다. 메시지에 [여러 페이지]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page)가 있는 경우 디스플레이 유형 및 최대 너비를 제외한 개별 페이지에 대한 메시지 수준 스타일을 재정의할 수도 있습니다. If you try to apply both page-level and message-level styles, the page-level style will override the message-level style.

더 쉬운 디자인 경험을 위해 메시지 수준 스타일을 설정한 후 블록 수준에서 스타일을 커스텀하는 것을 권장합니다.

언제든지 **메시지 스타일** 탭으로 돌아가려면:

- 개별 블록 속성에서 닫기 X 버튼을 클릭
- 메시지 컨테이너, 메시지 닫기 X 버튼 또는 편집기 배경을 선택하십시오

### 커스텀 글꼴

`.ttf`, `.woff`, `.otf`, 및 `.woff2` 파일 형식을 글꼴로 허용합니다. 자세한 내용은 [자산 파일]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/html_in-app_messages#asset-files)을 참조하십시오.

여러 가지 변형된 글꼴 패밀리를 추가할 수 있습니다. 일부 스타일링 옵션은 커스텀 글꼴에 사용할 수 없을 수 있습니다. 현재 URL을 통해 글꼴 추가를 지원하지 않습니다.

커스텀 폰트를 추가하려면:

1. **콘텐츠** 섹션으로 이동하여 **메시지 스타일** 탭을 엽니다.
2. **커스텀 폰트 추가**를 클릭합니다.
3. 미디어 라이브러리를 사용하여 글꼴을 업로드하세요. 

{% alert note %}
메시지 수준 글꼴은 현재 메시지 및 복제된 메시지에만 적용되며, 향후 템플릿에는 적용되지 않습니다.
{% endalert %}

## 메시지 구성 요소

![A GIF showing a promotional in-app message being created.]({% image_buster /assets/img_archive/dnd_iam_create.gif %})

드래그 앤 드롭 편집기는 인앱 메시지를 작성하기 위해 두 가지 주요 구성 요소를 사용합니다: **rows** 및 **blocks**. 모든 블록은 한 줄에 배치되어야 합니다.

### 행

행은 셀을 사용하여 메시지 섹션의 가로 구성을 정의하는 구조적 단위입니다.

![Rows you can add in your in-app message.]({% image_buster /assets/img_archive/dnd_iam_rows.png %}){: style="max-width:40%"}

행을 선택하면 **열 사용자 지정** 섹션에서 필요한 열 수를 추가하거나 제거하여 서로 다른 콘텐츠 요소를 나란히 배치할 수 있습니다. 

기존 열의 크기를 조정하려면 슬라이드할 수도 있습니다.

![Adjusting columns from the "Column customization" section.]({% image_buster /assets/img_archive/dnd_iam_column_customization.gif %}){: style="max-width:40%"}

모범 사례로서, 행 내부의 블록을 포맷하기 전에 행 및 열 속성을 포맷하세요. 조정할 수 있는 많은 장소가 있으므로, 기초부터 시작하면 진행하면서 편집하기가 더 쉽습니다.

### 블록

블록은 메시지에 사용할 수 있는 다양한 유형의 콘텐츠를 나타냅니다. 기존 행 세그먼트 안에 하나를 끌어다 놓으면 셀 너비에 맞게 자동으로 조정됩니다.

{% alert tip %}
블록을 추가하기 전에 메시지 컨테이너, 글꼴, 색상 및 사용자 지정하려는 모든 항목에 대한 [메시지 수준 스타일](#set-message-level-styles)을 설정하십시오. 그런 다음 필요에 따라 개별 블록을 사용자 지정할 수 있습니다. **닫기 버튼**은 메시지의 상단 섹션에 남아 있어 사용자가 메시지를 항상 닫을 수 있는 옵션을 제공합니다.
{% endalert %}

![Drag-and-drop boxes to select from.]({% image_buster /assets/img_archive/dnd_iam_editor_blocks.png %}){: style="max-width:40%"}

모든 블록에는 패딩에 대한 세밀한 제어와 같은 설정이 있습니다. 오른쪽 패널은 선택한 콘텐츠 요소에 대한 스타일링 패널로 자동 전환됩니다. 자세한 내용은 [편집기 블록 속성]({{site.baseurl}}/editor_blocks_dnd_iam/)을 참조하십시오.

인앱 메시지를 빌드할 때 툴바에서 모바일, 태블릿 또는 데스크탑 보기를 선택하여 사용자 그룹에 대한 인앱 메시지가 어떻게 보일지 미리 볼 수 있습니다. 이것은 콘텐츠가 응답형이 되도록 보장하며, 진행 중에 필요한 모든 조정을 할 수 있습니다.

#### Span text

{% multi_lang_include span_text.md %}

## 창의적인 세부 사항

### 큰 화면에서 전체 화면 {#fullscreen}

태블릿 또는 데스크톱 브라우저에서 전체 화면 인앱 메시지는 앱 화면의 중앙에 위치합니다. 전체 화면 메시지의 최대 너비에 대한 모든 편집은 태블릿 및 데스크탑 장치에만 적용됩니다. 

![Full screen in-app message example.]({% image_buster /assets/img_archive/dnd_iam_fullscreen_example.png %}){: style="border:none"}

### 배경 이미지 추가

**메시지 스타일** 탭에서 메시지의 배경에 이미지를 추가할 수 있습니다. 

1. 캔버스 영역에서 배경 컨테이너를 선택합니다. 이것은 당신의 메시지의 스크롤 가능한 섹션입니다.
2. **메시지 스타일** 탭에서 **배경 이미지**를 켭니다.
3. 미디어 라이브러리에서 이미지를 추가하거나 이미지가 호스팅된 URL을 입력하세요.

{% alert tip %}
블록을 선택하는 데 어려움이 있다면, 블록의 인라인 도구 모음에서 위쪽 화살표를 사용하여 포커스를 각 상위 블록으로 이동할 수 있습니다.
{% endalert %}

### 액체 추가

![Icon to add Liquid personalization.]({% image_buster /assets/img_archive/dnd_iam_liquid.png %}){: style="float:right;max-width:25%;margin-left:15px"}

인앱 메시지에 [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid)을 추가하려면 편집기 도구 모음에서 <i class="fa-solid fa-circle-plus"></i> **개인화 추가**를 선택하세요. 여기에서 기본 속성, 기기 속성, 커스텀 속성 등 다양한 개인화 유형을 추가할 수 있습니다.

다음으로, 생성된 Liquid 스니펫을 메시지에 삽입하세요. 인앱 메시지를 디자인하고 빌드한 후, **미리보기 및 테스트**로 이동하여 메시지를 미리보기하십시오.

### AI 카피라이터 사용

When a text block is selected in your in-app message, click <i class="fa-solid fa-wand-magic-sparkles" title="AI copywriter"></i> in the block toolbar to launch the [AI-powered copywriting assistant]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). AI 카피라이팅 어시스턴트는 간단한 제품명이나 설명을 OpenAI의 GPT3 카피 생성 도구에 전달하여 메시징에 사람과 유사한 마케팅 카피를 생성합니다.

{% alert tip %}
아이콘을 클릭하기 전에 블록 안의 텍스트를 강조 표시하여 몇 번의 클릭을 저장할 수 있습니다. 하이라이트된 텍스트가 도구에 추가되고 복사본이 즉시 생성됩니다.
{% endalert %}

![GIF of the AI copywriter.]({% image_buster /assets/img_archive/dnd_iam_ai_copywriter.gif %})

### 스타일을 기본값으로 재설정

기본 스타일에서 변경한 속성은 주황색 점으로 표시됩니다. 특정 속성을 기본 스타일로 재설정하려면 필드 위로 마우스를 가져가 **기본값으로 재설정**을 선택하세요.

![Orange dot that resets a text size to its default size.]({% image_buster /assets/img_archive/dnd_iam_reset_styles.gif %}){: style="max-width:45%"}

선택한 요소의 모든 스타일을 재설정하려면 속성 패널 이름 옆에 있는 <i class="fas fa-paintbrush" title="스타일 복사 또는 붙여넣기 버튼"></i>을 선택하고 **기본값으로 스타일 재설정**을 선택하십시오.

### 스타일 복사 및 붙여넣기

요소의 스타일을 변경한 후, 해당 스타일을 다른 요소에 복사하여 붙여넣을 수 있습니다. 스타일을 붙여넣을 때 해당 요소와 관련된 속성만 적용됩니다.

![Dropdown menu with option to copy styles.]({% image_buster /assets/img_archive/dnd_iam_copypaste_styles.png %}){: style="float:right;margin-left:15px;max-width:35%"}

1. 요소를 선택한 상태에서 속성 패널 이름 옆에 있는 <i class="fas fa-paintbrush" title="스타일 복사 또는 붙여넣기"></i>를 선택합니다 (예: 버튼을 선택한 경우, "버튼 속성" 옆에 있습니다).
2. 클릭 **스타일 복사**를 클릭하고 복사된 스타일을 적용할 요소를 선택합니다.
3. 다시 <i class="fas fa-paintbrush" title="스타일 복사 또는 붙여넣기"></i>를 선택하고 **스타일 붙여넣기**를 선택하세요.

#### 키보드 단축키

키보드 단축키를 사용하여 스타일을 복사하고 붙여넣을 수도 있습니다:

| 작업       | Mac                                            | Windows                                           |
| ------------ | ---------------------------------------------- | ------------------------------------------------- |
| 스타일 복사  | <kbd>⌘</kbd> + <kbd>Shift</kbd> + <kbd>c</kbd> | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>c</kbd> |
| 스타일 붙여넣기 | <kbd>⌘</kbd> + <kbd>Shift</kbd> + <kbd>v</kbd> | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>v</kbd> |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
