---
nav_title: 연결된 소스
article_title: 연결된 소스
description: "이 참조 문서에서는 Braze Cloud 데이터 수집을 사용하여 관련 데이터를 Snowflake, Redshift, BigQuery 및 Databricks 통합과 동기화하는 방법을 다룹니다."
page_order: 2
page_type: reference

---

# 연결된 소스

> 연결된 소스는 Braze의 클라우드 데이터 수집(CDI) 기능과 데이터를 직접 동기화하는 것에 대한 제로 복사 대안입니다. 연결된 소스가 데이터 웨어하우스에 직접 쿼리를 실행하여 Braze에 기본 데이터의 복사 없이 새로운 세그먼트를 생성합니다. 

연결된 소스를 Braze 작업 공간에 추가한 후, 세그먼트 확장 내에서 CDI 세그먼트를 생성할 수 있습니다. CDI 세그먼트를 사용하면 SQL을 작성하여 데이터 웨어하우스를 직접 쿼리할 수 있습니다(여기서 CDI 연결 소스를 통해 제공되는 데이터를 사용) 그리고 Braze 내에서 타겟팅할 수 있는 사용자 그룹을 생성하고 유지합니다. 

이 소스를 사용하여 세그먼트를 만드는 방법에 대한 자세한 내용은 [CDI 세그먼트]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/)를 참조하십시오.

{% alert warning %}
연결된 소스가 데이터 웨어하우스에서 직접 실행되기 때문에 이러한 쿼리를 데이터 웨어하우스에서 실행하는 데 관련된 모든 비용이 발생합니다. 연결된 소스는 데이터 포인트를 소비하지 않으며, CDI 세그먼트는 SQL 세그먼트 크레딧을 소비하지 않습니다.
{% endalert %}

## 연결된 소스 통합

### 1단계: 연결 자원

클라우드 데이터 수집 연결된 소스는 Braze와 귀하의 인스턴스에서 일부 설정이 필요합니다. 다음 단계를 따라 통합을 설정하세요. 일부 단계는 데이터 웨어하우스에서 수행되고 일부 단계는 Braze 대시보드에서 수행됩니다.

{% tabs %}
{% tab Snowflake %}
**데이터 웨어하우스에서**
1. 역할을 생성하고 스키마에서 테이블을 쿼리하고 생성할 수 있는 권한을 부여합니다.
2. 창고를 설정하고 해당 역할에 접근 권한을 부여하세요.
3. 해당 역할에 대한 사용자를 생성하십시오.
4. 구성에 따라 Snowflake 네트워크 정책에서 Braze IP를 허용해야 할 수 있습니다.

**Braze 대시보드에서**

{: start="5"}
5\. Braze 대시보드에서 새 연결 소스를 생성합니다.
6\. 연결된 소스의 동기화 세부 정보를 구성합니다.
7\. Braze 대시보드에 제공된 공개 키를 검색합니다.

**데이터 웨어하우스에서**

{: start="8"}
8\. 인증을 위해 [Snowflake 사용자](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)에 Braze 대시보드에서 공개 키를 추가합니다. 완료되면 연결된 소스를 사용하여 하나 이상의 CDI 세그먼트를 만들 수 있습니다.
{% endtab %}

{% tab Redshift %}
1. Redshift 환경에서 소스 데이터 및 필요한 리소스를 설정합니다.
2. Braze 대시보드에서 새 연결 소스를 생성합니다.
4. 통합을 테스트합니다.
5. 연결된 소스를 사용하여 하나 이상의 CDI 세그먼트를 만드십시오.
{% endtab %}

{% tab BigQuery %}
1. BigQuery 환경에서 소스 데이터와 필요한 리소스를 설정하십시오.
2. 서비스 계정을 만들고 동기화하려는 데이터가 포함된 BigQuery 프로젝트 및 데이터 세트에 대한 액세스를 허용합니다.  
3. Braze 대시보드에서 새 연결 소스를 생성합니다.
4. 통합을 테스트합니다.
5. 연결된 소스를 사용하여 하나 이상의 CDI 세그먼트를 만드십시오.
{% endtab %}

