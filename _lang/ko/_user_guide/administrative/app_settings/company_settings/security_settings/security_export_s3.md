---
nav_title: S3로 보안 이벤트 내보내기
article_title: S3로 보안 설정 내보내기
page_order: 1
page_type: reference
description: "이 참조 문서에서는 매일 자정(UTC)에 보안 이벤트를 Amazon S3로 자동으로 내보내는 방법에 대해 설명합니다."
---

# Amazon S3를 사용한 보안 이벤트 내보내기

> 매일 자정(UTC)에 실행되는 작업을 통해 보안 이벤트를 클라우드 스토리지 제공업체인 Amazon S3로 자동으로 내보낼 수 있습니다. 설정 후에는 대시보드에서 보안 이벤트를 수동으로 내보낼 필요가 없습니다. 이 작업은 지난 24시간 동안의 보안 이벤트를 CSV 형식으로 구성된 S3 스토리지로 내보냅니다. CSV 파일은 수동으로 내보낸 보고서와 동일한 구조를 갖습니다.

Braze는 Amazon S3 내보내기를 설정하기 위해 두 가지 다른 S3 인증 및 권한 부여 방법을 지원합니다:

- AWS 비밀 액세스 키 방법
- AWS 역할 ARN 방법

## AWS 비밀 액세스 키 방법

이 방법은 비밀 키와 액세스 키 ID를 생성하여 Braze가 버킷에 데이터를 쓰기 위해 AWS 계정에서 사용자로 인증할 수 있도록 합니다.

### 1단계: 인앱 메시지 사용자 만들기

비밀 액세스 키와 액세스 키 ID를 검색하려면 [AWS 계정 설정하기의](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started-account-iam.html#create-an-admin) 안내에 따라 인앱 메시지 사용자를 만들어야 합니다.

### 2단계: 자격 증명 받기

1. 새 사용자를 만든 후 액세스 키를 생성하고 액세스 키 ID와 비밀 액세스 키를 다운로드합니다.

!"라는 역할에 대한 요약 페이지입니다.]({% image_buster /assets/img/security_export/credentials1.png %})

{: start="2"}
2\. 나중에 Braze에 입력해야 하므로 이러한 자격 증명을 어딘가에 메모해 두거나 자격 증명 파일을 다운로드하세요.

액세스 키와 비밀 액세스 키가 포함된 필드입니다.]({% image_buster /assets/img/security_export/retrieve_access_keys.png %})

### 3단계: 정책 만들기

1. **IAM** > **정책** > **정책 만들기로** 이동하여 사용자에 대한 권한을 추가합니다. 
2. 나만의 **정책 만들기를** 선택하면 Braze가 지정된 버킷에만 액세스할 수 있도록 제한된 권한을 부여할 수 있습니다.
3. 원하는 정책 이름을 지정합니다.
4. **정책 설명서** 섹션에 다음 코드 스니펫을 입력합니다. "INSERTBUCKETNAME"을 버킷 이름으로 바꿔야 합니다. 이러한 권한이 없으면 통합이 자격 증명 검사에 실패하여 생성되지 않습니다.

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

### 4단계: 정책 첨부

1. 새 정책을 만든 후 **사용자로** 이동하여 특정 사용자를 선택합니다. 
2. **권한** 탭에서 **권한 추가를** 선택하고 정책을 직접 첨부한 다음 해당 정책을 선택합니다. 

이제 AWS 자격 증명을 Braze 계정에 연결할 준비가 되었습니다!

### 5단계: Braze를 AWS에 연결하기

1. Braze에서 **설정** > **회사 설정** > **관리자 설정** > **보안 설정으로** 이동하여 **보안 이벤트 다운로드** 섹션으로 스크롤합니다.
2. **클라우드 스토리지로 내보내기** 아래에서 **AWS S3로** 내보내기를 토글하고 S3 내보내기를 인에이블먼트하는 **AWS 비밀 액세스 키를** 선택합니다. 
3. 다음을 입력합니다:
- AWS 액세스 키 ID
- AWS 비밀 액세스 키
    - 이 키를 입력할 때는 먼저 자격 증명 **테스트를** 선택하여 자격 증명이 제대로 작동하는지 확인하세요.
- AWS 버킷 이름 

!"보안 이벤트 다운로드" 페이지에 Braze 계정과 Braze 외부 ID가 채워져 있습니다.]({% image_buster /assets/img/security_export/security_event_download1.png %})

{: start="4"}
4\. **변경 사항 저장을** 선택합니다. 

!"["변경 사항 저장" 버튼.]({% image_buster /assets/img/security_export/save_changes_button.png %}){: style="max-width:50%;"}

AWS S3를 Braze 계정에 통합했습니다!

