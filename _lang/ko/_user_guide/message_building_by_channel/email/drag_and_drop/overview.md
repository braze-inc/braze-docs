---
nav_title: 이메일 만들기
article_title: 드래그 앤 드롭으로 이메일 만들기
alias: "/dnd/overview/"
channel: email
page_order: 0
description: "이 도움말에서는 이메일 메시지에 대한 끌어서 놓기 편집기를 설정하고 올바르게 사용하는 방법에 대해 설명합니다."
tool:
- Campaigns
- Canvas
---

# 드래그 앤 드롭으로 이메일 만들기

> 드래그 앤 드롭 편집기를 사용하여 캠페인이나 캔버스를 위해 완전히 커스텀화되고 개인화된 이메일 메시지를 만들 수 있으며, 이메일 본문을 구축하기 위해 HTML을 사용할 필요가 없습니다.

## 편집자에 대하여

드래그 앤 드롭 편집기는 [콘텐츠와](#content) [행을](#rows) 두 가지 핵심 구성 요소로 사용하여 HTML을 추가로 사용하지 않고도 워크플로우를 간소화합니다.

<table style="width: 100%; table-layout: fixed;">
    <tr>
        <th style="width: 50%;">콘텐츠</th>
        <th style="width: 50%;">행</th>
    </tr>
    <tr>
        <td style="text-align: center;">
            <img src="{% image_buster /assets/img/dnd/dnd_content.png %}" alt="The &apos;Rows&apos; tab that includes different structural combinations for your email layout." style="max-width: 100%; height: auto;">
        </td>
        <td style="text-align: center;">
            <img src="{% image_buster /assets/img/dnd/dnd_rows.png %}" alt="The &apos;Content&apos; tab that includes basic blocks, media, and advanced" style="max-width: 100%; height: auto;">
        </td>
    </tr>
</table>
{: .reset-td-br-1 role="presentation"}

### 콘텐츠

**콘텐츠**에는 메시지에서 사용할 수 있는 다양한 유형의 콘텐츠를 나타내는 일련의 타일이 포함되어 있습니다. 기본, 미디어, 고급의 세 가지 카테고리로 구성되어 있습니다. 

{% tabs %}
{% tab Basic %}

기본 블록은 이메일의 기본입니다. 이러한 블록을 사용하여 이메일 본문에 다음 요소 중 하나를 추가할 수 있습니다:

- 제목
- 단락 
- 목록
- 버튼
- 구분선
- 공백

{% endtab %}
{% tab Media %}

미디어 블록을 사용하면 이미지, 동영상, 소셜 미디어 아이콘 및 링크, 커스텀 가능한 아이콘 등 다양한 시각적 콘텐츠를 추가할 수 있습니다.

{% endtab %}
{% tab Advanced %}

드래그 앤 드롭 편집기는 이러한 블록을 사용하여 워크플로를 간소화하지만 고급 블록을 사용하여 HTML을 삽입하거나 이메일 본문에 메뉴를 추가할 수도 있습니다. 자체 HTML을 사용하면 메시지가 렌더링되는 방식에 영향을 줄 수 있다는 점에 유의하세요.

{% endtab %}
{% endtabs %}

### 행

**행**은 열을 사용하여 메시지 섹션의 가로 구성을 정의하는 구조적 단위입니다. 행 또는 [콘텐츠 블록]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/)을 비울 수 있습니다. 두 개 이상의 열을 사용하면 서로 다른 콘텐츠 요소를 나란히 배치할 수 있습니다. 이렇게 하면 시작할 때 선택한 템플릿에 관계없이 메시지에 필요한 모든 구조적 요소를 추가할 수 있습니다.

#### Cards Style

**Cards Style** is a row property that lets you add spacing between columns and round their corners. With card-style formatting, you can create more visually engaging layouts to help highlight your most important content, such as new product features, testimonials, special offers, news updates, and more.

## 드래그 앤 드롭 편집기를 사용하여