{% tab Databricks %}
1. 소스 데이터 및 필요한 리소스를 Databricks 환경에 설정하세요.
2. 서비스 계정을 만들고 동기화하려는 데이터를 포함하는 Databricks 프로젝트 및 데이터 세트에 대한 액세스를 허용합니다.  
3. Braze 대시보드에서 새 연결 소스를 생성합니다.
4. 통합을 테스트합니다.
5. 연결된 소스를 사용하여 하나 이상의 CDI 세그먼트를 만드십시오.

{% alert important %}
Braze가 Classic 및 Pro SQL 인스턴스에 연결될 때 2분에서 5분 정도의 워밍업 시간이 있을 수 있으며, 이는 연결 설정 및 테스트 중뿐만 아니라 CDI 세그먼트 생성 및 새로고침 중에도 지연을 초래할 수 있습니다. 서버리스 SQL 인스턴스를 사용하면 워밍업 시간을 최소화하고 쿼리 처리량을 향상시킬 수 있지만, 통합 비용이 약간 증가할 수 있습니다.
{% endalert %}

{% endtab %}
{% endtabs %}

### 2단계: 데이터 웨어하우스를 설정하세요

데이터 웨어하우스 환경에서 소스 데이터와 필요한 리소스를 설정하십시오. 연결된 소스는 하나 이상의 테이블을 참조할 수 있으므로, 연결된 소스에서 원하는 모든 테이블에 접근할 수 있는 권한이 Braze 사용자에게 있는지 확인하십시오.

{% tabs %}
{% tab Snowflake %}
#### 2.1 단계: 역할을 만들고 권한을 부여하십시오

연결된 소스가 사용할 역할을 만드십시오. 이 역할은 귀하의 CDI 세그먼트에서 사용할 수 있는 테이블 목록을 생성하고, 소스 테이블을 쿼리하여 새로운 세그먼트를 생성하는 데 사용됩니다. 연결된 소스가 생성된 후, Braze는 소스 스키마에서 사용자가 사용할 수 있는 모든 테이블의 이름과 설명을 발견합니다.

스키마의 모든 테이블에 대한 액세스 권한을 부여하거나 특정 테이블에만 권한을 부여할 수 있습니다. Braze 역할이 액세스할 수 있는 모든 테이블은 CDI 세그먼트에서 쿼리할 수 있습니다.

`create table` 권한은 Braze가 CDI 세그먼트 쿼리 결과로 테이블을 생성한 후 Braze에서 세그먼트를 업데이트할 수 있도록 필요합니다. Braze는 세그먼트당 임시 테이블을 생성하며, 테이블은 Braze가 세그먼트를 업데이트하는 동안에만 유지됩니다.

```json
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT CREATE TABLE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;

-- grant access to all current and future tables or views in the schema
GRANT SELECT ON ALL TABLES IN SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON FUTURE TABLES IN SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;

-- grant access to specific tables or views in the schema
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;

```

#### 2.2 단계: 웨어하우스를 설정하고 Braze 역할에 액세스 권한을 부여하세요.

```json
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
창고에는 **자동 재개** 플래그가 켜져 있어야 합니다. 그렇지 않으면, 쿼리를 실행할 때 Braze가 이를 켤 수 있도록 Braze에 추가 `OPERATE` 권한을 부여해야 합니다.
{% endalert %}

#### 2.3 단계: 사용자를 설정하세요.
```json
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

연결 정보를 Braze와 공유하고 나중 단계에서 사용자에게 추가할 공개 키를 받게 됩니다.

