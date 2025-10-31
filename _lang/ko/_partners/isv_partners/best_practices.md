---
nav_title: 모범 사례
hidden: true
---

# 사용자 수명 주기 및 식별자 모범 사례

## 데이터 수집

Braze가 데이터를 수집하는 방법에 대해 자세히 알아보세요.
- [SDK 데이터 수집]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/)
- [데이터 수집 모범 사례]({{site.baseurl}}/user_guide/data/user_data_collection/best_practices/)
- [사용자 프로필 수명 주기]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/)

## 브레이즈 식별자

- `braze_id`: Braze에서 할당된 식별자로, 변경할 수 없으며 데이터베이스에서 생성될 때 해당 사용자와 연결됩니다.
- `external_id`: 고객이 할당하는 식별자(일반적으로 UUID). 사용자를 고유하게 식별할 수 있는 경우 고객은 `external_id`를 할당하는 것이 좋습니다. 사용자가 식별된 후에는 익명으로 되돌릴 수 없습니다.
- `user_alias`: `external_id` 할당 전에 ID로 사용자를 참조하기 위한 수단으로 고객이 할당할 수 있는 고유한 대체 식별자. User aliases can later be merged with other aliases or an `external_id` when one becomes available through the Braze [User identify]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) endpoint.
    - [사용자 식별]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) 엔드포인트 내에서 `merge_behavior` 필드를 사용하여 알려진 사용자 프로필에 유지되어야 하는 사용자 별칭 프로필의 데이터를 지정할 수 있습니다.
    - 사용자 별칭이 전송 가능한 프로필이 되려면 프로필에 이메일 및/또는 전화번호를 표준 속성으로 포함해야 합니다.
- `device_id`: 자동으로 생성되는 기기별 식별자입니다. 고객 프로필에는 여러 개의 `device_ids`를 연결할 수 있습니다. 예를 들어 회사 컴퓨터, 집 컴퓨터, 태블릿, iOS 앱에서 계정에 로그인한 사용자는 프로필에 4개의 `device_ids`를 연결할 수 있습니다.
- 이메일 주소 및 전화번호:
    - Supported as an identifier in the Braze track user endpoint. 
    - 요청 내에서 이메일 주소 또는 전화번호를 식별자로 사용하는 경우 다음과 같은 세 가지 결과가 발생할 수 있습니다.
        1. 이 이메일/휴대폰을 가진 사용자가 Braze 내에 존재하지 않는 경우 이메일 전용/휴대폰 전용 사용자 프로필이 생성되며, 요청의 모든 데이터가 프로필에 추가됩니다.
        2. 이 이메일/전화 번호가 포함된 프로필이 이미 Braze 내에 존재하는 경우, 요청 내에서 전송된 모든 데이터를 포함하도록 프로필이 업데이트됩니다.
        3. 이 이메일/전화를 사용하는 프로필이 두 개 이상 있는 사용 사례에서는 가장 최근에 업데이트된 프로필이 우선됩니다.
    - 이메일 전용/전화 전용 고객 프로필이 존재하는 상태에서 동일한 이메일/전화로 식별된 프로필이 생성되면(예: 이메일 주수와 외부 ID가 동일한 다른 프로필), Braze는 두 번째 프로필을 생성합니다. 이후 업데이트 시 외부 ID가 있는 프로필로 이동합니다.
        - 두 프로필은 Braze [/merge/users]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) 엔드포인트를 사용하여 병합할 수 있습니다.

## 익명 사용자 처리하기

`external_id`에 액세스하지 않고 Braze에서 고객 프로필을 생성하거나 업데이트해야 하는 사용 사례의 경우, 이메일 주소나 전화번호와 같은 다른 식별자를 Braz의 [식별자로 사용자 내보내기]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) 엔드포인트로 전달하여 고객 프로필이 Braze에 존재하는지 확인할 수 있습니다. 

```json
{
 "email_address": "test@braze.com",
 "fields_to_export": ["braze_id", "user_aliases"]
}
```

