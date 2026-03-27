{% if include.section == "UTM parameters" %}

링크 단축을 사용하면 URL을 자동으로 추적할 수 있지만, URL에 UTM 매개변수를 추가하여 Google 애널리틱스와 같은 타사 분석 도구에서 캠페인의 성과를 추적할 수도 있습니다.

URL에 UTM 매개변수를 추가하려면 다음과 같이 하세요:

1. 기본 URL로 시작하세요. 추적하려는 페이지의 URL(예: `https://www.example.com`)입니다.
2. 기본 URL 뒤에 물음표(?)를 추가합니다.
3. 앰퍼샌드(&)로 구분하여 각 UTM 매개변수를 추가합니다.

예시: `https://www.example.com?utm_source=newsletter&utm_medium=sms`

{% endif %}

{% if include.section == "Frequently Asked Questions" %}

## 자주 묻는 질문

### 테스트 발송 시 받은 링크가 실제 URL인가요?

테스트 발송 전에 캠페인을 초안으로 저장한 경우, 그렇습니다. 그렇지 않으면 입력 안내 링크입니다. 실제로 시작된 캠페인에서 발송되는 정확한 URL은 테스트 발송에서 전송된 URL과 다를 수 있습니다.

### URL이 단축되기 전에 UTM 매개변수를 추가할 수 있나요?

예. 정적 및 동적 매개변수를 모두 추가할 수 있습니다. 

### 단축 URL은 얼마 동안 유효하나요?

개인화된 URL은 URL 등록 시점부터 2개월 동안 유효합니다. 정적 또는 개인화된 구분이 없는 [통합 링크 단축]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/?sdktab=unified)의 경우, 모든 링크는 9주 동안 유효합니다.

### 링크를 단축하려면 Braze SDK를 설치해야 하나요?

아니요. 링크 단축은 SDK 통합 없이 작동합니다.

{% endif %}

{% if include.section == "Custom Domains" %}

## 커스텀 도메인

링크 단축을 사용하면 자체 도메인을 사용하여 단축 URL의 모양과 느낌을 개인화할 수 있으므로 일관된 브랜드 이미지를 표현하는 데 도움이 됩니다. 자세한 내용은 [커스텀 도메인]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/custom_domains/)을 참조하세요.

{% endif %}