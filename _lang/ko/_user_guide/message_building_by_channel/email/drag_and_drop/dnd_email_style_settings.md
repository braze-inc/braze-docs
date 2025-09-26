---
nav_title: 이메일 전역 스타일 설정
article_title: 이메일 전역 스타일 설정
alias: "/dnd/global_style_settings/"
channel: email
page_order: 3
description: "이 참조 문서에서는 캠페인 및 캔버스에 대한 드래그 앤 드롭 편집기에서 글로벌 이메일 스타일 설정을 설정하는 방법에 대해 설명합니다."
tool: 
  - Campaigns
  - Canvas
---

# 이메일 글로벌 스타일 설정

> 글로벌 스타일 설정을 통해 이메일 캠페인과 캔버스의 모양을 개인화할 수 있습니다. 드래그 앤 드롭 편집기의 기본 테마를 추가하고 사용자 지정할 수 있습니다. 여기에는 이메일 제목, 텍스트, 버튼 등에 대한 스타일 편집이 포함됩니다. 이러한 설정을 조합하여 사용하면 이메일 메시징 전반에 걸쳐 일관된 디자인을 만들 수 있습니다.

전역 스타일 설정을 편집하려면 **설정** > **이메일 환경설정** > **이메일 환경설정 끌어서 놓기로** 이동하세요. After editing the styles in the drag-and-drop email editor, select **Save**. To further customize your email campaigns and Canvases, check out how you can incorporate [drag-and-drop editor blocks]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks).

![Email Global Style Settings section in the Drag-And-Drop Email Editor Settings tab.]({% image_buster /assets/img_archive/dnd_global_style_settings.png %})

{% alert note %}
글로벌 스타일 설정에 대한 업데이트는 향후 모든 이메일 캠페인과 캔버스에 적용됩니다.
{% endalert %} 

## 기본 스타일링 

**기본 스타일링**의 경우 이메일 캠페인 및 캔버스에 대한 기본 이메일 및 콘텐츠 배경색을 설정할 수 있습니다. 기본 글꼴을 선택하고, 사용자 지정 글꼴을 추가하고, 링크 색상을 편집할 수도 있습니다.

![Basic styling options that include options to edit the email and content background colors, default font name, and default link color.]({% image_buster /assets/img_archive/dnd_basic_styling.png %}) 

## 사용자 지정 글꼴

사용자 지정 글꼴을 사용하면 다양한 이메일 플랫폼에서 일관성 있는 브랜딩을 위해 웹 글꼴을 수동으로 추가할 수 있습니다. You can add one custom font for each styling section.

### Requirements

사용자 정의 글꼴을 추가하기 전에 사용자 정의 글꼴 파일이 다음 요구 사항을 충족하는지 확인하세요:

- 사용자 정의 글꼴 파일을 제공하는 서버에서 CORS가 활성화되어 있어야 합니다. 이는 일반적으로 IT 팀에서 관리합니다. 
  - 사용자 정의 글꼴 파일에는 헤더가 있어야 합니다: `Access-Control-Allow-Origin: *`
- The file URL must point to a CSS file (not WOFF or OTF).
- The custom font name must match the name of the font face in the CSS file.

Note that the custom font provider may collect personal data from your recipients. 사용하기 전에 글꼴 제공업체의 정책을 검토해야 합니다.

### Adding a custom font

To add a custom font, do the following:

1. In the **Default Font Name** section of **Basic Styling**, select **Add a custom font**.
2. **글꼴 이름** 필드에 사용자 정의 글꼴 소스 파일에 표시되는 것과 동일한 글꼴 이름을 입력합니다. Make sure this name is capitalized and spaced correctly.
3. **글꼴 URL** 필드에 해당 URL을 입력합니다.
4. Check that the preview shows your custom font.
5. Select **Save** to use the custom font as your default email font. 

{% alert important %}
Gmail은 커스텀 글꼴을 지원하지 않으므로 커스텀 글꼴이 기본 시스템 글꼴로 표시될 수 있습니다. 다른 이메일 플랫폼의 경우 이메일 메시지를 보내기 전에 커스텀 글꼴이 올바르게 표시되는지 확인하세요.
{% endalert %}

To use other custom fonts in your email campaigns, you can create an [email template]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template/) or [Content Blocks]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/) that includes the custom font. For example, you can create a specific email template designed with festive custom fonts tailored to your sale theme. 선택한 글꼴이 여전히 웹에서 안전하며 이메일 플랫폼에서 지원되는지 확인하세요.

### 대체 글꼴

