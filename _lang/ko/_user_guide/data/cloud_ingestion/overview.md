---
nav_title: 개요
article_title: 클라우드 데이터 수집 개요 
page_order: 0
page_type: reference
description: "이 페이지에서는 클라우드 데이터 수집, 모범 사례 및 제품 제한 사항에 대한 개요를 제공합니다."

---

# Braze 클라우드 데이터 수집 개요

> Braze 클라우드 데이터 수집을 사용하면 데이터 웨어하우스 또는 파일 저장 시스템에서 Braze로 직접 연결하여 관련 사용자 또는 카탈로그 데이터를 동기화할 수 있습니다. Braze에 동기화되면 이 데이터는 개인화, 트리거링 또는 세분화와 같은 사용 사례에 활용될 수 있습니다. 

## 작동 방식

Braze 클라우드 데이터 수집(CDI)을 사용하면 데이터 웨어하우스 인스턴스와 Braze 워크스페이스 간의 통합을 설정하여 데이터를 정기적으로 동기화할 수 있습니다. 이 동기화는 사용자가 설정한 일정에 따라 실행되며, 각 통합은 다른 일정을 가질 수 있습니다. 동기화는 15분마다 자주 실행되거나 한 달에 한 번씩 드물게 실행될 수 있습니다. 15분보다 더 자주 동기화를 수행해야 하는 경우에는 고객 성공 관리자에게 문의하거나 실시간 데이터 수집을 위해 REST API 호출을 사용하는 것을 고려하세요.

동기화가 실행되면 Braze는 데이터 웨어하우스 인스턴스에 직접 연결하여 지정된 테이블에서 모든 새 데이터를 검색하고 Braze 대시보드에서 해당 데이터를 업데이트합니다. 동기화가 실행될 때마다 업데이트된 데이터는 Braze에 반영됩니다.

## 지원되는 데이터 소스

클라우드 데이터 수집은 다음 소스에서 Braze로 데이터를 동기화할 수 있습니다:

- 데이터 웨어하우스 소스 
   - Amazon Redshift
   - Databricks 
   - Google BigQuery
   - Microsoft Fabric
   - Snowflake

- 파일 스토리지 소스 
   - Amazon S3

## 지원되는 데이터 유형 

클라우드 데이터 수집은 다음 데이터 유형을 지원합니다. 
- 사용자 속성, 포함:
   - 중첩된 커스텀 속성
   - 객체 배열
   - 구독 상태
- 사용자 지정 이벤트
- 구매 이벤트
- 카탈로그 항목
- 사용자 삭제 요청

사용자 데이터는 외부 ID, 사용자 별칭, Braze ID, 이메일 또는 전화번호로 업데이트할 수 있습니다. 사용자는 외부 ID, 사용자 별칭 또는 Braze ID로 삭제할 수 있습니다. 

## 무엇이 동기화됩니까

동기화가 실행될 때마다 Braze는 이전에 동기화되지 않은 행을 찾습니다. Braze는 테이블 또는 뷰에서 `UPDATED_AT` 열을 사용하여 이를 확인합니다. `UPDATED_AT`이 마지막 동기화된 행보다 나중인 모든 행이 선택되어 Braze로 가져옵니다.

데이터 웨어하우스에 다음 사용자 및 속성을 테이블에 추가하고 `UPDATED_AT` 시간을 이 데이터를 추가하는 시간으로 설정하세요:

| UPDATED_AT | EXTERNAL_ID | PAYLOAD |
| --- | --- | --- |
| `2022-07-19 09:07:23` | `customer_1234` | {<br>    "attribute_1":"abcdefg"<br>    "attribute_2": {<br>        "attribute_a":"예시_값_2"<br>        "attribute_b":"예시_값_2"<br>    },<br>    "attribute_3":"2019-07-16T19:20:30+1:00"<br>} |
| `2022-07-19 09:07:23` | `customer_3456` | {<br>    "attribute_1":"abcdefg"<br>    "attribute_2":42,<br>    "attribute_3":"2019-07-16T19:20:30+1:00"<br>    "attribute_5":"테스팅"<br>} |
| `2022-07-19 09:07:23` | `customer_5678` | {<br>    "attribute_1":"abcdefg"<br>    "attribute_4":true,<br>    "attribute_5":"testing_123"<br>} |