{% alert note %}
다른 워크스페이스를 동일한 Snowflake 계정에 연결할 때, 통합을 생성하는 각 Braze 워크스페이스에 고유한 사용자를 생성해야 합니다. 워크스페이스 내에서 동일한 사용자를 통합 간에 재사용할 수 있지만, 동일한 Snowflake 계정의 사용자가 워크스페이스 간에 중복되면 통합 생성이 실패합니다.
{% endalert %}

#### 2.4 단계: 당신의 Snowflake 네트워크 정책에서 Braze IP를 허용하십시오 (선택 사항)

Snowflake 계정의 구성에 따라 Snowflake 네트워크 정책에서 다음 IP 주소를 허용해야 할 수 있습니다. 이 작업에 대한 자세한 정보는 [네트워크 정책 수정](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies)에 대한 관련 Snowflake 설명서를 참조하십시오.

{% subtabs %}
{% subtab United States (US) %}
예를 들어 `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`, `US-07`, 다음은 관련 IP 주소입니다.
- `23.21.118.191`
- `34.206.23.173`
- `50.16.249.9`
- `52.4.160.214`
- `54.87.8.34`
- `54.156.35.251`
- `52.54.89.238`
- `18.205.178.15`
{% endsubtab %}

{% subtab European Union (EU) %}
인스턴스 `EU-01` 및 `EU-02`의 경우, 관련 IP 주소는 다음과 같습니다.
- `52.58.142.242`
- `52.29.193.121`
- `35.158.29.228`
- `18.157.135.97`
- `3.123.166.46`
- `3.64.27.36`
- `3.65.88.25`
- `3.68.144.188`
- `3.70.107.88`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Redshift %}
#### 2.1 단계: 사용자를 생성하고 권한을 부여하십시오 

