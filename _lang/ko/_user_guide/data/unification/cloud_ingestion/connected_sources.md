---
nav_title: 연결된 소스
article_title: 연결된 소스
description: "이 페이지에서는 Braze Cloud 데이터 수집을 사용하여 관련 데이터를 Snowflake, Redshift, BigQuery 및 Databricks 통합과 동기화하는 방법을 설명합니다."
page_order: 2
page_type: reference

---

# 연결된 소스

> 연결된 데이터 소스는 Braze의 클라우드 데이터 수집(CDI) 기능으로 데이터를 직접 동기화하는 대신 복사본이 필요 없는 대안입니다. 연결된 소스는 데이터 웨어하우스에 직접 쿼리하여 기본 데이터를 Braze에 복사하지 않고도 새로운 세그먼트를 생성합니다. 

Braze 워크스페이스에 연결된 소스를 추가한 후 세그먼트 확장 내에서 CDI 세그먼트를 만들 수 있습니다. CDI 세그먼트 확장을 사용하면 데이터 웨어하우스에 직접 쿼리하는 SQL을 작성하고(CDI 커넥티드 소스를 통해 제공되는 데이터를 사용하여), Braze 내에서 타겟팅할 수 있는 사용자 그룹을 만들고 유지 관리할 수 있습니다. 

이 소스를 사용하여 세그먼트를 만드는 방법에 대한 자세한 내용은 [CDI 세그먼트 확장을]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/) 참조하세요.

{% alert warning %}
연결된 소스는 데이터 웨어하우스에서 직접 실행되므로, 데이터 웨어하우스에서 이러한 쿼리를 실행하는 것과 관련된 모든 비용은 사용자가 부담하게 됩니다. 연결된 소스는 데이터 포인트를 기록하지 않으며, CDI 세그먼트 확장은 SQL 세그먼트 크레딧을 소비하지 않습니다.
{% endalert %}

## 연결된 소스 통합하기

### 1단계: 리소스 연결

클라우드 데이터 수집 연결 소스를 사용하려면 Braze와 인스턴스에서 몇 가지 설정이 필요합니다. 통합을 설정하려면 다음 단계를 따르세요. 일부 단계는 데이터 웨어하우스에서 수행되고 일부 단계는 Braze 대시보드에서 수행됩니다.

{% tabs %}
{% tab Snowflake %}
**데이터 웨어하우스에서**
1. 역할을 만들고 스키마에서 테이블을 쿼리하고 만들 수 있는 권한을 부여합니다.
2. 창고를 설정하고 해당 역할에 대한 액세스 권한을 부여하세요.
3. 해당 역할에 대한 사용자를 만듭니다.
4. 구성에 따라 Snowflake 네트워크 정책에서 Braze IP를 허용해야 할 수도 있습니다.

**Braze 대시보드에서**

{: start="5"}
5\. Braze 대시보드에서 새 연결 소스를 만듭니다.
6\. 연결된 소스에 대한 동기화 세부 정보를 구성합니다.
7\. Braze 대시보드에서 제공된 공개 키를 검색합니다.

**데이터 웨어하우스에서**

{: start="8"}
8\. [인증을 위해](https://docs.snowflake.com/en/user-guide/key-pair-auth.html) Braze 대시보드의 공개 키를 [Snowflake 사용자에게](https://docs.snowflake.com/en/user-guide/key-pair-auth.html) 추가합니다. 작업이 끝나면 연결된 소스를 사용하여 하나 이상의 CDI 세그먼트 확장을 만들 수 있습니다.
{% endtab %}

{% tab Redshift %}
1. Redshift 환경에서 데이터 소스 데이터와 필요한 리소스를 설정하세요.
2. Braze 대시보드에서 새 연결 소스를 만듭니다.
4. 통합을 테스트합니다.
5. 연결된 소스를 사용하여 하나 이상의 CDI 세그먼트 확장을 만듭니다.
{% endtab %}

{% tab BigQuery %}
1. BigQuery 환경에서 데이터 소스 데이터와 필요한 리소스를 설정합니다.
2. 서비스 계정을 만들고 동기화하려는 데이터가 포함된 BigQuery 프로젝트 및 데이터 집합에 대한 액세스를 허용합니다.  
3. Braze 대시보드에서 새 연결 소스를 만듭니다.
4. 통합을 테스트합니다.
5. 연결된 소스를 사용하여 하나 이상의 CDI 세그먼트 확장을 만듭니다.
{% endtab %}

{% tab Databricks %}
1. 데이터브릭스 환경에서 데이터 소스 데이터와 필요한 리소스를 설정하세요.
2. 서비스 계정을 만들고 동기화하려는 데이터가 포함된 데이터브릭스 프로젝트 및 데이터세트에 대한 액세스를 허용하세요.  
3. Braze 대시보드에서 새 연결 소스를 만듭니다.
4. 통합을 테스트합니다.
5. 연결된 소스를 사용하여 하나 이상의 CDI 세그먼트 확장을 만듭니다.

{% alert important %}
Braze가 클래식 및 프로 SQL 인스턴스에 연결할 때 2~5분 정도의 워밍업 시간이 있을 수 있으며, 이로 인해 연결 설정 및 테스트는 물론 CDI 세그먼트 확장 생성 및 새로고침 중에 지연이 발생할 수 있습니다. 서버리스 SQL 인스턴스를 사용하면 워밍업 시간이 최소화되고 쿼리 처리량이 향상되지만 통합 비용이 약간 높아질 수 있습니다.
{% endalert %}

{% endtab %}

{% tab Microsoft Fabric %}
1. 서비스 주체를 만들고 통합에 사용할 Fabric 워크스페이스에 대한 액세스를 허용하세요.   
2. Fabric 워크스페이스에서 소스 데이터를 설정하고 서비스 주체에 권한을 부여합니다. 
3. Braze 대시보드에서 새 연결 소스를 만듭니다.
4. 통합을 테스트합니다.
5. 연결된 소스를 사용하여 하나 이상의 CDI 세그먼트 확장을 만듭니다.
{% endtab %}

{% endtabs %}

### 2단계: 데이터 웨어하우스 설정하기

데이터 웨어하우스 환경에서 소스 데이터와 필요한 리소스를 설정하세요. 연결된 소스는 하나 이상의 테이블을 참조할 수 있으므로 연결된 소스에서 원하는 모든 테이블에 액세스할 수 있는 권한이 Braze 사용자에게 있는지 확인하세요.

{% tabs %}
{% tab Snowflake %}
#### 2.1단계: 역할 만들기 및 권한 부여

연결된 소스가 사용할 역할을 만듭니다. 이 역할은 CDI 세그먼트 확장에 사용할 수 있는 테이블 목록을 생성하고 소스 테이블을 쿼리하여 새 세그먼트를 만드는 데 사용됩니다. 연결된 소스가 생성되면 Braze는 소스 스키마에서 사용자가 사용할 수 있는 모든 테이블의 이름과 설명을 검색합니다.

스키마의 모든 테이블에 대한 액세스 권한을 부여하거나 특정 테이블에만 권한을 부여하도록 선택할 수 있습니다. Braze 역할이 액세스할 수 있는 테이블은 CDI 세그먼트 확장에서 쿼리할 수 있습니다.

`create table` 권한은 Braze에서 세그먼트를 업데이트하기 전에 CDI 세그먼트 확장 쿼리 결과가 포함된 테이블을 만들 수 있도록 하기 위해 필요합니다. Braze는 세그먼트별로 임시 테이블을 생성하며, 이 테이블은 Braze가 세그먼트를 업데이트하는 동안에만 유지됩니다.

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

#### 2.2단계: 창고를 설정하고 Braze 역할에 대한 액세스 권한을 부여합니다.

```json
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
창고에 **자동 재개** 플래그가 켜져 있어야 합니다. 그렇지 않은 경우, 쿼리를 실행할 때 Braze가 켜지도록 창고에 대한 `OPERATE` 권한을 추가로 부여해야 합니다.
{% endalert %}

#### 2.3단계: 사용자 설정
```json
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Braze와 연결 정보를 공유하고 나중에 사용자에게 추가할 공개 키를 받게 됩니다.

{% alert note %}
서로 다른 워크스페이스를 동일한 Snowflake 계정에 연결할 때는 통합을 만들고자 하는 각 Braze 워크스페이스에 대해 고유한 사용자를 만들어야 합니다. 워크스페이스 내에서 동일한 사용자를 여러 통합에서 재사용할 수 있지만, 동일한 Snowflake 계정의 사용자가 여러 워크스페이스에 중복되어 있으면 통합 생성이 실패합니다.
{% endalert %}

#### 2.4단계: Snowflake 네트워크 정책에서 Braze IP 허용(선택 사항)

Snowflake 계정의 구성에 따라 Snowflake 네트워크 정책에서 다음 IP 주소를 허용해야 할 수 있습니다. 이 작업에 대한 자세한 내용은 [네트워크 정책 수정에](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies) 관한 관련 Snowflake 설명서를 참조하세요.

{% multi_lang_include data_centers.md datacenters='ips' %}
{% endtab %}

{% tab Redshift %}
#### 2.1단계: 사용자 만들기 및 권한 부여 

```json
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT CREATE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

연결된 소스를 사용할 사용자를 만듭니다. 이 사용자는 CDI 세그먼트 확장에 사용할 수 있는 테이블 목록을 생성하고 소스 테이블을 쿼리하여 새 세그먼트를 만드는 데 사용됩니다. 연결된 소스가 생성되면 Braze는 소스 스키마에서 사용자가 사용할 수 있는 모든 테이블의 이름과 설명을 검색합니다. 여러 CDI 통합을 만드는 경우 스키마에 권한을 부여하거나 그룹을 사용하여 권한을 관리할 수 있습니다. 

스키마의 모든 테이블에 대한 액세스 권한을 부여하거나 특정 테이블에만 권한을 부여하도록 선택할 수 있습니다. Braze 역할이 액세스할 수 있는 테이블은 CDI 세그먼트 확장에서 쿼리할 수 있습니다. 새 테이블을 만들 때 사용자에게 액세스 권한을 부여하거나 사용자에 대한 기본값을 설정하세요. 

`create table` 권한은 Braze에서 세그먼트를 업데이트하기 전에 CDI 세그먼트 확장 쿼리 결과가 포함된 테이블을 만들 수 있도록 하기 위해 필요합니다. Braze는 세그먼트별로 임시 테이블을 생성하며, 이 임시 테이블은 Braze가 세그먼트를 업데이트하는 동안에만 유지됩니다.


#### 2.2단계: Braze IP에 대한 액세스 허용    

방화벽이나 기타 네트워크 정책이 있는 경우, Redshift 인스턴스에 대한 Braze 네트워크 액세스 권한을 부여해야 합니다. Braze 대시보드의 지역에 해당하는 아래 IP에서 액세스를 허용합니다. 

또한, 보안 그룹을 변경하여 Redshift에서 Braze가 데이터에 액세스할 수 있도록 허용해야 할 수도 있습니다. 아래 IP와 Redshift 클러스터를 쿼리하는 데 사용되는 포트에서 인바운드 트래픽을 명시적으로 허용해야 합니다(기본값은 5439). 인바운드 규칙이 "모두 허용"으로 설정되어 있더라도 이 포트에서 Redshift TCP 연결을 명시적으로 허용해야 합니다. 또한, Redshift 클러스터의 엔드포인트가 공개적으로 액세스할 수 있어야 Braze가 클러스터에 연결할 수 있습니다.

Redshift 클러스터에 공개적으로 액세스하지 않으려는 경우, VPC 및 EC2 인스턴스를 설정하여 ssh 터널을 사용하여 Redshift 데이터에 액세스하도록 할 수 있습니다. 자세한 내용은 [AWS를 참조하세요: 로컬 머신에서 프라이빗 Amazon Redshift 클러스터에 액세스하려면 어떻게 하나요?](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine)

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% tab BigQuery %}
#### 2.1단계: 서비스 계정 만들기 및 권한 부여하기 

Braze가 테이블에서 데이터를 연결하고 읽는 데 사용할 서비스 계정을 GCP에서 생성하세요. 서비스 계정에는 아래 권한이 있어야 합니다: 

- **BigQuery 연결 사용자:** Braze가 연결할 수 있도록 허용합니다.
- **BigQuery 사용자:** 쿼리를 실행하고, 데이터 세트 메타데이터를 읽고, 테이블을 나열할 수 있는 Braze 액세스를 제공합니다.
- **BigQuery 데이터 뷰어:** 데이터 세트와 그 콘텐츠를 볼 수 있는 Braze 액세스 권한을 제공합니다.
- **BigQuery 작업 사용자:** 작업을 실행하기 위한 Braze 액세스 권한을 제공합니다.
- **bigquery.tables.create** 세그먼트를 새로고침하는 동안 임시 테이블을 만들 수 있는 Braze 액세스 권한을 제공합니다.

연결된 소스를 사용할 서비스 계정을 만듭니다. 이 사용자는 CDI 세그먼트 확장에 사용할 수 있는 테이블 목록을 생성하고 소스 테이블을 쿼리하여 새 세그먼트를 만드는 데 사용됩니다. 연결된 소스가 생성되면 Braze는 소스 스키마에서 사용자가 사용할 수 있는 모든 테이블의 이름과 설명을 검색합니다. 

데이터 집합의 모든 테이블에 대한 액세스 권한을 부여하거나 특정 테이블에만 권한을 부여하도록 선택할 수 있습니다. Braze 역할이 액세스할 수 있는 테이블은 CDI 세그먼트 확장에서 쿼리할 수 있습니다. 

`create table` 권한은 Braze에서 세그먼트를 업데이트하기 전에 CDI 세그먼트 확장 쿼리 결과가 포함된 테이블을 만들 수 있도록 하기 위해 필요합니다. Braze는 세그먼트별로 임시 테이블을 생성하며, 이 테이블은 Braze가 세그먼트를 업데이트하는 동안에만 유지됩니다. 

서비스 계정을 만들고 권한을 부여한 후 JSON 키를 생성합니다. 자세한 내용은 [Google Cloud를 참조하세요: 서비스 계정 키 생성 및 삭제](https://cloud.google.com/iam/docs/keys-create-delete). 이 내용은 나중에 Braze 대시보드에 업로드할 예정입니다.

#### 2.2단계: Braze IP에 대한 액세스 허용    

네트워크 정책이 설정되어 있는 경우, 빅 쿼리 인스턴스에 대한 Braze 네트워크 액세스 권한을 부여해야 합니다. Braze 대시보드의 지역에 해당하는 아래 IP에서 액세스를 허용합니다.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% tab Databricks %}
#### 2.1단계: 액세스 토큰 만들기  

Braze가 데이터브릭에 액세스하려면 개인 액세스 토큰을 생성해야 합니다.

1. 데이터브릭스 작업 영역의 상단 표시줄에서 데이터브릭스 사용자 이름을 선택한 다음 드롭다운에서 **사용자 설정을** 선택합니다.
2. 서비스 계정에 연결된 소스에 사용된 스키마에 대한 `CREATE TABLE` 권한이 있는지 확인하세요. 
3. **토큰 액세스** 탭에서 **새 토큰 생성을** 선택합니다.
4. 이 토큰을 식별하는 데 도움이 되는 댓글(예: "Braze CDI")을 입력하고 토큰의 수명을 수명(일) 상자를 비워 두어(공란) 토큰의 수명을 수명 없음으로 변경합니다.
5. **생성을** 선택합니다.
6. 표시된 토큰을 복사한 다음 **완료를** 선택합니다.

이 토큰은 CDI 세그먼트 확장 프로그램에서 사용 가능한 테이블 목록을 생성하고 소스 테이블을 쿼리하여 새 세그먼트를 생성하는 데 사용됩니다. 연결된 소스가 생성되면 Braze는 소스 스키마에서 사용자가 사용할 수 있는 모든 테이블의 이름과 설명을 검색합니다. 

스키마의 모든 테이블에 대한 액세스 권한을 부여하거나 특정 테이블에만 권한을 부여하도록 선택할 수 있습니다. Braze 역할이 액세스할 수 있는 테이블은 CDI 세그먼트 확장에서 쿼리할 수 있습니다.

`create table` 권한은 Braze에서 세그먼트를 업데이트하기 전에 CDI 세그먼트 확장 쿼리 결과가 포함된 테이블을 만들 수 있도록 하기 위해 필요합니다. Braze는 세그먼트별로 임시 테이블을 생성하며, 이 임시 테이블은 Braze가 세그먼트를 업데이트하는 동안에만 유지됩니다. 

자격 증명 생성 단계에서 Braze 대시보드에 토큰을 입력해야 할 때까지 토큰을 안전한 곳에 보관하세요.

#### 2.2단계: Braze IP에 대한 액세스 허용    

네트워크 정책을 설정한 경우, 데이터브릭스 인스턴스에 대한 네트워크 액세스 권한을 Braze에 부여해야 합니다. Braze 대시보드의 지역에 해당하는 아래 IP에서 액세스를 허용합니다.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% tab Microsoft Fabric %}
#### 2.1단계: 패브릭 리소스에 대한 액세스 권한 부여 
Braze는 Entra ID 인증이 있는 서비스 주체를 사용하여 Fabric 웨어하우스에 연결합니다. Braze가 사용할 새 서비스 주체를 생성하고 필요에 따라 Fabric 리소스에 대한 액세스 권한을 부여합니다. Braze를 연결하려면 다음 세부 정보가 필요합니다:    

* Azure 계정의 테넌트 ID(디렉터리라고도 함) 
* 서비스 주체에 대한 주체 ID(애플리케이션 ID라고도 함) 
* Braze가 인증하기 위한 클라이언트 암호

1. Azure 포털에서 Microsoft Entra 관리 센터로 이동한 다음 **앱 등록으로** 이동합니다.
2. **신원 > 애플리케이션 > 앱 등록에서** **\+ 신규 등록을** 선택합니다 **.** 
3. 이름을 입력하고 지원되는 계정 유형으로 `Accounts in this organizational directory only` 을 선택합니다. 그런 다음 **등록을** 선택합니다. 
4. 방금 만든 애플리케이션(서비스 주체)을 선택한 다음 **인증서 & 비밀 > + 새 클라이언트 비밀로** 이동합니다.
5. 비밀 번호에 대한 설명을 입력하고 비밀 번호의 만료 기간을 설정합니다. 그런 다음 **추가를** 선택합니다. 
6. Braze 설정에서 사용하기 위해 생성한 클라이언트 비밀 번호를 기록해 두세요. 

{% alert note %}
Azure에서는 서비스 계정 암호의 만료를 무제한으로 허용하지 않습니다. 만료되기 전에 자격 증명을 새로고침하여 Braze에 대한 데이터 흐름을 유지해야 한다는 점을 잊지 마세요.
{% endalert %}

#### 2.2단계: 패브릭 리소스에 대한 액세스 권한 부여 
Braze가 Fabric 인스턴스에 연결할 수 있는 액세스 권한을 제공해야 합니다. Fabric 관리자 포털에서 **설정** > **거버넌스 및 인사이트** > **관리자 포털** > **테넌트 설정으로** 이동합니다.    

* **개발자 설정에서** "서비스 주체가 Fabric API를 사용할 수 있음"을 인에이블먼트하여 Braze가 Microsoft Entra ID를 사용하여 연결할 수 있도록 하세요.
* 서비스 주체가 외부 앱에서 데이터에 액세스할 수 있도록 **원레이크 설정에서** "사용자가 Fabric 외부의 앱으로 원레이크에 저장된 데이터에 액세스할 수 있음"을 인에이블먼트하세요.

#### 2.3단계: 웨어하우스 연결 문자열 가져오기 

Braze를 연결하려면 웨어하우스에 대한 SQL 엔드포인트가 필요합니다. SQL 엔드포인트를 검색하려면 Fabric의 **워크스페이스로** 이동하여 항목 목록에서 창고 이름 위로 마우스를 가져간 다음 **SQL 연결 문자열 복사를** 선택합니다.

사용자가 SQL 연결 문자열을 검색해야 하는 Microsoft Azure의 "Fabric Console" 페이지입니다.]({% image_buster /assets/img/cloud_ingestion/fabric_1.png %})

#### 2.4단계: 방화벽에서 Braze IP 허용(선택 사항)

Microsoft Fabric 계정의 구성에 따라 방화벽에서 다음 IP 주소를 허용하여 Braze의 트래픽을 허용해야 할 수 있습니다. 인에이블먼트에 대한 자세한 내용은 [Entra 조건부 액세스에](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access) 대한 관련 설명서를 참조하세요.

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### 3단계: Braze 대시보드에서 연결된 소스 만들기

{% tabs %}
{% tab Snowflake %}
#### 3.1단계: Snowflake 연결 정보 및 소스 테이블 추가하기

Braze 대시보드에서 연결된 소스를 만듭니다. **데이터 설정** > **클라우드 데이터 수집** > **연결된 소스로** 이동한 다음 **새 데이터 동기화 만들기** > **Snowflake 가져오기를** 선택합니다.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Snowflake 데이터 웨어하우스 및 소스 스키마에 대한 정보를 입력한 다음 다음 단계로 진행합니다.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_1.png %})

#### 3.2단계: 동기화 세부 정보 구성

연결된 소스의 이름을 선택합니다. 이 이름은 새 CDI 세그먼트 확장을 만들 때 사용 가능한 소스 목록에 사용됩니다. 

이 소스의 최대 런타임을 구성합니다. Braze는 세그먼트를 생성하거나 새로고침할 때 최대 런타임을 초과하는 모든 쿼리를 자동으로 중단합니다. 허용되는 최대 런타임은 60분이며, 런타임이 짧을수록 Snowflake 계정에서 발생하는 비용이 줄어듭니다. 

{% alert note %}
쿼리 시간이 계속 초과되고 최대 실행 시간을 60분으로 설정한 경우, 쿼리 실행 시간을 최적화하거나 더 큰 저장소를 Braze 사용자에게 할당하는 것을 고려해 보세요.
{% endalert %}

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_2.png %})

#### 3.3단계: 공개 키에 유의하십시오.  

**연결 테스트** 단계에서 RSA 공개 키를 기록해 두세요. Snowflake에서 통합을 완료하려면 이 정보가 필요합니다.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_3.png %})

{% endtab %}
{% tab Redshift %}
#### 3.1단계: Redshift 연결 정보 및 소스 테이블 추가

Braze 대시보드에서 연결된 소스를 만듭니다. **데이터 설정** > **클라우드 데이터 수집** > **연결된 소스로** 이동한 다음, **데이터 연결 만들기** > **Amazon Redshift 가져오기를** 선택합니다.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Redshift 데이터 웨어하우스 및 소스 스키마에 대한 정보를 입력한 후 다음 단계로 진행합니다.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_1.png %})

#### 3.2단계: 동기화 세부 정보 구성

연결된 소스의 이름을 선택합니다. 이 이름은 새 CDI 세그먼트 확장을 만들 때 사용 가능한 소스 목록에 사용됩니다. 

이 소스의 최대 런타임을 구성합니다. Braze는 세그먼트를 생성하거나 새로고침할 때 최대 런타임을 초과하는 모든 쿼리를 자동으로 중단합니다. 허용되는 최대 런타임은 60분이며, 런타임이 짧을수록 Redshift 계정에서 발생하는 비용이 줄어듭니다. 

{% alert note %}
쿼리 시간이 계속 초과되고 최대 실행 시간을 60분으로 설정한 경우, 쿼리 실행 시간을 최적화하거나 더 큰 저장소를 Braze 사용자에게 할당하는 것을 고려해 보세요.
{% endalert %}

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_2.png %})

#### 3.3단계: 공개 키 참고(선택 사항)

자격 증명에 **SSH 터널로 연결이** 선택되어 있는 경우, **연결 테스트** 단계에서 RSA 공개 키를 기록해 두세요. Redshift에서 통합을 완료하려면 이 정보가 필요합니다.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_3.png %})

{% endtab %}
{% tab BigQuery %}
#### 3.1단계: BigQuery 연결 정보 및 소스 테이블 추가

Braze 대시보드에서 연결된 소스를 만듭니다. **데이터 설정** > **클라우드 데이터 수집** > **연결된 소스로** 이동한 다음, **새 데이터 동기화 만들기** > **Google BigQuery 가져오기를** 선택합니다.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

BigQuery 프로젝트 및 데이터 집합에 대한 정보를 입력한 다음 다음 단계로 진행합니다.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_bg_1.png %})

#### 3.2단계: 동기화 세부 정보 구성

연결된 소스의 이름을 선택합니다. 이 이름은 새 CDI 세그먼트 확장을 만들 때 사용 가능한 소스 목록에 사용됩니다. 

이 소스의 최대 런타임을 구성합니다. Braze는 세그먼트를 생성하거나 새로고침할 때 최대 런타임을 초과하는 모든 쿼리를 자동으로 중단합니다. 허용되는 최대 런타임은 60분이며, 런타임이 짧을수록 BigQuery 계정에서 발생하는 비용이 줄어듭니다. 

{% alert note %}
쿼리 시간이 계속 초과되고 최대 실행 시간을 60분으로 설정한 경우, 쿼리 실행 시간을 최적화하거나 더 큰 저장소를 Braze 사용자에게 할당하는 것을 고려해 보세요.
{% endalert %}

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_bg_2.png %})

#### 3.3단계: 연결 테스트

**연결 테스트를** 선택하여 사용자에게 표시되는 테이블 목록이 예상한 것과 일치하는지 확인한 다음 **완료를** 선택합니다. 이제 연결된 소스가 생성되어 CDI 세그먼트 확장에 사용할 준비가 되었습니다.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% tab Databricks %}
#### 3.1단계: 데이터브릭스 연결 정보 및 소스 테이블 추가하기

Braze 대시보드에서 연결된 소스를 만듭니다. **데이터 설정** > **클라우드 데이터 수집** > **연결된 소스로** 이동한 다음 **새 데이터 동기화 만들기** > **데이터브릭스 가져오기를** 선택합니다.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

데이터브릭스 자격 증명과 선택 사항인 카탈로그 및 소스 스키마에 대한 정보를 입력한 후 다음 단계로 진행합니다.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_databricks_1.png %})

#### 3.2단계: 동기화 세부 정보 구성

연결된 소스의 이름을 선택합니다. 이 이름은 새 CDI 세그먼트 확장을 만들 때 사용 가능한 소스 목록에 사용됩니다. 

이 소스의 최대 런타임을 구성합니다. Braze는 세그먼트를 생성하거나 새로고침할 때 최대 런타임을 초과하는 모든 쿼리를 자동으로 중단합니다. 허용되는 최대 런타임은 60분이며, 런타임이 짧을수록 데이터브릭스 계정에서 발생하는 비용이 줄어듭니다. 

{% alert note %}
쿼리 시간이 계속 초과되고 최대 실행 시간을 60분으로 설정한 경우, 쿼리 실행 시간을 최적화하거나 더 큰 저장소를 Braze 사용자에게 할당하는 것을 고려해 보세요.
{% endalert %}

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_db_2.png %})

#### 3.3단계: 연결 테스트

**연결 테스트를** 선택하여 사용자에게 표시되는 테이블 목록이 예상한 것과 일치하는지 확인한 다음 **완료를** 선택합니다. 이제 연결된 소스가 생성되어 CDI 세그먼트 확장에 사용할 준비가 되었습니다.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% tab Microsoft Fabric %}
#### 3.1단계: Microsoft 패브릭 연결 정보 및 소스 테이블 추가

Braze 대시보드에서 연결된 소스를 만듭니다. **데이터 설정** > **클라우드 데이터 수집** > **연결된 소스로** 이동한 다음, **새 데이터 동기화 만들기** > **Microsoft 패브릭 가져오기를** 선택합니다.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Microsoft 패브릭 자격 증명과 소스 웨어하우스 및 스키마에 대한 정보를 입력한 다음 다음 단계로 진행합니다.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_mf_1.png %})

#### 3.2단계: 동기화 세부 정보 구성

연결된 소스의 이름을 선택합니다. 이 이름은 새 CDI 세그먼트 확장을 만들 때 사용 가능한 소스 목록에 사용됩니다. 

이 소스의 최대 런타임을 구성합니다. Braze는 세그먼트를 생성하거나 새로고침할 때 최대 런타임을 초과하는 모든 쿼리를 자동으로 중단합니다. 허용되는 최대 런타임은 60분이며, 런타임이 짧을수록 Microsoft Fabric 계정에서 발생하는 비용이 줄어듭니다. 

{% alert note %}
쿼리 시간이 지속적으로 초과되고 최대 실행 시간을 60분으로 설정한 경우 쿼리 실행 시간을 최적화하거나 Fabric 용량을 확장하는 것을 고려해 보세요.
{% endalert %}

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_mf_2.png %})

#### 3.3단계: 연결 테스트

**연결 테스트를** 선택하여 사용자에게 표시되는 테이블 목록이 예상한 것과 일치하는지 확인한 다음 **완료를** 선택합니다. 이제 연결된 소스가 생성되어 CDI 세그먼트 확장에 사용할 준비가 되었습니다.

\![]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% endtabs %}

### 4단계: 데이터 웨어하우스 구성 마무리하기

{% tabs %}
{% tab Snowflake %}
마지막 단계에서 기록한 공개 키를 Snowflake에서 사용자에게 추가합니다. 이렇게 하면 Braze가 Snowflake에 연결할 수 있습니다. 이 작업에 대한 자세한 내용은 [Snowflake 설명서를](https://docs.snowflake.com/en/user-guide/key-pair-auth.html) 참조하세요. 

언제든지 키를 교체하려면 **클라우드 데이터 수집의** **데이터 액세스 관리로** 이동하여 해당 계정에 대한 **새 키 생성을** 선택하여 새 공개 키를 만들 수 있습니다.

새 키 생성 버튼이 있는 Snowflake 데이터 액세스 자격 증명을 위한 데이터 액세스 관리.]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_4.png %})

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='{INSERT_YOUR_KEY}';
```

Snowflake에서 사용자에게 키를 추가한 후 Braze에서 **테스트 연결을** 선택한 다음 **완료를** 선택합니다. 이제 연결된 소스가 생성되어 CDI 세그먼트 확장에 사용할 준비가 되었습니다.
{% endtab %}

{% tab Redshift %}
SSH 터널로 연결하는 경우 마지막 단계에서 기록한 공개 키를 SSH 터널 사용자에게 추가합니다. 

사용자에게 키를 추가한 후 Braze에서 **연결 테스트를** 선택한 다음 **완료를** 선택합니다. 이제 연결된 소스가 생성되어 CDI 세그먼트 확장에 사용할 준비가 되었습니다.

{% endtab %}
{% tab BigQuery %}
이는 BigQuery에는 적용되지 않습니다.

{% endtab %}
{% tab Databricks %}
데이터브릭스에는 적용되지 않습니다.

{% endtab %}
{% tab Microsoft Fabric %}
이는 Microsoft Fabric에는 적용되지 않습니다.

{% endtab %}
{% endtabs %}

{% alert note %}
소스를 '초안'에서 '활성' 상태로 전환하려면 테스트를 성공적으로 마쳐야 합니다. 생성 페이지에서 닫아야 하는 경우 통합이 저장되며 세부 정보 페이지를 다시 방문하여 변경하고 테스트할 수 있습니다.  
{% endalert %}

## 추가 통합 또는 사용자 설정(선택 사항)

{% tabs %}
{% tab Snowflake %}
Braze와 여러 통합을 설정할 수 있지만 각 통합은 서로 다른 스키마를 연결하도록 구성해야 합니다. 추가 연결을 만들 때 동일한 Snowflake 계정에 연결할 경우 기존 자격 증명을 재사용할 수 있습니다.

여러 통합에서 동일한 사용자 및 역할을 재사용하는 경우 공개 키를 다시 추가할 필요가 없습니다.
{% endtab %}

{% tab Redshift %}
Braze로 여러 소스를 설정할 수 있지만 각 소스는 서로 다른 스키마를 연결하도록 구성해야 합니다. 추가 소스를 만들 때 동일한 Redshift 계정에 연결하는 경우 기존 자격 증명을 재사용할 수 있습니다.
{% endtab %}

{% tab BigQuery %}
Braze로 여러 소스를 설정할 수 있지만, 각 소스는 서로 다른 데이터 집합을 연결하도록 구성해야 합니다. 추가 소스를 만들 때 동일한 BigQuery 계정에 연결하는 경우 기존 자격 증명을 재사용할 수 있습니다.
{% endtab %}

{% tab Databricks %}
Braze로 여러 소스를 설정할 수 있지만 각 소스는 서로 다른 스키마를 연결하도록 구성해야 합니다. 추가 소스를 만들 때 동일한 데이터브릭스 계정에 연결하는 경우 기존 자격 증명을 재사용할 수 있습니다.
{% endtab %}

{% tab Microsoft Fabric %}
Braze로 여러 소스를 설정할 수 있지만 각 소스는 서로 다른 스키마를 연결하도록 구성해야 합니다. 추가 소스를 만들 때 동일한 Azure 계정에 연결하는 경우 기존 자격 증명을 재사용할 수 있습니다.
{% endtab %}
{% endtabs %}

## 연결된 소스 사용

소스가 생성된 후에는 이를 사용하여 하나 이상의 CDI 세그먼트 확장을 만들 수 있습니다. 이 소스를 사용하여 세그먼트를 만드는 방법에 대한 자세한 내용은 [CDI 세그먼트 확장 설명서를]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/) 참조하세요.

{% alert note %}
쿼리 시간이 계속 초과되고 최대 실행 시간을 60분으로 설정한 경우, 쿼리 실행 시간을 최적화하거나 더 큰 저장소 등 더 많은 컴퓨팅 리소스를 Braze 사용자에게 할당하는 것을 고려해 보세요.
{% endalert %}
