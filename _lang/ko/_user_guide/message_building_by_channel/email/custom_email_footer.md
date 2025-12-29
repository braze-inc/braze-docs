---
nav_title: 사용자 정의 이메일 바닥글
article_title: 사용자 정의 이메일 바닥글
page_order: 6.5
description: "이 문서에서는 작업 공간 전체에 대한 사용자 정의 이메일 바닥글을 설정하는 방법을 설명합니다."
channel:
  - email

---

# 사용자 정의 이메일 바닥글

> 모든 이메일에 {% raw %}`{{${email_footer}}}`{% endraw %} Liquid 속성을 템플릿으로 사용할 수 있는 작업 공간 전체의 사용자 정의 이메일 바닥글을 설정할 수 있습니다.

사용자 정의 이메일 바닥글을 사용하면 사용하는 모든 이메일 템플릿이나 이메일 캠페인에 대해 새 바닥글을 만들 필요가 없습니다. 사용자 정의 바닥글에 대한 변경 사항은 모든 새로운 및 기존 이메일 캠페인에 반영됩니다. 2003년 [CAN-SPAM 법](https://www.ftc.gov/tips-advice/business-center/guidance/can-spam-act-compliance-guide-business) 준수는 귀하의 회사에 대한 물리적 주소와 이메일에 구독 취소 링크를 포함해야 함을 요구합니다.

{% alert warning %}
사용자 정의 바닥글이 위의 요구 사항을 충족하는지 확인하는 것은 귀하의 책임입니다.
{% endalert %}

## 사용자 정의 바닥글 만들기

사용자 정의 바닥글을 만들거나 편집하려면 다음을 수행하십시오:

1. **설정** > **이메일 기본 설정**으로 이동합니다.
2. **사용자 정의 바닥글** 섹션으로 이동하여 사용자 정의 바닥글을 켭니다.
3. **작성** 섹션에서 바닥글을 편집합니다.
4. 테스트 메시지를 보냅니다. 

\![사용자 정의 바닥글의 예.]({% image_buster /assets/img_archive/custom_footer.png %})

기본 바닥글은 {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} 속성과 우리의 물리적 우편 주소를 사용합니다. 이 기본값을 사용하는 경우 **<other>**를 **프로토콜**에 대해 선택해야 합니다.

{% alert important %}
CAN-SPAM 규정을 준수하려면 사용자 정의 바닥글에 {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %}를 포함해야 합니다. 이 속성이 없으면 사용자 정의 바닥글을 저장할 수 없습니다.
{% endalert %}

\![사용자 정의 바닥글에 필요한 프로토콜 및 URL 값.]({% image_buster /assets/img_archive/email_unsub_protocol.png %}){: style="max-width:50%;"}

## 구독 취소 링크가 없는 바닥글

구독 취소 링크 태그 {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} 없이 사용자 정의 바닥글 {% raw %}`{{${email_footer}}}`{% endraw %} 가 있는 템플릿을 사용할 때 매우 주의해야 합니다. 경고가 표시되지만, 구독 취소 링크가 있는지 없는지에 따라 이메일을 보낼지는 귀하의 선택입니다.

이메일 작성기에서 경고가 표시됩니다:

\![바닥글 없이 작성된 예시 이메일.]({% image_buster /assets/img_archive/no_unsub_link_warning.png %})

캠페인 작성기에서 경고가 표시됩니다:

\![바닥글 없는 캠페인 구성.]({% image_buster /assets/img_archive/no_footer_test.png %})

### 사용자 정의 구독 취소 링크 추가하기

사용자 정의 구독 취소 링크를 추가하려면, 사용자 정의 바닥글의 구독 취소 링크를 {% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %}에서 사용자 ID를 포함하는 쿼리 매개변수가 있는 귀하의 웹사이트 링크로 변경할 수 있습니다. 예시는 다음과 같습니다:
{% raw %} 
> https://www.braze.com/unsubscribe?user_id={{${user_id}}}
{% endraw %}

다음으로, [`/email/status` 엔드포인트]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/)를 호출하여 사용자의 구독 상태를 업데이트합니다. 자세한 내용은 [이메일 구독 상태 변경]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions)에 대한 문서를 참조하십시오.

그런 다음 이 새 링크를 저장합니다. 기본 Braze 구독 취소 태그 {%raw%}(``${set_user_to_unsubscribed_url}``){%endraw%}는 바닥글에 있어야 합니다. 이는 기본 링크를 포함해야 함을 의미하며, 태그를 주석에 넣거나 숨겨진 `<div>` 태그에 넣어 "숨기는" 방법으로 포함해야 합니다.

## 모범 사례

사용자 정의 바닥글을 만들고 사용할 때 다음 모범 사례를 제안합니다.

### 속성으로 개인화하기

사용자 정의 바닥글을 만들 때, Braze는 [개인화를 위한 속성]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)을 사용하는 것을 권장합니다. 기본 및 사용자 정의 속성의 전체 세트가 제공되지만, 유용할 수 있는 몇 가지를 소개합니다:

| 속성 | 태그 |
| --------- | --- |
| 사용자의 이메일 주소 | {% raw %}`{{${email_address}}}`{% endraw %} |
| 사용자의 사용자 정의 구독 취소 URL | {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} <br><br>이 태그는 이전의 {% raw %}`{{${unsubscribe_url}}}`{% endraw %} 태그를 대체합니다. 더 새로운 {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} 태그를 사용하는 것이 좋습니다. |
| 사용자의 사용자 정의 옵트인 URL | {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} |
| 사용자의 사용자 정의 구독 URL | {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}|
| 사용자의 사용자 정의 Braze 기본 설정 센터 URL | {% raw %}`{{${preference_center_url}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 구독 취소 링크 및 옵트인 링크 포함하기

{% raw  %}
모범 사례로서, Braze는 사용자 정의 바닥글에 구독 취소 링크(예: ``{{${set_user_to_unsubscribed_url}}}``)와 옵트인 링크(예: ``{{${set_user_to_opted_in_url}}}``)를 포함할 것을 권장합니다. 이렇게 하면 사용자가 구독 취소 또는 옵트인할 수 있으며, 사용자의 일부에 대한 옵트인 데이터를 수집할 수 있습니다.
{% endraw %}

### 일반 텍스트 이메일에 대한 사용자 정의 바닥글 설정하기

또한 **구독 페이지 및 바닥글** 탭의 **이메일 기본 설정** 페이지에서 일반 텍스트 이메일에 대한 사용자 정의 바닥글을 설정할 수 있으며, 이는 HTML 이메일에 대한 사용자 정의 바닥글과 동일한 규칙을 따릅니다. 

일반 텍스트 바닥글을 포함하지 않으면, Braze는 HTML 바닥글에서 자동으로 하나를 생성합니다. 사용자 정의 바닥글이 마음에 드시면 **저장**을 선택하세요.

\![사용자 정의 일반 텍스트 바닥글 옵션이 선택된 이메일.]({% image_buster /assets/img_archive/custom_footer_save_changes.png %}){: style="max-width:70%" }