다음 예정된 동기화 중에 가장 최근 타임스탬프보다 `UPDATED_AT` 타임스탬프가 나중인 모든 행이 Braze 고객 프로필에 동기화됩니다. 필드는 업데이트되거나 추가될 것이므로 매번 전체 고객 프로필을 동기화할 필요는 없습니다. 동기화 후, 사용자는 새로운 업데이트를 반영할 것입니다:

```json
{
  "external_id":"customer_1234",
  "email":"jane@example.com",
  "attribute_1":"abcdefg",
  "attribute_2":{
        "attribute_a":"example_value_1",
        "attribute_b":"example_value_2"
    },
  "attribute_3":"2019-07-16T19:20:30+1:00",
  "attribute_4":false,
  "attribute_5":"testing"
}
```
```json
{
  "external_id":"customer_3456",
  "email":"michael@example.com",
  "attribute_1":"abcdefg",
  "attribute_2":42,
  "attribute_3":"2019-07-16T19:20:30+1:00",
  "attribute_4":true,
  "attribute_5":"testing"
}
```
```json
{
  "external_id":"customer_5678",
  "email":"bob@example.com",
  "attribute_1":"abcdefg",
  "attribute_2":42,
  "attribute_3":"2017-08-10T09:20:30+1:00",
  "attribute_4":true,
  "attribute_5":"testing_123"
}
```

### 사용 사례: 첫 번째 동기화 및 이후 업데이트

이 예제는 데이터를 처음으로 동기화하는 일반적인 프로세스를 보여주며, 이후 업데이트에서는 변경된 데이터(델타)만 업데이트합니다. Braze가 일부 사용자 데이터가 포함된 테이블 `EXAMPLE_DATA`가 있다고 가정해 봅시다. 첫째 날에는 다음과 같은 값이 있습니다:

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>

<table>
    <thead>
        <tr>
            <th>external_id</th>
            <th>속성_1</th>
            <th>속성_2</th>
            <th>속성_3</th>
            <th>속성_4</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>12345</td>
            <td>823</td>
            <td>파란색</td>
            <td>380</td>
            <td>거짓</td>
        </tr>
        <tr>
            <td>23456</td>
            <td>28</td>
            <td>파란색</td>
            <td>823</td>
            <td>진실</td>
        </tr>
        <tr>
            <td>34567</td>
            <td>234</td>
            <td>파란색</td>
            <td>384</td>
            <td>진실</td>
        </tr>
        <tr>
            <td>45678</td>
            <td>245</td>
            <td>빨간</td>
            <td>349</td>
            <td>진실</td>
        </tr>
        <tr>
            <td>56789</td>
            <td>1938</td>
            <td>빨간</td>
            <td>813</td>
            <td>거짓</td>
        </tr>
    </tbody>
</table>

이 데이터를 CDI가 기대하는 형식으로 가져오려면 다음 쿼리를 실행할 수 있습니다:

```sql
SELECT
    CURRENT_TIMESTAMP AS UPDATED_AT,
    EXTERNAL_ID AS EXTERNAL_ID,
    TO_JSON(
        OBJECT_CONSTRUCT(
            'attribute_1', attribute_1,
            'attribute_2', attribute_2,
            'attribute_3', attribute_3,
            'attribute_4', attribute_4
        )
    ) AS PAYLOAD
FROM EXAMPLE_DATA;
```

이 중 어느 것도 이전에 Braze에 동기화되지 않았으므로 모든 것을 CDI의 소스 테이블에 추가하세요.

