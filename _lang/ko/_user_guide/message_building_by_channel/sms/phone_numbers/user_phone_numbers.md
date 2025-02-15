---
nav_title: "사용자 전화번호"
article_title: SMS 사용자 전화번호
page_order: 1
description: "이 참고 문서에서는 SMS 전화번호 서식 지정, 전화번호 가져오기 방법, SMS 구독 그룹에 사용자를 추가하는 방법에 대해 설명합니다."
page_type: reference
channel: 
  - SMS
  
---

# 사용자 전화번호

> 이 문서에서는 사용자 또는 고객의 전화번호와 관련된 다양한 주제에 대해 설명합니다. 자신의 전화번호에 대한 정보를 찾고 있다면 [전화번호 보내기]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_setup/short_and_long_codes/) 도움말 문서를 참조하세요.

전화번호는 사용자 프로필에 숫자 문자열로 표시됩니다. 숫자가 아닌 숫자(예: `,`, `-`, `(` 등)가 포함된 숫자를 가져오면 숫자가 아닌 부분이 제거됩니다. 예를 들어 `+1 (724) 123-4567` 을 가져오면 `17241234567` 으로 표시됩니다.

## 전화번호 가져오기

[CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv)를 업로드하거나 [API]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint)를 통해 전화번호를 가져와서 사용자를 만들 수 있습니다.

### 서식 지정

가장 좋은 방법은 전화번호를 가져오는 가장 좋은 방법은 [`E.164`](https://en.wikipedia.org/wiki/e.164) 형식을 사용하는 것입니다. 그러나 Braze는 최선을 다해 U.S. 번호를 해석하거나 변환하려고 노력할 것입니다.

모든 U.S. 번호는 유효한 지역 번호가 포함된 유효한 10자리 전화번호여야 합니다. `+` 및 국가 코드 없이 입력할 수 있으며, Braze는 모든 유효한 10자리 전화번호를 U.S 번호로 가정하고 매핑합니다.

모든 국제 번호는 `+`로 시작하고 그 뒤에 해당 국가 코드와 전화번호를 입력해야 합니다. (e.g `+442071838750`)

![][그림]{: style="max-width:50%;border: 0;"}

그러나 국가 또는 지역 번호가 다른 여러 지역으로 보내는 경우 정확성을 보장하기 위해 U.S.기반 전화번호라도 `E.164` 형식을 사용하는 것이 좋습니다.

다음 표에서 로컬 숫자 형식과 범용 `E.164` 형식의 차이점을 볼 수 있습니다:

| 국가 | 로컬 | 국가 코드 | `E.164` |
|---|---|---|---|
| USA | `4155552671` | 1 | `+14155552671` |
| 영국 | `2071838750` | 44 | `+442071838750` |
| 브라질 | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 reset-td-br-4}

### SMS 수신 그룹에 사용자 추가하기

고객이 SMS 메시지를 받으려면 유효한 전화번호가 있어야 하며 구독 그룹에 옵트인되어 있어야 합니다. 구독 그룹은 실행 중인 SMS 프로그램에 연결됩니다([SMS에 대한 법적 요구 사항]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/)을 준수하고 각 고객에 대한 동의를 기록했는지 확인해야 합니다). 자세한 내용은 [SMS 구독 그룹][1]을 참조하십시오. 

### 유효하지 않은 전화번호 처리하기

전화번호가 유효하지 않은 것으로 간주되면 Braze는 해당 사용자의 전화번호를 유효하지 않은 것으로 표시하고 해당 전화번호로 더 이상의 커뮤니케이션을 시도하지 않습니다. 유효하지 않은 전화번호는 사용자 프로필의 **참여 탭에** 표시됩니다.

![][사진2]{: style="max-width:50%;border: 0;"}

다음과 같은 이유로 전화 번호가 유효하지 않은 것으로 간주됩니다:
- **공급자 오류**: SMS 공급자로부터 영구 오류가 수신되었습니다. 이는 입력한 전화번호의 형식이 잘못되었거나 영구적으로 SMS 메시지를 수신할 수 없음을 나타냅니다.
- **비활성화됨**: 모바일 가입자가 서비스를 해지하고 통신사로부터 번호를 해제하여 전화번호가 비활성화되었습니다(향후 재활용되어 새 사용자에게 할당될 수 있음).

이러한 유효하지 않은 전화번호는 [SMS 엔드포인트]({{site.baseurl}}/api/endpoints/sms/)를 사용하여 관리할 수 있습니다. 

{% alert note %}
여러 사용자 프로필에 동일한 전화번호가 있고 해당 전화번호가 유효하지 않은 것으로 표시된 경우 해당 번호가 있는 기존의 모든 사용자 프로필이 유효하지 않은 것으로 표시됩니다. 새로 생성된 사용자 프로필은 처음에 유효하지 않은 것으로 표시되지 않습니다.
{% endalert %}

[세그먼트를 만들][2] 때 잘못된 전화번호를 가진 사용자를 포함하거나 제외할 수도 있습니다. 

### 타사 소싱 및 검증

Braze는 타사 도구에 의존하여 유효하지 않은 번호를 소싱합니다. Braze는 이러한 서비스의 중단이나 잘못된 정보에 대해 책임을 지지 않습니다. 따라서 이 도구를 유효하지 않은 번호 확인을 위한 유일한 규정 준수 수단으로 사용해서는 안 됩니다.

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/
[2]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment
[picture]: {% image_buster /assets/img/sms/e164.png %}
[picture2]: {% image_buster /assets/img/sms/invalid_banner.png %}
