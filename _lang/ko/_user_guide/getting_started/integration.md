---
nav_title: 통합
article_title: 온보딩 통합 개요
page_order: 8
page_type: reference
description: "이 참조 문서에서는 엔지니어 또는 개발자에게 필요한 통합 단계를 간략하게 다룹니다."

---

# 통합

> Braze와의 통합은 가치 있는 과정입니다. 하지만 당신은 똑똑합니다. **도착했습니다**. 이미 알고 계실 겁니다. 하지만 여러분은 아마도 여러분과 개발자가 함께 기술적 전문성, 전략적 계획, 그리고 둘 사이의 조율에 도움이 되는 일관된 커뮤니케이션이 필요한 여정을 함께 가고 있다는 사실을 모를 것입니다.

{% alert note %}
이 도움말의 내용은 이메일에는 적용되지 않습니다. [이메일 설정]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/) 섹션에서 확인하세요.
{% endalert %}

## 통합 프로세스의 기술적 측면

"우리 개발자들은 정말 대단해!"라고 생각하실 수도 있습니다. 그들은 무엇이든 할 수 있기 때문에 보통은 그냥 내버려 둡니다!" 그리고 그들은 아마도 그럴 수 있을 것입니다! 하지만 그들이 뒤에서 무슨 일을 하는지 모를 이유는 없습니다. 실제로 "API 키와 API 엔드포인트를 보내주실 수 있나요?"라고 물었을 때 언제 정보를 제공해야 하는지, 무엇을 찾아야 하는지 알고 있다면 전체 프로세스에 도움이 될 것입니다.

그렇다면 앱이나 사이트와 Braze를 통합할 때 무엇을 할 수 있을까요? 물어봐 주셔서 감사합니다!

### 1단계: 이들은 Braze 소프트웨어 개발 키트를 구현합니다.

Braze SDK(소프트웨어 개발 키트)는 당사가 회원님의 앱이나 사이트와 정보를 주고받는 방식입니다. 엔지니어링 팀은 기본적으로 앱을 하나로 묶는 역할을 합니다. 이를 위해서는 몇 가지 핵심 정보가 필요합니다:

* [API 키]({{site.baseurl}}/api/api_key/)
* [SDK 엔드포인트]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/)
  * Braze는 더 이상 커스텀 엔드포인트를 제공하지 않으므로 미리 정의된 SDK 엔드포인트를 사용하세요. 기존 커스텀 엔드포인트가 제공된 경우 여기에서 [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-5-optional-custom-endpoint-setup), [iOS]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) 및 [웹]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#initializing-the-sdk) 통합과 관련된 설정 단계를 확인할 수 있습니다.

이 정보를 직접 제공하거나 계정을 생성하여 자녀에게 Braze에 대한 액세스 권한을 부여할 수 있습니다. 

{% alert warning %}
구현 과정에서 문제가 발생하거나 한 명 이상의 계정이 잠길 수 있으므로 여러분과 여러분의 개발자가 의도치 않게 또는 실수로 Braze에서 회사의 자격 증명을 변경하지 않도록 하세요.
{% endalert %}

### 2단계: 원하는 메시징 채널을 구현합니다.

Braze에는 사용자와 연락할 수 있는 다양한 옵션이 있으며, 각 옵션은 원하는 방식으로 작동하려면 자체 설정 또는 조정이 필요합니다. 바로 이 지점에서 엔지니어링 팀과의 커뮤니케이션이 중요해집니다.

개발자에게 어떤 채널을 사용할지 알려주어 구현이 효율적이고 적절한 순서로 이루어질 수 있도록 하세요.

| 채널 | 세부 정보 |
|---|---|
| 인앱 메시지 | 이러한 채널별 단계뿐만 아니라 소프트웨어 개발 키트 구현이 필요합니다. |
| 푸시 | 메시징 자격 증명 및 푸시 토큰에 대한 적절한 처리를 제공하려면 소프트웨어 개발 키트 구현이 필요합니다. |
| 이메일 | 이것은 완전히 다른 프로세스입니다. 통합에 대한 자세한 내용은 [이메일 설정]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/) 섹션을 참조하세요. |
| 콘텐츠 카드 | [콘텐츠 카드를]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/) 시작하려면 Braze 고객 성공 매니저에게 문의하세요. |
| SMS & MMS | 통합에 대한 자세한 내용은 [SMS 설정]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/sms/sms_setup/sms_sending/) 섹션을 참조하세요. |
| 웹훅 | 소프트웨어 개발 키트 구현과 채널별 단계가 필요합니다. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Braze를 사용하여 각 채널에서 접근성 높은 메시징 캠페인을 만들 수 있습니다. 개발자와 협력하여 구현 시 접근성 표준을 충족할 수 있도록 하세요.
{% endalert %}