| UPDATED_AT          | EXTERNAL_ID | PAYLOAD                                                                                   |
| :------------------ | ----------- | ----------------------------------------------------------------------------------------- |
| 2023-03-16 15:00:00 | 12345       | { "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"} |
| 2023-03-16 15:00:00 | 23456       | { "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"}   |
| 2023-03-16 15:00:00 | 34567       | { "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"}  |
| 2023-03-16 15:00:00 | 45678       | { "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"}   |
| 2023-03-16 15:00:00 | 56789       | { "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

동기화가 실행되고 Braze는 사용 가능한 모든 데이터를 “2023-03-16 15:00:00”까지 동기화했다고 기록합니다. 그런 다음, 2일째 아침에 ETL이 실행되고 사용자 테이블의 일부 필드가 업데이트됩니다(강조 표시됨).

<table>
    <thead>
        <tr>
            <th>external_id</th>
            <th>속성_1</th>
            <th>속성_2</th>
            <th>속성_3</th>
            <th>속성_4</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>12345</td>
            <td style="background-color: #FFFF00;">145</td>
            <td style="background-color: #FFFF00;">빨간</td>
            <td>380</td>
            <td style="background-color: #FFFF00;">진실</td>
        </tr>
        <tr>
            <td>23456</td>
            <td style="background-color: #FFFF00;">15</td>
            <td>파란색</td>
            <td>823</td>
            <td>진실</td>
        </tr>
        <tr>
            <td>34567</td>
            <td>234</td>
            <td>파란색</td>
            <td style="background-color: #FFFF00;">495</td>
            <td style="background-color: #FFFF00;">거짓</td>
        </tr>
        <tr>
            <td>45678</td>
            <td>245</td>
            <td style="background-color: #FFFF00;">녹색</td>
            <td>349</td>
            <td>진실</td>
        </tr>
        <tr>
            <td>56789</td>
            <td>1938</td>
            <td>빨간</td>
            <td style="background-color: #FFFF00;">693</td>
            <td>거짓</td>
        </tr>
    </tbody>
</table>

이제 변경된 값만 CDI 소스 테이블에 추가하면 됩니다. 이 행들은 이전 행을 업데이트하는 대신 추가할 수 있습니다. 그 테이블은 이제 이렇게 보입니다:

| UPDATED_AT          | EXTERNAL_ID | PAYLOAD                                                                                   |
| :------------------ | ----------- | ----------------------------------------------------------------------------------------- |
| 2023-03-16 15:00:00 | 12345       | { "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"} |
| 2023-03-16 15:00:00 | 23456       | { "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"}   |
| 2023-03-16 15:00:00 | 34567       | { "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"}  |
| 2023-03-16 15:00:00 | 45678       | { "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"}   |
| 2023-03-16 15:00:00 | 56789       | { "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"} |
| 2023-03-17 09:30:00 | 12345       | { "ATTRIBUTE_1": "145", "ATTRIBUTE_2":"red", "ATTRIBUTE_4":"TRUE"} |
| 2023-03-17 09:30:00 | 23456       | { "ATTRIBUTE_1": "15"} |
| 2023-03-17 09:30:00 | 34567       | { "ATTRIBUTE_3":"495", "ATTRIBUTE_4":"FALSE"} |
| 2023-03-17 09:30:00 | 45678       | { "ATTRIBUTE_2":"green"} |
| 2023-03-17 09:30:00 | 56789       | { "ATTRIBUTE_3":"693"} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

CDI는 새 행만 동기화하므로 다음 동기화가 실행되면 마지막 다섯 행만 동기화됩니다.

### 사용 사례: 기존 객체 배열의 필드를 업데이트합니다

이 예제는 기존 객체 배열의 필드를 업데이트하는 방법을 보여줍니다. 다음 정의를 가진 소스 테이블이 있다고 가정해 봅시다:

```json 
Create table BRAZE_CLOUD_INGESTION_DEMO.BRAZE_SCHEMA.pet_list (
    pet_id int IDENTITY(1,1), 
    breed VARCHAR, 
    type VARCHAR, 
    name VARCHAR, 
    owner_id VARCHAR, 
    age int
);
```

이 예제에서는 각 사용자에 의해 소유된 애완동물 배열을 추가하고자 합니다. 이는 `owner_id`에 해당합니다. 구체적으로, 우리는 식별, 품종, 유형 및 이름을 포함하고자 합니다. 다음 쿼리를 사용하여 테이블 또는 뷰를 채울 수 있습니다.

```json
SELECT 
CURRENT_TIMESTAMP as UPDATED_AT,
owner_id as EXTERNAL_ID,
TO_JSON(
    OBJECT_CONSTRUCT(
        '_merge_objects','true',
       'pets',
        OBJECT_CONSTRUCT(
           '$add', ARRAY_AGG( OBJECT_CONSTRUCT(
                'id',
                pet_id,
                'breed',
                breed,
                'type',
                type,
                'name',
                name
                )) WITHIN GROUP (ORDER BY type ASC)    
        )
    )
)
as PAYLOAD from BRAZE_CLOUD_INGESTION_DEMO.BRAZE_SCHEMA.pet_list group by EXTERNAL_ID;
```

예상되는 출력은 다음과 같습니다:

```json
UPDATED_AT	EXTERNAL_ID	PAYLOAD
2023-10-02 19:56:17.377 +0000	03409324	{"_merge_objects":"true","pets":{"$add":[{"breed":"parakeet","id":5,"name":"Mary","type":"bird"}]}}
2023-10-02 19:56:17.377 +0000	21231234	{"_merge_objects":"true","pets":{"$add":[{"breed":"calico","id":2,"name":"Gerald","type":"cat"},{"breed":"beagle","id":1,"name":"Gus","type":"dog"}]}}
2023-10-02 19:56:17.377 +0000	12335345	{"_merge_objects":"true","pets":{"$add":[{"breed":"corgi","id":3,"name":"Doug","type":"dog"},{"breed":"salmon","id":4,"name":"Larry","type":"fish"}]}}
```

다음으로, 각 소유자의 업데이트된 이름 필드와 새로운 나이 필드를 보내기 위해, 다음 쿼리를 사용하여 테이블 또는 뷰를 채울 수 있습니다.

```json
SELECT 
CURRENT_TIMESTAMP as UPDATED_AT,
owner_id as EXTERNAL_ID,
TO_JSON(
    OBJECT_CONSTRUCT(
        '_merge_objects','true',
       'pets',
        OBJECT_CONSTRUCT(
           '$update', ARRAY_AGG( OBJECT_CONSTRUCT(
                '$identifier_key','id',
                '$identifier_value',pet_id,
                '$new_object',OBJECT_CONSTRUCT(
                    'name',name,
                    'age',age
                )
                )) WITHIN GROUP (ORDER BY type ASC)    
        )
    )
)
as PAYLOAD from BRAZE_CLOUD_INGESTION_DEMO.BRAZE_SCHEMA.pet_list group by EXTERNAL_ID; 
```

예상되는 출력은 다음과 같습니다:

```json
UPDATED_AT	EXTERNAL_ID	PAYLOAD
2023-10-02 19:50:25.266 +0000	03409324	{"_merge_objects":"true","pets":{"$update":[{"$identifier_key":"id","$identifier_value":5,"$new_object":{"age":7,"name":"Mary"}}]}}
2023-10-02 19:50:25.266 +0000	21231234	{"_merge_objects":"true","pets":{"$update":[{"$identifier_key":"id","$identifier_value":2,"$new_object":{"age":3,"name":"Gerald"}},{"$identifier_key":"id","$identifier_value":1,"$new_object":{"age":3,"name":"Gus"}}]}}
2023-10-02 19:50:25.266 +0000	12335345	{"_merge_objects":"true","pets":{"$update":[{"$identifier_key":"id","$identifier_value":3,"$new_object":{"age":6,"name":"Doug"}},{"$identifier_key":"id","$identifier_value":4,"$new_object":{"age":1,"name":"Larry"}}]}}
```

## 데이터 포인트 사용량

클라우드 데이터 수집에 대한 데이터 포인트 청구는 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track)를 통한 업데이트에 대한 청구와 동일합니다. [데이터 포인트]({{site.baseurl}}/user_guide/data/data_points/)에 대한 자세한 내용은 참조하세요. 

