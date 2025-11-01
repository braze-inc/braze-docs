{% if include.section == "UTM parameters" %}

링크 단축을 사용하면 URL을 자동으로 추적할 수 있지만, URL에 UTM 매개변수를 추가하여 Google 애널리틱스와 같은 타사 분석 도구에서 캠페인의 성과를 추적할 수도 있습니다.

URL에 UTM 매개변수를 추가하려면 다음과 같이 하세요:

1. 기본 URL로 시작하세요. 추적하려는 페이지의 URL(예: `https://www.example.com`)입니다.
2. 기본 URL 뒤에 물음표(?)를 추가합니다.
3. 각 UTM 매개변수를 앰퍼샌드(&)로 구분하여 추가합니다.

예는 `https://www.example.com?utm_source=newsletter&utm_medium=sms` 입니다.

{% endif %}

{% if include.section == "Frequently Asked Questions" %}

## Frequently asked questions

### 테스트 전송 시 받은 링크가 실제 URL인가요?

테스트 전송 전에 캠페인을 초안으로 저장한 경우, 예. 그렇지 않으면 플레이스홀더 링크입니다. 실행된 캠페인에서 전송된 정확한 URL은 테스트 전송에서 전송된 URL과 다를 수 있습니다.

### URL이 단축되기 전에 UTM 매개변수를 추가할 수 있나요?

예. 정적 및 동적 매개변수를 모두 추가할 수 있습니다. 

### 단축 URL은 얼마 동안 유효하나요?

맞춤 설정된 URL은 URL 등록 시점부터 2개월 동안 유효합니다.

### 링크를 단축하려면 Braze SDK를 설치해야 하나요?

아니요. 링크 단축은 SDK 통합 없이 작동합니다.

{% endif %}

{% if include.section == "Custom Domains" %}

## Custom domains

또한 링크 단축을 사용하면 자체 도메인을 사용하여 단축 URL의 모양과 느낌을 맞춤화할 수 있으므로 일관된 브랜드 이미지를 표현하는 데 도움이 됩니다. 자세한 내용은 [사용자 정의 도메인을]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/custom_domains/) 참조하세요.

{% endif %}