---
nav_title: Amazon S3
article_title: Amazon S3
alias: /partners/amazon_s3/
description: "이 참조 문서에서는 Amazon Web Services에서 제공하는 확장성이 뛰어난 스토리지 시스템인 Braze와 Amazon S3의 파트너십에 대해 간략하게 설명합니다."
page_type: partner
search_tag: Partner

---

# Amazon S3

> [Amazon S3는](https://aws.amazon.com/s3/) Amazon Web Services에서 제공하는 확장성이 뛰어난 스토리지 시스템입니다.

Braze와 Amazon S3 통합을 통해 [커런츠]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/)를 활용하여 Braze 데이터를 S3 인스턴스로 전송하고, 다른 플랫폼, 툴 및 위치에 데이터를 연결할 때까지 데이터를 저장할 수 있습니다. 대시보드 데이터 내보내기를 통해 통합할 수도 있습니다. 이 페이지의 지침에 따라 AWS S3 통합을 시작합니다.

## 필수 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Amazon S3 계정 | 이 파트너십을 이용하려면 Amazon S3 계정이 필요합니다. |
| 전용 S3 버킷 | Amazon S3와 통합하기 전에 앱에 대한 S3 버킷을 만들어야 합니다.<br><br>이미 S3 버킷이 있는 경우에도 여전히 권한을 제한할 수 있도록 Braze 전용 버킷을 새로 생성하는 것이 좋습니다. 새 버킷을 만드는 방법은 다음 안내를 참조하세요. |
| 커런츠 | Amazon S3로 데이터를 다시 내보내려면 계정에 [Braze Currents가]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) 설정되어 있어야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 새 S3 버킷 만들기

앱용 버킷을 생성하려면 [Amazon S3 콘솔](https://console.aws.amazon.com/s3/)을 열고 **로그인** 또는 **AWS에서 계정 생성** 지침을 따르세요. 로그인한 후 **스토리지 및 콘텐츠 전송** 카테고리에서 **S3**를 선택합니다. 다음 화면에서 **버킷 생성**을 선택합니다. 버킷을 생성하고 지역을 선택하라는 메시지가 표시됩니다.

## 통합

Braze는 Amazon S3와 두 가지 통합 전략을 가지고 있습니다. 하나는 [Braze Currents용이고]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) 다른 하나는 모든 대시보드 데이터 내보내기(CSV 내보내기, 참여 보고서 등)를 위한 것입니다. 두 통합 모두 서로 다른 두 가지 인증/권한 부여 방법을 지원합니다.