기본 글꼴이 받은 편지함 공급자나 운영 체제에서 지원되지 않는 경우 제목, 머리글, 본문 텍스트에 대체 글꼴이 사용됩니다. 기본적으로 Braze는 글로벌 스타일 설정이 저장될 때 Arial을 대체 글꼴로 자동 설정합니다. 또한 기본 글꼴 모음에 세리프 또는 산세리프를 옵션으로 추가하는 옵션도 있습니다.

![An example of "Arial" as a fallback font with "Sans-serif" as the font family.]({% image_buster /assets/img_archive/dnd_fallbacks.png %})

대체 글꼴을 최대 17개까지 추가할 수 있습니다. 선택한 첫 번째 대체 글꼴이 가장 먼저 시도되는 글꼴이 됩니다. 대체 글꼴은 새로 만든 템플릿, 이메일 캠페인 및 캔버스 구성 요소에 대해서만 적용됩니다. 대체 글꼴이 지정되기 전에 작성된 메시지의 경우 대체 글꼴이 자동으로 설정되지 않습니다. 브랜딩 전반의 일관성을 유지하기 위해 이메일 메시지와 유사한 대체 글꼴을 선택하는 것이 좋습니다.

## 제목 스타일링

여기에서 글꼴 크기, 글꼴 색상 및 텍스트 정렬을 편집하여 이메일 제목의 스타일을 조정할 수 있습니다. 이는 메인 헤더와 보조 헤더에 적용됩니다. 

![Title Styling settings for a center-aligned main header and secondary header.]({% image_buster /assets/img_archive/dnd_title_styling.png %})

원하는 경우 끌어서 놓기 편집기 테마의 기본 스타일을 재정의할 수 있습니다. Select **Override default style** to apply your choice of title styling. 여기에는 다른 글꼴 및 링크 색상 설정이 포함될 수 있습니다.

## 단락 스타일링

기본 단락 스타일을 설정하려면 **단락 스타일 지정**으로 이동하여 **글꼴 크기**를 입력하고 **글꼴 색상**을 선택하여 글꼴 색상을 선택합니다. 또한 **상단 패딩**, **오른쪽 패딩**, **하단 패딩** 및 **왼쪽 패딩** 값을 편집하여 본문 텍스트의 블록 스타일을 조정할 수도 있습니다. 이는 단락 블록을 둘러싼 네 영역의 간격에 모두 적용됩니다.

![Paragraph Styling settings for text with 14pt font.]({% image_buster /assets/img_archive/dnd_paragraph_styling.png %})

## 목록 스타일링

메시지에 목록을 추가할 때 **목록 스타일** 지정 섹션을 사용하면 목록의 스타일이 일관성 있게 지정됩니다. 여기에는 다음과 같은 세부 정보가 포함됩니다: 

- 글꼴 크기
- 글꼴 색상
- 글꼴 두께
- 줄 높이
- 정렬
- 텍스트 방향
- 문자 간격
- 목록 항목 간격
- 목록 항목 들여쓰기
- 목록 유형
- 목록 스타일 유형

**목록 유형**을 번호 매기기 또는 글머리 기호로 설정할 수 있습니다. **목록 스타일 유형**은 목록 스타일에 대한 추가 커스텀 기능을 제공합니다. 예를 들어 목록 유형은 항상 글머리 기호로, 각 글머리 기호는 사각형으로 설정할 수 있습니다.  

![List Styling settings for a bulleted list.]({% image_buster /assets/img_archive/dnd_list_styling.png %})

## 버튼 스타일링

**버튼 스타일링** 섹션에서 버튼의 다음 기본 스타일을 편집할 수 있습니다:
- 배경색
- 글꼴 크기
- 글꼴 색상
- 테두리 반지름
- 테두리 색
- 테두리 무게
- 버튼 패딩

![Button Styling settings for a rectangular button with a blue background.]({% image_buster /assets/img_archive/dnd_button_styling.png %})

다른 모든 스타일링 섹션과 마찬가지로 **패딩 상단**, **패딩 오른쪽**, **패딩 하단** 및 **패딩 왼쪽** 값을 편집하여 블록 스타일링을 조정할 수 있습니다.

## 이메일 템플릿 너비

이메일 템플릿 너비를 사용하여 이메일 캠페인 전반에서 일관성을 유지할 수 있도록 너비를 조정하고 설정할 수 있습니다. 

![Email template width set to 600px.]({% image_buster /assets/img_archive/dnd_email_template_width.png %})

## 콘텐츠 블록 너비

이메일 드래그 앤 드롭 편집기에서 콘텐츠 블록 너비를 설정할 수도 있습니다. 콘텐츠 블록 너비를 이메일 템플릿 너비와 일치시키는 것이 좋습니다.

![Content Block width set to 600px.]({% image_buster /assets/img_archive/dnd_content_block_width.png %})
