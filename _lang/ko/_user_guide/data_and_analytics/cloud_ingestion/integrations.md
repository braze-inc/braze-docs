---
nav_title: 데이터 웨어하우스 통합
article_title: 데이터 웨어하우스 통합
description: "이 참조 문서에서는 Braze Cloud 데이터 수집을 사용하여 관련 데이터를 Snowflake, Redshift, BigQuery 및 Databricks 통합과 동기화하는 방법을 다룹니다."
page_order: 2
page_type: reference

---

# 데이터 웨어하우스 스토리지 통합

> 이 문서에서는 Braze Cloud 데이터 수집(CDI)을 사용하여 관련 데이터를 Snowflake, Redshift, BigQuery 및 Databricks 통합과 동기화하는 방법을 다룹니다.

## 제품 설정

클라우드 데이터 수집 통합은 Braze 측과 귀하의 인스턴스에서 일부 설정이 필요합니다. 다음 단계를 따라 통합을 설정하십시오:

{% tabs %}
{% tab Snowflake %}
1. Snowflake 인스턴스에서 Braze와 동기화하려는 테이블 또는 뷰를 설정하십시오.
2. Braze 대시보드에서 새 통합을 생성합니다.
3. Braze 대시보드에 제공된 공개 키를 검색하고 [Snowflake 사용자에게 인증을 위해 추가합니다](https://docs.snowflake.com/en/user-guide/key-pair-auth.html).
4. 통합을 테스트하고 동기화를 시작하십시오.
{% endtab %}
{% tab Redshift %}
1. Redshift 테이블과 동기화하려는 Braze 액세스가 허용되었는지 확인하십시오. Braze는 인터넷을 통해 Redshift에 연결됩니다.
2. Redshift 인스턴스에서 Braze와 동기화하려는 테이블 또는 뷰를 설정하십시오.
3. Braze 대시보드에서 새 통합을 생성합니다.
4. 통합을 테스트하고 동기화를 시작하십시오.
{% endtab %}
{% tab BigQuery %}
1. 서비스 계정을 만들고 동기화하려는 데이터가 포함된 BigQuery 프로젝트 및 데이터 세트에 대한 액세스를 허용합니다.  
2. BigQuery 계정에서 Braze와 동기화하려는 테이블 또는 뷰를 설정합니다.   
3. Braze 대시보드에서 새 통합을 생성합니다.  
4. 통합을 테스트하고 동기화를 시작하십시오.  
{% endtab %}
{% tab Databricks %}
1. 서비스 계정을 만들고 동기화하려는 데이터를 포함하는 Databricks 프로젝트 및 데이터 세트에 대한 액세스를 허용합니다.  
2. Databricks 계정에서 Braze와 동기화하려는 테이블 또는 뷰를 설정하세요.   
3. Braze 대시보드에서 새 통합을 생성합니다.  
4. 통합을 테스트하고 동기화를 시작하십시오.

{% alert important %}
Braze가 Classic 및 Pro SQL 인스턴스에 연결될 때 연결 설정 및 테스트 중뿐만 아니라 예약된 동기화 시작 시에도 지연을 초래하는 2~5분의 준비 시간이 있을 수 있습니다. 서버리스 SQL 인스턴스를 사용하면 워밍업 시간을 최소화하고 쿼리 처리량을 향상시킬 수 있지만, 통합 비용이 약간 증가할 수 있습니다.
{% endalert %}

{% endtab %}
{% endtabs %}

### 1단계: 테이블 또는 뷰 설정

{% tabs %}
{% tab Snowflake %}

#### 1단계: 테이블을 설정하세요

```json
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     --at least one of external_id, alias_name and alias_label, email, phone, or braze_id is required  
     EXTERNAL_ID VARCHAR(16777216),
     --if using user alias, both alias_name and alias_label are required
     ALIAS_LABEL VARCHAR(16777216),
     ALIAS_NAME VARCHAR(16777216),
     --braze_id can only be used to update existing users created through the Braze SDK
     BRAZE_ID VARCHAR(16777216),
     --If you include both email and phone, we will use the email as the primary identifier
     EMAIL VARCHAR(16777216),
     PHONE VARCHAR(16777216),
     PAYLOAD VARCHAR(16777216) NOT NULL
);
```

데이터베이스, 스키마 및 테이블의 이름은 원하는 대로 지정할 수 있지만, 열 이름은 앞서 정의한 것과 일치해야 합니다.

- `UPDATED_AT` - 이 행이 테이블에 업데이트되거나 추가된 시간. 우리는 마지막 동기화 이후에 추가되거나 업데이트된 행만 동기화할 것입니다.
- **사용자 식별자 열** \- 테이블에는 하나 이상의 사용자 식별자 열이 포함될 수 있습니다. 각 행에는 하나의 식별자(`external_id`, `alias_name`과 `alias_label`의 조합 또는 `braze_id` 중 하나)만 포함되어야 합니다. 소스 테이블에는 하나, 둘 또는 세 가지 식별자 유형에 대한 열이 있을 수 있습니다. 
    - `EXTERNAL_ID` - 업데이트하려는 사용자를 식별합니다. 이 값은 Braze에서 사용하는 `external_id` 값과 일치해야 합니다. 
    - `ALIAS_NAME` 및 `ALIAS_LABEL` \- 이 두 열은 사용자 별칭 개체를 만듭니다. `alias_name`은 고유 식별자이고 `alias_label`은 별칭의 유형을 지정합니다. 사용자는 여러 레이블이 있는 여러 별칭을 가질 수 있지만 `alias_label`당 하나의 `alias_name`만 가질 수 있습니다.
    - `BRAZE_ID` - Braze 사용자 식별자입니다. 이것은 Braze SDK에 의해 생성되었으며, 새로운 사용자는 Braze ID를 통해 클라우드 데이터 수집을 사용하여 생성될 수 없습니다. 새 사용자를 만들려면 외부 사용자 ID 또는 사용자 별칭을 지정합니다.
    - `EMAIL` - 사용자의 이메일 주소. 동일한 이메일 주소를 가진 여러 프로필이 존재하는 경우, 가장 최근에 업데이트된 프로필이 업데이트 우선순위가 됩니다. 이메일과 전화번호를 모두 포함하면 이메일을 기본 식별자로 사용하겠습니다.
    - `PHONE` - 사용자의 전화번호입니다. 동일한 전화번호를 가진 여러 프로필이 존재하는 경우, 가장 최근에 업데이트된 프로필이 업데이트에 우선됩니다. 
- `PAYLOAD` - 이것은 Braze에서 사용자와 동기화하려는 필드의 JSON 문자열입니다.

#### 2단계: 역할 및 데이터베이스 권한 설정

```json
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;
```

이름을 필요에 따라 업데이트하지만 권한은 이전 예와 일치해야 합니다.

#### 3단계: 웨어하우스를 설정하고 Braze 역할에 액세스 권한을 부여하세요.

```json
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
창고에는 **자동 재개** 플래그가 켜져 있어야 합니다. 그렇지 않으면, 쿼리를 실행할 때 이를 켜기 위해 웨어하우스에 대한 추가 `OPERATE` 권한을 Braze에 부여해야 합니다.
{% endalert %}

#### 4단계: 사용자를 설정하세요.

```json
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

이 단계를 완료한 후 Braze와 연결 정보를 공유하고 사용자에게 추가할 공개 키를 받게 됩니다.

{% alert note %}
다른 워크스페이스를 동일한 Snowflake 계정에 연결할 때, 통합을 생성하는 각 Braze 워크스페이스에 고유한 사용자를 생성해야 합니다. 워크스페이스 내에서 동일한 사용자를 통합 간에 재사용할 수 있지만, 동일한 Snowflake 계정의 사용자가 워크스페이스 간에 중복되면 통합 생성이 실패합니다.
{% endalert %}

#### 5단계: Snowflake 네트워크 정책에서 Braze IP 허용(선택 사항)

Snowflake 계정의 구성에 따라 Snowflake 네트워크 정책에서 다음 IP 주소를 허용해야 할 수 있습니다. 자세한 내용은 [네트워크 정책 수정](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies)에 대한 관련 Snowflake 설명서를 참조하세요.

| 예: `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`, `US-07` | 인스턴스 `EU-01` 및 `EU-02`의 경우 |
|---|---|
| `23.21.118.191`| `52.58.142.242`
| `34.206.23.173`| `52.29.193.121`
| `50.16.249.9`| `35.158.29.228`
| `52.4.160.214`| `18.157.135.97`
| `54.87.8.34`| `3.123.166.46`
| `54.156.35.251`| `3.64.27.36`
| `52.54.89.238`| `3.65.88.25`
| `18.205.178.15`| `3.68.144.188`
|   | `3.70.107.88`
{% endtab %}
{% tab Redshift %}

#### 1단계: 테이블을 설정하세요 

선택적으로 소스 테이블을 보유할 새 데이터베이스 및 스키마를 설정하세요
```json
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```
CDI 통합에 사용할 테이블(또는 뷰)을 만드십시오
```json
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
   updated_at timestamptz default sysdate,
   --at least one of external_id, alias_name and alias_label, or braze_id is required
   external_id varchar,
   --if using user alias, both alias_name and alias_label are required
   alias_label varchar,
   alias_name varchar,
   --braze_id can only be used to update existing users created through the Braze SDK
   braze_id varchar,
   --If you include both email and phone, we will use the email as the primary identifier
   email varchar,
   phone varchar,
   payload varchar(max)
)
```

데이터베이스, 스키마 및 테이블의 이름은 원하는 대로 지정할 수 있지만, 열 이름은 앞서 정의한 것과 일치해야 합니다.

- `UPDATED_AT` - 이 행이 테이블에 업데이트되거나 추가된 시간. 우리는 마지막 동기화 이후에 추가되거나 업데이트된 행만 동기화할 것입니다.
- 사용자 식별자 열. 테이블에 하나 이상의 사용자 식별자 열이 포함될 수 있습니다. 각 행에는 하나의 식별자( `external_id`, `alias_name`과 `alias_label`의 조합 또는 `braze_id`)만 포함되어야 합니다. 소스 테이블에는 하나, 둘 또는 세 가지 식별자 유형에 대한 열이 있을 수 있습니다. 
    - `EXTERNAL_ID` - 업데이트하려는 사용자를 식별합니다. 이 값은 Braze에서 사용하는 `external_id` 값과 일치해야 합니다. 
    - `ALIAS_NAME` 및 `ALIAS_LABEL` \- 이 두 열은 사용자 별칭 개체를 만듭니다. `alias_name`은 고유 식별자이고 `alias_label`은 별칭의 유형을 지정합니다. 사용자는 여러 레이블이 있는 여러 별칭을 가질 수 있지만 `alias_label`당 하나의 `alias_name`만 가질 수 있습니다.
    - `BRAZE_ID` - Braze 사용자 식별자입니다. 이것은 Braze SDK에 의해 생성되었으며, 새로운 사용자는 Braze ID를 통해 클라우드 데이터 수집을 사용하여 생성될 수 없습니다. 새 사용자를 만들려면 외부 사용자 ID 또는 사용자 별칭을 지정합니다.
    - `EMAIL` - 사용자의 이메일 주소. 동일한 이메일 주소를 가진 여러 프로필이 존재하는 경우, 가장 최근에 업데이트된 프로필이 업데이트 우선순위가 됩니다. 이메일과 전화번호를 모두 포함하면 이메일을 기본 식별자로 사용하겠습니다.
    - `PHONE` - 사용자의 전화번호입니다. 동일한 전화번호를 가진 여러 프로필이 존재하는 경우, 가장 최근에 업데이트된 프로필이 업데이트에 우선됩니다. 
- `PAYLOAD` - 이것은 Braze에서 사용자와 동기화하려는 필드의 JSON 문자열입니다.
 
#### 2단계: 사용자를 생성하고 권한을 부여하십시오 

```json
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

이 사용자를 위한 최소한의 권한입니다. 여러 CDI 통합을 생성하는 경우 스키마에 대한 권한을 부여하거나 그룹을 사용하여 권한을 관리할 수 있습니다. 

#### 3단계: Braze IP에 대한 액세스 허용

방화벽이나 기타 네트워크 정책이 있는 경우 Braze 네트워크에 Redshift 인스턴스에 대한 액세스 권한을 부여해야 합니다. Redshift URL 엔드포인트의 예는 "example-cluster.ap-northeast-2.redshift.amazonaws.com"입니다.

알아야 할 중요한 사항들:
- Braze가 Redshift에서 데이터에 액세스할 수 있도록 보안 그룹을 변경해야 할 수도 있습니다.
- IP 테이블과 Redshift 클러스터를 쿼리하는 데 사용되는 포트(기본값은 5439)에서 인바운드 트래픽을 명시적으로 허용해야 합니다. 이 포트에서 Redshift TCP 연결을 명시적으로 허용해야 합니다. 수신 규칙이 "모두 허용"으로 설정되어 있더라도.
- Braze가 클러스터에 연결할 수 있도록 Redshift 클러스터의 엔드포인트는 공개적으로 접근 가능해야 합니다.
     - Redshift 클러스터가 공개적으로 액세스할 수 없도록 하려면 VPC와 EC2 인스턴스를 설정하여 SSH 터널을 사용하여 Redshift 데이터에 액세스할 수 있습니다. 이 [AWS 지식 센터 게시물](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine)을 확인하여 자세한 정보를 확인하세요.
 
다음 IP에서 Braze 대시보드의 지역에 해당하는 액세스를 허용합니다.

| 예: `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`, `US-07` | 인스턴스 `EU-01` 및 `EU-02`의 경우 |
|---|---|
| `23.21.118.191`| `52.58.142.242`
| `34.206.23.173`| `52.29.193.121`
| `50.16.249.9`| `35.158.29.228`
| `52.4.160.214`| `18.157.135.97`
| `54.87.8.34`| `3.123.166.46`
| `54.156.35.251`| `3.64.27.36`
| `52.54.89.238`| `3.65.88.25`
| `18.205.178.15`| `3.68.144.188`
|   | `3.70.107.88`
{% endtab %}
{% tab BigQuery %}

#### 1단계: 테이블을 설정하세요 

선택적으로 소스 테이블을 보유할 새 프로젝트 또는 데이터 세트를 설정합니다.

```json
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

다음 필드를 사용하여 CDI 통합에 사용할 하나 이상의 테이블을 만드세요.

```json
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  --At least one of external_id, alias_name and alias_label, or braze_id is required  
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  --braze_id can only be used to update existing users created through the Braze SDK
  braze_id STRING,
  --If you include both email and phone, we will use the email as the primary identifier
  email STRING,
  phone STRING,
  payload JSON
);
```

| 필드 이름 | 유형 | 모드 |
|---|---|---|
| `UPDATED_AT`| 타임스탬프 | 필수 |
| `PAYLOAD`| JSON | 필수 |
| `EXTERNAL_ID`| 문자열 | NULLABLE |
| `ALIAS_NAME`| 문자열 | NULLABLE |
| `ALIAS_LABEL`| 문자열 | NULLABLE |
| `BRAZE_ID`| 문자열 | NULLABLE |
| `EMAIL`| 문자열 | NULLABLE |
| `PHONE`| 문자열 | NULLABLE |

프로젝트, 데이터셋 및 테이블의 이름은 원하는 대로 지정할 수 있지만, 열 이름은 앞서 정의한 것과 일치해야 합니다.

- `UPDATED_AT` - 이 행이 테이블에 업데이트되거나 추가된 시간. 우리는 마지막 동기화 이후에 추가되거나 업데이트된 행만 동기화할 것입니다.
- 사용자 식별자 열. 테이블에 하나 이상의 사용자 식별자 열이 포함될 수 있습니다. 각 행에는 하나의 식별자(`external_id`, `alias_name`과 `alias_label`의 조합 또는 `braze_id` 중 하나)만 포함되어야 합니다. 소스 테이블에는 하나, 둘 또는 세 가지 식별자 유형에 대한 열이 있을 수 있습니다. 
    - `EXTERNAL_ID` - 업데이트하려는 사용자를 식별합니다. 이 값은 Braze에서 사용하는 `external_id` 값과 일치해야 합니다. 
    - `ALIAS_NAME` 및 `ALIAS_LABEL` \- 이 두 열은 사용자 별칭 개체를 만듭니다. `alias_name`은 고유 식별자이고 `alias_label`은 별칭의 유형을 지정합니다. 사용자는 여러 레이블이 있는 여러 별칭을 가질 수 있지만 `alias_label`당 하나의 `alias_name`만 가질 수 있습니다.
    - `BRAZE_ID` - Braze 사용자 식별자입니다. 이것은 Braze SDK에 의해 생성되었으며, 새로운 사용자는 Braze ID를 통해 클라우드 데이터 수집을 사용하여 생성될 수 없습니다. 새 사용자를 만들려면 외부 사용자 ID 또는 사용자 별칭을 지정합니다.
    - `EMAIL` - 사용자의 이메일 주소. 동일한 이메일 주소를 가진 여러 프로필이 존재하는 경우, 가장 최근에 업데이트된 프로필이 업데이트 우선순위가 됩니다. 이메일과 전화번호를 모두 포함하면 이메일을 기본 식별자로 사용하겠습니다.
    - `PHONE` - 사용자의 전화번호입니다. 동일한 전화번호를 가진 여러 프로필이 존재하는 경우, 가장 최근에 업데이트된 프로필이 업데이트에 우선됩니다.
   이메일 varchar,
   phone_number varchar,
- `PAYLOAD` - 이것은 Braze에서 사용자와 동기화하려는 필드의 JSON 문자열입니다.

#### 2단계: 서비스 계정을 만들고 권한을 부여하십시오 

GCP에서 Braze가 테이블에서 데이터를 연결하고 읽을 수 있도록 서비스 계정을 만드세요. 서비스 계정에는 아래 권한이 있어야 합니다: 

- **BigQuery 연결 사용자:** 이것은 Braze가 연결을 만들 수 있게 해줍니다
- **BigQuery 사용자:** 이를 통해 Braze는 쿼리를 실행하고, 데이터셋 메타데이터를 읽고, 테이블을 나열할 수 있습니다.
- **BigQuery 데이터 Viewer:** 이렇게 하면 Braze가 데이터 세트와 그 내용을 볼 수 있는 접근 권한을 제공합니다.
- **BigQuery 작업 사용자:** 이렇게 하면 Braze에 작업을 실행할 수 있는 권한이 부여됩니다

서비스 계정을 생성하고 권한을 부여한 후, JSON 키를 생성합니다. 자세한 내용은 [여기](https://cloud.google.com/iam/docs/keys-create-delete)에서 확인하세요. 나중에 Braze 대시보드로 업데이트할 것입니다. 

#### 3단계: Braze IP에 대한 액세스 허용    

네트워크 정책이 있는 경우 Braze 네트워크에 Big Query 인스턴스에 대한 액세스 권한을 부여해야 합니다. 아래 IP에서 Braze 대시보드의 지역에 해당하는 액세스를 허용합니다.  

| 예: `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`, `US-07` | 인스턴스 `EU-01` 및 `EU-02`의 경우 |
|---|---|
| `23.21.118.191`| `52.58.142.242`
| `34.206.23.173`| `52.29.193.121`
| `50.16.249.9`| `35.158.29.228`
| `52.4.160.214`| `18.157.135.97`
| `54.87.8.34`| `3.123.166.46`
| `54.156.35.251`| `3.64.27.36`
| `52.54.89.238`| `3.65.88.25`
| `18.205.178.15`| `3.68.144.188`
|   | `3.70.107.88`

{% endtab %}
{% tab Databricks %}

#### 1단계: 테이블을 설정하세요 

선택적으로 소스 테이블을 보유할 새 카탈로그 또는 스키마를 설정하십시오.

```json
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

다음 필드를 사용하여 CDI 통합에 사용할 하나 이상의 테이블을 만드세요.


```json
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp(),
  --At least one of external_id, alias_name and alias_label, or braze_id is required  
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  --braze_id can only be used to update existing users created through the Braze SDK
  braze_id STRING,
  --If you include both email and phone, we will use the email as the primary identifier
  email STRING,
  phone STRING,
  payload STRING
);
```


| 필드 이름 | 유형 | 모드 |
|---|---|---|
| `UPDATED_AT`| 타임스탬프 | 필수 |
| `PAYLOAD`| 문자열 또는 구조체 | 필수 |
| `EXTERNAL_ID`| 문자열 | NULLABLE |
| `ALIAS_NAME`| 문자열 | NULLABLE |
| `ALIAS_LABEL`| 문자열 | NULLABLE |
| `BRAZE_ID`| 문자열 | NULLABLE |
| `EMAIL`| 문자열 | NULLABLE |
| `PHONE`| 문자열 | NULLABLE |

스키마와 테이블의 이름은 원하는 대로 지정할 수 있지만, 열 이름은 앞서 정의한 것과 일치해야 합니다.

- `UPDATED_AT` - 이 행이 테이블에 업데이트되거나 추가된 시간. 우리는 마지막 동기화 이후에 추가되거나 업데이트된 행만 동기화할 것입니다.
- 사용자 식별자 열. 테이블에 하나 이상의 사용자 식별자 열이 포함될 수 있습니다. 각 행에는 하나의 식별자(`external_id`, `alias_name`과 `alias_label`의 조합 또는 `braze_id` 중 하나)만 포함되어야 합니다. 소스 테이블에는 하나, 둘 또는 세 가지 식별자 유형에 대한 열이 있을 수 있습니다. 
    - `EXTERNAL_ID` - 업데이트하려는 사용자를 식별합니다. 이 값은 Braze에서 사용하는 `external_id` 값과 일치해야 합니다. 
    - `ALIAS_NAME` 및 `ALIAS_LABEL` \- 이 두 열은 사용자 별칭 개체를 만듭니다. `alias_name`은 고유 식별자이고 `alias_label`은 별칭의 유형을 지정합니다. 사용자는 여러 레이블이 있는 여러 별칭을 가질 수 있지만 `alias_label`당 하나의 `alias_name`만 가질 수 있습니다.
    - `BRAZE_ID` - Braze 사용자 식별자입니다. 이것은 Braze SDK에 의해 생성되었으며, 새로운 사용자는 Braze ID를 통해 클라우드 데이터 수집을 사용하여 생성될 수 없습니다. 새 사용자를 만들려면 외부 사용자 ID 또는 사용자 별칭을 지정합니다. 
    - `EMAIL` - 사용자의 이메일 주소. 동일한 이메일 주소를 가진 여러 프로필이 존재하는 경우, 가장 최근에 업데이트된 프로필이 업데이트 우선순위가 됩니다. 이메일과 전화번호를 모두 포함하면 이메일을 기본 식별자로 사용하겠습니다.
    - `PHONE` - 사용자의 전화번호입니다. 동일한 전화번호를 가진 여러 프로필이 존재하는 경우, 가장 최근에 업데이트된 프로필이 업데이트에 우선됩니다. 
- `PAYLOAD` - 이것은 Braze에서 사용자에게 동기화하려는 필드의 문자열 또는 구조체입니다.

#### 2단계: 액세스 토큰 생성  

Braze가 Databricks에 접근하려면 개인 액세스 토큰을 생성해야 합니다.

1. 데이터브릭스 작업 영역의 상단 표시줄에서 데이터브릭스 사용자 아이디를 선택한 다음 드롭다운에서 **사용자 설정을** 선택합니다.
2. 액세스 토큰 탭에서 **새 토큰 생성**을 선택합니다.
3. 이 토큰을 식별하는 데 도움이 되는 "Braze CDI"와 같은 주석을 입력하고, Lifetime 상자(일days)를 비워 두어(blank) 토큰의 수명을 무수명으로 변경하세요.
4. **생성**을 선택하십시오.
5. 표시된 토큰을 복사한 다음 **완료**를 선택합니다.

자격 증명 생성 단계에서 Braze 대시보드에 입력할 때까지 토큰을 안전한 장소에 보관하세요.

#### 3단계: Braze IP에 대한 액세스 허용    

네트워크 정책이 있는 경우 Braze 네트워크에 Databricks 인스턴스에 대한 액세스 권한을 부여해야 합니다. 아래 IP에서 Braze 대시보드의 지역에 해당하는 액세스를 허용합니다.  

| 예: `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`, `US-07` | 인스턴스 `EU-01` 및 `EU-02`의 경우 |
|---|---|
| `23.21.118.191`| `52.58.142.242`
| `34.206.23.173`| `52.29.193.121`
| `50.16.249.9`| `35.158.29.228`
| `52.4.160.214`| `18.157.135.97`
| `54.87.8.34`| `3.123.166.46`
| `54.156.35.251`| `3.64.27.36`
| `52.54.89.238`| `3.65.88.25`
| `18.205.178.15`| `3.68.144.188`
|   | `3.70.107.88`

{% endtab %}

{% endtabs %}

### 2단계: Braze 대시보드에서 새 통합을 생성하십시오

{% tabs %}
{% tab Snowflake %}

**파트너 통합** > **기술 파트너**. Snowflake 페이지를 찾아 **새 가져오기 동기화 만들기**를 선택하세요.

{% alert note %}
[구버전 네비게이션]({{site.baseurl}}/navigation)을 사용 중인 경우 **기술 파트너**로 이동하세요.
{% endalert %}

#### 1단계: Snowflake 연결 정보 및 소스 테이블 추가

Snowflake 데이터 웨어하우스 및 소스 테이블에 대한 정보를 입력한 후 다음 단계로 진행하세요.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_1.png %})

#### 2단계: 동기화 세부 정보 구성
다음으로, 동기화 이름을 선택하고 연락처 이메일을 입력하세요. 이 연락처 정보를 사용하여 테이블에 대한 접근이 예상치 못하게 제거되는 등의 통합 오류에 대해 알려드리겠습니다.

연락처 이메일은 누락된 테이블, 권한 등과 같은 글로벌 또는 동기화 수준 오류에 대한 알림만 받게 됩니다. 그들은 행 수준 문제를 받지 않을 것입니다. 전역 오류는 동기화 실행을 방해하는 연결의 치명적인 문제를 나타냅니다. 이러한 문제에는 다음이 포함될 수 있습니다:

- 연결 문제
- 리소스의 부족
- 권한 문제
- (카탈로그 동기화 전용) 카탈로그 계층의 공간이 부족합니다

![]({% image_buster /assets/img/cloud_ingestion/ingestion_2.png %})

또한 데이터 유형과 동기화 빈도를 선택합니다. 빈도는 15분마다 한 번에서 한 달에 한 번까지 어디에서나 있을 수 있습니다. Braze 대시보드에 구성된 시간대를 사용하여 반복 동기화를 예약합니다. 지원되는 데이터 유형은 커스텀 속성, 커스텀 이벤트 및 구매 이벤트이며, 동기화의 데이터 유형은 생성 후 변경할 수 없습니다. 

#### Braze 사용자에게 공개 키 추가
이 시점에서 설정을 완료하려면 Snowflake로 돌아가야 합니다. 대시보드에 표시된 공개 키를 Braze가 Snowflake에 연결할 수 있도록 생성한 사용자에게 추가하세요.

추가 정보는 [Snowflake 설명서](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)를 참조하세요. 키를 언제든지 회전시키고 싶다면, 저희가 새로운 키 쌍을 생성하여 새로운 공개 키를 제공해 드릴 수 있습니다.

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```
{% endtab %}
{% tab Redshift %}

**파트너 통합** > **기술 파트너**. Redshift 페이지를 찾아 **새 가져오기 동기화 생성**을 선택하세요.

{% alert note %}
[구버전 네비게이션]({{site.baseurl}}/navigation)을 사용 중인 경우 **기술 파트너**로 이동하세요.
{% endalert %}

#### 1단계: Redshift 연결 정보 및 소스 테이블 추가
Redshift 데이터 웨어하우스 및 소스 테이블에 대한 정보를 입력하십시오. 프라이빗 네트워크 터널을 사용 중인 경우, 슬라이더를 토글하고 터널 정보를 입력하세요. 그런 다음 다음 단계로 진행하십시오.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_6.png %})

