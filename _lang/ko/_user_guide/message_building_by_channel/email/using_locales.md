---
nav_title: 메시지의 로캘
article_title: 메시지의 로캘
page_order: 6.3
description: "이 문서에서는 메시징에서 로캘을 사용하는 방법에 대한 단계를 설명합니다."
---

# 메시징의 로캘

> 워크스페이스에 로캘을 추가한 후에는 하나의 이메일 메시지 내에서 다양한 언어의 사용자를 타겟팅할 수 있습니다.

## 전제 조건

[다국어 지원]({{site.baseurl}}/multi_language_support/)을 편집하고 관리하려면 "다국어 설정 관리" 사용자 권한이 있어야 합니다. 메시지에 로캘을 추가하려면 캠페인을 편집할 수 있는 권한이 필요합니다.

{% alert important %}
Multi-language support and locales in messages are currently in early access. Contact your Braze account manager if you’re interested in participating in this early access.
{% endalert %}

## 로캘 사용

메시징에 로캘을 사용하려면 이메일 캠페인이나 캔버스를 작성하세요. HTML 편집기 또는 드래그 앤 드롭 편집기를 선택한 다음 편집기에 따라 단계를 따릅니다.

{% tabs %}
{% tab HTML 편집기 %}

1. 번역하려는 텍스트를 강조 표시합니다. **번역 태그 삽입**을 선택합니다. 이렇게 하면 번역 태그로 텍스트가 래핑됩니다. <br>![선택한 로캘이 하나 있는 HTML 편집기]({% image_buster /assets/img/multi-language_support/html_editor_translation_tag_example.png %})
2. 메시지를 초안으로 저장합니다.
3. **다국어**를 선택하고 드롭다운을 사용하여 메시지의 로캘을 추가합니다.
4. **템플릿 다운로드를** 선택하여 번역 템플릿을 CSV 파일로 다운로드합니다. 그런 다음 CSV 파일에 번역을 입력합니다. <br>![번역 CSV 파일의 예.]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})
5. 번역 **업로드**를 선택하여 번역이 완료된 CSV 파일을 업로드합니다.

{% endtab %}
{% tab 드래그 앤 드롭 편집기 %}

1. 번역 태그 {% raw %}`{% translation %}` 및 `{% endtranslation %}`{% endraw %}을 추가하여 번역할 모든 텍스트와 이미지 또는 링크 URL을 래핑합니다. 
2. 각 번역 태그에 ID 태그를 추가합니다. 예를 들면 다음과 같습니다: {% raw %}`{% translation id_1 %}`{% endraw %} <br>![두 개의 번역 ID가 있는 드래그 앤 드롭 편집기]({% image_buster /assets/img/multi-language_support/dnd_editor_translation_example.png %})
3. 태그를 추가한 후 메시지를 초안으로 저장합니다.
4. **다국어**를 선택하고 드롭다운을 사용하여 메시지의 로캘을 추가합니다.
5. **템플릿 다운로드를** 선택하여 번역 템플릿을 CSV 파일로 다운로드합니다. 
6. CSV 파일에 번역을 입력합니다. 1단계에서 번역 태그를 직접 복사하여 붙여넣은 경우에는 CSV 파일의 **번역 태그** 열에서 `<code>` 을 제거해야 할 수 있습니다.
7. 번역 **업로드**를 선택하여 번역이 완료된 CSV 파일을 업로드합니다.

{% endtab %}
{% endtabs %}

CSV 파일의 ID 또는 로캘에 대한 변경 사항은 메시지에서 자동으로 업데이트되지 않습니다. 번역을 업데이트하려면 CSV 파일을 업데이트하고 파일을 다시 업로드하세요.

## 로캘 미리보기

**미리보기 및 테스트** 섹션에서 **다국어 사용자를** 선택하여 메시지가 예상대로 번역되는지 확인합니다.

## 번역 관리

### 론칭된 캠페인 및 캔버스에 대한 번역 편집하기

캠페인이나 캔버스가 시작된 후에도 초안 모드에서는 번역을 수정할 수 있습니다. 이는 컴포저에서 직접 번역을 편집하든, CSV 업로드를 통해 편집하든, API를 통해 편집하든 모두 적용됩니다. 

번역을 업데이트하기 전에 먼저 캠페인 또는 캔버스를 초안으로 저장해야 합니다.

1. **캠페인/캔버스 편집을** 선택한 다음 작성기에서 편집합니다.
2. **초안으로 저장을** 선택한 다음 모달에서 **예를** 선택합니다.
3. **요약 검토** 단계로 이동하여 **캠페인/캔버스 업데이트를** 선택합니다.
4. 모달에서 **캠페인/캔버스 업데이트를** 선택합니다.

출시 후 캠페인 및 캔버스 관리에 대한 자세한 내용은 [출시된 캠페인]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/) 및 [캔버스 초안 편집하기 및 출시 후 편집하기를]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/canvas_drafts/) 참조하세요.

### 캔버스 단계 또는 캠페인 및 번역 복제하기

캔버스 단계 또는 캠페인을 복제할 때, 실행 후 초안 모드에서든 초기 생성 중에든 해당 단계와 관련된 번역은 이월되지 않습니다. 필요한 번역은 새 단계 또는 캠페인에 추가해야 합니다. 캔버스 또는 캠페인을 수정할 때는 번역을 검토하고 그에 따라 업데이트해야 합니다.

### 캔버스에서 다국어 API 사용

[캔버스에서 다국어 API를]({{site.baseurl}}/api/endpoints/translations/) 사용하려면 매개변수 목록에 `workflow_id`, `step_id`, `message_variation_id` 을 포함해야 합니다.

#### 출시 후 초안에 캔버스 단계 추가

캔버스를 시작한 후에 만든 캔버스 단계와 함께 다국어 API를 사용하는 경우, API에 전달하는 `message_variation_id` 은 비어 있거나 비어 있습니다.

{% multi_lang_include locales.md section="자주 묻는 질문" %}