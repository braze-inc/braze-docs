---
nav_title: 동적 코드 생성
article_title: Punchh 동적 코드 생성
page_order: 2
description: "이 참조 문서에서는 Braze에서 Punchh 동적 코드 생성을 사용하는 방법을 간략히 설명합니다."
page_type: partner
search_tag: Partner
---

# Punchh로 동적 코드 생성

> 쿠폰 코드는 한 명의 사용자가 사용할 수 있는 고유 코드입니다(1회 또는 여러 번 사용 가능). Punchh 프레임워크는 모바일 앱 또는 POS(Point-of-Sale) 시스템에서 처리할 수 있는 쿠폰 코드를 생성합니다.

_This integration is maintained by Punchh._

## 통합 정보

Punchh 쿠폰 프레임워크와 Braze를 사용하면 다음과 같은 시나리오를 달성할 수 있습니다:

- 게스트가 이메일의 쿠폰 생성 링크를 클릭하면 쿠폰 코드를 생성합니다: 쿠폰 코드는 동적으로 생성되어 웹 페이지에 표시됩니다.
- 게스트가 이메일을 열면 쿠폰 코드를 생성합니다: 쿠폰 코드는 동적으로 생성되며 이메일 내에 이미지로 표시됩니다.

## 동적 쿠폰 코드 생성 통합

### 1단계: 쿠폰 캠페인 만들기

1. 펀치 쿠폰 캠페인을 사용하여 다음 이미지와 같이 동적 생성 쿠폰 캠페인을 생성합니다.
2. 펀치 쿠폰 프레임워크는 동적 쿠폰 생성을 활성화하기 위해 다음 파라미터를 생성합니다:
    - 동적 쿠폰 생성 토큰: 암호화를 위해 시스템에서 생성된 보안 토큰입니다.
    - 동적 쿠폰 생성 URL: 이 URL은 비즈니스의 필요에 따라 링크 또는 이미지로 이메일에 포함됩니다.

![The form for creating a coupon campaign in Punchh.]({% image_buster /assets/img/punchh/punchh8.png %}){: style="max-width:60%;"}

### 2단계: 서명 생성 및 URL 구성

JWT.IO 라이브러리는 두 당사자 간에 클레임을 안전하게 표현하기 위한 개방형 업계 표준 RFC 7519 방식인 JSON 웹 토큰을 디코딩, 검증 및 생성합니다. 

게스트와 쿠폰의 고유성을 보장하기 위해 다음 `ClaimType` 이름을 사용할 수 있습니다.

- `campaign_id`: 시스템에서 생성된 Punchh 캠페인 ID를 나타냅니다.
- `email`: 사용자의 이메일 주소를 나타냅니다. 
- `first_name`: 사용자의 이름을 캡처합니다. 
- `last_name`: 사용자의 성을 캡처합니다.

Punchh 동적 쿠폰 코드 API를 사용하려면 JWT 토큰을 생성해야 합니다. 사용하려는 채널의 메시지 본문에 있는 Braze 대시보드에 다음 Liquid 템플릿을 추가하세요:

{% raw %}
```liquid
{% assign header = '{"alg":"HS256","typ":"JWT"}' | base64_encode | replace: '=', '' | replace: '+', '-' | replace: '/', '_' %}

{% capture payload_raw %}

{
  "campaign_id": "CAMPAIGN_ID",
  "email": "{{${email_address}}}",
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}"
}

{% endcapture %}

{% assign payload = payload_raw | replace: ' ', '' | replace: '\n', '' | base64_encode | replace: '=', '' | replace: '+', '-' | replace: '/', '_' %}

{% assign unsigned_token = header | append: "." | append: payload %}

{% assign secret = "DYNAMIC_COUPON_GENERATION_TOKEN" %}

{% assign signature_raw = unsigned_token | hmac_sha256_base64: secret %}

{% assign signature = signature_raw | replace: '=', '' | replace: '+', '-' | replace: '/', '_' %}

{% assign jwt = unsigned_token | append: "." | append: signature %}

```
{% endraw %}


다음을 교체합니다:

| 입력 안내        | 설명                                          |
|--------------------|------------------------------------------------------|
| `DYNAMIC_COUPON_GENERATION_TOKEN` | 동적 쿠폰 생성 토큰입니다. |
| `CAMPAIGN_ID`                     | 캠페인 ID.                     |

### 3단계: 메시지 본문에 쿠폰 코드 추가

