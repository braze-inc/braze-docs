---
nav_title: Shopify 사용자 조정
article_title: Shopify 사용자 조정
permalink: "/shopify_user_reconciliation/"
description: "이 참조 문서는 사용자가 결제 흐름에 도달할 때 사용자의 기기 ID 및 개인 정보를 조정하는 방법을 다룹니다."
hidden: true
---

# Shopify 사용자 조정 결제 흐름 외부 

> Shopify 통합은 사용자가 결제 흐름에 도달하여 Shopify 웹훅 이벤트를 수행할 때 사용자의 기기 ID 및 개인 정보를 조정합니다.

{% alert note %}
이 기능은 현재 베타 버전입니다. 관심이 있으시면 고객 성공 매니저 또는 계정 매니저에게 연락하십시오.
{% endalert %}

Shopify 가입 및 로그인 흐름을 통해 사용자 조정을 지원하기 위해 JavaScript 기능을 자동으로 Shopify 스토어에 체크아웃 흐름 외부에 구현할 수 있습니다. Braze는 아래 예시와 같이 Shopify 스토어에서 `type="email"`이 있는 양식을 볼 때마다 자동으로 기능을 구현합니다.

![1]{:style="max-width:60%;"}

이 함수가 호출되면 웹의 익명 사용자가 제공된 이메일 주소와 연결됩니다. 앞으로 Shopify에서 사용하는 식별자를 참조하는 모든 이벤트(예: Shopify 고객 ID, 이메일 주소, 전화번호)는 일치하는 경우 동일한 Braze 사용자에게 할당됩니다.

## 고려 사항

{% alert important %}
Braze는 고객의 Shopify 사이트에 `type="email"`을(를) 포함하는 모든 양식을 알지 못합니다. 이는 기능이 고객 조정에 사용되어야 하는 일부 입력 필드를 놓치거나 잘못된 이메일 주소(예: 추천 양식)를 고객 프로필에 설정하는 잘못된 필드를 선택할 가능성이 있음을 의미합니다.
{% endalert %}

Shopify 사이트에서 지원하는 모든 양식을 탐색하고 이 베타 솔루션이 귀하의 요구를 효과적으로 충족할 수 있는 방법을 평가해 보시기 바랍니다. 이 베타 기능을 사용하기로 선택함으로써, Shopify 양식에 수동으로 변경을 가하면 예상치 못한 동작이 발생할 수 있음을 이해합니다.

[1]: {% image_buster /assets/img/shopify_type_email.png %}
