---
nav_title: 데이터 웨어하우스 통합
article_title: 데이터 웨어하우스 통합
alias: /partners/databricks/
description: "이 페이지에서는 Braze 클라우드 데이터 수집을 사용하여 관련 데이터를 Snowflake, Redshift, BigQuery 및 Databricks 통합과 동기화하는 방법에 대해 설명합니다."
page_order: 2
page_type: reference

---

# 데이터 웨어하우스 스토리지 통합

> 이 페이지에서는 Braze 클라우드 데이터 수집(CDI)을 사용하여 Snowflake, Redshift, BigQuery 및 Databricks 통합과 관련 데이터를 동기화하는 방법에 대해 설명합니다.

## 데이터 웨어하우스 통합 설정

클라우드 데이터 수집 통합은 Braze 측과 데이터 웨어하우스 인스턴스에서 일부 설정이 필요합니다. 다음 단계를 따라 통합을 설정하십시오:

{% tabs %}
{% tab Snowflake %}
1. Snowflake 인스턴스에서 Braze와 동기화하려는 테이블 또는 뷰를 설정하십시오.
2. Braze 대시보드에서 새 통합을 생성합니다.
3. Braze 대시보드에 제공된 공개 키를 검색하고 [Snowflake 사용자에게 인증을 위해 추가합니다](https://docs.snowflake.com/en/user-guide/key-pair-auth.html).
4. 통합을 테스트하고 동기화를 시작하십시오.

{% alert tip %}
[Snowflake 빠른 시작 가이드](https://quickstarts.snowflake.com/guide/braze_cdi/index.html)에서는 샘플 코드를 제공하고, Snowflake Streams와 CDI를 사용하여 데이터를 Braze에 동기화하는 자동화된 파이프라인을 만드는 데 필요한 단계를 안내합니다.
{% endalert %}
{% endtab %}
{% tab Redshift %}
1. Braze가 동기화하려는 Redshift 테이블에 액세스할 수 있는지 확인하십시오. Braze는 인터넷을 통해 Redshift에 연결됩니다.
2. Redshift 인스턴스에서 Braze에 동기화하려는 테이블 또는 뷰를 설정합니다.
3. Braze 대시보드에서 새 통합을 생성합니다.
4. 통합을 테스트하고 동기화를 시작하십시오.
{% endtab %}
{% tab BigQuery %}
1. 서비스 계정을 만들고 동기화하려는 데이터가 포함된 BigQuery 프로젝트 및 데이터 세트에 대한 액세스를 허용합니다.  
2. BigQuery 계정에서 Braze에 동기화하려는 테이블 또는 뷰를 설정합니다.   
3. Braze 대시보드에서 새 통합을 생성합니다.  
4. 통합을 테스트하고 동기화를 시작하십시오.  
{% endtab %}
{% tab Databricks %}
1. 서비스 계정을 만들고 동기화하려는 데이터를 포함하는 Databricks 프로젝트 및 데이터 세트에 대한 액세스를 허용합니다.  
2. Databricks 계정에서 Braze와 동기화하려는 테이블 또는 뷰를 설정하세요.   
3. Braze 대시보드에서 새 통합을 생성합니다.  
4. 통합을 테스트하고 동기화를 시작하십시오.

{% alert important %}
Braze가 Classic 및 Pro SQL 인스턴스에 연결될 때 2~5분의 준비 시간이 있을 수 있으며, 이로 인해 연결 설정 및 테스트 중뿐만 아니라 예약된 동기화 시작 시에도 지연이 발생할 수 있습니다. 서버리스 SQL 인스턴스를 사용하면 워밍업 시간을 최소화하고 쿼리 처리량을 향상시킬 수 있지만, 통합 비용이 약간 증가할 수 있습니다.
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}
1. 서비스 주체를 만들고 통합에 사용할 Fabric 작업 영역에 대한 액세스를 허용합니다.   
2. Fabric 작업 영역에서 Braze에 동기화할 테이블 또는 뷰를 설정합니다.   
3. Braze 대시보드에서 새 통합을 생성합니다.  
4. 통합을 테스트하고 동기화를 시작하십시오.
{% endtab %}
{% endtabs %}

### 1단계: 테이블 또는 뷰 설정

{% tabs %}
{% tab Snowflake %}

#### 1.1단계: 테이블 설정

```sql
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
     --If you include both email and phone, email is used as the primary identifier
     EMAIL VARCHAR(16777216),
     PHONE VARCHAR(16777216),
     PAYLOAD VARCHAR(16777216) NOT NULL
);
```

데이터베이스, 스키마 및 테이블의 이름은 원하는 대로 지정할 수 있지만, 열 이름은 앞서 정의한 것과 일치해야 합니다.

- `UPDATED_AT` - 이 행이 테이블에 업데이트되거나 추가된 시간입니다. 마지막 동기화 이후 추가되거나 업데이트된 행만 동기화됩니다.
- **사용자 식별자 열** - 테이블에는 하나 이상의 사용자 식별자 열이 포함될 수 있습니다. 각 행에는 하나의 식별자(`external_id`, `alias_name`과 `alias_label`의 조합, `braze_id`, `email` 또는 `phone`)만 포함해야 합니다. 소스 테이블에는 하나, 둘, 셋, 넷 또는 다섯 가지 식별자 유형 모두에 대한 열이 있을 수 있습니다.
    - `EXTERNAL_ID` - 업데이트하려는 사용자를 식별합니다. 이 값은 Braze에서 사용하는 `external_id` 값과 일치해야 합니다. 
    - `ALIAS_NAME` 및 `ALIAS_LABEL` - 이 두 열은 사용자 별칭 객체를 만듭니다. `alias_name`은 고유 식별자이고 `alias_label`은 별칭의 유형을 지정합니다. 사용자는 여러 레이블이 있는 여러 별칭을 가질 수 있지만 `alias_label`당 하나의 `alias_name`만 가질 수 있습니다.
    - `BRAZE_ID` - Braze 사용자 식별자입니다. 이것은 Braze 소프트웨어 개발 키트에 의해 생성되며, 새로운 사용자는 클라우드 데이터 수집을 통해 Braze ID로 생성할 수 없습니다. 새 사용자를 만들려면 외부 사용자 ID 또는 사용자 별칭을 지정합니다.
    - `EMAIL` - 사용자의 이메일 주소입니다. 동일한 이메일 주소를 가진 프로필이 여러 개 있는 경우 가장 최근에 업데이트된 프로필이 업데이트 우선순위를 갖습니다. 이메일과 전화번호를 모두 포함하는 경우 이메일이 기본 식별자로 사용됩니다.
    - `PHONE` - 사용자의 전화번호입니다. 동일한 전화번호를 사용하는 프로필이 여러 개 있는 경우 가장 최근에 업데이트된 프로필이 업데이트 우선순위를 갖습니다.
- `PAYLOAD` - Braze에서 사용자와 동기화하려는 필드의 JSON 문자열입니다.

#### 1.2단계: 역할 및 데이터베이스 권한 설정

```sql
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;
```

이름을 필요에 따라 업데이트하되, 권한은 이전 예와 일치해야 합니다.

#### 1.3단계: 웨어하우스를 설정하고 Braze 역할에 액세스 권한 부여

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
웨어하우스에 **자동 재개** 플래그가 설정되어 있어야 합니다. 그렇지 않으면, 쿼리를 실행할 때 이를 켜기 위해 웨어하우스에 대한 추가 `OPERATE` 권한을 Braze에 부여해야 합니다.
{% endalert %}

#### 1.4단계: 사용자 설정

```sql
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

이 단계를 완료한 후 Braze와 연결 정보를 공유하고 사용자에게 추가할 공개 키를 받게 됩니다.

{% alert note %}
다른 워크스페이스를 동일한 Snowflake 계정에 연결할 때, 통합을 생성하는 각 Braze 워크스페이스에 고유한 사용자를 생성해야 합니다. 워크스페이스 내에서 동일한 사용자를 통합 간에 재사용할 수 있지만, 동일한 Snowflake 계정의 사용자가 워크스페이스 간에 중복되면 통합 생성이 실패합니다.
{% endalert %}

#### 1.5단계: Snowflake 네트워크 정책에서 Braze IP 허용(선택 사항)

Snowflake 계정의 구성에 따라 Snowflake 네트워크 정책에서 다음 IP 주소를 허용해야 할 수 있습니다. 자세한 내용은 [네트워크 정책 수정](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies)에 대한 관련 Snowflake 설명서를 참조하세요.

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Redshift %}

#### 1.1단계: 테이블 설정 

선택적으로 소스 테이블을 보유할 새 데이터베이스 및 스키마를 설정하세요
```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```
CDI 통합에 사용할 테이블(또는 뷰)을 만드십시오
```sql
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
   updated_at timestamptz default sysdate,
   --at least one of external_id, alias_name and alias_label, or braze_id is required
   external_id varchar,
   --if using user alias, both alias_name and alias_label are required
   alias_label varchar,
   alias_name varchar,
   --braze_id can only be used to update existing users created through the Braze SDK
   braze_id varchar,
   --If you include both email and phone, email is used as the primary identifier
   email varchar,
   phone varchar,
   payload varchar(max)
)
```

데이터베이스, 스키마 및 테이블의 이름은 원하는 대로 지정할 수 있지만, 열 이름은 앞서 정의한 것과 일치해야 합니다.

- `UPDATED_AT` - 이 행이 테이블에 업데이트되거나 추가된 시간입니다. 마지막 동기화 이후 추가되거나 업데이트된 행만 동기화됩니다.
- **사용자 식별자 열** - 테이블에는 하나 이상의 사용자 식별자 열이 포함될 수 있습니다. 각 행에는 하나의 식별자(`external_id`, `alias_name`과 `alias_label`의 조합, `braze_id`, `email` 또는 `phone`)만 포함해야 합니다. 소스 테이블에는 하나, 둘, 셋, 넷 또는 다섯 가지 식별자 유형 모두에 대한 열이 있을 수 있습니다.
    - `EXTERNAL_ID` - 업데이트하려는 사용자를 식별합니다. 이 값은 Braze에서 사용하는 `external_id` 값과 일치해야 합니다. 
    - `ALIAS_NAME` 및 `ALIAS_LABEL` - 이 두 열은 사용자 별칭 객체를 만듭니다. `alias_name`은 고유 식별자이고 `alias_label`은 별칭의 유형을 지정합니다. 사용자는 여러 레이블이 있는 여러 별칭을 가질 수 있지만 `alias_label`당 하나의 `alias_name`만 가질 수 있습니다.
    - `BRAZE_ID` - Braze 사용자 식별자입니다. 이것은 Braze 소프트웨어 개발 키트에 의해 생성되며, 새로운 사용자는 클라우드 데이터 수집을 통해 Braze ID로 생성할 수 없습니다. 새 사용자를 만들려면 외부 사용자 ID 또는 사용자 별칭을 지정합니다.
    - `EMAIL` - 사용자의 이메일 주소입니다. 동일한 이메일 주소를 가진 프로필이 여러 개 있는 경우 가장 최근에 업데이트된 프로필이 업데이트 우선순위를 갖습니다. 이메일과 전화번호를 모두 포함하는 경우 이메일이 기본 식별자로 사용됩니다.
    - `PHONE` - 사용자의 전화번호입니다. 동일한 전화번호를 사용하는 프로필이 여러 개 있는 경우 가장 최근에 업데이트된 프로필이 업데이트 우선순위를 갖습니다.
- `PAYLOAD` - Braze에서 사용자와 동기화하려는 필드의 JSON 문자열입니다.
 
#### 1.2단계: 사용자 생성 및 권한 부여

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

이 사용자에게 필요한 최소 권한입니다. 여러 CDI 통합을 생성하는 경우 스키마에 대한 권한을 부여하거나 그룹을 사용하여 권한을 관리할 수 있습니다. 

#### 1.3단계: Braze IP에 대한 액세스 허용

방화벽이나 기타 네트워크 정책이 있는 경우 Braze 네트워크에 Redshift 인스턴스에 대한 액세스 권한을 부여해야 합니다. Redshift URL 엔드포인트의 예는 "example-cluster.ap-northeast-2.redshift.amazonaws.com"입니다.

알아야 할 중요한 사항들:
- Braze가 Redshift에서 데이터에 액세스할 수 있도록 보안 그룹을 변경해야 할 수도 있습니다.
- IP 테이블과 Redshift 클러스터를 쿼리하는 데 사용되는 포트(기본값은 5439)에서 인바운드 트래픽을 명시적으로 허용해야 합니다. 인바운드 규칙이 "모두 허용"으로 설정되어 있더라도 이 포트에서 Redshift TCP 연결을 명시적으로 허용해야 합니다.
- Braze가 클러스터에 연결할 수 있도록 Redshift 클러스터의 엔드포인트는 공개적으로 접근 가능해야 합니다.
     - Redshift 클러스터를 공개적으로 액세스할 수 없도록 하려면 VPC와 EC2 인스턴스를 설정하여 SSH 터널을 사용하여 Redshift 데이터에 액세스할 수 있습니다. 자세한 내용은 이 [AWS 지식 센터 게시물](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine)을 확인하세요.
 
다음 IP에서 Braze 대시보드의 지역에 해당하는 액세스를 허용합니다.

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab BigQuery %}

#### 1.1단계: 테이블 설정 

선택적으로 소스 테이블을 보유할 새 프로젝트 또는 데이터 세트를 설정합니다.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

다음 필드를 사용하여 CDI 통합에 사용할 하나 이상의 테이블을 만드세요:

```sql
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
  --If you include both email and phone, email is used as the primary identifier
  email STRING,
  phone STRING,
  payload JSON
);
```

| 필드 이름 | 유형 | 모드 |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUIRED |
| `PAYLOAD`| JSON | REQUIRED |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
| `EMAIL`| STRING | NULLABLE |
| `PHONE`| STRING | NULLABLE |

프로젝트, 데이터셋 및 테이블의 이름은 원하는 대로 지정할 수 있지만, 열 이름은 앞서 정의한 것과 일치해야 합니다.

- `UPDATED_AT` - 이 행이 테이블에 업데이트되거나 추가된 시간입니다. 마지막 동기화 이후 추가되거나 업데이트된 행만 동기화됩니다.
- **사용자 식별자 열** - 테이블에는 하나 이상의 사용자 식별자 열이 포함될 수 있습니다. 각 행에는 하나의 식별자(`external_id`, `alias_name`과 `alias_label`의 조합, `braze_id`, `email` 또는 `phone`)만 포함해야 합니다. 소스 테이블에는 하나, 둘, 셋, 넷 또는 다섯 가지 식별자 유형 모두에 대한 열이 있을 수 있습니다.
    - `EXTERNAL_ID` - 업데이트하려는 사용자를 식별합니다. 이 값은 Braze에서 사용하는 `external_id` 값과 일치해야 합니다. 
    - `ALIAS_NAME` 및 `ALIAS_LABEL` - 이 두 열은 사용자 별칭 객체를 만듭니다. `alias_name`은 고유 식별자이고 `alias_label`은 별칭의 유형을 지정합니다. 사용자는 여러 레이블이 있는 여러 별칭을 가질 수 있지만 `alias_label`당 하나의 `alias_name`만 가질 수 있습니다.
    - `BRAZE_ID` - Braze 사용자 식별자입니다. 이것은 Braze 소프트웨어 개발 키트에 의해 생성되며, 새로운 사용자는 클라우드 데이터 수집을 통해 Braze ID로 생성할 수 없습니다. 새 사용자를 만들려면 외부 사용자 ID 또는 사용자 별칭을 지정합니다.
    - `EMAIL` - 사용자의 이메일 주소입니다. 동일한 이메일 주소를 가진 프로필이 여러 개 있는 경우 가장 최근에 업데이트된 프로필이 업데이트 우선순위를 갖습니다. 이메일과 전화번호를 모두 포함하는 경우 이메일이 기본 식별자로 사용됩니다.
    - `PHONE` - 사용자의 전화번호입니다. 동일한 전화번호를 사용하는 프로필이 여러 개 있는 경우 가장 최근에 업데이트된 프로필이 업데이트 우선순위를 갖습니다.
- `PAYLOAD` - Braze에서 사용자와 동기화하려는 필드의 JSON 문자열입니다.

{% alert important %}
**BigQuery 파티셔닝**

CDI는 BigQuery용 파티션을 지원합니다. `UPDATED_AT` 함수로 파티션을 분할하는 경우(예: 데이터 세트의 크기에 따라 일, 주 또는 시간 단위로), BigQuery는 스캔해야 하는 데이터를 잘라낼 수 있습니다. 이렇게 하면 초대형 테이블의 성능과 효율성이 향상됩니다.

다른 필드로 파티션을 나누지 마세요. 다양한 구성을 테스트하여 특정 데이터에 가장 적합한 설정을 찾아보세요.

모든 CDI 쿼리는 `UPDATED_AT`으로 필터링되지만 이 동작은 변경될 수 있습니다. 쿼리에 이 절이 _포함되지 않아도 되도록_ 테이블 스키마를 설계하세요.

자세한 내용은 [BigQuery 파티셔닝 설명서](https://docs.cloud.google.com/bigquery/docs/partitioned-tables)를 참조하세요.
{% endalert %}

#### 1.2단계: 서비스 계정 생성 및 권한 부여 

GCP에서 Braze가 테이블에서 데이터를 연결하고 읽을 수 있도록 서비스 계정을 만드세요. 서비스 계정에는 아래 권한이 있어야 합니다: 

- **BigQuery Connection User:** Braze가 연결을 만들 수 있게 해줍니다
- **BigQuery User:** Braze가 쿼리를 실행하고, 데이터셋 메타데이터를 읽고, 테이블을 나열할 수 있도록 합니다.
- **BigQuery Data Viewer:** Braze가 데이터 세트와 그 내용을 볼 수 있는 액세스 권한을 제공합니다.
- **BigQuery Job User:** Braze에 작업을 실행할 수 있는 권한을 부여합니다

서비스 계정을 생성하고 권한을 부여한 후, JSON 키를 생성합니다. 자세한 방법은 [여기](https://cloud.google.com/iam/docs/keys-create-delete)에서 확인하세요. 나중에 Braze 대시보드에 업로드할 것입니다. 

#### 1.3단계: Braze IP에 대한 액세스 허용    

네트워크 정책이 있는 경우 Braze 네트워크에 BigQuery 인스턴스에 대한 액세스 권한을 부여해야 합니다. 아래 IP에서 Braze 대시보드의 지역에 해당하는 액세스를 허용합니다.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Databricks %}

#### 1.1단계: 테이블 설정 

선택적으로 소스 테이블을 보유할 새 카탈로그 또는 스키마를 설정하십시오.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

다음 필드를 사용하여 CDI 통합에 사용할 하나 이상의 테이블을 만드세요:


```sql
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
  --If you include both email and phone, email is used as the primary identifier
  email STRING,
  phone STRING,
  payload STRING, STRUCT, or MAP
);
```


| 필드 이름 | 유형 | 모드 |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUIRED |
| `PAYLOAD`| STRING, STRUCT, or MAP | REQUIRED |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
| `EMAIL`| STRING | NULLABLE |
| `PHONE`| STRING | NULLABLE |

스키마와 테이블의 이름은 원하는 대로 지정할 수 있지만, 열 이름은 앞서 정의한 것과 일치해야 합니다.

- `UPDATED_AT` - 이 행이 테이블에 업데이트되거나 추가된 시간입니다. 마지막 동기화 이후 추가되거나 업데이트된 행만 동기화됩니다.
- **사용자 식별자 열** - 테이블에는 하나 이상의 사용자 식별자 열이 포함될 수 있습니다. 각 행에는 하나의 식별자(`external_id`, `alias_name`과 `alias_label`의 조합, `braze_id`, `email` 또는 `phone`)만 포함해야 합니다. 소스 테이블에는 하나, 둘, 셋, 넷 또는 다섯 가지 식별자 유형 모두에 대한 열이 있을 수 있습니다.
    - `EXTERNAL_ID` - 업데이트하려는 사용자를 식별합니다. 이 값은 Braze에서 사용하는 `external_id` 값과 일치해야 합니다. 
    - `ALIAS_NAME` 및 `ALIAS_LABEL` - 이 두 열은 사용자 별칭 객체를 만듭니다. `alias_name`은 고유 식별자이고 `alias_label`은 별칭의 유형을 지정합니다. 사용자는 여러 레이블이 있는 여러 별칭을 가질 수 있지만 `alias_label`당 하나의 `alias_name`만 가질 수 있습니다.
    - `BRAZE_ID` - Braze 사용자 식별자입니다. 이것은 Braze 소프트웨어 개발 키트에 의해 생성되며, 새로운 사용자는 클라우드 데이터 수집을 통해 Braze ID로 생성할 수 없습니다. 새 사용자를 만들려면 외부 사용자 ID 또는 사용자 별칭을 지정합니다. 
    - `EMAIL` - 사용자의 이메일 주소입니다. 동일한 이메일 주소를 가진 프로필이 여러 개 있는 경우 가장 최근에 업데이트된 프로필이 업데이트 우선순위를 갖습니다. 이메일과 전화번호를 모두 포함하는 경우 이메일이 기본 식별자로 사용됩니다.
    - `PHONE` - 사용자의 전화번호입니다. 동일한 전화번호를 사용하는 프로필이 여러 개 있는 경우 가장 최근에 업데이트된 프로필이 업데이트 우선순위를 갖습니다.
- `PAYLOAD` - Braze에서 사용자에게 동기화하려는 필드의 문자열 또는 구조체입니다.

#### 1.2단계: 액세스 토큰 만들기  

Braze가 Databricks에 액세스하려면 개인 액세스 토큰을 생성해야 합니다.

1. Databricks 작업 영역의 상단 표시줄에서 Databricks 사용자 이름을 선택한 다음 드롭다운에서 **사용자 설정**을 선택합니다.
2. 액세스 토큰 탭에서 **새 토큰 생성**을 선택합니다.
3. 이 토큰을 식별하는 데 도움이 되는 "Braze CDI"와 같은 주석을 입력하고, Lifetime(일) 상자를 비워 두어 토큰의 수명을 무제한으로 변경하세요.
4. **생성**을 선택하십시오.
5. 표시된 토큰을 복사한 다음 **완료**를 선택합니다.

자격 증명 생성 단계에서 Braze 대시보드에 입력할 때까지 토큰을 안전한 장소에 보관하세요.

#### 1.3단계: Braze IP에 대한 액세스 허용    

네트워크 정책이 있는 경우 Braze 네트워크에 Databricks 인스턴스에 대한 액세스 권한을 부여해야 합니다. 아래 IP에서 Braze 대시보드의 지역에 해당하는 액세스를 허용합니다.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Microsoft Fabric %}

#### 1.1단계: 서비스 주체 설정 및 액세스 권한 부여
Braze는 Entra ID 인증이 있는 서비스 주체를 사용하여 Fabric 웨어하우스에 연결합니다. Braze가 사용할 새 서비스 주체를 생성하고 필요에 따라 Fabric 리소스에 대한 액세스 권한을 부여합니다. Braze에 연결하려면 다음 세부 정보가 필요합니다:    

* Azure 계정의 테넌트 ID(디렉터리라고도 함) 
* 서비스 주체에 대한 주체 ID(애플리케이션 ID라고도 함) 
* Braze가 인증하기 위한 클라이언트 비밀

1. Azure 포털에서 Microsoft Entra 관리 센터로 이동한 다음 앱 등록으로 이동합니다. 
2. **ID** > **애플리케이션** > **앱 등록**에서 **+ 새 등록**을 선택합니다.
3. 이름을 입력한 다음 지원되는 계정 유형으로 `Accounts in this organizational directory only`을 선택합니다. 그런 다음 **등록**을 선택합니다. 
4. 방금 만든 애플리케이션(서비스 주체)을 선택한 다음 **인증서 및 비밀** > **+ 새 클라이언트 비밀**로 이동합니다.
5. 비밀에 대한 설명을 입력하고 비밀의 만료 기간을 설정합니다. 그런 다음 **추가**를 선택합니다. 
6. Braze 설정에서 사용하기 위해 생성한 클라이언트 비밀을 기록해 두세요. 

{% alert note %}
Azure는 서비스 주체 비밀의 무제한 만료를 허용하지 않습니다. 자격 증명이 만료되기 전에 새로고침하여 Braze로의 데이터 흐름을 유지하는 것을 잊지 마세요.
{% endalert %}

#### 1.2단계: Fabric 리소스에 대한 액세스 권한 부여 
Braze가 Fabric 인스턴스에 연결할 수 있도록 액세스 권한을 제공해야 합니다. Fabric 관리자 포털에서 **설정** > **거버넌스 및 인사이트** > **관리자 포털** > **테넌트 설정**으로 이동합니다.    

* **개발자 설정**에서 "서비스 주체가 Fabric API를 사용할 수 있음"을 활성화하여 Braze가 Microsoft Entra ID를 사용하여 연결할 수 있도록 합니다.
* **OneLake 설정**에서 "사용자가 Fabric 외부 앱으로 OneLake에 저장된 데이터에 액세스할 수 있음"을 활성화하여 서비스 주체가 외부 앱에서 데이터에 액세스할 수 있도록 합니다.


#### 1.3단계: 테이블 설정
Braze는 Fabric 웨어하우스에서 테이블과 뷰를 모두 지원합니다. 새 웨어하우스를 생성해야 하는 경우, Fabric 콘솔에서 **만들기 > 데이터 웨어하우스 > 웨어하우스**로 이동하세요. 

```sql
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
  --If you include both email and phone, email is used as the primary identifier
  EMAIL VARCHAR,
  PHONE VARCHAR
)
GO
```

웨어하우스, 스키마, 테이블 또는 뷰의 이름은 원하는 대로 지정할 수 있지만 열 이름은 앞의 정의와 일치해야 합니다.

- `UPDATED_AT` - 이 행이 테이블에 업데이트되거나 추가된 시간입니다. 마지막 동기화 이후 추가되거나 업데이트된 행만 동기화됩니다.
- **사용자 식별자 열** - 테이블에는 하나 이상의 사용자 식별자 열이 포함될 수 있습니다. 각 행에는 하나의 식별자(`external_id`, `alias_name`과 `alias_label`의 조합, `braze_id`, `email` 또는 `phone`)만 포함해야 합니다. 소스 테이블에는 하나, 둘, 셋, 넷 또는 다섯 가지 식별자 유형 모두에 대한 열이 있을 수 있습니다.
    - `EXTERNAL_ID` - 업데이트하려는 사용자를 식별합니다. 이 값은 Braze에서 사용하는 `external_id` 값과 일치해야 합니다. 
    - `ALIAS_NAME` 및 `ALIAS_LABEL` - 이 두 열은 사용자 별칭 객체를 만듭니다. `alias_name`은 고유 식별자이고 `alias_label`은 별칭의 유형을 지정합니다. 사용자는 여러 레이블이 있는 여러 별칭을 가질 수 있지만 `alias_label`당 하나의 `alias_name`만 가질 수 있습니다.
    - `BRAZE_ID` - Braze 사용자 식별자입니다. 이것은 Braze 소프트웨어 개발 키트에 의해 생성되며, 새로운 사용자는 클라우드 데이터 수집을 통해 Braze ID로 생성할 수 없습니다. 새 사용자를 만들려면 외부 사용자 ID 또는 사용자 별칭을 지정합니다.
    - `EMAIL` - 사용자의 이메일 주소입니다. 동일한 이메일 주소를 가진 프로필이 여러 개 있는 경우 가장 최근에 업데이트된 프로필이 업데이트 우선순위를 갖습니다. 이메일과 전화번호를 모두 포함하는 경우 이메일이 기본 식별자로 사용됩니다.
    - `PHONE` - 사용자의 전화번호입니다. 동일한 전화번호를 사용하는 프로필이 여러 개 있는 경우 가장 최근에 업데이트된 프로필이 업데이트 우선순위를 갖습니다.
- `PAYLOAD` - Braze에서 사용자와 동기화하려는 필드의 JSON 문자열입니다.


#### 1.4단계: 웨어하우스 연결 문자열 가져오기
Braze가 연결하려면 웨어하우스에 대한 SQL 엔드포인트가 필요합니다. 이를 검색하려면 Fabric의 **작업 영역**으로 이동하여 항목 목록에서 웨어하우스 이름 위로 마우스를 가져간 다음 **SQL 연결 문자열 복사**를 선택합니다.

![사용자가 SQL 연결 문자열을 검색해야 하는 Microsoft Azure의 "Fabric Console" 페이지입니다.]({% image_buster /assets/img/cloud_ingestion/fabric_1.png %})


#### 1.5단계: 방화벽에서 Braze IP 허용(선택 사항)

Microsoft Fabric 계정의 구성에 따라 방화벽에서 다음 IP 주소를 허용하여 Braze의 트래픽을 허용해야 할 수도 있습니다. 이 기능을 활성화하는 방법에 대한 자세한 내용은 [Entra 조건부 액세스](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access)에 대한 관련 설명서를 참조하세요.

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### 2단계: Braze 대시보드에서 새 통합 생성

{% tabs %}
{% tab Snowflake %}

Braze 대시보드에서 **데이터 설정** > **클라우드 데이터 수집**으로 이동하여 **새 데이터 동기화 만들기**를 선택한 다음 **Snowflake 가져오기**를 선택합니다.

#### 2.1단계: Snowflake 연결 정보 및 소스 테이블 추가

Snowflake 데이터 웨어하우스 및 소스 테이블에 대한 정보를 입력한 후 다음 단계로 진행하세요.

![예제 데이터가 입력된 Braze 대시보드의 Snowflake에 대한 "새 가져오기 동기화 만들기" 페이지, 1단계: "연결 설정".]({% image_buster /assets/img/cloud_ingestion/ingestion_1.png %})

#### 2.2단계: 동기화 세부 정보 구성

다음으로, 동기화 이름을 선택하고 연락처 이메일을 입력하세요. 이 연락처 정보를 사용하여 테이블에 대한 액세스가 예상치 못하게 제거되는 등의 통합 오류에 대해 알려드리겠습니다.

연락처 이메일은 누락된 테이블, 권한 등과 같은 글로벌 또는 동기화 수준 오류에 대한 알림만 받게 됩니다. 행 수준 이슈는 수신되지 않습니다. 전역 오류는 동기화 실행을 방해하는 연결의 치명적인 문제를 나타냅니다. 이러한 문제에는 다음이 포함될 수 있습니다:

- 연결 문제
- 리소스 부족
- 권한 문제
- (카탈로그 동기화 전용) 카탈로그 계층의 공간 부족

![예제 데이터가 입력된 Braze 대시보드의 Snowflake에 대한 "새 가져오기 동기화 만들기" 페이지, 2단계: "동기화 세부 정보 설정".]({% image_buster /assets/img/cloud_ingestion/ingestion_2.png %})

또한 데이터 유형과 동기화 빈도를 선택합니다. 빈도는 15분마다 한 번에서 한 달에 한 번까지 설정할 수 있습니다. Braze 대시보드에 구성된 시간대를 사용하여 반복 동기화를 예약합니다. 지원되는 데이터 유형은 커스텀 속성, 커스텀 이벤트 및 구매 이벤트이며, 동기화의 데이터 유형은 생성 후 변경할 수 없습니다. 

#### Braze 사용자에게 공개 키 추가

이 시점에서 설정을 완료하려면 Snowflake로 돌아가야 합니다. 대시보드에 표시된 공개 키를 Braze가 Snowflake에 연결할 수 있도록 생성한 사용자에게 추가하세요.

추가 정보는 [Snowflake 설명서](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)를 참조하세요. 키를 언제든지 회전시키고 싶다면, 새로운 키 쌍을 생성하여 새로운 공개 키를 제공해 드릴 수 있습니다.

```sql
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```
{% endtab %}
{% tab Redshift %}

Braze 대시보드에서 **데이터 설정** > **클라우드 데이터 수집**으로 이동하여 **새 데이터 동기화 만들기**를 선택한 다음 **Amazon Redshift 가져오기**를 선택합니다.

#### 2.1단계: Redshift 연결 정보 및 소스 테이블 추가

Redshift 데이터 웨어하우스 및 소스 테이블에 대한 정보를 입력하십시오. 비공개 네트워크 터널을 사용하는 경우 슬라이더를 토글하고 터널 정보를 입력합니다. 그런 다음 다음 단계로 진행합니다. 

{% alert note %}
Braze 대시보드의 **데이터베이스 이름** 필드에는 Amazon Redshift에서 데이터베이스 식별자에 추가 문자를 지원하더라도 문자(A-Z, a-z), 숫자(0-9) 및 밑줄(_)만 허용됩니다.
{% endalert %}

![Braze 대시보드의 Redshift에 대한 "새 가져오기 동기화 만들기" 페이지, 1단계: "연결 설정".]({% image_buster /assets/img/cloud_ingestion/ingestion_6.png %})

#### 2.2단계: 동기화 세부 정보 구성

다음으로, 동기화 이름을 선택하고 연락처 이메일을 입력하세요. 이 연락처 정보를 사용하여 테이블에 대한 액세스가 예상치 못하게 제거되는 등의 통합 오류에 대해 알려드리겠습니다.

연락처 이메일은 누락된 테이블, 권한 등과 같은 글로벌 또는 동기화 수준 오류에 대한 알림만 받게 됩니다. 행 수준 이슈는 수신되지 않습니다. 전역 오류는 동기화 실행을 방해하는 연결의 치명적인 문제를 나타냅니다. 이러한 문제에는 다음이 포함될 수 있습니다:

- 연결 문제
- 리소스 부족
- 권한 문제
- (카탈로그 동기화 전용) 카탈로그 계층의 공간 부족

![예제 데이터가 입력된 Braze 대시보드의 Redshift에 대한 "새 가져오기 동기화 만들기" 페이지, 2단계: "동기화 세부 정보 설정".]({% image_buster /assets/img/cloud_ingestion/ingestion_7.png %})

또한 데이터 유형과 동기화 빈도를 선택합니다. 빈도는 15분마다 한 번에서 한 달에 한 번까지 설정할 수 있습니다. Braze 대시보드에 구성된 시간대를 사용하여 반복 동기화를 예약합니다. 지원되는 데이터 유형은 커스텀 속성, 커스텀 이벤트 및 구매 이벤트이며, 동기화의 데이터 유형은 생성 후 변경할 수 없습니다. 
{% endtab %}
{% tab BigQuery %}

Braze 대시보드에서 **데이터 설정** > **클라우드 데이터 수집**으로 이동하여 **새 데이터 동기화 만들기**를 선택한 다음 **Google BigQuery 가져오기**를 선택합니다.

#### 2.1단계: BigQuery 연결 정보 및 소스 테이블 추가

JSON 키를 업로드하고 서비스 계정의 이름을 제공한 다음 소스 테이블의 세부 정보를 입력합니다.

![Braze 대시보드의 BigQuery에 대한 "새 가져오기 동기화 만들기" 페이지, 1단계: "연결 설정".]({% image_buster /assets/img/cloud_ingestion/ingestion_11.png %})

#### 2.2단계: 동기화 세부 정보 구성

다음으로, 동기화 이름을 선택하고 연락처 이메일을 입력하세요. 이 연락처 정보를 사용하여 테이블에 대한 액세스가 예상치 못하게 제거되는 등의 통합 오류에 대해 알려드리겠습니다.

연락처 이메일은 누락된 테이블, 권한 등과 같은 글로벌 또는 동기화 수준 오류에 대한 알림만 받게 됩니다. 행 수준 이슈는 수신되지 않습니다. 전역 오류는 동기화 실행을 방해하는 연결의 치명적인 문제를 나타냅니다. 이러한 문제에는 다음이 포함될 수 있습니다:

- 연결 문제
- 리소스 부족
- 권한 문제
- (카탈로그 동기화 전용) 카탈로그 계층의 공간 부족

![Braze 대시보드의 BigQuery에 대한 "새 가져오기 동기화 만들기" 페이지, 2단계: "동기화 세부 정보 설정".]({% image_buster /assets/img/cloud_ingestion/ingestion_12.png %})

또한 데이터 유형과 동기화 빈도를 선택합니다. 빈도는 15분마다 한 번에서 한 달에 한 번까지 설정할 수 있습니다. Braze 대시보드에 구성된 시간대를 사용하여 반복 동기화를 예약합니다. 지원되는 데이터 유형은 커스텀 속성, 커스텀 이벤트, 구매 이벤트 및 사용자 삭제입니다. 동기화의 데이터 유형은 생성 후 변경할 수 없습니다. 

{% endtab %}
{% tab Databricks %}

Braze 대시보드에서 **데이터 설정** > **클라우드 데이터 수집**으로 이동하여 **새 데이터 동기화 만들기**를 선택한 다음 **Databricks 가져오기**를 선택합니다.

#### 2.1단계: Databricks 연결 정보 및 소스 테이블 추가

Databricks 데이터 웨어하우스 및 소스 테이블에 대한 정보를 입력한 다음, 다음 단계로 진행하세요.

![Braze 대시보드의 Databricks에 대한 "새 가져오기 동기화 만들기" 페이지, 1단계: "연결 설정".]({% image_buster /assets/img/cloud_ingestion/ingestion_16.png %})

#### 2.2단계: 동기화 세부 정보 구성

다음으로, 동기화 이름을 선택하고 연락처 이메일을 입력하세요. 이 연락처 정보를 사용하여 테이블에 대한 액세스가 예상치 못하게 제거되는 등의 통합 오류에 대해 알려드리겠습니다.

연락처 이메일은 누락된 테이블, 권한 등과 같은 글로벌 또는 동기화 수준 오류에 대한 알림만 받게 됩니다. 행 수준 이슈는 수신되지 않습니다. 전역 오류는 동기화 실행을 방해하는 연결의 치명적인 문제를 나타냅니다. 이러한 문제에는 다음이 포함될 수 있습니다:

- 연결 문제
- 리소스 부족
- 권한 문제
- (카탈로그 동기화 전용) 카탈로그 계층의 공간 부족

![Braze 대시보드의 Databricks에 대한 "새 가져오기 동기화 만들기" 페이지, 2단계: "동기화 세부 정보 설정".]({% image_buster /assets/img/cloud_ingestion/ingestion_12.png %})

또한 데이터 유형과 동기화 빈도를 선택합니다. 빈도는 15분마다 한 번에서 한 달에 한 번까지 설정할 수 있습니다. Braze 대시보드에 구성된 시간대를 사용하여 반복 동기화를 예약합니다. 지원되는 데이터 유형은 커스텀 속성, 커스텀 이벤트, 구매 이벤트 및 사용자 삭제입니다. 동기화의 데이터 유형은 생성 후 변경할 수 없습니다. 

{% endtab %}
{% tab Microsoft Fabric %}

Br