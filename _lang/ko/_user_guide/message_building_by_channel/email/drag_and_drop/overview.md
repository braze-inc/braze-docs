---
nav_title: 이메일 만들기
article_title: 드래그 앤 드롭으로 이메일 만들기
alias: "/dnd/overview/"
channel: email
page_order: 0
description: "이 도움말에서는 이메일 메시지를 위한 드래그 앤 드롭 편집기를 설정하고 올바르게 사용하는 방법에 대해 설명합니다."
tool:
- Campaigns
- Canvas
---

# 드래그 앤 드롭으로 이메일 만들기

> 드래그 앤 드롭 편집기를 사용하면 HTML을 사용하여 이메일 본문을 구축하지 않고도 캠페인 또는 캔버스에 대한 완전히 커스텀되고 개인화된 이메일 메시지를 만들 수 있습니다.

## 편집기 정보

드래그 앤 드롭 편집기는 [콘텐츠와](#content) [행을](#rows) 두 가지 핵심 구성 요소로 사용하여 HTML을 추가로 사용하지 않고도 워크플로를 간소화합니다.

<table style="width: 100%; table-layout: fixed;">
    <tr>
        <th style="width: 50%;">콘텐츠</th>
        <th style="width: 50%;">행</th>
    </tr>
    <tr>
        <td style="text-align: center;">
            <img src="{% image_buster /assets/img/dnd/dnd_content.png %}" alt="&apos;행&apos; 탭에는 이메일 레이아웃을 위한 다양한 구조 조합이 포함되어 있습니다." style="max-width: 100%; height: auto;">
        </td>
        <td style="text-align: center;">
            <img src="{% image_buster /assets/img/dnd/dnd_rows.png %}" alt="기본 블록, 미디어 및 고급을 포함하는 &apos;콘텐츠&apos; 탭" style="max-width: 100%; height: auto;">
        </td>
    </tr>
</table>
{: .reset-td-br-1 role="presentation"}

### 콘텐츠

**콘텐츠에는** 메시징에 사용할 수 있는 다양한 유형의 콘텐츠를 담당하는 일련의 타일이 포함되어 있습니다. 기본, 미디어, 고급의 세 가지 카테고리로 구성되어 있습니다. 

{% tabs %}
{% tab Basic %}

기본 블록은 이메일의 기초입니다. 이러한 블록을 사용하여 이메일 본문에 다음 요소를 추가할 수 있습니다:

- 제목
- 단락
- 목록
- 버튼
- 디바이더
- 스페이서

{% endtab %}
{% tab Media %}

미디어 블록을 사용하면 이미지, 동영상, 소셜 미디어 아이콘 및 링크, 사용자 지정 가능한 아이콘 등 다양한 시각적 콘텐츠를 추가할 수 있습니다.

{% endtab %}
{% tab Advanced %}

드래그 앤 드롭 편집기는 이러한 블록을 사용하여 워크플로우를 간소화하지만, 고급 블록을 사용하여 HTML을 삽입하거나 이메일 본문에 메뉴를 추가할 수도 있습니다. 자체 HTML을 사용하면 메시징이 렌더링되는 방식에 영향을 줄 수 있습니다.

{% endtab %}
{% endtabs %}

### 행

**행은** 열을 사용하여 메시지 섹션의 가로 구성을 정의하는 구조적 단위입니다. 행 또는 [콘텐츠 블록을]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/) 비울 수 있습니다. 두 개 이상의 열을 사용하면 서로 다른 콘텐츠 요소를 나란히 배치할 수 있습니다. 이렇게 하면 시작할 때 선택한 템플릿에 관계없이 메시징에 필요한 모든 구조적 요소를 추가할 수 있습니다.

#### 카드 스타일

**카드 스타일은** 열 사이에 간격을 추가하고 모서리를 둥글게 만들 수 있는 행 속성입니다. 카드 스타일 서식을 사용하면 신제품 기능, 회원 평가, 특별 행사, 뉴스 업데이트 등 가장 중요한 콘텐츠를 강조하는 데 도움이 되는 시각적으로 더욱 참여도가 높은 레이아웃을 만들 수 있습니다.

## 드래그 앤 드롭 편집기 사용하기