#### 2단계: 동기화 세부 정보 구성
다음으로, 동기화 이름을 선택하고 연락처 이메일을 입력하세요. 이 연락처 정보를 사용하여 테이블에 대한 접근이 예상치 못하게 제거되는 등의 통합 오류에 대해 알려드리겠습니다.

연락처 이메일은 누락된 테이블, 권한 등과 같은 글로벌 또는 동기화 수준 오류에 대한 알림만 받게 됩니다. 그들은 행 수준 문제를 받지 않을 것입니다. 전역 오류는 동기화 실행을 방해하는 연결의 치명적인 문제를 나타냅니다. 이러한 문제에는 다음이 포함될 수 있습니다:

- 연결 문제
- 리소스의 부족
- 권한 문제
- (카탈로그 동기화 전용) 카탈로그 계층의 공간이 부족합니다

![]({% image_buster /assets/img/cloud_ingestion/ingestion_7.png %})

또한 데이터 유형과 동기화 빈도를 선택합니다. 빈도는 15분마다 한 번에서 한 달에 한 번까지 어디에서나 있을 수 있습니다. Braze 대시보드에 구성된 시간대를 사용하여 반복 동기화를 예약합니다. 지원되는 데이터 유형은 커스텀 속성, 커스텀 이벤트 및 구매 이벤트이며, 동기화의 데이터 유형은 생성 후 변경할 수 없습니다.
{% endtab %}
{% tab BigQuery %}

