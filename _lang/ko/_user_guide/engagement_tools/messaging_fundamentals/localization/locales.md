---
nav_title: 메시지의 로캘
article_title: 현지화 번역하기
alias: /locales_in_messages/
page_order: 0
page_type: reference
description: "이 문서에서는 메시징에서 현지화를 사용하는 방법에 대한 단계를 설명합니다."
---

# 현지화 번역하기

> 작업 영역에 현지화를 추가한 후에는 푸시, 이메일, 배너 또는 인앱 메시지 하나로 다양한 언어의 사용자를 타겟팅할 수 있습니다.

{% multi_lang_include locales.md section="Prerequisites" %}

## 로캘 사용

### 1단계: 작업 공간에서 현지화 설정하기 {#workspace-setup}

로캘 및 번역 태그를 사용하려면 먼저 [작업 영역에 로캘을 추가해야]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings) 합니다.

### 2단계: 메시징에 번역 Liquid 태그 추가하기 {#add-translation-tags}

번역 태그 {% raw %}`{% translation your_id_here %}` 및 `{% endtranslation %}`{% endraw %} 을 추가하여 번역할 모든 텍스트, 이미지 또는 링크 URL을 래핑합니다.

각 번역에는 고유한 `id`. 예를 들어 간단한 인사말을 번역할 때는 ID의 이름을 "인사말"로 지정할 수 있습니다:

{% raw %}`{% translation greeting %}Hello!{% endtranslation}`{% endraw %}

#### HTML 블록 현지화하기

더 복잡한 단락에는 여러 번역 태그가 있을 수 있습니다( ("offer_text" 및 "offer_amount"):

{% raw %}
```
{% translation offer_text %}Sign up now to save{% endtranslation %}
<b>{% translation offer_amount %}50% Off{% endtranslation %}</b>
```
{% endraw %}

{% alert important %}
번역 태그에 큰 HTML 블록을 래핑하면 스타일시트 또는 스타일링 문제가 발생할 수 있습니다. 가능한 한 가장 작은 텍스트 섹션을 줄 바꿈합니다.
{% endalert %}

#### 링크 현지화하기

앵커 태그 링크를 현지화하려면 `href` URL 속성 전체가 아닌 **언어별 부분만** 래핑해야 합니다. 전체 URL을 줄 바꿈하면 링크 서식 지정이 제대로 작동하지 않을 수 있습니다.

##### 올바른 사용법

{% raw %}
```
<a href="https://www.braze.com/{% translation link_href %}en{% endtranslation %}/page"></a>
```
{% endraw %}

##### 잘못된 사용법

{% raw %}
```
<a href="{% translation link_href %}https://www.braze.com/en/page{% endtranslation %}"></a>
```
{% endraw %}

### 3단계: 메시지 로캘 선택하기 {#choose-locales}

번역 태그를 메시징에 넣은 후 메시징의 다국어 설정으로 이동하여 이 메시지에 대해 번역할 로캘을 하나 이상 선택합니다.

![드롭다운 필드가 있는 다국어 설정으로 현지화를 선택할 수 있습니다.]({% image_buster /assets/img/multi-language_support/manage_language_dropdown.png %}){: style="max-width:80%;"}

{% tabs %}
{% tab Email %}
메시지를 편집할 때 콘텐츠 메뉴에서 **다국어를** 선택합니다.

![이메일에 대한 다국어 설정.]({% image_buster /assets/img/multi-language_support/email_multi_language.png %}){: style="max-width:45%;"}

{% endtab %}

{% tab Push %}
메시지를 편집할 때 **언어 관리를** 선택합니다.

![푸시를 위한 다국어 설정.]({% image_buster /assets/img/multi-language_support/push_manage_languages.png %})

{% endtab %}

{% tab In-app message %}
{% subtabs %}
{% subtab Drag-and-Drop Editor %}
**구축** 섹션 하단에서 **언어 관리를** 선택합니다.

![인앱 드래그 앤 드롭 메시지를 위한 다국어 설정.]({% image_buster /assets/img/multi-language_support/iam_dnd_manage_languages.png %}){: style="max-width:45%;"}

{% endsubtab %}
{% subtab Traditional editor %}

메시지를 편집할 때 **언어 관리를** 선택합니다.

![인앱 HTML 메시징에 대한 다국어 설정.]({% image_buster /assets/img/multi-language_support/iam_html_manage_languages.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Banner %}
메시지를 편집할 때 **언어 관리를** 선택합니다.

![배너의 다국어 설정.]({% image_buster /assets/img/multi-language_support/banner_manage_languages.png %})

{% endtab %}
{% endtabs %}

### 4단계: CSV 템플릿 다운로드 {#download-csv}

로캘을 선택한 후 **템플릿 다운로드를** 선택하여 선택한 번역 ID 및 로캘의 매트릭스가 포함된 CSV 템플릿을 다운로드합니다.

![en, fr, es 현지화용 CSV 예시입니다.]({% image_buster /assets/img/multi-language_support/example_translation_csv.png %}){: style="max-width:70%;"}

### 5단계: 완성된 CSV 업로드 {#upload-csv}

{% alert important %}
CSV 파일의 ID 또는 로캘에 대한 변경 사항은 메시지에서 자동으로 업데이트되지 않습니다. 번역을 업데이트하려면 CSV 파일을 업데이트하고 파일을 다시 업로드하세요.
{% endalert %}

다음은 완성된 CSV의 예시 형식입니다:

```
Variant1,,,,
,Translation tags,en,es,fr
title,We noticed you've left something behind,We noticed you've left something behind,Notamos que has dejado algo atrás,Nous avons remarqué que vous avez oublié quelque chose derrière vous
offer_text,Check out now and receive,Check out now and receive,Paga ahora y recibe,Payez maintenant et recevez
offer_amount,10% Off,10% Off,10% de Descuento,10 % de réduction
cta,CHECK OUT NOW,CHECK OUT NOW,VERIFICAR AHORA,VÉRIFIER MAINTENANT
```

### 6단계: 현지화 미리보기 {#preview-locales}

메시지를 미리 볼 때 **사용자로 미리 보기** 드롭다운에서 **다국어 사용자** 옵션을 선택합니다. 이를 통해 다양한 로캘 정의 간에 전환하여 메시징의 모든 번역을 미리 볼 수 있습니다.

![로캘 미리보기]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %})

