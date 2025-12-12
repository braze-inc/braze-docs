---
nav_title: HTML 이메일 템플릿 업로드하기
article_title: HTML 이메일 템플릿 업로드하기
page_order: 2
description: "이 참조 문서에서는 Braze 대시보드를 사용하여 HTML 이메일 템플릿을 만들고, 관리하고, 문제 해결하는 방법을 다룹니다."
tool:
  - Templates
channel:
  - email

---

# HTML 이메일 템플릿 업로드하기

> Braze 대시보드에서는 나만의 HTML 이메일 템플릿을 업로드하고 나중에 캠페인에 사용할 수 있도록 저장할 수 있습니다. 편집기를 사용하여 [이메일 템플릿을 만들]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template/) 수도 있습니다.

## 전제 조건 {#upload-requirements}

먼저 HTML 이메일 템플릿을 만들어야 합니다. 다음이 포함된 ZIP 파일이어야 합니다:

* 단일 HTML 파일 - 이메일 본문
* HTML 파일에서 참조되는 이미지 폴더
* 이미지 파일 50개 미만
* 5MB 미만이어야 합니다.

## 템플릿 업로드하기

### 1단계: 이메일 템플릿 편집기로 이동합니다.

**템플릿** > **이메일 템플릿으로** 이동합니다.

### 2단계: 업로더 열기

**템플릿 유형** 섹션에서 **HTML 편집기를** 선택하고 아래로 스크롤하여 **기본 HTML 템플릿에서 시작** 섹션으로 이동합니다. **파일에서** 선택합니다.

### 3단계: 템플릿 업로드

**파일에서 업로드를** 선택하고 컴퓨터에서 템플릿을 선택합니다. 템플릿이 업로드 요구 사항을 충족하는지 확인하려면 [전제](#upload-requirements) 조건 섹션을 참조하세요.

#### 템플릿 업로드 오류 문제 해결

HTML 템플릿 파일을 업로드할 때 받을 수 있는 몇 가지 이메일 오류 메시지가 있습니다. 오류가 발생하면 다음 표에서 일반적인 문제와 권장 해결 방법을 참조하세요:

| 오류 | 수정 |
|------|---|
|.zip 5MB 이상| 파일 크기를 줄이고 다시 업로드해 보세요.|
|.zip 손상| 파일을 검사하고 다시 업로드해 보세요. |
|누락된 HTML| HTML 파일을 ZIP 파일에 추가하고 다시 업로드해 보세요.|
|여러 HTML| HTML 파일 중 하나를 제거하고 다시 업로드해 보세요.|
|5MB 이상의 이미지| 이미지 수를 줄이고 다시 업로드해 보세요. |
|추가 이미지| 파일에 HTML 파일에 참조되지 않은 추가 이미지가 있을 수 있습니다. 이렇게 해도 실패 오류는 발생하지 않지만 여분의 이미지는 삭제됩니다. 해당 이미지가 HTML 파일에서 참조되어야 하는 이미지인 경우 콘텐츠를 확인하고 오류를 수정한 후 다시 업로드해 보세요.|
|누락된 이미지| HTML 파일에 참조된 이미지가 있지만 해당 이미지가 ZIP 파일의 이미지 폴더에 포함되어 있지 않은 경우 파일 오류가 발생합니다. 파일을 검사하여 철자 오류 등의 오류를 수정하거나 누락된 이미지를 ZIP 파일에 추가하고 다시 업로드해 보세요.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 4단계: 템플릿 완성 및 저장하기

**템플릿 저장을** 선택하여 템플릿을 저장하세요. 이제 원하는 캠페인이나 캔버스에서 이 템플릿을 사용할 준비가 되었습니다!

{% alert note %}
기존 템플릿을 편집하는 경우 해당 변경 사항은 해당 템플릿의 이전 버전을 사용하여 만든 캠페인에 반영되지 않습니다.
{% endalert %}

## API 캠페인에서 템플릿 사용하기 {#api_for_upload_email_templates}

API 캠페인에 이메일을 사용하려면 Braze에서 만든 모든 이메일 템플릿 하단에 있는 `email_template_id` 이 필요합니다.

!!! HTML 이메일 템플릿의 API 식별자 섹션입니다.]({% image_buster /assets/img_archive/email_template_id.png %}){: style="max-width:50%;"}

## 이메일 템플릿 관리하기

이메일 템플릿을 [복제하고]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) [보관할]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) 수 있습니다! [템플릿에서]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/) 템플릿과 크리에이티브 콘텐츠를 만들고 관리하는 방법에 대해 자세히 알아보세요.

## 자주 묻는 질문

이메일 템플릿에 대해 자주 묻는 질문에 대한 답변은 [이메일 및 링크 템플릿 FAQ]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/) 페이지에서 확인하세요.