해당 이메일 또는 휴대폰을 사용하는 사용자가 Braze 내에 존재하는 경우, 해당 프로필이 반환됩니다. 그렇지 않으면 빈 '사용자' 배열이 반환됩니다. 내보내기 엔드포인트를 사용하여 해당 이메일 주소를 가진 사용자가 이미 존재하는지 확인하면 익명 사용자 프로필이 해당 사용자와 연결되어 있는지 확인할 수 있다는 이점이 있습니다. 예를 들어 SDK를 통해 생성된 익명 프로필(`braze_id` 포함)이나 이전에 생성된 사용자 별칭 프로필이 있습니다. 

요청이 고객 프로필을 반환하지 않으면 사용자 별칭을 생성하거나 이메일 전용 사용자를 생성하도록 선택할 수 있습니다.

### 사용자 별칭

사용자 추적 엔드포인트를 사용하여 선택한 식별자를 별칭 이름으로 사용하여 사용자 별칭을 생성합니다. 새 사용자 별칭이 정의된 속성, 이벤트 또는 구매 오브젝트 내에서 `_update_existing_only`를 `false`로 포함하면 별칭 프로필을 생성하고 해당 프로필에 속성, 이벤트 및 구매를 동시에 추가할 수 있습니다. 

사용자 별칭이 전송 가능한 프로필이 되려면 아래와 같이 `email` 필드에 이메일 주소를 포함해야 합니다.

```json
{
   "attributes": [
   {
     "user_alias" : {
       "alias_name" : "test@braze.com",
       "alias_label" : "email"
     },
     "email": "test@braze.com",
     "_update_existing_only": false,
     "string_attribute": "sherman",
     "boolean_attribute_1": true,
     "integer_attribute": 25,
     "array_attribute": ["banana", "apple"]
   }
   ]
}
```

나중에 [사용자 식별]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) 엔드포인트를 통해 사용자 별칭을 사용할 수 있게 되면 이 사용자 별칭을 식별하여 `external_id`와 병합할 수 있습니다. 

### 이메일 전용 사용자 생성

사용자 추적 엔드포인트에서 이메일 주소를 식별자로 사용합니다. 

```json
{
    "attributes": [
        {
            "email": "test@braze.com",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ]
}
```
{% alert important %}
이 기능은 현재 얼리 액세스에서 제공ㅂ니다.
{% endalert %}

## 고객 프로필에 데이터 동기화

[사용자 추적]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
- 고객 프로필에 속성을 기록하는 등 Braze에서 사용자를 생성하고 업데이트할 수 있는 공개적으로 액세스할 수 있는 엔드포인트입니다. 이 엔드포인트에는 워크스페이스 수준에서 분당 50,000건의 요청으로 사용량 제한이 적용됩니다.
- 이 엔드포인트를 사용할 때는 파트너 설명에 표시된 대로 `partner` 키를 포함합니다.

[클라우드 데이터 수집]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview/#what-is-cloud-data-ingestion)
- 사용자 추적 엔드포인트와 마찬가지로 클라우드 데이터 수집을 통해 데이터를 고객 프로필에 동기화할 수 있습니다. 이 도구를 사용할 때 동기화하려는 데이터 웨어하우스 테이블 또는 보기를 설정하고 원하는 Braze 작업 공간에 연결하여 속성, 이벤트 및 구매를 프로필에 기록합니다.

[데이터 포인트]({{site.baseurl}}/user_guide/data/data_points/)
- Braze는 값의 변경 여부와 관계없이 고객 프로필에 '쓸' 때마다 데이터 포인트가 발생하는 데이터 포인트 소비 모델을 보유하고 있습니다. 따라서 변경된 속성만 Braze에 전송하는 것이 좋습니다. 

## 사용자 오디언스를 Braze로 보내기

[코호트 가져오기 동기화 파트너 설명서]({{site.baseurl}}/partners/isv_partners/cohort_import/)<br>
- Audiences of users can be synced to Braze as a cohort using the Braze Cohort Import API endpoints. 이러한 오디언스가 고객 프로필에 사용자 속성으로 저장되는 대신, 고객은 세분화 툴 내의 파트너 브랜드 필터를 통해 이 코호트를 구축하고 타겟팅할 수 있습니다. 이를 통해 고객은 특정 사용자 세그먼트를 더 쉽고 간편하게 찾고 타겟팅할 수 있습니다.
- 코호트 가져오기 엔드포인트는 공개되지 않으며 각 파트너에 따라 다릅니다. 따라서 코호트 엔드포인트에 대한 동기화는 고객의 워크스페이스 사용량 제한에 포함되지 않습니다. 

