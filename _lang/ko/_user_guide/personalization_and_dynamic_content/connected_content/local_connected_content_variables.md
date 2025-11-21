---
nav_title: 로컬 연결된 콘텐츠 변수
article_title: 로컬 연결된 콘텐츠 변수
page_order: 1
description: "이 참조 문서에서는 로컬 연결된 콘텐츠 변수를 사용하는 방법과 저장하는 방법을 다룹니다."
search_rank: 1
---

# 로컬 연결된 콘텐츠 변수

> 이 페이지에서는 로컬 연결된 콘텐츠 변수와 이를 사용하는 방법 및 저장하는 방법에 대한 개요를 제공합니다.

Braze는 `connected_content` 태그 내에 지정된 엔드포인트에 대해 전송 시 표준 GET 요청을 수행합니다. 엔드포인트가 JSON을 반환하면 자동으로 구문 분석되어 `connected`라는 변수에 저장됩니다. 엔드포인트가 텍스트를 반환하면 `connected_content` 태그 대신 메시지에 직접 삽입됩니다.

응답을 변수에 저장하려면 JSON 객체를 반환하는 것이 좋습니다. 그리고 연결된 콘텐츠의 응답이 태그를 텍스트로 대체하도록 하려면 응답이 유효한 JSON이 아니어야 합니다(예: [json.org](http://www.json.org)).

URL 뒤에 `:save your_variable_name`을 지정하여 데이터를 다른 것으로 저장할 수도 있습니다. 예를 들어, 다음 `connected_content` 태그는 응답을 `localweather`이라는 로컬 변수에 저장합니다(여러 `connected_content` JSON 변수를 저장할 수 있습니다).

{% raw %}
```js
{% connected_content https://www.metaweather.com/api/location/2459115/ :save localweather %}
```
{% endraw %}

메타날씨는 지역의 날씨를 반환하기 위해 "지구상의 위치 ID"를 사용하는 무료 날씨 API입니다. 이 코드는 테스트 및 학습 목적으로만 사용하십시오.

>  저장된 변수는 `connected_content` 요청을 포함하는 필드 내에서만 액세스할 수 있습니다. 예를 들어, 메시지와 제목 필드 모두에서 `localweather` 변수를 사용하려면 두 필드 모두에서 `connected_content` 요청을 만들어야 합니다. 요청이 동일하면 Braze는 두 번째 요청을 목적지 서버에 보내는 대신 캐시된 결과를 사용합니다. 그러나 HTTP POST를 통해 이루어진 연결된 콘텐츠 호출은 기본적으로 캐시되지 않으며 목적지 서버에 두 번째 요청을 보냅니다. POST 호출에 캐싱을 추가하려면 [`cache_max_age`](#configurable-caching) 옵션을 참조하십시오.

## JSON 구문 분석

연결된 콘텐츠는 `:save`을 지정할 때 JSON 형식의 결과를 로컬 변수로 해석합니다. 예를 들어, 날씨 관련 연결된 콘텐츠 엔드포인트는 다음 JSON 객체를 반환하며, 이를 `:save localweather`을 지정하여 로컬 변수 `localweather`에 저장합니다.
{% raw %}

```js
{
  "consolidated_weather": [
    {
      "id": 5.8143475362693e+15,
      "weather_state_name": "Clear",
      "weather_state_abbr": "c",
      "wind_direction_compass": "WSW",
      "created": "2017-06-12T14:14:46.268110Z",
      "applicable_date": "2017-06-12",
      "min_temp": 22.511666666667,
      "max_temp": 31.963333333333,
      "the_temp": 27.803333333333,
      "wind_speed": 6.8884690250312,
      "wind_direction": 251.62921994166,
      "air_pressure": 1021.335,
      "humidity": 50,
      "visibility": 14.945530601288,
      "predictability": 68
    },
    .
    .
    .
    "title": "New York",
    "location_type": "City",
    "woeid": 2459115,
    "latt_long": "40.71455,-74.007118",
    "timezone": "US\/Eastern"
  }
```

비가 오는지 여부를 확인하려면 `{{localweather.consolidated_weather[0].weather_state_name}}`을 참조하면 되며, 이 객체에서 사용하면 `Clear`를 반환합니다. 결과 위치 이름으로 개인화하려면 `{{localweather.title}}`이 `New York`를 반환합니다.
{% endraw %}

다음 이미지는 대시보드에서 설정이 올바르게 되어 있는 경우 볼 수 있는 구문 강조 유형을 보여줍니다. 또한 예제 `connected_content` 요청을 활용할 수 있는 방법을 보여줍니다!

{% raw %}
```liquid
{% connected_content https://www.metaweather.com/api/location/search/?query={{custom_attribute.${customCity}}} :save locationjson %}
{% connected_content https://www.metaweather.com/api/location/{{locationjson[0].woeid}}/ :save localweather %}

{% if {{localweather.consolidated_weather[0].weather_state_name}} == 'Rain' %}
It's raining! Grab an umbrella!
{% elsif {{localweather.consolidated_weather[0].weather_state_name}} == 'Clouds' %}
No sunscreen needed :)
{% else %}
Enjoy the weather!
{% endif %}
```
{% endraw %}

API가 {%raw%}`{{localweather.consolidated_weather[0].weather_state_name}}`{%endraw%}으로 응답하여 `Rain`를 반환하면 사용자는 이 푸시를 받게 됩니다.

\![메시지 "비가 오고 있습니다!"가 포함된 푸시 알림 우산을 챙기세요!"]({% image_buster /assets/img_archive/connected_weather_push2.png %} "Connected Content Push Usage Example"){:style="max-width:50%" }

{% multi_lang_include connected_content.md section='default behavior' %}

## HTTP POST

{% multi_lang_include connected_content.md section='http post' %}

### JSON 본문 제공

자신의 JSON 본문을 제공하려면 공백이 없으면 인라인으로 작성할 수 있습니다. 본문에 공백이 있는 경우 할당 또는 캡처 문을 사용해야 합니다. 즉, 이 세 가지 중 어느 것이든 허용됩니다:

{% raw %}
##### 인라인: 공백 허용되지 않음

```js
{% connected_content https://example.com/api/endpoint :method post :body {"foo":"bar","baz":"{{1|plus:1}}"} :content_type application/json %}
```

##### 캡처 문에 있는 본문: 공백 허용

```js
{% capture postbody %}
{"foo": "bar", "baz": "{{ 1 | plus: 1 }}"}
{% endcapture %}
{% connected_content https://example.com/api/endpoint :method post :body {{postbody}} :content_type application/json %}
```
{% endraw %}

{% raw %}
```js
{% capture postbody %}
{
"ids":[ca_57832,ca_75869],"include":{"attributes":{"withKey":["daily_deals"]}}
}
{% endcapture %}

{% connected_content
    https://example.com/api/endpoint
    :method post
    :headers {
      "Content-Type": "application/json"
  }
  :body {{postbody}}
  :save result
%}
```
{% endraw %}

{% raw %}
##### 할당 문에 있는 본문: 공백 허용

```js
{% assign postbody = '{"foo":"bar", "baz": "2"}' %}
{% connected_content https://example.com/api/endpoint :method post :body {{postbody}} :content_type application/json %}
```
{% endraw %}

## HTTP 상태 코드

연결된 콘텐츠 호출에서 HTTP 상태를 사용하려면 먼저 이를 로컬 변수로 저장한 다음 `__http_status_code__` 키를 사용하면 됩니다. 예를 들어:

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :save result %}
{% if result.__http_status_code__ != 200 %}
  {% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert important %}
이 키는 엔드포인트가 유효한 JSON 객체와 `2XX` 응답을 반환하는 경우에만 연결된 콘텐츠 객체에 자동으로 추가됩니다. 엔드포인트가 배열 또는 다른 유형을 반환하는 경우, 해당 키는 응답에 자동으로 설정될 수 없습니다.
{% endalert %}


[16]: [success@braze.com](mailto:success@braze.com)