이메일 메시지를 캠페인으로 보내야 할지 캔버스로 보내야 할지 잘 모르시겠어요? 캠페인은 단일의 간단한 메시징 캠페인에 적합하며, 캔버스는 여러 단계의 사용자 여정에 적합합니다.

메시지를 구축할 위치를 선택한 후에는 드래그 앤 드롭으로 이메일을 만드는 단계를 살펴보겠습니다.

### 1단계: 템플릿 선택

드래그 앤 드롭 편집기를 편집 환경으로 선택한 후 선택할 수 있습니다:

- 빈 템플릿으로 시작하세요.
- 미리 디자인된 Braze 드래그 앤 드롭 이메일 템플릿을 사용하세요.
- 저장된 드래그 앤 드롭 이메일 템플릿을 사용합니다.

{% alert note %}
기존 커스텀 HTML 템플릿이나 타사에서 만든 템플릿을 사용하려면 **템플릿** > **이메일 템플릿으로** 이동하여 **드래그 앤 드롭 편집기를** 선택하여 템플릿을 다시 만들어야 편집할 수 있습니다.
{% endalert %}

**템플릿** 섹션에서 모든 템플릿에 액세스할 수도 있습니다.

템플릿을 선택하면 **이메일 배리언트** 아래에 전송 정보 및 이메일 본문이 포함된 이메일 개요가 표시됩니다. 

그런 다음 **이메일 본문 편집을** 선택하여 드래그 앤 드롭 편집기에서 이메일 구조를 디자인하기 시작합니다. 

이메일 본문 예시가 포함된 '이메일 배리언트' 섹션입니다.]({% image_buster /assets/img/dnd/dnd_emailvariant.png %})

### 2단계: 이메일 구축하기

드래그 앤 드롭 편집 환경은 세 가지 섹션으로 나뉩니다: **설정**, **콘텐츠** 및 **미리보기****보내기** ** & 테스트**. 이메일 본문 구축의 마법은 **콘텐츠** 섹션에서 이루어집니다. 이메일을 구축하기 전에 이메일 구축 환경을 안내하는 주요 구성 요소를 이해하는 것이 중요합니다. 검토가 필요한 경우 [편집기 정보를](#about-the-editor) 참조하세요.

준비가 되면 드래그 앤 드롭 콘텐츠 블록을 사용하여 이메일을 구축하세요.

1. **행** 패널을 선택합니다. 행 구성을 기본 편집기로 드래그 앤 드롭합니다. 이렇게 하면 이메일 콘텐츠의 레이아웃이 매핑됩니다.
- 새 구성은 기존 섹션의 상단 또는 하단으로 드래그해야 한다는 점에 유의하세요.
- 행 구성을 선택하면 행 배경색, 이미지 및 커스텀 열 크기를 추가로 사용자 지정할 수 있는 **행 속성** 설정이 나타납니다.
2. **콘텐츠** 패널을 선택합니다. 원하는 콘텐츠 타일을 행 구성 요소로 드래그 앤 드롭합니다.
- **콘텐츠** 타일을 기본 편집기로 드래그할 수도 있습니다. 이렇게 하면 타일에 대한 행이 생성됩니다.
- 타일을 선택하고 **콘텐츠 속성** 및 **블록 옵션에서** 필드를 조정하여 타일을 더 세분화할 수 있습니다. 여기에는 글자 간격, 패딩, 줄 높이 등을 편집하는 것이 포함됩니다.

드래그 앤 드롭 이메일을 더욱 커스텀하는 다른 방법은 [기타 사용자 지정에서](#other-customizations) 확인하세요.

이메일을 구축할 때 데스크톱 보기와 모바일 보기를 토글하여 사용자 그룹에 대한 이메일 메시징이 어떻게 표시되는지 미리 볼 수 있습니다. 이렇게 하면 콘텐츠가 반응형인지 확인하고 필요한 경우 조정할 수 있습니다.

{% alert tip %}
멋진 카피를 만드는 데 도움이 필요하신가요? [AI 카피라이팅 도]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/)우미를 사용해 보세요. 제품 이름이나 설명을 입력하면 AI가 메시징에 사용할 수 있는 사람과 유사한 마케팅 문구를 생성합니다.

드래그 앤 드롭 편집기의 스타일 설정 옆에 있는 콘텐츠 패널에 있는 카피라이터 버튼입니다.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_dnd.png %})
{% endalert %}

### 3단계: 전송 정보 추가

