---
nav_title: 옵틸리즈
article_title: 옵틸리즈
description: "이 참조 문서에서는 Optilyz와 Braze 간의 파트너십을 간략히 설명합니다. 이를 통해 고객 중심의 지속 가능하고 수익성 있는 다이렉트 메일 캠페인을 운영할 수 있습니다."
alias: /partners/optilyz/
page_type: partner
search_tag: Partner

---

# 옵틸리즈

> [optilyz][1]는 보다 고객 중심적이고 지속 가능하며 수익성 높은 다이렉트 메일 캠페인을 시행할 수 있는 다이렉트 메일 자동화 플랫폼입니다. 

_This integration is maintained by optilyz._

## 통합 정보

optilyz와 Braze 웹훅 통합을 사용하여 고객에게 편지, 엽서, 셀프 메일러 등의 다이렉트 메일을 보낼 수 있습니다.

## 전제 조건

| 요구 사항 | 설명 |
|---|---|
|optilyz 계정 | 이 파트너십을 활용하려면 Optilyz 계정이 필요합니다. |
| optilyz API 키<br><br>`<OPTILYZ_API_KEY>`| optilyz 고객 성공 매니저가 optilyz API 키를 제공합니다.<br><br>이 API 키를 사용하면 Braze와 Optilyz 계정을 연결할 수 있습니다. |
| optilyz 자동화 ID<br><br>`<OPTILYZ_AUTOMATION_ID>` | 자동화 ID는 페이지 헤더의 상자에서 찾을 수 있습니다.<br><br>optilyz에 로그인하면 데이터를 전송할 자동화로 이동할 수 있습니다.<br>먼저 자동화를 활성화해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 사용 사례

다이렉트 메일을 디지털 채널처럼 운영한다는 것은 대량 메일 발송에서 벗어나 채널을 (디지털) 고객 여정의 일부로 활용한다는 의미입니다. 다이렉트 메일에 대한 최신 접근 방식의 이점은 다음과 같습니다:
- 관련성 향상, 추가 사용 사례, 간편한 A/B 테스트, 크로스 채널 효과를 통한 전환율 증대
- 자동화와 엔드투엔드 솔루션을 통한 노력 절감
- 프레임 계약 및 비용 투명성을 통한 비용 절감

## 통합

optilyz와 통합하려면 [optilyz API][2]를 사용하여 수신자 데이터를 Braze 웹훅으로 전송합니다.

### 1단계: Braze 웹훅 템플릿 만들기

향후 캠페인 또는 캔버스에서 사용할 옵틸리즈 웹훅 템플릿을 만들려면 Braze 플랫폼에서 **템플릿** > **웹훅 템플릿으로** 이동하세요. 

일회성 optilyz 웹훅 캠페인을 생성하거나 기존 템플릿을 사용하려면 새 캠페인을 생성할 때 Braze에서 **웹훅**을 선택합니다.

새 웹훅 템플릿에서 다음 필드를 입력합니다:
- **웹훅 URL**: 웹훅 URL은 고객마다 고유하며 Optilyz 고객 성공 매니저가 제공합니다.
- **요청 본문**: 원시 텍스트

#### 요청 헤더 및 메서드

optilyz에는 권한 부여용 HTTP 헤더와 HTTP 메서드도 필요합니다. 다음은 이미 템플릿에 키-값 페어로 포함되어 있지만 **설정** 탭에서 `<OPTILYZ_API_KEY>`를 optilyz API 키로 바꿔야 합니다. 이 키는 키 바로 뒤에 ':'를 포함하고 base 64로 인코딩되어야 합니다. 

- **HTTP 메서드**: POST
- **요청 헤더**:
  - **권한 부여**: {% raw %} `{{ '<OPTILYZ_API_KEY>:' | base64_encode }}` {% endraw %}
  - **Content-Type**: application/json

![Braze 웹훅 빌더에 표시되는 요청 헤더와 HTTP 메서드입니다.][6]{: style="max-width:50%"}

#### 요청 본문

다음 요청 본문에서 optilyz [API 설명서][2]에 따라 커스텀 요청 템플릿을 빌드하고 Liquid 개인화 태그를 사용할 수 있습니다.

`variation` 필드는 선택 사항이며 자동화 내부에서 사용할 디자인을 정의할 수 있습니다. 변형을 생략하면 optilyz는 정의된 변형 중 하나를 무작위로 할당합니다.

{% raw %}
```json
{
    "address": {
        "title": "{{custom_attribute.${salutation}}}",
        "firstName": "{{${first_name}}}",
        "lastName": "{{${last_name}}}",
        "street": "{{custom_attribute.${street}}}",
        "houseNumber": "{{custom_attribute.${houseNumber}}}",
        "address2": "{{custom_attribute.${address2}}}",
        "zipCode": "{{custom_attribute.${zipCode}}}",
        "city": "{{custom_attribute.${city}}}",
        "country": "{{custom_attribute.${country}}}"
    },
    "variation": {{custom_attribute.${designVariation}}}
}
```
{% endraw %}

![Braze 웹훅 빌더 작성 탭에 표시되는 요청 본문 코드 및 웹훅 URL 이미지입니다.][5]

### 2단계: 요청 미리보기

그런 다음 **미리보기** 패널에서 요청을 미리 보거나 **테스트** 탭으로 이동하여 무작위 사용자, 기존 사용자를 선택하거나 직접 사용자 지정하여 웹훅을 테스트할 수 있습니다. 페이지에서 나가기 전에 템플릿을 저장하는 것을 잊지 마세요!

![Braze 웹훅 빌더의 테스트 탭에서 사용 가능한 여러 테스트 필드.][7]

{% alert important %}
페이지에서 나가기 전에 템플릿을 저장하는 것을 잊지 마세요! <br>업데이트된 웹훅 템플릿은 새 [웹훅 캠페인을]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) 만들 때 **저장된 웹훅 템플릿** 목록에서 찾을 수 있습니다.
{% endalert %}


[1]: https://optilyz.com
[2]: https://www.optilyz.com/doc/api/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template/
[5]: {% image_buster /assets/img/optilyz/optilyz_compose.png %}
[6]: {% image_buster /assets/img/optilyz/optilyz_settings.png %}
[7]: {% image_buster /assets/img/optilyz/optilyz_testing.png %}
[9]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/