#### Punchh 웹 페이지로 연결

Punchh 호스팅 웹 페이지로 연결하려면 [앞서 생성](#step-1-create-a-coupon-campaign-in-punchh)한 동적 생성 URL에 `{% raw %}{{jwt}}{% endraw %}`를 추가합니다. 링크는 다음과 유사해야 합니다: 

{% raw %}
```
https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX?sign={{jwt}}
```
{% endraw %}

사용자가 쿠폰 URL을 클릭하면 Punchh에서 호스팅하는 웹 페이지로 리디렉션되며, 생성된 쿠폰이 표시됩니다.

![사용자가 쿠폰 코드를 성공적으로 생성한 후 확인 메시지 예제.]({% image_buster /assets/img/punchh/punchh7.png %})

#### JSON을 통해 일반 텍스트로 코드 추출하기

JSON 응답을 반환하려면 [앞서 생성](#step-1-create-a-coupon-campaign-in-punchh)한 동적 생성 URL에 `{% raw %}{{jwt}}{% endraw %}`를 추가한 다음, URL 문자열의 토큰 뒤에 `.json`을 추가합니다. 링크는 다음과 유사해야 합니다:

{% raw %}
```liquid
https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.json?sign={{jwt}}
```
{% endraw %}

그런 다음, [연결된 콘텐츠]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/)를 활용하여 메시지 본문에 일반 텍스트로 코드를 삽입할 수 있습니다. 예를 들어, 다음과 같습니다.

{% raw %}
```liquid
{% connected_content https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.json?sign={{jwt}} :save punchh_coupon %}
{{punchh_coupon.coupon}}
````
{% endraw %}

#### 이메일 콘텐츠에 이미지 링크하기

이미지 안에 쿠폰 코드를 링크하려면:

1. [앞서 생성](#step-1-create-a-coupon-campaign-in-punchh)한 동적 생성 URL에 `{% raw %}{{jwt}}{% endraw %}`를 추가합니다.
2. URL 문자열의 토큰 뒤에 `.png` 을 추가합니다.
3. HTML {% raw %}`<img>`{% endraw %} 태그에 링크를 삽입합니다.

{% tabs 로컬 %}
{% tab 입력 예제 %}
{% raw %}
```liquid
<img src="https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.png?sign={{jwt}}">
````
{% endraw %}
{% endtab %}

{% tab 출력 예제 %}
![쿠폰 코드 이미지 태그의 렌더링 출력.]({% image_buster /assets/img/punchh/punchh9.png %})
{% endtab %}
{% endtabs %}

## 오류 메시지

| 오류 코드 | 오류 메시지 | 설명 |
| --- | --- | --- |
| `coupon_code_expired` | 이 프로모션 코드가 만료되었습니다. | 이 코드는 구성된 만료일 이후에 사용됩니다. |
| `coupon_code_success` | 축하합니다, 프로모션 코드가 성공적으로 적용되었습니다. | 코드가 성공적으로 사용되었습니다. |
| `coupon_code_error` | 유효한 프로모션 코드를 입력하세요. | 사용된 코드가 유효하지 않습니다. |
| `coupon_code_type_error` | 쿠폰 유형이 잘못되었습니다. 이 쿠폰은 `%{coupon_type}` 에서만 사용할 수 있습니다. | POS에서 사용해야 하는 코드가 모바일 앱에서 사용되면 이 오류가 발생합니다. |
| `usage_exceeded` | 이 쿠폰 코드의 캠페인 사용량이 모두 사용되었습니다. 다음에 다시 시도하세요. | 코드 사용량이 허용된 사용자 수를 초과합니다. 예를 들어 대시보드 구성에서 3,000명의 사용자가 코드를 사용할 수 있도록 허용했을 때 사용자 수가 3,000명을 초과하는 경우 이 오류가 발생합니다. |
| `usage_exceeded_by_guest` | 이 프로모션 코드는 이미 처리되었습니다. | 사용자의 코드 사용 횟수가 사용자가 코드를 사용할 수 있는 횟수를 초과합니다. 예를 들어, 대시보드 구성에서는 사용자가 하나의 코드를 세 번 사용할 수 있도록 허용합니다. 이를 초과하여 사용하면 이 오류가 발생합니다. |
| `already_used_by_other_guest` | 이 프로모션 코드는 다른 게스트가 이미 사용했습니다. | 다른 사용자가 이미 코드를 사용했습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

