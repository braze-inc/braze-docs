---
nav_title: 다국어 설정
article_title: 번역 및 다국어 설정
alias: "/multi_language_support/"
page_order: 5.5
description: "이 문서에서는 Braze 대시보드의 다국어 설정에 대한 개요와 메시징에서 로캘을 사용하는 방법에 대해 설명합니다."
---

# 번역 및 다국어 설정

> 다국어 기능을 사용하면 [번역 태그]({{ site.baseurl }}/user_guide/engagement_tools/messaging_fundamentals/localization/locales) ]를 사용하여 하나의 메시지 내에서 다양한 언어와 위치의 사용자를 타겟팅할 수 있습니다.

{% multi_lang_include locales.md section="Prerequisites" %}

## 로캘 추가

1. **설정** > **현지화 설정으로** 이동합니다.
2. 로케일을 선택 **추가 로케일**한 다음, **기본값 로케일** 또는 **커스텀 속성**을 선택합니다.<br><br>!["로케일 추가" 드롭다운에는 기본값 또는 커스텀 속성을 선택할 수 있는 옵션이 있습니다.]({% image_buster /assets/img/multi-language_support/add_locale_options.png %}){: style="max-width:40%;"}
3. 로캘의 이름을 입력합니다.
4. 선택한 지역 옵션에 대한 해당 사용자 속성을 선택하십시오.

{% tabs %}
{% tab Default locale %}

**기본값**의 로케일에 대해, 추가할 언어를 선택하기 위해 드롭다운을 사용하고, 선택적으로 언어와 연관된 국가를 선택하십시오.<br><br>!["로캘 추가 - 기본값 언어 및 국가"라는 창에서 언어와 국가를 지정할 수 있습니다.]({% image_buster /assets/img/multi-language_support/default_option.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab Custom attributes %}

**커스텀 속성**에 대해 드롭다운을 사용하여 관련 커스텀 속성을 선택하고 텍스트 필드에 값을 입력하세요.<br><br>!["로캘 추가 - 커스텀 속성"이라는 창에서 커스텀 속성과 값을 지정할 수 있습니다.]({% image_buster /assets/img/multi-language_support/custom_attributes_option.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

{: start="5"}
5\. **로캘 추가**를 선택합니다. 

이메일 캠페인 및 캔버스에서 이러한 로캘을 사용하는 단계는 [로캘 사용]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales/)을 참조하세요.

## 고려 사항

- 로케일을 설정할 때, 기본값 사용자 속성 또는 커스텀 속성에서 언어를 선택할 수 있습니다. 당신은 둘 다 선택할 수 없습니다.
- 하나의 로케일에서 최대 두 개의 커스텀 속성을 선택하거나 최대 두 개의 기본값 사용자 속성 언어를 선택할 수 있습니다. 두 경우 모두 두 번째 속성은 선택 사항입니다.
- CSV 파일에서 번역된 값을 수정할 때, 파일의 기본값을 수정하지 않도록 하십시오.
- 업로드한 파일의 로케일 키는 다국어 설정의 키와 일치해야 합니다.

### 지원 및 우선순위

- 사용자가 커스텀 속성 로케일과 일치하면 기본 사용자 속성과 일치하는 사용자보다 우선시됩니다.
- 커스텀 속성 지원은 문자열 유형과 `equals` 비교 키로 제한됩니다.
- 커스텀 속성이 삭제되거나 유형이 변경되면 사용자는 더 이상 해당 로케일에 속할 수 없으며, 그들이 속한 로케일의 우선 순위 목록으로 내려가거나 기본 마케팅 번역을 받게 됩니다.
- 로케일이 유효하지 않으면(커스텀 속성이 변경되거나 삭제된 경우) 오류가 **다국어 지원** 페이지에 나타납니다.

## Frequently asked questions

#### 로캘을 몇 개까지 추가할 수 있나요?

로캘을 최대 200개까지 추가할 수 있습니다.

#### Braze의 번역 파일은 어디에 저장되나요?

번역 파일은 캠페인 수준에서 저장되므로 각 메시지 변형에 업로드된 번역이 있어야 합니다.

#### 로캘 이름이 특정 패턴이나 형식을 따라야 하나요?

아니요. 원하는 이름 지정 규칙을 사용할 수 있습니다. 로캘 이름은 편집기에서 로캘을 선택할 때 사용되며 번역 ID와 함께 다운로드하는 파일의 제목에 표시됩니다.