이메일 메시지 디자인 및 구축을 완료했으면 이제 **전송 설정** 섹션에서 전송 정보를 추가할 차례입니다.

1. **정보 보내기에서** **발신자 표시 이름 + 주소로** 이메일을 선택합니다. **표시 이름 + 주소에서 커스텀을** 선택하여 커스텀할 수도 있습니다.
2. **회신할 주소로** 이메일을 선택합니다. **답장 받는 사람 주소 사용자 지정을** 선택하여 커스텀할 수도 있습니다.
3. 다음으로, 이메일을 **BCC 주소로** 선택하여 이 주소에 이메일을 표시합니다.
4. 이메일에 제목란을 추가합니다. 선택적으로 프리헤더와 프리헤더 뒤에 공백을 추가할 수도 있습니다.

{% multi_lang_include alerts/tip_alerts.md alert='Liquid email display name and reply-to address' %}

오른쪽 패널의 미리보기가 추가한 전송 정보로 채워집니다. 이 정보는 **설정** > **이메일 환경설정** > **보내기 구성으로** 이동하여 업데이트할 수도 있습니다.

#### 이메일 헤더 개인화하기(진행 중)

**전송 설정에서** 이메일 헤더 및 추가 이메일에 대한 개인화를 추가하여 다른 이메일 서비스 제공업체에 추가 데이터를 다시 보낼 수 있습니다. 수신자의 이름을 포함하는 등 이메일 헤더를 개인화하면 이메일이 열릴 가능성도 높일 수 있습니다.

{% alert note %}
캠페인 또는 캔버스 작성기에 고급 기능이 표시됩니다. 고급 기능에서는 인라인 CSS 설정을 수정하고 헤더 또는 추가 키-값 페어(구성된 경우)를 입력할 수 있습니다.
{% endalert %}

### 4단계: 이메일 테스트

전송 정보를 추가한 후에는 마지막으로 이메일을 테스트할 차례입니다. 

**미리보기 및 테스트** 섹션으로 이동합니다. 여기에서 사용자로서 이메일을 미리 보거나 테스트 메시지를 보낼 수 있는 옵션이 있습니다. 이 섹션에는 [받은편지함 비전도]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/) 포함되어 있어 다양한 모바일 및 웹 클라이언트에서 이메일이 올바르게 렌더링되었는지 확인할 수 있습니다.

{% alert tip %}
또한 미리보기 패널의 **다크 모드 미리보기** 토글을 사용하여 다크 모드에서 이메일 본문을 보고 필요에 따라 이메일을 조정할 수 있습니다.
{% endalert %}

동일한 이메일의 세 가지 버전을 실제 편집기, 받은편지함 비전, 실제 테스트 이메일에서 볼 수 있으므로 모든 플랫폼에서 세부 사항을 조정하는 것이 중요합니다.

#### 미리보기 및 테스트 보내기
 
**사용자로 미리보기** 탭에서 다음 사용자 유형을 선택하여 메시지를 미리 볼 수 있습니다.

- **무작위 사용자:** Braze는 데이터베이스에서 무작위로 사용자를 선택하고 해당 사용자의 속성 또는 이벤트 정보를 기반으로 이메일을 미리 봅니다.
- **사용자를 선택합니다:** 이메일 주소 또는 외부 ID를 기준으로 특정 사용자를 선택할 수 있습니다. 이메일은 해당 사용자의 속성 및 이벤트 정보를 기반으로 미리 볼 수 있습니다.
- **커스텀 사용자:** 사용자를 커스텀할 수 있습니다. Braze는 사용 가능한 모든 속성과 이벤트에 대한 입력을 제공합니다. 미리보기 이메일에 보고 싶은 정보를 입력할 수 있습니다.

{% alert note %}
무작위 사용자는 세분화 기준에 포함될 수도 있고 포함되지 않을 수도 있습니다. 세그먼트 세분화는 나중에 선택되므로 현재로서는 Braze가 타겟 오디언스를 인식하지 못합니다.
{% endalert %}

**미리보기 링크 복사를** 선택하여 임의의 사용자에게 이메일이 어떻게 표시되는지 보여주는 공유 가능한 미리보기 링크를 생성하고 복사할 수도 있습니다. 링크는 7일 동안 지속되며 그 후 다시 생성해야 합니다. 