- [AWS 비밀 액세스 키 방법](#aws-secret-key-auth-method)
- [AWS 역할 ARN 방법](#aws-role-arn-auth-method)

## AWS 비밀 키 인증 방법

이 인증 방법은 비밀 키와 액세스 키 ID를 생성하여 Braze를 AWS 계정에서 사용자로 인증하여 버킷에 데이터를 쓸 수 있도록 합니다.

### 1단계: 사용자 만들기 {#secret-key-1}

액세스 키 ID와 비밀 액세스 키를 검색하려면 [AWS에서 IAM 사용자 및 관리자 그룹을 생성](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)해야 합니다.

### 2단계: 자격 증명 가져오기 {#secret-key-2}

새 사용자를 생성한 후 **사용자 보안 자격 증명 표시**를 클릭하여 액세스 키 ID와 비밀 액세스 키를 공개합니다. 다음으로, 나중에 Braze 대시보드에 입력해야 하므로 이 자격 증명을 어딘가에 메모하거나 **자격 증명 다운로드** 버튼을 클릭합니다.

![][11]

### 3단계: 정책 만들기 {#secret-key-3}

**정책 > 시작하기 > 정책 만들기로** 이동하여 사용자에 대한 권한을 추가합니다. 다음으로, **나만의 정책 생성**을 선택합니다. 이렇게 하면 제한된 권한이 부여되므로 Braze는 지정된 버킷에만 액세스할 수 있습니다. 

![][12]

{% alert note %}
'커런츠'와 '대시보드 데이터 내보내기'에는 서로 다른 정책이 필요합니다.
{% endalert %}

원하는 정책 이름을 지정하고 **정책 문서** 섹션에 다음 코드 스니펫을 입력합니다. `INSERTBUCKETNAME`을 버킷 이름으로 바꾸어야 합니다. 이러한 권한이 없으면 통합은 자격 증명 확인에 실패하고 생성되지 않습니다.

{% tabs %}
{% tab Braze 커런츠 %}
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```
{% endtab %}
{% tab 대시보드 데이터 내보내기 %}
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME*", "arn:aws:s3:::INSERTBUCKETNAME/", "arn:aws:s3:::INSERTBUCKETNAME"]
        }
    ]
}
```
{% endtab %}
{% endtabs %}

### 4단계: 정책 첨부 {#secret-key-4}

새 정책을 만든 후 **사용자로** 이동하여 특정 사용자를 클릭합니다. **권한** 탭에서 **정책 첨부하기를** 클릭하고 새로 만든 정책을 선택합니다. 이제 AWS 자격 증명을 Braze 계정에 연결할 준비가 되었습니다.

![][13]

### 5단계: AWS에 Braze 연결 {#secret-key-5}

{% tabs %}
{% tab Braze 커런츠 %}

Braze에서 **파트너 통합** > **데이터 내보내기**로 이동합니다.

{% alert note %}
[이전 탐색]({{site.baseurl}}/navigation)을 사용하는 경우 **통합**에서 **커런츠**를 찾을 수 있습니다.
{% endalert %}

다음으로, **커런츠 생성**을 클릭하고 **Amazon S3 데이터 내보내기**를 선택합니다.

현재 이름을 지정한 다음 **자격 증명** 섹션에서 **AWS 비밀 액세스 키** 라디오 버튼이 선택되어 있는지 확인한 다음 지정된 필드에 S3 액세스 ID, AWS 비밀 액세스 키, AWS S3 버킷 이름을 입력합니다.

![]({{site.baseurl}}/assets/img/currents-s3-example.png)

{% alert warning %}
AWS 액세스 키 ID와 비밀 액세스 키를 최신 상태로 유지하세요. 커넥터의 자격 증명이 만료되면 커넥터는 이벤트 전송을 중지합니다. **48시간** 넘게 지속되면 커넥터의 이벤트가 삭제되고 데이터가 영구적으로 손실됩니다.
{% endalert %}

필요에 따라 다음과 같은 사용자 지정을 추가할 수도 있습니다:

- **폴더 경로:** 기본값은 `currents` 입니다. 이 폴더가 존재하지 않으면 Braze가 자동으로 폴더를 생성합니다. 
- **서버 측, 저장 시 AES-256 암호화:** 기본값은 꺼짐이며 `x-amz-server-side-encryption` 헤더를 포함합니다.

계속하려면 **커런츠 시작**을 클릭합니다.

알림을 통해 자격 증명이 성공적으로 인증되었는지 여부를 알립니다. 이제 AWS S3가 Braze Currents를 위해 설정되어야 합니다.

{% endtab %}
{% tab 대시보드 데이터 내보내기 %}

Braze에서 **파트너 통합** > **기술 파트너로** 이동하여 **Amazon S3를** 클릭합니다.

{% alert note %}
[이전 탐색]({{site.baseurl}}/navigation)을 사용하는 경우 **통합**에서 **기술 파트너**를 찾을 수 있습니다.
{% endalert %}

AWS 자격증명 페이지에서 **AWS 비밀 액세스 키** 라디오 버튼이 선택되어 있는지 확인한 다음, 지정된 필드에 AWS 액세스 ID, AWS 비밀 액세스 키, AWS S3 버킷 이름을 입력합니다. 비밀 키를 입력할 때 먼저 **자격 증명 테스트**를 클릭하여 자격 증명이 작동하는지 확인한 다음, 성공하면 **저장**을 클릭합니다.

![]({{site.baseurl}}/assets/img/s3_tech_partners.png)

{% alert tip %}
언제든지 사용자로 이동하여 AWS 콘솔의 **보안 자격 증명** 탭에서 **액세스 키 생성**을 클릭해 새 자격 증명을 검색할 수 있습니다.
{% endalert %}

알림을 통해 자격 증명이 성공적으로 인증되었는지 여부를 알립니다. 이제 AWS S3가 Braze 계정에 통합되었습니다.

{% endtab %}
{% endtabs %}

## AWS 역할 ARN 인증 방법

이 인증 방법은 버킷에 데이터를 쓰기 위해 생성한 역할의 멤버로 인증할 수 있는 역할 Amazon 리소스 이름(ARN)을 생성하여 Braze의 Amazon 계정을 인증합니다.

### 1단계: 정책 만들기 {#role-arn-1}

시작하려면 계정 관리자로 AWS 관리 콘솔에 로그인합니다. AWS 콘솔의 IAM 섹션으로 이동하고 탐색 표시줄에서 **정책**을 클릭한 다음, **정책 생성**을 클릭합니다.

![]({{site.baseurl}}/assets/img/create_policy_1_list.png)

{% alert note %}
'커런츠'와 '대시보드 데이터 내보내기'에는 서로 다른 정책이 필요합니다.
{% endalert %}

**JSON** 탭을 열고 **정책 문서** 섹션에 다음 코드 스니펫을 입력합니다. `INSERTBUCKETNAME`을 버킷 이름으로 바꾸어야 합니다. 완료하면 **정책 검토**를 클릭합니다.

{% tabs %}
{% tab Braze 커런츠 %}

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```

{% endtab %}
{% tab 대시보드 데이터 내보내기 %}

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject","s3:DeleteObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```

{% endtab %}
{% endtabs %}

그런 다음, 정책의 이름 및 설명을 제공하고 **정책 생성**을 선택합니다.

![]({{site.baseurl}}/assets/img/create_policy_3_name.png)

![]({{site.baseurl}}/assets/img/create_policy_4_created.png)

### 2단계: 역할 생성 {#role-arn-2}

콘솔의 동일한 IAM 섹션에서 **역할 > 역할 생성**을 클릭합니다.

![]({{site.baseurl}}/assets/img/create_role_1_list.png)

Braze 계정에서 Braze 계정 ID와 외부 ID를 검색합니다.
- **커런츠**: Braze에서 **파트너 통합** > **데이터 내보내기**로 이동합니다. 다음으로, **커런츠 생성**을 클릭하고 **Amazon S3 데이터 내보내기**를 선택합니다. 여기에서 역할을 만드는 데 필요한 식별자를 찾을 수 있습니다.
- **대시보드 데이터 내보내기**: Braze에서 **파트너 통합** > **기술 파트너로** 이동하여 **Amazon S3를** 클릭합니다. 여기에서 역할을 만드는 데 필요한 식별자를 찾을 수 있습니다.

{% alert note %}
[이전 탐색을]({{site.baseurl}}/navigation) 사용하는 경우 이러한 페이지는 다른 위치에 있습니다:<br>- **전류는** **통합** > **전류** 아래에 있습니다. <br>- **기술 파트너**는 **통합** 아래에 있음
{% endalert %}

AWS 콘솔로 돌아와서 신뢰할 수 있는 엔터티 선택기 유형으로 **다른 AWS 계정**을 선택합니다. Braze 계정 ID를 입력하고 **외부 ID 필요** 확인란을 선택한 다음 Braze 외부 ID를 입력합니다. 완료되면 **다음**을 클릭합니다.

![S3 "역할 만들기" 페이지. 이 페이지에는 역할 이름, 역할 설명, 신뢰할 수 있는 엔터티, 정책 및 권한 경계에 대한 필드가 있습니다.]({{site.baseurl}}/assets/img/create_role_2_another.png)

### 3단계: 정책 첨부 {#role-arn-3}

그런 다음 앞서 만든 정책을 역할에 첨부합니다. 검색창에서 정책을 검색하고 정책 옆에 체크 표시를 하여 첨부합니다. 완료되면 **다음**을 클릭합니다.

![역할 ARN]({{site.baseurl}}/assets/img/create_role_3_attach.png)

역할에 이름과 설명을 입력한 다음 **역할 만들기**를 클릭합니다.

![역할 ARN]({{site.baseurl}}/assets/img/create_role_4_name.png)

이제 목록에 새로 만든 역할이 표시됩니다.

### 4단계: Braze AWS에 링크 {#role-arn-4}

AWS 콘솔의 목록에서 새로 생성한 역할을 찾습니다. 이름을 클릭하면 해당 역할의 세부 정보가 열립니다.

![]({{site.baseurl}}/assets/img/create_role_5_created.png)

역할 요약 페이지 상단에 있는 **역할 ARN**을 기록합니다.

![]({{site.baseurl}}/assets/img/create_role_6_summary.png)

Braze 계정으로 돌아가서 제공된 필드에 역할 ARN을 복사합니다.

{% tabs %}
{% tab Braze 커런츠 %}

Braze에서 **통합** 아래의 **커런츠** 페이지로 이동합니다. 다음으로 **현재 생성을** 클릭하고 **Amazon S3 데이터 내보내기를** 선택합니다.

![]({{site.baseurl}}/assets/img/currents-role-arn.png)

커런츠에 이름을 지정합니다. 그런 다음 **자격증명** 섹션에서 **AWS 역할 ARN** 라디오 버튼이 선택되어 있는지 확인한 다음 지정된 필드에 역할 ARN과 AWS S3 버킷 이름을 입력합니다.

필요에 따라 다음과 같은 사용자 지정을 추가할 수도 있습니다:

- 폴더 경로(기본값: `currents`)
- 서버 측, 저장 시 AES-256 암호화(기본값: 꺼짐) - `x-amz-server-side-encryption` 헤더 포함

계속하려면 **커런츠 시작**을 클릭합니다.

알림을 통해 자격 증명이 성공적으로 인증되었는지 여부를 알립니다. 이제 AWS S3가 Braze Currents를 위해 설정되어야 합니다.

{% alert important %}
'S3 자격 증명이 유효하지 않음' 오류가 표시되는 경우 AWS에서 역할을 생성한 후 너무 빨리 통합했기 때문일 수 있습니다. 잠시 기다렸다가 다시 시도하세요.
{% endalert %}

{% endtab %}
{% tab 대시보드 데이터 내보내기 %}

Braze에서 **통합** 아래의 **기술 파트너** 페이지로 이동하여 **Amazon S3를** 클릭합니다.

![]({{site.baseurl}}/assets/img/data-export-role-arn.png)

**AWS 자격 증명** 페이지에서 **AWS 역할 ARN** 라디오 버튼이 선택되어 있는지 확인한 다음 지정된 필드에 역할 ARN과 AWS S3 버킷 이름을 입력합니다. 먼저 **자격 증명 테스트**를 클릭하여 자격 증명이 제대로 작동하는지 확인한 다음, 성공하면 **저장**을 클릭합니다.

{% alert tip %}
언제든지 사용자로 이동하여 AWS 콘솔의 **보안 자격 증명** 탭에서 **액세스 키 생성**을 클릭해 새 자격 증명을 검색할 수 있습니다.
{% endalert %}

알림을 통해 자격 증명이 성공적으로 인증되었는지 여부를 알립니다. 이제 AWS S3가 Braze 계정에 통합되었습니다.

{% endtab %}
{% endtabs %}

## 내보내기 동작

클라우드 데이터 스토리지 솔루션을 통합하고 API, 대시보드 보고서 또는 CSV 보고서를 내보내려고 하는 사용자는 다음을 경험합니다.

- 모든 API 내보내기는 응답 본문에 다운로드 URL을 반환하지 않으며 데이터 스토리지를 통해 검색해야 합니다.
- 모든 대시보드 보고서와 CSV 보고서는 다운로드할 수 있도록 사용자 이메일로 전송되며(스토리지 권한이 필요하지 않음) 데이터 스토리지에 백업됩니다. 

## 여러 커넥터

S3 버킷으로 전송할 커런츠 커넥터를 두 개 이상 만들려는 경우 동일한 자격 증명을 사용할 수 있지만 각각에 대해 다른 폴더 경로를 지정해야 합니다. 동일한 워크스페이스에서 생성하거나 여러 워크스페이스에서 분할하여 생성할 수 있습니다. 각 통합에 대해 단일 정책을 생성하거나 두 통합을 모두 포함하는 하나의 정책을 생성할 수도 있습니다. 

커런츠와 데이터 내보내기 모두에 동일한 S3 버킷을 사용하려는 경우, 각 통합에는 서로 다른 권한이 필요하므로 두 개의 정책을 별도로 생성해야 합니다.


[11]: {% image_buster /assets/img_archive/S3_Credentials.png %}
[12]: {% image_buster /assets/img_archive/S3_CreatePolicy.png %}
[13]: {% image_buster /assets/img_archive/S3_AttachPolicy.png %}
