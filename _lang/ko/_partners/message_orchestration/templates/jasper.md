---
nav_title: 재스퍼
article_title: 재스퍼
description: "이 참조 문서에서는 Braze와 Jasper의 통합에 대해 간략하게 설명합니다."
alias: /partners/jasper/
page_type: partner
search_tag: Partner
---

# 재스퍼 

> [재스퍼는](https://www.jasper.ai/) 브랜드가 블로그, 광고, 소셜 미디어 등 다양한 채널에서 고품질의 브랜드 콘텐츠를 제작, 관리, 확장할 수 있도록 지원하는 AI 기반 콘텐츠 플랫폼입니다.

_이 통합은 Jasper에서 유지 관리합니다._

## Overview

Jasper와 Braze의 통합을 통해 콘텐츠 제작과 캠페인 실행을 간소화할 수 있습니다. Jasper를 사용하면 마케팅 팀은 몇 분 안에 고품질의 브랜드 카피를 생성할 수 있습니다. 그러면 Braze는 이러한 메시지를 최적의 타이밍에 적절한 오디언스에게 전달할 수 있도록 지원합니다. 이러한 통합은 원활한 워크플로우를 촉진하고 수작업을 줄이며 더 강력한 참여 성과를 이끌어냅니다.

이 통합 기능을 사용하면 다음과 같은 이점이 있습니다:

- **빠른 캠페인 실행:** 몇 주가 아닌 몇 분 안에 캠페인을 시작하세요.
- **일관된 브랜드 목소리:** Jasper 템플릿을 사용하여 생성된 카피가 브랜드 가이드라인을 엄격하게 준수하는지 확인하세요.
- **타겟팅된 콘텐츠 생성:** 오디언스 세그먼트, 스타일 가이드, 독점 지식 항목으로 고도로 맞춤화된 메시징을 만들 수 있습니다.
- **동적 개인화:** Braze 내에서 확장 가능한 개인화를 위해 {% raw %}```{{${first_name}}}```{% endraw %} 와 같은 Liquid 입력 안내를 사용하세요.
- **오류 감소:** 자동화된 워크플로로 복사-붙여넣기 오류를 최소화하고 수동 단계를 줄일 수 있습니다.

## 필수 조건

| Requirement   | 설명  |
| ------------------- | ---------------- |
| 재스퍼 계정      | 이 파트너십을 이용하려면 Jasper 계정이 필요합니다. |
| Braze REST API 키  | 다음 권한이 있는 Braze REST API 키입니다. <br>  <br>`templates.email.create` <br> `templates.email.update` <br>`content_blocks.create` <br>`content_blocks.update` <br><br>이 키는 **설정 > API 키로** 이동하여 Braze 대시보드에서 생성할 수 있습니다.  |
| Braze REST 엔드포인트 | Your REST endpoint URL. 특정 엔드포인트는 인스턴스의 Braze URL에 따라 다릅니다. [Braze API 기본 사항을 참조하세요: 자세한 내용은 엔드포인트]({{site.baseurl}}/api/basics#endpoints) 설명서를 참조하세요. |
{: .reset-td-br-1 .rest-td-br-2 role=“presentation” }

## 통합 방법

Jasper에서 콘텐츠를 생성하고 Braze 템플릿을 업데이트하는 방법에는 두 가지가 있습니다:

1. Jasper API 직접 사용
2. Jasper Studio를 사용하여 Braze 지원 커스텀 앱 구축하기

{% tabs %}
{% tab Jasper API %}

## Method: Jasper API 직접 사용

이 방법은 Jasper 및 Braze에서 수동 설정을 거치지 않고 프로그래밍 방식으로 이메일 HTML 템플릿을 만들고 업데이트하는 데 이상적입니다.

### 1단계: Jasper 설정

1. [시작하기의](https://developers.jasper.ai/docs/getting-started-1) 안내에 따라 Jasper API 키를 생성하세요.
2. 템플릿 ID가 `skl_BC53D8AC5B4B47E8BE557EBB706E9B47` 인 Braze HTML 이메일 템플릿 생성에 최적화된 Jasper의 사전 구축된 템플릿을 사용하세요.
3. Braze HTML 이메일 템플릿의 콘텐츠 생성을 요청하는 데 필요한 다음 필드의 값을 수집합니다.

| 필드 | Description |
| --- | --- |
| `emailObjective`| 이메일의 목표를 명확하게 정의하세요. |
| `ctaLink`| 클릭 유도 문안의 URL입니다. |
| `unsubscribeLink`| 마케팅 이메일에 필요합니다. |
| `brandColor`| 브랜드의 기본 색상을 16진수 형식으로 표시합니다(예: `#4dfa8a`). |
{: .reset-td-br-1 .rest-td-br-2 role=“presentation” }

**선택적 필드**

| 필드 | Description |
| --- | --- |
|`toneId` | 브랜드 목소리 |
| `audienceId`| 오디언스 세분화 |
| `styleId`| 스타일 가이드 |
| `knowledgeIds` | 향상된 콘텐츠 컨텍스트. 최대 3개의 ID를 추가할 수 있습니다. |
{: .reset-td-br-1 .rest-td-br-2 role=“presentation” }

{: start="4"}
4\. Jasper API를 통해 템플릿을 실행하여 출력을 생성하세요. 그러면 `subject`, `preheader`, `body` (HTML 콘텐츠)가 포함된 JSON 페이로드가 생성됩니다.

{% subtabs %}
{% subtab Sample request %}

### 샘플 요청

{% raw %}
```json
curl --location 'https://api.jasper.ai/v1/templates/skl_BC53D8AC5B4B47E8BE557EBB706E9B47/run?toneId=ton_811696974b3c4db4b3ac0041685c3b7c&knowledgeIds=kno_0a62fc17529e4fe69a71f30b6f0e88a7&audienceId=aud_0199117a690a7cc98481f8700916e2a6' \
--header 'Content-Type: application/json' \
--header 'x-api-key: ••••••' \
--data '{
  "inputs": {
    "emailObjective": "Announce a webinar and highlight Jasper + Braze integration benefits. Use {{${firstname}}} in the subject and body. Body length ~400 words. Include CTA buttons for registration and footer with unsubscribe link. Apply brand color to buttons and links.",
    "ctaLink": "https://yourbrand.com/register",
    "unsubscribeLink": "{{${unsubscribe_link}}}",
    "brandColor":"#4dfa8a"
  },
  "options": {
    "outputCount": 1,
    "outputLanguage": "English",
    "inputLanguage": "English",
    "languageFormality": "less"
  }
}'
```
{% endraw %}

{% endsubtab %}
{% subtab Sample output %}

### 샘플 출력
```
{
  "subject": "GlowUp Serum is Here! Limited-Time 20% Off!",
  "preheader": "GlowUp Serum is here with a 20% launch discount for 7 days only!",
  "body": "<html> ... </html>"
}
```
{% endsubtab %}
{% endsubtabs %}

### 2단계: Braze 설정하기

1단계에서 Jasper에서 생성한 `subject`, `preheader`, `body` 를 사용하여 Braze REST API에 POST 요청을 보내 [새 이메일 템플릿을 만듭니다]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/). Braze REST API 키에 `templates.email.create` 및 `templates.email.update` 권한이 있는지 확인하세요.

### 이메일 템플릿을 생성하기 위한 샘플 Braze API 요청

```json
curl --location --request POST 'https://rest.iad-03.braze.com/templates/email/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <YOUR_BRAZE_API_KEY>' \
--data '{
  "template_name": "email_template_jasperapi_20231104T142300Z",
  "subject": "GlowUp Serum is Here! Limited-Time 20% Off!",
  "preheader": "GlowUp Serum is here with a 20% launch discount for 7 days only!",
  "body": "<html> ... </html>"
}'
```
{% endtab %}
{% tab Jasper Studio %}

## Method: Jasper Studio로 Braze 지원 커스텀 앱 구축하기

Jasper Studio는 IT 지원 없이도 맞춤형 AI 앱을 구축할 수 있는 Jasper 내 노코드 플랫폼입니다. Braze API에 맞게 특별히 포맷된 JSON 구조를 생성하는 커스텀 앱을 디자인하거나, 수동으로 추가할 수 있는 콘텐츠를 생성하여 Braze 메시징에 추가할 수 있습니다.

1. Jasper 홈 화면에서 **앱 만들기를** 선택합니다.
2. **Braze HTML 이메일 템플릿** 또는 **콘텐츠 블록 템플릿과** 같이 만들려는 앱을 지정합니다.
3. Jasper가 생성하는 입력 프롬프트 필드를 편집합니다. HTML 이메일 템플릿의 경우 제목란, 프리헤더, HTML 본문, 태그, 인라인 CSS 토글, 템플릿 이름에 대한 입력 양식을 포함할 수 있습니다.
4. 일관된 개인화 및 동적 콘텐츠를 위해 지식 임베드를 Liquid 모범 사례에 대한 안내와 통합하세요.
5. 콘텐츠 생성을 위해 LLM(대규모 언어 모델)에 제공되는 지침을 구체화합니다.
6. 원하는 출력의 예를 제공하며, 여기에는 Braze 페이로드용으로 포맷된 자동화된 JSON 출력이 포함될 수 있습니다.
7. 다음을 생성하고 내보냅니다:
- **직접 복사/붙여넣기:** 콘텐츠를 복사하여 Braze 플랫폼에 직접 붙여넣을 수 있습니다.
- **JSON 출력:** JSON 출력을 생성합니다. 그런 다음 이 페이로드를 사용하여 `curl` 또는 미들웨어를 통해 Braze 엔드포인트를 직접 호출하거나 이메일 운영 워크플로에 통합할 수 있습니다.

![Jasper Braze 커스텀 앱.]({% image_buster /assets/img/jasper/jasper_custom_app.png %})

{% subtabs %}
{% subtab Sample JSON output (custom app) %}

## 샘플 JSON 출력(커스텀 앱)

{% raw %}
```json
{
  "template_name": "email_webinar_2025",
  "subject": "Join Our Webinar, {{${firstname}}}!",
  "preheader": "Unlock the potential of seamless integration.",
  "body": "<html> ... </html>",
  "tags": ["jasperapi"],
  "should_inline_css": true
}
```
{% endraw %}

{% endsubtab %}
{% subtab Sample Braze API request (using custom app output) %}

## 샘플 Braze API 요청(커스텀 앱 출력 사용)

{% raw %}
```json
curl --location --request POST 'https://rest.iad-03.braze.com/templates/email/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <YOUR_BRAZE_API_KEY>' \
--data '{
  "template_name": "email_template_jasperapi_20231104T142300Z",
  "subject": "GlowUp Serum is Here! Limited-Time 20% Off!",
  "preheader": "GlowUp Serum is here with a 20% launch discount for 7 days only!",
  "body": "<html> ... </html>"
}'
```
{% endraw %}

{% endsubtab %}
{% endsubtabs %}

또는 마케터라면 브랜드 가이드라인에 맞게 커스텀 앱을 만들어 HTML과 복사 및 붙여넣기 없이 콘텐츠를 생성하고 Braze 템플릿을 사용하여 스타일링할 수 있습니다.

{% endtab %}
{% endtabs %}

{% alert note %}
추가 지원은 [Jasper API 설명서](https://developers.jasper.ai/reference/gettemplate-1) 및 [Jasper Studio 도움말 센터를](https://help.jasper.ai/hc/en-us/articles/36783295610395-Jasper-Studio) 참조하세요.
{% endalert %}