이메일 메시지를 캠페인으로 보내야 할지 캔버스로 보내야 할지 잘 모르시겠어요? 캠페인은 단일의 간단한 메시징 캠페인에 적합하며, 캔버스는 여러 단계의 사용자 여정에 적합합니다.

메시지를 구축할 위치를 선택한 후, 드래그 앤 드롭 이메일을 만드는 단계로 들어가 보겠습니다.

### 1단계: 템플릿 선택

드래그 앤 드롭 편집기를 편집 환경으로 선택한 후 다음을 선택할 수 있습니다.

- 빈 템플릿으로 시작하세요.
- 미리 디자인된 Braze 드래그 앤 드롭 이메일 템플릿을 사용하세요.
- 저장된 끌어서 놓기 이메일 템플릿을 사용합니다.

{% alert note %}
기존의 커스텀 HTML 템플릿이나 제3자가 만든 템플릿을 사용하려면, **템플릿**  >** 이메일 템플릿으로** 이동하여 **드래그 앤  드롭 편집기를 **편집 경험으로 선택하여 템플릿을 재생성해야 합니다.
{% endalert %}

**템플릿** 섹션에서 모든 템플릿에 액세스할 수도 있습니다.

템플릿을 선택하면 **이메일 변형** 아래에 전송 정보 및 이메일 본문이 포함된 이메일 개요가 표시됩니다. 

Then, select **Edit Email Body** to begin designing the email structure in the drag-and-drop editor. 

![The "Email Variants" section with an example email body.]({% image_buster /assets/img/dnd/dnd_emailvariant.png %})

### 2단계: 이메일 작성

드래그 앤 드롭 편집 환경은 세 가지 섹션으로 나뉩니다: **보내기 설정**, **콘텐츠**, **미리보기 및 테스트**. 이메일 본문 작성의 마법은 **콘텐츠** 섹션에서 이루어집니다. 이메일을 작성하기 전에 이메일 작성 환경을 안내하는 주요 구성 요소를 이해하는 것이 중요합니다. If you need to review, see [About the editor](#about-the-editor).

준비가 되면 드래그 앤 드롭 콘텐츠 블록을 사용하여 이메일을 구축하세요.

1. **행** 패널을 선택합니다. 행 구성을 기본 편집기로 끌어다 놓습니다. 이렇게 하면 이메일 콘텐츠의 레이아웃이 매핑됩니다.
- 새 구성은 기존 섹션의 상단 또는 하단으로 드래그해야 한다는 점에 유의하세요.
- When you select a row configuration, the **Row Properties** settings appear for further customization of row background colors, images, and custom column sizes.
2. **콘텐츠** 패널을 선택합니다. 원하는 콘텐츠 타일을 행 구성 요소로 끌어다 놓습니다.
- **콘텐츠** 타일을 기본 편집기로 드래그할 수도 있습니다. 이렇게 하면 타일에 대한 행이 생성됩니다.
- 타일을 선택하고 **콘텐츠 속성** 및 **블록 옵션**에서 필드를 조정하여 타일을 더 세분화할 수 있습니다. 여기에는 글자 간격, 패딩, 줄 높이 등을 편집하는 것이 포함됩니다.

드래그 앤 드롭 이메일을 더욱 사용자 정의할 수 있는 다른 방법에 대한 다른 [사용자 정의를 확인하세요.](#other-customizations)

이메일을 작성할 때 데스크톱 보기와 모바일 보기를 전환하여 사용자 그룹에 대한 이메일 메시지가 어떻게 표시되는지 미리 볼 수 있습니다. 이렇게 하면 콘텐츠가 반응형인지 확인하고 필요한 경우 조정할 수 있습니다.

{% alert tip %}
멋진 카피를 만드는 데 도움이 필요하신가요? Try using the [AI copywriting assistant]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Input a product name or description, and the AI will generate human-like marketing copy for use in your messaging.

![드래그 앤 드롭 편집기의 스타일 설정 옆 콘텐츠 패널에 있는 카피라이터 버튼.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_dnd.png %})
{% endalert %}

### 3단계: 전송 정보 추가

이메일 메시지 디자인 및 작성을 완료했다면 이제 **전송 설정** 섹션에서 전송 정보를 추가할 차례입니다.

1. **정보 보내기**에서 발신자 **표시 이름 + 주소로** 이메일을 선택합니다. **표시 이름 + 주소에서 커스텀**을 선택하여 이를 커스텀할 수도 있습니다.
2. **회신 주소**로 이메일을 선택합니다. **회신 주소 커스텀**을 선택하여 이를 커스텀할 수도 있습니다.
3. 다음으로, 이메일을 **BCC 주소**로 선택하여 이 주소에 이메일을 표시합니다.
4. 이메일에 제목을 추가합니다. 선택 사항으로 프리헤더와 프리헤더 뒤에 공백을 추가할 수도 있습니다.

오른쪽 패널의 미리보기가 추가한 전송 정보로 채워집니다. 이 정보는 **설정** > **이메일 환경설정** > **보내기 구성으로** 이동하여 업데이트할 수도 있습니다.

#### 개인화된 이메일 헤더 (고급)

**전송 설정**에서 이메일 헤더 및 이메일 추가 정보에 대한 개인 설정을 추가하여 다른 이메일 서비스 제공업체에 추가 데이터를 다시 보낼 수 있습니다. 받는 사람의 이름을 포함하는 등 이메일 헤더를 커스텀하는 것도 이메일이 열릴 가능성을 높이는 데 도움이 될 수 있습니다.

{% alert note %}
캠페인 또는 캔버스 작성기에 고급 기능이 표시됩니다. 고급 기능에서는 인라인 CSS 설정을 수정하고 헤더 또는 추가 키-값 쌍(구성된 경우)을 입력할 수 있습니다.
{% endalert %}

### 4단계: 이메일 테스트

전송 정보를 추가한 후에는 마지막으로 이메일을 테스트할 차례입니다. 

**미리보기 및 테스트** 섹션으로 이동합니다. 여기에서 사용자로서 이메일을 미리 보거나 테스트 메시지를 보낼 수 있는 옵션이 있습니다. 이 섹션에는 다양한 모바일 및 웹 클라이언트에서 이메일이 올바르게 렌더링되었는지 확인할 수 있는 받은 편지함 [비전]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/) 기능도 포함되어 있습니다.

