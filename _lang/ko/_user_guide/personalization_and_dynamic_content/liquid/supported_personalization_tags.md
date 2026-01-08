---
nav_title: 지원되는 개인화 태그
article_title: 지원되는 Liquid 개인화 태그
page_order: 1
description: "이 참고 문서에서는 지원되는 Liquid 개인화 태그의 전체 목록을 다룹니다."
search_rank: 1
---

# 지원되는 개인화 태그

> 이 참고 문서에서는 지원되는 Liquid 개인화 태그의 전체 목록을 다룹니다.

## 지원되는 태그 요약

편의를 위해 지원되는 개인화 태그의 요약이 제공됩니다. 각 태그 유형과 모범 사례에 대한 자세한 내용은 계속 읽어보세요.

{% raw %}

| 개인화 태그 유형 | 태그 |
| -------------  | ---- |
| 표준(기본) 속성 | `{{${city}}}` <br> `{{${country}}}` <br> `{{${date_of_birth}}}` <br> `{{${email_address}}}` <br> `{{${first_name}}}` <br> `{{${gender}}}` <br> `{{${language}}}` <br> `{{${last_name}}}` <br> `{{${last_used_app_date}}}` <br> `{{${most_recent_app_version}}}` <br> `{{${most_recent_locale}}}` <br> `{{${most_recent_location}}}` <br> `{{${phone_number}}}` <br> `{{${time_zone}}}` <br> `{{${user_id}}}` <br> `{{${braze_id}}}` <br> `{{${random_bucket_number}}}` <br> `{{subscribed_state.${email_global}}}` <br> `{{subscribed_state.${subscription_group_id}}}` |
| 기기 속성 | `{{most_recently_used_device.${carrier}}}` <br> `{{most_recently_used_device.${id}}}` <br> `{{most_recently_used_device.${idfa}}}` <br> `{{most_recently_used_device.${model}}}` <br> `{{most_recently_used_device.${os}}}` <br> `{{most_recently_used_device.${platform}}}` <br> `{{most_recently_used_device.${google_ad_id}}}` <br> `{{most_recently_used_device.${roku_ad_id}}}` <br> `{{most_recently_used_device.${foreground_push_enabled}}}`|
| <a href='/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions'>이메일 목록 속성</a> | `{{${set_user_to_unsubscribed_url}}}` <br>이 태그는 이전 `{{${unsubscribe_url}}}` 태그를 대체합니다. 이전 태그는 이전에 작성한 이메일에서 계속 작동하지만, 대신 최신 태그를 사용하는 것이 좋습니다. <br><br> `{{${set_user_to_subscribed_url}}}` <br> `{{${set_user_to_opted_in_url}}}`|
| <a href='/docs/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/#trigger-messages'>SMS 속성</a> | `{{sms.${inbound_message_body}}}` <br> `{{sms.${inbound_media_urls}}}` |
| <a href='/docs/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages/'>WhatsApp 속성</a> | `{{whats_app.${inbound_message_body}}}` <br> `{{whats_app.${inbound_media_urls}}}` |
| 캠페인 속성 | `{{campaign.${api_id}}}` <br> `{{campaign.${dispatch_id}}}` <br> `{{campaign.${name}}}` <br> `{{campaign.${message_name}}}` <br> `{{campaign.${message_api_id}}}` |
| 캔버스 속성 | `{{canvas.${name}}}` <br> `{{canvas.${api_id}}}` <br> `{{canvas.${variant_name}}}` <br> `{{canvas.${variant_api_id}}}` |
| 캔버스 단계 속성 | `{{campaign.${api_id}}}` <br> `{{campaign.${dispatch_id}}}` <br> `{{campaign.${name}}}` <br> `{{campaign.${message_name}}}` <br> `{{campaign.${message_api_id}}}` |
| 카드 속성 | `{{card.${api_id}}}` <br> `{{card.${name}}}` |
| 지오펜싱 이벤트 | `{{event_properties.${geofence_name}}}` <br> `{{event_properties.${geofence_set_name}}}` |
| 이벤트 속성정보 <br> (이는 작업 공간에 맞게 커스텀됩니다.)| `{{event_properties.${your_custom_event_property}}}` |
| 캔버스 컨텍스트 변수 | `{{context}}` |
| 커스텀 속성 <br> (이는 작업 공간에 맞게 커스텀됩니다.) | `{{custom_attribute.${your_custom_attribute}}}` |
| <a href='/docs/api/objects_filters/trigger_properties_object/'>API 트리거 속성</a> |`{{api_trigger_properties}}` |
| 캔버스 항목 속성 | `{{canvas_entry_properties.${property_name}}}` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}

