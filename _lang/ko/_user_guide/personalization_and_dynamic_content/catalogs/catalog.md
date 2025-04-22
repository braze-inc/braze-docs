---
nav_title: 카탈로그 만들기
article_title: 카탈로그 만들기
alias: "/catalogs/"
page_order: 1
description: "이 참고 문서에서는 Liquid를 통해 Braze 캠페인에서 비사용자 데이터를 참조하는 카탈로그를 만드는 방법을 설명합니다."
---

# 카탈로그 만들기

> 카탈로그를 만들려면 비사용자 데이터의 CSV 파일을 Braze로 가져와야 합니다. 그러면 해당 정보에 액세스하여 메시지를 더욱 풍부하게 만들 수 있습니다. 모든 유형의 데이터를 카탈로그로 가져올 수 있습니다. This data is typically some sort of metadata from your company such as product information for an eCommerce business, or course information for an education provider.<br><br>This page covers how to prepare and upload a CSV file to create a catalog, how to manage catalogs, and more.

Commons use cases for catalogs include:

- 제품
- 서비스
- 음식
- 예정된 이벤트
- 음악
- 패키지

After this information is imported, you can begin accessing it in messages in a similar way to accessing custom attributes or custom event properties through Liquid.

## CSV 파일 준비하기

카탈로그를 생성하기 전에 선호하는 카탈로그 생성 방법을 업로드하는 경우 CSV 파일을 준비해야 합니다.

{% alert note %}
CSV 파일을 저장할 공간이 더 필요하신가요? 카탈로그 업그레이드에 대한 자세한 내용은 Braze 계정 관리자에게 문의하세요.
{% endalert %}

### CSV 파일 가이드라인

CSV 파일을 만들 때 다음 가이드라인을 참고하세요. CSV 파일의 첫 번째 열은 `id`의 헤더여야 하며 각 항목의 `id`는 고유해야 합니다. 다른 모든 열 이름은 고유해야 합니다. 또한 카탈로그 CSV 파일에는 다음과 같은 제한 사항이 적용됩니다:

- 최대 1,000개 필드(열)
- 최대 250자의 필드(열) 이름
- 회사 전체에 걸쳐 모든 CSV 파일을 합쳐 최대 100MB(무료)
- 최대 CSV 파일 크기 2GB(Pro)
- 최대 필드 값(셀) 5,000자
- `id` 및 헤더 값에는 문자, 숫자, 하이픈, 밑줄만 사용할 수 있습니다.

또한 CSV 파일의 모든 텍스트 서식을 소문자로 지정하는 것이 좋습니다. 다음 단계에서 CSV 파일을 성공적으로 업로드하려면 UTF-8 형식을 사용하여 CSV 파일을 인코딩하고 있는지 확인하세요.

## 방법 선택

카탈로그를 만들려면 **데이터 설정** > **카탈로그로** 이동합니다.

**새 카탈로그 만들기**를 선택한 다음, **CSV 업로드** 또는 **브라우저에서 만들기**를 선택합니다.

### 방법 1: CSV 업로드

1. Drag and drop your file to the upload zone, or select **Upload CSV** and choose your file. <br>![][1]{: style="max-width:80%;"} <br><br>
2. 각 열에 대해 부울, 숫자, 문자열 또는 시간 중 하나의 데이터 유형을 선택합니다.
<br> ![][9]{: style="max-width:80%;"} <br><br>
3. 카탈로그에 이름을 지정합니다. 카탈로그 이름에 대한 다음 요구 사항을 염두에 두세요:
- 고유해야 합니다.
- 최대 250자
- 숫자, 문자, 하이픈, 밑줄만 포함할 수 있습니다.<br><br>
4. (선택 사항) 카탈로그에 대한 설명을 추가합니다.
5. Select **Process Catalog** to create the catalog.

{% alert note %}
이 데이터 유형은 카탈로그를 설정한 후에는 편집할 수 없습니다. 또한, CSV 업로드에서는 `NULL` 값이 지원되지 않으며 문자열로 처리됩니다.
{% endalert %}

카탈로그 이름에 템플릿을 사용할 수도 있습니다. 예를 들어 다음을 사용할 수 있습니다:
{% raw %}
```liquid
{% assign language = "content_spanish" %}

{% catalog_items {{language}} fall_campaign %}
{{ items[0].body }}
```
{% endraw %}

