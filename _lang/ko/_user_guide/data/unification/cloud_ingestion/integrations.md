---
nav_title: 데이터 웨어하우스 통합
article_title: 데이터 웨어하우스 통합
description: "이 페이지에서는 Braze Cloud 데이터 수집을 사용하여 관련 데이터를 Snowflake, Redshift, BigQuery 및 Databricks 통합과 동기화하는 방법을 설명합니다."
page_order: 2
page_type: reference

---

# 데이터 웨어하우스 스토리지 통합

> 이 페이지에서는 Braze 클라우드 데이터 수집(CDI)을 사용하여 관련 데이터를 Snowflake, Redshift, BigQuery 및 데이터브릭스 통합과 동기화하는 방법에 대해 설명합니다.

## 데이터 웨어하우스 통합 설정하기

클라우드 데이터 수집 통합을 위해서는 Braze 측과 데이터 웨어하우스 인스턴스에서 몇 가지 설정이 필요합니다. 통합을 설정하려면 다음 단계를 따르세요:

{% tabs %}
{% tab Snowflake %}
1. Snowflake 인스턴스에서 Braze에 동기화할 테이블 또는 뷰를 설정합니다.
2. Braze 대시보드에서 새 통합을 만듭니다.
3. Braze 대시보드에서 제공된 공개 키를 가져와서 [Snowflake 사용자에게 추가하여 인증합니다](https://docs.snowflake.com/en/user-guide/key-pair-auth.html).
4. 통합을 테스트하고 동기화를 시작합니다.

{% alert tip %}
[Snowflake 빠른 시작 가이드에서는](https://quickstarts.snowflake.com/guide/braze_cdi/index.html) 샘플 코드를 제공하고, Snowflake 스트림과 CDI를 사용하여 데이터를 Braze에 동기화하는 자동화 파이프라인을 만드는 데 필요한 단계를 안내합니다.
{% endalert %}
{% endtab %}
{% tab Redshift %}
1. 동기화하려는 Redshift 테이블에 대한 Braze 액세스가 허용되어 있는지 확인하세요. Braze는 인터넷을 통해 Redshift에 연결됩니다.
2. Redshift 인스턴스에서 Braze에 동기화할 테이블 또는 보기를 설정합니다.
3. Braze 대시보드에서 새 통합을 만듭니다.
4. 통합을 테스트하고 동기화를 시작합니다.
{% endtab %}
{% tab BigQuery %}
1. 서비스 계정을 만들고 동기화하려는 데이터가 포함된 BigQuery 프로젝트 및 데이터 집합에 대한 액세스를 허용합니다.  
2. BigQuery 계정에서 Braze에 동기화하려는 테이블 또는 보기를 설정합니다.   
3. Braze 대시보드에서 새 통합을 만듭니다.  
4. 통합을 테스트하고 동기화를 시작합니다.  
{% endtab %}
{% tab Databricks %}
1. 서비스 계정을 만들고 동기화하려는 데이터가 포함된 데이터브릭스 프로젝트 및 데이터세트에 대한 액세스를 허용하세요.  
2. 데이터브릭스 계정에서 Braze에 동기화할 테이블 또는 뷰를 설정합니다.   
3. Braze 대시보드에서 새 통합을 만듭니다.  
4. 통합을 테스트하고 동기화를 시작합니다.

{% alert important %}
Braze가 클래식 및 프로 SQL 인스턴스에 연결할 때 2~5분 정도의 워밍업 시간이 있을 수 있으며, 이로 인해 연결 설정 및 테스트 중, 그리고 예약된 동기화 시작 시 지연이 발생할 수 있습니다. 서버리스 SQL 인스턴스를 사용하면 워밍업 시간이 최소화되고 쿼리 처리량이 향상되지만 통합 비용이 약간 높아질 수 있습니다.
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}
1. 서비스 주체를 만들고 통합에 사용할 Fabric 워크스페이스에 대한 액세스를 허용하세요.   
2. Fabric 작업 공간에서 Braze에 동기화하려는 테이블 또는 보기를 설정합니다.   
3. Braze 대시보드에서 새 통합을 만듭니다.  
4. 통합을 테스트하고 동기화를 시작합니다.
{% endtab %}
{% endtabs %}

### 1단계: 테이블 또는 뷰 설정

{% tabs %}
{% tab Snowflake %}

#### 1.1단계: 테이블 설정

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

데이터베이스, 스키마 및 테이블의 이름은 원하는 대로 지정할 수 있지만 열 이름은 앞의 정의와 일치해야 합니다.

- `UPDATED_AT` - 이 행이 테이블에서 업데이트되거나 테이블에 추가된 시간입니다. 마지막 동기화 이후 추가되거나 업데이트된 행만 동기화합니다.
- **사용자 식별자 열** \- 테이블에 하나 이상의 사용자 식별자 열이 포함될 수 있습니다. 각 행에는 하나의 식별자( `external_id`, `alias_name` 과 `alias_label` 의 조합 , `braze_id`, `email` 또는 `phone`)만 포함해야 합니다. 소스 테이블에는 하나, 둘, 셋, 넷 또는 다섯 가지 식별자 유형 모두에 대한 열이 있을 수 있습니다.
    - `EXTERNAL_ID` - 업데이트하려는 사용자를 식별합니다. 이 값은 Braze에서 사용된 `external_id` 값과 일치해야 합니다. 
    - `ALIAS_NAME` 및 `ALIAS_LABEL` \- 이 두 열은 사용자 별칭 개체를 만듭니다. `alias_name` 은 고유 식별자이고 `alias_label` 은 별칭의 유형을 지정합니다. 사용자는 서로 다른 라벨을 가진 여러 개의 별칭을 가질 수 있지만 `alias_label` 당 `alias_name` 은 하나만 지정할 수 있습니다.
    - `BRAZE_ID` - Braze 사용자 식별자입니다. 이는 Braze 소프트웨어 개발 키트에 의해 생성되며, 클라우드 데이터 수집을 통해 새로운 사용자 ID를 생성할 수 없습니다. 새 사용자를 만들려면 외부 사용자 ID 또는 사용자 별칭을 지정합니다.
    - `EMAIL` - 사용자의 이메일 주소입니다. 동일한 이메일 주소를 가진 프로필이 여러 개 있는 경우 가장 최근에 업데이트된 프로필이 우선적으로 업데이트됩니다. 이메일과 전화번호를 모두 포함하는 경우 이메일을 기본 식별자로 사용합니다.
    - `PHONE` - 사용자의 전화번호입니다. 동일한 전화번호를 사용하는 프로필이 여러 개 있는 경우 가장 최근에 업데이트된 프로필이 우선적으로 업데이트됩니다. 
- `PAYLOAD` - Braze에서 사용자에게 동기화하려는 필드의 JSON 문자열입니다.

#### 1.2단계: 역할 및 데이터베이스 권한 설정

```json
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;
```

필요에 따라 이름을 업데이트하되 권한은 앞의 예와 일치해야 합니다.

#### 1.3단계: 창고를 설정하고 Braze 역할에 대한 액세스 권한을 부여합니다.

```json
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
창고에 **자동 재개** 플래그가 설정되어 있어야 합니다. 그렇지 않은 경우, 쿼리를 실행할 때가 되면 창고에 대한 추가 권한( `OPERATE` )을 Braze에 부여해야 합니다.
{% endalert %}

#### 1.4단계: 사용자 설정

```json
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

이 단계가 끝나면 Braze와 연결 정보를 공유하고 사용자에게 추가할 공개 키를 받게 됩니다.

{% alert note %}
서로 다른 워크스페이스를 동일한 Snowflake 계정에 연결할 때는 통합을 만들고자 하는 각 Braze 워크스페이스에 대해 고유한 사용자를 만들어야 합니다. 워크스페이스 내에서 동일한 사용자를 여러 통합에서 재사용할 수 있지만, 동일한 Snowflake 계정의 사용자가 여러 워크스페이스에 중복되어 있으면 통합 생성이 실패합니다.
{% endalert %}

#### 1.5단계: Snowflake 네트워크 정책에서 Braze IP 허용(선택 사항)

Snowflake 계정의 구성에 따라 Snowflake 네트워크 정책에서 다음 IP 주소를 허용해야 할 수 있습니다. 이 기능을 인에이블먼트하는 방법에 대한 자세한 내용은 [네트워크 정책 수정에](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies) 관한 관련 Snowflake 설명서를 참조하세요.

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Redshift %}