**파트너 통합** > **기술 파트너**. BigQuery 페이지를 찾아 **새 가져오기 동기화 만들기**를 선택하세요.

{% alert note %}
[구버전 네비게이션]({{site.baseurl}}/navigation)을 사용 중인 경우 **기술 파트너**로 이동하세요.
{% endalert %}

#### 1단계: BigQuery 연결 정보 및 소스 테이블 추가
JSON 키를 업로드하고 서비스 계정의 이름을 제공한 다음 소스 테이블의 세부 정보를 입력합니다.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_11.png %})

#### 2단계: 동기화 세부 정보 구성
다음으로, 동기화 이름을 선택하고 연락처 이메일을 입력하세요. 이 연락처 정보를 사용하여 테이블에 대한 접근이 예상치 못하게 제거되는 등의 통합 오류에 대해 알려드리겠습니다.

연락처 이메일은 누락된 테이블, 권한 등과 같은 글로벌 또는 동기화 수준 오류에 대한 알림만 받게 됩니다. 그들은 행 수준 문제를 받지 않을 것입니다. 전역 오류는 동기화 실행을 방해하는 연결의 치명적인 문제를 나타냅니다. 이러한 문제에는 다음이 포함될 수 있습니다:

- 연결 문제
- 리소스의 부족
- 권한 문제
- (카탈로그 동기화 전용) 카탈로그 계층의 공간이 부족합니다

