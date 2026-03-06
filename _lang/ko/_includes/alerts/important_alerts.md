{% if include.alert == "Shopify deprecation" %}

{% alert important %}
[Shopify 통합]({{site.baseurl}}/partners/shopify/#new-shopify-integration)의 새로운 버전이 2025년 4월부터 단계적으로 출시될 예정입니다. The phases will be based on the type of Shopify store and the external ID used to set up the initial integration. <br><br>**통합의 이전 버전은 2025년 8월 28일 이후 더 이상 사용할 수 없습니다. 이 날짜 이전에 새로운 버전으로 업데이트하여 통합을 문제 없이 계속 사용할 수 있습니다.**
{% endalert %}

{% endif %}

{% if include.alert == 'Web push private browsing' %}

{% alert important %}
개인 브라우징 창은 웹 푸시를 지원하지 않습니다.
{% endalert %}

{% endif %}

{% if include.alert == 'BCC address billable emails' %}

{% alert important %}
캠페인 또는 캔버스에 BCC 주소를 추가하면 Braze가 사용자에게 한 메시지와 BCC 주소에 한 메시지를 보내기 때문에 캠페인 또는 캔버스 구성 요소의 청구 가능한 이메일이 두 배로 증가합니다.
{% endalert %}

{% endif %}

{% if include.alert == 'Android notification priority' %}

{% alert important %}
알림 표시 우선 순위 설정은 Android O 이상을 실행하는 장치에서 더 이상 사용되지 않습니다. 이 장치에서는 [알림 채널 구성](https://developer.android.com/training/notify-user/channels#importance)를 통해 우선 순위를 설정합니다.
{% endalert %}

{% endif %}

{% if include.alert == "Email via SMS" %}

{% alert important %}
법적으로 요구되는 거래 이메일은 전달되지 않을 가능성이 높으므로 SMS 게이트웨이로 보내지 마세요.
<br><br>
전화번호와 제공업체의 게이트웨이 도메인(MM3라고 함)을 사용하여 보내는 이메일은 SMS(문자) 메시지로 수신될 수 있지만, 일부 이메일 제공업체는 이 동작을 지원하지 않습니다. 예를 들어, T-Mobile 휴대폰 번호(예: "9999999999@tmomail.net")로 이메일을 보내면 T-Mobile 네트워크에서 해당 휴대폰 번호를 소유한 모든 사람에게 SMS 메시지가 전송됩니다.
<br><br>
이러한 이메일이 SMS 게이트웨이로 전달되지 않더라도 이메일 요금 청구에 포함된다는 점에 유의하세요. 지원되지 않는 게이트웨이로 이메일을 보내지 않으려면 [지원되지 않는 게이트웨이 도메인 이름 목록](https://www.fcc.gov/consumer-governmental-affairs/about-bureau/consumer-policy-division/can-spam/domain-name-downloads)을 검토하세요.
{% endalert %}

{% endif %}

{% if include.alert == 'SDK auth' %}

{% alert important %}
보안을 강화하려면 사용자 사칭을 방지하기 위해 [SDK 인증]({{site.baseurl}}/developer_guide/authentication/) 기능을 추가하는 것이 좋습니다.
{% endalert %}

{% endif %}

{% if include.alert == 'Preference Center warning' %}

{% alert important %}
네이버 안드로이드 및 iOS 앱과 같은 특정 브라우저는 Braze 환경설정 센터를 지원하지 않는 경우가 있습니다. 일부 사용자가 이러한 브라우저를 사용할 것으로 예상되는 경우 사용자가 이메일 환경설정을 관리할 수 있는 대체 방법을 제공하는 것이 좋습니다.
{% endalert %}

{% endif %}

{% if include.alert == 'Purchase event deprecation' %}

{% alert important %}
구매 이벤트를 단계적으로 중단할 계획은 2026년에 발표될 예정입니다. 구매 이벤트는 궁극적으로 새로운 [전자상거래 추천 이벤트]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/)로 대체되며, 이는 세분화, 보고, 분석 등을 위한 향상된 기능을 제공합니다. 그러나 새로운 전자상거래 이벤트는 생애주기 가치(LTV) 또는 캔버스나 캠페인에서의 매출 보고와 같은 기존 구매 이벤트 관련 기능을 지원하지 않습니다. 구매 이벤트와 관련된 기능의 전체 목록은 [구매 이벤트 로깅]({{site.baseurl}}/user_guide/data/activation/custom_data/purchase_events/#logging-purchase-events)을 참조하십시오.
{% endalert %}

{% endif %}

{% if include.alert == 'Purchase event deprecation for eCommerce filters' %}

{% alert important %}
구매 이벤트를 단계적으로 중단할 계획은 2026년에 발표될 예정입니다. 구매 이벤트는 궁극적으로 새로운 [전자상거래 추천 이벤트]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/)로 대체되며, 이는 세분화, 보고, 분석 등을 위한 향상된 기능을 제공합니다. 이 경우 세그먼트 필터는 더 이상 구매 행동 아래에 채워지지 않습니다. 구매 이벤트의 전체 목록은 [구매 이벤트 로깅하기를]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/#logging-purchase-events) 참조하세요.
{% endalert %}

{% endif %}

{% if include.alert == 'S3 file bucket export' %}

{% alert important %}
S3 버킷에 저장된 내보내기 파일은 다운로드 링크가 만료된 후 자동으로 삭제됩니다(내보내기 이메일이 전송된 시점으로부터 4시간 후, 별도로 명시되지 않는 한).
{% endalert %} 

{% endif %}

{% if include.alert == 'Shopify customer create' %}

{% alert important %}
Shopify 통합은 데이터 구성 설정에 위치한 Shopify 고객 생성 및 고객 업데이트 웹훅을 지원합니다. Shopify에서 사용자 프로필이 생성되거나 업데이트되면 Braze에서 해당 사용자 프로필이 생성되거나 업데이트됩니다. <br><br>이러한 작업은 Braze에서 커스텀 이벤트를 트리거하지 않으며 오로지 [Shopify 사용자 데이터와 Braze 동기화]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview/#how-the-integration-works)에만 사용됩니다. 동기화된 데이터에는 [커스텀 속성]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#supported-shopify-custom-attributes), [표준 속성]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#supported-shopify-standard-attributes), 그리고 구성 내에서 활성화된 경우 [구독 그룹 상태]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview#syncing-shopify-email-and-sms-marketing-opt-ins)가 포함됩니다.
{% endalert %}

{% endif %}

{% if include.alert == 'context variable' %}

{% alert important %}
Canvas Context 조기 액세스에 참여하는 경우, Canvas 진입 속성은 Canvas 컨텍스트 변수의 일부입니다. 즉, `canvas_entry_properties` 은 이제 `context` 으로 참조됩니다. 각 컨텍스트 변수에는 이름, 데이터 유형, Liquid를 포함할 수 있는 값이 포함됩니다. 현재 `canvas_entry_properties`는 여전히 이전 버전과 호환됩니다. 자세한 내용은 [컨텍스트]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#how-it-works) 및 [Canvas 진입 속성 객체]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/)를 참조하십시오.
{% endalert %}

{% endif %}

{% if include.alert == 'time filter types' %}

{% alert important %}
**"연도의 날"과 "시간" 필터 유형 간의 선택**: 날짜가 포함된 컨텍스트 변수를 필터링할 때, 날짜가 매년 반복되는지 여부에 따라 올바른 비교 유형을 선택하십시오:

- **"연중일"**을 사용하세요. 날짜가 매년 반복될 때 (예: 생일, 기념일, 크리스마스와 같은 휴일). 이 비교 유형은 연도 구성 요소를 무시하고 연중일(1-365/366)을 기준으로 계산합니다.
- **"시간"**을 사용하세요. 날짜가 반복되지 않는 절대 날짜일 때 (예: 계약 종료 날짜, 약속 날짜, 구독 갱신 날짜). 이 비교 유형은 연도를 포함한 전체 타임스탬프를 기준으로 계산합니다.

절대 날짜에 대해 "연중일"을 사용하면 계산이 연도 구성 요소를 무시하기 때문에 잘못되거나 예상치 못한 결과가 발생할 수 있습니다. 예를 들어, 4월의 미래 계약 종료 날짜를 비교하여 63일 이내인지 확인할 때, "연중일"을 사용하면 날짜 번호(119 vs 359)만 비교하므로 잘못된 일치가 발생할 수 있습니다. 실제로 4월은 188일 남았습니다.

**일반 지침**: 날짜가 매년 반복되나요? **예** → "연중일"을 사용하세요. **아니오** → "시간"을 사용하세요.
{% endalert %}

{% endif %}