## AWS 역할 ARN 방법

AWS 역할 ARN 메서드는 Braze Amazon 계정이 해당 역할의 멤버로 인증할 수 있는 역할 ARN(Amazon 리소스 이름)을 생성합니다.

### 1단계: 정책 만들기

1. AWS 관리 콘솔에 계정 매니저로 로그인합니다. 
2. AWS 콘솔에서 **IAM** 섹션 > **정책으로** 이동한 다음 **정책 만들기를** 선택합니다.

정책 목록과 '정책 만들기' 버튼이 있는 페이지입니다.]({% image_buster /assets/img/security_export/policies.png %})

{: start="3"}
3\. **JSON** 탭을 열고 **정책 설명서** 섹션에 다음 코드 스니펫을 입력합니다. `INSERTBUCKETNAME` 을 버킷 이름으로 바꾸세요. 

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

{: start="4"}
4\. 정책을 검토한 후 **다음을** 선택합니다.

정책을 검토하고 선택적으로 권한을 추가할 수 있는 페이지입니다.]({% image_buster /assets/img/security_export/specify_permissions.png %})

{: start="5"}
5\. 정책의 이름과 설명을 입력한 다음 **정책 만들기를** 선택합니다.

정책을 검토하고 작성할 수 있는 페이지입니다.]({% image_buster /assets/img/security_export/review_and_create.png %})

### 2단계: 역할 만들기

1. Braze에서 **설정** > **회사 설정** > **관리자 설정** > **보안 설정으로** 이동하여 **보안 이벤트 다운로드** 섹션으로 스크롤합니다. 
2. **AWS 역할 ARN을** 선택합니다. 
3. 역할을 만드는 데 필요한 식별자, Braze 계정 ID, Braze 외부 ID를 메모해 두세요.

!"보안 이벤트 다운로드" 페이지에 Braze 계정과 Braze 외부 ID가 채워져 있습니다.]({% image_buster /assets/img/security_export/security_event_download2.png %})

4. AWS 콘솔에서 **IAM** 섹션 > **역할** > **역할 만들기로** 이동합니다. 
5. 신뢰할 수 있는 엔터티 선택기 유형으로 **다른 AWS 계정을** 선택합니다. 
6. Braze 계정 ID를 입력하고 **외부 ID 필요** 확인란을 선택한 다음 Braze 외부 ID를 입력합니다. 
7. 완료되면 **다음을** 선택합니다.

신뢰할 수 있는 엔터티 유형을 선택하고 AWS 계정에 대한 정보를 제공하는 옵션이 있는 페이지입니다.]({% image_buster /assets/img/security_export/select_trusted_entity.png %})

### 3단계: 정책 첨부

1. 검색창에서 이전에 만든 정책을 검색한 다음 정책 옆에 체크 표시를 하여 첨부합니다. 
2. **다음을** 선택합니다.

유형 및 설명에 대한 열이 있는 정책 목록입니다.]({% image_buster /assets/img/security_export/add_permissions.png %})

{: start="3"}
3\. 역할에 이름과 설명을 입력하고 **역할 만들기를** 선택합니다.

이름, 설명, 신뢰 정책, 권한 및 태그와 같은 역할 세부 정보를 제공하는 필드입니다.]({% image_buster /assets/img/security_export/name_review_create.png %})

새로 생성한 역할이 목록에 표시됩니다!

### 4단계: Braze AWS 링크

1. AWS 콘솔의 목록에서 새로 만든 역할을 찾습니다. 이름을 선택하여 해당 역할의 세부 정보를 열고 **ARN을** 기록해 두세요.

!"보안 이벤트 내보내기 올라프"라는 역할에 대한 요약 페이지입니다.]({% image_buster /assets/img/security_export/credentials2.png %})

{: start="2"}
2\. Braze에서 **설정** > **회사 설정** > **관리자 설정** > **보안 설정으로** 이동하여 **보안 이벤트 다운로드** 섹션으로 스크롤합니다.

!"["보안 이벤트 다운로드" 섹션에서 "AWS S3로 내보내기"에 대한 토글이 켜져 있습니다.]({% image_buster /assets/img/security_export/security_event_download3.png %})

{: start="3"}
3\. **AWS 역할 ARN이** 선택되었는지 확인한 다음 지정된 필드에 역할 ARN과 AWS S3 버킷 이름을 입력합니다.
4\. 자격 증명 **테스트를** 선택하여 자격 증명이 제대로 작동하는지 확인합니다.
5\. **변경 사항 저장을** 선택합니다. 

!"["변경 사항 저장" 버튼.]({% image_buster /assets/img/security_export/save_changes_button.png %}){: style="max-width:40%;"}

AWS S3를 Braze 계정에 통합했습니다!