![]({% image_buster /assets/img/cloud_ingestion/ingestion_12.png %})

또한 데이터 유형과 동기화 빈도를 선택합니다. 빈도는 15분마다 한 번에서 한 달에 한 번까지 어디에서나 있을 수 있습니다. Braze 대시보드에 구성된 시간대를 사용하여 반복 동기화를 예약합니다. 지원되는 데이터 유형은 커스텀 속성, 커스텀 이벤트, 구매 이벤트 및 사용자 삭제입니다. 동기화의 데이터 유형은 생성 후 변경할 수 없습니다. 

{% endtab %}
{% tab Databricks %}

**파트너 통합** > **기술 파트너**. Databricks 페이지를 찾아 **Create new import sync**을 선택하세요.

{% alert note %}
[구버전 네비게이션]({{site.baseurl}}/navigation)을 사용 중인 경우 **기술 파트너**로 이동하세요.
{% endalert %}

#### 1단계: Databricks 연결 정보 및 소스 테이블 추가
Databricks 데이터 웨어하우스 및 소스 테이블에 대한 정보를 입력한 다음, 다음 단계로 진행하세요.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_16.png %})

#### 2단계: 동기화 세부 정보 구성
다음으로, 동기화 이름을 선택하고 연락처 이메일을 입력하세요. 이 연락처 정보를 사용하여 테이블에 대한 접근이 예상치 못하게 제거되는 등의 통합 오류에 대해 알려드리겠습니다.