{% alert tip %}
또한 미리보기 패널의 **다크 모드 미리보기** 토글을 사용하여 이메일 본문을 다크 모드로 보고 필요에 따라 이메일을 조정할 수도 있습니다.
{% endalert %}

동일한 이메일의 세 가지 버전을 실제 편집기, 받은편지함 비전, 실제 테스트 이메일에서 볼 수 있으므로 모든 플랫폼에서 세부 사항을 일치시키는 것이 중요합니다.

#### 미리보기 및 테스트 보내기
 
**사용자로 미리보기** 탭에서 다음 사용자 유형을 선택하여 메시지를 미리 볼 수 있습니다.

- **무작위 사용자:** Braze는 데이터베이스에서 무작위로 사용자를 선택하고 해당 사용자의 속성 또는 이벤트 정보를 기반으로 이메일을 미리 봅니다.
- **사용자 선택:** 이메일 주소 또는 외부 ID를 기준으로 특정 사용자를 선택할 수 있습니다. The email will be previewed based on that user's attributes and event information
- **사용자 지정 사용자:** 사용자를 사용자 정의할 수 있습니다. Braze는 사용 가능한 모든 속성과 이벤트에 대한 입력을 제공합니다. 미리보기 이메일에 보고 싶은 정보를 입력할 수 있습니다.

{% alert note %}
무작위 사용자는 세분화 기준에 포함될 수도 있고 포함되지 않을 수도 있습니다. 세분화는 나중에 선택되므로 현재로서는 Braze가 타겟 오디언스를 인식하지 못합니다.
{% endalert %}

You can also select **Copy preview link** to generate and copy a shareable preview link that shows what the email will look like for a random user. The link will last for seven days before it needs to be regenerated. 

