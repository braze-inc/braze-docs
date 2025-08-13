---
nav_title: Fivetran
article_title: Fivetran
alias: /partners/fivetran/
description: "이 참조 문서에서는 바로 조회 가능한 데이터를 클라우드 웨어하우스에 제공하여 데이터 기반 의사 결정을 지원하는 워크플로 자동화 도구인 Braze와 Fivetran의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner
tool: Currents

---

# Fivetran

> [Fivetran](https://fivetran.com/)은 분석가 중심의 제품과 완전 관리형 파이프라인을 통해 바로 쿼리 가능한 데이터를 클라우드 웨어하우스에 제공함으로써 데이터에 기반한 의사 결정을 내릴 수 있도록 지원하는 세계적으로 인정받는 브랜드입니다.

Braze와 Fivetran의 통합을 통해 사용자는 모든 애플리케이션과 데이터베이스를 중앙 데이터 웨어하우스에 연결하여 유지 관리가 필요 없는 파이프라인을 생성하여 Braze 데이터를 수집하고 분석할 수 있습니다. 중앙 데이터 웨어하우스에 데이터가 수집되면 데이터 팀은 선호하는 비즈니스 인텔리전스 툴을 사용하여 Braze 데이터를 효과적으로 탐색할 수 있습니다. 

## 필수 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Fivetran 계정 | 이 파트너십을 이용하려면 [Fivetran](https://fivetran.com/login?next=%2Fdashboard) 계정이 필요합니다. |
| Braze REST API 키 | 다음 권한이 있는 Braze REST API 키입니다:<br>- users.export.ids<br>- users.export.segment<br>- email.unsubscribe<br>- email.hard_bounces<br>- messages.schedule_roadcasts<br>- campaigns.list<br>- campaigns.details<br>- canvas.list<br>- canvas.details<br>- segments.list<br>- segments.details<br>- purchases.product_list<br>- events.list<br>- feed.list<br>- feed.details<br>- templates.email.info<br>- templates.email.list<br>- subscription.status.get<br>- subscription.groups.get <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트  | REST 엔드포인트 URL. 엔드포인트는 [인스턴스의 Braze URL에][1] 따라 달라집니다. |
| Braze 커런츠 | [Braze 커런츠](https://www.braze.com/product/data-agility-management/currents/)를 Amazon S3 또는 Google Cloud Storage에 연결해야 합니다. |
| Amazon S3 또는 Google 클라우드 스토리지 | 이 통합을 사용하려면 하나의 Amazon S3 또는 Google Cloud Storage에 액세스할 수 있어야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## 통합

다음 커런츠 통합은 [Amazon S3와](#setting-up-braze-currents-for-s3) [Google 클라우드 스토리지](#setting-up-braze-currents-for-google-cloud-storage) 모두에 대해 지원됩니다.

### S3용 Braze 커런츠 설정

#### 1단계: 외부 ID 찾기 {#step-one}

[Fivetran 대시보드에서](https://fivetran.com/dashboard) **\+ 커넥터를** 선택한 다음 **Braze** 커넥터를 선택하여 설정 양식을 실행합니다. 다음으로 **Amazon S3를** 선택합니다. 여기에 제공된 외부 ID는 Fivetran이 S3 버킷에 액세스할 수 있도록 허용하는 데 필요합니다. 

![Fivetran에서 Braze 커넥터 양식을 설정합니다. 이 단계에 필요한 외부 ID 필드는 페이지 중앙의 밝은 회색 상자에 있습니다.]({% image_buster /assets/img/fivetran_braze_setupform_as3.png %})

#### 2단계: 지정된 S3 버킷에 대한 액세스 권한을 Fivetran에 부여

##### IAM 정책 만들기

[Amazon IAM 콘솔을](https://console.aws.amazon.com/iam/home#home) 열고 **정책 > 정책 만들기로** 이동합니다.

![정책 목록이 있는 Amazon IAM 콘솔]({% image_buster /assets/img/fivetran_as3_iam.png %})

그런 다음 **JSON** 탭을 열고 다음 정책을 붙여넣습니다. `{your-bucket-name}`을 S3 버킷의 이름으로 바꿔야 합니다.

{% raw %}
```json
{
"Version": "2012-10-17",
"Statement": [
    {
      "Effect": "Allow",
      "Action": [
"s3:Get*",
"s3:List*"
      ],
      "Resource": "arn:aws:s3:::{your-bucket-name}/*"
    },
    {
      "Effect": "Allow",
      "Action": [
"s3:Get*",
"s3:List*"
      ],
      "Resource": "arn:aws:s3:::{your-bucket-name}"
    }
  ]
}
```
{% endraw %}

마지막으로 **정책 검토를** 선택하고 정책의 고유한 이름과 설명을 입력합니다. **정책 생성을** 선택하여 정책을 작성합니다. 

![정책의 이름을 지정하고 설명을 입력하는 필드입니다.]({% image_buster /assets/img/fivetran_iam_policy_meta.png %})

##### IAM 역할 만들기 {#step-two}

AWS에서 **역할**로 이동한 다음, **새 역할 생성**을 선택합니다.

![새 역할을 만들 수 있는 버튼이 있는 '역할' 페이지.]({% image_buster /assets/img/fivetran_iam_new_role.png %})

**다른 AWS 계정**을 선택하고 Fivetran 계정 ID `834469178297`을 제공합니다. **외부 ID 필요** 확인란을 선택해야 합니다. 여기에서 1단계에서 찾은 외부 ID를 입력합니다.

!['계정 ID'를 입력하는 필드, 외부 ID를 요구하는 확인란, '외부 ID'를 입력하는 빈 텍스트 상자입니다.]({% image_buster /assets/img/fivetran_another_aws_account.png %})

다음으로 **다음을 선택합니다: 권한**을 클릭하여 방금 생성한 정책을 선택합니다.

![정책 목록]({% image_buster /assets/img/fivetran_as3_select_policy.png %})

**다음을 선택합니다: ** 을 검토하고 새 역할의 이름(예: Fivetran)을 지정한 다음 **역할 만들기를** 선택합니다. 역할이 생성된 후 해당 역할을 선택하고 표시되는 역할 ARN을 확인합니다.

![역할에 나열된 Amazon S3 ARN.]({% image_buster /assets/img/fivetran_iam_role_arn.png %})

{% alert note %}
Fivetran에 지정하는 역할 ARN에 대한 권한을 지정할 수 있습니다. 이 역할에 선택적 권한을 부여하면 Fivetran이 볼 수 있는 권한이 있는 항목만 동기화할 수 있습니다.
{% endalert %}

#### 3단계: Fivetran 커넥터 완성

Fivetran에서 **\+ 커넥터를** 선택한 다음 **Braze** 커넥터를 선택하여 설정 양식을 실행합니다. 양식 내에서 주어진 필드를 적절한 값으로 채웁니다:
- `Destination schema`: 고유한 스키마 이름입니다.
- `API URL`: Braze REST API 엔드포인트.
- `API Key`: Braze REST API 키입니다. 
- `External ID`: 커런츠 설정 지침의 [2단계](#step-two)에서 설정한 외부 ID. 이 ID는 고정된 값입니다.
- `Bucket`: **파트너 연동** > **데이터 내보내기** > 현재 이름으로 이동하여 Braze 계정에서 찾을 수 있습니다.
- `Role ARN`: 역할 ARN은 현재 설정 지침의 [1단계](#step-one)에서 찾을 수 있습니다.

{% alert important %}
**클라우드 스토리지로** **Amazon S3가** 선택되어 있는지 확인합니다.
{% endalert %}

마지막으로 **저장 및 테스트를** 선택하면 Fivetran이 Braze 계정의 데이터와 동기화하여 나머지 작업을 수행합니다!

### Google 클라우드 스토리지용 Braze Currents 설정하기

#### 1단계: Google Cloud Storage에서 Fivetran 이메일 검색 {#step-one2}

[Fivetran 대시보드에서](https://fivetran.com/dashboard) **\+ 커넥터를** 선택한 다음 **Braze** 커넥터를 선택하여 설정 양식을 실행합니다. 다음으로 **Google 클라우드 스토리지를** 선택합니다. 표시되는 이메일 주소를 메모해 두세요.

![Fivetran에서 Braze 커넥터 양식을 설정합니다. 이 단계에 필요한 이메일 필드는 페이지 중앙의 밝은 회색 상자에 있습니다.]({% image_buster /assets/img/fivetran_braze_setupform_gcs.png %})

#### 2단계: 버킷 액세스 권한 부여

[Google 스토리지 콘솔로](https://console.cloud.google.com/storage/browser) 이동하여 Braze Currents를 구성한 버킷을 선택한 다음 **버킷 권한 편집을** 선택합니다.

![Google 스토리지 콘솔에서 사용 가능한 버킷입니다. 버킷을 찾아 세로 점 3개 아이콘을 선택하면 버킷 권한을 편집할 수 있는 드롭다운이 열립니다.]({% image_buster /assets/img/fivetran_edit_bucket_permissions_gcs.png %})

그런 다음, [1단계](#step-one2)의 이메일을 구성원으로 추가하여 해당 이메일에 `Storage Object Viewer` 액세스 권한을 부여합니다. 버킷 이름을 메모해 두세요. 다음 단계에서 Fivetran을 구성할 때 필요하기 때문입니다.

![권한이 있는 버킷]({% image_buster /assets/img/fivetran_add_members_gcs.png %})

#### 3단계: Fivetran 커넥터 완성

Fivetran에서 **\+ 커넥터를** 선택한 다음 **Braze** 커넥터를 선택하여 설정 양식을 실행합니다. 양식 내에서 주어진 필드를 적절한 값으로 채웁니다:
- `Destination schema`: 고유한 스키마 이름입니다.
- `API URL`: Braze REST API 엔드포인트.
- `API Key`: Braze REST API 키입니다. 
- `Bucket Name`: **파트너 연동** > **데이터 내보내기** > 현재 이름으로 이동하여 Braze 계정에서 찾을 수 있습니다.
- `Folder`: **파트너 연동** > **데이터 내보내기** > 현재 이름으로 이동하여 Braze 계정에서 찾을 수 있습니다.

{% alert important %}
**Google Cloud Storage**가 **클라우드 스토리지** 선택 항목으로 선택되어 있는지 확인합니다.
{% endalert %}

마지막으로 **저장 및 테스트를** 선택하면 Fivetran이 Braze 계정의 데이터와 동기화하여 나머지 작업을 수행합니다!

[1]: {{site.baseurl}}/api/basics/#api-definitions