연락처 이메일은 누락된 테이블, 권한 등과 같은 글로벌 또는 동기화 수준 오류에 대한 알림만 받게 됩니다. 그들은 행 수준 문제를 받지 않을 것입니다. 전역 오류는 동기화 실행을 방해하는 연결의 치명적인 문제를 나타냅니다. 이러한 문제에는 다음이 포함될 수 있습니다:

- 연결 문제
- 리소스의 부족
- 권한 문제
- (카탈로그 동기화 전용) 카탈로그 계층의 공간이 부족합니다

![]({% image_buster /assets/img/cloud_ingestion/ingestion_12.png %})

또한 데이터 유형과 동기화 빈도를 선택합니다. 빈도는 15분마다 한 번에서 한 달에 한 번까지 어디에서나 있을 수 있습니다. Braze 대시보드에 구성된 시간대를 사용하여 반복 동기화를 예약합니다. 지원되는 데이터 유형은 커스텀 속성, 커스텀 이벤트, 구매 이벤트 및 사용자 삭제입니다. 동기화의 데이터 유형은 생성 후 변경할 수 없습니다. 

{% endtab %}
{% endtabs %}

### 3단계: 테스트 연결

{% tabs %}
{% tab Snowflake %}

Braze 대시보드로 돌아가서 **연결 테스트**를 선택하세요. 성공하면 데이터 미리보기를 볼 수 있습니다. 만약 어떤 이유로 연결할 수 없다면, 문제를 해결할 수 있도록 오류 메시지를 표시할 것입니다.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_3.png %})
{% endtab %}
{% tab Redshift %}
Braze 대시보드로 돌아가서 **연결 테스트**를 선택하세요. 성공하면 데이터 미리보기를 볼 수 있습니다. 만약 어떤 이유로 연결할 수 없다면, 문제를 해결할 수 있도록 오류 메시지를 표시할 것입니다.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_8.png %})
{% endtab %}
{% tab Redshift 프라이빗 네트워크 %}