```json
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT CREATE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

연결된 소스에서 사용할 사용자를 만드십시오. 이 사용자는 CDI 세그먼트에서 사용할 수 있는 테이블 목록을 생성하고, 소스 테이블을 쿼리하여 새로운 세그먼트를 만드는 데 사용됩니다. 연결된 소스가 생성된 후, Braze는 소스 스키마에서 사용자가 사용할 수 있는 모든 테이블의 이름과 설명을 발견합니다. 여러 CDI 통합을 생성하는 경우 스키마에 대한 권한을 부여하거나 그룹을 사용하여 권한을 관리할 수 있습니다. 

스키마의 모든 테이블에 대한 액세스 권한을 부여하거나 특정 테이블에만 권한을 부여할 수 있습니다. Braze 역할이 액세스할 수 있는 모든 테이블은 CDI 세그먼트에서 쿼리할 수 있습니다. 새 테이블이 생성될 때 사용자에게 액세스 권한을 부여하거나 사용자에 대한 기본값 권한을 설정하세요. 

`create table` 권한이 필요합니다. 그래야 Braze가 CDI 세그먼트 쿼리 결과로 테이블을 생성한 후 Braze에서 세그먼트를 업데이트할 수 있습니다. 브레이즈는 세그먼트당 임시 테이블을 생성하며, 이는 브레이즈가 세그먼트를 업데이트하는 동안에만 유지됩니다.


#### 2.2 단계: Braze IP에 대한 액세스 허용    

방화벽이나 기타 네트워크 정책이 있는 경우 Braze 네트워크에 Redshift 인스턴스에 대한 액세스 권한을 부여해야 합니다. 아래 IP에서 Braze 대시보드의 지역에 해당하는 액세스를 허용합니다. 

Braze가 Redshift에서 데이터에 접근할 수 있도록 보안 그룹을 변경해야 할 수도 있습니다. IP 아래 및 Redshift 클러스터를 쿼리하는 데 사용되는 포트(기본값은 5439)에서 인바운드 트래픽을 명시적으로 허용해야 합니다. 이 포트에서 Redshift TCP 연결을 명시적으로 허용해야 합니다. 수신 규칙이 "모두 허용"으로 설정되어 있더라도. 또한 Braze가 클러스터에 연결할 수 있도록 Redshift 클러스터의 엔드포인트가 공개적으로 액세스 가능해야 합니다.

Redshift 클러스터를 공개적으로 접근할 수 없게 하려면, VPC와 EC2 인스턴스를 설정하여 ssh 터널을 사용하여 Redshift 데이터에 접근할 수 있습니다. 자세한 내용은 [AWS:을 참조하십시오. 내 로컬 머신에서 개인 Amazon Redshift 클러스터에 어떻게 접근하나요?](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine)

{% subtabs %}
{% subtab United States (US) %}
예를 들어 `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`, `US-07`, 다음은 관련 IP 주소입니다.
- `23.21.118.191`
- `34.206.23.173`
- `50.16.249.9`
- `52.4.160.214`
- `54.87.8.34`
- `54.156.35.251`
- `52.54.89.238`
- `18.205.178.15`
{% endsubtab %}

{% subtab European Union (EU) %}
인스턴스 `EU-01` 및 `EU-02`의 경우, 관련 IP 주소는 다음과 같습니다.
- `52.58.142.242`
- `52.29.193.121`
- `35.158.29.228`
- `18.157.135.97`
- `3.123.166.46`
- `3.64.27.36`
- `3.65.88.25`
- `3.68.144.188`
- `3.70.107.88`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab BigQuery %}
#### 2.1 단계: 서비스 계정을 만들고 권한을 부여하십시오 

GCP에서 Braze가 테이블에서 데이터를 연결하고 읽을 수 있도록 서비스 계정을 만드세요. 서비스 계정에는 아래 권한이 있어야 합니다: 

- **BigQuery 연결 사용자:** 연결을 만들기 위해 Braze를 허용합니다.
- **BigQuery 사용자:** 쿼리를 실행하고, 데이터 세트 메타데이터를 읽고, 테이블을 나열하기 위해 Braze에 대한 액세스를 제공합니다.
- **BigQuery 데이터 Viewer:** 데이터 세트 및 해당 내용 보기 위한 Braze 접근을 제공합니다.
- **BigQuery 작업 사용자:** 작업을 실행하기 위해 Braze에 대한 액세스를 제공합니다.
- **bigquery.tables.create** 브레이즈 액세스를 제공하여 세그먼트 새로고침 중에 임시 테이블을 생성합니다.

연결된 소스에서 사용할 서비스 계정을 만드십시오. 이 사용자는 CDI 세그먼트에서 사용할 수 있는 테이블 목록을 생성하고, 소스 테이블을 쿼리하여 새로운 세그먼트를 만드는 데 사용됩니다. 연결된 소스가 생성된 후, Braze는 소스 스키마에서 사용자가 사용할 수 있는 모든 테이블의 이름과 설명을 발견합니다. 

데이터 세트의 모든 테이블에 대한 액세스 권한을 부여하거나 특정 테이블에만 권한을 부여할 수 있습니다. Braze 역할이 액세스할 수 있는 모든 테이블은 CDI 세그먼트에서 쿼리할 수 있습니다. 

`create table` 권한은 Braze가 CDI 세그먼트 쿼리 결과로 테이블을 생성한 후 Braze에서 세그먼트를 업데이트할 수 있도록 필요합니다. Braze는 세그먼트당 임시 테이블을 생성하며, 테이블은 Braze가 세그먼트를 업데이트하는 동안에만 유지됩니다. 

서비스 계정을 만들고 권한을 부여한 후 JSON 키를 생성합니다. 자세한 정보는 [Google Cloud를 참조하세요. 서비스 계정 키](https://cloud.google.com/iam/docs/keys-create-delete)를 생성하고 삭제합니다. 나중에 Braze 대시보드에 이것을 업로드할 것입니다.

#### 2.2 단계: Braze IP에 대한 액세스 허용    

네트워크 정책이 있는 경우 Braze 네트워크에 Big Query 인스턴스에 대한 액세스 권한을 부여해야 합니다. 아래 IP에서 Braze 대시보드의 지역에 해당하는 액세스를 허용합니다.  

{% subtabs %}
{% subtab United States (US) %}
예를 들어 `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`, `US-07`, 다음은 관련 IP 주소입니다.
- `23.21.118.191`
- `34.206.23.173`
- `50.16.249.9`
- `52.4.160.214`
- `54.87.8.34`
- `54.156.35.251`
- `52.54.89.238`
- `18.205.178.15`
{% endsubtab %}

{% subtab European Union (EU) %}
인스턴스 `EU-01` 및 `EU-02`의 경우, 관련 IP 주소는 다음과 같습니다.
- `52.58.142.242`
- `52.29.193.121`
- `35.158.29.228`
- `18.157.135.97`
- `3.123.166.46`
- `3.64.27.36`
- `3.65.88.25`
- `3.68.144.188`
- `3.70.107.88`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Databricks %}
#### 2.1 단계: 액세스 토큰을 생성하다  

브레이즈가 Databricks에 접근하려면 개인 액세스 토큰을 생성해야 합니다.

1. Databricks 작업 공간에서 상단 바에서 Databricks 사용자 이름을 선택한 다음 드롭다운에서 **사용자 설정**을 선택합니다.
2. 서비스 계정이 연결된 소스에 사용된 스키마에 대한 `CREATE TABLE` 권한을 가지고 있는지 확인하세요. 
3. **액세스 토큰** 탭에서 **새 토큰 생성**을 선택합니다.
4. 이 토큰을 식별하는 데 도움이 되는 "Braze CDI"와 같은 주석을 입력하고, Lifetime 상자(days)를 비워 두어(blank) 토큰의 수명을 무수명으로 변경하세요.
5. **생성**을 선택하십시오.
6. 표시된 토큰을 복사한 다음 **완료**를 선택합니다.

이 토큰은 CDI 세그먼트에서 사용할 수 있는 테이블 목록을 생성하고, 소스 테이블을 쿼리하여 새로운 세그먼트를 생성하는 데 사용됩니다. 연결된 소스가 생성된 후, Braze는 소스 스키마에서 사용자가 사용할 수 있는 모든 테이블의 이름과 설명을 발견합니다. 

스키마의 모든 테이블에 대한 액세스 권한을 부여하거나 특정 테이블에만 권한을 부여할 수 있습니다. Braze 역할이 액세스할 수 있는 모든 테이블은 CDI 세그먼트에서 쿼리할 수 있습니다.

`create table` 권한이 필요합니다. 그래야 Braze가 CDI 세그먼트 쿼리 결과로 테이블을 생성한 후 Braze에서 세그먼트를 업데이트할 수 있습니다. 브레이즈는 세그먼트당 임시 테이블을 생성하며, 이는 브레이즈가 세그먼트를 업데이트하는 동안에만 유지됩니다. 

자격 증명 생성 단계에서 Braze 대시보드에 입력할 때까지 토큰을 안전한 장소에 보관하세요.

#### 2.2 단계: Braze IP에 대한 액세스 허용    

네트워크 정책이 있는 경우 Braze 네트워크에 Databricks 인스턴스에 대한 액세스 권한을 부여해야 합니다. 아래 IP에서 Braze 대시보드의 지역에 해당하는 액세스를 허용합니다.  

{% subtabs %}
{% subtab United States (US) %}
예를 들어 `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`, `US-07`, 다음은 관련 IP 주소입니다.
- `23.21.118.191`
- `34.206.23.173`
- `50.16.249.9`
- `52.4.160.214`
- `54.87.8.34`
- `54.156.35.251`
- `52.54.89.238`
- `18.205.178.15`
{% endsubtab %}

{% subtab European Union (EU) %}
인스턴스 `EU-01` 및 `EU-02`의 경우, 관련 IP 주소는 다음과 같습니다.
- `52.58.142.242`
- `52.29.193.121`
- `35.158.29.228`
- `18.157.135.97`
- `3.123.166.46`
- `3.64.27.36`
- `3.65.88.25`
- `3.68.144.188`
- `3.70.107.88`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### 3단계: Braze 대시보드에서 연결된 소스를 생성합니다

{% tabs %}
{% tab Snowflake %}
#### 3.1 단계: Snowflake 연결 정보 및 소스 테이블 추가

Braze 대시보드에서 연결된 소스를 생성합니다. **데이터 설정** > **클라우드 데이터 수집** > **연결된 소스**, 그리고 **새 데이터 동기화 만들기** > **스노우플레이크 가져오기**.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Snowflake 데이터 웨어하우스 및 소스 스키마에 대한 정보를 입력한 후 다음 단계로 진행하세요.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_1.png %})

#### 3.2 단계: 동기화 세부 정보 구성

연결된 소스의 이름을 선택하세요. 이 이름은 새로운 CDI 세그먼트를 생성할 때 사용 가능한 소스 목록에 사용됩니다. 

이 소스에 대한 최대 실행 시간을 구성하십시오. Braze는 세그먼트를 생성하거나 새로 고칠 때 최대 실행 시간을 초과하는 모든 쿼리를 자동으로 중단합니다. 최대 실행 시간은 60분이며, 더 짧은 실행 시간은 Snowflake 계정에서 발생하는 비용을 줄여줍니다. 

{% alert note %}
쿼리가 지속적으로 시간 초과되고 최대 실행 시간을 60분으로 설정한 경우, 쿼리 실행 시간을 최적화하거나 Braze 사용자에게 더 큰 웨어하우스를 할당하는 것을 고려하세요.
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_2.png %})

#### 3.3 단계: 공개 키에 주목하세요  

**테스트 연결** 단계에서 RSA 공개 키를 주의 깊게 확인하세요. Snowflake에서 통합을 완료하는 데 필요합니다.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_3.png %})

{% endtab %}
{% tab Redshift %}
#### 3.1 단계: Redshift 연결 정보 및 소스 테이블 추가

Braze 대시보드에서 연결된 소스를 생성합니다. **데이터 설정** > **클라우드 데이터 수집** > **연결된 소스**, 그리고 **데이터 연결 생성** > **아마존 레드시프트 가져오기**.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Redshift 데이터 웨어하우스 및 소스 스키마에 대한 정보를 입력한 후 다음 단계로 진행하십시오.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_1.png %})

#### 3.2 단계: 동기화 세부 정보 구성

연결된 소스의 이름을 선택하세요. 이 이름은 새로운 CDI 세그먼트를 생성할 때 사용 가능한 소스 목록에 사용됩니다. 

이 소스에 대한 최대 실행 시간을 구성하십시오. Braze는 세그먼트를 생성하거나 새로 고칠 때 최대 실행 시간을 초과하는 모든 쿼리를 자동으로 중단합니다. 허용되는 최대 실행 시간은 60분입니다. 더 짧은 실행 시간은 Redshift 계정에서 발생하는 비용을 줄입니다. 

{% alert note %}
쿼리가 지속적으로 시간 초과되고 최대 실행 시간을 60분으로 설정한 경우, 쿼리 실행 시간을 최적화하거나 Braze 사용자에게 더 큰 웨어하우스를 할당하는 것을 고려하세요.
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_2.png %})

#### 3.3 단계: 공개 키 (선택 사항)

SSH 터널로 **연결**이 선택된 경우, **연결 테스트** 단계에서 RSA 공개 키를 기록해 두십시오. Redshift에서 통합을 완료하는 데 필요할 것입니다.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_3.png %})

{% endtab %}
{% tab BigQuery %}
#### 3.1 단계: BigQuery 연결 정보 및 소스 테이블 추가

Braze 대시보드에서 연결된 소스를 생성합니다. **데이터 설정** > **클라우드 데이터 수집** > **연결된 소스**, 그런 다음 **새 데이터 동기화 만들기** > **구글 빅쿼리 가져오기**.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

BigQuery 프로젝트와 데이터 세트에 대한 정보를 입력한 다음 다음 단계로 진행하십시오.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_bg_1.png %})

#### 3.2 단계: 동기화 세부 정보 구성

연결된 소스의 이름을 선택하세요. 이 이름은 새로운 CDI 세그먼트를 생성할 때 사용 가능한 소스 목록에 사용됩니다. 

이 소스에 대한 최대 실행 시간을 구성하십시오. Braze는 세그먼트를 생성하거나 새로 고칠 때 최대 실행 시간을 초과하는 모든 쿼리를 자동으로 중단합니다. 허용되는 최대 실행 시간은 60분입니다. 더 낮은 실행 시간은 BigQuery 계정에서 발생하는 비용을 줄입니다. 

{% alert note %}
쿼리가 지속적으로 시간 초과되고 최대 실행 시간을 60분으로 설정한 경우, 쿼리 실행 시간을 최적화하거나 Braze 사용자에게 더 큰 웨어하우스를 할당하는 것을 고려하세요.
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_bg_2.png %})

#### 3.3 단계: 연결 테스트

사용자가 볼 수 있는 테이블 목록이 예상한 대로인지 확인하려면 **테스트 연결**을 선택한 다음 **완료**를 선택하십시오. 귀하의 연결된 소스가 이제 생성되었으며 CDI 세그먼트에서 사용할 준비가 되었습니다.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% tab Databricks %}
#### 3.1 단계: Databricks 연결 정보 및 소스 테이블 추가

Braze 대시보드에서 연결된 소스를 생성합니다. **데이터 설정** > **클라우드 데이터 수집** > **연결된 소스**, 그리고 **새 데이터 동기화 만들기** > **다트브릭스 가져오기**.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Databricks 자격 증명 및 선택적 카탈로그와 소스 스키마에 대한 정보를 입력한 후 다음 단계로 진행하십시오.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_databricks_1.png %})

#### 3.2 단계: 동기화 세부 정보 구성

연결된 소스의 이름을 선택하세요. 이 이름은 새로운 CDI 세그먼트를 생성할 때 사용 가능한 소스 목록에 사용됩니다. 

이 소스에 대한 최대 실행 시간을 구성하십시오. Braze는 세그먼트를 생성하거나 새로 고칠 때 최대 실행 시간을 초과하는 모든 쿼리를 자동으로 중단합니다. 허용되는 최대 실행 시간은 60분입니다. 더 짧은 실행 시간은 Databricks 계정에서 발생하는 비용을 줄입니다. 

{% alert note %}
쿼리가 지속적으로 시간 초과되고 최대 실행 시간을 60분으로 설정한 경우, 쿼리 실행 시간을 최적화하거나 Braze 사용자에게 더 큰 웨어하우스를 할당하는 것을 고려하세요.
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_db_2.png %})

#### 3.3 단계: 연결 테스트

사용자가 볼 수 있는 테이블 목록이 예상한 대로인지 확인하려면 **테스트 연결**을 선택한 다음 **완료**를 선택하십시오. 귀하의 연결된 소스가 이제 생성되었으며 CDI 세그먼트에서 사용할 준비가 되었습니다.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% endtabs %}

### 4단계: 데이터 웨어하우스 구성을 완료하십시오

{% tabs %}
{% tab Snowflake %}
마지막 단계에서 기록한 공개 키를 Snowflake의 사용자에게 추가하세요. 이를 통해 Braze가 Snowflake에 연결할 수 있습니다. 자세한 내용은 [Snowflake 설명서](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)를 참조하십시오. 

키를 언제든지 회전하려면 **데이터 접근 관리**으로 가서 **클라우드 데이터 수집**에서 해당 계정에 대해 **새 키 생성**을 선택하여 새 공개 키를 만들 수 있습니다.

![데이터 접근 관리 위한 Snowflake 데이터 접근 자격 증명, 새로운 키 생성 버튼이 있습니다.]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_4.png %})

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='{INSERT_YOUR_KEY}';
```