### 지원되는 속성

캠페인, 카드 및 캔버스 속성은 해당 메시징 템플릿에서만 지원됩니다(예: `dispatch_id` 는 인앱 메시지 캠페인에서 사용할 수 없음).

이 도움말 문서를 참조하여 [Braze에서 이러한 속성의 일부가 소스마다 어떻게 다른지]({{site.baseurl}}/help/help_articles/api/attribute_name_id_across_sources/) 자세히 알아보세요.

### 캔버스와 캠페인 태그의 차이점 

다음 태그의 동작은 캔버스와 캠페인 간에 다릅니다:
{% raw %}
- `dispatch_id` 동작은 캔버스 단계가 "예약된" 경우에도 트리거된 이벤트로 취급하기 때문에 다릅니다(예약 가능한 진입 단계는 제외). 자세히 알아보려면 [Dispatch ID 동작을]({{site.baseurl}}/help/help_articles/data/dispatch_id/) 참조하세요.
- `{{campaign.${name}}}` 태그를 캔버스와 함께 사용하면 캔버스 컴포넌트 이름이 표시됩니다. 이 태그를 캠페인에 사용하면 캠페인 이름이 표시됩니다.
{% endraw %}

## 가장 최근에 사용한 기기 정보

모든 플랫폼에서 사용자의 가장 최근 기기에 대해 다음 속성을 템플릿으로 만들 수 있습니다. 사용자가 애플리케이션을 사용하지 않은 경우(예: REST API를 통해 사용자를 가져오기) 이 값은 모두 `null` 입니다.

{% raw %}

|태그 | 설명 |
|---|---|
|`{{most_recently_used_device.${browser}}}` | 사용자 기기에서 가장 최근에 사용한 브라우저입니다. 예를 들어 'Chrome'과 'Safari'가 있습니다. |
|`{{most_recently_used_device.${id}}}` | Braze 기기 식별자입니다. iOS에서는 IDFV(Apple 식별자 for Vendor) 또는 UUID일 수 있습니다. Android 및 기타 플랫폼의 경우 무작위로 생성된 UUID입니다. |
| `{{most_recently_used_device.${carrier}}}` | 가장 최근에 사용한 기기의 전화 서비스 통신사(가능한 경우). 예를 들면 "Verizon" 및 "Orange" 등이 있습니다. |
| `{{most_recently_used_device.${ad_tracking_enabled}}}` | 기기에 광고 추적이 인에이블먼트되어 있는지 여부. 부울 값입니다 (`true` 또는 `false`). |
| `{{most_recently_used_device.${idfa}}}` | iOS 기기의 경우, 애플리케이션이 [선택 사항인 IDFA 컬렉션으로]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/) 구성된 경우 이 값은 광고 식별자(IDFA)가 됩니다. iOS가 아닌 기기의 경우 이 값은 null이 됩니다. |
| `{{most_recently_used_device.${google_ad_id}}}` | Android 기기의 경우, 애플리케이션이 선택 사항인 Google Play 광고 ID 수집으로 구성된 경우 이 값은 Google Play 광고 식별자가 됩니다. Android 이외의 기기의 경우 이 값은 null이 됩니다. |
| `{{most_recently_used_device.${roku_ad_id}}}` | Roku 기기의 경우, 이 값은 애플리케이션이 Braze로 구성될 때 수집되는 Roku 광고 식별자가 됩니다. Roku가 아닌 기기의 경우 이 값은 null이 됩니다. |
| `{{most_recently_used_device.${model}}}` | 기기의 모델명(사용 가능한 경우). 예를 들어 'iPhone 6S' 및 'Nexus 6P', 'Firefox'가 있습니다. |
| `{{most_recently_used_device.${os}}}` | 기기의 운영 체제(사용 가능한 경우). 예를 들어 "iOS 9.2.1" 및 "Android(롤리팝)", "Windows" 등이 있습니다. |
| `{{most_recently_used_device.${platform}}}` | 기기의 플랫폼(사용 가능한 경우). 설정된 경우 값은 `ios`, `android`, `kindle`, `android_china`, `web` 또는 `tvos` 중 하나가 됩니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