[사용자 추적]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)<br>
- 사용자 속성을 통해 특정 오디언스에서 사용자를 표시하여 Braze에서 사용자를 생성하는 데 즉시 사용할 수 있는 공개적으로 액세스할 수 있는 엔드포인트입니다. 이 엔드포인트와 코호트 가져오기 엔드포인트의 주요 차이점은 이 엔드포인트를 사용하여 전송된 오디언스는 고객 프로필에 저장되는 반면, 코호트 가져오기 엔드포인트는 세분화 툴에 필러로 표시된다는 점입니다. 이 엔드포인트에는 워크스페이스 수준에서 분당 50,000건의 요청으로 사용량 제한이 적용됩니다.
- 이 엔드포인트를 사용할 때는 [파트너 설명서]({{site.baseurl}}/partners/isv_partners/api_partner)에 표시된 대로 `partner` 키를 포함해야 합니다.

[데이터 포인트]({{site.baseurl}}/user_guide/data/data_points/)<br>
- Braze는 값의 변경 여부와 관계없이 고객 프로필에 '쓸' 때마다 데이터 포인트가 발생하는 데이터 포인트 소비 모델을 보유하고 있습니다.
- 데이터 포인트는 코호트 가져오기와 사용자 추적 엔드포인트 모두에서 발생합니다.

## 파트너로 인게이지먼트 분석 스트리밍

### 커런츠

Currents are a near real-time message engagement analytics streaming tool in Braze. 이렇게 하면 고객의 워크스페이스에서 전송된 캠페인 및 캔버스에 대한 모든 전송, 전달, 열람, 클릭 등에 대한 사용자 수준 데이터가 스트리밍됩니다. 몇 가지 주의해야 할 사항이 있습니다: 커런츠는 고객의 커넥터당 가격이 책정되므로 모든 신규 커런츠 파트너는 EA 프로세스를 거쳐야 합니다. 커스텀 브랜드 UI를 구축하고 커넥터를 공개적으로 제공하기 전에 파트너에게 5명의 고객을 EA의 일부로 확보할 것을 요청합니다. 
- [파트너 설명서]({{site.baseurl}}/partners/isv_partners/currents_integration/)
- [메시지 참여 이벤트]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) \- 커런츠 커넥터를 구매한 모든 고객은 이러한 이벤트에 액세스할 수 있습니다.
- [사용자 행동 이벤트]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) \- 현재 커넥터를 구매하는 모든 고객이 이러한 이벤트를 포함하는 '모든 이벤트' 커넥터를 구매하는 것은 아닙니다. 

### Snowflake 데이터 공유

Snowflake 데이터 공유 커넥터를 구매한 고객은 자동으로 메시지 인게이지먼트 및 사용자 행동 이벤트에 모두 액세스할 수 있습니다. Snowflake 데이터 공유를 파트너 통합으로 사용하는 경우, Braze는 고객을 대신하여 파트너의 Snowflake 인스턴스에 공유를 프로비저닝합니다. 참고로, 리전 간 데이터 공유는 고객에게 더 높은 비용을 요구하므로, Snowflake와 통합하려는 파트너에게 `US-EAST-1` 및/또는 `EU-CENTRAL-1`에 계정이 필요하다는 안내를 요청합니다.
- [파트너 설명서]({{site.baseurl}}/partners/isv_partners/currents_integration/)

## 캠페인 및 캔버스 구축 및 트리거하기

### Braze에서 에셋 생성
Braze는 고객과 파트너가 고객의 워크스페이스 내에서 이메일 템플릿과 콘텐츠 블록을 생성/업데이트할 수 있는 다양한 엔드포인트를 제공합니다. 이러한 템플릿과 콘텐츠 블록은 고객의 Braze 캠페인과 캔버스 전반에 걸쳐 사용할 수 있습니다.
- 이메일 템플릿
    - [템플릿 엔드포인트 만들기]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/)
    - [템플릿 엔드포인트 업데이트]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/#rate-limit)
