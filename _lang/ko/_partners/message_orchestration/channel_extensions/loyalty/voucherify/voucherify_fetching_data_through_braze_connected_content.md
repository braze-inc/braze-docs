---
nav_title: 커넥티드 콘텐츠를 통해 데이터 가져오기
article_title: Voucherify에서 연결된 콘텐츠를 통해 데이터 가져오기
page_order: 2
alias: /partners/voucherify/connected_content/
description: "이 참조 문서에서는 Braze 연결된 콘텐츠를 통해 Voucherify API에서 데이터를 가져와 특정 Braze 세그먼트에 메시지를 보내는 방법을 간략하게 설명합니다."
page_type: partner
search_tag: Partner
---

# 커넥티드 콘텐츠를 통해 데이터 가져오기

> Braze 커넥티드 콘텐츠를 사용하면 Voucherify API에서 데이터를 가져와 특정 Braze 세그먼트에 메시지를 보낼 수 있습니다. 이 참조 문서에서는 연결된 콘텐츠 스크립트를 설정하여 Voucherify 쿠폰을 게시하고, 새 추천인을 초대하며, 로열티 카드 잔액을 검색하는 등의 작업을 수행하는 방법을 설명합니다.

_This integration is maintained by Voucherify._

## 통합 정보

스크립트의 기본 스키마는 다음과 같습니다:
{% raw %}
```json
{% connected content
  "voucherify-API-ENDPOINT-url"
  :method post
  :headers {
    "X-App-Id": "Voucherify-API-key",
    "X-App-Token": "Voucherify-Secret-key",
  }
  :content_type application/json
  :retry
  :save {{result_variable}}
}
```
{% endraw %}

연결된 콘텐츠 스크립트 예제를 보려면 Voucherify [GitHub 리포지토리](https://github.com/voucherifyio/braze-connected-content)를 참조하세요.

## 보안 설정

연결된 콘텐츠 메시지가 트리거될 때마다 다음 설정을 구성하지 않으면 Voucherify API를 최소 두 번 호출합니다. 이러한 설정은 Braze에 청구되는 API 호출 수를 줄이고 메시지 전송을 중단시킬 수 있는 하드 블로킹 API 한도에 도달할 위험을 줄여줍니다.

{% tabs %}
{% tab 사용량 제한 도구 %}

**사용량 제한 도구**

Braze에서 분당 전송할 수 있는 [메시지 수를 제한]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting)해야 합니다. 이렇게 하면 캠페인에서 너무 많은 트래픽이 발생하지 않도록 Braze와 Voucherify API를 모두 보호할 수 있습니다. 캠페인 설정 중 사용자를 타겟팅할 때는 전송 속도를 분당 500건으로 제한합니다.

![]({% image_buster /assets/img/voucherify/voucherify_cc_limiter.png %})

{% endtab %}
{% tab 캐싱 %}

**POST 호출에서 캐싱**

HTTP POST를 통해 수행되는 연결된 콘텐츠 호출은 기본적으로 캐시되지 않으며 게시된 각 코드당 두 번의 API 요청을 수행합니다. 이 동작은 API 한도에 부담을 줄 수 있습니다. 캐싱 메커니즘을 사용하면 바우처 게시당 한 번의 API 호출로 제한할 수 있습니다. 

{% alert important %}
이 튜토리얼의 모든 연결된 콘텐츠 예제에는 Braze에서 트리거되는 API 호출 수를 줄이기 위한 기본 캐싱이 포함되어 있습니다.
{% endalert %}

POST 호출에 캐싱을 추가하려면 다음과 같이 하세요:

1. {% raw %}`:cache_max_age`{% endraw %} 어트리뷰트를 추가합니다. 기본적으로 캐싱 기간은 5분입니다. 초 단위로 기간을 사용자 지정할 수 있습니다. 5분에서 4시간 사이로 설정할 수 있습니다. 예: {% raw %}`:cache_max_age 3600`{% endraw %} 1시간 동안 캐시됩니다.
2. 대상 엔드포인트 쿼리 매개변수에 캐싱 키 {% raw %}`cache_id={{cache_id}}`{% endraw %}를 제공하여 Braze가 고유한 게시를 식별할 수 있도록 합니다. 먼저 변수를 정의한 다음, 고유한 쿼리 문자열을 엔드포인트에 추가합니다. 그러면 {% raw %}`source_id`{% endraw %}로 각 게시를 구분합니다.

