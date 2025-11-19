---
nav_title: 카탈로그 만들기
article_title: 카탈로그 만들기
alias: "/catalogs/"
page_order: 1
description: "이 참고 문서에서는 Liquid를 통해 Braze 캠페인에서 비사용자 데이터를 참조하는 카탈로그를 만드는 방법에 대해 설명합니다."
---

# 카탈로그 만들기

> 카탈로그를 만들려면 비사용자 데이터의 CSV 파일을 Braze로 가져와야 합니다. 그러면 해당 정보에 액세스하여 메시지를 더욱 풍부하게 만들 수 있습니다. 모든 유형의 데이터를 카탈로그로 가져올 수 있습니다. 이 데이터는 일반적으로 전자상거래 비즈니스의 제품 정보나 교육 제공업체의 강좌 정보와 같은 회사의 일종의 메타데이터입니다.

## 사용 사례

카탈로그의 일반적인 사용 사례는 다음과 같습니다:

- 제품
- 서비스
- 음식
- 예정된 이벤트
- 음악
- 패키지

이 정보를 가져온 후에는 Liquid를 통해 커스텀 속성 또는 커스텀 이벤트 속성에 액세스하는 것과 유사한 방식으로 메시지에서 해당 정보에 액세스할 수 있습니다.

## 카탈로그 만들기

카탈로그를 만들려면 **데이터 설정** > **카탈로그로** 이동한 다음 **새 카탈로그 만들기를** 선택하고 다음 옵션 중 하나를 선택합니다:

{% tabs local %}
{% tab Upload CSV %}
### 1단계: CSV 파일 검토하기

CSV 파일을 업로드하기 전에 CSV 파일이 다음 요구 사항을 충족하는지 확인하세요:

| CSV 요구 사항 | 세부 정보 |
|-----------------|---------|
| 헤더 | CSV 파일의 첫 번째 열 이름은 `id` 이어야 하며 각 행은 고유한 `id` 값을 가져야 합니다. |
| 열 | CSV 파일에는 최대 1,000개의 필드(열)를 포함할 수 있으며, 각 열 이름은 최대 250자까지 입력할 수 있습니다. |
| 파일 크기 | 무료 요금제의 경우 회사 전체에 걸친 모든 CSV 파일의 총 크기는 100MB로 제한됩니다. Pro 요금제의 경우 단일 CSV 파일의 최대 파일 크기는 2GB입니다. |
| 필드 값 | 각 셀(필드 값)에는 최대 5,000자까지 입력할 수 있습니다. |
| 유효한 문자 | `id` 열과 모든 헤더 값에는 문자, 숫자, 하이픈, 밑줄만 포함할 수 있습니다. |
| 데이터 유형 | CSV 파일 업로드에 지원되는 데이터 유형에는 문자열, 정수, 플로트, 부울 또는 날짜/시간이 있습니다. |
| 서식 지정 | 일관성을 유지하기 위해 모든 텍스트의 서식을 소문자로 지정합니다. |
| 인코딩 | UTF-8 인코딩을 사용하여 CSV 파일을 저장하고 업로드합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert note %}
CSV 파일을 저장할 공간이 더 필요하신가요? 카탈로그 업그레이드에 대한 자세한 내용은 Braze 계정 매니저에게 문의하세요.
{% endalert %}

### 2단계: CSV 업로드

파일을 업로드 영역으로 드래그 앤 드롭하거나 **CSV 업로드를** 선택하고 파일을 선택합니다.

\![]({% image_buster /assets/img_archive/catalog_CSV_upload.png %}){: style="max-width:80%;"}

각 열의 데이터 유형을 선택합니다.

{% alert note %}
이 데이터 유형은 카탈로그를 설정한 후에는 편집할 수 없습니다. 또한 `NULL` 값은 CSV 업로드에서 지원되지 않으며 문자열 값으로 처리됩니다.
{% endalert %}