### 3단계: 데이터를 설정합니다.

Braze는 한 방에 끝나는 조랑말이 아닙니다. 단순히 이메일을 보내거나 푸시를 보내는 것이 아닙니다. 이는 모든 사용자와 고객에게 고유한 개인화된 고객 여정을 만드는 것입니다. 고객 여정은 앱이나 사이트 내에서 고객의 행동을 기반으로 하며, 이를 정의할 수 있습니다! 개발자의 다음 과제는 앱이나 사이트 내에서 수행된 작업이 Braze에 포착되도록 하는 것입니다.

그렇다면 이 정보를 얻으려면 어떻게 해야 할까요?

1. 마케팅 팀과 협력하여 추적해야 할 캠페인, 목표, 속성, 이벤트를 정의하세요. 이러한 사용 사례를 정의하고 팀원들과 공유하세요.
2. 커스텀 데이터 요구 사항[(커스텀 속성]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/), [커스텀 이벤트]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) 등)을 정의합니다.
3. 거기서부터 해당 데이터를 추적하는 방법(소프트웨어 개발 키트 등을 통해 트리거)에 대해 논의하세요.
4. 필요한 [작업 공간의]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/) 수를 정의하세요. 엔지니어링 담당자는 이러한 작업 공간을 [테스트하고 구성하는]({{site.baseurl}}/user_guide/getting_started/workspaces/) 방법을 알아야 합니다.

이 모든 정보를 발견한 후에는 엔지니어링 담당자와 공유하세요. 해당 정보를 가져와 [고객 데이터를]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/) 구현합니다. [일부 사용자를 가져와야]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/) 할 수도 있습니다. [이벤트 이름 지정 규칙도]({{site.baseurl}}/user_guide/data/custom_data/event_naming_conventions/) 알고 있어야 합니다.

### 4단계: 고객이 원하는 것을 기반으로 커스텀합니다.

API 트리거된 실행 및 연결된 콘텐츠와 같은 기능을 원하는 경우, 앱과 Braze 외부에 있는 데이터를 메시지로 가져올 수 있도록 Braze 담당자 및 개발자와 함께 논의하세요.

### 5단계: 둘 다 구현에 대한 QA를 수행합니다.

엔지니어링 담당자와 협력하여 모든 것이 제대로 작동하는지 확인하세요. [테스트 메시지를]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages/) 보내고, [Android용 테스트 앱]({{site.baseurl}}/developer_guide/references/?tab=android) 과 [iOS용 테스트 앱을]({{site.baseurl}}/developer_guide/references/?tab=swift) 사용하여 전송을 시작하기 전에 모든 상자를 체크하세요!

[Android 또는 FireOS 통합 테스트와]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/test_your_basic_integration/#test-your-basic-integration) [iOS용 푸시]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/testing/) 테스트에 대한 구체적인 지침도 마련되어 있습니다.

## 구현 후

구현이 완료되었다고 해서 한 번에 백만 개의 메시지를 보낼 수 있는 청신호가 켜지는 것은 아니라는 점을 명심하세요. 푸시를 백만 번 보내도 모든 고객이 동시에 같은 링크를 클릭하면 앱이 중단될 수 있습니다. **보내기** 버튼을 클릭하기 전에 Braze의 요청을 처리할 수 있는 내부 설정의 용량이 어느 정도인지 검토하는 것이 좋습니다. 그런 다음 이를 기준으로 [요금 제한을]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting) 설정할 수 있습니다.

\![]({% image_buster/assets/img/torchie/firebrands.png %}){: style="max-width:15%;float:right;margin-left:15px;border:none;"}

Braze 사용에 익숙해졌다면 Braze 파이어브랜드가 되어 보세요! 고객 참여 커뮤니티인 Braze Firebrands를 통해 고객 경험 및 마케팅을 현대화하기 위해 Braze를 사용하는 무버와 셰이커의 커뮤니티를 구축하고 있습니다. 자세히 알아보고 싶으신가요? [지금 가입하세요](https://brazefirebrands.splashthat.com/).