{% alert important %}
Braze 클라우드 데이터 수집은 사용 가능한 속도 제한에 포함되므로 다른 방법으로 데이터를 전송하는 경우 Braze API와 클라우드 데이터 수집 간에 사용량 제한이 결합됩니다.
{% endalert %}

## 데이터 설정 권장 사항

### 영어에서 한국어로 번역된 텍스트

동기화가 실행될 때마다 Braze는 이전에 동기화되지 않은 행을 찾습니다. Braze는 테이블 또는 뷰에서 `UPDATED_AT` 열을 사용하여 이를 확인합니다. `UPDATED_AT`이 마지막 동기화된 행보다 나중인 모든 행은 현재 고객 프로필에 있는 것과 동일한지 여부에 관계없이 Braze로 선택되어 가져옵니다. 그렇기 때문에 추가하거나 업데이트하려는 속성만 동기화할 것을 권장합니다.

데이터 포인트 소비는 REST API 또는 SDK와 같은 다른 수집 방법과 마찬가지로 CDI를 사용하여 동일하므로 소스 테이블에 새 속성이나 업데이트된 속성만 추가하도록 해야 합니다.

### `UPDATED_AT` 열에 UTC 타임스탬프 사용

`UPDATED_AT` 열은 일광 절약 시간 문제를 방지하기 위해 UTC로 설정해야 합니다. 가능한 경우 `SYSDATE()` 대신 `CURRENT_DATE()`와 같은 UTC 전용 기능을 선호하세요.

