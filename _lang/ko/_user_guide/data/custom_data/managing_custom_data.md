---
nav_title: 커스텀 데이터 관리
article_title: 커스텀 데이터 관리
page_order: 20
page_type: reference
description: "이 참조 문서는 캠페인 및 세그먼트를 미리 채우거나 데이터 차단 및 삭제와 같은 커스텀 데이터를 관리하는 방법을 다룹니다."
---

# 커스텀 데이터 관리

> 이 페이지에서는 캠페인 및 세그먼트에 사용자 지정 데이터를 미리 채우고, 더 이상 유용하지 않은 데이터를 차단하고, 사용자 지정 이벤트와 속성 및 속성을 관리하는 방법에 대해 설명합니다.<br><br>특히 사용자 지정 속성을 관리하는 방법을 알아보려면 [사용자 지정 속성 관리하기를]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) 참조하세요.

## 커스텀 데이터를 미리 채우기

개발 팀이 해당 커스텀 데이터를 통합하기 전에 커스텀 데이터를 사용하여 캠페인 및 세그먼트를 설정하고 싶은 경우가 있을 수 있습니다. Braze는 이러한 데이터가 추적되기 전에 대시보드에서 커스텀 이벤트 및 속성을 미리 채워서 드롭다운 및 캠페인 생성 프로세스의 일부로 사용할 수 있도록 합니다.

커스텀 이벤트 및 속성을 미리 채우려면 다음을 수행하십시오:

1. **데이터 설정** > **커스텀 이벤트** 또는 **커스텀 속성** 또는 **제품**로 이동합니다.

![Navigate to Custom Attributes or Custom Events or Products.]({% image_buster /assets/img_archive/prepopulate_page.png %}){: style="max-width:90%;" }

{: start="2"}
2\. 사용자 지정 속성, 이벤트 또는 제품을 추가하려면 해당 페이지로 이동하여 **사용자 지정 속성 추가** 또는 **사용자 지정 이벤트 추가** 또는 **제품 추가를** 선택합니다.<br><br>For custom attributes, select a [data type]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types) for this attribute (for instance, boolean or string). 속성의 데이터 유형은 해당 속성에 사용할 수 있는 세분화 필터를 결정합니다. <br><br>![Add new attribute or event]({% image_buster /assets/img_archive/prepopulate_add.png %}){: style="max-width:80%;" }
3\. Select **Save**.

### 커스텀 이벤트 및 커스텀 속성 명명

커스텀 이벤트 및 커스텀 속성은 대소문자를 구분합니다. 나중에 개발 팀이 이러한 커스텀 이벤트 또는 속성을 통합할 때 이를 염두에 두세요. 팀은 커스텀 이벤트 또는 속성을 여기에 명명한 대로 정확히 명명해야 하며, 그렇지 않으면 Braze가 다른 커스텀 이벤트 또는 속성을 생성할 것입니다.

## 부동산 관리

사용자 지정 이벤트 또는 제품을 만든 후 해당 이벤트 또는 제품에 대한 **속성 관리를** 선택하여 새 속성을 추가하고 기존 속성을 차단 목록에 추가하고 [트리거 이벤트에서]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) 이 속성을 사용하는 캠페인 또는 캔버스를 확인합니다.

![Custom properties for a custom event.]({% image_buster /assets/img_archive/manageproperties1.png %}){: style="max-width:80%"}

이러한 추가된 커스텀 속성, 이벤트, 제품 또는 이벤트 속성정보를 추적 가능하게 만들려면 개발 팀에 요청하여 이전에 추가한 것과 동일한 이름을 사용하여 SDK에서 생성해야 합니다. 또는 Braze [API]({{site.baseurl}}/api/basics/)를 사용하여 해당 속성에 대한 데이터를 가져올 수 있습니다. 그 후, 커스텀 속성, 이벤트 또는 기타가 실행 가능해지고 사용자에게 적용됩니다.

{% alert note %}
모든 고객 프로필 데이터(커스텀 이벤트, 커스텀 속성, 커스텀 데이터)는 해당 프로필이 활성 상태인 동안 저장됩니다.
{% endalert %}

## 커스텀 데이터 차단 목록

때때로 커스텀 속성, 커스텀 이벤트, 또는 구매 이벤트가 너무 많은 데이터 포인트를 소비하거나, 더 이상 마케팅 전략에 유용하지 않거나, 오류로 기록된 것을 식별할 수 있습니다. 

이 데이터를 Braze로 보내지 않으려면, 엔지니어링 팀이 앱 또는 웹사이트의 백엔드에서 이를 제거하는 동안 커스텀 데이터 객체를 차단할 수 있습니다. 차단 목록에 추가하면 특정 커스텀 데이터 객체가 앞으로 Braze에 기록되지 않으므로 특정 사용자를 검색할 때 표시되지 않습니다.