Note that any edits made to an email template won't reflect in a previously generated link. You'll need to generate a new link preview to see any edits.

![Email preview with a button to "Copy preview link" and copy the generated link.]({% image_buster /assets/img/dnd_email_link_preview.png %})

#### Inbox Vision 사용

받은편지함 비전을 사용하면 이메일 클라이언트 및 모바일 기기의 관점에서 이메일 캠페인을 볼 수 있습니다. 받은편지함 비전을 사용하여 이메일 메시지를 테스트하려면 **미리 보기 및 테스트** 섹션에서 **받은편지함** 비전을 선택하고 **받은편지함 비전 실행**을 클릭합니다.

{% alert tip %}
이메일 메시지의 배경 이미지로 인해 이미지 사이에 흰색 선이나 끊김 현상이 나타날 수 있으므로 이메일 메시지의 세부적인 내용을 테스트하고 확인하는 것이 중요합니다.
{% endalert %}

After using the drag-and-drop editor to design and create your email message, continue to [build]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#step-4-build-the-remainder-of-your-campaign-or-canvas) the remainder of your campaign or Canvas.

{% details 업데이트된 HTML 엔진 정보 %}
드래그 앤 드롭 편집기에서 HTML을 생성하는 기본 엔진이 최적화 및 업데이트되어 HTML 파일 압축 및 렌더링과 관련된 이점이 있습니다.

내보낸 평균 HTML 데이터 공간 크기가 줄어들어 로딩 및 렌더링 속도가 빨라지고 모바일 클리핑이 감소하며 대역폭 소비가 줄어듭니다.

조건부 주석 및 CSS 미디어 쿼리 수를 최소화하는 다음 업데이트를 기반으로 HTML 렌더링이 개선되었습니다. 결과적으로 HTML 파일은 더 작고 효율적으로 코딩됩니다.
- `<div>` 요소 기반 디자인에서 표준 `<table>` 형식의 코드베이스로 마이그레이션
- [Editor blocks]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/) have been re-coded for conciseness
- The final HTML code is compressed to remove whitespace between tags
- 투명 디바이더는 자동으로 콘텐츠 패딩으로 변환됩니다.
{% enddetails %}

## 기타 사용자 정의

드래그 앤 드롭 이메일을 계속 작성하면서 이러한 창의적인 세부 정보를 조합하여 각 이메일 본문을 추가로 사용자 지정하여 잠재 고객의 관심과 메시지를 사로잡을 수 있습니다.

{% alert tip %}
[전역 스타일 설정을]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings/) 사용하여 드래그 앤 드롭 편집기에 대한 사용자 지정 테마를 만들 수 있습니다.
{% endalert %}

### 자동 너비 이미지

이메일에 추가된 이미지는 **자동 너비**로 자동 설정됩니다. 이 설정을 조정하려면 **자동 너비** 설정을 끄고 필요에 따라 너비 비율을 조정합니다.

![Auto width option in the Content tab of the drag-and-drop editor.]({% image_buster /assets/img/dnd/dnd1.png %})

### 색상 레이어링

색상 레이어링을 사용하여 이메일 배경, 콘텐츠 영역 및 다양한 콘텐츠 구성 요소의 색상을 변경할 수 있습니다. 색상 순서는 콘텐츠 구성 요소 색상, 콘텐츠 영역 배경색, 배경색 순으로 앞뒤로 정렬됩니다.

![Example of the color layering in the drag-and-drop editor.]({% image_buster /assets/img/dnd/dnd2.png %})

### 콘텐츠 패딩

