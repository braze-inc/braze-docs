---
nav_title: Inkit
article_title: Inkit
alias: /partners/inkit/
description: "이 참고 문서에서는 다이렉트 메일 캠페인을 자동화하여 시간과 노력을 절약하고 오프라인 고객을 다시 온라인으로 유도할 수 있는 Braze와 Inkit의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner

---

# Inkit

> [Inkit][1]과 Braze는 디지털 방식은 물론 다이렉트 메일을 통해서도 문서를 안전하게 생성 및 배포할 수 있도록 조직의 역량을 강화합니다.

_This integration is maintained by Inkit._

## 통합 정보

Braze와 Inkit의 통합을 통해 문서를 생성하고 Braze 웹훅을 사용하여 Braze 사용자에게 직접 메일을 보낼 수 있습니다.

## 전제 조건

|요구 사항| 설명|
| ---| ---|
|Inkit 계정 | 이 파트너십을 활용하려면 [Inkit 계정](https://www.inkit.com/)이 필요합니다. |
| Inkit API 키<br><br>`<INKIT_API_TOKEN>` | 이 키는 [Inkit 대시보드](https://app.inkit.io/#/account/integrations)의 **개발** 탭에서 찾을 수 있으며, 이 키를 사용해 Braze와 Inkit 계정을 연결할 수 있습니다.|
| Inkit 템플릿 ID<br><br>`<INKIT_TEMPLATE_ID>` | 템플릿을 만든 후 **템플릿** 탭에서 템플릿 ID를 복사하여 Braze의 템플릿에 사용할 수 있습니다.<br><br>예를 들어, Inkit 환경에서 템플릿 ID가 `tmpl_3bDScFl9cwr3OAVR1RSdEC`인 `invoice_template`이라는 템플릿을 생성할 수 있습니다.
| HTTP 헤더 | HTTP 헤더는 Braze에서 Inkit으로 보내는 API 요청의 일부입니다. 여기에는 Inkit API 호출을 인증하고 권한을 부여하기 위한 Inkit API 키가 포함됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 통합

### 1단계: Inkit 템플릿 만들기

Inkit 플랫폼에서 Braze 캠페인에 사용할 템플릿을 HTML, Word, PowerPoint, Excel 또는 PDF로 생성합니다. 자세한 내용은 [Inkit 설명서를](https://docs.inkit.com/docs/create-a-template) 참조하세요.

### 2단계: Braze 웹훅 템플릿 만들기

향후 캠페인이나 캔버스에서 사용할 Inkit 웹훅 템플릿을 만들려면 Braze 플랫폼에서 **템플릿** > **웹훅 템플릿으로** 이동하세요. 

일회성 Inkit 웹훅 캠페인을 생성하거나 기존 템플릿을 사용하려면 새 캠페인을 생성할 때 Braze에서 **웹훅**을 선택합니다.

![템플릿 및 미디어 섹션의 웹훅 템플릿 탭에서 미리 디자인된 선택 가능한 웹훅 템플릿 옵션.][7]

Inkit 웹훅 템플릿을 선택하면 다음과 같은 내용이 표시됩니다:
- **웹훅 URL**: 빈 여백
- **요청 본문**: 원시 텍스트

웹훅 URL 필드에 Inkit 웹훅 URL을 [생성](https://docs.inkit.com/docs/set-up-a-webhook-to-an-event)하고 입력해야 합니다.

![Braze 웹훅 빌더 작성 탭에 표시된 요청 본문 코드와 웹훅 URL.][5]

#### 요청 헤더 및 메서드

Inkit은 base 64로 인코딩된 Inkit API 키가 포함된 인증용 `HTTP Header`를 요구합니다. 다음은 이미 템플릿에 키-값 페어로 포함되어 있지만 **설정** 탭에서 `<INKIT_API_TOKEN>`을 Inkit API 키로 바꿔야 합니다.

{% raw %}
- **HTTP 메서드**: POST
- **요청 헤더**:
  - **권한 부여**: 기본 `{{ '<INKIT_API_TOKEN>' | base64_encode }}`
  - **Content-Type**: application/json
{% endraw %}

#### 요청 본문

Liquid가 다음 필수 필드 및 선택적 필드와 관련된 적절한 커스텀 속성과 일치하는지 확인합니다. 요청에 사용자 지정 데이터 필드를 추가할 수도 있습니다.

```json
{% raw %}{
  "api_token": "<INKIT_API_TOKEN>",
  "template_id": "<INKIT_TEMPLATE_ID>",
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}",
  "email": "{{${email_address}}}",
  "company": "{{custom_attribute.${company_name}}}",
  "phone" : "{{${phone_number}}}",
  "address_line_1": "{{custom_attribute.${address}}}",
  "address_line_2": "{{custom_attribute.${address2}}}",
  "address_city": "{{${city}}}",
  "address_state": "{{custom_attribute.${state}}}",
  "address_zip": "{{custom_attribute.${zip}}}",
  "address_country": "{{${country}}}",
  "source" : "Braze"
}{% endraw %}
```

### 3단계: 요청 미리보기

원시 텍스트가 적용 가능한 Braze 태그인 경우 자동으로 강조 표시됩니다. 이 웹훅을 전송하려면 `street`, `unit`, `state`, `zip`을 [커스텀 속성][3]으로 설정해야 합니다.

**미리보기** 패널에서 요청을 미리 보거나 **테스트** 탭으로 이동하여 무작위 사용자, 기존 사용자를 선택하거나 직접 사용자 지정하여 웹훅을 테스트할 수 있습니다.

{% alert important %}
페이지에서 나가기 전에 템플릿을 저장하는 것을 잊지 마세요! <br>업데이트된 웹훅 템플릿은 새 [웹훅 캠페인을]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) 만들 때 **저장된 웹훅 템플릿** 목록에서 찾을 수 있습니다.
{% endalert %}


[1]: https://www.inkit.com
[2]: https://help.inkit.com/hc/en-us/articles/360036546873-Braze-Inkit-Integration
[3]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attributes
[5]: {% image_buster /assets/img/inkit-integration.png %}
[6]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
[7]: {% image_buster /assets/img/inkit-webhook-template.png %}