사용자가 Snowflake에 키를 추가한 후, Braze에서 **연결 테스트**을 선택하고, 그 다음 **완료**를 선택합니다. 귀하의 연결된 소스가 이제 생성되었으며 CDI 세그먼트에서 사용할 준비가 되었습니다.
{% endtab %}

{% tab Redshift %}
SSH 터널에 연결하는 경우, 마지막 단계에서 기록한 공개 키를 SSH 터널 사용자에게 추가하십시오. 

사용자에게 키를 추가한 후, Braze에서 **연결 테스트**를 선택한 다음, **완료**를 선택합니다. 귀하의 연결된 소스가 이제 생성되었으며 CDI 세그먼트에서 사용할 준비가 되었습니다.

{% endtab %}
{% tab BigQuery %}
이것은 BigQuery에 적용되지 않습니다.

{% endtab %}
{% tab Databricks %}
이것은 Databricks에 적용되지 않습니다.

{% endtab %}
{% endtabs %}

{% alert note %}
소스는 "초안" 상태에서 "활성" 상태로 이동하기 전에 성공적으로 테스트해야 합니다. 만약 생성 페이지를 닫아야 한다면, 통합은 저장되며, 세부 사항 페이지를 다시 방문하여 변경 및 테스트를 할 수 있습니다.  
{% endalert %}