\![]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:80%;"}

카탈로그의 이름과 설명(선택 사항)을 입력합니다. 카탈로그 이름을 지정할 때 다음 요구 사항을 염두에 두세요:

  - 고유해야 합니다.
  - 최대 250자
  - 숫자, 문자, 하이픈, 밑줄만 포함할 수 있습니다.

{% alert tip %}
[카탈로그 이름에 템플릿을 사용하여](#template-catalog-names) 언어나 캠페인과 같은 변수를 기반으로 카탈로그 이름을 동적으로 생성할 수도 있습니다.
{% endalert %}

\![ "my_catalog".]({% image_buster /assets/img_archive/in_browser_catalog.png %}라는 카탈로그){: style="max-width:80%;"}

**프로세스 카탈로그를** 선택하여 카탈로그를 생성합니다.

{% alert important %}
해당 [티어를](#tiers) 초과하는 경우 CSV 파일이 거부될 수 있습니다.
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
    <th class="tg-0pky">title</th>
    <th class="tg-0pky">가격</th>
    <th class="tg-0pky">image_link</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">1234</td>
    <td class="tg-0pky">Tales</td>
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

CSV 파일을 업로드하여 카탈로그를 생성합니다. `id`, `title`, `price`, `image_link` 의 데이터 유형은 각각 문자열, 문자열, 숫자, 문자열입니다. 

{% alert note %}
이 데이터 유형은 카탈로그를 설정한 후에는 편집할 수 없습니다.
{% endalert %}

\![네 개의 카탈로그 열 이름: "ID", "제목", "가격", "image_link".]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:85%;"}

다음으로 이 카탈로그의 이름을 "games_catalog" 으로 지정하고 **카탈로그 처리** 버튼을 선택합니다. 그런 다음 Braze는 카탈로그 생성 전에 카탈로그에 오류가 있는지 확인합니다.

\![ "games_catalog".]({% image_buster /assets/img_archive/catalog_new_name.png %}라는 카탈로그){: style="max-width:85%;"}

카탈로그가 생성된 후에는 이 이름을 편집할 수 없다는 점에 유의하세요. 카탈로그를 삭제하고 동일한 카탈로그 이름을 사용하여 업데이트된 버전을 다시 업로드할 수 있습니다.

카탈로그를 만든 후에는 [캠페인에서 카탈로그를]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/) 참조할 수 있습니다.
{% endtab %}

{% tab Create in browser %}
### 전제 조건

브라우저에서 카탈로그를 편집하거나 만들려면 먼저 **카탈로그 대시보드 관리** 권한이 필요합니다.

### 1단계: 카탈로그 세부 정보 입력

카탈로그의 이름과 설명(선택 사항)을 입력합니다. 카탈로그 이름을 지정할 때 다음 요구 사항을 염두에 두세요:

- 고유해야 합니다.
- 최대 250자
- 숫자, 문자, 하이픈, 밑줄만 포함할 수 있습니다.

{% alert tip %}
[카탈로그 이름에 템플릿을 사용하여](#template-catalog-names) 언어나 캠페인과 같은 변수를 기반으로 카탈로그 이름을 동적으로 생성할 수도 있습니다.
{% endalert %}

\![ "my_catalog".]({% image_buster /assets/img_archive/in_browser_catalog.png %}라는 카탈로그){: style="max-width:80%;"}

### 2단계: 카탈로그 만들기

목록에서 카탈로그를 선택한 다음 **카탈로그 업데이트** > **필드 추가를** 선택합니다. **필드 이름을** 입력하고 드롭다운을 사용하여 데이터 유형을 선택합니다. 필요에 따라 반복합니다.

!!\![두 개의 예제 필드 "등급" 및 "이름".]({% image_buster /assets/img_archive/add_catalog_fields.png %}){: style="max-width:50%;"}

**카탈로그 업데이트** > **항목 추가를** 선택하여 이전에 추가한 필드를 기반으로 정보를 입력하여 카탈로그에 항목을 추가합니다. 그런 다음 **항목 저장** 또는 **저장 후 다른** 항목 추가를 선택하여 항목을 계속 추가합니다.

\![카탈로그 항목 추가.]({% image_buster /assets/img_archive/add_catalog_items.png %}){: style="max-width:50%;"}

{% alert note %}
Braze는 대시보드 타임스탬프를 기준으로 시간 값을 처리합니다. 예를 들어 열의 값이 "03/13/2024"이고 표준 시간대가 태평양 표준 시간대인 경우 이 시간은 "Mar 12, 2024, 5:00 PM"으로 Braze에 가져올 수 있습니다.
{% endalert %}
{% endtab %}
{% endtabs %}

## 카탈로그 이름에 템플릿 사용 {#template-catalog-names}

카탈로그 이름을 지정할 때 카탈로그 이름에 템플릿을 사용할 수도 있습니다. 이를 통해 언어 또는 캠페인과 같은 변수를 기반으로 카탈로그 이름을 동적으로 생성할 수 있습니다. 예를 들어 다음을 사용할 수 있습니다:

{% raw %}
```liquid
{% assign language = "content_spanish" %}

{% catalog_items {{language}} fall_campaign %}
{{ items[0].body }}
```
{% endraw %}

## 카탈로그 관리

### 대시보드에서

CSV를 업로드하거나 브라우저에서 카탈로그를 생성한 후 카탈로그를 업데이트하려면 카탈로그 **업데이트 > CSV 업로드를** 선택한 다음 카탈로그의 항목을 업데이트, 추가 또는 삭제할지 여부를 선택합니다.

### REST API 사용하기

더 많은 카탈로그를 구축할 때 [목록 카탈로그 엔드포인트를]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) 사용하여 워크스페이스에 있는 카탈로그 목록을 반환할 수도 있습니다.

API 사용 시 지원되는 데이터 유형은 문자열, 정수, 플로트, 부울 또는 날짜/시간입니다. API로 카탈로그를 관리할 때 배열과 오브젝트를 업로드할 수도 있습니다.

## 카탈로그 항목 관리

카탈로그 관리 외에도 비동기 및 동기 엔드포인트를 사용하여 카탈로그 항목을 관리할 수도 있습니다. 여기에는 카탈로그 항목을 편집 및 삭제하고 카탈로그 항목 세부 정보를 나열하는 기능이 포함됩니다. 

예를 들어 개별 카탈로그 항목을 편집하려는 경우 [`/catalogs/catalog_name/items/item_id` 엔드포인트를]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/) 사용할 수 있습니다.

## 카탈로그 저장 {#tiers}

무료 버전의 카탈로그는 회사 전체에서 결합된 모든 CSV 파일에 대해 최대 100MB의 CSV 파일 크기를 지원하는 반면, Catalogs Pro 버전은 단일 CSV 파일에 대해 최대 2GB의 CSV 파일 크기를 지원합니다.

{% alert important %}
Braze 대시보드에 표시되는 패키지 자격은 시각적 편의를 위해 가장 가까운 단위로 반올림되었지만, 구매한 전체 자격은 그대로 사용할 수 있습니다. 카탈로그 저장 용량 업그레이드를 요청하려면 Braze 계정 매니저에게 문의하세요.
{% endalert %}

#### 무료 버전

무료 버전의 카탈로그 저장 용량은 최대 100MB입니다. 100MB 미만인 항목은 무제한으로 보관할 수 있습니다. 

#### 카탈로그 프로

회사 수준에서 Catalogs Pro의 최대 저장 용량은 카탈로그 데이터의 크기를 기준으로 합니다. 저장소 크기 옵션은 다음과 같습니다: 5GB, 10GB 또는 15GB. 각 요금제에는 무료 버전의 저장 용량(100MB)이 포함되어 있습니다.
