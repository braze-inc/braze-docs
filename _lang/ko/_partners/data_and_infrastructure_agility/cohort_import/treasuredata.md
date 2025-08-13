---
nav_title: Treasure Data
article_title: Treasure Data 코호트 가져오기
description: "이 참조 문서에서는 Treasure Data의 코호트 가져오기 기능을 간략히 설명합니다."
page_type: partner
search_tag: Partner

---
# Treasure Data 코호트 가져오기

> 이 문서에서는 Treasure Data에서 Braze로 사용자 코호트를 가져와서 창고에만 존재할 수 있는 데이터를 기반으로 타겟 캠페인을 보낼 수 있는 방법을 설명합니다.

{% alert important %}
이 기능은 현재 베타 버전입니다. 자세한 내용은 Treasure Data 및 Braze 담당자에게 문의합니다.
{% endalert %}

## 전제 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Treasure Data 계정 | 이 파트너십을 활용하려면 [Treasure Data](https://www.treasuredata.com/) 계정이 필요합니다. |
| Braze 데이터 가져오기 키 | This can be captured in the Braze dashboard from **Partner Integrations** > **Technology Partners** and then select **Treasure Data**. |
| Braze REST 엔드포인트 | [당신의 REST 엔드포인트 URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). 사용자의 엔드포인트는 인스턴스를 위한 Braze URL에 따라 달라집니다. |
| Treasure Data의 정적 IP 주소 | Treasure Data의 정적 IP 주소는 이 통합을 위한 액세스 지점이자 출처입니다. 정적 IP 주소를 확인하려면 Treasure Data 고객 성공 담당자 또는 Treasure Data 기술 지원에 문의합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 데이터 가져오기 통합

### 1단계: Braze 데이터 가져오기 키 가져오기

Braze에서 **파트너 통합** > **기술 파트너**로 이동하여 **Treasure Data**를 선택합니다. 여기에서 REST 엔드포인트를 찾아 Braze 데이터 가져오기 키를 생성합니다. 키가 생성된 후에는 새 키를 생성하거나 기존 키를 무효화할 수 있습니다.

### 2단계: 데이터 연결 생성

Treasure Data 내에서 데이터 연결을 생성하기 전에 인증해야 합니다. 먼저 **통합 허브**을 선택한 다음 **카탈로그**를 선택합니다.

![Treasure Data 통합 허브 카탈로그]({% image_buster /assets/img/treasure_data/cohort/cohort1.png %}) 

**카탈로그**에서 Braze 통합을 검색한 다음 아이콘 위로 마우스를 이동하고 **인증 생성**을 선택합니다. 자격 증명을 입력하고 인증에 이름을 지정한 다음 **완료**를 선택하십시오.

![Treasure Data 통합 허브 카탈로그]({% image_buster /assets/img/treasure_data/cohort/cohort2.png %}) 

### 3단계: 코호트 오디언스 정의

**Audience Studio** 또는 **데이터 워크벤치**에서 쿼리를 실행하여 Braze에 코호트를 동기화합니다.

{% alert important %}
Braze 내에 이미 존재하는 사용자만 코호트에 추가되거나 제거됩니다. 코호트 가져오기는 Braze에서 새로운 사용자를 생성하지 않습니다.
{% endalert %}

{% tabs local %}
{% tab Data Workbench %}
#### 3.1단계: 쿼리 정의

{% alert note %}
쿼리 열은 정확한 열 이름과 데이터 유형으로 지정해야 합니다. 쿼리 열은 `user_ids`, `device_ids` 중 하나 이상의 열을 포함해야 합니다. 또는 UI의 구성과 일치하는 braze 별칭 열을 포함해야 합니다. Braze 내에 존재하는 사용자 프로필만 코호트에 추가됩니다. 코호트 가져오기는 새로운 사용자 프로필을 생성하지 않습니다.
{% endalert %}

1. **데이터 워크벤치** > **쿼리**로 이동합니다.
2. **새 쿼리**를 선택하십시오.
3. 쿼리를 실행하여 결과 집합을 검증합니다.

