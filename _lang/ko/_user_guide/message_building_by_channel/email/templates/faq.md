---
nav_title: 자주 묻는 질문
article_title: 이메일 및 링크 템플릿 FAQ
page_order: 10

page_type: FAQ
description: "이 페이지에서는 이메일 템플릿 및 링크 템플릿에 대해 자주 묻는 질문을 다룹니다."
tool:
  - Templates
channel: email

---

# 자주 묻는 질문

> 이 페이지에서는 이메일 템플릿 및 링크 템플릿에 대해 자주 묻는 질문에 대한 답변을 제공합니다.

## 이메일 템플릿

### 내 이메일에 "브라우저에서 이 이메일 보기" 링크를 추가할 수 있나요?

아니요, Braze는 이 기능을 제공하지 않습니다. 이미지와 콘텐츠를 문제 없이 렌더링하는 최신 이메일 클라이언트와 모바일 기기에서 이메일을 여는 경우가 점점 더 많아지고 있기 때문입니다.

**해결 방법:** 이와 동일한 결과를 얻으려면 이메일 본문을 편집할 때 **링크** 도구를 사용하여 구축 중인 이메일 캠페인에서 링크할 수 있는 외부 랜딩 페이지(예: 웹사이트)에 이메일 콘텐츠를 호스팅할 수 있습니다.

### 이메일 템플릿에 커스텀 탈퇴 링크를 만들려면 어떻게 해야 하나요?

탈퇴 페이지에 대한 리디렉션 옵션이 있습니다.

커스텀 바닥글의 탈퇴 링크를 {% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %} 에서 사용자 ID가 포함된 쿼리 매개변수를 사용하여 자신의 웹사이트로 연결되는 링크로 변경할 수 있습니다. 예를 들면 다음과 같습니다:
{% raw %} 
> https://www.braze.com/unsubscribe?user_id={{${user_id}}}
{% endraw %}

그런 다음 [`/email/status` 엔드포인트를]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/) 호출하여 사용자의 구독 상태를 업데이트할 수 있습니다. 자세한 내용은 [이메일 구독 상태 변경에]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions) 대한 설명서를 참조하세요.

이 새 링크를 저장하려면 기본값인 Braze 탈퇴 태그 {%raw%}(``${set_user_to_unsubscribed_url}``){%endraw%} 가 바닥글에 있어야 합니다. 즉, 댓글에 태그를 넣거나 숨겨진 `<div>` 태그를 사용하여 기본값 링크를 '숨겨서' 포함해야 합니다.

- **댓글에 태그** 넣기 예시**:** 댓글에 태그 넣기 예시: `<!-- ${set_user_to_unsubscribed_url} -->`
- **숨겨진 댓글 `<div>` 태그 예시:** {%raw%}`<div style="display:none;max-height:0px;overflow:hidden;">${set_user_to_unsubscribed_url}</div>`{%endraw%}

### 현재 캠페인에서 사용 중인 이메일 템플릿을 편집하면 어떻게 되나요?

기존 템플릿에 대한 편집 내용은 해당 템플릿의 이전 버전을 사용하여 만든 캠페인에는 반영되지 않습니다. REST API 본문에 템플릿을 사용하는 API 캠페인의 경우 Braze는 전송 시점에 최신 버전의 템플릿을 사용합니다.  

## 링크 템플릿

### 내 이메일에 여러 개의 링크 템플릿을 업로드할 수 있나요?

예, 이메일 메시징에 원하는 만큼 템플릿을 삽입할 수 있습니다. 대부분의 브라우저에서 링크를 줄이거나 잘라내므로 이메일의 링크가 2,000자를 초과하지 않는지 테스트하는 것이 좋습니다.

### 모든 태그가 적용된 링크를 미리 보려면 어떻게 하나요?

링크를 미리 보는 방법에는 여러 가지가 있습니다. [링크 템플릿을]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_template/) 적용한 후 자신에게 [테스트 이메일을]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages/) 보내 모든 링크를 확인할 수 있습니다. 

새 탭의 미리보기 창에서 링크를 열어 링크를 볼 수도 있습니다. 미리보기 창에서 링크 위로 마우스를 가져가 브라우저 하단에서 확인할 수도 있습니다.

### Liquid에서 링크 템플릿은 어떻게 작동하나요?

링크 템플릿은 Liquid 확장이 일어나기 전에 각 URL에 확장 및 추가됩니다. URL의 일부가 Liquid 스니펫을 사용하여 생성된 경우 링크 템플릿이 올바르게 확장되도록 URL 베이스와 물음표(?)를 하드코딩하는 것이 좋습니다. 

Liquid에 물음표(?)를 추가하면 링크 템플릿이 먼저 물음표(?)를 추가하고 나중에 Liquid 확장 프로세스에서 두 번째 물음표(?)를 추가하게 되므로 물음표(?)를 추가하지 마세요.

## 링크 별칭 지정

### 링크 별칭 지정은 콘텐츠 블록과 링크 템플릿에 어떤 영향을 주나요?

링크 별칭 지정은 회사 차원의 기능이므로 새로 만들어지는 모든 콘텐츠 블록에 대해 워크스페이스 전체에 적용됩니다. 

링크 별칭 지정이 인에이블먼트된 경우 기존 콘텐츠 블록은 수정되지 않습니다. 기존 링크 템플릿은 수정되지 않지만 메시징의 기존 링크 템플릿 섹션은 제거됩니다. 자세한 내용은 [콘텐츠 블록의 링크 별칭 지]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/#link-aliasing-in-content-blocks) 정을 확인하세요.

### HTML 앵커 태그 내에서만 Liquid 조건 로직을 사용할 수 있나요?

아니요, Braze 링크 별칭 지정이 HTML을 제대로 인식하지 못합니다. 

이와 같은 로직을 프리헤더 또는 링크 템플릿과 같이 HTML을 구문 분석해야 하는 기능과 함께 사용하면 HTML을 스캔하는 데 사용되는 라이브러리가 적절한 `href` 템플릿이 생성되지 않도록 하는 방식으로 앵커 태그를 수정할 수 있습니다. 그러면 라이브러리는 HTML이 Liquid 코드와 무관하므로 유효하지 않다고 판단합니다. 

대신 각 단계에서 완전한 앵커 태그가 포함된 Liquid 로직을 사용하세요. 로직에는 유효한 HTML의 여러 인스턴스가 포함되므로 HTML 구문 분석에 방해가 되지 않습니다. 변수를 적절한 앵커 태그에 할당하고 템플릿을 지정하여 로직을 단순화할 수도 있습니다.
