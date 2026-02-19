---
nav_title: 커스텀 이메일 바닥글
article_title: 사용자 지정 이메일 바닥글
page_order: 6.5
description: "이 문서에서는 워크스페이스 전체에 커스텀 이메일 바닥글을 설정하는 방법을 설명합니다."
channel:
  - email

---

# 커스텀 이메일 바닥글

> {% raw %}`{{${email_footer}}}`{% endraw %} Liquid 속성을 사용하여 모든 이메일에 템플릿으로 사용할 수 있는 워크스페이스 전체 커스텀 이메일 바닥글을 설정할 수 있습니다.

커스텀 이메일 바닥글을 사용하면 사용하는 모든 이메일 템플릿이나 이메일 캠페인에 대해 새 바닥글을 만들 필요가 없습니다. 모든 신규 및 기존 이메일 캠페인에는 커스텀 푸터에 변경한 내용이 반영됩니다. [CAN-SPAM 법 2003](https://www.ftc.gov/tips-advice/business-center/guidance/can-spam-act-compliance-guide-business) 준수를 위해 회사의 실제 주소와 이메일에 탈퇴 링크를 포함해야 합니다.

{% alert warning %}
귀하의 커스텀 바닥글이 앞서 언급한 요구 사항을 충족하는지 확인하는 것은 귀하의 책임입니다.
{% endalert %}

## 커스텀 바닥글 만들기

사용자 지정 바닥글을 만들거나 편집하려면 다음을 수행하십시오:

1. **설정** > **이메일 환경설정** > **구독 페이지 및 바닥글로** 이동합니다.
2. **커스텀 바닥** 글 섹션으로 이동하여 커스텀 바닥글을 켭니다.
3. **작성** 섹션에서 **편집을** 선택한 다음 바닥글을 편집합니다.
4. **미리** 보기를 선택하면 이메일 바닥글이 고객의 받은편지함에 어떻게 표시되는지 미리 볼 수 있습니다. 선택적으로 **미리보기 링크 복사를** 선택하여 임의의 사용자에게 이메일이 어떻게 표시되는지 보여주는 공유 가능한 미리보기 링크를 생성하고 복사할 수 있습니다. 링크는 7일 동안 지속되며 그 후 다시 생성해야 합니다.
5. 테스트 메시지를 보냅니다. 

![커스텀 바닥글의 예입니다.]({% image_buster /assets/img_archive/custom_footer.png %})

기본값 바닥글은 {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} 속성과 실제 우편 주소를 사용합니다. 이 기본값을 사용하는 경우 프로토콜에 대해 **<other>** 를 선택해야 합니다.

{% alert important %}
CAN-SPAM 규정을 준수하려면 커스텀 푸터에 수신 거부 링크를 포함해야 합니다. 이 Liquid 속성 {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} 또는 커스텀 탈퇴 URL을 사용할 수 있습니다. 탈퇴 링크가 없으면 커스텀 푸터를 저장할 수 없습니다.
{% endalert %}

![프로토콜 및 URL 값은 커스텀 바닥글에 필요합니다.]({% image_buster /assets/img_archive/email_unsub_protocol.png %}){: style="max-width:50%;"}

## 탈퇴 링크가 없는 바닥글

템플릿을 커스텀 바닥글 {% raw %}`{{${email_footer}}}`와 함께 사용할 때 `{{${set_user_to_unsubscribed_url}}}`{% endraw %} 탈퇴 링크 태그 없이 매우 주의하세요. 경고가 나타나지만, 탈퇴 링크가 포함된 이메일을 보낼지 여부는 귀하의 선택입니다.

이메일 작성기에는 다음과 같은 경고가 표시됩니다:

![예시 이메일은 바닥글 없이 작성되었습니다.]({% image_buster /assets/img_archive/no_unsub_link_warning.png %})

캠페인 작성기에는 다음과 같은 경고가 표시됩니다:

![바닥글이 없는 캠페인 작성.]({% image_buster /assets/img_archive/no_footer_test.png %})

### 커스텀 탈퇴 링크 추가하기

커스텀 탈퇴 링크를 추가하려면 사용자 ID가 포함된 쿼리 매개변수를 사용하여 커스텀 바닥글의 탈퇴 링크를 {% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %} 에서 자신의 웹사이트 링크로 변경하면 됩니다. 예를 들면 다음과 같습니다:
{% raw %} 
> https://www.braze.com/unsubscribe?user_id={{${user_id}}}
{% endraw %}

그런 다음 [`/email/status` 엔드포인트를]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/) 호출하여 사용자의 구독 상태를 업데이트합니다. 자세한 내용은 [이메일 구독 상태 변경]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions)에 대한 설명서를 참조하십시오.

그런 다음 이 새 링크를 저장합니다. 기본값인 Braze 탈퇴 태그 {%raw%}(``${set_user_to_unsubscribed_url}``){%endraw%} 는 바닥글에 있어야 합니다. 즉, 댓글에 태그를 넣거나 숨겨진 `<div>` 태그를 사용하여 기본값 링크를 '숨김'으로 포함시켜야 합니다.

## Best practices

커스텀 푸터를 만들고 사용할 때 다음과 같은 모범 사례를 제안합니다.

### 속성으로 개인화

커스텀 바닥글을 만들 때 Braze는 [개인화를 위한 속성]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)을 사용할 것을 제안합니다. 기본값 및 커스텀 속성의 전체 세트가 제공되지만, 유용할 수 있는 몇 가지는 다음과 같습니다.

| 속성 | 태그 |
| --------- | --- |
| 사용자의 이메일 주소 | {% raw %}`{{${email_address}}}`{% endraw %} |
| 사용자의 커스텀 탈퇴 URL | {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} <br><br>이 태그는 이전 {% raw %}`{{${unsubscribe_url}}}`{% endraw %} 태그를 대체합니다. 우리는 대신 새 {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} 태그를 사용할 것을 권장합니다. |
| 사용자의 커스텀 옵트인 URL | {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} |
| 사용자의 커스텀 구독 URL | {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}|
| 사용자의 커스텀 Braze 환경 설정 센터 URL | {% raw %}`{{${preference_center_url}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 탈퇴 링크 및 옵트인 링크 포함

{% raw  %}
모범 사례로서 Braze는 커스텀 바닥글에 탈퇴 링크(예: ``{{${set_user_to_unsubscribed_url}}}``)와 옵트인 링크(예: ``{{${set_user_to_opted_in_url}}}``)를 모두 포함할 것을 권장합니다. 이 방법을 사용하면 사용자는 탈퇴하거나 옵트인할 수 있으며, 일부 사용자의 옵트인 데이터를 수동으로 수집할 수 있습니다.
{% endraw %}

### 플레인텍스트 이메일에 커스텀 바닥글 설정

**구독 페이지 및 바닥글** 탭의 **이메일 환경 설정** 페이지에서 일반 텍스트 이메일에 대한 커스텀 바닥글을 설정할 수도 있으며, 이는 HTML 이메일의 커스텀 바닥글과 동일한 규칙을 따릅니다. 

플레인 텍스트 바닥글을 포함하지 않으면 Braze에서 HTML 바닥글을 자동으로 구축합니다. 커스텀 바닥글이 원하는 대로 완성되면 **저장을** 선택합니다.

![커스텀 일반 텍스트 바닥글 설정 옵션이 선택된 이메일.]({% image_buster /assets/img_archive/custom_footer_save_changes.png %}){: style="max-width:70%" }