![Treasure Data 통합 허브 카탈로그]({% image_buster /assets/img/treasure_data/cohort/cohort3.png %})

##### 사용 사례: 식별자로 코호트 동기화

{% subtabs local %}
{% subtab Syncing External IDs %}
다음은 Treasure Data의 예제 테이블입니다.

| external_id |	이메일	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |

{% alert warning %}
열 이름은 `user_ids`이어야 동기화가 실패하지 않습니다.
{% endalert %}

외부 ID를 사용하여 코호트를 동기화하려면 다음 쿼리를 실행하십시오:

```sql
SELECT
  external_id as user_ids
FROM
  example_cohort_table
```

쿼리를 실행한 후, 이러한 사용자 별칭이 Braze의 코호트에 추가됩니다.

 - `TDCohort1`
 - `TDCohort2`
 - `TDCohort3`
 - `TDCohort4`
{% endsubtab %}

{% subtab Syncing User Aliases %}
다음은 Treasure Data의 예제 테이블입니다.

| external_id |	이메일	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |

사용자 별칭을 사용하여 코호트를 동기화하려면 다음 쿼리를 실행하십시오:

```sql
SELECT
  email
FROM
  example_cohort_table
```

쿼리를 실행한 후, 이러한 사용자 별칭이 Braze의 코호트에 추가됩니다.

 - `"alias_label":"email", "alias_name":"TDCohort1@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort2@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort3@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort4@gmail.com"`
{% endsubtab %}

{% subtab Syncing Device IDs %}
다음은 Treasure Data의 예제 테이블입니다.

| external_id |	이메일	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |

{% alert warning %}
열 이름은 `device_ids`이어야 동기화가 실패하지 않습니다.
{% endalert %}

기기 ID를 사용하여 코호트를 동기화하려면 다음 쿼리를 실행하십시오:

```sql
SELECT
  device_ids
FROM
  example_cohort_table
```

쿼리를 실행한 후, 이러한 기기 ID가 Braze의 코호트에 추가됩니다.

- `1a2b3c`
- `4d5f6g`
- `7h8j9k`
- `1ab2cd`
{% endsubtab %}
{% endsubtabs %}

#### 3.2단계: 결과 내보내기 대상을 지정하십시오

쿼리가 생성되면 **결과 내보내기**를 선택합니다. 기존 인증(마지막 단계에서 선택한 인증)을 선택하거나 출력을 위해 사용할 새 인증을 생성할 수 있습니다. 

![Treasure Data 통합 허브 카탈로그]({% image_buster /assets/img/treasure_data/cohort/cohort5.png %}) 


| 결과 매핑 내보내기 |	설명	| 
| ----------- | ----------- |
| 코호트 ID	| 이것은 Braze로 전송될 백엔드 코호트 식별자입니다. 	|
| 코호트 이름 (선택 사항)	| Braze 세분화 툴의 코호트 필터 내에 나타나는 이름입니다. 이것이 설정되지 않으면 `Cohort ID`이(가) `Cohort Name`으로(로) 사용됩니다.	|
| 작업	| 쿼리가 Braze의 코호트에서 프로필을 추가하거나 제거해야 하는지 여부를 결정하는 데 사용됩니다.	| 
| 별명 (선택 사항) | 정의되면 쿼리 내 해당 열의 이름이 `alias_label`로 전송되고, 열에서 각 행의 값이 `alias_name`으로 전송됩니다.	| 
| 스레드 수 | 동시 API 호출 수. |

