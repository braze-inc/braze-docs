---
nav_title: Lytics
article_title: Lytics
description: "이 참조 문서에서는 Braze 및 Lytics 통합에 대해 다룹니다. Lytics는 마케터, 분석가 및 기술 전문가를 위한 엔터프라이즈 고객 데이터 플랫폼입니다. 이 통합을 통해 브랜드는 Lytics 데이터를 Braze에 직접 동기화하고 매핑할 수 있습니다."
alias: /partners/lytics/
page_type: partner
search_tag: Partner
---

# Lytics

> [Lytics][1]는 차세대 고객 중심 비즈니스를 위한 고객 데이터 플랫폼(CDP)입니다. Lytics Decision Engine, Conductor, 및 Cloud Connect 솔루션은 마케터와 데이터 Teams에게 실시간으로 프라이버시를 준수하면서 신원 확인, 오케스트레이션 및 캠페인 최적화를 수행할 수 있는 기회를 제공합니다.

_This integration is maintained by Lytics._

## 통합 정보

Braze와 Lytics 통합은 강력한 개인화를 가능하게 하고 다음 최적의 행동 오케스트레이션 및 결정을 사용하여 최적화된 캠페인을 추진하기 위해 고객에 대한 통합된 뷰를 제공합니다.

통합을 통해 브랜드는 다음을 수행할 수 있습니다:

- Lytics에서 Braze로 직접 오디언스를 내보내기
- 개인화된 캠페인을 지원하고 풍부한 고객 프로필을 빌드하기 위해 Braze 캠페인 또는 캔버스에서 Lytics로 이벤트를 실시간으로 전송합니다.

## 사용 사례

Lytics에 Braze를 연결하여 이메일, SMS 및 푸시 활동을 [가져와](#importing-data-from-braze-to-lytics) Lytics 고객 프로필을 보강합니다. Braze와 Lytics를 함께 사용하면 Lytics의 크로스채널, 행동 기반 오디언스를 [내보내](#integration) 퍼스트파티 데이터를 사용하여 고도로 개인화된 Braze 고객 여정을 빌드할 수 있습니다.

## 필수 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Lytics 계정 | 이 통합을 활용하려면 Lytics 계정이 필요합니다. |
| Lytics 계정 번호 | Lytics 계정 번호는 웹훅 엔드포인트 URL을 구성하는 데 필요합니다. |
| Lytics API 토큰 | 데이터 매니저 권한이 있는 Lytics REST API 토큰. <br><br> 이는 **계정 설정 콘솔** > **액세스 토큰** > **새 토큰 생성**에서 Lytics 대시보드 내에서 생성할 수 있습니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> 이것은 **설정** > **API 키**에서 Braze 대시보드에서 생성할 수 있습니다. |
| Braze 인스턴스 | 귀하의 [Braze 인스턴스]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints). 이 정보가 확실하지 않은 경우 Braze 온보딩 매니저에게 문의하십시오. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

이 섹션에서는 Lytics 데이터를 Braze로 내보내는 방법을 설명합니다.

### 1단계: 권한 부여 생성

Lytics에서 탐색 모음의 **Authorization** 대시보드 내 **Data** 콘솔로 이동합니다. **Create New Authorization**을 선택하고 **Braze**를 검색하여 선택합니다.

표시되는 **권한 부여 구성** 프롬프트에서 라벨과 설명을 제공하고 REST API 키와 Braze 인스턴스를 입력합니다. 완료되면 **완료**를 선택하십시오.

![][2]{: style="max-width:80%;"}

### 2단계: 새 작업 생성

Lytics에서 탐색 모음의 **작업** 대시보드 내 **데이터** 콘솔로 이동합니다. **Create New Job**을 선택하고 **Braze**를 검색하여 선택합니다.  **작업 유형 선택** 프롬프트에서 **오디언스 내보내기**를 선택합니다.

![][3]{: style="max-width:80%;"}

다음으로, **인증 선택** 옵션에서 인증을 선택하십시오.

![][4]{: style="max-width:80%;"}