#### 1.1단계: 테이블 설정 

선택 사항으로, 소스 테이블을 보관할 새 데이터베이스 및 스키마를 설정합니다.
```json
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```
CDI 통합에 사용할 테이블(또는 뷰) 만들기
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

데이터베이스, 스키마 및 테이블의 이름은 원하는 대로 지정할 수 있지만 열 이름은 앞의 정의와 일치해야 합니다.

- `UPDATED_AT` - 이 행이 테이블에서 업데이트되거나 테이블에 추가된 시간입니다. 마지막 동기화 이후 추가되거나 업데이트된 행만 동기화합니다.
- **사용자 식별자 열** \- 테이블에 하나 이상의 사용자 식별자 열이 포함될 수 있습니다. 각 행에는 하나의 식별자( `external_id`, `alias_name` 과 `alias_label` 의 조합 , `braze_id`, `email` 또는 `phone`)만 포함해야 합니다. 소스 테이블에는 하나, 둘, 셋, 넷 또는 다섯 가지 식별자 유형 모두에 대한 열이 있을 수 있습니다.
    - `EXTERNAL_ID` - 업데이트하려는 사용자를 식별합니다. 이 값은 Braze에서 사용된 `external_id` 값과 일치해야 합니다. 
    - `ALIAS_NAME` 및 `ALIAS_LABEL` \- 이 두 열은 사용자 별칭 개체를 만듭니다. `alias_name` 은 고유 식별자이고 `alias_label` 은 별칭의 유형을 지정합니다. 사용자는 서로 다른 라벨을 가진 여러 개의 별칭을 가질 수 있지만 `alias_label` 당 `alias_name` 은 하나만 지정할 수 있습니다.
    - `BRAZE_ID` - Braze 사용자 식별자입니다. 이는 Braze 소프트웨어 개발 키트에 의해 생성되며, 클라우드 데이터 수집을 통해 새로운 사용자 ID를 생성할 수 없습니다. 새 사용자를 만들려면 외부 사용자 ID 또는 사용자 별칭을 지정합니다.
    - `EMAIL` - 사용자의 이메일 주소입니다. 동일한 이메일 주소를 가진 프로필이 여러 개 있는 경우 가장 최근에 업데이트된 프로필이 우선적으로 업데이트됩니다. 이메일과 전화번호를 모두 포함하는 경우 이메일을 기본 식별자로 사용합니다.
    - `PHONE` - 사용자의 전화번호입니다. 동일한 전화번호를 사용하는 프로필이 여러 개 있는 경우 가장 최근에 업데이트된 프로필이 우선적으로 업데이트됩니다. 
- `PAYLOAD` - Braze에서 사용자에게 동기화하려는 필드의 JSON 문자열입니다.
 
#### 1.2단계: 사용자 만들기 및 권한 부여 

```json
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

이 사용자에게 필요한 최소 권한입니다. 여러 CDI 통합을 만드는 경우 스키마에 권한을 부여하거나 그룹을 사용하여 권한을 관리할 수 있습니다. 

#### 1.3단계: Braze IP에 대한 액세스 허용

방화벽이나 기타 네트워크 정책이 있는 경우, Redshift 인스턴스에 대한 Braze 네트워크 액세스 권한을 부여해야 합니다. Redshift URL 엔드포인트의 예는 "example-cluster.ap-northeast-2.redshift.amazonaws.com" 입니다.

몇 가지 중요한 사항을 알아두세요:
- 또한 보안 그룹을 변경하여 Braze가 Redshift에서 데이터에 액세스할 수 있도록 허용해야 할 수도 있습니다.
- 테이블의 IP와 Redshift 클러스터를 쿼리하는 데 사용되는 포트에서 인바운드 트래픽을 명시적으로 허용해야 합니다(기본값은 5439). 인바운드 규칙이 "모두 허용"으로 설정되어 있더라도 이 포트에서 Redshift TCP 연결을 명시적으로 허용해야 합니다.
- Redshift 클러스터의 엔드포인트는 공개적으로 액세스할 수 있어야 Braze가 클러스터에 연결할 수 있습니다.
     - Redshift 클러스터에 공개적으로 액세스하지 않으려는 경우, VPC 및 EC2 인스턴스를 설정하여 SSH 터널을 사용하여 Redshift 데이터에 액세스할 수 있습니다. 자세한 내용은 이 [AWS 지식 센터 게시물을](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine) 확인하세요.
 
Braze 대시보드의 지역에 해당하는 다음 IP에서 액세스를 허용합니다.

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab BigQuery %}

#### 1.1단계: 테이블 설정 

원하는 경우, 새 프로젝트 또는 데이터 집합을 설정하여 소스 테이블을 보관합니다.

```json
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

다음 필드를 사용하여 CDI 통합에 사용할 테이블을 하나 이상 만듭니다:

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

프로젝트, 데이터 집합 및 테이블의 이름은 원하는 대로 지정할 수 있지만 열 이름은 앞의 정의와 일치해야 합니다.