이메일 템플릿에 편집한 내용은 이전에 생성된 링크에 반영되지 않습니다. 편집 내용을 확인하려면 새 링크 미리 보기를 생성해야 합니다.

'미리보기 링크 복사' 버튼이 있는 이메일 미리 보기를 클릭하고 생성된 링크를 복사합니다.]({% image_buster /assets/img/dnd_email_link_preview.png %})

#### 받은편지함 비전 사용

받은편지함 비전을 사용하면 이메일 클라이언트와 모바일 기기의 관점에서 이메일 캠페인을 볼 수 있습니다. 받은편지함 비전을 사용하여 이메일 메시지를 테스트하려면 ** & 테스트 미리 보기** 섹션에서 **받은편지함** 비전을 선택하고 **받은편지함 비전 실행을** 선택합니다.

{% alert tip %}
이메일 메시징의 배경 이미지로 인해 이미지 사이에 흰색 선이나 끊김 현상이 나타날 수 있으므로 이메일 메시지의 세부적인 내용을 테스트하고 확인하는 것이 중요합니다.
{% endalert %}

드래그 앤 드롭 편집기를 사용하여 이메일 메시지를 디자인하고 만든 후, 나머지 캠페인 또는 캔버스를 계속 [구축하세요]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#step-4-build-the-remainder-of-your-campaign-or-canvas).

{% details About the updated HTML engine %}
드래그 앤 드롭 편집기에서 HTML을 생성하는 기본 엔진이 최적화 및 업데이트되어 HTML 파일 압축 및 렌더링과 관련된 이점이 있습니다.

내보내는 평균 HTML 데이터 풋프린트 크기가 줄어들어 로드 및 렌더링 속도가 빨라지고 모바일 클리핑이 감소하며 대역폭 소비가 줄어듭니다.

조건부 주석 및 CSS 미디어 쿼리 수를 최소화하는 다음 업데이트를 기반으로 HTML 렌더링이 개선되었습니다. 결과적으로 HTML 파일은 더 작고 효율적으로 코딩됩니다.
- `<div>` 요소 기반 디자인에서 표준 `<table>` 형식의 코드베이스로 마이그레이션
- 간결성을 위해 [편집기 블록이]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/) 다시 코드화되었습니다.
- 최종 HTML 코드는 태그 사이의 공백을 제거하기 위해 압축됩니다.
- 투명 디바이더는 자동으로 콘텐츠 패딩으로 변환됩니다.
{% enddetails %}

## 기타 커스텀 기능

드래그 앤 드롭 이메일을 계속 구축하면서 이러한 창의적인 세부 정보를 조합하여 각 이메일 본문을 추가로 커스텀하여 오디언스의 관심과 메시지에 대한 흥미를 사로잡을 수 있습니다.

{% alert tip %}
[글로벌 스타일 설정을]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings/) 사용하여 드래그 앤 드롭 편집기에 대한 커스텀 테마를 만들 수 있습니다.
{% endalert %}

### 자동 너비 이미지

이메일에 추가된 이미지는 자동으로 **자동 너비로** 설정됩니다. 이 설정을 조정하려면 **자동 너비** 설정을 토글하고 필요에 따라 너비 비율을 조정합니다.

드래그 앤 드롭 편집기의 콘텐츠 탭에서 자동 너비 옵션을 선택합니다.]({% image_buster /assets/img/dnd/dnd1.png %})

### 색상 레이어링

색상 레이어링을 사용하여 이메일 배경, 콘텐츠 영역 및 다양한 콘텐츠 구성 요소의 색상을 변경할 수 있습니다. 색상 순서는 콘텐츠 구성 요소 색상, 콘텐츠 영역 배경색, 배경색 순으로 앞뒤로 정렬됩니다.

드래그 앤 드롭 편집기의 색상 레이어링 예시.]({% image_buster /assets/img/dnd/dnd2.png %})

### 콘텐츠 패딩

