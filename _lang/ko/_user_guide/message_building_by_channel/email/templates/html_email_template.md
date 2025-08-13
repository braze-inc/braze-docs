---
nav_title: HTML 이메일 템플릿 업로드 중
article_title: HTML 이메일 템플릿 업로드 중
page_order: 2
description: "이 참조 문서에서는 Braze 대시보드를 사용하여 HTML 이메일 템플릿을 생성, 관리 및 문제를 해결하는 방법을 다룹니다."
tool:
  - Templates
channel:
  - email

---

# HTML 이메일 템플릿 업로드 중

> Braze 대시보드는 사용자가 직접 HTML 이메일 템플릿을 업로드하고 캠페인에서 나중에 사용할 수 있도록 저장할 수 있게 해줍니다. You can also [create an email template]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template/) using our editor.

## 필수 조건 {#upload-requirements}

먼저, HTML 이메일 템플릿을 만들어야 합니다. 이것은 다음을 포함하는 ZIP 파일이어야 합니다:

* 단일 HTML 파일 - 이메일 본문
* HTML 파일에서 참조되는 이미지 폴더
* 50개 미만의 이미지 파일
* 5MB 미만

## 템플릿 업로드 중

### 1단계: 이메일 템플릿 편집기로 이동

**템플릿** > **이메일 템플릿**으로 이동합니다.

### 2단계: 업로더를 열다

**템플릿 유형** 섹션에서 **HTML 편집기**를 선택하고 **기본 HTML 템플릿에서 시작** 섹션으로 스크롤합니다. **파일에서 선택**.

### 3단계: 템플릿을 업로드하세요

Select **Upload From File** and select your template from your computer. [전제 조건](#upload-requirements) 섹션을 참조하여 템플릿이 업로드 요구 사항을 충족하는지 확인하십시오.

#### 템플릿 업로드 오류 문제 해결

HTML 템플릿 파일을 업로드할 때 받을 수 있는 여러 이메일 오류 메시지가 있습니다. 오류가 발생하면 다음 표를 참조하여 일반적인 문제와 권장 수정 사항을 확인하세요.

| 오류 | 고치다 |
|------|---|
|.zip 5MB 이상| 파일 크기를 줄이고 다시 업로드해 보세요.|
|.zip 손상됨| 파일을 검사하고 다시 업로드해 보세요. |
|누락된 HTML| HTML 파일을 ZIP 파일에 추가하고 다시 업로드해 보세요.|
|다중 HTML| HTML 파일 중 하나를 제거하고 다시 업로드해 보세요.|
|5MB 이상의 이미지| 이미지 수를 줄이고 다시 업로드해 보세요. |
|추가 이미지| HTML 파일에 참조되지 않은 추가 이미지가 파일에 있을 수 있습니다. 이것은 실패 오류를 일으키지 않지만, 추가 이미지는 폐기될 것입니다. 만약 그 이미지들이 HTML 파일에서 참조되어야 한다면, 내용을 확인하고 오류를 수정한 후 다시 업로드해 보세요.|
|이미지 누락| HTML 파일에 참조된 이미지가 있지만 ZIP 파일의 이미지 폴더에 해당 이미지가 포함되어 있지 않으면 파일 오류가 발생합니다. 파일을 검사하고 오류(철자 오류와 같은)를 수정하거나 누락된 이미지를 ZIP 파일에 추가한 후 다시 업로드해 보세요.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 4단계: 마치고 템플릿을 저장하세요

Be sure to save your template by selecting **Save Template**. 이제 이 템플릿을 사용하여 원하는 모든 캠페인 또는 캔버스에서 사용할 준비가 되었습니다!

{% alert note %}
기존 템플릿을 수정하면 해당 템플릿의 이전 버전을 사용하여 생성된 캠페인에는 변경 사항이 반영되지 않습니다.
{% endalert %}

## API 캠페인 {#api_for_upload_email_templates}에서 템플릿 사용

API 캠페인에 이메일을 사용하려면 `email_template_id`가 필요하며, 이는 Braze에서 생성된 모든 이메일 템플릿 하단에서 찾을 수 있습니다.

![API Identifier section of an HTML email template.]({% image_buster /assets/img_archive/email_template_id.png %}){: style="max-width:50%;"}

## 이메일 템플릿 관리

You can [duplicate]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) and [archive]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) email templates! [템플릿]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/)에서 템플릿 및 창의적인 콘텐츠를 만들고 관리하는 방법에 대해 자세히 알아보세요.

## 자주 묻는 질문

For answers to frequently asked questions about email templates, check out our [email and link templates FAQ]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/) page.