- `UPDATED_AT` - 이 행이 테이블에서 업데이트되거나 테이블에 추가된 시간입니다. 마지막 동기화 이후 추가되거나 업데이트된 행만 동기화합니다.
- **사용자 식별자 열** \- 테이블에 하나 이상의 사용자 식별자 열이 포함될 수 있습니다. 각 행에는 하나의 식별자( `external_id`, `alias_name` 과 `alias_label` 의 조합 , `braze_id`, `email` 또는 `phone`)만 포함해야 합니다. 소스 테이블에는 하나, 둘, 셋, 넷 또는 다섯 가지 식별자 유형 모두에 대한 열이 있을 수 있습니다.
    - `EXTERNAL_ID` - 업데이트하려는 사용자를 식별합니다. 이 값은 Braze에서 사용된 `external_id` 값과 일치해야 합니다. 
    - `ALIAS_NAME` 및 `ALIAS_LABEL` \- 이 두 열은 사용자 별칭 개체를 만듭니다. `alias_name` 은 고유 식별자이고 `alias_label` 은 별칭의 유형을 지정합니다. 사용자는 서로 다른 라벨을 가진 여러 개의 별칭을 가질 수 있지만 `alias_label` 당 `alias_name` 은 하나만 지정할 수 있습니다.
    - `BRAZE_ID` - Braze 사용자 식별자입니다. 이는 Braze 소프트웨어 개발 키트에 의해 생성되며, 클라우드 데이터 수집을 통해 새로운 사용자 ID를 생성할 수 없습니다. 새 사용자를 만들려면 외부 사용자 ID 또는 사용자 별칭을 지정합니다.
    - `EMAIL` - 사용자의 이메일 주소입니다. 동일한 이메일 주소를 가진 프로필이 여러 개 있는 경우 가장 최근에 업데이트된 프로필이 우선적으로 업데이트됩니다. 이메일과 전화번호를 모두 포함하는 경우 이메일을 기본 식별자로 사용합니다.
    - `PHONE` - 사용자의 전화번호입니다. 동일한 전화번호를 사용하는 프로필이 여러 개 있는 경우 가장 최근에 업데이트된 프로필이 우선적으로 업데이트됩니다.
   이메일 varchar,
   phone_number varchar,
- `PAYLOAD` - Braze에서 사용자에게 동기화하려는 필드의 JSON 문자열입니다.

#### 1.2단계: 서비스 계정 만들기 및 권한 부여하기 

Braze가 테이블에서 데이터를 연결하고 읽는 데 사용할 서비스 계정을 GCP에서 생성하세요. 서비스 계정에는 아래 권한이 있어야 합니다: 

- **BigQuery 연결 사용자:** 이렇게하면 Braze가 연결할 수 있습니다.
- **BigQuery 사용자:** 이렇게 하면 쿼리를 실행하고, 데이터 세트 메타데이터를 읽고, 테이블을 나열할 수 있는 Braze 액세스 권한이 제공됩니다.
- **BigQuery 데이터 뷰어:** 이렇게 하면 데이터 세트와 그 내용을 볼 수 있는 Braze 액세스 권한이 제공됩니다.
- **BigQuery 작업 사용자:** 이렇게 하면 작업을 실행할 수 있는 Braze 액세스 권한이 제공됩니다.

서비스 계정을 만들고 권한을 부여한 후 JSON 키를 생성합니다. 자세한 방법은 [여기를](https://cloud.google.com/iam/docs/keys-create-delete) 참조하세요. 이 기능은 나중에 Braze 대시보드에 업데이트될 예정입니다. 

#### 1.3단계: Braze IP에 대한 액세스 허용    

네트워크 정책이 설정되어 있는 경우, 빅 쿼리 인스턴스에 대한 Braze 네트워크 액세스 권한을 부여해야 합니다. Braze 대시보드의 지역에 해당하는 아래 IP에서 액세스를 허용합니다.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Databricks %}

#### 1.1단계: 테이블 설정 

선택 사항으로 소스 테이블을 보관할 새 카탈로그 또는 스키마를 설정합니다.

```json
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

다음 필드를 사용하여 CDI 통합에 사용할 테이블을 하나 이상 만듭니다:


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
  payload STRING, STRUCT, or MAP
);
```


| 필드 이름 | 유형 | 모드 |
|---|---|---|
| `UPDATED_AT`| 타임스탬프 | 필수 |
| `PAYLOAD`| 문자열, 구조체 또는 매핑 | 필수 |
| `EXTERNAL_ID`| 문자열 | NULLABLE |
| `ALIAS_NAME`| 문자열 | NULLABLE |
| `ALIAS_LABEL`| 문자열 | NULLABLE |
| `BRAZE_ID`| 문자열 | NULLABLE |
| `EMAIL`| 문자열 | NULLABLE |
| `PHONE`| 문자열 | NULLABLE |

스키마와 테이블의 이름은 원하는 대로 지정할 수 있지만 열 이름은 앞의 정의와 일치해야 합니다.

- `UPDATED_AT` - 이 행이 테이블에서 업데이트되거나 테이블에 추가된 시간입니다. 마지막 동기화 이후 추가되거나 업데이트된 행만 동기화합니다.
- **사용자 식별자 열** \- 테이블에 하나 이상의 사용자 식별자 열이 포함될 수 있습니다. 각 행에는 하나의 식별자( `external_id`, `alias_name` 과 `alias_label` 의 조합 , `braze_id`, `email` 또는 `phone`)만 포함해야 합니다. 소스 테이블에는 하나, 둘, 셋, 넷 또는 다섯 가지 식별자 유형 모두에 대한 열이 있을 수 있습니다.
    - `EXTERNAL_ID` - 업데이트하려는 사용자를 식별합니다. 이 값은 Braze에서 사용된 `external_id` 값과 일치해야 합니다. 
    - `ALIAS_NAME` 및 `ALIAS_LABEL` \- 이 두 열은 사용자 별칭 개체를 만듭니다. `alias_name` 은 고유 식별자이고 `alias_label` 은 별칭의 유형을 지정합니다. 사용자는 서로 다른 라벨을 가진 여러 개의 별칭을 가질 수 있지만 `alias_label` 당 `alias_name` 은 하나만 지정할 수 있습니다.
    - `BRAZE_ID` - Braze 사용자 식별자입니다. 이는 Braze 소프트웨어 개발 키트에 의해 생성되며, 클라우드 데이터 수집을 통해 새로운 사용자 ID를 생성할 수 없습니다. 새 사용자를 만들려면 외부 사용자 ID 또는 사용자 별칭을 지정합니다. 
    - `EMAIL` - 사용자의 이메일 주소입니다. 동일한 이메일 주소를 가진 프로필이 여러 개 있는 경우 가장 최근에 업데이트된 프로필이 우선적으로 업데이트됩니다. 이메일과 전화번호를 모두 포함하는 경우 이메일을 기본 식별자로 사용합니다.
    - `PHONE` - 사용자의 전화번호입니다. 동일한 전화번호를 사용하는 프로필이 여러 개 있는 경우 가장 최근에 업데이트된 프로필이 우선적으로 업데이트됩니다. 
