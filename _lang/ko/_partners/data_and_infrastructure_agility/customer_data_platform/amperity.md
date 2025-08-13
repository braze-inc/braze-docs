---
nav_title: Amperity
article_title: Amperity
alias: /partners/amperity/
description: "이 참조 문서에서는 종합적인 엔터프라이즈 고객 데이터 플랫폼인 Braze와 Amperity 간의 파트너십에 대해 설명하며, 이를 통해 Amperity 사용자를 동기화하고, 데이터를 통합하고, AWS S3 버킷을 사용하여 데이터를 Braze로 전송하는 등의 작업을 수행할 수 있습니다."
page_type: partner
search_tag: Partner

---

# Amperity

> [Amperity는](https://amperity.com/) 종합적인 기업 고객 데이터 플랫폼으로, 브랜드가 고객을 파악하고 전략적 결정을 내리며 소비자에게 더 나은 서비스를 제공하기 위한 올바른 조치를 일관되게 취할 수 있도록 지원합니다. Amperity는 데이터 관리 통합, 분석, 인사이트, 활성화 전반에 걸쳐 지능적인 기능을 제공합니다.

_This integration is maintained by Amperity._

{% multi_lang_include video.html id="06G0lxaSjgk" align="오른쪽" %}

Braze와 Amperity의 통합은 두 플랫폼에서 고객에 대한 통합된 보기를 제공합니다. 이 통합을 통해 다음을 수행할 수 있습니다:
- **고객 프로필 동기화**: 사용자 데이터와 사용자 지정 속성을 Amperity에서 Braze로 매핑하세요. 
- **오디언스 생성 및 전송**: 활성 고객 목록과 관련 커스텀 속성을 Braze에 반환하는 세그먼트를 구축하여 Braze로 전송합니다.
- **데이터 업데이트 관리**: 사용자 지정 속성에 대한 업데이트를 Braze에 전송하는 빈도를 제어합니다.
- **데이터 통합**: Amperity가 지원하는 다양한 플랫폼과 Braze에서 데이터를 통합합니다.
- **Braze 데이터를 Amazon S3에 동기화합니다**: Braze Currents를 사용하면 Braze 캠페인의 참여 데이터를 통합하여 데이터를 Apache Avro 형식으로 Amazon S3에 동기화할 수 있습니다.

## 필수 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Amperity 계정 | 이 파트너십을 이용하려면 [Amperity 계정이](https://amperity.com/request-a-demo) 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br> Braze 대시보드에서 **개발자 콘솔** > **API 키 복원** > **새 API 키 생성으로** 이동하여 생성할 수 있습니다. |
| 브레이즈 인스턴스 | Braze 인스턴스는 Braze 온보딩 매니저로부터 가져오거나 [API 개요 페이지]({{site.baseurl}}/api/basics#endpoints)에서 찾을 수 있습니다. |
| Braze REST 엔드포인트 | Braze 엔드포인트 URL. 엔드포인트는 Braze 인스턴스에 따라 달라집니다. |
| 커런츠 커넥터(선택 사항) | S3 전류 커넥터. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 데이터 매핑

표준 및 사용자 지정 속성을 모두 Amperity에서 Braze로 전송할 수 있으므로, 다양한 소스의 데이터로 Braze의 고객 프로필을 Amperity를 통해 강화할 수 있습니다. 전송할 수 있는 특정 속성은 Amperity 시스템의 데이터와 Braze에서 설정한 속성에 따라 달라집니다.

아래에서 이러한 속성에 대해 자세히 알아보세요.

### 표준 속성 

[프로필 속성]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields)은 고객이 누구인지를 설명합니다. 다음과 같이 고객의 신원과 관련된 경우가 많습니다.
- 이름
- 생년월일
- 이메일 주소
- 전화번호

### 사용자 지정 속성 

Braze의 [커스텀 속성]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/)은 브랜드에 따라 결정되는 필드입니다. Amperity에서 Braze에 이미 존재하는 커스텀 속성을 관리하려면 Amperity에서 전송되는 출력을 Braze 워크스페이스에 이미 있는 이름과 일치시킵니다. 여기에는 다음이 포함될 수 있습니다:
- 구매 내역
- 로열티 상태
- 가치 계층
- 최근 참여 데이터