기기 통신사, 모델명, 운영 체제가 매우 다양하기 때문에 이러한 값에 조건부로 의존하는 모든 Liquid를 철저히 테스트하는 것이 좋습니다. 이 값은 특정 기기에서 사용할 수 없는 경우 `null` 입니다.

## 타겟팅 앱 정보

인앱 메시징의 경우 Liquid 내에서 다음 앱 속성을 사용할 수 있습니다. 이 값은 앱이 메시징을 요청하는 데 사용하는 소프트웨어 개발 키트 API 키를 기반으로 합니다.

|태그 | 설명 |
|------------------|---|
| `{{app.${api_id}}}` | 메시지를 요청하는 앱의 API 키입니다. 예를 들어, 이 키를 `abort_message()` Liquid와 함께 사용하면 별도의 소프트웨어 개발 키트 API 키를 사용하는 TV 플랫폼 또는 개발 빌드와 같은 특정 앱에 인앱 메시지를 보내지 않도록 할 수 있습니다.|
| `{{app.${name}}}` | 메시지를 요청하는 앱의 이름(Braze 대시보드에 정의된 대로)입니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

예를 들어, 이 Liquid 코드는 요청하는 앱이 목록에 있는 두 API 키 중 하나가 아닌 경우 메시지를 중단합니다:

```liquid
{% assign allowed_api_keys = 'sdk_api_key_1,sdk_api_key_2' | split: ',' %}
{% if allowed_api_keys contains {{app.${api_id}}} %}
User is in list of apps
{% else %}
{% abort_message("User not in list of apps") %}
{% endif %}
```

## 타겟팅 기기 정보

푸시 알림 및 인앱 메시지 채널의 경우 메시지가 전송되는 기기에 대해 다음 속성을 템플릿으로 만들 수 있습니다. 즉, 푸시 알림 또는 인앱 메시지에는 메시지를 읽고 있는 기기의 기기 속성이 포함될 수 있습니다. 콘텐츠 카드에는 이러한 속성이 작동하지 않습니다. 

|태그 | 설명 |
|------------------|---|
| `{{targeted_device.${id}}}` | 이것은 Braze 기기 식별자입니다. iOS에서는 IDFV(Apple 식별자 for Vendor) 또는 UUID일 수 있습니다. Android 및 기타 플랫폼의 경우 무작위로 생성된 UUID입니다. 예를 들어, 사용자에게 5대의 기기가 있는 경우 각각 해당 기기 식별자를 사용하여 5대의 기기 모두에 대해 전송 시도가 발생합니다. 메시징이 사용자가 가장 최근에 사용한 기기로 전송되도록 구성된 경우, Braze를 통해 식별된 가장 최근에 사용한 기기로 한 번만 전송 시도가 이루어집니다. |
| `{{targeted_device.${carrier}}}` | 가장 최근에 사용한 기기의 전화 서비스 통신사(가능한 경우). 예를 들면 "Verizon" 및 "Orange" 등이 있습니다. |
| `{{targeted_device.${idfa}}}` | iOS 기기의 경우, 애플리케이션이 [선택 사항인 IDFA 컬렉션으로]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/) 구성된 경우 이 값은 광고 식별자(IDFA)가 됩니다. iOS가 아닌 기기의 경우 이 값은 null이 됩니다. |
| `{{targeted_device.${google_ad_id}}}` | Android 기기의 경우, 애플리케이션이 [선택 사항인 Google Play 광고 ID 수집]으로 구성된 경우 이 값은 Google Play 광고 식별자가 됩니다. Android 이외의 기기의 경우 이 값은 null이 됩니다. |
| `{{targeted_device.${roku_ad_id}}}` | Roku 기기의 경우, 이 값은 애플리케이션이 Braze로 구성될 때 수집되는 Roku 광고 식별자가 됩니다. Roku가 아닌 기기의 경우 이 값은 null이 됩니다. |
| `{{targeted_device.${model}}}` | 기기의 모델명(사용 가능한 경우). 예를 들어 'iPhone 6S' 및 'Nexus 6P', 'Firefox'가 있습니다. |
| `{{targeted_device.${os}}}` | 기기의 운영 체제(사용 가능한 경우). 예를 들어 "iOS 9.2.1" 및 "Android(롤리팝)", "Windows" 등이 있습니다. |
| `{{targeted_device.${platform}}}` | 기기의 플랫폼(사용 가능한 경우). 설정된 경우 값은 `ios`, `android`, `kindle`, `android_china`, `web` 또는 `tvos` 중 하나가 됩니다. `most_recently_used_device` 개인화 태그를 사용할 수도 있습니다. |
| `{{targeted_device.${foreground_push_enabled}}}` | 이 값은 타겟팅된 기기가 포그라운드 푸시에 인에이블먼트된 경우 `true`, 그렇지 않은 경우 `false` 입니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}

기기 통신사, 모델명, 운영 체제가 매우 다양하므로 이러한 값에 조건부로 의존하는 로직을 철저히 테스트하는 것이 좋습니다. 이 값은 특정 기기에서 사용할 수 없는 경우 `null` 입니다. 

또한 푸시 알림의 경우 API를 통해 푸시 토큰을 가져온 경우와 같이 특정 상황에서 Braze가 푸시 알림에 연결된 기기를 식별하지 못해 해당 메시지에 대한 값이 `null` 가 될 수 있습니다.

푸시 메시지에서 이름 변수를 사용할 때 기본값 "there"를 사용하는 예시입니다.]({% image_buster /assets/img_archive/personalized_firstname_.png %})

### 기본값 대신 조건 로직 사용

경우에 따라 기본값을 설정하는 대신 [조건 로직을]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/) 사용하도록 선택할 수 있습니다. 조건 로직을 사용하면 커스텀 속성의 값에 따라 다른 메시지를 보낼 수 있습니다. 또한 조건 로직을 사용하여 속성 값이 0이거나 공백인 고객에 대한 [메시지를 중단할]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/) 수 있습니다. 

#### 사용 사례

예를 들어 고객에게 리워드 잔액 알림을 보낸다고 가정해 보겠습니다. 기본값을 사용하여 잔액이 낮거나 0인 고객을 설명할 수 있는 좋은 방법은 없습니다.

이 경우 기본값을 설정하는 것보다 두 가지 옵션이 더 효과적일 수 있습니다:

1. 잔액이 낮거나, 0이거나, 비어 있는 고객에게는 메시지를 중단합니다.

{% raw %}

   ```liquid
   {% if {{custom_attribute.${balance}}} > 0 %}
   Your rewards balance is {{custom_attribute.${balance}}}
   {% else %}
   {% abort_message() %}
   {% endif %}
   ```

{% endraw %}

2. 이러한 고객에게 다음과 같이 완전히 다른 메시지를 보내세요:

{% raw %}

   ```liquid
   {% if ${first_name} != blank and ${first_name} != null %}
   Hello {{${first_name} | default: 'there'}}, thanks for downloading!
   {% else %}
   Thanks for downloading!
   {% endif %}
   ```

이 사용 사례에서 이름이 공백이거나 0인 사용자에게는 "다운로드해 주셔서 감사합니다"라는 메시지가 표시됩니다. 이름에 대한 [기본값을]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/setting_default_values/) 포함해야 실수로 고객이 Liquid를 보지 않도록 할 수 있습니다.

{% endraw %}

## 변수 태그

`assign` 태그를 사용하여 메시지 작성기에서 변수를 만들 수 있습니다. 변수에 고유한 이름을 사용하는 것이 좋습니다. 지원되는 개인화 태그와 유사한 이름의 변수(예: `language`)를 만들면 메시징 로직에 영향을 미칠 수 있습니다.

변수를 만든 후에는 메시징 로직이나 메시지에서 해당 변수를 참조할 수 있습니다. 이 태그는 [연결된 콘텐츠]({% image_buster /assets/img_archive/personalized_firstname_.png %}) ] 기능에서 반환된 콘텐츠의 형식을 다시 지정할 때 유용하게 사용할 수 있습니다. 자세한 내용은 Shopify의 [가변 태그에](https://docs.shopify.com/themes/liquid/tags/variable-tags) 대한 설명서를 참조하십시오.

{% alert tip %}
모든 메시징에 동일한 변수를 할당하고 계신가요? `assign` 태그를 반복해서 작성하는 대신 해당 태그를 콘텐츠 블록으로 저장하여 메시지 상단에 넣을 수 있습니다.

1. [콘텐츠 블록을 만듭니다]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#create-a-content-block).
2. 콘텐츠 블록에 이름을 지정합니다(공백이나 특수 문자 제외).
3. 페이지 하단에서 **편집을** 선택합니다.
4. `assign` 태그를 입력합니다.

콘텐츠 블록이 메시지 상단에 있는 한, 변수가 메시징에 오브젝트로 삽입될 때마다 선택한 커스텀 속성을 참조합니다!
{% endalert %}

### 사용 사례

고객이 리워드 포인트 100점을 적립한 후 리워드 포인트를 현금화하여 경품으로 받을 수 있도록 허용한다고 가정해 보겠습니다. 따라서 추가 구매 시 포인트 잔액이 100보다 크거나 같은 고객에게만 메시징을 보낼 수 있습니다:

{% raw %}
```liquid
{% assign new_points_balance = {{custom_attribute.${current_rewards_balance} | plus: 50}} %}
{% if new_points_balance >= 100 %}
Make a purchase to bring your rewards points to {{new_points_balance}} and cash in today!
{% else %}
{% abort_message('not enough points') %}
{% endif %}
```
{% endraw %}

## Iteration 태그

{% raw %}
Iteration 태그를 사용하여 코드 블록을 반복적으로 실행할 수 있습니다. 아래 사용 사례는 `for` 태그를 기능합니다.

### 사용 사례

나이키 운동화 세일을 진행 중이고 나이키에 관심을 표명한 고객에게 메시지를 보내고 싶다고 가정해 보겠습니다. 각 고객의 프로필에서 다양한 제품 브랜드를 볼 수 있습니다. 이 배열에는 최대 25개의 제품 브랜드가 포함될 수 있지만, 가장 최근에 본 5개의 제품 중 하나로 Nike 제품을 본 고객에게만 메시징을 보내려고 합니다.

```liquid
{% for items in {{custom_attribute.${Brands Viewed}}} limit:5 %}
{% if {{items}} contains 'Converse' %}
{% assign converse_viewer = true %}
{% endif %}
{% endfor %}
{% if converse_viewer == true %}
Sale on Converse!
{% else %}
{% abort_message() %}
{% endif %}
```

이 사용 사례에서는 스니커즈 브랜드 조회 배열의 처음 5개 항목을 확인합니다. 이러한 항목 중 하나가 대화인 경우 `converse_viewer` 변수를 생성하고 true로 설정합니다.

그런 다음 `converse_viewer` 이 참이면 세일 메시지를 보냅니다. 그렇지 않으면 메시징을 중단합니다.

다음은 Braze 메시지 작성기에서 반복 태그를 사용하는 간단한 예시입니다. 자세한 내용은 Shopify의 [반복 태그에](https://docs.shopify.com/themes/liquid/tags/iteration-tags) 대한 설명서를 참조하십시오.

## 구문 태그

구문 태그를 사용하여 Liquid가 렌더링되는 방식을 제어할 수 있습니다. `echo` 태그를 사용하여 표현식을 반환할 수 있습니다. 중괄호를 사용하여 표현식을 래핑하는 것과 동일하지만 이 태그를 Liquid 태그 내에서 사용할 수 있다는 점이 다릅니다. `liquid` 태그를 사용하여 각 태그에 구분 기호 없이 Liquid 블록을 만들 수도 있습니다. `liquid` 태그를 사용할 때 각 태그는 고유한 줄에 있어야 합니다. 자세한 내용과 예제는 [구문 태그에](https://shopify.dev/api/liquid/tags#syntax-tags) 대한 Shopify 설명서를 확인하십시오.

[공백 제어](https://shopify.github.io/liquid/basics/whitespace/) 기능을 사용하면 태그 주변의 공백을 제거하여 Liquid 출력물의 모양을 더욱 세밀하게 제어할 수 있습니다.

## HTTP 상태 코드 {#http-personalization}

먼저 로컬 변수로 저장한 다음 `__http_status_code__` 키를 사용하여 [연결된 콘텐츠]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) 호출의 HTTP 상태를 활용할 수 있습니다. 예를 들어

```html
{% connected_content https://example.com/api/endpoint :save connected %}
{% if connected.__http_status_code__ != 200 %}
{% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert note %}
이 키는 엔드포인트가 JSON 객체를 반환하는 경우에만 연결된 콘텐츠 객체에 자동으로 추가됩니다. 엔드포인트가 배열이나 다른 유형을 반환하는 경우 해당 키는 응답에서 자동으로 설정할 수 없습니다.
{% endalert %}

## 언어, 가장 최근 로캘 및 시간대를 기준으로 메시지 보내기

경우에 따라 특정 로케일에 맞는 메시지를 보내야 할 수도 있습니다. 예를 들어 브라질 포르투갈어는 일반적으로 유럽식 포르투갈어와 다릅니다.

### 사용 사례: 최근 로캘에 기반한 현지화

다음은 최신 로캘을 사용하여 국제화된 메시지를 더욱 현지화하는 방법에 대한 사용 사례입니다.

{% raw %}

```liquid
{% if ${language} == 'en' %}
Message in English
{% elsif  ${language} == 'fr' %}
Message in French
{% elsif  ${language} == 'ja' %}
Message in Japanese
{% elsif  ${language} == 'ko' %}
Message in Korean
{% elsif  ${language} == 'ru' %}
Message in Russian
{% elsif ${most_recent_locale} == 'pt_BR' %}
Message in Brazilian Portuguese
{% elsif ${most_recent_locale} == 'pt_PT' %}
Message in European Portuguese
{% elsif  ${language} == 'pt' %}
Message in default Portuguese
{% else %}
Message in default language
{% endif %}
```

이 사용 사례에서 가장 최근 로캘이 `pt_BR` 인 고객은 브라질 포르투갈어로 메시지를 받고, 가장 최근 로캘이 `pt_PT` 인 고객은 유럽 포르투갈어로 메시지를 받게 됩니다. 앞의 두 조건을 충족하지 않지만 언어를 포르투갈어로 설정한 고객에게는 기본값으로 설정한 포르투갈어 유형으로 메시징이 전송됩니다.

### 사용 사례: 시간대별 사용자 타겟팅

시간대별로 사용자를 타겟팅할 수도 있습니다. 예를 들어, 상대방의 기준이 동부 표준시인 경우 한 메시지를 보내고 동부 표준시인 경우 다른 메시지를 보내세요. 이렇게 하려면 현재 시간을 UTC로 저장하고 if/else 문과 사용자의 현재 시간을 비교하여 올바른 시간대에 맞는 메시지를 보내세요. 사용자에게 적절한 시간에 캠페인을 제공하려면 사용자의 현지 시간대로 캠페인을 전송하도록 설정해야 합니다. 

오후 2시에서 오후 3시 사이에 발송할 메시지를 작성하는 방법과 각 시간대에 대한 특정 메시지를 포함하는 사용 사례는 다음 사용 사례를 참조하세요.

```liquid
{% assign hour_in_utc = 'now' | date: '%H' | plus:0 %}
{% if hour_in_utc >= 19 && hour_in_utc < 20 %}
It is between 2:00:00 pm and 2:59:59 pm ET!
{% elsif hour_in_utc >= 22 && hour_in_utc < 23 %}
It is between 2:00:00 pm and 2:59:59 pm PT!
{% else %}
{% abort_message %}
{% endif %}
```

{% endraw %}

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
