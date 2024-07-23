---
nav_title: "이벤트 개체"
article_title: API 이벤트 객체
page_order: 6
page_type: reference
description: "이 참고 문서에서는 이벤트 객체의 정의와 이벤트 객체가 이벤트 기반 캠페인 전략에서 어떻게 중요한 역할을 하는지에 대해 설명합니다."

---

# 이벤트 객체

> 이 문서에서는 이벤트 객체의 다양한 구성 요소, 이 객체를 사용하는 방법 및 예제에 대해 설명합니다.

## 이벤트 객체란 무엇인가요?

이벤트 객체는 특정 이벤트가 발생할 때 API를 통해 전달되는 객체입니다. 이벤트 객체는 이벤트 배열에 보관됩니다. 이벤트 배열의 각 이벤트 개체는 지정된 시간 값에 특정 사용자가 커스텀 이벤트의 단일 발생을 나타냅니다. 이벤트 객체에는 메시지, 데이터 수집 및 개인화에서 이벤트 속성정보를 설정하고 사용하여 사용자 지정할 수 있는 다양한 필드가 있습니다.

[개발자 가이드][1]의 플랫폼 통합 가이드에서 특정 플랫폼에 대한 커스텀 이벤트를 설정하는 방법을 확인할 수 있습니다. 이 정보는 다양한 플랫폼의 **애널리틱스** 탭 아래에 있는 **사용자 지정 이벤트 추적** 페이지에서 찾을 수 있습니다. 몇 가지를 링크해 두었습니다.

사용자 지정 이벤트 추적하기 문서를 참조하세요:

- [Android][2]
- [iOS][3]
- [웹][4]

### 개체 본문

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" is required
  "external_id" : (optional, string) External user ID,
  "user_alias" : (optional, User Alias Object) User alias object,
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "app_id" : (optional, string) see App Identifier,
  "name" : (required, string) the name of the event,
  "time" : (required, datetime as string in ISO 8601 or in `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format),
  "properties" : (optional, Properties Object) properties of the event
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean)
  // See following notes regarding anonymous push token imports
}
```

- [외부 사용자 ID]({{site.baseurl}}/api/basics/#user-ids)
- [앱 식별자]({{site.baseurl}}/api/identifier_types/)
- [ISO 8601 타임코드 위키][22]

#### 기존 프로필만 업데이트

Braze에서 기존 고객 프로필만 업데이트하려면 요청 본문에 `true` 값과 함께 `_update_existing_only` 키를 전달해야 합니다. 이 값을 생략하면 `external_id`가 없는 경우 Braze에서 새 고객 프로필을 생성합니다.

{% alert note %}
`/users/track` 엔드포인트를 통해 별칭 전용 고객 프로필을 만드는 경우 `_update_existing_only`를 `false`로 설정해야 합니다. 이 값을 생략하면 별칭 전용 프로필이 생성되지 않습니다.
{% endalert %}

## 이벤트 속성 개체
사용자 지정 이벤트 및 구매에는 이벤트 속성이 있을 수 있습니다. "속성" 값은 키가 속성 이름이고 값이 속성 값인 객체여야 합니다. 속성 이름은 비어 있지 않은 255자 이하의 문자열이어야 하며 선행 달러 기호($)가 없어야 합니다.

속성 값은 다음 데이터 유형 중 하나를 사용할 수 있습니다.

| 데이터 유형 | 설명 | 
| --- | --- |
| [정수](https://en.wikipedia.org/wiki/Integer) 또는 [부동](https://en.wikipedia.org/wiki/Floating-point_arithmetic) 소수점 | 숫자
| Booleans |  |
| Datetimes | [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 또는 `yyyy-MM-dd'T'HH:mm:ss:SSSZ` 형식의 문자열로 지정합니다. 배열 내에서는 지원되지 않습니다. |
| 문자열 | 255자 이하. |
| 배열 | 배열에는 날짜/시간을 포함할 수 없습니다. |
| 오브젝트 | 오브젝트가 문자열로 수집됩니다. |
{: .reset-td-br-1 .reset-td-br-2}

배열 또는 개체 값을 포함하는 이벤트 속성 개체는 최대 50KB의 이벤트 속성 페이로드를 가질 수 있습니다.

### 이벤트 속성 지속성
이벤트 속성정보는 상위 이벤트에 의해 트리거된 메시지를 필터링하고 Liquid 개인화할 수 있도록 설계되었습니다. 기본적으로 이러한 정보는 Braze 사용자 프로필에 유지되지 않습니다. 세분화에서 이벤트 속성 값을 사용하려면 이벤트 속성 값을 장기 저장하는 다양한 접근 방식에 대해 자세히 설명하는 [커스텀 이벤트][5]를 참조하세요.

#### 이벤트 예제 요청

```json
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "events" : [
    {
      "external_id" : "user1",
      "app_id" : "your-app-id",
      "name" : "watched_trailer",
      "time" : "2013-07-16T19:20:30+01:00"
    },
    {
      "external_id" : "user1",
      "app_id" : "your-app-id",
      "name" : "rented_movie",
      "time" : "2013-07-16T19:20:45+01:00",
      "properties": {
        "movie": "The Sad Egg",
        "director": "Dan Alexander"
      }
    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "app_id" : "your-app-id",
      "name" : "watched_trailer",
      "time" : "2013-07-16T19:20:50+01:00"
    }
  ]
}
```
- [ISO 8601 타임코드 위키][19]

## 이벤트 개체

제공된 예시를 사용하면 누군가 최근에 예고편을 시청한 후 영화를 대여한 것을 확인할 수 있습니다. 캠페인에 들어가서 이러한 속성을 기반으로 사용자를 세분화할 수는 없지만, 이러한 속성을 영수증 형태로 사용하여 Liquid를 사용하는 채널을 통해 사용자 지정 메시지를 보내는 데 전략적으로 사용할 수 있습니다. 예를 들어, "안녕하세요 **베스**, **댄 알렉산더의** **슬픈 달걀을** 대여해 주셔서 감사합니다. 대여하신 영화를 기반으로 추천 영화를 몇 가지 알려드립니다..."와 같은 예시입니다.


[1]: {{site.baseurl}}/developer_guide/home/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/
[5]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[19]: http://en.wikipedia.org/wiki/ISO_8601 "ISO 8601 타임코드 위키"
[21]: {{site.baseurl}}/api/api_key/#the-app-identifier-api-key
[22]: https://en.wikipedia.org/wiki/ISO_8601 "ISO 8601 시간 코드"
[23]: {{site.baseurl}}/api/basics/#external-user-id-explanation