![]({% image_buster /assets/img/voucherify/voucherify_cc_cache.png %})

_결과는 다음과 같습니다._ Braze는 URL을 기반으로 API 호출을 캐시합니다. 쿼리 매개변수로 사용된 고유 문자열은 Voucherify에서 무시되지만, Braze에 대한 다양한 API 요청을 구분하고 각 고유 시도를 개별적으로 캐시할 수 있습니다. 해당 쿼리 매개변수가 없으면 모든 고객이 캐시 기간 동안 동일한 쿠폰 코드를 받게 됩니다.

{% endtab %}
{% tab 재시도 속성 %}

**재시도 속성**

연결된 콘텐츠는 Voucherify 응답의 유효성을 검증하지 않으므로 연결된 콘텐츠 스크립트에 [재시도]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries) 속성을 추가하는 것이 좋습니다. 연결된 콘텐츠 로직은 메시지를 중단하기 전에 5번 재시도를 시도합니다(사용량 제한 도구를 준수함). 이 방법은 Voucherify에서 데이터를 가져오는 데 시간이 오래 걸릴 때 코드 게시 실패를 방지하는 데 도움이 됩니다.

{% raw %}`:retry`{% endraw %}를 사용하지 않는 경우, Voucherify에서 반환된 응답에 관계없이 Braze에서 배포를 시도하므로 게시된 코드가 없는 이메일이 생성될 수 있습니다.

![]({% image_buster /assets/img/voucherify/voucherify_cc_retry.png %})

{% endtab %}
{% tab 고유한 게시 %}

**고객당 고유한 게시**

스크립트 본문의 {% raw %}`source_id`{% endraw %} 매개변수는 각 고객이 단일 Braze 캠페인에서 하나의 고유 코드만 수신할 수 있도록 합니다. 그 결과, Braze가 의도치 않게 요청을 늘린다고 해도 각 사용자는 첫 번째 메시지에서 게시된 것과 동일한 고유 코드를 수신합니다.

![]({% image_buster /assets/img/voucherify/voucherify_cc_sourceId_unique_publication.png %})

다음 구성을 사용하여 {% raw %}`{{source_id}}`{% endraw %} 및 게시에 미치는 영향을 수정할 수 있습니다.

| 구성 | 효과 |
| ------------- | ------ |
| {% raw %}`{{campaign.${dispatch_id}}}`{% endraw %} | 단일 발송 내 고객은 동일한 게시를 사용합니다. |
| {% raw %}`{{campaign.${api_id}}}`{% endraw %} | 단일 캠페인 내 모든 고객은 동일한 게시를 사용합니다. |
| {% raw %}`{{${user_id}}}`{% endraw %} 또는 {% raw %}`{{${braze_id}}}`{% endraw %} | 어떤 캠페인이 전송되더라도 모든 고객이 동일한 게시를 사용하는지 확인합니다({% raw %}`${user_id}`{% endraw %}({% raw %}`external_id`{% endraw %}) 및 {% raw %}`${braze_id}`{% endraw %}(내부 ID)를 사용할 수 있음). |
| {% raw %}`{{campaign.${dispatch_id}}}`{% endraw %} 및 {% raw %}`{{campaign.${user_id}}}`{% endraw %} | 단일 발송 내 각 고객은 고유한 같은 게시를 사용합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab 한 번 가입 %}

**한 번 가입**

Voucherify 캠페인에 _고객이 한 번만 가입_할 수 있다는 제한이 있는 경우 스크립트 본문에서 게시 소스 ID를 제거합니다. Voucherify는 동일한 고객에게 보내는 각 Braze 메시지가 처음에 게시된 동일한 코드를 전달하는지 확인합니다.

![]({% image_buster /assets/img/voucherify/voucherify_cc_join_once.png %}){: style="max-width:50%;"}

커넥티드 콘텐츠 스크립트는 다음과 같아야 합니다:

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign cache_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}

{% connected_content
   https://api.voucherify.io/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
    "X-App-Id": "VOUCHERIFY-APP-ID",
    "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :body campaign={{voucherify_campaign_id}}&customer={{customer_id}}&channel=Braze
   :content_type application/json
   :cache_max_age
   :retry
   :save publication
 %}