## 추가 통합 또는 사용자 설정(선택 사항)

{% tabs %}
{% tab Snowflake %}
Braze와 여러 통합을 설정할 수 있지만, 각 통합은 다른 스키마에 연결되도록 구성해야 합니다. 추가 연결을 생성할 때 동일한 Snowflake 계정에 연결하는 경우 기존 자격 증명을 재사용할 수 있습니다.

통합 간에 동일한 사용자와 역할을 재사용하면 공개 키를 다시 추가할 필요가 없습니다.
{% endtab %}

{% tab Redshift %}
여러 소스를 Braze와 설정할 수 있지만, 각 소스는 다른 스키마에 연결되도록 구성해야 합니다. 추가 소스를 생성할 때 동일한 Redshift 계정에 연결하는 경우 기존 자격 증명을 재사용할 수 있습니다.
{% endtab %}

{% tab BigQuery %}
여러 소스를 Braze와 설정할 수 있지만, 각 소스는 다른 데이터 세트에 연결되도록 구성해야 합니다. 추가 소스를 만들 때 동일한 BigQuery 계정에 연결하는 경우 기존 자격 증명을 재사용할 수 있습니다.
{% endtab %}

{% tab Databricks %}
여러 소스를 Braze와 설정할 수 있지만, 각 소스는 다른 스키마에 연결되도록 구성해야 합니다. 추가 소스를 만들 때 동일한 Databricks 계정에 연결하는 경우 기존 자격 증명을 재사용할 수 있습니다.
{% endtab %}
{% endtabs %}

## 연결된 소스 사용

소스가 생성된 후, 하나 이상의 CDI 세그먼트를 생성하는 데 사용할 수 있습니다. 이 소스를 사용하여 세그먼트를 만드는 방법에 대한 자세한 내용은 [CDI 세그먼트 설명서]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/)를 참조하십시오.

{% alert note %}
쿼리가 지속적으로 시간 초과되고 최대 실행 시간을 60분으로 설정한 경우, 쿼리 실행 시간을 최적화하거나 Braze 사용자에게 더 많은 컴퓨팅 리소스(예: 더 큰 웨어하우스)를 할당하는 것을 고려해 보십시오.
{% endalert %}
