---
nav_title: FAQ
article_title: 이메일 및 링크 템플릿 FAQ
page_order: 10

page_type: FAQ
description: "이 페이지는 이메일 템플릿 및 링크 템플릿에 대한 자주 묻는 질문을 다룹니다."
tool:
  - Templates
channel: email

---

# 자주 묻는 질문

> 이 페이지는 이메일 템플릿 및 링크 템플릿에 대한 자주 묻는 질문에 대한 답변을 제공합니다.

## 이메일 템플릿

### 내 이메일에 "브라우저에서 이 이메일 보기" 링크를 추가할 수 있나요?

아니요, Braze는 이 기능을 제공하지 않습니다. 이는 이미지와 콘텐츠를 문제 없이 렌더링하는 최신 이메일 클라이언트와 모바일 장치에서 이메일을 열어보는 경우가 점점 더 많아지고 있기 때문입니다.

**해결 방법:** 이와 동일한 결과를 얻으려면 이메일의 내용을 외부 랜딩 페이지(예: 웹사이트)에 호스팅한 다음, 이메일 본문을 편집할 때 **링크** 도구를 사용하여 작성 중인 이메일 캠페인에서 해당 페이지로 연결할 수 있습니다.

### 내 이메일 템플릿에 대한 커스텀 탈퇴 링크를 어떻게 만드나요?

탈퇴 페이지에 대한 리디렉션 옵션이 있습니다.

사용자 ID를 포함하는 쿼리 매개변수가 있는 링크로 {% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %}의 커스텀 바닥글의 탈퇴 링크를 변경할 수 있습니다. 예를 들면 다음과 같습니다:
{% raw %} 
> https://www.braze.com/unsubscribe?user_id={{${user_id}}}
{% endraw %}

다음으로, 사용자의 구독 상태를 업데이트하기 위해 [`/email/status` 엔드포인트]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/)를 호출할 수 있습니다. 자세한 내용은 [이메일 구독 상태 변경]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions)에 대한 설명서를 참조하십시오.

이 새 링크를 저장하려면 기본값 Braze 탈퇴 태그 {%raw%}(``${set_user_to_unsubscribed_url}``){%endraw%}가 바닥글에 있어야 합니다. 이것은 태그를 주석에 넣거나 숨겨진 `<div>` 태그에 넣어 "숨김"으로써 기본값 링크를 포함해야 함을 의미합니다.

- **댓글의 태그 예시:** 댓글에 태그 넣기 예시: `<!-- ${set_user_to_unsubscribed_url} -->`
- **숨겨진 `<div>` 태그 예제의 댓글:** {%raw%}`<div style="display:none;max-height:0px;overflow:hidden;">${set_user_to_unsubscribed_url}</div>`{%endraw%}

### 캠페인에서 현재 사용 중인 이메일 템플릿을 편집하면 어떻게 되나요?

기존 템플릿에 대한 수정 사항은 해당 템플릿의 이전 버전을 사용하여 생성된 캠페인에 반영되지 않습니다. REST API 본문에 템플릿을 사용하는 API 캠페인의 경우, Braze는 전송 시점에 최신 버전의 템플릿을 사용합니다.  

## 링크 템플릿

### 내 이메일에 여러 링크 템플릿을 업로드할 수 있나요?

네, 이메일 메시지에 원하는 만큼 템플릿을 삽입할 수 있습니다. 모범 사례로서 링크가 대부분의 브라우저에서 짧아지거나 잘리지 않도록 이메일을 테스트하여 링크가 2,000자를 초과하지 않도록 해야 합니다.

### 내 링크를 모든 태그가 적용된 상태로 미리 보려면 어떻게 해야 하나요?

링크를 미리 보는 여러 가지 방법이 있습니다. After you have applied the [link template]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_template/), you can send a [test email]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages/) to yourself to view all the links. 

새 탭의 미리보기 창에서 링크를 열어 링크를 볼 수도 있습니다. 미리보기 창에서 링크 위에 마우스를 올리면 브라우저 하단에서 링크를 볼 수 있습니다.

### 링크 템플릿은 Liquid와 어떻게 작동합니까?

링크 템플릿은 Liquid 확장이 일어나기 전에 각 URL에 확장 및 추가됩니다. URL의 일부가 Liquid 스니펫을 사용하여 생성된 경우 링크 템플릿이 올바르게 확장되도록 URL 기반과 물음표(?)를 하드코딩하는 것이 좋습니다. 

Liquid에 물음표(?)를 추가하지 마십시오. 이렇게 하면 링크 템플릿이 먼저 물음표(?)를 추가한 다음 Liquid 확장 프로세스가 두 번째 물음표(?)를 추가하게 됩니다.

## 링크 별칭 지정

### 링크 별칭 지정을 활성화하면 내 콘텐츠 블록 및 링크 템플릿에 어떤 영향을 미칠까요?

새로 생성된 모든 콘텐츠 블록에 대해 링크 별칭 지정이 작업 공간 전반에 걸쳐 적용됩니다. 이는 회사 수준의 기능이기 때문입니다. 

링크 별칭 지정이 활성화되면 기존 콘텐츠 블록은 수정되지 않습니다. 기존 링크 템플릿은 수정되지 않지만, 메시지의 기존 링크 템플릿 섹션은 제거됩니다. 자세한 정보는 [콘텐츠 블록에서 링크 별칭 지정을 확인하세요]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/#link-aliasing-in-content-blocks).

### HTML 앵커 태그 내에서 Liquid 조건 로직을 완전히 사용할 수 있습니까?

아니요, Braze 링크 별칭 지정은 HTML을 제대로 인식하지 못할 것입니다. 

이와 같은 논리가 HTML을 구문 분석해야 하는 기능(예: 프리헤더 또는 링크 템플릿)과 함께 사용될 때, HTML을 스캔하는 데 사용되는 라이브러리가 앵커 태그를 수정하여 적절한 `href`이 템플릿화되는 것을 방지할 수 있습니다. 라이브러리는 HTML이 Liquid 코드와 무관하기 때문에 유효하지 않다고 판단합니다. 

대신 각 단계에서 전체 앵커 태그를 포함하는 Liquid 논리를 사용하십시오. 이것은 유효한 HTML의 여러 인스턴스를 포함하는 논리를 포함하기 때문에 HTML 구문 분석에 방해가 되지 않습니다. 또한 변수를 적절한 앵커 태그에 할당한 다음 템플릿화하여 논리를 단순화할 수 있습니다.