```

{% endraw %}
{% endtab %}
{% endtabs %}

## 사용 사례

아래의 모든 사용 사례는 Voucherify 게시 소스 ID와 Braze 캐시 및 재시도 매개변수를 사용하여 Braze 캠페인에서 호출하는 API 호출을 제한합니다. 다음과 같은 결과에 유의해야 합니다.

- 하나의 Braze 캠페인에서 동일한 고객에게 서로 다른 코드를 게시하고 전송할 수는 없습니다.
- 바우처파이 캠페인에서 _한 번만 참여하기 기능을_ 사용하는 경우, 위의 한 번만 참여하기 탭에 설명된 대로 연결된 콘텐츠 본문에서 `source_id` 을 제거해야 합니다.

연결된 콘텐츠 스크립트 예제를 보려면 Voucherify [GitHub 리포지토리](https://github.com/voucherifyio/braze-connected-content)를 참조하세요.

### 고유 쿠폰 코드 게시 및 전송

이 사용 사례에서는 커넥티드 콘텐츠 스크립트가 Voucherify API를 호출하여 고유 쿠폰 코드를 게시하고 이를 Braze 메시지로 전송합니다. 각 Braze 사용자는 하나의 고유 코드만 받습니다.

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
{% assign cache_id = source_id %}

{% connected_content
   YOUR API ENDPOINT/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
        "X-App-Id": "VOUCHERIFY-APP-ID",
        "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :body campaign={{voucherify_campaign_id}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
   :content_type application/json
   :cache_max_age
   :retry
   :save publication
 %}
```

{% endraw %}

### 새로운 추천인 초대

고객이 추천 프로그램에 참여하도록 하려면 해당 고객에게 추천 코드를 할당해야 합니다. 연결된 콘텐츠는 앞의 예제와 동일합니다. 이 커넥티드 콘텐츠 스크립트를 사용하면 선택한 Braze 사용자에게 고유한 추천 코드를 게시하고 보낼 수 있습니다. 각 사용자는 하나의 추천 코드만 수신하여 다른 사용자와 공유하고 새로운 추천을 받습니다. 

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
{% assign cache_id = source_id %}

{% connected_content
   YOUR API ENDPOINT/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
        "X-App-Id": "VOUCHERIFY-APP-ID",
        "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :body campaign={{voucherify_campaign_id}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
   :content_type application/json
   :cache_max_age
   :retry
   :save publication
 %}
```

{% endraw %}

### 로열티 카드 잔액 가져오기

다음은 사용자 지정 속성으로 미리 Braze에 전송된 로열티 카드 코드를 기반으로 현재 로열티 잔액을 가져오는 커넥티드 콘텐츠 스크립트의 사용 사례입니다. 이 스크립트를 사용하기 전에 Braze 고객 프로필에 로열티 카드 코드를 커스텀 속성으로 저장해야 합니다.

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
{% assign cache_id = source_id %}

{% connected_content
   YOUR API ENDPOINT/v1/loyalties/members/{{custom_attribute.${loyalty.card}}}?cache_id={{cache_id}}
   :method get
   :headers {
        "X-App-Id": "VOUCHERIFY-APP-ID",
        "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :content_type application/json
   :cache_max_age
   :retry
   :save member
 %}
```

{% endraw %}

### 사용자 지정 코드 만들기

커넥티드 콘텐츠는 창의적인 시나리오를 도입할 수 있는 강력한 도구입니다. 고객의 프로필 정보를 기반으로 사용자 지정 쿠폰 코드를 생성할 수 있습니다.

다음은 고유 코드를 생성할 때 고객의 전화번호를 고려하는 코드 스니펫입니다. 이 사용 사례에서는 커넥티드 콘텐츠 스크립트가 Voucherify API를 호출하여 사용자 지정 쿠폰 코드를 게시합니다.

