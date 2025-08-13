---
nav_title: Lob
article_title: Lob 
alias: /partners/lob/
description: "이 참고 문서에서는 우편을 통해 편지, 엽서, 수표 등의 다이렉트 메일을 보낼 수 있는 Braze와 Lob.com의 파트너십에 대해 간략하게 설명합니다."
page_type: partner
search_tag: Partner

---

# Lob

> [Lob.com][38]은 사용자에게 다이렉트 메일을 보낼 수 있는 온라인 서비스입니다.

Braze와 Lob의 통합을 통해 Braze 웹훅과 Lob API를 활용하여 편지, 엽서, 수표 등의 메일을 우편으로 전송할 수 있습니다.  

## 필수 조건

|요구 사항| 설명|
| ---| ---|
|Lob 계정 | 이 파트너십을 이용하려면 Lob 계정이 필요합니다. |
| Lob API 키 | Lob API 키는 Lob 대시보드의 사용자 이름 아래 설정 섹션에서 찾을 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

### 1단계: Lob 엔드포인트 선택

웹훅에서 요청할 HTTP URL은 Lob에 수행할 수 있는 작업마다 다릅니다. 다음 예제에서는 엽서 API 엔드포인트 `https://api.lob.com/v1/postcards` 를 사용합니다. 사용 사례에 적합한 엔드포인트를 선택하려면 [전체 엔드포인트 목록][39]을 참조하세요. 

| API 엔드포인트 | 사용 가능한 엔드포인트 |
| ------------ | ------------------- |
| https://api.lob.com/ | /v1/addresses<br>/v1/addresses/{id}<br>/v1/verify<br>/v1/postcards<br>/v1/postcards/{id}<br>/v1/letter<br>/v1/letter/{id}<br>/v1/checks<br>/v1/checks/{id}<br>/v1/bank_accounts<br>/v1/bank_accounts/{id}<br>/v1/bank_accounts/{id}/verify<br>/v1/areas<br>/v1/areas/{id}<br>/v1/routes/{zip_code}<br>/v1/routes<br>/v1/countries<br>/v1/states|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 2단계: Braze 웹훅 템플릿 만들기

향후 캠페인이나 캔버스에서 사용할 Lob 웹훅 템플릿을 만들려면 Braze 플랫폼에서 **템플릿** > **웹훅 템플릿으로** 이동하세요. 

일회성 Lob 웹훅 캠페인을 만들거나 기존 템플릿을 사용하려면 새 캠페인을 만들 때 Braze에서 **웹훅을** 선택하세요.

새 웹훅 템플릿에서 다음 필드를 입력합니다:
- **웹훅 URL**: `<LOB_API_ENDPOINT>`
- **요청 본문**: 원시 텍스트

#### 요청 헤더 및 메서드

Lob에는 권한 부여를 위한 HTTP 헤더와 HTTP 메서드가 필요합니다. 다음은 이미 템플릿에 키-값 페어로 포함되어 있지만 **설정** 탭에서 `<LOB_API_KEY>`를 Lob API 키로 바꿔야 합니다. 이 키는 키 바로 뒤에 ':'를 포함하고 base 64로 인코딩되어야 합니다. 

- **HTTP 메서드**: POST
- **요청 헤더**:
  - **권한 부여**: 기본 `{{'<LOB_API_KEY>:' | base64_encode}}`
  - **Content-Type**: application/json

![Braze 웹훅 빌더 작성 탭에 표시된 요청 본문 코드와 웹훅 URL.][35]

#### 요청 본문

다음은 Lob 엽서 엔드포인트의 요청 본문 예시입니다. 이 요청 본문은 Braze의 기본 Lob 템플릿에서 제공되지만, 다른 엔드포인트를 사용하려면 적절히 Liquid 필드를 조정해야 합니다.

```json
{% raw %}"description": "Demo Postcard",
"to": {
    "name": "{{${first_name}}} {{${last_name}}}",
    "address_line1": "{{custom_attribute.${address_line1}}}",
    "address_city": "{{custom_attribute.${address_city}}}",
    "address_zip": "{{custom_attribute.${address_zip}}}",
    "address_country": "{{custom_attribute.${address_country}}}"
},
"front": "https://lob.com/postcardfront.pdf",
"back": "https://lob.com/postcardback.pdf"{% endraw %}
```

### 3단계: 요청 미리보기

이 시점에서 캠페인을 테스트하고 전송할 준비가 된 것입니다. 오류가 발생하면 Lob 대시보드와 Braze 개발자 콘솔 오류 메시지 로그를 확인합니다. 예를 들어 다음 오류는 잘못된 형식의 인증 헤더로 인해 발생했습니다. 

![시간, 앱 이름, 채널, 오류 메시지가 표시된 메시지 오류 로그. 오류 메시지에는 메시지 경고와 상태 코드가 포함됩니다.][36]

{% alert important %}
페이지에서 나가기 전에 템플릿을 저장하는 것을 잊지 마세요! <br>업데이트된 웹훅 템플릿은 새 [웹훅 캠페인을]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) 만들 때 **저장된 웹훅 템플릿** 목록에서 찾을 수 있습니다.
{% endalert %}

[33]: {% image_buster /assets/img_archive/lob_api_key.png %}
[34]: {% image_buster /assets/img_archive/lob_success_response.png %}
[35]: {% image_buster /assets/img_archive/lob_full_request.png %}
[36]: {% image_buster /assets/img_archive/error_log.png %}
[37]: {% image_buster /assets/img_archive/lob_api_endpoint.png %}
[38]:https://lob.com
[39]:https://lob.com/docs#intro
[40]:https://lob.com/docs#auth