### 3단계: 작업을 구성합니다

**작업 구성** 프롬프트 내에서 레이블과 선택적 설명을 제공하십시오. 다음으로, **Braze 외부 사용자 ID 필드** 입력에서 Braze 외부 사용자 ID(`braze_id`)가 포함된 Lytics의 필드를 선택합니다. 다음 단계가 가장 중요합니다. Braze로 내보낼 오디언스를 선택합니다.

![][5]{: style="max-width:80%;"}

마지막으로, **기존 사용자** 체크박스에 대해 선호하는 옵션을 선택하십시오. 이 상자를 선택한 상태로 두면 선택한 Lytics 오디언스에 이미 존재하는 사용자가 추가됩니다. 선택하지 않으면, 사용자는 워크플로우가 시작된 후 오디언스에 들어가거나 나올 때만 Braze로 내보내집니다.

{% alert note %}
이 상자를 선택하면 선택한 오디언스의 모든 기존 사용자가 Braze로 푸시됩니다. 이로 인해 초기 동기화 시 사용자당 오디언스를 기반으로 데이터 포인트가 발생합니다.
{% endalert %}

완료되면 **완료**를 클릭하여 내보내기를 시작하고 저장합니다.

![][6]{: style="max-width:80%;"}

내보내기 작업이 구성된 후, Lytics는 선택한 오디언스를 기본 통합을 통해 Braze로 전송합니다. 다음은 Braze로 전송된 오디언스의 JSON 구조를 보여주는 샘플 오디언스입니다.

```json
{
    "lytics_to_braze_audience": [{
            "external_id": "ABC124ID",
            "lytics_segments": {
                "add": [
                    "lytics_all",
                    "lytics_new"
                ]
            }
        },
        {
            "external_id": "XYZ234ID",
            "lytics_segments": {
                "add": [
                    "lytics_known"
                ],
                "remove": [
                    "lytics_new"
                ]
            }
        }
    ]
}
```

Braze에 아직 존재하지 않는 오디언스 내보내기에 `external_id`가 포함된 경우 새로운 사용자가 Braze에서 생성됩니다. 

## Braze에서 Lytics로 데이터 가져오기

다음 방법을 사용하여 Braze에서 Lytics로 오디언스 데이터를 가져올 수 있습니다:

- [웹훅 사용](#using-webhooks)
- [CSV 파일에서](#from-a-csv-file)

### 웹훅 사용

#### 1단계: Lytics API 토큰 생성

왼쪽 하단의 Lytics 계정 메뉴로 이동하여 계정 이름을 선택한 다음 드롭다운 메뉴에서 **액세스 토큰**을 선택합니다. 다음으로, **API 토큰 생성**을 선택하세요

![][7]{: style="max-width:80%;"}

이름, 선택적 설명 및 토큰 만료 기간을 입력합니다. 다음으로, API 권한에 대한 **데이터 매니저** 범위를 토글하고 **토큰 생성**을 클릭합니다. 토큰을 복사하여 안전한 장소에 보관하십시오.

![][8]{: style="max-width:80%;"}

#### 2단계: Lytics 웹훅 URL을 구성하십시오

Lytics 웹훅 URL은 Braze에서 Lytics API로 메시지를 보내기 위해 Braze에서 사용됩니다. 이 메시지는 Lytics에서 캠페인을 개인화하거나 Lytics 고객 프로필을 보강하는 데 사용할 수 있습니다. Lytics 웹훅 URL 내에 다음 두 매개변수를 추가해야 합니다:

- Lytics 계정 번호
- Lytics API 토큰

웹훅 URL을 다음과 같이 구성하십시오:

```
https://api.lytics.io/c/<ACCOUNT-NUMBER>/braze_users?key=<LYTICS-API-TOKEN>
```

`<ACCOUNT-NUMBER>`를 계정 번호로 바꾸고 `<LYTICS-API-TOKEN>`을 Lytics API 토큰으로 바꿉니다.

#### 3단계: Braze에서 웹훅 생성 

Braze에서 새 [웹훅 캠페인]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)을(를) 만드세요. **Webhook URL** 필드에 Lytics 웹훅 URL을 추가하세요.

요청 유형(HTTP `POST` 메서드)을 정의하고 나머지 웹훅 세부 정보를 구성한 후, 웹훅을 테스트 및 배포할 준비가 됩니다. 다음은 Braze에서 웹훅을 구성한 후 POST 요청의 샘플 본문입니다:

```json
{
  "city": "AnyTown",
  "country": "United States",
  "first_name": "John",
  "gender": "male",
  "language": "English",
  "last_name": "Smith",
  "date_of_birth": "19820101",
  "phone_number": "5551231234",
  "time_zone": "GMT+7",
  "twitter_handle": "johnsmith",
  "email": "john.smith@email.com",
  "braze_id": "xxxxxx" 
}
```

### CSV 파일에서

이 섹션에서는 세그먼트에서 Lytics로 Braze 사용자 데이터를 가져오는 방법을 설명합니다.

#### 1단계: 권한 부여 생성

Lytics에서 탐색 모음의 **Authorization** 대시보드 내 **Data** 콘솔로 이동합니다. **Create New Authorization**을 선택하고 **커스텀 Integrations**을 검색하여 선택합니다.

비즈니스 및 보안 요구 사항에 따라 선호하는 SFTP 인증 유형을 선택하십시오. 다음 권한 부여 유형은 SFTP를 통해 Lytics로 파일 가져오기를 지원합니다.

- 클라이언트 SFTP 서버 권한 부여
- PGP 비공개 키를 사용하는 클라이언트 SFTP 서버 권한 부여
- Lytics 관리 SFTP 서버 권한 부여

공개 키 SFTP 권한 부여는 SFTP 내보내기 전용입니다.

![][9]{: style="max-width:80%;"}

표시되는 **권한 부여 구성** 프롬프트에서 라벨과 설명을 제공하고 나머지 구성 요구 사항을 완료합니다. 완료되면 **완료**를 클릭합니다.

#### 2단계: 세그먼트 데이터를 CSV로 내보내기

Braze에서 **오디언스** > **세그먼트**로 이동합니다. 내보내려는 세그먼트를 찾은 다음, <i class="fas fa-gear" aria-label="설정"></i>을 선택하고 **CSV 내보내기 사용자 데이터**를 선택합니다. 세그먼트에서 최대 500,000명의 사용자를 내보낼 수 있습니다. 자세한 내용은 [CSV로 세그먼트 데이터 내보내기]({{site.baseurl}}/user_guide/data/export_braze_data/segment_data_to_csv/)를 참조하세요.

#### 3단계: CSV 가져오기 작업 구성

Lytics에서 탐색 모음의 **작업** 대시보드 내 **데이터** 콘솔로 이동합니다. **Create New Job**을 선택하고 **커스텀 Integrations**을 검색하여 선택합니다.

다음으로, 작업 유형을 선택하십시오. Lytics로 Braze CSV 파일을 가져오려면 작업 유형으로 **CSV 가져오기**를 선택합니다.

![][10]{: style="max-width:80%;"}

마지막으로, 작업에 대한 라벨과 선택적 설명을 입력하고 필요한 다른 세부 정보를 구성합니다. **완료**를 클릭하여 시작하고 작업을 저장합니다.


[1]: https://www.lytics.com/
[2]: {% image_buster /assets/img/lytics/braze_authorization.png %}
[3]: {% image_buster /assets/img/lytics/braze_jobtype.png %}
[4]: {% image_buster /assets/img/lytics/braze_jobauth.png %}
[5]: {% image_buster /assets/img/lytics/braze_job.png %}
[6]: {% image_buster /assets/img/lytics/braze_backfill.png %}
[7]: {% image_buster /assets/img/lytics/create_token.png %}
[8]: {% image_buster /assets/img/lytics/data_manager.png %}
[9]: {% image_buster /assets/img/lytics/authorization_method.png %}
[10]: {% image_buster /assets/img/lytics/configure_job.png %}





