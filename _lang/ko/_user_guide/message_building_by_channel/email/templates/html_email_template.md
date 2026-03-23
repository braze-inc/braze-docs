---
nav_title: HTML 이메일 템플릿 업로드하기
article_title: HTML 이메일 템플릿 업로드하기
page_order: 2
description: "이 참조 문서에서는 Braze 대시보드를 사용하여 HTML 이메일 템플릿을 생성, 관리 및 문제 해결하는 방법을 다룹니다."
tool:
  - Templates
channel:
  - email

---

# HTML 이메일 템플릿 업로드하기

> Braze 대시보드를 사용하면 직접 만든 HTML 이메일 템플릿을 업로드하고 캠페인에서 나중에 사용할 수 있도록 저장할 수 있습니다. 에디터를 사용하여 [이메일 템플릿을 생성]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template/)할 수도 있습니다.

## 필수 조건 {#upload-requirements}

먼저 HTML 이메일 템플릿을 만들어야 합니다. 이것은 다음을 포함하는 ZIP 파일이어야 합니다:

* 단일 HTML 파일—이메일 본문
* HTML 파일에서 참조되는 이미지 폴더
* 50개 미만의 이미지 파일
* 5&nbsp;MB 미만

## 템플릿 업로드하기

### 1단계: 이메일 템플릿 편집기로 이동

**템플릿** > **이메일 템플릿**으로 이동합니다.

### 2단계: 업로더 열기

**템플릿 유형** 섹션에서 **HTML 편집기**를 선택하고 **기본 HTML 템플릿에서 시작** 섹션으로 스크롤합니다. **파일에서**를 선택합니다.

### 3단계: 템플릿 업로드하기

**파일에서 업로드**를 선택하고 컴퓨터에서 템플릿을 선택합니다. [필수 조건](#upload-requirements) 섹션을 참조하여 템플릿이 업로드 요구 사항을 충족하는지 확인하세요.

### 4단계: 마치고 템플릿 저장하기

**템플릿 저장**을 선택하여 템플릿을 저장하세요. 이제 이 템플릿을 원하는 캠페인이나 캔버스에서 사용할 준비가 되었습니다!

{% alert note %}
기존 템플릿을 수정하면 해당 템플릿의 이전 버전을 사용하여 생성된 캠페인에는 변경 사항이 반영되지 않습니다.
{% endalert %}

## API 캠페인에서 템플릿 사용하기 {#api_for_upload_email_templates}

API 캠페인에 이메일을 사용하려면 `email_template_id`가 필요하며, 이는 Braze에서 생성된 모든 이메일 템플릿 하단에서 찾을 수 있습니다.

![HTML 이메일 템플릿의 API 식별자 섹션.]({% image_buster /assets/img_archive/email_template_id.png %}){: style="max-width:50%;"}

## 이메일 템플릿 관리

이메일 템플릿을 [복제]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) 및 [아카이브]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/)할 수 있습니다! [템플릿]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/)에서 템플릿 및 크리에이티브 콘텐츠를 만들고 관리하는 방법에 대해 자세히 알아보세요.

## 문제 해결

HTML 템플릿 파일을 업로드할 때 여러 이메일 오류 메시지를 받을 수 있습니다. 오류가 발생하면 다음 표를 참조하여 일반적인 문제와 권장 수정 사항을 확인하세요:

| 오류 | 수정 방법 |
|------|---|
|`.zip 5&nbsp;MB 초과`| 파일 크기를 줄이고 다시 업로드해 보세요.|
|`.zip 손상됨`| 파일을 검사하고 다시 업로드해 보세요. |
|`HTML 누락`| HTML 파일을 ZIP 파일에 추가하고 다시 업로드해 보세요.|
|`다중 HTML`| HTML 파일 중 하나를 제거하고 다시 업로드해 보세요.|
|`이미지 5&nbsp;MB 초과`| 이미지 수를 줄이고 다시 업로드해 보세요. |
|`추가 이미지`| HTML 파일에서 참조되지 않은 추가 이미지가 파일에 있을 수 있습니다. 이것은 실패 오류를 일으키지 않지만 추가 이미지는 삭제됩니다. 해당 이미지가 HTML 파일에서 참조되어야 하는 경우 콘텐츠를 확인하고 오류를 수정한 후 다시 업로드해 보세요.|
|`이미지 누락`| HTML 파일에 참조된 이미지가 있지만 ZIP 파일의 이미지 폴더에 해당 이미지가 포함되어 있지 않으면 파일 오류가 발생합니다. 파일을 검사하고 오류(철자 오류 등)를 수정하거나 누락된 이미지를 ZIP 파일에 추가한 후 다시 업로드해 보세요.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Windows 컴퓨터에서 HTML 캠페인, 이메일 메시지가 포함된 캔버스 단계 또는 템플릿의 파일을 다운로드할 때 `|`(파이프 문자)가 지원되지 않으므로 ZIP 파일에서 다운로드 콘텐츠를 추출하려면 다른 애플리케이션을 사용해야 할 수 있습니다.

## 자주 묻는 질문

이메일 템플릿에 대한 자주 묻는 질문의 답변은 [이메일 및 링크 템플릿 FAQ]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/) 페이지를 확인하세요.