1.  먼저 필요한 모든 변수를 정의합니다. 그런 다음 접두사 "SummerTime-"로 시작하는 쿠폰 코드를 생성하고 나머지 코드는 고객의 전화번호가 됩니다. 쿠폰 코드의 기준이 될 사용자 지정 속성을 결정할 수 있습니다.  
    
    {% raw %}
    
    ```liquid
    {% assign braze_campaign_id = {{campaign.${dispatch_id}}} %}
    {% assign customer_id = {{${user_id}}} %}
    {% assign phoneNumber = {{${phone_number}}} %}
    {% assign source_id = braze_campaign_id | append: customer_id %}
    {% assign cache_id = source_id %}
    {% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
    {% assign prefix = "SummerTime-" %}
    ```
    
    {% endraw %}
    
2.  다음으로, 캠페인에서 단일 코드를 생성하도록 Voucherify에 요청합니다. URL에 생성할 쿠폰 코드의 이름을 입력합니다:  
    
    {% raw %}
    
    ```liquid
    {% connected_content
       YOUR-API-ENDPOINT/v1/campaigns/{{voucherify_campaign_id}}/vouchers/{{prefix}}{{phoneNumber}}?cache_id={{cache_id}}
       :method post
       :headers {
            "X-App-Id": "VOUCHERIFY-APP-ID",
            "X-App-Token": "VOUCHERIFY-APP-TOKEN"
       }
       :content_type application/json
       :cache_max_age 
       :save voucher_created
       :retry
    %}  
    ```  
    
    {% endraw %}  

3.  마지막으로 방금 만든 코드를 게시합니다. 코드 스니펫은 캠페인에서 무작위 바우처를 생성하는 데 사용한 것과 거의 동일합니다. 하지만 이번에는 특정 바우처 코드를 대상으로 합니다.  
    
    {% raw %}  
    
    ```liquid
    {% connected_content
       YOUR-API-ENDPOINT/v1/publications?cache_id={{cache_id}}
       :method post
       :headers {
           "X-App-Id": "VOUCHERIFY-APP-ID",
           "X-App-Token": "VOUCHERIFY-APP-TOKEN"
       }
       :body voucher={{prefix}}{{phoneNumber}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
       :content_type application/json
       :cache_max_age 
       :save publication
       :retry
    %}
    ```
    
    {% endraw %}

결과적으로 고객은 다음과 같은 이메일을 받게 됩니다:  

![]({% image_buster /assets/img/voucherify/voucherify_cc_custom_code_email.png %})

