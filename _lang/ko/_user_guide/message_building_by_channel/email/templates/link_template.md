---
nav_title: 링크 템플릿
article_title: 링크 템플릿
page_order: 4
description: "이 문서는 이메일에서 다양한 유형의 링크 템플릿을 만드는 방법을 다룹니다."
tool:
  - Templates
channel:
  - email

---

# 링크 템플릿

> 링크 템플릿을 사용하면 매개변수를 추가하거나 URL을 앞에 붙여 이메일 캠페인을 위한 동적이고 재사용 가능한 링크를 만들 수 있습니다. 이것은 캠페인과 메시지 전반에 걸쳐 URL의 일관성을 생성할 수 있습니다. 

{% alert note %}
링크 템플릿은 선택적 기능입니다. **이메일 링크 템플릿**이(가) **템플릿** 섹션에 없으면 기능을 켜기 위해 계정 매니저에게 문의하세요.
{% endalert %}

## 작동 방식

링크 템플릿은 다음과 같은 사용 사례에서 가장 자주 사용됩니다:

- 주어진 이메일 메시지의 모든 링크에 Google 분석 쿼리 매개변수를 추가하기
- 주어진 이메일 메시지의 모든 링크에 URL을 앞에 추가하기

신제품 출시를 위한 프로모션 이메일 캠페인을 진행한다고 가정해 보겠습니다. 사용자는 제품 페이지로 안내하는 링크 템플릿을 사용할 수 있으며, 링크를 개인화하여 사용자의 이름이나 특정 프로모션 코드를 포함할 수 있습니다. 이것은 사용자가 링크를 클릭하고 구매한 횟수를 추적할 수 있게 해줍니다. 이렇게 하면 링크 전반에 걸쳐 일관성을 만들고 분석을 더 잘 추적할 수 있습니다.

## 링크 템플릿 만들기

무제한 링크 템플릿을 만들어 다양한 요구를 지원할 수 있습니다. 링크 템플릿을 만들려면 다음을 수행하십시오:

1. **템플릿** > **이메일 링크 템플릿**로 이동합니다. 
2. **이메일 링크 템플릿 만들기** 선택.
3. 링크 템플릿에 이름을 지정하세요.
4. (선택 사항) 링크 템플릿에 대한 세부정보를 추가하기 위해 설명, 팀 또는 태그를 추가하세요.
5. (선택 사항) 이메일 캠페인 및 캔버스의 링크에 링크 템플릿을 자동으로 추가하려면 토글을 선택하세요. 이것은 새 링크를 새 이메일이나 기존 이메일에 추가할 때 적용됩니다.

생성할 수 있는 링크 템플릿에는 두 가지 유형이 있습니다:

- [URL 앞에 삽입되는 링크 템플릿](#prepend-link-template)
- [URL 뒤에 삽입되는 링크 템플릿](#append-link-template)

링크 템플릿과 [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)을 사용할 때 Liquid는 일관된 렌더링을 보장하기 위해 본문 태그 내에만 추가해야 합니다.

### 앞에 추가: URL {#prepend-link-template} 전에 삽입하는 링크 템플릿을 만드십시오

이메일 메시지의 링크 앞에 문자열 또는 URL을 추가하려면 다음을 수행하십시오:

1. 새 링크 템플릿을 만드세요.
2. **URL 이전**에 **템플릿 위치**를 설정합니다. 
3. URL에 항상 추가될 문자열을 입력하세요. 

**템플릿 미리보기**는 링크 템플릿이 URL 앞에 어떻게 삽입될지를 보여주는 예시를 제공합니다.

![템플릿 위치, URL 앞에 URL 추가 및 링크 템플릿 삽입 프로세스를 위한 템플릿 미리보기 필드.]({% image_buster /assets/img_archive/link_template_preappend.png %}){: style="max-width:90%;"}

### 추가: URL {#append-link-template} 뒤에 삽입되는 링크 템플릿을 만드십시오

URL 뒤에 쿼리 매개변수를 추가하려면 이메일 메시지에서:

1. 새 링크 템플릿을 만드세요.
2. **URL 뒤**에 **템플릿 위치**를 설정합니다. 
3. 각 URL의 끝에 쿼리 매개변수(`value=example`)를 입력하세요. URL 끝에 여러 매개변수를 추가할 수 있습니다.

![템플릿 위치, 쿼리 매개변수 및 URL 뒤의 링크 템플릿 삽입 프로세스를 위한 템플릿 미리보기 필드.]({% image_buster /assets/img_archive/link_template_postappend.png %}){: style="max-width:90%;"}

## 이메일 캠페인에서 링크 템플릿 사용

링크 템플릿을 설정한 후 이메일에서 사용할 템플릿을 선택할 수 있습니다.

- **HTML 편집기:** **링크 관리** 탭으로 이동하여 **콘텐츠** 섹션을 확인하세요. **링크 템플릿 추가**를 선택하고, 링크 템플릿을 선택한 후 **추가**를 선택하세요.

{% alert important %}
업데이트된 HTML 이메일 편집기에서 **링크 관리** 탭에 액세스하려면 링크 별칭 지정을 켜야 합니다. 링크 별칭 지정을 켜려면 계정 매니저에게 문의하세요.
{% endalert %}

- **드래그 앤 드롭 편집기:** **콘텐츠** > **링크 관리** 탭을 선택합니다. 그런 다음, **링크 템플릿 추가**를 선택합니다. 드래그 앤 드롭 편집기에서 링크 템플릿에 액세스하려면 [링크 별칭 지정]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/)이(가) 켜져 있어야 합니다.

![드래그 앤 드롭 편집기의 링크 관리 탭에 링크 템플릿의 예제 목록이 있습니다.][1]

{% alert note %}
링크 템플릿은 일반 텍스트에 적용되지 않습니다. 이것은 커런츠가 링크 템플릿의 매개변수를 포함하지 않는 클릭을 표시할 수 있음을 의미합니다. 이러한 클릭은 이메일의 일반 텍스트 버전에서 올 수 있습니다.
{% endalert %}

**링크 관리** 탭에 링크 템플릿을 추가하면 추가한 템플릿을 보려면 오른쪽으로 스크롤하십시오. If existing links within an email already have a link template added, newly added links will also have the link template added by default.

## 링크 템플릿 관리

You can also [duplicate]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) link templates. [템플릿 및 미디어]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/)에서 템플릿 및 창의적인 콘텐츠를 만들고 관리하는 방법에 대해 자세히 알아보세요.

{% alert important %}
링크 템플릿에 대한 템플릿 보관은 현재 사용할 수 없습니다.
{% endalert %}

## 자주 묻는 질문

링크 템플릿에 대한 자주 묻는 질문에 대한 답변은 [템플릿 FAQ][10] 페이지를 확인하세요.

[1]:{% image_buster /assets/img_archive/link_template_messagecomposer2.png %}
[2]:{% image_buster /assets/img_archive/link_template_postappend.png %}
[3]:{% image_buster /assets/img_archive/link_template_preappend.png %}
[4]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/Liquid/
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/
[11]: {% image_buster /assets/img_archive/create_link_template.png %}
