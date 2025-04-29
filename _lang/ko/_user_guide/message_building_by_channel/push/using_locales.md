---
nav_title: 메시지의 로캘
article_title: 메시지의 로캘
page_order: 9
description: "이 문서에서는 푸시 알림에서 로캘을 사용하는 방법에 대한 단계를 설명합니다."
---

# 메시지의 로캘

> 작업 영역에 로캘을 추가한 후에는 하나의 푸시 알림 내에서 다양한 언어의 사용자를 타겟팅할 수 있습니다.

## Prerequisites

[다국어 지원]({{site.baseurl}}/multi_language_support/)을 편집하고 관리하려면 "다국어 설정 관리" 사용자 권한이 있어야 합니다. 메시지에 로캘을 추가하려면 캠페인을 편집할 수 있는 권한이 필요합니다.

## 로캘 사용

메시징에 로캘을 사용하려면 푸시 캠페인 또는 캔버스를 작성하고 다음을 완료하세요:

1. 번역 태그 {% raw %}`{% translation %}` 및 `{% endtranslation %}`{% endraw %}을 추가하여 번역할 모든 텍스트와 이미지 또는 링크 URL을 래핑합니다.<br><br>![제목 및 메시지 필드에 번역 태그가 추가된 푸시 알림 작성기.]({% image_buster /assets/img/multi-language_support/push_translation_tags.png %})<br><br>
2. 메시지를 초안으로 저장합니다.
3. **언어 관리를** 선택하고 드롭다운을 사용하여 메시지의 로캘을 추가합니다.
4. **템플릿 다운로드를** 선택한 다음 CSV 템플릿 내에서 번역을 입력합니다. <br><br>![]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})<br><br>
5. 완성된 CSV 템플릿을 업로드하려면 **번역 업로드를** 선택합니다. <br><br>![두 개의 로캘이 선택되어 있는 '다국어 메시지' 창과 템플릿을 다운로드하거나 번역을 업로드하는 버튼이 있습니다.]({% image_buster /assets/img/multi-language_support/upload_translation.png %})

번역을 업데이트하려면 CSV를 업데이트하고 파일을 다시 업로드하세요. 즉, CSV의 ID 또는 로캘에 대한 변경 사항은 메시지에서 자동으로 업데이트되지 않습니다.

{% alert tip %}
[번역 API를]({{site.baseurl}}/api/endpoints/translations) 확인하여 캠페인과 캔버스에서 번역을 관리하고 업데이트하세요.
{% endalert %}

## 로캘 미리보기

**테스트** 탭의 **사용자로 메시지 미리보기** 드롭다운에서 **사용자 지정 사용자를** 선택하고 다른 언어를 입력하여 메시지가 예상대로 번역되는지 미리 확인합니다.

{% multi_lang_include locales.md section="자주 묻는 질문" %}
