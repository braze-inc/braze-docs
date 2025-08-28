---
nav_title: 사용자 가져오기
article_title: 사용자 가져오기
page_order: 4
description: "Learn about Braze's various user import options, like CSV import, REST API, Cloud Data Ingestion, and more."

---
# 사용자 가져오기

> Learn about Braze's various user import options, like CSV import, REST API, Cloud Data Ingestion, and more.

## About HTML validation

Keep in mind that Braze does not sanitize, validate, or reformat HTML data during import, meaning script tags must be removed from all import data you use for web personalization.

데이터를 웹 브라우저에서 개인화 용도로 사용하기 위해 Braze에 가져올 때는 웹 브라우저에서 렌더링될 때 악의적으로 활용될 수 있는 HTML, JavaScript 또는 기타 스크립트 태그가 제거되었는지 확인하세요.

또는 HTML의 경우 Braze Liquid 필터(`strip_html`)를 사용하여 렌더링된 텍스트를 HTML로 이스케이프할 수 있습니다. 예를 들어, 다음과 같습니다.

{% tabs local %}
{% tab 입력 %}
{% raw %}
```liquid
{{ "Have <em>you</em> read <strong>Ulysses</strong>?" | strip_html }}
```
{% endraw %}
{% endtab %}
{% tab 출력 %}
{% raw %}
```liquid
Have you read Ulysses?
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Import options

### Braze CSV import

You can use CSV import to record and update the following user attributes and custom events. To get started, see [CSV Import]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/csv_import).

|Type|Definition|Example|Maximum file size|
|---|---|---|---|
|Default Attributes|Reserved user attributes recognized by Braze.|`first_name`, `email`|500 MB|
|Custom Attributes|User attributes unique to your business.|`last_destination_searched`|500 MB|
|Custom Events|Events unique to your business that represent user actions.|`trip_booked`|50 MB|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

### 람다 사용자 CSV 가져오기

You can use our serverless S3 Lambda CSV import script to upload user attributes to Braze. 이 솔루션은 CSV 업로더로 작동하며, CSV를 S3 버킷에 넣으면 스크립트가 API를 통해 업로드합니다.

1,000,000개의 행이 있는 파일의 예상 실행 시간은 5분 정도입니다. See [User attribute CSV to Braze import](https://www.braze.com/docs/user_guide/data/cloud_ingestion/) for more information.

### REST API

Use the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) to record custom events, user attributes, and purchases for users.

### 클라우드 데이터 수집

Use Braze [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/) to import and maintain user attributes.

## Legally required transactional emails

{% multi_lang_include email-via-sms-warning.md %}