\![드래그 앤 드롭 편집기의 블록 옵션.]({% image_buster /assets/img/dnd/dnd3.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

패딩을 조정하려면 아래로 스크롤하여 **차단 옵션으로** 이동한 후 **추가 옵션을** 선택합니다. 패딩을 미세하게 조정하여 이메일에 딱 맞는 모양을 만들 수 있습니다.

### 콘텐츠 배경

행 구성에 배경 이미지를 추가하여 이메일 캠페인에 더 많은 디자인 및 시각적 콘텐츠를 포함할 수 있습니다.

### 언어 속성

**설정** 탭으로 이동하여 원하는 언어를 선택하면 언어 속성을 설정할 수 있습니다. 메시징이 동적 언어 값을 가진 사용자를 대상으로 하는 경우 사용자 속성 {%raw%} `{{${language}}}` {%endraw%} 을 타겟팅할 수도 있습니다.

이메일의 '언어' 값 설정하기.]({% image_buster /assets/img/dnd/language_setting_dnd.png %}){: style="max-width:70%;"}

### 개인화

드래그 앤 드롭 편집기에 개인화를 추가하는 옵션입니다.]({% image_buster /assets/img/dnd/dnd4.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

기본 Liquid는 드래그 앤 드롭 이메일 편집기에서 지원됩니다. 이메일에 개인화된 기능을 추가하려면 다음과 같이 하세요:

1. **콘텐츠** 섹션에서 **개인화를** 선택합니다. 
2. 개인화 유형을 선택합니다. 여기에는 기본(표준) 속성, 기기 속성, 커스텀 속성 등이 포함됩니다. 
3. 추가할 속성을 검색합니다.
4. 생성된 Liquid 스니펫을 복사하여 이메일 본문에 붙여넣습니다.

이미지 블록 및 버튼 링크 유형 필드에는 Liquid 개인화가 지원되지 않습니다. 

#### 동적 이미지

이미지 소스 속성에 Liquid를 포함시켜 이메일 메시징에 동적 이미지를 포함하도록 선택할 수 있습니다. 예를 들어 정적 이미지 대신 {% raw %} `https://example.com/images/?imageBanner={{first_name}}` {% endraw %} 을 이미지 URL로 삽입하여 이미지에 사용자의 이름을 포함할 수 있습니다. 이를 통해 각 사용자에게 이메일을 개인화할 수 있습니다.

### 텍스트 방향

메시지를 작성할 때 각각의 **텍스트 방향** 버튼을 선택하여 텍스트 방향을 왼쪽에서 오른쪽으로 또는 오른쪽에서 왼쪽으로 토글할 수 있습니다. 아랍어 및 히브리어와 같은 언어로 메시지를 작성할 때 이 옵션을 사용할 수 있습니다.

텍스트 정렬을 오른쪽에서 왼쪽으로, 왼쪽에서 오른쪽으로 토글할 수 있는 버튼이 있는 이메일 드래그 앤 드롭 편집기 메뉴.]({% image_buster /assets/img/dnd/dnd_template1.png %}){: style="max-width:50%;"}

오른쪽에서 왼쪽으로 표시되는 메시징의 최종 모양은 서비스 제공업체가 어떻게 렌더링하느냐에 따라 크게 달라집니다. 최대한 정확하게 오른쪽에서 왼쪽으로 표시되는 메시지를 작성하는 모범 사례는 [오른쪽에서 왼쪽으로 메시지 만들기를]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) 참조하세요.

### HTML

#### 링크에 대한 HTML 속성