[Treasure Data의 단계](https://docs.treasuredata.com/articles/#!int/braze-cohort-export-integration/a/ExportIntegrationTemplate-SpecifytheResultExportTarget)를 따라 사용 사례에 맞게 내보내기를 구성합니다.

#### 3.3단계: 쿼리를 실행하십시오

쿼리를 이름으로 저장하고 실행하거나, 그냥 쿼리를 실행하십시오. 쿼리가 성공적으로 완료되면 쿼리 결과가 자동으로 Braze로 내보내집니다.

{% endtab %}
{% tab 오디언스 Studio %}
#### 3.1단계: 활성화 만들기

새 세그먼트를 만들거나 기존 세그먼트를 선택하여 Braze에 코호트로 동기화합니다. 세그먼트 내에서 **활성화 만들기**를 선택하십시오.

#### 3.2단계: 활성화 세부 정보를 작성합니다

![Treasure Data 통합 활성화 세부 정보]({% image_buster /assets/img/treasure_data/cohort/cohort7.png %}) 

| 활성화 세부 설정 |	설명	| 
| ----------- | ----------- |
| 활성화 이름	| 활성화 이름.	|
| 활성화 설명| 활성화에 대한 간략한 설명.	|
| 인증	| 2단계에서 생성된 Braze 코호트 인증을 선택합니다.	| 
| 코호트 ID	| 이것은 Braze로 전송될 백엔드 코호트 식별자입니다. 	|
| 코호트 이름 (선택 사항)	| Braze 세분화 툴의 코호트 필터 내에 나타나는 이름입니다. 이것이 설정되지 않으면 `Cohort ID`이(가) `Cohort Name`으로(로) 사용됩니다.	|
| 작업	| 쿼리가 Braze의 코호트에서 프로필을 추가하거나 제거해야 하는지 여부를 결정하는 데 사용됩니다.	| 
| 별명 (선택 사항) | 정의되면 쿼리 내 해당 열의 이름이 `alias_label`로 전송되고, 열에서 각 행의 값이 `alias_name`으로 전송됩니다.	| 
| 스레드 수 | 동시 API 호출 수. |

#### 3.3단계: 출력 매핑 설정

![Treasure Data 통합 활성화 출력 매핑]({% image_buster /assets/img/treasure_data/cohort/cohort6.png %}) 

| 활성화 출력 매핑 |	설명	| 
| ----------- | ----------- |
| 속성 열	| 세그먼트 데이터베이스에서 프로필을 Braze 코호트에 동기화할 때 식별자로 매핑될 열을 결정합니다.	|
| 문자열 빌더| 문자열 빌더는 Braze 통합에 필요하지 않습니다.	|

{% alert important %}
 - `device_id`을(를) 식별자로 사용할 때, **출력 열 이름**은(는) `device_ids`으로 명명되어야 합니다.
 - 식별자로 별칭을 사용하는 경우 **출력 열 이름**은 해당 열 이름이어야 하며, 쿼리 내 해당 열의 이름이 `alias_label`로 전송되고, 열에서 각 행의 값이 `alias_name`으로 전송됩니다.
 - `external_id`을(를) 식별자로 사용할 때, **출력 열 이름**은(는) `user_ids`으로 명명되어야 합니다.
{% endalert %}

모든 관련이 없거나 잘못된 이름의 열 이름은 무시됩니다. 동기화에서 둘 이상의 식별자를 사용할 수 있습니다.

#### 3.4 단계: 활성화 스케줄 정의

원하는 동기화 일정을 정의하고 활성화를 저장하십시오.

![Treasure Data 통합 활성화 스케줄]({% image_buster /assets/img/treasure_data/cohort/cohort8.png %})
{% endtab %}
{% endtabs %}

### 4단계: Treasure Data 내보내기에서 Braze 세그먼트 생성

Braze에서 **세그먼트**로 이동하고 새 세그먼트를 생성한 후 **Treasure Data 코호트**를 필터로 선택합니다. 여기에서 포함할 Treasure Data 코호트를 선택할 수 있습니다. Treasure Data 코호트 세그먼트가 생성된 후 캠페인 또는 캔버스를 생성할 때 오디언스 필터로 선택할 수 있습니다.

![Treasure Data 통합 허브 카탈로그]({% image_buster /assets/img/treasure_data/cohort/cohort4.png %}) 

## 사용자 일치

식별된 사용자는 `external_id` 또는 `alias`로 일치할 수 있습니다. 익명 사용자는 `device_id`로 매칭될 수 있습니다. 익명 사용자로 처음 생성된 식별된 사용자는 `device_id`로 식별할 수 없으며, `external_id` 또는 `alias`로 식별해야 합니다.
