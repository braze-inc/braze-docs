---
nav_title: Apple 개인 릴레이에 이메일 보내기
article_title: Apple 개인 릴레이에 이메일 보내기
alias: /email_relay/
page_order: 0
description: "이 문서에서는 Apple 개인 릴레이에 이메일을 보내는 과정을 다룹니다."
channel:
  - email
  
---

# Apple 개인 릴레이에 이메일 보내기

> Apple의 단일 로그인(SSO) 기능을 사용하면 사용자가 이메일 주소(`example@icloud.com`)를 공유하거나 브랜드에 제공된 내용을 마스킹하여 이메일 주소를 숨길 수 있습니다(`tq1234snin@privaterelay.appleid.com`). Apple은 릴레이 주소로 전송된 메시지를 사용자의 실제 이메일 주소로 전달합니다. 

Apple의 개인 이메일 릴레이에 이메일을 보내려면 발신 도메인을 Apple에 등록하세요. Apple에 도메인을 구성하지 않으면 릴레이 주소로 전송된 이메일은 반송됩니다.

사용자가 앱의 릴레이 이메일로의 이메일 전달을 비활성화하기로 결정하면 Braze는 평소와 같이 이메일 반송 정보를 받게 됩니다. 이 사용자들은 Apple ID 설정 페이지에서 Apple로 로그인하여 사용하는 앱을 관리할 수 있습니다(참조: [Apple의 문서](https://support.apple.com/en-us/HT210426)).

## SendGrid를 위한 이메일 보내기

SendGrid를 이메일 제공업체로 사용하는 경우 DNS 변경 없이 Apple에 이메일을 보낼 수 있습니다. 

1. [Apple 개발자 포털](https://developer.apple.com/)에 로그인하세요.
2. **인증서, 식별자 & 프로필** 페이지로 이동하세요.
3. **서비스** > **이메일 통신을 위한 Apple로 로그인**를 선택하세요.
4. **이메일 소스** 섹션에서 도메인과 하위 도메인을 추가하세요.
- 주소는 다음과 같은 형식이어야 합니다: `bounces+<YOUR_UID>@<YOUR_WHITELABELED_SUBDOMAIN_AND_DOMAIN>` (예: `bounces+1234567@braze.online.docs.com`). 

원하는 "보낸 사람" 주소가 `abmail` 주소인 경우 하위 도메인에 포함하세요. 예를 들어, `docs.braze.com` 대신 `abmail.docs.braze.com`를 사용하세요.

## SparkPost를 위한 이메일 보내기

SparkPost에 대한 Apple 개인 릴레이를 설정하려면 다음 단계를 따르세요: 

1. Apple로 로그인하세요.
2. 이메일 도메인을 등록하려면 [Apple의 문서](https://developer.apple.com/help/account/configure-app-capabilities/configure-private-email-relay-service)를 따르세요.
3. Apple은 도메인을 자동으로 확인하고, 어떤 도메인이 검증되었는지 보여주며, 재검증 또는 도메인 삭제 옵션을 제공합니다.

### 고려사항

발신 도메인이 바운스 도메인으로도 사용되는 경우, 기록을 저장할 수 없으며 다음 추가 단계를 따라야 합니다:

1. 도메인이 이미 SparkPost에서 검증된 경우, MX 및 TXT 레코드를 **생성해야 합니다.** 

| 인스턴스 | MX 레코드                   | TXT 레코드                                    |
|----------|-----------------------------|-----------------------------------------------|
| 미국       | `smtp.sparkpostmail.com`    | `"v=spf1 redirect=_spf.sparkpostmail.com"`    |
| 유럽       | `smtp.eu.sparkpostmail.com` | `"v=spf1 redirect=_spf.eu.sparkpostmail.com"` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert important %}
SPF 실패를 피하려면, MX 및 TXT 레코드를 생성하고 DNS에 **전파된 후** CNAME 레코드를 삭제해야 합니다.
{% endalert %}

{:start="2"}
2\. CNAME 레코드를 삭제하세요.
3\. 올바른 라우팅을 위해 MX 및 TXT 레코드로 교체하세요.
4\. CDN 또는 파일 호스팅을 가리키도록 A 레코드를 생성하세요.

추가 질문이 있으시면 [지원 티켓]({{site.baseurl}}/braze_support/)을 열어주세요.