{% alert tip %}
[번역 API를]({{site.baseurl}}/api/endpoints/translations) 확인하여 캠페인과 캔버스에서 번역을 관리하고 업데이트하세요.
{% endalert %}

## 오른쪽에서 왼쪽으로 읽는 메시지

아랍어처럼 오른쪽에서 왼쪽으로 쓰이는 언어의 번역 파일을 작성할 때는 `span` 으로 번역을 감싸서 올바른 형식이 되도록 합니다:

{% raw %}
```
{% translation your_id_here %}<span dir='rtl'>default text</span>{% endtranslation %}
```
{% endraw %}

## 번역 관리

### 론칭된 캠페인 및 캔버스에 대한 번역 편집하기

캠페인이나 캔버스가 시작된 후에도 초안 모드에서는 번역을 수정할 수 있습니다. 이는 컴포저에서 직접 번역을 편집하든, CSV 업로드를 통해 편집하든, API를 통해 편집하든 모두 적용됩니다. 

출시 후 캠페인 및 캔버스 관리에 대한 자세한 내용은 [출시된 캠페인]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/) 및 [캔버스 초안 편집하기 및 출시 후 편집하기를]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/canvas_drafts/) 참조하세요.

### 캔버스 단계 또는 캠페인 및 번역 복제하기

번역은 캔버스 단계, 캠페인 또는 캠페인 변형과 함께 복사됩니다. 이는 대상 워크스페이스에 현지화가 정의되어 있는 한 워크스페이스 간에 복사할 때도 마찬가지입니다. 캔버스 또는 캠페인을 수정할 때는 번역을 검토하고 그에 따라 업데이트해야 합니다.

### 캔버스와 함께 다국어 API 사용하기

[캔버스에서 다국어 API를]({{site.baseurl}}/api/endpoints/translations/) 사용하려면 매개변수 목록에 `workflow_id`, `step_id`, `message_variation_id` 을 포함해야 합니다.

#### 출시 후 초안에 캔버스 단계 추가

캔버스가 실행된 후 생성된 캔버스 단계와 함께 다국어 API를 사용하는 경우 API에 전달하는 `message_variation_id` 은 비어 있거나 공백으로 표시됩니다.

## Frequently asked questions

#### 내 로캘 중 하나에서 번역된 사본을 변경할 수 있나요?
예. 먼저 CSV에서 편집한 다음 파일을 다시 업로드하여 번역된 사본을 변경합니다.

#### 번역 태그를 중첩할 수 있나요?
아니요.

#### 번역이 스타일링을 위한 HTML을 지원하나요?
예. 하지만 HTML 스타일이 콘텐츠와 함께 번역되지 않았는지 확인하세요.

#### 전체 HTML 메시지를 번역 태그로 래핑할 수 있나요?
아니요, 번역 태그는 성능/성과 또는 크기 제한을 피하기 위해 가능한 한 작게 만들어야 합니다.

#### Braze는 어떤 검증 또는 추가 확인을 수행하나요?

| 시나리오                                                                                                                                                 | Braze의 유효성 검사                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| 현재 메시지와 관련된 번역 파일에 로캘이 누락되었습니다.                                                                               | 이 번역 파일은 업로드되지 않습니다.                                                                       |
| 번역 파일에 현재 이메일 메시지에서 Liquid 번역 태그 내의 텍스트와 같은 텍스트 블록이 누락되었습니다.                                | 이 번역 파일은 업로드되지 않습니다.                                                                       |
| 번역 파일에는 현재 이메일 메시지의 텍스트 블록과 일치하지 않는 기본 텍스트가 포함되어 있습니다.                                          | 이 번역 파일은 업로드되지 않습니다. 다시 업로드를 시도하기 전에 CSV에서 이 문제를 해결하세요.               |
| 번역 파일에는 **다국어 지원** 설정에 없는 로캘이 포함되어 있습니다.                                                           | 이러한 로캘은 Braze에 저장되지 않습니다.                                                                      |
| 번역 파일에는 현재 메시지에 존재하지 않는 텍스트 블록(예: 번역이 업로드될 당시의 현재 초안)이 포함되어 있습니다. | 현재 메시지에 존재하지 않는 텍스트 블록은 번역 파일에서 Braze로 저장되지 않습니다. |
| 해당 로캘이 이미 번역 파일의 일부로 메시지에 업로드된 후 메시지에서 로캘을 제거합니다.                           | 로캘을 제거하면 메시지의 로캘과 관련된 모든 번역이 제거됩니다.                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
