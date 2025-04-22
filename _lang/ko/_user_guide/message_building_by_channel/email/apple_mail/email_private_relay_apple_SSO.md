---
nav_title: Apple 비공개 릴레이로 이메일 보내기
article_title: Apple 비공개 릴레이로 이메일 보내기
alias: /email_relay/
page_order: 0
description: "이 도움말에서는 Apple 비공개 릴레이로 이메일을 보내는 과정을 설명합니다."
channel:
  - email
  
---

# Apple 비공개 릴레이로 이메일 보내기

> Apple의 싱글 사인온(SSO) 기능을 사용하면 사용자가 이메일 주소를 공유(`example@icloud.com`)하거나 개인 이메일 주소 대신 브랜드에 제공되는 이메일 주소(`tq1234snin@privaterelay.appleid.com`)를 마스킹하여 이메일 주소를 숨길 수 있습니다. 그러면 Apple은 릴레이 주소로 전송된 메시지를 사용자의 실제 이메일 주소로 전달합니다. 

Apple의 비공개 이메일 릴레이로 이메일을 보내려면 Apple에 보내는 도메인을 등록하세요. Apple에서 도메인을 구성하지 않으면 릴레이 주소로 전송된 이메일이 반송됩니다.

사용자가 앱의 릴레이 이메일에 대한 이메일 전달을 비활성화하기로 결정하면 Braze는 평소와 같이 이메일 반송 정보를 수신합니다. 이러한 사용자는 Apple ID 설정 페이지에서 Apple로 로그인을 사용하는 앱을 관리할 수 있습니다( [Apple 설명서](https://support.apple.com/en-us/HT210426) 참조).

## SendGrid용 이메일 보내기

SendGrid를 이메일 공급업체로 사용하는 경우 DNS를 변경하지 않고도 Apple에 이메일을 보낼 수 있습니다. 

1. 
2. 
3. 
4. 

 

## SparkPost용 이메일 보내기

SparkPost용 Apple 비공개 릴레이를 설정하려면 다음 단계를 따르세요. 

1. Apple로 로그인합니다.
2. Follow [Apple's documentation](https://developer.apple.com/help/account/configure-app-capabilities/configure-private-email-relay-service) to register the email domains.
3. 

### 고려 사항

발신 도메인이 반송 도메인으로도 사용되는 경우 레코드를 저장할 수 없으므로 이러한 추가 단계를 따라야 합니다:

1. 도메인이 이미 SparkPost에서 확인된 경우 MX 및 TXT 레코드를 **만들어야** 합니다: 

| 인스턴스 | MX 레코드                   | TXT 기록                                    |
|----------|-----------------------------|-----------------------------------------------|
| 미국       | `smtp.sparkpostmail.com`    | `"v=spf1 redirect=_spf.sparkpostmail.com"`    |
| 유럽연합       | `smtp.eu.sparkpostmail.com` | `"v=spf1 redirect=_spf.eu.sparkpostmail.com"` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert important %}

{% endalert %}

{:start="2"}
2\. CNAME 레코드를 삭제합니다.
3\. 적절한 라우팅을 위해 MX 및 TXT 레코드로 교체하세요.
4\. CDN 또는 파일 호스팅을 가리키는 A 레코드를 생성합니다.

더 궁금한 점이 있으면 [지원 티켓을]({{site.baseurl}}/braze_support/) 개설하세요.
