---
nav_title: FAQ
article_title: 자주 묻는 질문
page_order: 12
description: "이 문서에서는 Liquid에 대해 자주 묻는 질문에 대한 답변을 제공합니다."

---

# 자주 묻는 질문

> 이 페이지에서는 Liquid에 관해 자주 묻는 질문에 대한 답변을 확인할 수 있습니다.<br><br>Braze는 현재 Shopify Liquid의 100%를 지원하지 않으며, 설명서에서 설명한 특정 부분만 지원합니다. 오류나 지원되지 않는 Liquid를 사용할 위험을 줄이기 위해 모든 메시지를 보내기 전에 Liquid를 사용하여 테스트하는 것을 적극 권장합니다.

### Braze에서 리퀴드 스니펫은 어떻게 사용하나요?

대부분의 경우 캠페인 또는 캔버스로 이동하여 이메일 메시지 본문이나 세그먼트와 같은 영역의 개인화 모달에 Liquid 스니펫을 삽입하여 Liquid 스니펫을 통합할 수 있습니다. 

#### 자세한 내용은 어디에서 확인할 수 있나요?

Liquid에 대한 자세한 내용은 [Liquid Braze 학습 경로를 통한 동적 개인화](https://learning.braze.com/path/dynamic-personalization-with-liquid) 가이드를 확인하세요! 또한 Liquid [사용 사례 라이브러리를]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/) 참조하여 영감을 얻고 Liquid를 사용한 다양한 개인화 사례를 살펴볼 수도 있습니다.

### 개인화를 위해 리퀴드와 커넥티드 콘텐츠를 사용하는 것의 차이점은 무엇인가요?

Braze 연결된 콘텐츠는 Liquid 태그의 예시입니다. 이 데이터는 개인화에도 사용되지만, Braze 내에 저장된 데이터가 아닌 외부 엔드포인트에서 가져온 데이터입니다. 메시지를 맞춤 설정하는 방법을 확장하는 방법에 대해 자세히 알아보려면 전용 [커넥티드 콘텐츠]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) 섹션을 확인하세요.

### 리퀴드 템플릿이란 무엇인가요?

이것은 Braze에서 Liquid를 사용하는 가장 일반적인 방법입니다. Liquid 템플릿은 고객 프로필에서 데이터를 메시지로 가져오는 작업을 포함합니다. 이 데이터는 사용자의 이름부터 이벤트 트리거된 메시지의 커스텀 이벤트까지 다양합니다.

지원되는 Liquid 태그의 전체 목록은 [지원되는 개인화 태그]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)를 참조하세요.

### Liquid로 변수를 할당하려면 어떻게 하나요?

`assign` 태그를 사용하여 변수를 생성하고 할당할 수 있습니다. 이렇게 하면 메시지 작성기에 메시지 전체에서 참조할 수 있는 변수가 만들어집니다.

### Liquid를 사용하면 데이터 포인트가 소모되나요?

아니요.

### Liquid를 사용하여 개인화된 인사말을 보내려면 어떻게 해야 하나요?

사용자의 이름을 사용하여 개인화된 인사말을 만들려면 {% raw %} `{{${first_name}}}`, `{{${last_name}}}`과 같은 표준 고객 프로필 속성을 가져올 수 있습니다.

Liquid `{% if X %}` {% endraw %}문을 사용하여 요일이나 커스텀 속성 등 무엇이든 기반으로 조건부 렌더링을 수행할 수도 있습니다. 조건문에 사용할 수 있는 지원되는 Liquid 연산자에 대한 자세한 내용은 [연산자에서]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/operators/) 확인하세요.

### 고객의 위치를 기반으로 메시지를 개인화하려면 어떻게 해야 하나요?

{% raw %}
사용자 위치에 대한 기본 속성은 `{{${most_recent_location}}}` 입니다.

### {{campaign.${name}}}와 {{campaign.${message_name}}}의 차이점은 무엇인가요?

`{{campaign.${name}}}` 및 `{{campaign.${message_name}}}` 모두 Liquid 개인화 태그가 지원됩니다. 두 태그는 캠페인 속성을 참조합니다. `{{campaign.${name}}}`은 캠페인의 이름을 나타내고 `{{campaign.${message_name}}}`은 메시지 배리언트의 이름입니다.
{% endraw %}

### 중첩된 오브젝트와 함께 Liquid를 사용하려면 어떻게 해야 하나요?

Braze에는 메시지에서 사용할 수 있는 세그먼트에 대한 리퀴드 코드를 생성하는 기능이 내장되어 있습니다. 특히 개체에서 여러 기준과 일치하는 세그먼트를 만들 수 있습니다.

자세한 내용은 [다중 기준 세분화를]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#multi-criteria-segmentation) 참조하세요.

### 이벤트 속성을 사용하여 이벤트가 트리거하는 메시지를 개인화하려면 어떻게 해야 하나요?

{% raw %}
`api_triggered_property` 태그(`{{api_trigger_properties.${attribute_key}}}`)를 사용하여 API 트리거 이벤트의 속성에 액세스할 수 있습니다.  
{% endraw %}

### 중단 로직이란 무엇이며 어떻게 사용할 수 있나요?

중단 로직을 사용하면 조건이 충족되는 경우 메시지 전송을 중지할 수 있습니다. 이는 특히 사용자에게 불완전한 메시지가 전송되는 것을 방지하는 데 유용합니다. 마케팅 캠페인에서 로직 중단의 예를 보려면 [메시지 중단하기]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/)에서 자세히 알아보세요.

### 루프 로직이란 무엇이며 어떻게 사용할 수 있나요?

루프는 [반복 태그](https://shopify.github.io/liquid/tags/iteration/)라고도 합니다. Liquid 스니펫에서 for 루프 로직을 사용하면 조건이 충족될 때까지 Liquid 블록을 순환할 수 있습니다. 

Braze에서는 배열 사용자 지정 속성의 항목이나 [카탈로그]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs) 또는 [커넥티드 콘텐츠]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) 호출 응답에서 반환된 값 및 개체 목록을 확인하는 데 사용할 수 있습니다. 특히, 제품의 재고가 있는지 또는 제품의 최소 등급이 있는지 확인하는 메시징의 일부로 루프 로직을 사용할 수 있습니다. 

예를 들어 100개의 행으로 구성된 카탈로그를 검색하고 Get Going이라는 신발 회사의 모든 이미지를 포함하려는 경우 이 Liquid 스니펫을 사용할 수 있습니다:

{% raw %}

```liquid
{% for item in catalog %}
{% if {{item.brand}} = "GetGoing %}
{{item.image}}
{% endif %}
{% endfor %}
```

{% endraw %}

설정된 조건이 충족되면 메시지를 진행할 수 있습니다. 이 로직을 사용하면 다양한 조건에 대해 Liquid 블록을 반복하는 대신 시간을 절약할 수 있습니다.