### `UPDATED_AT` 시간이 동기화 시간과 같지 않은지 확인하세요.

`UPDATED_AT` 필드가 이전 동기화 시간과 정확히 같은 시간인 경우 CDI 동기화에 데이터가 중복될 수 있습니다. This is because CDI will choose an "inclusive boundary" when it identifies any row that is the same time as the previous sync, and will make the rows able to sync. CDI will re-ingest those rows and create duplicate data.

### `EXTERNAL_ID` 열과 `PAYLOAD` 열을 구분합니다.

`PAYLOAD` 객체에는 외부 ID 또는 다른 ID 유형이 포함되어서는 안 됩니다. 

### 속성 제거

사용자 프로필에서 속성을 생략하려면 `null` 으로 설정하면 됩니다. 속성을 변경하지 않은 상태로 유지하려면 업데이트될 때까지 Braze에 보내지 마세요. 속성을 완전히 제거하려면 `TO_JSON(OBJECT_CONSTRUCT_KEEP_NULL(...))` 을 사용하세요.

### 점진적 업데이트 수행

데이터를 점진적으로 업데이트하여 동시 업데이트 시 의도치 않은 덮어쓰기를 방지할 수 있습니다.

다음 예제에서는 사용자에게 두 가지 속성이 있습니다:
- 색상: "녹색"
- 크기: "대형"

그러면 Braze는 해당 사용자에게 다음 두 가지 업데이트를 동시에 수신합니다:
- 요청 1: 색상을 "빨간색"으로 변경
- 요청 2: 크기를 "중간"으로 변경

요청 1이 먼저 발생하므로 사용자의 속성이 다음과 같이 업데이트됩니다:
- 색상: "Red"
- 크기: "대형"

그러나 요청 2가 발생하면 Braze는 원래 속성 값("녹색" 및 "대형")으로 시작한 다음 사용자의 속성을 다음과 같이 업데이트합니다:
- 색상: "녹색"
- 크기: "Medium"

요청이 완료되면 요청 2가 요청 1의 업데이트를 덮어쓰게 되므로 요청이 덮어쓰이지 않도록 시차를 두고 업데이트를 진행하는 것이 가장 좋습니다.

### 다른 테이블에서 JSON 문자열 만들기

각 속성을 내부적으로 자체 열에 저장하려면 해당 열을 JSON 문자열로 변환하여 Braze와 동기화해야 합니다. 그렇게 하려면 다음과 같은 쿼리를 사용할 수 있습니다:

{% tabs 로컬 %}
{% tab Snowflake %}
```json
CREATE TABLE "EXAMPLE_USER_DATA"
    (attribute_1 string,
     attribute_2 string,
     attribute_3 number,
     my_user_id string);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
        OBJECT_CONSTRUCT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'yet_another_attribute',
            attribute_3)
    )as PAYLOAD FROM "EXAMPLE_USER_DATA";
```
{% endtab %}
{% tab Redshift %}
```json
CREATE TABLE "EXAMPLE_USER_DATA"
    (attribute_1 string,
     attribute_2 string,
     attribute_3 number,
     my_user_id string);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    JSON_SERIALIZE(
        OBJECT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'yet_another_attribute',
            attribute_3)
    ) as PAYLOAD FROM "EXAMPLE_USER_DATA";
```
{% endtab %}
{% tab BigQuery %}
```json
CREATE OR REPLACE TABLE BRAZE.EXAMPLE_USER_DATA (attribute_1 string,
     attribute_2 STRING,
     attribute_3 NUMERIC,
     my_user_id STRING);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
      STRUCT(
        'attribute_1' AS attribute_1,
        'attribute_2'AS attribute_2,
        'yet_another_attribute'AS attribute_3
      )
    ) as PAYLOAD 
  FROM BRAZE.EXAMPLE_USER_DATA;
```
{% endtab %}
{% tab Databricks %}
```json
CREATE OR REPLACE TABLE BRAZE.EXAMPLE_USER_DATA (
    attribute_1 string,
    attribute_2 STRING,
    attribute_3 NUMERIC,
    my_user_id STRING
);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
      STRUCT(
        attribute_1,
        attribute_2,
        attribute_3
      )
    ) as PAYLOAD 
  FROM BRAZE.EXAMPLE_USER_DATA;
```
{% endtab %}
{% tab Microsoft Fabric %}
```json
CREATE TABLE [braze].[users] (
    attribute_1 VARCHAR,
    attribute_2 VARCHAR,
    attribute_3 VARCHAR,
    attribute_4 VARCHAR,
    user_id VARCHAR
)
GO

CREATE VIEW [braze].[user_update_example]
AS SELECT 
    user_id as EXTERNAL_ID,
    CURRENT_TIMESTAMP as UPDATED_AT,
    JSON_OBJECT('attribute_1':attribute_1, 'attribute_2':attribute_2, 'attribute_3':attribute_3, 'attribute_4':attribute_4) as PAYLOAD

FROM [braze].[users] ;
```
{% endtab %}

{% endtabs %}

### `UPDATED_AT` 타임스탬프 사용

Braze는 `UPDATED_AT` 타임스탬프를 사용하여 어떤 데이터가 Braze에 성공적으로 동기화되었는지 추적합니다. 동기화가 실행되는 동안 동일한 타임스탬프로 많은 행이 작성되면 Braze에 중복 데이터가 동기화될 수 있습니다. 중복 데이터를 피하기 위한 몇 가지 제안:
- `VIEW` 에 대해 동기화를 설정하는 경우 `CURRENT_TIMESTAMP` 을 기본값으로 사용하지 마세요. 이로 인해 동기화가 실행될 때마다 모든 데이터가 동기화됩니다. 왜냐하면 `UPDATED_AT` 필드가 우리의 쿼리가 실행되는 시간으로 평가되기 때문입니다. 
- 매우 오랜 시간 실행되는 파이프라인이나 쿼리가 소스 테이블에 데이터를 쓰는 경우, 이를 동기화와 동시에 실행하거나 삽입된 모든 행에 동일한 타임스탬프를 사용하는 것을 피하세요.
- 동일한 타임스탬프를 가진 모든 행을 쓰려면 트랜잭션을 사용하십시오.

### 테이블 구성

고객이 모범 사례 또는 코드 스니펫을 공유할 수 있도록 [GitHub 저장소](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion)가 공개되어 있습니다. 자신의 스니펫을 기여하려면 풀 리퀘스트를 생성하세요!

### 데이터 형식화

Braze `/users/track` 엔드포인트를 통해 가능한 모든 작업은 클라우드 데이터 수집을 통해 지원되며, 중첩 커스텀 속성 업데이트, 구독 상태 추가 및 커스텀 이벤트 또는 구매 동기화가 포함됩니다. 

페이로드 내의 필드는 해당 `/users/track` 엔드포인트와 동일한 형식을 따라야 합니다. 자세한 형식 요구 사항은 다음을 참조하십시오:

| 데이터 유형 | 서식 지정 사양 |
| --------- | ---------| --------- | ----------- |
| `attributes` | [사용자 속성 객체]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | [이벤트 객체]({{site.baseurl}}/api/objects_filters/event_object/) 보기 |
| `purchases` | [구매 객체]({{site.baseurl}}/api/objects_filters/purchase_object/)을 참조하십시오 |

중첩된 속성에서 [날짜를 캡처하는]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#capturing-dates-as-object-properties) 특별 요구 사항에 유의하세요. 

{% tabs 로컬 %}
{% tab 중첩 커스텀 속성 %}
커스텀 속성 동기화용 페이로드 열에 중첩 커스텀 속성을 포함할 수 있습니다. 

```json
{
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "genre": "Jazz",
        "play_analytics": {
            "count": 1000,
            "top_10_listeners": true
        }
      }
}
```