Braze 대시보드로 돌아가서 **연결 테스트**를 선택하세요. 성공하면 데이터 미리보기를 볼 수 있습니다. 만약 어떤 이유로 연결할 수 없다면, 문제를 해결할 수 있도록 오류 메시지를 표시할 것입니다.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_19.png %})
{% endtab %}
{% tab BigQuery %}

모든 동기화 구성 세부 정보를 입력한 후 **연결 테스트**를 선택합니다. 성공하면 데이터 미리보기를 볼 수 있습니다. 만약 어떤 이유로 연결할 수 없다면, 문제를 해결할 수 있도록 오류 메시지를 표시할 것입니다.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_13.png %})

{% endtab %}
{% tab Databricks %}

모든 동기화 구성 세부 정보를 입력한 후 **연결 테스트**를 선택합니다. 성공하면 데이터 미리보기를 볼 수 있습니다. 만약 어떤 이유로 연결할 수 없다면, 문제를 해결할 수 있도록 오류 메시지를 표시할 것입니다.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_13.png %})

{% endtab %}
{% endtabs %}

{% alert note %}
통합을 초안에서 활성 상태로 전환하기 전에 반드시 성공적으로 테스트해야 합니다. 생성 페이지를 닫아야 하는 경우, 통합이 저장되며, 세부 정보 페이지를 다시 방문하여 변경 및 테스트를 할 수 있습니다.  
{% endalert %}