- [콘텐츠 블록]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks) 
    - [콘텐츠 블록 엔드포인트 만들기]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/)
    - [콘텐츠 블록 엔드포인트 업데이트]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/)

### API 트리거 캠페인 및 캔버스

고객은 캠페인과 캔버스가 API로 트리거되도록 설정할 수 있습니다. 이러한 캠페인을 트리거하는 API 요청은 API 트리거 속성정보 및 오디언스 또는 수신자 매개변수를 전달하여 캠페인을 더욱 개인화 및 세분화하는 데 사용할 수 있습니다. 
- [API를 통한 캠페인 트리거]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#request-body)
    - 캠페인은 개별 이메일과 같은 단일 메시지입니다.
- [API를 통한 캔버스 트리거]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#request-body)
    - 캔버스는 마케터가 여러 메시지와 단계로 캠페인을 만들어 일관된 여정을 구성할 수 있는 통합 인터페이스입니다. 캔버스를 트리거할 때 사용자가 캔버스 흐름에 진입합니다. 이 경우 캔버스 기준에 더 이상 맞지 않을 때까지 사용자는 메시징을 계속 수신합니다. 
- [API 트리거 속성/캔버스 항목 속성]({{site.baseurl}}/api/objects_filters/trigger_properties_object) 
    - 전송 시 메시지에 동적으로 채워질 수 있는 데이터입니다.

### API 캠페인
API 캠페인을 생성할 때(위에서 언급한 API 트리거 캠페인과는 다름) Braze 대시보드는 고객이 캠페인 보고를 위한 분석을 추적할 수 있는 `campaign_id`를 생성하는 데만 사용됩니다. 캠페인 메시지 자체는 API 요청 내에서 정의됩니다. 
- [즉시 API 캠페인 보내기]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)
- [API 캠페인 예약하기]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/)

### ID 보내기
Use the Braze endpoint to generate a send ID which can be used to break down campaign analytics by send. 예를 들어, 위치별로 `campaign_id`(API 캠페인)가 생성된 경우 특정 위치에 대한 다양한 메시징의 성과를 추적하기 위해 전송별로 전송 ID를 생성할 수 있습니다. 
- [ID 보내기]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/)

## 연결된 콘텐츠

연결된 콘텐츠는 모든 채널 유형 내에서 전송 시점에 지정된 엔드포인트로 API 요청을 수행하고 응답으로 반환된 내용을 메시지에 채우는 데 사용할 수 있습니다.

연결된 콘텐츠의 다양한 기능을 통해 많은 고객이 Braze에서 상주하지 않거나 상주할 수 없는 콘텐츠를 삽입하는 데 이 기능을 사용하고 있습니다. 보다 일반적인 사용 사례는 다음과 같습니다:
- 블로그 또는 기사 콘텐츠를 메시지로 템플릿화하기
- 콘텐츠 추천
- 제품 메타데이터
- 로컬라이제이션 및 번역

주의해야 할 사항:
- Braze는 API 호출에 대해 요금을 부과하지 않으며, 데이터 포인트 할당량에 포함되지 않습니다.
- 연결된 콘텐츠 응답에는 1MB의 제한이 있습니다.
- 연결된 콘텐츠 호출은 메시지가 전송될 때 발생하지만, 인앱 메시지는 메시지를 볼 때 이 호출을 수행합니다.
- 연결된 콘텐츠 호출에서는, 성능상의 이유로 서버 응답 시간이 2초 미만이어야 하는 redirects.Braze를 따르지 않습니다. 서버가 응답하는 데 2초 이상 걸리면 콘텐츠가 삽입되지 않습니다.
- Braze 시스템은 수신자당 동일한 연결된 콘텐츠 API를 두 번 이상 호출할 수 있습니다. 이는 Braze가 메시지 페이로드를 렌더링하기 위해 연결된 콘텐츠 API 호출을 해야 할 수 있으며, 유효성 검사, 재시도 로직 또는 기타 내부 목적을 위해 수신자당 메시지 페이로드가 여러 번 렌더링될 수 있기 때문입니다. 

커넥티드 콘텐츠에 대해 자세히 알아보려면 이 문서를 참조하세요:
- [Making a Connected Content call]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/)
- [Aborting Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content)
- [Connected Content retries]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries)