{% endtab %}
{% tab 이벤트 %}
이벤트를 동기화하려면 이벤트 이름이 필요합니다. `time` 필드는 ISO 8601 문자열 또는 `yyyy-MM-dd'T'HH:mm:ss:SSSZ` 형식으로 서식이 지정되어야 합니다. `time` 필드가 없으면 `UPDATED_AT` 열 값이 이벤트 시간으로 사용됩니다. 기타 필드에는 `app_id` 및 `properties`가 선택 사항입니다. 

행당 하나의 이벤트만 동기화할 수 있다는 점에 유의하세요.

```json
{
    "app_id" : "your-app-id",
    "name" : "rented_movie",
    "time" : "2013-07-16T19:20:45+01:00",
    "properties": {
        "movie": "The Sad Egg",
        "director": "Dan Alexander"
    }
} 
```

{% endtab %}
{% tab 구매 %}
구매 이벤트를 동기화하려면 `product_id`, `currency`, `price` 이 필요합니다. `time` 필드는 선택 사항이며 ISO 8601 문자열 또는 `yyyy-MM-dd'T'HH:mm:ss:SSSZ` 형식으로 형식화해야 합니다. `time` 필드가 없으면 `UPDATED_AT` 열 값이 이벤트 시간으로 사용됩니다. 기타 필드, `app_id`, `quantity` 및 `properties`를 포함하여 선택 사항입니다.

구매 이벤트는 행당 하나의 구매 이벤트만 동기화할 수 있습니다.

```json
{
    "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
    "product_id" : "Completed Order",
    "currency" : "USD",
    "price" : 219.98,
    "time" : "2013-07-16T19:20:30+01:00",
    "properties" : {
        "products" : [ { "name": "Monitor", "category": "Gaming", "product_amount": 19.99, },
        { "name": "Gaming Keyboard", "category": "Gaming ", "product_amount": 199.99, }
        ]
    }
}
```

{% endtab %}
{% tab 구독 그룹 %}
```json
{
    "subscription_groups" : [
        {
            "subscription_group_id": "subscription_group_identifier_1",
            "subscription_state": "unsubscribed"
        },
        {
            "subscription_group_id": "subscription_group_identifier_2",
            "subscription_state": "subscribed"
        },
        {
            "subscription_group_id": "subscription_group_identifier_3",
            "subscription_state": "subscribed"
        }
      ]
}
```
{% endtab %}
{% endtabs %}

### 데이터 웨어하우스 쿼리에 대한 시간 초과 방지

쿼리가 최적의 성능과 잠재적인 오류를 피하기 위해 한 시간 이내에 완료되도록 권장합니다. 쿼리가 이 시간 프레임을 초과하면 데이터 웨어하우스 구성을 검토하세요. 창고에 할당된 자원을 최적화하면 쿼리 실행 속도를 향상시킬 수 있습니다.

## 제품 제한

| Limitation            | 설명                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 통합 수 | 통합 설정의 수에는 제한이 없습니다. 그러나 테이블 또는 보기당 하나의 통합만 설정할 수 있습니다.                                             |
| 행 수         | By default, each run can sync up to 500 million rows. Any syncs with more than 500 million new rows will be stopped. If you need a higher limit than this, contact your Braze customer success manager or Braze Support. |
| 행별 속성     | 각 행에는 단일 사용자 ID와 최대 250개의 속성을 포함하는 JSON 객체가 포함되어야 합니다. JSON 객체의 각 키는 하나의 속성으로 간주됩니다 (즉, 배열은 하나의 속성으로 간주됩니다). |
| 페이로드 크기           | 각 행에는 최대 1MB의 페이로드가 포함될 수 있습니다. Payloads greater than 1 MB will be rejected, and the error "Payload was greater than 1MB" will be logged to the sync log along with the associated external ID and truncated payload. |
| 데이터 유형              | 클라우드 데이터 수집을 통해 사용자 속성, 이벤트 및 구매를 동기화할 수 있습니다.                                                                                                  |
| Braze 지역           | 이 제품은 모든 Braze 지역에서 사용할 수 있습니다. 어떤 Braze 지역이든 어떤 소스 데이터 지역에든 연결할 수 있습니다.                                                                              |
| 출처 지역       | Braze는 모든 지역 또는 클라우드 제공업체의 데이터 웨어하우스 또는 클라우드 환경에 연결됩니다.                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<br><br>
