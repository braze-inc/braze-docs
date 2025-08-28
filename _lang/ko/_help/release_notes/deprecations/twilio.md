---
nav_title: Twilio 파트너십
alias: /partners/twilio/

description: "이 기사는 Braze와 Twilio 간의 파트너십을 설명합니다."
page_type: update
channel: 
  - SMS
  - Webhook
---

# Twilio

{% alert warning %}
Twilio 웹훅 통합에 대한 지원은 2020년 1월 31일에 중단됩니다. Braze에서 여전히 SMS 서비스에 액세스하려면 [SMS 문서를]({{site.baseurl}}/user_guide/message_building_by_channel/sms/) 참조하세요.
{% endalert %}

이 예제에서는 Braze 웹훅 채널을 구성하여 Twilio의 [메시지 전송 API](https://www.twilio.com/docs/api/rest/sending-messages)를 통해 사용자에게 SMS 및 MMS를 보냅니다. 사용자의 편의를 위해 대시보드에 Twilio 웹훅 템플릿이 포함되어 있습니다.

## HTTP URL

대시보드에서 Twilio가 제공한 웹훅 URL입니다. 이 URL은 Twilio 계정 ID(`TWILIO_ACCOUNT_SID`)를 포함하고 있기 때문에 사용자의 Twilio 계정에 고유합니다.

Braze의 Twilio 예제에서, 웹훅 URL은 `https://api.twilio.com/2010-04-01/Accounts/TWILIO_ACCOUNT_SID/Messages.json`입니다. Twilio 콘솔의 *시작하기* 섹션에서 이 URL을 찾을 수 있습니다.

![트윌리오_콘솔]({% image_buster /assets/img_archive/Twilio_Console.png %})

## 요청 본문

Twilio API는 요청 본문이 URL 인코딩되기를 기대하므로 Braze 웹훅 작성기에서 요청 유형을 `Raw Text`로 변경하는 것부터 시작해야 합니다. 요청 본문에 필요한 매개변수는 *To*, *From*, 및 *Body*입니다.

다음 스크린샷은 각 사용자의 전화번호로 SMS를 보낼 때 본문에 "Braze에서 인사드립니다!"라는 메시지를 포함한 요청이 어떻게 보일 수 있는지에 대한 예시입니다.

- 각 고객 프로필에 유효한 전화번호가 대상 오디언스에 있어야 합니다.
- Twilio의 요청 형식을 충족하려면 메시지 내용에 `url_param_escape` Liquid 필터를 사용하세요. 이 필터는 문자열을 인코딩하여 모든 문자가 HTML 요청에서 허용되도록 합니다. 예를 들어, 전화번호 `+12125551212`의 더하기 문자(`+`)는 URL 인코딩된 데이터에서 금지되어 있으며 `%2B12125551212`로 변환됩니다.

![웹훅 본문]({% image_buster /assets/img_archive/Webhook_Body.png %})

## 요청 헤더 및 메서드

Twilio는 두 개의 요청 헤더, 즉 요청 콘텐츠 유형과 [HTTP 기본 인증](https://en.wikipedia.org/wiki/Basic_access_authentication#Client_side) 헤더를 요구합니다. 웹훅 작성기 옆에 있는 톱니바퀴 아이콘을 클릭한 다음 *새 쌍 추가*를 두 번 클릭하여 웹훅에 추가하십시오.

헤더 이름 | 헤더 값
--- | ---
콘텐츠-유형 | `application/x-www-form-urlencoded`
승인 | `{% raw %}Basic {{ 'TWILIO_ACCOUNT_SID:TWILIO_AUTH_TOKEN' | base64_encode }}{% endraw %}`

`TWILIO_ACCOUNT_SID` 및 `TWILIO_AUTH_TOKEN`을 Twilio 대시보드의 값으로 바꾸세요. 마지막으로, Twilio의 API 엔드포인트는 HTTP POST 요청을 기대하고 있으므로 *HTTP Method* 드롭다운에서 해당 옵션을 선택하세요.

![웹훅 방법]({% image_buster /assets/img_archive/Webhook_Method.png %})

## 요청 미리보기

웹훅 작성기를 사용하여 무작위 사용자 또는 특정 자격 증명을 가진 사용자의 요청을 미리 보고 요청이 올바르게 렌더링되는지 확인하세요.

![웹훅 미리보기]({% image_buster /assets/img_archive/Webhook_Preview.png %})