- `PAYLOAD` - Braze에서 사용자에게 동기화하려는 필드의 문자열 또는 구조체입니다.

#### 1.2단계: 액세스 토큰 만들기  

Braze가 데이터브릭에 액세스하려면 개인 액세스 토큰을 생성해야 합니다.

1. 데이터브릭스 작업 영역의 상단 표시줄에서 데이터브릭스 사용자 아이디를 선택한 다음 드롭다운에서 **사용자 설정을** 선택합니다.
2. 토큰 액세스 탭에서 **새 토큰 생성을** 선택합니다.
3. 이 토큰을 식별하는 데 도움이 되는 댓글(예: "Braze CDI")을 입력하고 토큰의 수명을 수명(일) 상자를 비워 두어(공란) 토큰의 수명을 수명 없음으로 변경합니다.
4. **생성을** 선택합니다.
5. 표시된 토큰을 복사한 다음 **완료를** 선택합니다.

자격 증명 생성 단계에서 Braze 대시보드에 토큰을 입력해야 할 때까지 토큰을 안전한 곳에 보관하세요.

#### 1.3단계: Braze IP에 대한 액세스 허용    

네트워크 정책을 설정한 경우, 데이터브릭스 인스턴스에 대한 네트워크 액세스 권한을 Braze에 부여해야 합니다. Braze 대시보드의 지역에 해당하는 아래 IP에서 액세스를 허용합니다.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Microsoft Fabric %}

#### 1.1단계: 서비스 주체를 설정하고 액세스 권한을 부여합니다.
Braze는 Entra ID 인증이 있는 서비스 주체를 사용하여 Fabric 웨어하우스에 연결합니다. Braze가 사용할 새 서비스 주체를 생성하고 필요에 따라 Fabric 리소스에 대한 액세스 권한을 부여합니다. Braze를 연결하려면 다음 세부 정보가 필요합니다:    

* Azure 계정의 테넌트 ID(디렉터리라고도 함) 
* 서비스 주체에 대한 주체 ID(애플리케이션 ID라고도 함) 
* Braze가 인증하기 위한 클라이언트 암호

1. Azure 포털에서 Microsoft Entra 관리 센터로 이동한 다음 앱 등록으로 이동합니다. 
2. **ID** > **애플리케이션** > **앱 등록에서** **\+ 새 등록을** 선택합니다.
3. 이름을 입력한 다음 지원되는 계정 유형으로 `Accounts in this organizational directory only` 을 선택합니다. 그런 다음 **등록을** 선택합니다. 
4. 방금 만든 애플리케이션(서비스 계정)을 선택한 다음 **인증서 & 비밀** > **\+ 새 클라이언트 비밀로** 이동합니다.
5. 비밀 번호에 대한 설명을 입력하고 비밀 번호의 만료 기간을 설정합니다. 그런 다음 **추가를** 선택합니다. 
6. Braze 설정에서 사용하기 위해 생성한 클라이언트 비밀 번호를 기록해 두세요. 

{% alert note %}
Azure에서는 서비스 계정 암호의 만료를 무제한으로 허용하지 않습니다. 만료되기 전에 자격 증명을 새로고침하여 Braze에 대한 데이터 흐름을 유지하는 것을 잊지 마세요.
{% endalert %}

#### 1.2단계: 패브릭 리소스에 대한 액세스 권한 부여 
Braze가 Fabric 인스턴스에 연결할 수 있는 액세스 권한을 제공해야 합니다. Fabric 관리자 포털에서 **설정** > **거버넌스 및 인사이트** > **관리자 포털** > **테넌트 설정으로** 이동합니다.    

* **개발자 설정에서** "서비스 주체가 Fabric API를 사용할 수 있음"을 인에이블먼트하여 Braze가 Microsoft Entra ID를 사용하여 연결할 수 있도록 하세요.
* 서비스 주체가 외부 앱에서 데이터에 액세스할 수 있도록 **원레이크 설정에서** "사용자가 Fabric 외부의 앱으로 원레이크에 저장된 데이터에 액세스할 수 있음"을 인에이블먼트하세요.


#### 1.3단계: 테이블 설정
Braze는 패브릭 웨어하우스에서 테이블과 뷰를 모두 지원합니다. 새 웨어하우스를 생성해야 하는 경우, Fabric 콘솔에서 **생성 > 데이터 웨어하우스 > 창고로** 이동하세요. 

```json
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name] 
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PAYLOAD VARCHAR NOT NULL,
  --at least one of external_id, alias_name and alias_label, email, phone, or braze_id is required  
  EXTERNAL_ID VARCHAR,
  --if using user alias, both alias_name and alias_label are required
  ALIAS_NAME VARCHAR,
  ALIAS_LABEL VARCHAR,
  --braze_id can only be used to update existing users created through the Braze SDK
  BRAZE_ID VARCHAR,
  --If you include both email and phone, we will use the email as the primary identifier
  EMAIL VARCHAR,
  PHONE VARCHAR
)
GO
```

웨어하우스, 스키마, 테이블 또는 뷰의 이름은 원하는 대로 지정할 수 있지만 열 이름은 앞의 정의와 일치해야 합니다.