![Block Options for the drag-and-drop editor.]({% image_buster /assets/img/dnd/dnd3.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

패딩을 조정하려면 아래로 스크롤하여 **차단 옵션으로** 이동한 후 **추가 옵션을** 선택합니다. 패딩을 미세 조정하여 이메일이 보기 좋게 보이도록 할 수 있습니다.

### 콘텐츠 배경

행 구성에 배경 이미지를 추가하여 이메일 캠페인에 더 많은 디자인 및 시각적 콘텐츠를 포함할 수 있습니다.

### 개인화 추가

![Options for adding personalization for the drag-and-drop editor.]({% image_buster /assets/img/dnd/dnd4.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

기본 Liquid는 드래그 앤 드롭 이메일 편집기에서 지원됩니다. 이메일에 개인화 설정을 추가하려면

1. **콘텐츠** 섹션에서 **개인화를** 선택합니다. 
2. 개인화 유형을 선택합니다. 여기에는 기본(표준) 속성, 기기 속성, 커스텀 속성 등이 포함됩니다. 
3. 추가할 속성을 검색합니다.
4. Copy your generated Liquid snippet and paste it in your email body.

이미지 블록 및 버튼 링크 유형 필드에는 리퀴드 개인화가 지원되지 않습니다. 

#### 동적 이미지

이미지 소스 속성에 Liquid를 포함하여 이메일 메시지에 동적 이미지를 포함하도록 선택할 수 있습니다. 예를 들어 정적 이미지 대신 {% raw %} `https://example.com/images/?imageBanner={{first_name}}` {% endraw %}를 이미지 URL로 삽입하여 이미지에 사용자의 이름을 포함할 수 있습니다. 이렇게 하면 각 사용자에게 맞춤화된 이메일을 보낼 수 있습니다.

### Change text direction

When composing your message, you can toggle the text direction between left-to-right to right-to-left by selecting the respective **Text direction** button. You might use this option when creating messages in languages like Arabic and Hebrew.

![Email drag-and-drop editor menu with button to toggle text alignment between right-to-left and left-to-right.]({% image_buster /assets/img/dnd/dnd_template1.png %}){: style="max-width:50%;"}

The final appearance of right-to-left messages depends largely on how service providers render them. For best practices on crafting right-to-left messages that display as accurately as possible, refer to [Creating right-to-left messages]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

### 링크에 HTML 속성 추가

![The "Attributes" section with the attribute "clicktracking" turned off for a link.]({% image_buster /assets/img/dnd_custom_attributes.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

끌어서 놓기 편집기에서 링크, 버튼, 이미지 및 동영상을 사용하는 경우 **콘텐츠** 섹션의 **속성에서** **새 속성 추가를** 선택하여 이메일의 HTML 태그에 추가 정보를 추가할 수 있습니다. 이는 메시지 개인화, 세분화 및 스타일링에 특히 유용할 수 있습니다.

일반적인 사용 사례는 Braze를 통해 전송할 때 클릭 추적을 비활성화하기 위해 앵커 태그에 속성을 삽입하는 것입니다.

* **SendGrid:** `clicktracking = "off"`
* **SparkPost:** `data-msys-clicktrack = "0"`

또 다른 일반적인 사용 사례는 특정 링크를 유니버설 링크로 플래그를 지정하는 것입니다. 유니버설 링크는 앱으로 리디렉션되는 링크로, 사용자에게 통합된 경험을 제공합니다.

* **SendGrid:** `universal = "true"`
* **SparkPost:** `data-msys-sublink = "open-in-app"` ( [사용자 지정 하위 경로를](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#custom-link-sub-paths) 구성해야 함)

유니버설 링크를 설정하려면 [유니버설 링크 및 앱 링크]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/)를 참조하세요.

Alternatively, you can integrate with one of our attribution partners, such as [Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/) or [AppsFlyer]({{site.baseurl}}/partners/message_orchestration/attribution/appsflyer/appsflyer/#email-deep-linking-and-click-tracking), to manage universal links.

Lastly, predefined attributes are available to help make your message accessible. Learn more at our dedicated [Building accessible messages in Braze]({{site.baseurl}}/help/accessibility) article.

### Setting a language for email

You can set the language attribute by going to the **Settings** tab and selecting the desired language. You can also target the user attribute {%raw%} `{{${language}}}` {%endraw%} if the message is intended for users with dynamic language values.

![Setting the "Language" value for an email.]({% image_buster /assets/img/dnd/language_setting_dnd.png %})

