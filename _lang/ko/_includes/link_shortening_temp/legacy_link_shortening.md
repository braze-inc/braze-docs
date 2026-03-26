링크 단축 및 클릭 추적을 사용하면 SMS 또는 RCS 메시지에 포함된 URL을 자동으로 단축하고 클릭률 분석을 수집할 수 있어, 사용자가 캠페인에 어떻게 참여하고 있는지 이해하는 데 도움이 되는 추가 참여 측정기준을 제공합니다.

링크 단축 및 클릭 추적은 캠페인과 캔버스 모두에서 [메시지 배리언트 수준]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#step-1-create-your-campaign)에서 활성화할 수 있습니다.

URL의 길이는 활성화된 추적 유형에 따라 결정됩니다:
- **기본 추적**은 캠페인 수준의 클릭 추적을 활성화합니다. 정적 URL의 길이는 20자이며, 개인화된 URL의 길이는 25자입니다.
- **고급 추적**은 캠페인 수준 및 사용자 수준의 클릭 추적을 활성화하고, 클릭에 의존하는 세분화 및 리타겟팅 기능을 사용할 수 있게 합니다. 클릭은 커런츠를 통해 전송되는 [SMS 클릭 이벤트]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/)도 생성합니다. 고급 추적이 적용된 정적 URL의 길이는 27-28자이며, URL을 클릭한 사용자의 세그먼트를 생성할 수 있습니다. 개인화된 URL의 길이는 32-33자입니다.

링크는 공유 단축 도메인(`brz.ai`) 또는 커스텀 링크 단축 도메인을 사용하여 단축됩니다. URL 예시는 다음과 같습니다: `https://brz.ai/8jshX`(기본, 정적) 또는 `https://brz.ai/p/8jshX/2dj8d`(고급, 개인화). 자세한 내용은 [테스트](#testing)를 참조하세요.

`http://` 또는 `https://`로 시작하는 모든 정적 URL이 단축됩니다. 정적 단축 URL은 생성된 날짜로부터 1년간 유효합니다. Liquid 개인화가 포함된 단축 URL은 2개월간 유효합니다.

{% alert note %}
BrazeAI<sup>TM</sup> [인텔리전트 채널 필터]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/)를 사용할 계획이고 SMS 및 RCS 채널을 선택 가능하게 하려면, 고급 추적이 포함된 링크 단축을 활성화하세요.
{% endalert %}

## 링크 단축 사용하기

링크 단축을 사용하려면 메시지 작성기에서 링크 단축 토글이 활성화되어 있는지 확인하세요. 그런 다음 기본 추적 또는 고급 추적 중 하나를 선택합니다.

![링크 단축 토글이 있는 메시지 작성기.]({% image_buster /assets/img/link_shortening/legacy/temp_shortening1.png %})

Braze는 `http://` 또는 `https://`로 시작하는 URL만 인식합니다. URL이 인식되면 **미리보기** 섹션이 입력 안내 URL로 업데이트됩니다. Braze는 단축 후 URL의 길이를 추정하지만, 더 정확한 추정을 위해 테스트 사용자를 선택하고 메시지를 초안으로 저장하라는 경고가 표시됩니다.

!["메시지" 상자에 긴 URL이 있고 미리보기에 생성된 단축 링크가 있는 메시지 작성기.]({% image_buster /assets/img/link_shortening/legacy/temp_shortening3.png %})

### UTM 매개변수 추가

{% multi_lang_include analytics/click_tracking.md section='UTM parameters' %}

## URL의 Liquid 개인화

Braze 작성기 내에서 직접 URL을 동적으로 구성할 수 있어, URL에 동적 UTM 매개변수를 추가하거나 사용자에게 고유한 링크를 보낼 수 있습니다(예: 사용자를 유기한 장바구니로 안내하거나 재입고된 특정 제품으로 안내).

### 지원되는 Liquid 개인화 태그로 URL 생성

URL은 [지원되는 Liquid 개인화 태그]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)를 사용하여 동적으로 생성할 수 있습니다.

