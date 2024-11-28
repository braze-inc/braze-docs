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

> iOS 13 릴리스에서 Apple은 Apple 고객을 위해 이메일 전송 방식에 영향을 미치는 기능을 도입했습니다. Apple의 싱글 사인온(SSO) 기능을 사용하면 사용자가 이메일 주소를 공유(`example@icloud.com`)하거나 개인 이메일 주소가 아닌 브랜드에 제공되는 이메일 주소(`tq1234snin@privaterelay.appleid.com`)를 마스킹하여 이메일 주소를 숨길 수 있습니다.

이러한 사용자는 Apple ID 설정 페이지에서 Apple로 로그인을 사용하는 앱을 관리할 수 있습니다( [Apple 설명서](https://support.apple.com/en-us/HT210426) 참조). 사용자가 앱의 릴레이 이메일에 대한 이메일 전달을 비활성화하기로 결정하면 Braze는 평소와 같이 이메일 반송 정보를 수신합니다. Apple의 비공개 이메일 릴레이로 이메일을 보내려면 Apple에 보내는 도메인을 등록하세요.

## SendGrid용 이메일 보내기

SendGrid를 이메일 공급업체로 사용하는 경우 DNS를 변경하지 않고도 Apple에 이메일을 보낼 수 있습니다. **Apple 인증서** 페이지로 이동하여 Apple의 이메일 중계 서비스(원하는 '발신자' 주소)를 통해 전송할 이메일 주소를 허용합니다.  

![Apple 인증서 페이지에서 개별 이메일 주소를 허용 목록에 추가하는 옵션.]({% image_buster /assets/img/email-relay-whitelabel-address.png %})

주소 형식은 다음과 같아야 합니다: `bounces+<YOUR_UID>@<YOUR_WHITELABELED_SUBDOMAIN_AND_DOMAIN>`(e.g, `bounces+1234567@braze.online.docs.com`). 주소가 Apple 인증서 페이지에 추가되면 이 도메인의 이메일은 Apple 개인 릴레이 시스템을 통해 전달됩니다.

{% alert important %}
원하는 "보낸 사람" 주소가 `abmail` 주소인 경우 하위 도메인에 해당 주소를 포함하세요. 예를 들어 `docs.braze.com` 대신 `abmail.docs.braze.com` 을 사용합니다. 귀하의 주소는 그렇지 않을 수 있습니다. SendGrid에서 DNS 레코드를 확인하세요.
{% endalert %}

### 보낸 사람 주소

Apple 비공개 릴레이로 이메일 주소를 추가할 때 사용되는 구성 요소는 이 표를 참조하세요.

| 값 | 설명 |
|---|---|
| UID | 이 값은 Braze에서 제공하는 DNS 레코드(SendGrid에서 제공)에 제공됩니다. 이메일 주소에 UID에 문자 "u"를 포함하지 마세요. 예를 들어 SendGrid에 UID가 `u1234567.wl134.sendgrid.net`으로 표시되는 경우 `1234567`이 UID 값입니다. <br><br> DNS 레코드에 액세스할 수 없는 경우 Braze 고객 성공 관리자에게 문의하여 UID를 제공하세요. |
| 화이트 레이블 하위 도메인 및 도메인 | SendGrid에 입력한 초기 도메인 및 하위 도메인입니다. SendGrid의 DNS 레코드에서 **HOST 값**을 사용할 수도 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## SparkPost용 이메일 보내기

SparkPost용 Apple 비공개 릴레이를 설정하려면 다음 단계를 따르세요. 

1. Apple로 로그인합니다. 
2. 이메일 도메인을 추가합니다. 
3. Apple은 자동으로 도메인을 확인하여 확인된 도메인을 표시하고 도메인을 다시 확인하거나 삭제할 수 있는 옵션을 제공합니다.

{% alert important %}
인증 파일이 생성된 후 2~3일 이내에 이 프로세스를 완료해야 하며, 그렇지 않으면 만료됩니다. Apple은 유효 기간을 공개하지 않습니다.
{% endalert %}

더 궁금한 점이 있으면 [지원 티켓을]({{site.baseurl}}/braze_support/) 개설하세요.