이 예제에서 사용된 전체 스니펫은 다음과 같습니다:

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${dispatch_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign phoneNumber = {{${phone_number}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign cache_id = source_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
{% assign prefix = "Your Prefix" %}

{% connected_content
   YOUR-API-ENDPOINT/v1/campaigns/{{voucherify_campaign_id}}/vouchers/{{prefix}}{{phoneNumber}}?cache_id={{cache_id}}
   :method post
   :headers {
        "X-App-Id": "VOUCHERIFY-APP-ID",
        "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :content_type application/json
   :cache_max_age 
   :save voucher_created
   :retry
%} 

{% connected_content
   YOUR-API-ENDPOINT/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
       "X-App-Id": "VOUCHERIFY-APP-ID",
       "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :body voucher={{prefix}}{{phoneNumber}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
   :content_type application/json
   :cache_max_age 
   :save publication
   :retry
%}
```

{% endraw %}

## Braze 메시지에서 가져온 데이터 표시

연결된 콘텐츠 스크립트를 사용하려는 Braze 캠페인이나 캔버스가 이미 있다고 가정합니다.

### 1단계: 메시지 템플릿에 연결된 콘텐츠 스크립트 추가

1.  메시지 HTML 템플릿의 {% raw %}`<body>`{% endraw %} 태그 아래에 연결된 콘텐츠 스크립트를 복사하여 붙여넣습니다. **CAMPAIGN_ID**를 Voucherify 캠페인 대시보드의 URL 주소에서 복사한 Voucherify {% raw %}`campaign_id`{% endraw %}로 바꿉니다.<br>![]({% image_buster /assets/img/voucherify/voucherify_cc_campaignId.png %}){: style="margin-top:15px;margin-bottom:15px;"}
    {% raw %}  
    ```
    assign voucherify_campaign_id = "camp_Y7h1meBSyybsNs7UpSVVZZce"
    ```
    {% endraw %}

2. Voucherify API 엔드포인트를 제공하세요. API 엔드포인트가 무엇인지 모르는 경우 **프로젝트 설정** > **일반** > **API 엔드포인트에서** 확인할 수 있습니다.<br>
    {% raw %}
    ```
    YOUR API ENDPOINT/v1/publications?cache_id={{cache_id}}
    ```
    {% endraw %}
    
    | 공유 클러스터   | Braze 연결된 콘텐츠용 엔드포인트          |
    | ---------------- | --------------------------------------------- |
    | 유럽(기본값) | https://api.voucherify.io/v1/publications     |
    | 미국    | https://us1.api.voucherify.io/v1/publications |
    | 아시아(싱가포르) | https://as1.api.voucherify.io/v1/publications |
    {: .reset-td-br-1 .reset-td-br-2 role="presentation" }
    
3.  인증을 위해 API 키를 추가합니다. **프로젝트 설정 > 일반 > 애플리케이션 키**에서 `Voucherify-App-Id` 및 `Voucherify-App-Token`을 찾을 수 있습니다.<br>![]({% image_buster /assets/img/voucherify/voucherify_cc_app_keys.png %}){: style="margin-top:15px;margin-bottom:15px;"}
    {% raw %}
    ```
    "X-App-Id": "VOUCHERIFY-APP-ID",
    "X-App-Token": "VOUCHERIFY-APP-TOKEN"
    ```
    {% endraw %}
    
이제 연결된 콘텐츠 스크립트를 사용할 준비가 되었습니다.

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "camp_Y7h1meBSyybsNs7UpSVVZZce" %}
{% assign cache_id = source_id %}

{% connected_content
   https://api.voucherify.io/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
        "X-App-Id": "490a3fb6-a",
        "X-App-Token": "328099d5-a"
   }
   :body campaign={{voucherify_campaign_id}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
   :content_type application/json
   :cache_max_age
   :retry
   :save publication
 %}
```

{% endraw %}

### 2단계: 가져온 데이터를 표시하는 코드조각을 만듭니다.

Voucherify API의 응답은 연결된 콘텐츠에 의해 {% raw %}`:save`{% endraw %} 매개변수 값 아래에 저장됩니다. 예를 들어, 다음과 같습니다.

{% raw %}

```liquid
:save member
```
{% endraw %}

이를 통해 Braze 메시지에서 Voucherify 응답의 데이터를 검색하고 표시할 수 있습니다.

게시된 코드, 로열티 카드 잔액, 만료일, 기타 매개변수를 표시하는 스니펫을 생성하여 Voucherify API의 JSON 형식 응답에 포함시킬 수 있습니다.

예를 들어 게시된 코드를 메시지 템플릿에 표시하려면 바우처 개체에서 고유 코드를 가져오는 스니펫을 만들어야 합니다.

연결된 콘텐츠 스크립트:

![연결된 콘텐츠 호출이 끝날 때 Voucherify 응답을 저장하는 연결된 콘텐츠 스크립트 표시]({% image_buster /assets/img/voucherify/voucherify_cc_save_parameter.png %})

Braze 메시지 템플릿의 스니펫:

{% raw %}

```liquid
{{publication.voucher.code}}
```

{% endraw %}

결과적으로 각 고객은 프로필에 자동으로 할당된 고유 코드가 포함된 메시지를 받게 됩니다. 사용자가 코드를 수신할 때마다 Voucherify의 프로필에 코드가 게시됩니다.

Voucherify API에서 가져온 로열티 카드 잔액을 표시하려면 다음 스니펫을 생성해야 합니다.

{% raw %}

```liquid
{{member.loyalty_card.balance}}
```

{% endraw %}

여기서 구성원은 연결된 콘텐츠 스크립트에서 {% raw %}`:save`{% endraw %} 매개변수 값입니다.

{% raw %}

```liquid
:save member
```

{% endraw %}

'미리보기 모드'에 전적으로 의존하지 말고 모든 것이 정상적으로 작동하는지 확인하기 위해 몇 가지 테스트 메시지를 보내는 것이 좋습니다.

### 3단계: 사용량 제한 도구 설정

캠페인 목표를 설정할 때 고급 설정을 사용하여 분당 전송되는 메시지 수를 제합니다.

![]({% image_buster /assets/img/voucherify/voucherify_cc_limiter.png %})

사용량 제한 도구 및 최대 게재빈도 설정에 대한 자세한 내용은 Braze [설명서]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting)를 참조하세요.

