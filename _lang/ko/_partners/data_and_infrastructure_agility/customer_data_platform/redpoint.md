---
nav_title: Redpoint
article_title: Redpoint 
description: "Redpoint와 Braze의 통합을 통해 퍼스트파티 데이터로 Braze 고객 프로필을 온보딩하고 보강할 수 있습니다."
alias: /partners/redpoint/
page_type: partner
search_tag: Redpoint
---

# Redpoint

> [Redpoint][2]는 마케터에게 완전히 통합된 캠페인 오케스트레이션 플랫폼을 제공하는 기술 플랫폼입니다. Redpoint의 세분화, 예약 및 자동화 기능을 활용하여 CDP 데이터를 Braze로 가져오는 방법과 시기를 제어할 수 있습니다.

Braze와 Redpoint의 통합을 통해 Redpoint CDP 데이터를 기반으로 Braze 세그먼트를 만들 수 있습니다. Redpoint는 Braze에 데이터를 전달하는 두 가지 모드를 제공합니다. 

1. **브레이즈 온보딩 및 업서트** 모드: Redpoint에서 Braze로 고객 프로필을 '업서트'합니다. 데이터가 변경된 경우 사용자 레코드를 온보딩하거나 업데이트하는 데 사용됩니다. 
2. **Braze 추가** 모드: 해당 사용자가 이미 Braze에 존재하는 경우 사용자 프로필을 업데이트합니다. 

각 모드에 대한 내보내기 템플릿과 아웃바운드 채널을 구성합니다.

{% alert note %}
"업서트"는 "업데이트"와 "삽입"이라는 단어의 조합입니다. 데이터베이스 테이블에 새 레코드가 없는 경우 이를 삽입하거나 레코드가 있는 경우 이를 업데이트하려는 경우에 사용됩니다. 기본적으로 업서트는 특정 레코드가 데이터베이스에 있는지 여부를 확인합니다. 레코드가 있으면 업데이트되고, 없으면 새 레코드가 삽입됩니다.
{% endalert %}

## 전제 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br>이는 **설정** > **API 키**에서 Braze 대시보드에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [당신의 REST 엔드포인트 URL][1]. 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
| Redpoint 데이터 관리 아티팩트 | Braze 통합은 일련의 Redpoint 데이터 관리 아티팩트에 의해 지원됩니다. Redpoint 데이터 관리 버전에 대한 아티팩트를 요청하려면 [Redpoint 지원][3]에 문의하세요. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
[이전 탐색]({{site.baseurl}}/navigation)을 사용하는 경우 **개발자 콘솔** > **API 설정**에서 API 키를 생성할 수 있습니다.
{% endalert %}

## Redpoint CDP 커스텀 속성

Braze 고객 프로필에 추가할 수 있는 Redpoint 커스텀 속성은 다음과 같습니다.

| 필드               | 설명                                                                                                       |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `rpi_cdp_attributes` | Redpoint CDP 프로필 속성 오브젝트                                                                                  |
| `rpi_audience_outputs`| Redpoint 아웃바운드 전달 Braze 채널 실행에서 사용자가 타겟팅되는 오디언스 출력 태그 배열         |
| `rpi_offers`         | Redpoint 아웃바운드 전달 Braze 채널 실행에서 사용자가 타겟팅되는 오퍼 태그 배열                   |
| `rpi_contact_ids`    | Redpoint 아웃바운드 전달 Braze 채널 실행에서 사용자가 타겟팅되는 오퍼 이력 연락처 ID 배열     |
| `rpi_channel_exec_ids`| Redpoint 아웃바운드 전달 Braze 채널 실행에서 사용자가 타겟팅되는 채널 실행 ID 배열       |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][4]{: style="max-width:75%;"}

## 통합

### 1단계: 템플릿 설정

#### 1a단계: Braze 온보딩 및 업서트 템플릿 만들기

Redpoint Interaction(RPI)에서 새 내보내기 템플릿을 생성하고 이름을 **Braze 온보딩 및 업서트**로 지정합니다. 이 템플릿에서는 Braze의 고객 프로필에 추가하려는 추가 커스텀 속성과 함께 Redpoint CDP와 Braze 고객 프로필 간의 핵심 매핑을 정의합니다.