{% raw %}
```liquid
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

커스텀 정의 Liquid 변수의 단축도 지원합니다. 아래에 몇 가지 예시가 나와 있습니다:

### Liquid 변수를 사용하여 URL 생성

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

### Liquid 변수로 렌더링된 URL 단축

Liquid로 렌더링된 URL은 API 트리거 등록정보에 포함된 URL도 포함하여 단축됩니다. 예를 들어, {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %}가 유효한 URL을 나타내는 경우, 메시지를 보내기 전에 해당 URL을 단축하고 추적합니다.

### `/messages/send` 엔드포인트에서 URL 단축

링크 단축은 [`/messages/send` 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)를 통한 API 전용 메시지에도 활성화됩니다. 기본 또는 고급 추적도 활성화하려면 `link_shortening_enabled` 또는 `user_click_tracking_enabled` 요청 매개변수를 사용하세요.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
|`link_shortening_enabled`| 선택 사항 | 부울 | `link_shortening_enabled`를 `true`로 설정하면 링크 단축 및 캠페인 수준의 클릭 추적이 활성화됩니다. 추적을 사용하려면 `campaign_id`와 `message_variation_id`가 있어야 합니다.|
|`user_click_tracking_enabled`| 선택 사항 | 부울 | `user_click_tracking_enabled`를 `true`로 설정하면 링크 단축, 캠페인 수준 및 사용자 수준의 클릭 추적이 활성화됩니다. 추적된 데이터를 사용하여 URL을 클릭한 사용자의 세그먼트를 생성할 수 있습니다.<br><br> 이 매개변수를 사용하려면 `link_shortening_enabled`가 `true`여야 하며, `campaign_id`와 `message_variation_id`가 있어야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

전체 요청 매개변수 목록은 [요청 매개변수]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#request-parameters)를 참조하세요.

## 테스트

캠페인이나 캔버스를 시작하기 전에 먼저 메시지를 미리보기하고 테스트하는 것이 좋습니다. 이를 위해 **테스트** 탭으로 이동하여 [콘텐츠 테스트 그룹]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab#content-test-groups) 또는 개별 사용자에게 SMS 또는 RCS 메시지를 미리보기하고 보내세요.

이 미리보기는 관련 개인화 및 단축된 URL로 업데이트됩니다. 문자 수와 [청구 가능 세그먼트]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/)도 렌더링된 개인화 및 단축된 URL을 반영하여 업데이트됩니다.

메시지에 발송되는 단축 URL의 표현을 받으려면 테스트 메시지를 보내기 전에 캠페인이나 캔버스를 저장하세요. 테스트 발송 전에 캠페인이나 캔버스가 저장되지 않으면, 테스트 발송에 입력 안내 URL이 포함됩니다.

캔버스가 "단축 SMS 링크 클릭" 필터에 표시되려면, 단축 링크가 포함된 캔버스 단계에도 사용자 수준의 클릭 추적을 허용하는 고급 추적이 활성화되어 있어야 합니다. 단축 링크가 기본 추적으로 구성된 경우, SMS 단축 링크 클릭 이벤트를 필터링하는 옵션을 사용할 수 없습니다.

{% alert important %}
활성 캔버스 내에서 초안이 생성된 경우, 단축 URL이 생성되지 않습니다. 실제 단축 URL은 캔버스 초안이 활성화될 때 생성됩니다.
{% endalert %}

![테스트 수신자를 선택하는 필드가 있는 메시지 "테스트" 탭.]({% image_buster /assets/img/link_shortening/legacy/temp_shortening2.png %})

{% alert note %}
Liquid 개인화 및 단축 URL은 사용자가 선택된 후 **테스트** 탭에서 템플릿화됩니다. 정확한 문자 수를 받으려면 사용자를 선택하세요.
{% endalert %}

## 클릭 추적

링크 단축이 활성화되면, **SMS/MMS/RCS 성과** 테이블에 배리언트별 클릭 이벤트 수와 관련 클릭률을 보여주는 **총 클릭 수** 열이 포함됩니다. 측정기준에 대한 자세한 내용은 [메시지 성과]({{site.baseurl}}/sms_mms_rcs_reporting/)를 참조하세요.

![SMS 및 MMS 성과 측정기준 테이블.]({% image_buster /assets/img/link_shortening/shortening4.png %})

**과거 성과** 및 **SMS/MMS/RCS 성과** 테이블에도 **총 클릭 수** 옵션이 포함되어 있으며, 클릭 이벤트의 일별 시계열을 보여줍니다. 클릭은 리디렉션 시(예: 사용자가 링크를 방문할 때) 증가하며, 사용자당 두 번 이상 증가할 수 있습니다.

## 사용자 리타겟팅

리타겟팅에 대한 안내는 [리타겟팅]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/#filter-by-advanced-tracking-links)을 참조하세요.

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### URL을 클릭한 개별 사용자를 알 수 있나요?

네. **고급 추적**이 활성화되면, [SMS 리타겟팅 필터]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) 또는 커런츠에서 전송하는 SMS 클릭 이벤트(`users.messages.sms.ShortLinkClick`)를 활용하여 URL을 클릭한 사용자를 리타겟할 수 있습니다.

### 링크 단축은 딥링크 또는 유니버설 링크와 함께 작동하나요?

링크 단축은 딥링크와 함께 작동하지 않습니다. 대안으로 Branch나 Appsflyer와 같은 서드파티 제공업체의 유니버설 링크를 단축할 수 있지만, 사용자가 짧은 리디렉션 또는 "깜빡임" 효과를 경험할 수 있습니다. 이는 단축 링크가 앱 열기를 지원하는 유니버설 링크로 해석되기 전에 먼저 웹을 통해 라우팅되기 때문입니다. 또한 Braze는 유니버설 링크를 단축할 때 발생할 수 있는 문제(예: 기여도 손상 또는 예기치 않은 리디렉션)를 해결할 수 없습니다.

{% alert note %}
유니버설 링크와 함께 링크 단축을 구현하기 전에 사용자 경험을 테스트하여 기대에 부합하는지 확인하세요.
{% endalert %}

### `send_ids`가 SMS 클릭 이벤트와 연결되나요?

아니요. 하지만 고급 추적이 활성화된 경우, [쿼리 빌더]({{site.baseurl}}/query_builder/)를 사용하여 다음 쿼리로 커런츠 데이터를 조회함으로써 일반적으로 `send_ids`를 클릭 이벤트에 연결할 수 있습니다:

```sql
SELECT c.*, s.send_id
FROM USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED AS c
  INNER JOIN USERS_MESSAGES_SMS_SEND_SHARED AS s
    ON s.user_id = c.user_id 
      AND (s.message_variation_id = c.message_variation_id OR s.canvas_step_message_variation_id = c.canvas_step_message_variation_id)
WHERE s.send_id IS NOT NULL; 
```