{% alert important %}
해당 [티어](#tiers)를 초과하는 경우 CSV 파일이 거부될 수 있습니다.
{% endalert %}

브라우저에서 카탈로그 생성을 선택한 후 CSV 파일을 업데이트할 수도 있습니다. Select **Update Catalog > Upload CSV**, then select whether to update, add, or delete items in your catalog.

### 방법 2: 브라우저에서 만들기

To edit or create catalogs in the browser, you'll need "Manage Catalogs Dashboard" permission.

1. 카탈로그의 이름을 입력합니다. 카탈로그 이름에 대한 다음 요구 사항을 염두에 두세요:
- 고유해야 합니다.
- 최대 250자
- 숫자, 문자, 하이픈, 밑줄만 포함할 수 있습니다. <br> ![내 카탈로그라는 이름의 "my_catalog".][14]{: style="max-width:80%;"} <br><br>
2. (선택 사항) 카탈로그에 대한 설명을 입력합니다.
3. 목록 **카탈로그** 페이지에서 방금 생성한 카탈로그를 선택하여 카탈로그를 업데이트합니다.
4. 선택 **업데이트 카탈로그** > **필드 추가**하여 필드를 추가합니다. 그런 다음 **필드 이름을** 입력하고 드롭다운을 사용하여 데이터 유형을 선택합니다. 필요에 따라 반복합니다.<br> ![두 개의 예시 필드 "평가"와 "이름".][12]{: style="max-width:50%;"}<br><br>
5. **카탈로그 업데이트** 선택 > **항목 추가**를 선택하여 이전에 추가한 필드를 기반으로 정보를 입력하여 카탈로그에 항목을 추가합니다. 그런 다음 **항목 저장** 또는 **저장 및 추가**를 선택하여 항목을 계속 추가합니다. <br> ![카탈로그 항목 추가.][13]{: style="max-width:50%;"}

브라우저에서 카탈로그 생성을 선택한 후 CSV 파일을 업로드할 수도 있습니다.

{% alert note %}
Braze는 대시보드 타임스탬프를 기반으로 시간 값을 처리합니다. 예를 들어 열의 값이 "03/13/2024"이고 시간대가 태평양 표준 시간대인 경우, 이 시간은 "2024년 3월 12일, 오후 5시"로 Braze에 가져올 수 있습니다.
{% endalert %}

#### 튜토리얼: CSV 파일에서 카탈로그 만들기

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

![네 개의 카탈로그 열 이름: "ID", "제목", "가격", "이미지_링크".][9]{: style="max-width:85%;"}

Next, we'll name this catalog "games_catalog" and select the **Process Catalog** button. 그러면 Braze는 카탈로그를 생성하기 전에 카탈로그에 오류가 있는지 확인합니다.

![게임 카탈로그 이름 "games_catalog".][11]{: style="max-width:85%;"}

카탈로그가 생성된 후에는 이 이름을 편집할 수 없다는 점에 유의하세요. 카탈로그를 삭제하고 동일한 카탈로그 이름을 사용하여 업데이트된 버전을 다시 업로드할 수 있습니다.

카탈로그를 생성한 후에는 [캠페인에서 카탈로그]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/using_catalogs/)를 참조할 수 있습니다.

## API를 통한 카탈로그 관리

더 많은 카탈로그를 구축할 때 [목록 카탈로그 엔드포인트를]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) 사용하여 워크스페이스에 있는 카탈로그 목록을 반환할 수도 있습니다.

### 카탈로그 항목 관리

카탈로그를 관리하는 것 외에도 비동기 및 동기 엔드포인트를 사용하여 카탈로그 항목을 관리할 수도 있습니다. 여기에는 카탈로그 항목을 편집 및 삭제하고 카탈로그 항목 세부 정보를 나열하는 기능이 포함됩니다. 

예를 들어 개별 카탈로그 항목을 편집하려는 경우 [`/catalogs/catalog_name/items/item_id` 엔드포인트]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/)를 사용할 수 있습니다.

## 카탈로그 계층 {#tiers}

The free version of catalogs supports CSV file sizes of up to 100 MB for all CSV files combined across your company, whereas the Catalogs Pro version supports CSV file sizes of up to 2 GB for a single CSV file.

### 카탈로그 저장

{% alert important %}
Braze 대시보드에 표시되는 패키지 자격은 시각적 편의를 위해 가장 가까운 단위로 반올림되었지만, 구매하신 전체 자격은 계속 이용하실 수 있습니다. 카탈로그 저장소 업그레이드를 요청하려면 Braze 계정 관리자에게 문의하세요.
{% endalert %}

#### 무료 버전

무료 버전의 카탈로그 저장 용량은 최대 100MB입니다. 100MB 미만인 경우 무제한으로 항목을 보유할 수 있습니다. 선택 항목은 스토리지에 기여합니다. 선택 항목이 복잡할수록 더 많은 스토리지를 차지하게 됩니다. CSV 카탈로그 데이터와 우리 데이터 저장소에서 해당 데이터의 표현 간에도 크기 불일치가 있을 것입니다.

#### 카탈로그 프로

회사 수준에서 카탈로그 프로의 최대 저장 용량은 카탈로그 데이터의 크기에 따라 결정됩니다. 스토리지 크기 옵션은 다음과 같습니다: 5GB, 10GB 또는 15GB. 각 요금제에는 무료 버전의 저장 용량(100MB)이 포함되어 있습니다.

[1]: {% image_buster /assets/img_archive/catalog_CSV_upload.png %}
[5]: {% image_buster /assets/img_archive/catalog_CSV_example.png %}
[7]: {% image_buster /assets/img_archive/create_catalog_option.png %}
[9]: {% image_buster /assets/img_archive/catalog_data_type.png %}
[11]: {% image_buster /assets/img_archive/catalog_new_name.png %}
[12]: {% image_buster /assets/img_archive/add_catalog_fields.png %}
[13]: {% image_buster /assets/img_archive/add_catalog_items.png %}
[14]: {% image_buster /assets/img_archive/in_browser_catalog.png %}
