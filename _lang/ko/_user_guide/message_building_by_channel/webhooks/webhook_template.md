---
nav_title: 웹훅 템플릿 만들기
article_title: 웹훅 템플릿 만들기
page_order: 2
tool:
  - Templates
channel:
  - webhooks
description: "이 참조 문서에서는 나중에 Braze 플랫폼 내에서 사용할 수 있도록 웹훅 템플릿을 만들고 커스텀하는 방법에 대해 설명합니다."

---

# 웹훅 템플릿 만들기

> 웹훅을 구축하고 사용자 지정할 때, 나중에 Braze 플랫폼 내에서 사용할 수 있도록 웹훅 템플릿을 만들고 활용할 수 있습니다. 이렇게 하면 여러 캠페인에서 다양한 웹훅을 일관되게 구축할 수 있습니다.

## 1단계: 웹훅 템플릿 편집기로 이동

Braze 대시보드에서 **템플릿** > **웹훅 템플릿으로** 이동합니다.

![미리 디자인되고 저장된 웹훅 템플릿이 있는 '웹훅 템플릿' 페이지.]({% image_buster /assets/img_archive/webhook_template_campaign.png %})

## 2단계: 템플릿 선택

여기에서 새 템플릿을 만들거나 미리 디자인된 웹훅 템플릿 중 하나를 사용하거나 기존 템플릿을 편집할 수 있습니다.

예를 들어, [LINE을]({{site.baseurl}}/user_guide/message_building_by_channel/line) 메시징 채널로 사용하는 경우, 미리 디자인된 **LINE 캐러셀** 또는 **LINE 이미지용** 템플릿을 사용하여 여러 개의 웹훅을 설정할 수 있습니다.

## 3단계: 템플릿 세부 정보 작성

1. 웹훅 템플릿에 고유한 이름을 지정하세요.
2. (선택 사항) 템플릿 설명을 추가하여 이 템플릿의 사용 방법을 설명합니다.
3. 템플릿을 찾고 필터링하는 데 도움이 필요하면 [팀]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) 및 [태그]({{site.baseurl}}/user_guide/administrative/app_settings/tags/)를 추가하세요.

## 4단계: 템플릿 구축

1. 웹훅 URL을 입력합니다.
2. HTTP 방법을 선택합니다.
3. 요청 본문을 추가합니다. **JSON 키/값 쌍** 또는 **원시 텍스트가** 될 수 있습니다.
4. (선택 사항) 요청 헤더를 추가합니다. 웹훅 대상에서 요구할 수 있습니다.

![웹훅 템플릿을 만들 때 '작성' 탭입니다. 사용 가능한 필드는 웹훅 URL, HTTP 메서드, 요청 본문, 요청 헤더입니다. 언어를 추가할 수도 있습니다.]({% image_buster /assets/img_archive/Webhook_template_test.png %}){: style="max-width:90%"}

## 5단계: 템플릿 테스트

웹훅을 사용자에게 보내기 전에 웹훅이 어떻게 보이는지 확인하려면 **테스트** 탭을 사용하여 테스트 웹훅을 보낼 수 있습니다. 여기에서 무작위 사용자, 기존 사용자 또는 사용자 지정 사용자로 메시지를 미리 볼 수 있도록 선택할 수 있습니다.

## 6단계: 템플릿 저장

템플릿 **저장을** 선택하여 템플릿을 저장하세요. 이제 선택한 모든 캠페인에서 이 템플릿을 사용할 준비가 되었습니다.

{% alert note %}
기존 템플릿에 대한 편집 내용은 해당 템플릿의 이전 버전을 사용하여 만든 캠페인에는 반영되지 않습니다.
{% endalert %}

## 템플릿 관리하기

웹훅 템플릿을 [복제하고 보관하여]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) 템플릿 목록을 더 잘 정리하고 관리할 수 있습니다.

[템플릿 및 미디어에서 템플릿 및]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/) 크리에이티브 콘텐츠를 만들고 관리하는 방법에 대해 자세히 알아보세요.