Amperity에서 Braze로 전송할 커스텀 속성의 이름을 확인합니다. Amperity는 일치하는 이름이 없을 때마다 사용자 지정 속성을 추가합니다.

커스텀 속성은 Braze 내에서 `external_id` 또는 `braze_id`가 일치하는 사용자에 대해서만 업데이트됩니다.

### Amperity 오디언스

Amperity에서 Braze로 동기화된 오디언스는 사용자 프로필에 사용자 지정 속성으로 기록됩니다. 그런 다음 이를 사용하여 Braze에서 해당 사용자를 타겟팅할 수 있습니다.

![사용자 지정 데이터 카테고리에 사용자 지정 속성이 있는 필터의 드롭다운 목록이 표시됩니다.][1]{: style="max-width:60%;"}

!['l12m_frequency' 및 'l12m_monetary'와 같은 커스텀 속성을 포함하는 드롭다운 목록.][2]{: style="max-width:40%;"}

### 데이터 유형

지원되는 데이터 유형은 다음과 같습니다:
- 부울
- 날짜
- Datetime
- 소수
- 플로트
- 정수
- 문자열
- Varchar

사용되는 데이터 유형은 속성의 특성에 따라 다릅니다. 예를 들어 이메일 주소는 문자열이고 고객의 나이는 정수일 수 있습니다.

### 속성 중복

기본 사용자 프로필 필드와 중복되는 사용자 지정 속성을 보내지 마세요. For example, birthdates should be sent to Braze as a user profile field named "dob" to match the Braze standard attribute. '생일', '생년월일' 또는 기타 문자열로 전송되는 경우 커스텀 속성이 생성되며 'dob' 필드의 값은 업데이트되지 않습니다.

### 데이터 포인트

Amperity는 Braze에 동기화할 때마다 변경되는 사항과 전반적인 전송 상태를 추적합니다. Amperity는 마지막 동기화 이후 변경된 목록 멤버십 및 기타 선택된 속성만 Braze에 전송합니다.  

## 통합

### 1단계: Braze의 구성 세부 정보 캡처

1. **사용자 데이터** 아래의 `users.track` 권한으로 Braze 워크스페이스에 대한 Braze REST API 키를 만듭니다. `users.track` 엔드포인트는 Amperity 오디언스를 사용자 지정 속성으로 Braze에 동기화합니다.
2. Braze 인스턴스에 대한 [REST API 엔드포인트를]({{site.baseurl}}/api/basics#endpoints) 결정합니다. 예를 들어, Braze URL이 `https://dashboard-03.braze.com`이고 REST API 엔드포인트가 `https://rest.iad-03.braze.com`이며 인스턴스가 US-03'인 경우가 있습니다.
3. Amperity에서 Braze로 전송할 수 있는 [사용자 프로필 필드]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields) 및 [사용자 지정 속성]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) 목록을 결정합니다.

### 2단계: Braze를 대상으로 설정(DataGrid 운영자)

#### 2a단계: 고객 프로필 테이블 구축