- `UPDATED_AT` - 이 행이 테이블에서 업데이트되거나 테이블에 추가된 시간입니다. 마지막 동기화 이후 추가되거나 업데이트된 행만 동기화합니다.
- **사용자 식별자 열** \- 테이블에 하나 이상의 사용자 식별자 열이 포함될 수 있습니다. 각 행에는 하나의 식별자( `external_id`, `alias_name` 과 `alias_label` 의 조합 , `braze_id`, `email` 또는 `phone`)만 포함해야 합니다. 소스 테이블에는 하나, 둘, 셋, 넷 또는 다섯 가지 식별자 유형 모두에 대한 열이 있을 수 있습니다.
    - `EXTERNAL_ID` - 업데이트하려는 사용자를 식별합니다. 이 값은 Braze에서 사용된 `external_id` 값과 일치해야 합니다. 
    - `ALIAS_NAME` 및 `ALIAS_LABEL` \- 이 두 열은 사용자 별칭 개체를 만듭니다. `alias_name` 은 고유 식별자이고 `alias_label` 은 별칭의 유형을 지정합니다. 사용자는 서로 다른 라벨을 가진 여러 개의 별칭을 가질 수 있지만 `alias_label` 당 `alias_name` 은 하나만 지정할 수 있습니다.
    - `BRAZE_ID` - Braze 사용자 식별자입니다. 이는 Braze 소프트웨어 개발 키트에 의해 생성되며, 클라우드 데이터 수집을 통해 새로운 사용자 ID를 생성할 수 없습니다. 새 사용자를 만들려면 외부 사용자 ID 또는 사용자 별칭을 지정합니다.
    - `EMAIL` - 사용자의 이메일 주소입니다. 동일한 이메일 주소를 가진 프로필이 여러 개 있는 경우 가장 최근에 업데이트된 프로필이 우선적으로 업데이트됩니다. 이메일과 전화번호를 모두 포함하는 경우 이메일을 기본 식별자로 사용합니다.
    - `PHONE` - 사용자의 전화번호입니다. 동일한 전화번호를 사용하는 프로필이 여러 개 있는 경우 가장 최근에 업데이트된 프로필이 우선적으로 업데이트됩니다. 
- `PAYLOAD` - Braze에서 사용자에게 동기화하려는 필드의 JSON 문자열입니다.


#### 1.4단계: 웨어하우스 연결 문자열 가져오기 
Braze를 연결하려면 웨어하우스에 대한 SQL 엔드포인트가 필요합니다. 이를 검색하려면 Fabric의 **작업 공간으로** 이동하여 항목 목록에서 창고 이름 위로 마우스를 가져간 다음 **SQL 연결 문자열 복사를** 선택합니다.

사용자가 SQL 연결 문자열을 검색해야 하는 Microsoft Azure의 "Fabric Console" 페이지입니다.]({% image_buster /assets/img/cloud_ingestion/fabric_1.png %})


#### 1.5단계: 방화벽에서 Braze IP 허용(선택 사항)

Microsoft Fabric 계정의 구성에 따라 방화벽에서 다음 IP 주소를 허용하여 Braze의 트래픽을 허용해야 할 수 있습니다. 인에이블먼트에 대한 자세한 내용은 [Entra 조건부 액세스에](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access) 대한 관련 설명서를 참조하세요.

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### 2단계: Braze 대시보드에서 새 통합 만들기

{% tabs %}
{% tab Snowflake %}

Braze 대시보드에서 **데이터 설정** > **클라우드 데이터 수집으로** 이동하여 **새 데이터 동기화 만들기를** 선택한 다음 **Snowflake 가져오기를** 선택합니다.

#### 2.1단계: Snowflake 연결 정보 및 소스 테이블 추가하기

Snowflake 데이터 웨어하우스 및 소스 테이블에 대한 정보를 입력한 다음 다음 단계로 진행합니다.

1단계에 입력한 예제 데이터가 있는 Braze 대시보드의 Snowflake에 대한 "새 가져오기 동기화 만들기" 페이지: "연결 설정".]({% image_buster /assets/img/cloud_ingestion/ingestion_1.png %})

#### 2.2단계: 동기화 세부 정보 구성

다음으로 동기화할 이름을 선택하고 연락처 이메일을 입력합니다. 이 연락처 정보를 사용하여 테이블에 대한 액세스 권한이 예기치 않게 제거되는 등의 통합 오류가 발생하면 알려드립니다.

연락처 이메일은 누락된 테이블, 권한 등과 같은 전역 또는 동기화 수준 오류에 대한 알림만 수신합니다. 행 수준 이슈는 수신되지 않습니다. 전역 오류는 동기화를 실행할 수 없는 연결에 심각한 문제가 있음을 나타냅니다. 이러한 문제에는 다음이 포함될 수 있습니다:

- 연결 문제
- 리소스 부족
- 권한 문제
- (카탈로그 동기화에만 해당) 카탈로그 계층에 공간이 부족합니다.

2단계에 예제 데이터가 추가된 Braze 대시보드의 Snowflake에 대한 "새 가져오기 동기화 만들기" 페이지입니다: "동기화 세부 정보 설정".]({% image_buster /assets/img/cloud_ingestion/ingestion_2.png %})

데이터 유형과 동기화 빈도도 선택할 수 있습니다. 빈도는 15분마다부터 한 달에 한 번까지 다양합니다. Braze 대시보드에 구성된 시간대를 사용하여 반복 동기화를 예약합니다. 지원되는 데이터 유형은 커스텀 속성, 커스텀 이벤트 및 구매 이벤트이며, 동기화를 위한 데이터 유형은 생성 후에는 변경할 수 없습니다. 

#### Braze 사용자에게 공개 키 추가하기

이 시점에서 설정을 완료하려면 Snowflake로 돌아가야 합니다. 대시보드에 표시된 공개 키를 생성한 사용자에게 추가하여 Braze에 연결하면 Snowflake에 연결할 수 있습니다.

