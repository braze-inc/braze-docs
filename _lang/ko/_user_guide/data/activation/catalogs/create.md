---
nav_title: 카탈로그 생성
article_title: 카탈로그 생성
alias: "/catalogs/"
page_order: 1
description: "이 참고 문서에서는 Liquid를 통해 Braze 캠페인에서 비사용자 데이터를 참조하는 카탈로그를 만드는 방법을 설명합니다."
---

# 카탈로그 생성

> 카탈로그를 만들려면 비사용자 데이터의 CSV 파일을 Braze로 가져와야 합니다. 그러면 해당 정보에 액세스하여 메시지를 더욱 풍부하게 만들 수 있습니다. 모든 유형의 데이터를 카탈로그로 가져올 수 있습니다. This data is typically some sort of metadata from your company such as product information for an eCommerce business, or course information for an education provider.

## 사용 사례

Commons use cases for catalogs include:

- 제품
- 서비스
- 음식
- 예정된 이벤트
- 음악
- 패키지

After this information is imported, you can begin accessing it in messages in a similar way to accessing custom attributes or custom event properties through Liquid.

## 지원되는 데이터 유형 {#supported-data-types}

다음 표는 지원되는 카탈로그 데이터 유형과 생성 또는 업데이트 방법을 나열합니다.

| 데이터 유형    | 설명                                   | CSV 업로드를 통해 사용 가능 | API 및 CDI를 통해 사용 가능 |
|--------------|-----------------------------------------------|:------------------------:|:-------------------------:|
| 문자열       | 문자의 시퀀스입니다.                     | ✅ 예                    | ✅ 예                     |
| 숫자       | 정수 또는 플로트인 숫자 값입니다.     | ✅ 예                    | ✅ 예                     |
| 부울      | `true` 또는 `false` 값입니다.                    | ✅ 예                    | ✅ 예                     |
| Time         | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) 형식으로 포맷된 문자열입니다.                        | ✅ 예                    | ✅ 예                     |
| JSON 객체  | 키-값 쌍이 있는 중첩 객체입니다. 플랫폼에 표시될 수 있지만 API 또는 CDI를 통해서만 생성 또는 업데이트할 수 있습니다.         | ⛔ 아니오                     | ✅ 예                     |
| 문자열 배열 | 문자열 목록입니다. 플랫폼에 표시될 수 있지만 API 또는 CDI를 통해서만 생성 또는 업데이트할 수 있습니다. 최대 100개 요소입니다. | ⛔ 아니오                     | ✅ 예                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 카탈로그 만들기

카탈로그를 생성하려면 **데이터 설정** > **카탈로그**로 이동한 다음 **새 카탈로그 생성**을 선택하고 다음 옵션 중 하나를 선택하십시오:

{% tabs local %}
{% tab Upload CSV %}
### 1단계: CSV 파일 검토

CSV 파일을 업로드하기 전에 CSV 파일이 다음 요구 사항을 충족하는지 확인하십시오:

| CSV 요구 사항 | 세부 정보 |
|-----------------|---------|
| 헤더 | CSV 파일의 첫 번째 열은 `id`이라고 명명해야 하며, 각 행은 고유한 `id` 값을 가져야 합니다. |
| 열 | CSV 파일은 최대 1,000개의 필드(열)를 가질 수 있으며, 각 열 이름은 최대 250자까지 가능합니다. |
| 파일 크기 | 무료 요금제의 경우, 회사 전체의 모든 CSV 파일의 총 크기는 100MB로 제한됩니다. 프로 요금제의 경우, 단일 CSV 파일의 최대 파일 크기는 2GB입니다. |
| 필드 값 | 각 셀(필드 값)은 최대 5,000자를 포함할 수 있습니다. |
| 유효한 문자 | `id` 열과 모든 헤더 값은 문자, 숫자, 하이픈 및 밑줄만 포함할 수 있습니다. |
| Data types | CSV 업로드를 위한 지원되는 데이터 유형에는 문자열, 숫자, 불리언 및 시간이 포함됩니다. API 및 CDI를 통해서만 사용할 수 있는 데이터 유형을 포함한 전체 데이터 유형 목록은 [지원되는 데이터 유형](#supported-data-types)을 참조하십시오. |
| 서식 지정 | 일관성을 유지하기 위해 모든 텍스트를 소문자로 포맷하십시오. |
| 인코딩 | UTF-8 인코딩을 사용하여 CSV 파일을 저장하고 업로드하십시오. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert note %}
CSV 파일을 저장할 공간이 더 필요하신가요? 카탈로그 업그레이드에 대한 자세한 내용은 Braze 계정 관리자에게 문의하세요.
{% endalert %}

