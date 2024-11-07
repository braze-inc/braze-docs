---
nav_title: 커스텀 이메일 푸터
article_title: 커스텀 이메일 푸터
page_order: 6.5
description: "이 문서에서는 작업 공간 전체에 커스텀 이메일 바닥글을 설정하는 방법을 설명합니다."
channel:
  - email

---

# 커스텀 이메일 footer

> 워크스페이스 전체에 커스텀 이메일 바닥글을 설정할 수 있으며, 이를 {% raw %}`{{${email_footer}}}`{% endraw %} Liquid 속성을 사용하여 모든 이메일에 템플릿으로 사용할 수 있습니다.

커스텀 이메일 바닥글을 사용하면 사용하는 모든 이메일 템플릿이나 이메일 캠페인에 대해 새 바닥글을 만들 필요가 없습니다. 사용자가 커스텀 푸터에 가한 변경 사항은 모든 신규 및 기존 이메일 캠페인에 반영됩니다. CAN-SPAM 법 2003 준수를 위해 회사의 실제 주소와 이메일에 탈퇴 링크를 포함해야 합니다.

{% alert warning %}
귀하의 커스텀 바닥글이 앞서 언급한 요구 사항을 충족하는지 확인하는 것은 귀하의 책임입니다.
{% endalert %}

## 커스텀 푸터 만들기

사용자 지정 바닥글을 만들거나 편집하려면 다음을 수행하십시오:

1. **설정** > **이메일 환경설정**.

{% alert note %}
[이전 탐색<2>을 사용하는 경우 이 페이지는 **이메일 설정<3>이라고 하며 **설정 관리<4> 아래에 있습니다.
{% endalert %}

{: start="2"}
2\. **커스텀 Footer** 섹션으로 이동하여 커스텀 푸터를 켜십시오.
3\. **Compose** 섹션에서 바닥글을 편집하고 테스트 메시지를 보내십시오. 

![][20]

기본값 바닥글은 {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} 속성과 우리의 실제 우편 주소를 사용합니다. CAN-SPAM 규정을 준수하려면 커스텀 바닥글에 {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %}을 포함해야 합니다. 이 속성이 없으면 커스텀 바닥글을 저장할 수 없습니다.

기본값 바닥글을 사용하는 경우 {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} 속성을 사용하므로 **Protocol**에 대해 **<other>**을 선택해야 합니다.

![프로토콜 및 URL 값은 커스텀 바닥글에 필요합니다.][24]{: style="max-width:50%;"}

## 탈퇴 링크가 없는 바닥글

템플릿을 커스텀 푸터 {% raw %}`{{${email_footer}}}`와 함께 사용할 때 `{{${set_user_to_unsubscribed_url}}}`{% endraw %} 탈퇴 링크 태그 없이 매우 주의하십시오. 경고가 나타나지만, 탈퇴 링크가 포함된 이메일을 보낼지 여부는 귀하의 선택입니다.

**이메일 작성기 내 경고:**<br>![예시 이메일은 바닥글 없이 작성되었습니다.][21]

**캠페인 작성기 내 경고:**<br>![No-footer 캠페인 composition.][22]

## 모범 사례

Braze는 커스텀 바닥글을 만들고 사용할 때 다음 모범 사례를 제안합니다.

### 속성으로 개인화

커스텀 바닥글을 만들 때 Braze는 [개인화를 위한 속성]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)을 사용할 것을 제안합니다. 기본값 및 커스텀 속성의 전체 세트가 제공되지만, 유용할 수 있는 몇 가지는 다음과 같습니다:

| 속성 | 태그 |
| --------- | --- |
| 사용자의 이메일 주소 | {% raw %}`{{${email_address}}}`{% endraw %} |
| 사용자의 커스텀 탈퇴 URL | {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} <br><br>이 태그는 이전 {% raw %}`{{${unsubscribe_url}}}`{% endraw %} 태그를 대체합니다. 우리는 대신 새 {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} 태그를 사용할 것을 권장합니다. |
| 사용자의 커스텀 옵트인 URL | {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} |
| 사용자의 커스텀 가입하다 URL | {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}|
| 사용자의 커스텀 Braze 환경 설정 센터 URL | {% raw %}`{{${preference_center_url}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2}

### 탈퇴 링크 및 옵트인 링크 포함

{% raw  %}
모범 사례로서 Braze는 사용자 정의 바닥글에 탈퇴 링크(예: ``{{${set_user_to_unsubscribed_url}}}``)와 옵트인 링크(예: ``{{${set_user_to_opted_in_url}}}``)를 모두 포함할 것을 권장합니다. 이 방법을 사용하면 사용자는 탈퇴하거나 옵트인할 수 있으며, 일부 사용자의 옵트인 데이터를 수동으로 수집할 수 있습니다.
{% endraw %}

### 플레인텍스트 이메일에 커스텀 바닥글 설정

구독 페이지 및 바닥글 탭의 이메일 환경 설정 페이지에서 일반 텍스트 이메일에 대한 커스텀 바닥글을 설정할 수도 있으며, 이는 HTML 이메일의 커스텀 바닥글과 동일한 규칙을 따릅니다. 플레인 텍스트 바닥글을 포함하지 않으면 Braze에서 HTML 바닥글을 자동으로 구축합니다. 커스텀 바닥글이 마음에 들면 페이지 하단에서 **저장**을 클릭하세요.

![이메일 with Set 커스텀 Plaintext Footer option selected.][23]{: style="max-width:70%" }

[20]: {% image_buster /assets/img_archive/custom_footer.png %}
[21]: {% image_buster /assets/img_archive/no_unsub_link_warning.png %}
[22]: {% image_buster /assets/img_archive/no_footer_test.png %}
[23]: {% image_buster /assets/img_archive/custom_footer_save_changes.png %}
[24]: {% image_buster /assets/img_archive/email_unsub_protocol.png %}