이 작업을 수행하는 방법에 대한 자세한 내용은 [Snowflake 설명서를](https://docs.snowflake.com/en/user-guide/key-pair-auth.html) 참조하세요. 언제든지 키를 교체하고 싶다면 새 키 쌍을 생성하여 새 공개 키를 제공할 수 있습니다.

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```
{% endtab %}
{% tab Redshift %}

Braze 대시보드에서 **데이터 설정** > **클라우드 데이터 수집으로** 이동하여 **새 데이터 동기화 만들기를** 선택한 다음 **Amazon Redshift 가져오기를** 선택합니다.

#### 2.1단계: Redshift 연결 정보 및 소스 테이블 추가

Redshift 데이터 웨어하우스 및 소스 테이블에 대한 정보를 입력합니다. 비공개 네트워크 터널을 사용하는 경우 슬라이더를 토글하고 터널 정보를 입력합니다. 그런 다음 다음 단계로 진행합니다.

Braze 대시보드의 Redshift에 대한 "새 가져오기 동기화 만들기" 페이지에서 1단계로 설정합니다: "연결 설정".]({% image_buster /assets/img/cloud_ingestion/ingestion_6.png %})

#### 2.2단계: 동기화 세부 정보 구성

다음으로 동기화할 이름을 선택하고 연락처 이메일을 입력합니다. 이 연락처 정보를 사용하여 테이블에 대한 액세스 권한이 예기치 않게 제거되는 등의 통합 오류가 발생하면 알려드립니다.

연락처 이메일은 누락된 테이블, 권한 등과 같은 전역 또는 동기화 수준 오류에 대한 알림만 수신합니다. 행 수준 이슈는 수신되지 않습니다. 전역 오류는 동기화를 실행할 수 없는 연결에 심각한 문제가 있음을 나타냅니다. 이러한 문제에는 다음이 포함될 수 있습니다:

- 연결 문제
- 리소스 부족
- 권한 문제
- (카탈로그 동기화에만 해당) 카탈로그 계층에 공간이 부족합니다.

2단계에 몇 가지 예제 데이터가 추가된 Braze 대시보드의 Redshift에 대한 "새 가져오기 동기화 만들기" 페이지입니다: "동기화 세부 정보 설정".]({% image_buster /assets/img/cloud_ingestion/ingestion_7.png %})

데이터 유형과 동기화 빈도도 선택할 수 있습니다. 빈도는 15분마다부터 한 달에 한 번까지 다양합니다. Braze 대시보드에 구성된 시간대를 사용하여 반복 동기화를 예약합니다. 지원되는 데이터 유형은 커스텀 속성, 커스텀 이벤트 및 구매 이벤트이며, 동기화를 위한 데이터 유형은 생성 후에는 변경할 수 없습니다.
{% endtab %}
{% tab BigQuery %}

Braze 대시보드에서 **데이터 설정** > **클라우드 데이터 수집으로** 이동하여 **새 데이터 동기화 만들기를** 선택한 다음 **Google BigQuery 가져오기를** 선택합니다.

#### 2.1단계: BigQuery 연결 정보 및 소스 테이블 추가

JSON 키를 업로드하고 서비스 계정의 이름을 입력한 다음 소스 테이블의 세부 정보를 입력합니다.

Braze 대시보드의 BigQuery에 대한 "새 가져오기 동기화 만들기" 페이지에서 1단계로 설정합니다: "연결 설정".]({% image_buster /assets/img/cloud_ingestion/ingestion_11.png %})

#### 2.2단계: 동기화 세부 정보 구성

다음으로 동기화할 이름을 선택하고 연락처 이메일을 입력합니다. 이 연락처 정보를 사용하여 테이블에 대한 액세스 권한이 예기치 않게 제거되는 등의 통합 오류가 발생하면 알려드립니다.

연락처 이메일은 누락된 테이블, 권한 등과 같은 전역 또는 동기화 수준 오류에 대한 알림만 수신합니다. 행 수준 이슈는 수신되지 않습니다. 전역 오류는 동기화를 실행할 수 없는 연결에 심각한 문제가 있음을 나타냅니다. 이러한 문제에는 다음이 포함될 수 있습니다:

- 연결 문제
- 리소스 부족
- 권한 문제
- (카탈로그 동기화에만 해당) 카탈로그 계층에 공간이 부족합니다.

2단계로 설정된 Braze 대시보드의 BigQuery에 대한 "새 가져오기 동기화 만들기" 페이지로 이동합니다: "동기화 세부 정보 설정".]({% image_buster /assets/img/cloud_ingestion/ingestion_12.png %})

데이터 유형과 동기화 빈도도 선택할 수 있습니다. 빈도는 15분마다부터 한 달에 한 번까지 다양합니다. Braze 대시보드에 구성된 시간대를 사용하여 반복 동기화를 예약합니다. 지원되는 데이터 유형은 커스텀 속성, 커스텀 이벤트, 구매 이벤트, 사용자 삭제입니다. 동기화를 위한 데이터 유형은 생성 후에는 변경할 수 없습니다. 

{% endtab %}
{% tab Databricks %}

Braze 대시보드에서 **데이터 설정** > **클라우드 데이터 수집으로** 이동하여 **새 데이터 동기화 만들기를** 선택한 다음 **데이터 브릭스 가져오기를** 선택합니다.

#### 2.1단계: 데이터브릭스 연결 정보 및 소스 테이블 추가하기

데이터브릭스 데이터 웨어하우스 및 소스 테이블에 대한 정보를 입력한 후 다음 단계로 진행합니다.

Braze 대시보드에서 데이터브릭에 대한 "새 가져오기 동기화 만들기" 페이지에서 1단계로 설정합니다: "연결 설정".]({% image_buster /assets/img/cloud_ingestion/ingestion_16.png %})

#### 2.2단계: 동기화 세부 정보 구성

다음으로 동기화할 이름을 선택하고 연락처 이메일을 입력합니다. 이 연락처 정보를 사용하여 테이블에 대한 액세스 권한이 예기치 않게 제거되는 등의 통합 오류가 발생하면 알려드립니다.

연락처 이메일은 누락된 테이블, 권한 등과 같은 전역 또는 동기화 수준 오류에 대한 알림만 수신합니다. 행 수준 이슈는 수신되지 않습니다. 전역 오류는 동기화를 실행할 수 없는 연결에 심각한 문제가 있음을 나타냅니다. 이러한 문제에는 다음이 포함될 수 있습니다:

- 연결 문제
- 리소스 부족
- 권한 문제
- (카탈로그 동기화에만 해당) 카탈로그 계층에 공간이 부족합니다.

Braze 대시보드에서 데이터브릭에 대한 "새 가져오기 동기화 만들기" 페이지를 2단계로 설정합니다: "동기화 세부 정보 설정".]({% image_buster /assets/img/cloud_ingestion/ingestion_12.png %})

데이터 유형과 동기화 빈도도 선택할 수 있습니다. 빈도는 15분마다부터 한 달에 한 번까지 다양합니다. Braze 대시보드에 구성된 시간대를 사용하여 반복 동기화를 예약합니다. 지원되는 데이터 유형은 커스텀 속성, 커스텀 이벤트, 구매 이벤트, 사용자 삭제입니다. 동기화를 위한 데이터 유형은 생성 후에는 변경할 수 없습니다. 

{% endtab %}
{% tab Microsoft Fabric %}

#### 2.1단계: 클라우드 데이터 수집 동기화 설정하기

Microsoft 패브릭에 대한 새 데이터 동기화를 만듭니다. Braze 대시보드에서 **데이터 설정** > **클라우드 데이터 수집으로** 이동하고, **새 데이터 동기화 만들기를** 선택한 다음, **Microsoft 패브릭 가져오기를** 선택합니다.

#### 2.2단계: Microsoft 패브릭 연결 정보 및 소스 테이블 추가

Microsoft Fabric 웨어하우스 자격 증명 및 소스 테이블에 대한 정보를 입력한 다음 다음 단계로 진행합니다.

- 자격 증명 이름은 Braze에서 이러한 자격 증명을 위한 레이블이며, 여기에서 유용한 값을 설정할 수 있습니다.
- 테넌트 ID, Principal ID, 클라이언트 비밀 및 연결 문자열을 검색하는 방법에 대한 자세한 내용은 섹션 1의 단계를 참조하세요.

Braze 대시보드의 Microsoft용 '새 가져오기 동기화 만들기' 페이지에서 1단계로 설정합니다: "연결 설정".]({% image_buster /assets/img/cloud_ingestion/fabric_setup_1.png %})

#### 2.3단계: 동기화 세부 정보 구성

다음으로 동기화에 대한 다음 세부 정보를 구성합니다: 

- 동기화 이름 
- 데이터 유형 - 지원되는 데이터 유형은 커스텀 속성, 커스텀 이벤트, 구매 이벤트, 카탈로그 및 사용자 삭제입니다. 동기화를 위한 데이터 유형은 생성 후에는 변경할 수 없습니다. 
- 동기화 빈도 - 15분마다에서 한 달에 한 번까지 빈도를 지정할 수 있습니다. Braze 대시보드에 구성된 시간대를 사용하여 반복 동기화를 예약합니다. 
  - 비반복 동기화는 수동으로 또는 [API를]({{site.baseurl}}/api/endpoints/cdi) 통해 트리거할 수 있습니다. 

Braze 대시보드의 Microsoft Fabric에 대한 "새 가져오기 동기화 만들기" 페이지에서 2단계로 설정합니다: "동기화 세부 정보 설정".]({% image_buster /assets/img/cloud_ingestion/fabric_setup_2.png %})


#### 2.4단계: 알림 환경설정 구성

다음으로 연락처 이메일을 입력합니다. 이 연락처 정보를 사용하여 테이블에 대한 액세스 권한이 예기치 않게 제거되는 등의 통합 오류를 알리거나 특정 행이 업데이트되지 않을 때 알림을 보내드립니다.

기본값으로 연락처 이메일은 누락된 테이블, 권한 등과 같은 전역 또는 동기화 수준 오류에 대한 알림만 수신합니다. 전역 오류는 동기화를 실행할 수 없는 연결에 심각한 문제가 있음을 나타냅니다. 이러한 문제에는 다음이 포함될 수 있습니다:

- 연결 문제
- 리소스 부족
- 권한 문제
- (카탈로그 동기화에만 해당) 카탈로그 계층에 공간이 부족합니다.

행 수준 문제에 대한 알림을 구성하거나 동기화가 성공적으로 실행될 때마다 알림을 받도록 선택할 수도 있습니다. 

Braze 대시보드의 Microsoft Fabric에 대한 "새 가져오기 동기화 만들기" 페이지에서 3단계로 설정합니다: "알림 환경설정 설정하기".]({% image_buster /assets/img/cloud_ingestion/fabric_setup_3.png %})


{% endtab %}

{% endtabs %}

### 3단계: 연결 테스트

{% tabs %}
{% tab Snowflake %}

Braze 대시보드로 돌아와 **연결 테스트를** 선택합니다. 성공하면 데이터 미리보기가 표시됩니다. 어떤 이유로 연결할 수 없는 경우 문제 해결을 돕기 위해 오류 메시지가 표시됩니다.

3단계로 Braze 대시보드의 Snowflake에 대한 "새 가져오기 동기화 만들기" 페이지가 표시됩니다: "연결 테스트"는 RSA 공개 키를 표시합니다.]({% image_buster /assets/img/cloud_ingestion/ingestion_3.png %})
{% endtab %}

{% tab Redshift %}
{% subtabs local %}
{% subtab Public Network %}
Braze 대시보드로 돌아와 **연결 테스트를** 선택합니다. 성공하면 데이터 미리보기가 표시됩니다. 어떤 이유로 연결할 수 없는 경우 문제 해결을 돕기 위해 오류 메시지가 표시됩니다.

Braze 대시보드의 Redshift에 대한 "새 가져오기 동기화 만들기" 페이지에서 3단계로 설정합니다: "연결 테스트".]({% image_buster /assets/img/cloud_ingestion/ingestion_8.png %})
{% endsubtab %}

{% subtab Private Network %}
Braze 대시보드로 돌아와 **연결 테스트를** 선택합니다. 성공하면 데이터 미리보기가 표시됩니다. 어떤 이유로 연결할 수 없는 경우 문제 해결을 돕기 위해 오류 메시지가 표시됩니다.

Braze 대시보드의 Redshift 사설 네트워크에 대한 "새 가져오기 동기화 만들기" 페이지에 4단계가 표시됩니다: "연결 테스트"는 RSA 공개 키를 표시합니다.]({% image_buster /assets/img/cloud_ingestion/ingestion_19.png %})
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab BigQuery %}

동기화에 대한 모든 구성 세부 정보를 입력한 후 **연결 테스트를** 선택합니다. 성공하면 데이터 미리보기가 표시됩니다. 어떤 이유로 연결할 수 없는 경우 문제 해결을 돕기 위해 오류 메시지가 표시됩니다.

Braze 대시보드의 BigQuery에 대한 "새 가져오기 동기화 만들기" 페이지에서 3단계로 설정합니다: "연결 테스트".]({% image_buster /assets/img/cloud_ingestion/ingestion_13.png %})

{% endtab %}

{% tab Databricks %}

동기화에 대한 모든 구성 세부 정보를 입력한 후 **연결 테스트를** 선택합니다. 성공하면 데이터 미리보기가 표시됩니다. 어떤 이유로 연결할 수 없는 경우 문제 해결을 돕기 위해 오류 메시지가 표시됩니다.

Braze 대시보드에서 데이터브릭에 대한 "새 가져오기 동기화 만들기" 페이지를 3단계로 설정합니다: "연결 테스트".]({% image_buster /assets/img/cloud_ingestion/ingestion_13.png %})

{% endtab %}
{% tab Microsoft Fabric %}

동기화에 대한 모든 구성 세부 정보를 입력한 후 **연결 테스트를** 선택합니다. 성공하면 데이터 미리보기가 표시됩니다. 어떤 이유로 연결할 수 없는 경우 문제 해결을 돕기 위해 오류 메시지가 표시됩니다.

Braze 대시보드의 Microsoft Fabric에 대한 "새 가져오기 동기화 만들기" 페이지에서 4단계로 설정합니다: "연결 테스트".]({% image_buster /assets/img/cloud_ingestion/fabric_setup_4.png %})

{% endtab %}
{% endtabs %}

{% alert note %}
통합을 성공적으로 테스트해야 초안에서 활성 상태로 전환할 수 있습니다. 생성 페이지에서 닫아야 하는 경우 통합이 저장되며 세부 정보 페이지를 다시 방문하여 변경하고 테스트할 수 있습니다.  
{% endalert %}

## 추가 통합 또는 사용자 설정(선택 사항)

{% tabs %}
{% tab Snowflake %}
Braze와 여러 통합을 설정할 수 있지만 각 통합은 서로 다른 테이블을 동기화하도록 구성해야 합니다. 추가 동기화를 만들 때 Snowflake 계정에 연결할 경우 기존 자격 증명을 재사용할 수 있습니다.

1단계에서 '자격 증명 선택' 드롭다운이 열려 있는 Braze 대시보드의 Snowflake에 대한 '새 가져오기 동기화 만들기' 페이지가 열립니다: "연결 설정".]({% image_buster /assets/img/cloud_ingestion/ingestion_4.png %})

여러 통합에서 동일한 사용자 및 역할을 재사용하는 경우 공개 키를 다시 추가하는 단계를 거치지 **않아도** 됩니다.
{% endtab %}
{% tab Redshift %}
Braze와 여러 통합을 설정할 수 있지만 각 통합은 서로 다른 테이블을 동기화하도록 구성해야 합니다. 추가 동기화를 만들 때 동일한 Snowflake 또는 Redshift 계정에 연결할 경우 기존 자격 증명을 재사용할 수 있습니다.

1단계에서 '자격 증명 선택' 드롭다운이 열려 있는 Braze 대시보드의 Redshift에 대한 '새 가져오기 동기화 만들기' 페이지가 열립니다: "연결 설정".]({% image_buster /assets/img/cloud_ingestion/ingestion_9.png %})

여러 통합에서 동일한 사용자를 재사용하는 경우, 모든 활성 동기화에서 해당 사용자가 제거될 때까지는 Braze 대시보드에서 해당 사용자를 삭제할 수 없습니다.
{% endtab %}
{% tab BigQuery %}

Braze와 여러 통합을 설정할 수 있지만 각 통합은 서로 다른 테이블을 동기화하도록 구성해야 합니다. 추가 동기화를 만들 때 동일한 BigQuery 계정에 연결하는 경우 기존 자격 증명을 재사용할 수 있습니다.

1단계에서 '자격 증명 선택' 드롭다운이 열려 있는 Braze 대시보드의 BigQuery에 대한 '새 가져오기 동기화 만들기' 페이지가 열립니다: "연결 설정".]({% image_buster /assets/img/cloud_ingestion/ingestion_14.png %})

여러 통합에서 동일한 사용자를 재사용하는 경우, 모든 활성 동기화에서 해당 사용자가 제거될 때까지는 Braze 대시보드에서 해당 사용자를 삭제할 수 없습니다.

{% endtab %}
{% tab Databricks %}

Braze와 여러 통합을 설정할 수 있지만 각 통합은 서로 다른 테이블을 동기화하도록 구성해야 합니다. 추가 동기화를 생성할 때 동일한 데이터브릭스 계정에 연결하는 경우 기존 자격 증명을 재사용할 수 있습니다.

1단계에서 '자격 증명 선택' 드롭다운이 열려 있는 Braze 대시보드의 데이터브릭스용 '새 가져오기 동기화 만들기' 페이지가 열립니다: "연결 설정".]({% image_buster /assets/img/cloud_ingestion/ingestion_17.png %})

여러 통합에서 동일한 사용자를 재사용하는 경우, 모든 활성 동기화에서 해당 사용자가 제거될 때까지는 Braze 대시보드에서 해당 사용자를 삭제할 수 없습니다.

{% endtab %}
{% tab Microsoft Fabric %}

Braze와 여러 통합을 설정할 수 있지만 각 통합은 서로 다른 테이블을 동기화하도록 구성해야 합니다. 추가 동기화를 생성할 때 동일한 Fabric 계정에 연결하는 경우 기존 자격 증명을 재사용할 수 있습니다.

여러 통합에서 동일한 사용자를 재사용하는 경우, 모든 활성 동기화에서 해당 사용자가 제거될 때까지는 Braze 대시보드에서 해당 사용자를 삭제할 수 없습니다.

{% endtab %}
{% endtabs %}

## 동기화 실행

{% tabs %}
{% tab Snowflake %}
동기화를 활성화하면 설정 중에 구성한 일정에 따라 동기화가 실행됩니다. 일반 테스트 일정 외에 동기화를 실행하거나 가장 최신 데이터를 가져오려면 **지금 동기화를** 선택하세요. 이 실행은 향후 정기적으로 예정된 동기화에 영향을 미치지 않습니다.

\![수직 타원 메뉴에서 '지금 동기화' 옵션이 표시된 Braze 대시보드의 Snowflake에 대한 '데이터 가져오기' 페이지.]({% image_buster /assets/img/cloud_ingestion/ingestion_5.png %})

{% endtab %}
{% tab Redshift %}
동기화를 활성화하면 설정 중에 구성한 일정에 따라 동기화가 실행됩니다. 일반 테스트 일정 외에 동기화를 실행하거나 가장 최신 데이터를 가져오려면 **지금 동기화를** 선택하세요. 이 실행은 향후 정기적으로 예정된 동기화에 영향을 미치지 않습니다.

\![수직 타원 메뉴에서 '지금 동기화' 옵션이 표시된 Braze 대시보드의 Redshift용 '데이터 가져오기' 페이지.]({% image_buster /assets/img/cloud_ingestion/ingestion_10.png %})

{% endtab %}
{% tab BigQuery %}

동기화를 활성화하면 설정 중에 구성한 일정에 따라 동기화가 실행됩니다. 일반 테스트 일정 외에 동기화를 실행하거나 가장 최신 데이터를 가져오려면 **지금 동기화를** 선택하세요. 이 실행은 향후 정기적으로 예정된 동기화에 영향을 미치지 않습니다.

\![수직 타원 메뉴에서 '지금 동기화' 옵션이 표시된 Braze 대시보드의 BigQuery용 '데이터 가져오기' 페이지.]({% image_buster /assets/img/cloud_ingestion/ingestion_15.png %})

{% endtab %}
{% tab Databricks %}

동기화를 활성화하면 설정 중에 구성한 일정에 따라 동기화가 실행됩니다. 일반 테스트 일정 외에 동기화를 실행하거나 가장 최신 데이터를 가져오려면 **지금 동기화를** 선택하세요. 이 실행은 향후 정기적으로 예정된 동기화에 영향을 미치지 않습니다.

Braze 대시보드의 데이터 브릭에 대한 '데이터 가져오기' 페이지에서 세로 타원 메뉴의 '지금 동기화' 옵션이 표시됩니다.]({% image_buster /assets/img/cloud_ingestion/ingestion_18.png %})

{% endtab %}
{% tab Microsoft Fabric %}

동기화를 활성화하면 설정 중에 구성한 일정에 따라 동기화가 실행됩니다. 일반 테스트 일정 외에 동기화를 실행하거나 가장 최신 데이터를 가져오려면 **지금 동기화를** 선택하세요. 이 실행은 향후 정기적으로 예정된 동기화에 영향을 미치지 않습니다.

{% endtab %}

{% endtabs %}

