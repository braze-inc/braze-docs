---
nav_title: 메시지의 로캘
article_title: 메시지의 로캘
page_order: 4
alias: /iam_locales/
description: "이 문서에서는 인앱 메시지에서 로케일을 사용하는 방법에 대한 단계를 제공합니다."
---

# 메시지의 로케일

> 작업 공간에 로케일을 추가한 후, 단일 인앱 메시지 내에서 다양한 언어로 사용자에게 타겟팅할 수 있습니다.

{% multi_lang_include locales.md section="Prerequisites" %}

## 로캘 사용

메시징에서 로케일을 사용하려면 인앱 메시지 캠페인 또는 캔버스를 작성하십시오. 드래그 앤 드롭 편집기 또는 전통적인 편집기 중 하나를 선택한 후, 편집기에 따라 단계를 따르십시오.

{% tabs %}
{% tab 전통적인 편집기 %}

1. 번역 태그 {% raw %}`{% translation %}` 및 `{% endtranslation %}`{% endraw %}을 추가하여 번역할 모든 텍스트와 이미지 또는 링크 URL을 래핑합니다. 
2. 각 번역 태그에 ID 태그를 추가합니다. 예를 들면 다음과 같습니다: {% raw %}`{% translation id_1 %}`{% endraw %}

![번역 ID가 있는 전통적인 편집기.]({% image_buster /assets/img/multi-language_support/html_iam_editor_translation_tags.png %}){: style="max-width:60%;"}

{: start="3"}
3. 태그를 추가한 후 메시지를 초안으로 저장합니다.
4. **언어 관리**를 선택하고 드롭다운을 사용하여 메시지에 대한 로케일을 추가하십시오.

!["언어 관리" 모달에 선택된 로케일이 하나 있습니다.]({% image_buster /assets/img/multi-language_support/manage_languages_modal.png %})

{: start="5"}
5. **템플릿 다운로드를** 선택하여 번역 템플릿을 CSV 파일로 다운로드합니다. 그런 다음 CSV 파일에 번역을 입력합니다.

![번역 CSV 파일의 예.]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})

{: start="6"}
6. 번역 **업로드**를 선택하여 번역이 완료된 CSV 파일을 업로드합니다.

{% endtab %}
{% tab 드래그 앤 드롭 편집기 %}

1. 번역 태그 {% raw %}`{% translation %}` 및 `{% endtranslation %}`{% endraw %}을 추가하여 번역할 모든 텍스트와 이미지 또는 링크 URL을 래핑합니다. 
2. 각 번역 태그에 ID 태그를 추가합니다. 예를 들면 다음과 같습니다: {% raw %}`{% translation id_1 %}`{% endraw %} 

![번역 ID가 두 개 있는 드래그 앤 드롭 편집기.]({% image_buster /assets/img/multi-language_support/dnd_iam_editor_translation_tags.png %}){: style="max-width:70%;"}

{: start="3"}
3. 태그를 추가한 후, 메시지를 초안으로 저장하고 편집기를 다시 열어보십시오.
4. **구축** 패널에서 **다국어**를 선택하고 드롭다운을 사용하여 메시지에 대한 로케일을 추가하십시오.
5. **템플릿 다운로드를** 선택하여 번역 템플릿을 CSV 파일로 다운로드합니다. 

!["다국어" 패널에 템플릿 다운로드 버튼이 있습니다.]({% image_buster /assets/img/multi-language_support/dnd_iam_download_template.png %}){: style="max-width:40%;"}

{: start="6"}
6. CSV 파일에 번역을 입력합니다. 1단계에서 번역 태그를 직접 복사하여 붙여넣은 경우에는 CSV 파일의 **번역 태그** 열에서 `<code>` 을 제거해야 할 수 있습니다.
7. 번역 **업로드**를 선택하여 번역이 완료된 CSV 파일을 업로드합니다.

!["다국어" 패널에 템플릿 다운로드 및 번역 업로드 버튼이 있습니다.]({% image_buster /assets/img/multi-language_support/dnd_iam_upload_translations.png %}){: style="max-width:40%;"}

{% endtab %}
{% endtabs %}

CSV 파일의 ID 또는 로캘에 대한 변경 사항은 메시지에서 자동으로 업데이트되지 않습니다. 번역을 업데이트하려면 CSV 파일을 업데이트하고 파일을 다시 업로드하세요.

{% alert tip %}
[번역 API를]({{site.baseurl}}/api/endpoints/translations) 확인하여 캠페인과 캔버스에서 번역을 관리하고 업데이트하세요.
{% endalert %}

{% multi_lang_include locales.md section="Preview" %}

{% multi_lang_include locales.md section="Frequently Asked Questions" %}