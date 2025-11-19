---
nav_title: 사용자 가져오기
article_title: 사용자 가져오기
page_order: 4.1
description: "CSV 가져오기, REST API, 클라우드 데이터 수집 등과 같은 Braze의 다양한 사용자 가져오기 옵션에 대해 알아보세요."

---
# 사용자 가져오기

> CSV 가져오기, REST API, 클라우드 데이터 수집 등과 같은 Braze의 다양한 사용자 가져오기 옵션에 대해 알아보세요.

## HTML 유효성 검사 정보

Braze는 가져오기 중에 HTML 데이터를 살균, 유효성 검사 또는 재포맷하지 않으므로 웹 개인화에 사용하는 모든 가져오기 데이터에서 스크립트 태그를 제거해야 한다는 점에 유의하세요.

웹 브라우저에서 개인화 용도로 사용하기 위해 데이터를 Braze로 가져올 때는 웹 브라우저에서 렌더링될 때 악의적으로 활용될 수 있는 HTML, JavaScript 또는 기타 스크립트 태그가 제거되어 있는지 확인해야 합니다.

또는 HTML의 경우 Braze Liquid 필터(`strip_html`)를 사용하여 렌더링된 텍스트를 HTML 이스케이프 처리할 수 있습니다. 예를 들어

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{ "Have <em>you</em> read <strong>Ulysses</strong>?" | strip_html }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
Have you read Ulysses?
```
{% endraw %}
{% endtab %}
{% endtabs %}

## 가져오기 옵션

### Braze CSV 가져오기

CSV 가져오기를 사용하여 다음 사용자 속성 및 커스텀 이벤트를 기록하고 업데이트할 수 있습니다. 시작하려면 [CSV 가져오기를]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/csv_import) 참조하세요.

|유형|정의|예|최대 파일 크기|
|---|---|---|---|
|기본 속성|Braze에서 인식한 예약 사용자 속성.|`first_name`, `email`|500MB|
|커스텀 속성|비즈니스에 고유한 사용자 속성.|`last_destination_searched`|500MB|
|커스텀 이벤트|사용자 행동을 담당하는 비즈니스 고유의 이벤트.|`trip_booked`|50MB|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

### 람다 사용자 CSV 가져오기

서버리스 S3 Lambda CSV 가져오기 스크립트를 사용하여 사용자 속성을 Braze에 업로드할 수 있습니다. 이 솔루션은 CSV 업로더로 작동하며, CSV를 S3 버킷에 드롭하면 스크립트가 API를 통해 이를 업로드합니다.

1,000,000개의 행이 있는 파일의 예상 실행 시간은 5분 정도입니다. 자세한 내용은 [사용자 속성 CSV를 Braze로 가져오기를](https://www.braze.com/docs/user_guide/data/cloud_ingestion/) 참조하세요.

### REST API

[`/users/track` 엔드포인트를]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 사용하여 사용자에 대한 커스텀 이벤트, 사용자 속성 및 구매를 기록하세요.

### 클라우드 데이터 수집

Braze [Cloud 데이터 수집을]({{site.baseurl}}/user_guide/data/cloud_ingestion/) 사용하여 사용자 속성을 가져오고 유지 관리하세요.

## 법적으로 필요한 트랜잭션 이메일

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}