Redpoint CDP 속성을 **속성** 열로 드래그합니다. 각 **헤더 행 값**을 해당 Braze [사용자 속성][17]으로 설정합니다. 

다음 표에는 Redpoint CDP 속성과 그에 해당하는 Braze 속성이 나열되어 있습니다.

| Redpoint 속성 | 헤더 행 값 |
|--------------------|------------------|
| PID                | `external_id`    |
| Fist 이름          | `first_name`     |
| 성          | `last_name`      |
| 기본 이메일      | `email`          |
| 기본 국가    | `country`        |
| DOB                | `dob`            |
| 성별             | `gender`         |
| 기본 도시       | `home_city`      |
| 기본 전화      | `phone`          |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

**오퍼 내역** 테이블에서 **출력 이름** 속성을 추가합니다. 마지막으로, Braze에 병합하려는 커스텀 Redpoint 속성을 추가합니다. 예를 들어 다음은 교육, 소득, 결혼 여부가 추가 속성으로 포함된 온보딩 및 업서트 템플릿입니다.

![][7]{: style="max-width:75%;"}

#### 1b단계: Braze 추가 템플릿 만들기

추가 전용 작업을 위한 두 번째 내보내기 템플릿을 **Braze 추가**라는 이름으로 생성합니다.

이 템플릿에는 두 가지 속성만 설정합니다. **PID**에서 **헤더 행 값**을 `external_id`로 설정합니다. **출력 이름**에서 **헤더 행**을 `output_name`으로 설정합니다.

![`external_id` 및 출력 이름 속성이 포함된 샘플 내보내기 템플릿.][8]{: style="max-width:75%;"}

#### 1c단계: 날짜 형식 설정

두 내보내기 템플릿 모두 **옵션** 탭으로 이동하여 **날짜 형식**을 **커스텀 형식** 값으로 설정합니다. 형식을 **yyyy-MM-dd**로 설정합니다.

![yyyy-MM-dd로 설정된 날짜 형식을 보여주는 옵션 탭.][16]{: style="max-width:75%;"}

### 2단계: 아웃바운드 채널 만들기

RPI에서 두 개의 새 채널을 만듭니다. 두 채널을 모두 **아웃바운드 배달로** 설정합니다. 한 채널의 이름을 **Braze 온보딩 및 업서트**로, 다른 채널의 이름을 **Braze 추가**로 지정합니다.

![][9]{: style="max-width:75%;"}

{% alert note %}
CDP 레코드를 Braze에 처음 온보딩한 후, Braze 온보딩 및 업서트 채널을 사용하는 후속 Redpoint 상호 작용 워크플로가 초기 온보딩 동기화 이후 변경된 레코드만 선택하도록 설계되었는지 확인합니다.
{% endalert %}

### 3단계: 채널 구성

#### 3a단계: 템플릿 및 내보내기 경로 형식 설정

채널 **구성** 화면에서 **일반** 탭으로 이동합니다. 내보내기 템플릿을 각 채널로 설정합니다. 

다음으로, 두 채널 모두에서 공유 네트워크, 파일 전송 프로토콜 또는 외부 콘텐츠 공급자 위치를 가리키는 **내보내기 경로 형식**을 정의합니다. 해당 위치는 Redpoint Interaction과 Redpoint Data Management 모두에서 액세스할 수 있습니다. 

![][10]{: style="max-width:75%;"}

두 채널의 내보내기 디렉터리 형식은 동일하며 `\\[Channel]\\[Offer]\\[Workflow ID]` 로 끝나야 합니다.

![][11]{: style="max-width:50%;"}

#### 3b단계: 사후 실행 구성

채널 **구성** 화면에서 **실행 후** 탭으로 이동합니다. 

채널 실행 후 서비스 URL을 호출하려면 **실행 후** 확인란을 선택합니다. Redpoint 데이터 관리 웹 서비스 URL을 입력합니다. 이 항목은 온보딩 채널과 추가 채널 모두에서 동일합니다.

![][14]{: style="max-width:75%;"}

### 4단계: Redpoint 데이터 관리에서 Braze 구성요소 설정 

