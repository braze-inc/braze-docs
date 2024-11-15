---
nav_title: 다중 스토어 지원
permalink: "/shopify_multiple_store/"
hidden: true
---

# Shopify 다중 스토어 지원

> 여러 스토어를 하나의 작업 공간에 연결하여 모든 시장에서 고객을 전체적으로 파악할 수 있는 새로운 다중 스토어 지원 베타 기능을 통해 여러 Shopify 스토어를 하나의 작업 공간에 연결하세요. 빌드 및 실행 자동화 프로그램 및 여정을 단일 워크스페이스에서 여러 인스턴스에 걸쳐 노력을 중복하지 않고 수행합니다. 

{% alert important %}
여러 Shopify 스토어에 대한 지원이 베타 버전으로 제공되며, 버그가 포함될 수 있습니다. 이 기능은 개발이 계속됨에 따라 변경될 수 있습니다.
{% endalert %}

## 전제 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| 각 상점에 대해 [이메일 구독 그룹]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#create-a-group)을 만드십시오 | 이메일 구독 그룹이 생성된 후 설정 흐름의 “[이메일 또는 SMS 구독자 수집]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/#step-5-collect-email-or-sms-subscribers)” 단계에서 특정 스토어에 지정하게 됩니다.<br><br>이를 통해 사용자가 준수 목적으로 어떤 상점의 이메일 구독 그룹에 속하는지 추적할 수 있습니다. |
| Shopify 속성을 사용하여 세그먼트, 캠페인 및 캔버스를 감사하고 업데이트하십시오 | 여러 상점에서 수집된 커스텀 속성은 중첩된 객체 형식으로 제공되며, 이는 문자열 값으로 형식화된 전체 Shopify 통합에서 사용되는 현재 구조와 다릅니다. 결과적으로 여러 스토어를 연결하여 “중첩 커스텀 속성” 필터를 사용하거나 “커스텀 속성 변경” 트리거 이벤트를 업데이트한 후 모든 세그먼트, 캠페인 또는 캔버스를 새 형식으로 업데이트해야 합니다.<br><br>오늘 속성을 사용하지 않는다면 무시해도 됩니다. |
| Shopify 별칭 감사 및 업데이트 | `shopify_customer_id` 별칭은 하나 이상의 스토어를 연결한 후에 {% raw %}`shopify_customer_id_{{storename}}`{% endraw %}에 마이그레이션됩니다. 내부 시스템이 새 별칭을 사용하도록 업데이트하고 있는지 확인하세요. 레거시 별칭 `shopify_customer_id`는 사용 중단될 예정입니다. 오늘 별명을 사용하지 않는다면 무시해도 됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 통합
Braze의 다중 스토어 지원을 통해 다음을 수행할 수 있습니다:
- 스토어에서 고객을 360°로 파악하기
- 스토어 데이터 집계로 고객의 세그먼트 생성하기 
- 고객이 다른 스토어로 이동할 때 메시징 또는 여정 설정하기
- 다양한 상점에서 이메일 및 SMS 구독을 관리합니다

{% alert important %}
단일 작업 공간에서 여러 브랜드를 지원하면 사용자가 여러 브랜드에서 쇼핑할 수 있으므로 사용자 프로필이 중복될 가능성이 높아집니다. 각 브랜드를 각자의 작업 공간에 배치하는 것이 좋습니다.
{% endalert %}

### 추가 스토어 설정
1. 첫 번째 스토어를 설치한 후 **\+ 새 스토어 연결** 옵션을 선택합니다.<br>![][1]{: style="max-width:70%;"}<br><br>
2. 이 새 스토어에 대한 온보딩 흐름을 살펴봅니다. 자세한 내용은 [Shopify 설정]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/) 가이드에서 확인할 수 있습니다.<br><br>이전 스토어의 설정이 전달될 수 있지만, 온보딩을 진행하면서 설정을 업데이트할 수 있습니다.<br><br>
3. 수집 이메일 또는 SMS 구독자 단계의 경우:
- 각 상점의 이메일 및 SMS 구독을 적절하게 수집하려면 각 상점 설정에 고유한 구독 그룹을 할당해야 합니다. 
- Braze에서는 “사용자에 대한 기존 글로벌 상태 재정의”를 활성화하지 **말 것을** 권장합니다. 이는 고객이 여러 스토어과 상호작용한 경우 글로벌하게 탈퇴시킬 수 있기 때문입니다.<br><br>
4. 필요한 대로 스토어에 대해 이 설치를 반복하세요.<br><br>
5. 각 스토어의 통합을 확인하고 고급 설정을 구성하려면 드롭다운 메뉴에서 스토어를 클릭합니다:<br>![][2]{: style="max-width:70%;"}

## Shopify 데이터

### Shopify 별칭

{% raw %}하나 이상의 스토어를 연결하면 모든 Shopify 사용자는 기존 별칭 `shopify_customer_id`에 추가하여 새 별칭 `shopify_customer_id_{{storename}}`을(를) 갖게 됩니다. `shopify_customer_id`는 레거시 별칭이며 이 기능이 일반적으로 사용 가능해지면 사용 중단될 예정입니다. 앞으로는 새로운 별칭을 사용하도록 전환해야 합니다. {% endraw %}

### Shopify 커스텀 속성

둘 이상의 상점을 연결한 후에는 다음 속성이 상점별 값과 집계 값을 포함하는 중첩된 객체로 동기화됩니다:
- `shopify_tags`
- `shopify_order_count`(과거 백필을 통해서만 이용 가능)
- `shopify_total_spent`(과거 백필을 통해서만 이용 가능)

세그먼트를 생성하거나 편집할 때 커스텀 이벤트를 사용하려면 **중첩 고객 속성** 필터를 선택하고 중첩 속성을 찾으십시오. 특정 경로 또는 개체의 필드를 식별하는 데 도움이 필요하면 [스키마 생성]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support#generate-schema) 도구를 사용하십시오. 중첩된 속성을 선택하면 선택한 속성 옆에 더하기 버튼이 있는 필드가 나타나 경로를 지정할 수 있습니다. 자세한 내용은 [중첩 커스텀 속성]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/)을 참조하세요.

![3]{:style="max-width:70%;"}

필드를 입력하거나 더하기 버튼을 클릭하고 경로를 선택하여 경로를 지정할 수 있습니다.

![4]{:style="max-width:70%;"}

### Shopify 커스텀 이벤트

하나 이상의 스토어를 연결한 후에는 들어오는 Shopify 커스텀 이벤트에 새로운 이벤트 속성정보 `shopify_storefront`이(가) 포함됩니다. 이 통합에서 지원되는 모든 커스텀 이벤트를 보려면 [Shopify 데이터 처리]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_data_processing#supported-shopify-events)를 참조하세요. 이 이벤트 속성정보는 이벤트가 발생하는 Shopify 스토어 도메인을 제공합니다.

### 실행 기반 전달 또는 전환 추적 기술

특정 스토어에서 작업을 완료하는 사용자에게 메시징을 트리거하려면

1. 캠페인의 **전달 일정** 단계로 이동합니다.
2. **커스텀 이벤트 수행**을 트리거 이벤트로 선택합니다.
![5]{:style="max-width:70%;"}
3. 트리거 이벤트로 Shopify 이벤트를 선택하고, **shopify_created_order** 및 **속성 필터 추가** 체크박스를 선택합니다.
![6]{:style="max-width:70%;"}
4. **기본 속성**을(를) **필터 추가** 드롭다운에서 선택합니다.
5. **shopify_storefront**을 선택하고 상점의 전체 Shopify 도메인을 입력하세요.
![7]{:style="max-width:70%;"}


### Shopify 사용자 병합 및 동기화

사용자의 Shopify 고객 ID, 이메일 주소 또는 전화번호가 별칭 {% raw %}`shopify_customer_id_{{storefront_domain}}`, `shopify_email` 또는 `shopify_phone`, {% endraw %}을(를) 사용하여 Braze 내에 이미 존재하는 경우 기존 고객 프로필을 업데이트합니다. 해당 별칭이 Braze 내에 존재하지 않으면 새로운 고객 프로필을 생성합니다. 사용자의 데이터(예: 도시)가 동일한 사용자에 대해 여러 Shopify 스토어에서 다를 수 있음을 유의하십시오. 이러한 경우 Braze는 항상 가장 최근 활동으로 스토어에서 고객 프로필을 업데이트합니다. 

{% alert warning %}
Braze는 가장 최근 활동이 있는 상점의 Shopify 고객 데이터로 고객 프로필을 업데이트합니다. 이것은 이메일, 전화번호, 발신 전화, 구/군/시 등과 같은 모든 속성이 최신 스토어 활동으로 덮어쓸 수 있음을 의미합니다. 예를 들어, 고객이 두 개의 다른 매장에서 다른 전화번호를 가지고 있는 경우, Braze는 가장 최근 활동이 있는 매장의 전화번호로 고객 프로필을 업데이트합니다.
{% endalert %}

[1]: {% image_buster /assets/img/multiple_stores.png %}
[2]: {% image_buster /assets/img/multiple_stores2.png %}
[3]: {% image_buster /assets/img/shopify_nested_attributes.png %}
[4]: {% image_buster /assets/img/shopify_tags.png %}
[5]: {% image_buster /assets/img/shopify_add_trigger.png %}
[6]: {% image_buster /assets/img/shopify_select_event.png %}
[7]: {% image_buster /assets/img/shopify_enter_storefront.png %}
