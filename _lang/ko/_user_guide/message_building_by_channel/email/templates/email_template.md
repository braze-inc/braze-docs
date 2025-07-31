---
nav_title: 이메일 템플릿 만들기
article_title: 이메일 템플릿 만들기
page_order: 0
description: "이 참조 문서에서는 이메일 템플릿을 만들고, 사용자 지정하고, 관리하는 방법에 대해 설명합니다."
tool:
  - Templates
channel:
  - email
alias: "/dnd/email_template/"
search_rank: 1
---

# 이메일 템플릿 만들기

> Braze 대시보드에는 눈길을 사로잡는 맞춤형 이메일을 작성하고 나중에 캠페인에서 사용할 수 있도록 저장할 수 있는 이메일 템플릿 편집기가 있습니다. 나만의 [HTML 이메일 템플릿을]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/html_email_template/) 업로드할 수도 있습니다.

## 1단계: 이메일 템플릿 편집기로 이동합니다.

**템플릿** > **이메일 템플릿으로** 이동합니다.

## 2단계: 편집 환경 선택 

편집 환경에 맞게 **드래그 앤 드롭 편집기** 또는 **HTML 편집기** 중에서 선택합니다. 

다음으로 미리 디자인된 Braze 템플릿 중에서 선택하거나, 새 템플릿을 만들거나, 기존 템플릿(일반 또는 [모바일 반응형][8])을 편집할 수 있습니다.

![드래그 앤 드롭 편집기 또는 HTML 편집기를 선택하거나 Braze 템플릿에서 선택할 수 있는 옵션이 포함된 회사의 봄 세일용 이메일 템플릿입니다.][2]

{% alert note %}
기존 사용자 정의 HTML 템플릿은 드래그 앤 드롭 편집기를 사용하여 다시 만들어야 합니다.
{% endalert %}

## 3단계: 템플릿 사용자 지정

편집기 환경을 선택한 후에는 이메일 템플릿을 창의적으로 사용자 지정할 수 있는 기회입니다. HTML 편집기에서 HTML을 사용하여 브랜딩을 만들고 에뮬레이션하거나 드래그 앤 드롭 편집기에서 다양한 [크리에이티브 세부 정보를]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#creative-details) 포함할 수 있습니다.

### 구독 취소 링크 포함

이메일 템플릿을 디자인할 때 수신 거부 링크를 포함하지 않으면 모든 마케팅 이메일에 법적으로 요구되는 수신 거부 링크를 이메일에 추가하라는 메시지가 표시됩니다. Liquid 태그 {% raw %}``${email_footer}``{% endraw %}를 사용하거나 템플릿에서 [바닥글을 커스텀하여]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#custom-footer) 이메일 하단에 이 수신 거부 링크를 바닥글에 추가할 수 있습니다.

## 4단계: 이메일 오류 확인

이메일 오류는 메시지 워크플로우의 **작성** 탭에 표시됩니다. 오류로 인해 앞으로 진행하지 못합니다. "경고"는 모범 사례를 따르는 데 도움이 되는 알림을 표시합니다. 비즈니스에 따라 이를 무시할 수도 있습니다.

![예시 이메일의 오류 및 경고 목록입니다.][1]{: style="float:right;max-width:40%;margin-left:15px;"}

다음은 편집기에서 설명하는 오류 목록입니다:

- 잘못된 Liquid 구문
- [이메일 본문은 400kb 이상, 본문은 102kb 이하로 작성하는 것이 좋습니다.][7]
- 구독 취소 링크가 없는 템플릿
- **본문** 또는 **제목이** 비어 있는 이메일
- 수신 거부 링크가 없는 이메일

## 5단계: 메시지 미리보기 및 테스트

템플릿 작성을 완료한 후에는 템플릿을 보내기 전에 테스트할 수 있습니다.