### 2단계: CSV 업로드

Drag and drop your file to the upload zone, or select **Upload CSV** and choose your file.

![]({% image_buster /assets/img_archive/catalog_CSV_upload.png %}){: style="max-width:80%;"}

각 열에 대한 데이터 유형을 선택하십시오.

{% alert note %}
이 데이터 유형은 카탈로그를 설정한 후에는 편집할 수 없습니다. 또한, CSV 업로드에서는 `NULL` 값이 지원되지 않으며 문자열로 처리됩니다.
{% endalert %}

![]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:80%;"}

카탈로그에 대한 이름과 선택적 설명을 입력하십시오. 카탈로그 이름을 지정할 때 다음 요구 사항을 염두에 두십시오:

  - 고유해야 합니다.
  - 최대 250자
  - 숫자, 문자, 하이픈, 밑줄만 포함할 수 있습니다.

{% alert tip %}
카탈로그 이름에 [템플릿 사용](#template-catalog-names)을 사용하여 언어 또는 캠페인과 같은 변수를 기반으로 카탈로그 이름을 동적으로 생성할 수 있습니다.
{% endalert %}

![이름이 "my_catalog".]({% image_buster /assets/img_archive/in_browser_catalog.png %}){: style="max-width:80%;"}인 카탈로그

Select **Process Catalog** to create the catalog.

{% alert important %}
해당 [티어](#tiers)를 초과하는 경우 CSV 파일이 거부될 수 있습니다.
{% endalert %}

### 튜토리얼: CSV 파일에서 카탈로그 만들기

이 튜토리얼에서는 두 개의 게임과 해당 게임 비용, 이미지 링크가 나열된 카탈로그를 사용합니다.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">ID</th>
    <th class="tg-0pky">제목</th>
    <th class="tg-0pky">가격</th>
    <th class="tg-0pky">image_link</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">1234</td>
    <td class="tg-0pky">테일즈</td>
    <td class="tg-0pky">7.49</td>
    <td class="tg-0pky">https://picsum.photos/200</td>
  </tr>
  <tr>
    <td class="tg-0pky">1235</td>
    <td class="tg-0pky">재생성</td>
    <td class="tg-0pky">22.49</td>
    <td class="tg-0pky">https://picsum.photos/200</td>
  </tr>
</tbody>
</table>

CSV 파일을 업로드하여 카탈로그를 생성합니다. `id`, `title`, `price`, `image_link`의 데이터 유형은 각각 문자열, 문자열, 숫자, 문자열입니다. 

{% alert note %}
이 데이터 유형은 카탈로그를 설정한 후에는 편집할 수 없습니다.
{% endalert %}

![네 개의 카탈로그 열 이름: "id", "title", "price", "image_link".]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:85%;"}

다음으로 이 카탈로그 "games_catalog"의 이름을 지정하고 **프로세스 카탈로그** 버튼을 선택합니다. 그러면 Braze는 카탈로그를 생성하기 전에 카탈로그에 오류가 있는지 확인합니다.

![이름이 "games_catalog".]({% image_buster /assets/img_archive/catalog_new_name.png %}){: style="max-width:85%;"}인 카탈로그

카탈로그가 생성된 후에는 이 이름을 편집할 수 없다는 점에 유의하세요. 카탈로그를 삭제하고 동일한 카탈로그 이름을 사용하여 업데이트된 버전을 다시 업로드할 수 있습니다.

카탈로그를 생성한 후에는 [캠페인에서 카탈로그]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/)를 참조할 수 있습니다.
{% endtab %}

{% tab Create in browser %}
### 필수 조건

브라우저에서 카탈로그를 편집하거나 생성하기 전에 작업 공간에 대한 다음 [사용자 권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)이 필요합니다:

- 카탈로그 보기
- 카탈로그 편집
- 카탈로그 내보내기
- 카탈로그 삭제

{% multi_lang_include deprecations/user_permissions.md %}

### 1단계: 카탈로그 세부정보 입력

카탈로그에 대한 이름과 선택적 설명을 입력하십시오. 카탈로그 이름을 지정할 때 다음 요구 사항을 염두에 두십시오:

- 고유해야 합니다.
- 최대 250자
- 숫자, 문자, 하이픈, 밑줄만 포함할 수 있습니다.

{% alert tip %}
카탈로그 이름에 [템플릿 사용](#template-catalog-names)을 사용하여 언어 또는 캠페인과 같은 변수를 기반으로 카탈로그 이름을 동적으로 생성할 수 있습니다.
{% endalert %}

![이름이 "my_catalog".]({% image_buster /assets/img_archive/in_browser_catalog.png %}){: style="max-width:80%;"}인 카탈로그

### 2단계: 카탈로그 생성

목록에서 카탈로그를 선택한 다음 **카탈로그 업데이트** > **필드 추가**를 선택합니다. **필드 이름**을 입력하고 드롭다운을 사용하여 데이터 유형을 선택합니다. Repeat as needed.

![두 개의 예시 필드 "평가"와 "이름".]({% image_buster /assets/img_archive/add_catalog_fields.png %}){: style="max-width:50%;"}

**카탈로그 업데이트** 선택 > **항목 추가**를 선택하여 이전에 추가한 필드를 기반으로 정보를 입력하여 카탈로그에 항목을 추가합니다. 그런 다음 **항목 저장** 또는 **저장 및 추가**를 선택하여 항목을 계속 추가합니다.

![카탈로그 항목 추가.]({% image_buster /assets/img_archive/add_catalog_items.png %}){: style="max-width:50%;"}

{% alert note %}
Braze는 대시보드 타임스탬프를 기반으로 시간 값을 처리합니다. 예를 들어 열의 값이 "03/13/2024"이고 시간대가 태평양 표준 시간대인 경우, 이 시간은 "2024년 3월 12일, 오후 5시"로 Braze에 가져올 수 있습니다.
{% endalert %}
{% endtab %}
{% endtabs %}

## 카탈로그 데이터 유형

카탈로그는 데이터를 효과적으로 구성하고 구조화하는 데 도움이 되는 다양한 데이터 유형을 지원합니다. 다음 표는 지원되는 각 데이터 유형과 CSV 및 API 유형 이름에 대한 매핑을 설명합니다:

| Data Type | 형식 | 예시 | 설명 |
|-----------|--------|---------|-------------|
| 문자열 | 텍스트 | `"Hello World"` | 이름, 설명 및 ID와 같은 텍스트 데이터에 사용되는 모든 문자 시퀀스입니다. CSV 및 API 가져오기에서 `string` 유형에 해당합니다. |
| Time | ISO 8601 또는 Unix 타임스탬프(초) | `"2024-03-15T14:30:00Z"` | ISO 8601 또는 Unix 타임스탬프(초)로 형식화된 날짜 및 시간 값입니다. API에서 `time` 유형에 해당하며 CSV 가져오기에서 `datetime` 유형에 해당합니다. |
| 부울 | `true` 또는 `false` | `true` | 참 또는 거짓 상태를 나타내는 논리 값입니다. CSV 및 API 가져오기에서 `boolean` 유형에 해당합니다. |
| 숫자 | 정수 또는 소수 | `42` 또는 `19.99` | 가격, 수량, 등급 등을 위한 정수 및 부동 소수점 숫자를 포함한 숫자 값. CSV 가져오기에서 `integer` 및 `float` 유형과 API의 `number` 유형에 해당합니다. |
| 객체 | JSON 객체 | `{"key": "value", "price": 10}` | 복잡한 중첩 데이터 구조. API `type` 값은 `object`입니다. 대시보드에 JSON 객체로 표시됩니다. API 또는 클라우드 데이터 수집(CDI)을 통해서만 사용할 수 있습니다. |
| 배열 | 문자열 배열 | `["red", "blue", "green"]` | 문자열 값 목록. API `type` 값은 `array`입니다. 대시보드에 문자열 배열로 표시됩니다. API 또는 CDI를 통해서만 사용할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

## 카탈로그 이름 {#template-catalog-names}에 템플릿 사용

카탈로그 이름을 지정할 때 카탈로그 이름에 템플릿을 사용할 수도 있습니다. 이것은 언어 또는 캠페인과 같은 변수를 기반으로 카탈로그 이름을 동적으로 생성할 수 있게 해줍니다. 예를 들어 다음을 사용할 수 있습니다:

{% raw %}
```liquid
{% assign language = "content_spanish" %}

{% catalog_items {{language}} fall_campaign %}
{{ items[0].body }}
```
{% endraw %}

## 카탈로그 관리

### 대시보드에서

CSV를 업로드하거나 브라우저에서 카탈로그를 생성한 후 카탈로그를 업데이트하려면 **카탈로그 업데이트 > CSV 업로드**를 선택한 다음 카탈로그의 항목을 업데이트, 추가 또는 삭제할지 선택합니다.

### REST API 사용

더 많은 카탈로그를 구축할 때 [목록 카탈로그 엔드포인트를]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) 사용하여 워크스페이스에 있는 카탈로그 목록을 반환할 수도 있습니다.

REST API는 JSON 객체 및 문자열 배열을 포함한 모든 [카탈로그 데이터 유형](#supported-data-types)을 지원합니다. JSON 객체 및 문자열 배열은 REST API를 통해서만 생성하거나 업데이트할 수 있습니다.

### 클라우드 데이터 수집 사용

정기적으로 데이터 웨어하우스(예: Snowflake, Redshift, BigQuery, Databricks, Microsoft Fabric 또는 S3)에서 카탈로그 데이터를 직접 동기화하여 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data/)을 통해 카탈로그를 유지 관리할 수 있습니다.

## 카탈로그 항목 관리

카탈로그를 관리하는 것 외에도 비동기 및 동기 엔드포인트를 사용하여 카탈로그 항목을 관리할 수도 있습니다. 여기에는 카탈로그 항목을 편집 및 삭제하고 카탈로그 항목 세부 정보를 나열하는 기능이 포함됩니다. 

예를 들어 개별 카탈로그 항목을 편집하려는 경우 [`/catalogs/catalog_name/items/item_id` 엔드포인트]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/)를 사용할 수 있습니다.

## 카탈로그 저장 {#tiers}

The free version of catalogs supports CSV file sizes of up to 100 MB for all CSV files combined across your company, whereas the Catalogs Pro version supports CSV file sizes of up to 2 GB for a single CSV file.

{% alert important %}
Braze 대시보드에 표시되는 패키지 자격은 시각적 편의를 위해 가장 가까운 단위로 반올림되었지만, 구매하신 전체 자격은 계속 이용하실 수 있습니다. 카탈로그 저장소 업그레이드를 요청하려면 Braze 계정 관리자에게 문의하세요.
{% endalert %}

#### 무료 버전

무료 버전의 카탈로그 저장 용량은 최대 100MB입니다. You can have unlimited items as long as they're under 100 MB. 

#### 카탈로그 프로

회사 수준에서 카탈로그 프로의 최대 저장 용량은 카탈로그 데이터의 크기에 따라 결정됩니다. 스토리지 크기 옵션은 다음과 같습니다: 5GB, 10GB 또는 15GB. Note that the free version's storage (100 MB) is included in each of these plans.