## 추가 통합 또는 사용자 설정 (선택 사항)

{% tabs %}
{% tab Snowflake %}
Braze와 여러 통합을 설정할 수 있지만, 각 통합은 다른 테이블과 동기화되도록 구성해야 합니다. 추가 동기화를 생성할 때 Snowflake 계정에 연결하는 경우 기존 자격 증명을 재사용할 수 있습니다.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_4.png %})

동일한 사용자 및 역할을 통합에 걸쳐 재사용하는 경우, 공개 키를 다시 추가하는 단계를 거칠 필요가 **없습니다**.
{% endtab %}
{% tab Redshift %}
Braze와 여러 통합을 설정할 수 있지만, 각 통합은 다른 테이블과 동기화되도록 구성해야 합니다. 추가 동기화를 생성할 때 동일한 Snowflake 또는 Redshift 계정에 연결하는 경우 기존 자격 증명을 재사용할 수 있습니다.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_9.png %})

동일한 사용자를 통합 간에 재사용하는 경우 모든 활성 동기화에서 제거될 때까지 Braze 대시보드에서 사용자를 삭제할 수 없습니다.
{% endtab %}
{% tab BigQuery %}

Braze와 여러 통합을 설정할 수 있지만, 각 통합은 다른 테이블과 동기화되도록 구성해야 합니다. 추가 동기화를 생성할 때 동일한 BigQuery 계정에 연결하는 경우 기존 자격 증명을 재사용할 수 있습니다.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_14.png %})