개요 화면 하단에서 **미리보기 및 테스트**를 클릭합니다. 여기에서 이메일이 고객의 받은 편지함에 어떻게 표시되는지 미리 볼 수 있습니다. **사용자로 미리 보기를** 선택하면 임의의 사용자로 이메일을 미리 보거나 특정 사용자를 선택하거나 사용자 지정 사용자를 만들 수 있습니다. 이를 통해 연결된 콘텐츠 및 개인화 호출이 정상적으로 작동하는지 테스트할 수 있습니다.

또한 데스크톱, 모바일 및 일반 텍스트 보기 간에 전환하여 메시지가 다양한 상황에서 어떻게 표시되는지 파악할 수 있습니다.

최종 확인이 완료되면 **테스트 전송을** 선택하고 본인 또는 콘텐츠 테스터 그룹에게 테스트 메시지를 전송하여 다양한 장치와 이메일 클라이언트에서 이메일이 제대로 표시되는지 확인합니다.

![테스트를 위해 전송할 이메일 미리보기 예시입니다.][6]

템플릿에 문제가 있거나 변경하려는 사항이 있으면 **이메일 편집을** 클릭하여 편집기로 돌아갑니다.

## 6단계: 템플릿 저장

템플릿 **저장을** 클릭하여 템플릿을 저장하세요. 이제 이 템플릿을 원하는 캠페인이나 캔버스 구성 요소에 사용할 준비가 되었습니다. 템플릿에 액세스하려면 템플릿을 만든 편집 환경을 선택한 다음 사용 가능한 템플릿 목록에서 해당 템플릿을 선택합니다.

{% alert note %}
기존 템플릿을 편집하는 경우 해당 변경 사항은 해당 템플릿의 이전 버전을 사용하여 만든 캠페인에 반영되지 않습니다.
{% endalert %}

### 템플릿 관리하기

이메일 템플릿을 더 많이 만들면 이메일 템플릿을 [복제하고]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/#duplicate-templates) [보관]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/#archive-templates)할 수 있습니다. [템플릿 및 미디어에서 템플릿 및]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/) 크리에이티브 콘텐츠 라이브러리를 만들고 관리하는 방법에 대해 자세히 알아보세요.

### API 캠페인에서 템플릿 사용

API 캠페인에 이메일을 사용하려면 Braze에서 생성한 이메일 템플릿 하단에 있는 `email_template_id`가 필요합니다.

![이메일 템플릿 하단에 있는 API 식별자입니다.][5]

### 이메일 템플릿에 댓글 달기

끌어서 놓기 편집기에서 이메일 템플릿을 공동 작업하고 댓글을 달 수 있습니다. 

1. 댓글을 달려는 이메일 본문에서 콘텐츠 블록 또는 행을 클릭합니다.
2. <i class="fas fa-comment"></i> 댓글 아이콘을 선택합니다.
3. 사이드바에 댓글을 입력한 다음 **제출**을 클릭합니다.
4. 댓글을 입력한 후 **완료**를 클릭합니다.
5. **템플릿 저장**을 클릭하여 댓글을 저장합니다.

템플릿이 저장되면 사용자는 주소가 지정되지 않은 댓글 위에 아이콘을 볼 수 있습니다. **해결**을 선택하여 이러한 댓글을 해결합니다.

!["좋아 보인다"라는 이메일 템플릿 댓글.][10]

이메일 템플릿에 대해 자주 묻는 질문에 대한 답변은 [템플릿 FAQ][9]]를 참조하세요.

[1]: {% image_buster /assets/img/dnd_compose_error.png %}
[2]: {% image_buster /assets/img/email_templates/template2.png %}
[3]: {% image_buster /assets/img/email_templates/template3.png %}
[4]: {% image_buster /assets/img/email_templates/template4.png %}
[5]: {% image_buster /assets/img/email_templates/template5.png %}
[6]: {% image_buster /assets/img_archive/newEmailTest.png %}
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/
[8]: {{site.baseurl}}/help/release_notes/2018/may/#mobile-responsive-email-templates
[9]: {{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/
[10]: {% image_buster /assets/img/email_templates/template_comment.png %}