Amperity의 Customer 360 데이터베이스에 'Braze 고객 속성'이라는 새 표를 생성합니다. 이 표에는 브랜드가 Amperity에서 관리하고자 하는 Braze의 모든 속성이 포함되어야 하며, 여기에는 Braze에서 요구하는 기본 사용자 프로필 필드와 사용자 지정 속성이 모두 포함되어야 합니다. [Amperity 설명서](https://docs.amperity.com/datagrid/destination_braze.html#customer-profiles-table)에 표시된 대로 SQL을 사용하여 이 테이블의 구조를 정의합니다.

#### 2b단계: 테이블 이름 지정, 유효성 검사 및 저장

테이블 이름을 "Braze Customer Attributes"로 지정하고 저장합니다. 캠페인 내에서 **세그먼트** 편집기 및 **속성** 편집기에서 테이블에 액세스할 수 있는지 확인합니다.

#### 2c단계: Braze를 목적지로 추가

앰퍼티 플랫폼에서 **대상** 탭으로 이동합니다. 새 대상을 추가하는 옵션을 찾습니다. 사용 가능한 옵션에서 **Braze**를 선택합니다.

![이름이 'Braze API'이고 설명이 'Braze로 오디언스 속성 전송'이며 플러그인이 'Braze'인 새 대상 섹션.][3]{: style="max-width:60%;"}

#### 2d단계: 대상 세부 정보 구성

[Amperity 설명서](https://docs.amperity.com/datagrid/destination_braze.html#add-destination)에서 설명한 대로, **Braze 설정** 아래에 Braze 자격 증명과 대상 설정을 제공합니다. 마지막 단계에서 수집한 구성 세부 정보를 입력하고 Braze 식별자를 정의합니다. 일치시킬 수 있는 식별자는 다음과 같습니다:
- `braze_id`: 자동으로 할당된 Braze 식별자로, 변경할 수 없으며 Braze에서 생성될 때 해당 사용자와 연결됩니다.
- `external_id`: 고객이 할당하는 식별자(일반적으로 UUID). 

![인스턴스가 'US-03'이고 사용자 I가 'external_id'이며 세그먼트 이름은 비어 있고 S3 버킷은 'amperity-training-abc123'이며 S3 폴더는 'braze-attributes'인 Braze 설정 섹션.][4]{: style="max-width:60%;"}

#### 2e단계: 데이터 템플릿 추가

**대상** 탭에서 Braze 대상에 대한 메뉴를 열고 **데이터 템플릿 추가**를 선택합니다. 템플릿의 이름과 설명을 입력하고(예: 'Braze' 및 'Braze로 커스텀 속성 전송'), 비즈니스 사용자 액세스 권한을 확인한 다음, 모든 구성 설정을 확인합니다. 

필수 설정이 대상의 일부로 구성되지 않은 경우 데이터 템플릿의 일부로 구성하세요. 데이터 템플릿을 저장합니다.

![이름이 'Braze 오디언스 속성'이고 설명이 'Braze에 오디언스 속성 전송'인 데이터 템플릿 이름 섹션.][5]{: style="max-width:60%;"}

#### 2f 단계: 구성 저장 

필요한 세부 정보를 입력한 후 구성을 저장합니다. Braze가 대상으로 구성되었으므로 Amp360 및 AmpIQ 사용자는 데이터를 Braze에 동기화할 수 있습니다.

### 3단계: Braze에 데이터 동기화

Amperity 테넌트에 대해 Braze가 활성화되어 있는지 확인하세요. 그렇지 않은 경우 DataGrid 운영자 또는 Amperity 담당자에게 도움을 요청하세요.

그런 다음, 회사에 해당하는 Amp360 또는 AmpIQ에 대한 동기화 지침을 따릅니다.

#### 동기화 옵션 1: Amp360을 통해 Braze에 쿼리 결과 보내기

Amp360 사용자는 SQL을 사용하여 자유 양식 쿼리를 작성한 다음, 그 결과를 Braze로 전송하는 스케줄을 구성할 수 있습니다.

##### 1단계: Amperity에서 쿼리 만들기

Amperity의 쿼리 함수로 이동하여 원하는 고객 데이터 집합을 생성하는 SQL 쿼리를 작성합니다. 결과에는 Braze에 전송하려는 특정 속성이 포함되어야 합니다. 구매 내역이 있는 사용자 목록을 반환하는 Amperity 쿼리 예시를 참조하세요.

##### 2단계: Amperity에 새로운 오케스트레이션 추가하기

1. **오케스트레이션** 섹션으로 이동하여 새 오케스트레이션을 추가하는 옵션을 클릭합니다. 
2. 오케스트레이션이 수행해야 할 작업을 지정합니다. 여기에는 일반적으로 실행해야 하는 SQL 쿼리와 결과를 전송할 위치를 지정하는 작업이 포함됩니다. 이 경우 활성 고객 목록을 생성하기 위해 생성한 SQL 쿼리를 선택하고 결과의 대상으로 Braze를 지정합니다.
3. 오케스트레이션을 언제, 얼마나 자주 실행할지 정의합니다. 예를 들어 매일 특정 시간에 오케스트레이션을 실행할 수 있습니다.
4. 오케스트레이션을 원하는 대로 구성한 후 저장하세요. Amperity의 오케스트레이션 목록에 추가됩니다.
5. 오케스트레이션을 테스트하여 예상대로 작동하는지 확인합니다. 오케스트레이션을 수동으로 트리거하고 Braze에서 결과를 확인하면 됩니다.

##### 3단계: 오케스트레이션 실행 

오케스트레이션을 실행하여 쿼리를 실행하고 결과를 Braze로 전송합니다. 이 작업은 수동으로 수행하거나 오케스트레이션 설정에서 설정한 스케줄에 따라 수행할 수 있습니다.

#### 동기화 옵션 2: AmpIQ를 통해 Braze에 오디언스 전송

AmpIQ 사용자는 비-SQL 인터페이스를 통해 Amperity에서 세그먼트를 생성하고 이를 Braze와 같은 다운스트림 대상에 동기화할 수 있습니다. 사용자는 대상을 선택한 다음, 각 대상으로 전송할 속성 목록을 구성할 수 있습니다.

##### 1단계: Amperity에서 세그먼트 만들기 

Amperity에서 고객 목록을 반환하는 세그먼트를 만듭니다. 이 세그먼트는 Braze에서 업데이트하려는 사용자 지정 속성과 연결되어야 합니다.

{% alert note %}
Braze에 보낼 수 있는 다양한 세그먼트 유형의 예제는 Amperity 설명서를 참조하세요.
{% endalert %}

##### 2단계: Amperity에서 캠페인 구축

1. **캠페인** 섹션으로 이동하여 새 캠페인을 만드는 옵션을 클릭합니다.
2. 특히 캠페인이 여러 개 있는 경우 나중에 캠페인을 식별하는 데 도움이 되는 설명적이고 고유한 이름을 지정하세요.
3. 이 캠페인으로 타겟팅할 고객 세그먼트를 선택합니다. 이 세그먼트는 이전에 생성한 세그먼트여야 합니다. <br>![타겟팅에서 제외할 세그먼트의 드롭다운 필드입니다.][6]{: style="max-width:50%;"}<br><br>
4. 캠페인의 일부로 전송할 데이터를 선택합니다. 여기에는 다양한 고객 속성이 포함될 수 있습니다. ![캠페인 속성 편집 Modal에서는 대상 및 고객 속성을 선택할 수 있습니다. ][7]{: style="max-width:90%;"}<br><br>
5. 캠페인 데이터를 전송할 대상으로 **Braze**를 선택합니다.
6. 캠페인을 언제, 얼마나 자주 실행할지 선택하세요. 이는 일회성 이벤트일 수도 있고 반복되는 일정일 수도 있습니다.
7. 캠페인을 저장하고 테스트를 실행하여 예상대로 작동하는지 확인합니다.

##### 3단계: 캠페인 실행

캠페인을 실행하여 세그먼트를 Braze에 전송합니다. 이 작업은 수동으로 수행하거나 캠페인 설정에서 설정한 일정에 따라 수행할 수 있습니다.


### Braze 커런츠와 Amperity 사용
Braze 커런츠 데이터를 Amperity로 전송하려면 다음을 수행합니다.
1. 데이터를 Amazon S3 버킷으로 전송하는 [Braze Current를 설정하세요]({{site.baseurl}}/user_guide/data/braze_currents/setting_up_currents/).
2. [해당 Amazon S3 버킷에서 Apache Avro 파일을 읽도록](https://docs.amperity.com/datagrid/source_amazon_s3.html) Amperity를 구성합니다.
3. 표준 워크플로를 사용하여 피드를 구성하고 데이터 로드를 자동화합니다.


[1]: {% image_buster /assets/img/amperity/custom_attributes_filters.png %}
[2]: {% image_buster /assets/img/amperity/search_custom_attributes_filters.png %}
[3]: {% image_buster /assets/img/amperity/destination_name.png %}
[4]: {% image_buster /assets/img/amperity/braze_settings.png %}
[5]: {% image_buster /assets/img/amperity/data_template_name.png %}
[6]: {% image_buster /assets/img/amperity/select_segments.png %}
[7]: {% image_buster /assets/img/amperity/edit_campaign_attributes.png %}