동일한 사용자를 통합 간에 재사용하는 경우 모든 활성 동기화에서 제거될 때까지 Braze 대시보드에서 사용자를 삭제할 수 없습니다.

{% endtab %}
{% tab Databricks %}

Braze와 여러 통합을 설정할 수 있지만, 각 통합은 다른 테이블과 동기화되도록 구성해야 합니다. 추가 동기화를 생성할 때 동일한 Databricks 계정에 연결하는 경우 기존 자격 증명을 재사용할 수 있습니다.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_17.png %})

동일한 사용자를 통합 간에 재사용하는 경우 모든 활성 동기화에서 제거될 때까지 Braze 대시보드에서 사용자를 삭제할 수 없습니다.

{% endtab %}
{% endtabs %}

## 동기화 실행

{% tabs %}
{% tab Snowflake %}
활성화되면 동기화가 설정 중 구성된 일정에 따라 실행됩니다. 정기 테스트 일정 외에 동기화를 실행하거나 최신 데이터를 가져오려면 **지금 동기화**를 선택하십시오. 이 실행은 정기적으로 예정된 향후 동기화에 영향을 미치지 않습니다.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_5.png %})

{% endtab %}
{% tab Redshift %}
활성화되면 동기화가 설정 중 구성된 일정에 따라 실행됩니다. 정기 테스트 일정 외에 동기화를 실행하거나 최신 데이터를 가져오려면 **지금 동기화**를 선택하십시오. 이 실행은 정기적으로 예정된 향후 동기화에 영향을 미치지 않습니다.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_10.png %})

{% endtab %}
{% tab BigQuery %}

활성화되면 동기화가 설정 중 구성된 일정에 따라 실행됩니다. 정기 테스트 일정 외에 동기화를 실행하거나 최신 데이터를 가져오려면 **지금 동기화**를 선택하십시오. 이 실행은 정기적으로 예정된 향후 동기화에 영향을 미치지 않습니다.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_15.png %})

{% endtab %}
{% tab Databricks %}

활성화되면 동기화가 설정 중 구성된 일정에 따라 실행됩니다. 정기 테스트 일정 외에 동기화를 실행하거나 최신 데이터를 가져오려면 **지금 동기화**를 선택하십시오. 이 실행은 정기적으로 예정된 향후 동기화에 영향을 미치지 않습니다.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_18.png %})

{% endtab %}
{% endtabs %}

[1]: {% image_buster /assets/img/cloud_ingestion/ingestion_6.png %}
[2]: {% image_buster /assets/img/cloud_ingestion/ingestion_7.png %}
[3]: {% image_buster /assets/img/cloud_ingestion/ingestion_8.png %}
[4]: {% image_buster /assets/img/cloud_ingestion/ingestion_9.png %}
[5]: {% image_buster /assets/img/cloud_ingestion/ingestion_10.png %}
[6]: {% image_buster /assets/img/cloud_ingestion/ingestion_5.png %}
