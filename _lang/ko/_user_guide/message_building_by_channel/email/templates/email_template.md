---
nav_title: 이메일 템플릿 만들기
article_title: 이메일 템플릿 만들기
page_order: 0
description: "이 참조 문서에서는 이메일 템플릿을 만들고, 사용자 정의하고, 관리하는 방법을 다룹니다."
tool:
  - Templates
channel:
  - email
alias: "/dnd/email_template/"
search_rank: 1
---

# 이메일 템플릿 만들기

> Braze 대시보드에는 맞춤형으로 눈길을 끄는 이메일을 만들고 캠페인에서 나중에 사용할 수 있도록 저장할 수 있는 이메일 템플릿 편집기가 있습니다. 자신의 [HTML 이메일 템플릿]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/html_email_template/)을 업로드할 수도 있습니다.

## 1단계: 이메일 템플릿 편집기로 이동

**템플릿** > **이메일 템플릿**으로 이동합니다.

## 2단계: 편집 경험 선택 

편집 경험을 위해 **드래그 앤 드롭 편집기** 또는 **HTML 편집기** 중에서 선택합니다. 

다음으로, 미리 디자인된 Braze 템플릿 중에서 선택하거나 새 템플릿을 만들거나 기존 템플릿(일반 또는 [모바일 반응형]({{site.baseurl}}/help/release_notes/2018/may/#mobile-responsive-email-templates))을 편집할 수 있습니다.

\![회사의 봄 세일을 위한 이메일 템플릿으로, 드래그 앤 드롭 편집기 또는 HTML 편집기를 선택하거나 Braze 템플릿에서 선택할 수 있는 옵션이 있습니다.]({% image_buster /assets/img/email_templates/template2.png %})

{% alert note %}
기존의 사용자 정의 HTML 템플릿은 드래그 앤 드롭 편집기를 사용하여 다시 만들어야 합니다.
{% endalert %}

## 3단계: 템플릿 사용자 정의

편집 경험을 선택한 후, 이메일 템플릿을 사용자 정의하는 창의적인 기회를 가질 수 있습니다. HTML을 사용하여 HTML 편집기에서 브랜드를 만들고 에뮬레이트하거나 드래그 앤 드롭 편집기에서 다양한 [창의적인 세부 사항]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#creative-details)을 포함할 수 있습니다.

### 구독 취소 링크 포함

이메일 템플릿을 디자인할 때 구독 취소 링크를 포함하지 않으면, Braze는 모든 마케팅 이메일에 법적으로 요구되므로 이메일에 추가하라고 요청합니다. 이 구독 취소 링크를 Liquid 태그 {% raw %}``${email_footer}``{% endraw %}를 사용하여 이메일 하단의 바닥글로 추가하거나, 템플릿에서 [바닥글 사용자 정의]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#custom-footer)를 통해 추가할 수 있습니다.

## 4단계: 이메일 오류 확인

이메일 오류는 메시지 워크플로의 **작성** 탭에 표시됩니다. 오류는 진행을 방해합니다. "경고"는 모범 사례를 따르도록 돕기 위한 알림을 나타냅니다. 비즈니스에 따라 무시할 수도 있습니다.

\![예시 이메일의 오류 및 경고 목록.]({% image_buster /assets/img/dnd_compose_error.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

편집기에서 고려되는 오류 목록은 다음과 같습니다:

- 잘못된 Liquid 구문
- [이메일 본문이 400kb를 초과함; 본문은 102kb 미만으로 권장됨]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/)
- 구독 취소 링크가 없는 템플릿
- 빈 **본문** 또는 **제목**이 있는 이메일
- 구독 취소 링크가 없는 이메일

## 5단계: 메시지 미리보기 및 테스트

템플릿 작성을 마친 후, 발송하기 전에 테스트할 수 있습니다.

개요 화면 하단에서 **미리보기 및 테스트**를 선택합니다. 여기에서 고객의 받은 편지함에 이메일이 어떻게 표시되는지 미리 볼 수 있습니다. **사용자 미리보기**가 선택되면 무작위 사용자로 이메일을 미리 보거나 특정 사용자를 선택하거나 사용자 정의 사용자를 만들 수 있습니다. 이를 통해 연결된 콘텐츠와 개인화 호출이 제대로 작동하는지 테스트할 수 있습니다. 

그런 다음 **미리보기 링크 복사**를 선택하여 무작위 사용자에게 이메일이 어떻게 보일지 보여주는 공유 가능한 미리보기 링크를 생성하고 복사할 수 있습니다. 링크는 7일 동안 유효하며 그 후에는 다시 생성해야 합니다.

또한 데스크톱, 모바일 및 일반 텍스트 보기 간에 전환하여 메시지가 다양한 맥락에서 어떻게 표시되는지 확인할 수 있습니다.

{% alert tip %}
어두운 모드 사용자에게 이메일이 어떻게 보이는지 궁금하신가요? **어두운 모드 미리보기** 토글을 **미리보기 및 테스트** 섹션에서 선택하세요(드래그 앤 드롭 편집기 전용).
{% endalert %}

최종 확인을 할 준비가 되면 **테스트 전송**을 선택하고 자신이나 콘텐츠 테스터 그룹에 테스트 메시지를 보내 이메일이 다양한 장치와 이메일 클라이언트에서 제대로 표시되는지 확인하세요.

\![테스트를 위해 전송될 이메일 미리보기 예시.]({% image_buster /assets/img_archive/newEmailTest.png %})

템플릿에 문제가 있거나 변경 사항을 원하시면 **이메일 편집**을 선택하여 편집기로 돌아가세요.

## 6단계: 템플릿 저장

**템플릿 저장**을 선택하여 템플릿을 반드시 저장하세요. 이제 선택한 캠페인이나 캔버스 구성 요소에서 이 템플릿을 사용할 준비가 되었습니다. 템플릿에 접근하려면 템플릿을 만든 편집 경험을 선택한 다음 사용 가능한 템플릿 목록에서 선택하세요.

{% alert note %}
기존 템플릿을 수정하면 해당 변경 사항은 이전 버전의 템플릿을 사용하여 생성된 캠페인에 반영되지 않습니다.
{% endalert %}

### 템플릿 관리

더 많은 이메일 템플릿을 만들면서 이메일 템플릿을 [복제]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/#duplicate-templates)하고 [보관]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/#archive-templates)할 수 있습니다. 템플릿 및 창의적인 콘텐츠 라이브러리를 생성하고 관리하는 방법에 대해 [템플릿 및 미디어]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/)에서 자세히 알아보세요.

### API 캠페인에서 템플릿 사용하기

API 캠페인에 이메일을 사용하려면 `email_template_id`이 필요하며, 이는 Braze에서 생성된 모든 이메일 템플릿의 하단에서 찾을 수 있습니다.

\![이메일 템플릿 하단에 위치한 API 식별자.]({% image_buster /assets/img/email_templates/template5.png %})

### 이메일 템플릿에 대한 댓글 달기

드래그 앤 드롭 편집기에서 이메일 템플릿에 협업하고 댓글을 달 수 있습니다. 

1. 댓글을 달고 싶은 이메일 본문의 콘텐츠 블록 또는 행을 선택하세요.
2. <i class="fas fa-comment"></i> 댓글 아이콘을 선택하세요.
3. 사이드바에 댓글을 입력한 후 **제출**을 선택하세요.
4. 댓글을 입력한 후 **완료**을 선택하세요.
5. 댓글을 저장하려면 **템플릿 저장**을 선택하세요.

템플릿이 저장된 후, 사용자는 해결되지 않은 댓글 위에 아이콘을 볼 수 있습니다. 이 댓글을 해결하려면 **해결**을 선택하세요.

\!["좋아 보입니다"라고 적힌 이메일 템플릿 댓글.]({% image_buster /assets/img/email_templates/template_comment.png %})

이메일 템플릿에 대한 자주 묻는 질문에 대한 답변은 [템플릿 FAQ]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/)를 확인하세요.