Braze 통합을 지원하기 위한 Redpoint 데이터 관리(RPDM) 아티팩트가 포함된 아카이브에는 필요한 구성요소를 설정하는 자세한 지침이 포함된 README가 포함되어 있습니다. 통합을 구성할 때 다음 세부 사항을 염두에 두세요. 

#### 4a단계: Braze REST 엔드포인트 및 기본 RPI 출력 디렉토리를 사용하여 Braze로 RPI 자동화를 업데이트합니다. 

Braze 관련 아티팩트를 Redpoint 데이터 관리로 가져온 후, **AUTO_Process_RPI_to_Braze**라는 이름의 자동화를 열고 다음 두 자동화 변수를 맞는 값으로 업데이트합니다.

* **BRAZE_API_URL**: Braze REST 엔드포인트
* **BASE_OUTPUT_DIRECTORY**: Redpoint Interaction과 Redpoint 데이터 관리 간의 공유 출력 디렉토리

![][5]{: style="max-width:40%;"}

#### 4b단계: RPI를 Braze 추가 프로젝트로 업데이트하세요. 

**PROJ_RPI_to_Braze_Append**라는 이름의 Redpoint 데이터 관리 프로젝트에는 Braze의 `rpi_cdp_attributes` 커스텀 속성 오브젝트에 대한 아웃바운드 전달 내보내기 파일 스키마 및 매핑이 포함되어 있습니다. 

내보내기 파일 템플릿에 정의된 추가 커스텀 CDP 속성을 사용하여 파일 입력 스키마와 문서 인젝터 툴(**Braze로 RPI 문서 인젝터**)을 업데이트합니다. 이 예는 교육, 소득 및 결혼 여부에 대한 추가 매핑을 보여줍니다:

![][6]{: style="max-width:40%;"}

## 통합 사용

이제 Redpoint Interaction 워크플로 내에서 아웃바운드 전달 Braze 채널을 활용할 수 있습니다. RPI에서 선택 규칙 및 오디언스를 생성하고 관련 워크플로 스케줄 및 트리거를 빌드하는 표준 관행을 따르세요. 

RPI 오디언스 출력을 Braze에 동기화하려면 아웃바운드 전송 오퍼를 생성하고 이를 **Braze 온보딩 및 업서트** 또는 **Braze 앱드** 채널에 연결합니다. 이는 Braze에서 새 기록을 생성하거나 병합하려는 의도인지, 아니면 기록이 이미 Braze에 존재하는 경우 캠페인 데이터만 추가하려는 것인지에 따라 달라집니다.

![][13]{: style="max-width:80%;"}

RPI에서 워크플로가 성공적으로 실행되면 이제 RPI에서 가져온 오케스트레이션 및 CDP 데이터를 사용하여 Braze에서 세그먼트를 생성할 수 있습니다.

![][12]{: style="max-width:80%;"}

사용자 프로필에서 Redpoint 관련 속성을 볼 수 있습니다.

![][15]{: style="max-width:80%;"}

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://www.redpointglobal.com
[3]: https://support.redpointglobal.com/hc/en-us/restricted?return_to=https%3A%2F%2Fsupport.redpointglobal.com%2Fhc%2Fen-us
[4]: {% image_buster /assets/img/redpoint/rpi_to_braze_custom_attributes.png %}
[5]: {% image_buster /assets/img/redpoint/rpi_to_braze_auto_variables.png %}
[6]: {% image_buster /assets/img/redpoint/rpi_to_braze_doc_injector_mappings.png %}
[7]: {% image_buster /assets/img/redpoint/rpi_to_braze_upsert_export_format.png %}
[8]: {% image_buster /assets/img/redpoint/rpi_to_braze_append_export_format.png %}
[9]: {% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_general.png %}
[10]: {% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_specific.png %}
[11]: {% image_buster /assets/img/redpoint/rpi_to_braze_export_directory_setup.png %}
[12]: {% image_buster /assets/img/redpoint/rpi_to_braze_build_braze_segment.png %}
[13]: {% image_buster /assets/img/redpoint/rpi_to_braze_rpi_canvas.png %}
[14]: {% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_post_execution.png %}
[15]: {% image_buster /assets/img/redpoint/rpi_to_braze_record_example.png %}
[16]: {% image_buster /assets/img/redpoint/rpi_to_braze_export_format_config.png %}
[17]: {{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields
