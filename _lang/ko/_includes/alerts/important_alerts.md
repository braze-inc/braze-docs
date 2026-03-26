{% if include.alert == "Shopify deprecation" %}

{% alert important %}
[Shopify 통합의 새로운 버전]({{site.baseurl}}/partners/shopify/#new-shopify-integration)이 2025년 4월부터 단계적으로 출시될 예정입니다. 단계는 Shopify 스토어 유형과 초기 통합 설정에 사용된 외부 ID를 기반으로 합니다. <br><br>**통합의 이전 버전은 2025년 8월 28일 이후 더 이상 사용할 수 없습니다. 이 날짜 이전에 새로운 버전으로 업데이트하여 통합을 문제 없이 계속 사용하세요.**
{% endalert %}

{% endif %}

{% if include.alert == 'Web push private browsing' %}

{% alert important %}
개인 브라우징 창은 웹 푸시를 지원하지 않습니다.
{% endalert %}

{% endif %}

{% if include.alert == 'BCC address billable emails' %}

{% alert important %}
캠페인 또는 캔버스에 BCC 주소를 추가하면 Braze가 사용자에게 하나, BCC 주소에 하나의 메시지를 보내기 때문에 캠페인 또는 캔버스 구성요소의 청구 가능한 이메일이 두 배로 늘어납니다.
{% endalert %}

{% endif %}

{% if include.alert == 'Android notification priority' %}

{% alert important %}
알림 표시 우선순위 설정은 Android O 이상을 실행하는 기기에서 더 이상 사용되지 않습니다. 이러한 기기에서는 [알림 채널 구성](https://developer.android.com/training/notify-user/channels#importance)을 통해 우선순위를 설정하세요.
{% endalert %}

{% endif %}

{% if include.alert == "Email via SMS" %}

{% alert important %}
법적으로 요구되는 트랜잭션 이메일은 전달되지 않을 가능성이 높으므로 SMS 게이트웨이로 보내지 마세요.
<br><br>
전화번호와 제공업체의 게이트웨이 도메인(MM3라고 함)을 사용하여 보내는 이메일은 SMS(문자) 메시지로 수신될 수 있지만, 일부 이메일 제공업체는 이 동작을 지원하지 않습니다. 예를 들어, T-Mobile 전화번호(예: "9999999999@tmomail.net")로 이메일을 보내면 T-Mobile 네트워크에서 해당 전화번호를 소유한 사람에게 SMS 메시지가 전송됩니다.
<br><br>
이러한 이메일이 SMS 게이트웨이로 전달되지 않더라도 이메일 요금 청구에 포함된다는 점에 유의하세요. 지원되지 않는 게이트웨이로 이메일을 보내지 않으려면 [지원되지 않는 게이트웨이 도메인 이름 목록](https://www.fcc.gov/consumer-governmental-affairs/about-bureau/consumer-policy-division/can-spam/domain-name-downloads)을 검토하세요.
{% endalert %}

{% endif %}

{% if include.alert == 'SDK auth' %}

{% alert important %}
보안을 강화하려면 사용자 가장을 방지하기 위해 [SDK 인증]({{site.baseurl}}/developer_guide/authentication/) 기능을 추가하는 것을 권장합니다.
{% endalert %}

{% endif %}

{% if include.alert == 'Preference Center warning' %}

{% alert important %}
네이버 Android 및 iOS 앱과 같은 특정 브라우저는 Braze 환경설정 센터를 지원하지 않습니다. 일부 사용자가 이러한 브라우저를 사용할 것으로 예상되는 경우 이메일 환경설정을 관리할 수 있는 대체 방법을 제공하는 것이 좋습니다.
{% endalert %}

{% endif %}

{% if include.alert == 'Purchase event deprecation' %}

{% alert important %}
구매 이벤트를 단계적으로 중단할 계획은 2026년에 발표될 예정입니다. 구매 이벤트는 최종적으로 새로운 [전자상거래 추천 이벤트]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/)로 대체되며, 세분화, 보고, 분석 등의 기능이 향상됩니다. 그러나 새로운 전자상거래 이벤트는 생애주기 가치(LTV) 또는 캔버스나 캠페인의 매출 보고와 같은 기존 구매 이벤트 관련 기능을 지원하지 않습니다. 구매 이벤트와 관련된 기능의 전체 목록은 [구매 이벤트 로깅]({{site.baseurl}}/user_guide/data/activation/custom_data/purchase_events/#logging-purchase-events)을 참조하세요.
{% endalert %}

{% endif %}

{% if include.alert == 'Purchase event deprecation for eCommerce filters' %}

{% alert important %}
구매 이벤트를 단계적으로 중단할 계획은 2026년에 발표될 예정입니다. 구매 이벤트는 최종적으로 새로운 [전자상거래 추천 이벤트]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/)로 대체되며, 세분화, 보고, 분석 등의 기능이 향상됩니다. 이 변경이 적용되면 세그먼트 필터가 더 이상 구매 동작 아래에 표시되지 않습니다. 구매 이벤트의 전체 목록은 [구매 이벤트 로깅]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/#logging-purchase-events)을 참조하세요.
{% endalert %}

{% endif %}

{% if include.alert == 'S3 file bucket export' %}

{% alert important %}
S3 버킷에 저장된 내보내기 파일은 다운로드 링크가 만료된 후 자동으로 삭제됩니다(별도로 명시되지 않는 한, 내보내기 이메일이 전송된 시점으로부터 4시간 후).
{% endalert %} 

{% endif %}

{% if include.alert == 'Shopify customer create' %}

{% alert important %}
Shopify 통합은 데이터 구성 설정에 있는 Shopify 고객 생성 및 고객 업데이트 웹훅을 지원합니다. Shopify에서 고객 프로필이 생성되거나 업데이트되면 Braze에서도 해당 고객 프로필이 생성되거나 업데이트됩니다. <br><br>이러한 동작은 Braze에서 커스텀 이벤트를 트리거하지 않으며, [Shopify 사용자 데이터를 Braze와 동기화]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview/#how-the-integration-works)하는 용도로만 사용됩니다. 동기화되는 데이터에는 [커스텀 속성]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#supported-shopify-custom-attributes), [표준 속성]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#supported-shopify-standard-attributes), 그리고 구성에서 활성화된 경우 [구독 그룹 상태]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview#syncing-shopify-email-and-sms-marketing-opt-ins)가 포함됩니다.
{% endalert %}

{% endif %}

{% if include.alert == 'context variable' %}

{% alert important %}
캔버스 진입 등록정보는 캔버스 컨텍스트 변수의 일부입니다. 이는 `canvas_entry_properties`가 `context`로 참조됨을 의미합니다. 각 `context` 변수에는 이름, 데이터 유형, Liquid를 포함할 수 있는 값이 포함됩니다. 현재 `canvas_entry_properties`는 이전 버전과 호환됩니다. 자세한 내용은 [컨텍스트]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#how-it-works) 및 [캔버스 컨텍스트 오브젝트]({{site.baseurl}}/api/objects_filters/context_object)를 참조하세요.
{% endalert %}

{% endif %}

{% if include.alert == 'Braze Agents' %}

{% alert important %}
이 파트너는 [Braze 에이전트]({{site.baseurl}}/user_guide/brazeai/agents/)가 활성화된 경우에만 **기술 파트너** 페이지에 표시됩니다. 시작하는 데 도움이 필요하면 고객 성공 매니저에게 문의하세요.
{% endalert %}

{% endif %}

{% if include.alert == 'time filter types' %}

{% alert important %}
**"연중일"과 "시간" 필터 유형 중에서 선택하기**: 날짜가 포함된 컨텍스트 변수를 필터링할 때, 날짜가 매년 반복되는지에 따라 올바른 비교 유형을 선택하세요:

- **"연중일" 사용**: 날짜가 매년 반복될 때(예: 생일, 기념일 또는 크리스마스와 같은 휴일). 이 비교 유형은 연도 구성요소를 무시하고 연중일(1-365/366)을 기준으로 계산합니다.
- **"시간" 사용**: 날짜가 반복되지 않는 절대 날짜일 때(예: 계약 종료일, 약속 날짜 또는 구독 갱신 날짜). 이 비교 유형은 연도를 포함한 전체 타임스탬프를 기준으로 계산합니다.

절대 날짜에 "연중일"을 사용하면 연도 구성요소를 무시하므로 잘못되거나 예상치 못한 결과가 발생할 수 있습니다. 예를 들어, 4월의 미래 계약 종료일이 63일 이내인지 비교할 때, "연중일"을 사용하면 날짜 번호(119 vs 359)만 비교하기 때문에 잘못 일치할 수 있습니다. 실제로 4월까지는 188일이 남아 있기 때문입니다.

**일반 지침**: 날짜가 매년 반복되나요? **예** → "연중일"을 사용하세요. **아니오** → "시간"을 사용하세요.
{% endalert %}

{% endif %}

{% if include.alert == 'granular permissions ea' %}

{% alert important %}
세분화된 권한은 얼리 액세스 중입니다. 귀사의 마이그레이션이 계획되면, Braze 관리자에게 [세분화된 권한 마이그레이션]({{site.baseurl}}/granular_permissions_migration/)에 대한 이메일과 대시보드 내 배너가 전송됩니다.
{% endalert %}

{% endif %}

{% if include.alert == 'Shopify cart token alias' %}

{% alert important %}
이 통합에서 사용자 별칭은 Braze가 웹훅을 올바른 고객 프로필에 매칭할 수 있도록 다음 형식을 사용해야 합니다:<br><br>
- `alias_label`: `shopify_cart_${cartToken}`
- `alias_name`: `shopify_cart_token`
{% endalert %}

{% endif %}