{% alert important %}
사용자 지정 데이터를 차단하려면 캠페인, 캔버스 및 세그먼트에 액세스하고 편집할 수 있는 [사용자 권한이]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) 필요합니다.
{% endalert %}

차단된 데이터는 SDK에서 전송되지 않으며, Braze 대시보드는 다른 소스(예: API)에서 차단된 데이터를 처리하지 않습니다. 그러나 차단 목록에 추가해도 고객 프로필에서 데이터를 제거하거나 해당 커스텀 데이터 객체에 대해 발생한 데이터 포인트의 양을 소급하여 줄이지는 않습니다.

### 커스텀 속성, 커스텀 이벤트 및 제품 차단

{% alert important %}
이벤트 또는 속성이 차단 목록에 있으면 해당 이벤트 또는 속성을 사용하는 모든 세그먼트, 캠페인 또는 캔버스가 보관됩니다.
{% endalert %}

특정 커스텀 속성, 이벤트 또는 제품의 추적을 중지하려면 다음 단계를 따르세요.

1. **커스텀 속성**, **커스텀 이벤트**, 또는 **제품** 페이지에서 검색하세요.
2. 커스텀 속성, 이벤트 또는 제품을 선택하십시오. For custom attributes and events, you can select up to 100 to blocklist at a time.
3. **차단 목록을** 선택합니다.

![커스텀 속성 페이지에서 차단된 여러 선택된 커스텀 속성.]({% image_buster /assets/img_archive/blocklist_custom_attr.png %})

최대 300개의 커스텀 속성과 300개의 커스텀 이벤트를 차단할 수 있습니다. To prevent collecting certain device attributes, see our [SDK guide]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer/#blocking-data-collection). 

{% alert important %}
Custom attributes or custom events with a **Trashed** status will count towards the blocklisting limit until they're deleted.
{% endalert %}

커스텀 이벤트 또는 속성이 차단 목록에 포함된 경우 다음이 적용됩니다:

- Braze로 전송된 데이터는 처리되지 않으며, 차단된 이벤트 및 속성은 더 이상 데이터 포인트로 계산되지 않습니다.
- 기존 데이터는 다시 활성화되지 않는 한 사용할 수 없습니다
- 차단된 이벤트 및 속성은 필터 또는 그래프에 표시되지 않습니다
- 활성 캔버스의 초안 내에서 차단된 데이터에 대한 참조는 잘못된 값으로 로드되어 오류를 일으킬 수 있습니다
- 차단된 이벤트나 속성을 사용하는 모든 항목은 보관됩니다

이를 위해 Braze는 차단 목록 정보를 각 기기로 전송합니다. 이것은 수십만 또는 수백만 개의 이벤트 및 속성을 차단 목록에 추가하는 것에 대해 생각할 때 중요합니다. 이는 데이터 집약적인 작업이 될 것입니다.

### 차단 목록에 대한 고려 사항

많은 수의 이벤트와 속성을 차단 목록에 추가하는 것은 가능하지만 권장하지는 않습니다. 이것은 이벤트가 수행되거나 속성이 Braze로 전송될 때마다 이 이벤트나 속성이 전체 차단 목록과 대조되어야 하기 때문입니다.

Up to 300 items are sent to the SDK for blocklisting. If you blocklist more than 300 items, this data will be sent from the SDK. If you do not need to use the event or attribute in the future, consider removing it from your app code during your next release. 차단 목록의 변경 사항이 전파되는 데 몇 분 정도 걸릴 수 있습니다. You can re-enable any blocklist event or attribute at any time.

## 커스텀 데이터를 삭제하는 중

타겟팅 캠페인과 세그먼트를 구축하다 보면 더 이상 맞춤 이벤트나 맞춤 속성이 필요하지 않을 수 있습니다. 예를 들어, 특정 커스텀 속성을 일회성 캠페인의 일부로 사용했다면, [차단 목록에 추가한 후](#blocklisting-custom-attributes-custom-events-and-products) 이 데이터를 삭제하고 앱에서 해당 참조를 제거할 수 있습니다. 문자열, 숫자 및 중첩된 커스텀 속성과 같은 데이터 유형을 삭제할 수 있습니다.

{% alert important %}
You must be a [Braze admin]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#admin) to delete custom data.
{% endalert %}

사용자 지정 이벤트 또는 사용자 지정 속성을 삭제하려면 다음과 같이 하세요:

1. 삭제하려는 데이터 유형에 따라 **데이터 설정** > **사용자 지정 속성** 또는 **사용자 지정 이벤트로** 이동합니다.
2. 사용자 지정 데이터로 이동하여 <i class="fa-solid fa-ellipsis-vertical"></i> **작업** > **차단 목록을** 선택합니다.
3. 사용자 지정 데이터가 7일 동안 차단 목록에 등록된 후 <i class="fa-solid fa-ellipsis-vertical"></i> **작업** > **삭제를** 선택합니다.

### 삭제 작동 방식

사용자 지정 데이터를 삭제하면 다음과 같은 일이 발생합니다: 

- **사용자 지정 속성의 경우:** 모든 사용자의 프로필에서 속성 데이터를 영구적으로 제거합니다.
- **사용자 지정 이벤트의 경우:** 모든 사용자의 프로필에서 이벤트 메타데이터를 영구적으로 제거합니다.

삭제할 속성 또는 이벤트를 선택하면 해당 상태는 **휴지통으로** 변경됩니다. 향후 7일 동안 해당 속성 또는 이벤트를 복원할 수 있습니다. If you don't restore it after seven days, the data will be permanently deleted. 속성 또는 이벤트를 복원하면 차단된 상태로 다시 설정됩니다.

삭제해도 사용자 프로필에 사용자 지정 데이터 개체가 추가로 기록되는 것을 막지는 못하므로 이벤트나 속성을 삭제하기 전에 사용자 지정 데이터가 더 이상 기록되지 않는지 확인해야 합니다.

### 알아두어야 할 사항

커스텀 데이터를 삭제할 때 다음 세부 사항을 염두에 두십시오:

* **삭제는 영구적으로** 이루어집니다. 데이터를 복구할 수 없습니다.
* 데이터는 Braze 플랫폼과 사용자 프로필에서 삭제됩니다.
* 삭제 후 사용자 지정 속성 이름 또는 사용자 지정 이벤트 이름을 '재사용'할 수 있습니다. 즉, 삭제 후 사용자 지정 데이터가 Braze에 "다시 나타나는" 경우, 이는 중지되지 않은 통합이 동일한 사용자 지정 데이터 이름으로 데이터를 전송하고 있기 때문일 수 있습니다.
* 삭제한 사용자 지정 데이터가 다시 표시되는 경우 항목을 다시 차단 목록에 추가해야 할 수도 있습니다. 사용자 지정 데이터가 삭제되므로 차단 목록 상태는 유지되지 않습니다.
* 사용자 지정 데이터를 삭제해도 [데이터 포인트가]({{site.baseurl}}/user_guide/data/data_points) 소비되지 않으며 사용할 새 데이터 포인트도 생성되지 않습니다.

## 데이터 유형 비교 강제

Braze는 우리에게 전송된 속성 데이터의 데이터 유형을 자동으로 인식합니다. 그러나 여러 데이터 유형이 단일 속성에 적용되는 경우, 속성의 데이터 유형을 강제로 지정하여 실제로 무엇인지 알려줄 수 있습니다. **데이터 유형** 열의 드롭다운에서 선택합니다.

{% alert note %}
데이터 유형 강제 적용은 이벤트 속성정보 또는 구매 속성정보에 적용되지 않습니다.
{% endalert %}

![Custom attributes data type dropdown]({% image_buster /assets/img_archive/custom_events_view_data_type_dropdown.png %})

{% alert warning %}
If you choose to force the data type for an attribute, any data that comes in that isn't the specified type will be coerced into that type. If such coercion is impossible (for example, a string containing letters being coerced into a number), the data will be ignored. Any data ingested before the type change will continue to be stored as the old type (and therefore may not be segmentable), and a warning will appear next to the attribute on the affected users' profiles.
{% endalert %}

### 데이터 유형 변환

| 강제 데이터 유형 | 설명 |
|------------------|-------------|
| 부울 | `1`, `true`, `t`(대소문자 구분 없음)의 입력은 `true`로 저장됩니다 |
| 부울 | `0`, `false`, `f`(대소문자 구분 없음)의 입력은 `false`로 저장됩니다 |
| 숫자 | 정수 또는 플로트(`1`, `1.5`와 같은)는 숫자로 저장됩니다 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For more information on specific filter options exposed by different data type comparisons, check out [Configuring reporting]({{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting). For more information on the different available data types, refer to [Custom attribute data types]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types).

{% alert note %}
데이터가 Braze로 전송되면 변경할 수 없으며 수신 후 삭제하거나 수정할 수 없습니다. 그러나 대시보드에서 추적하는 항목을 제어하려면 앞의 섹션에 나열된 단계를 사용할 수 있습니다.
{% endalert %}