링크에 대해 '클릭 추적' 속성이 꺼져 있는 '속성' 섹션이 있습니다.]({% image_buster /assets/img/dnd_custom_attributes.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

드래그 앤 드롭 편집기에서 링크, 버튼, 이미지, 동영상을 사용하는 경우 **콘텐츠** 섹션의 **속성에서** **새 속성 추가를** 선택하여 이메일의 HTML 태그에 추가 정보를 추가할 수 있습니다. 이는 메시지 개인화, 세분화 및 스타일링에 특히 유용할 수 있습니다.

일반적인 사용 사례는 Braze를 통해 전송할 때 클릭 추적을 비활성화하기 위해 앵커 태그에 속성을 삽입하는 것입니다.

* **SendGrid:** `clicktracking = "off"`
* **SparkPost:** `data-msys-clicktrack = "0"`

또 다른 일반적인 사용 사례는 특정 링크를 유니버설 링크로 플래그를 지정하는 것입니다. 유니버설 링크는 앱으로 리디렉션되는 링크로, 사용자에게 통합된 경험을 제공합니다.

* **SendGrid:** `universal = "true"`
* **SparkPost:** `data-msys-sublink = "open-in-app"` ( [커스텀 하위 경로를](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#custom-link-sub-paths) 구성해야 함)

유니버설 링크를 설정하려면 [유니버설 링크 및 앱 링크를]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/) 참조하세요.

또는 [Branch나]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/) [AppsFlyer와]({{site.baseurl}}/partners/message_orchestration/attribution/appsflyer/appsflyer/#email-deep-linking-and-click-tracking) 같은 기여도 파트너와 통합하여 유니버설 링크를 관리할 수도 있습니다.

마지막으로, 미리 정의된 속성을 사용하여 메시징에 대한 접근성을 높일 수 있습니다. 자세한 내용은 [Braze에서 접근 가능한 메시지 구축하기]({{site.baseurl}}/help/accessibility) 문서에서 자세히 알아보세요.

#### 커스텀 헤드 태그

`<head>` 태그를 사용하여 이메일 메시징에 CSS 및 메타데이터를 추가하세요. 예를 들어 이러한 태그를 사용하여 스타일시트 또는 파비콘을 추가할 수 있습니다. Liquid는 `<head>` 태그에서 지원됩니다.

`<head>` 태그 외부에 추가되는 모든 내용은 이메일의 `<body>` 태그 뒤에 추가됩니다. 즉, 추가된 콘텐츠가 이메일에 표시됩니다.

##### 허용되는 태그 및 태그별 속성

| 태그 이름 | 설명 | 예 |
| --- | --- | --- |
| `base` | 메시징에 있는 모든 상대 URL의 기본 URL을 지정합니다. | `<base href="https://example.com" target="_blank">` |
| `link`| 메시지와 외부 리소스 간의 관계를 정의합니다. | `<link href="styles.css" rel="stylesheet" type="text/css">` |
| `meta` | 페이지 설명 또는 키워드와 같은 메타데이터를 제공합니다. | `<meta name="description" content="Free Web tutorials">` |
| `style` | 내부 CSS 스타일을 포함합니다. | `<style type="text/css" media="screen">body { font-size: 16px; }</style>` |
| `title` | 브라우저 탭에 표시되는 설명서의 제목을 설정합니다. | `<title>StyleRyde</title>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

| 태그 | 속성 | 설명 | 예 |
| --- | --- | --- | --- |
| `base` | `href` | 상대 URL에 사용할 기본 URL입니다. | ```<base href="https://braze.com">``` |
| `base` | `target`| 모든 하이퍼링크 및 양식의 기본값 타겟팅입니다. | ```<base target="_blank">``` |
| `link` | `href` | 외부 리소스에 대한 URL을 입력합니다. | ```<link href="style.css">``` |
| `link` | `rel` | 현재 메시지와 연결된 메시지 간의 관계를 정의합니다. | ```<link rel="stylesheet">``` |
| `link` | `type` | 연결된 리소스 유형입니다. | ```<link type="text/css">``` |
| `link` | `sizes` | 아이콘의 크기를 지정합니다. | ```<link rel="icon" sizes="32x32" href="favicon-32.png">``` |
| `link` | `media` | 스타일이 적용되는 미디어 또는 기기를 지정합니다. | ```<link rel="stylesheet" media="screen" href="style.css">``` |
| `meta` | `name` | 브라우저 탭에 표시되는 설명서의 제목을 설정합니다. | ```<meta name="viewport" content="width=device-width, initial-scale=1">``` |
| `meta` | `content` | 브라우저 탭에 표시되는 설명서의 제목을 설정합니다. | ```<meta name="description" content="Page about our newest products">``` |
| `meta` | `charset` | 문자 인코딩을 선언합니다. | ```<meta charset="UTF-8">``` |
| `meta` | `property` | 브라우저 탭에 표시되는 설명서의 제목을 설정합니다. | ```<meta property="og:title" content="Website title">``` |
| `style` | `type` | 스타일 콘텐츠의 MIME 유형입니다. | {% raw %}```<style type="text/css">p { color: red; }</style>```{% endraw %} |
| `style` | `media` | 스타일이 적용되는 미디어 또는 기기를 지정합니다. | ```<style media="print">body { font-size: 12pt; }</style>``` |
| `title` | 기여도 속성 없음 | `title` 태그는 어떤 속성도 허용하지 않습니다. | ```<title>Kitchenerie</title>``` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }
