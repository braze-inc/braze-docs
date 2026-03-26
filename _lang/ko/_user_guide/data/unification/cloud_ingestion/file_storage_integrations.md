---
nav_title: 파일 스토리지 통합
article_title: 파일 저장 통합
description: "이 페이지에서는 Braze 클라우드 데이터 수집과 S3에서 Braze로 관련 데이터를 동기화하는 방법에 대해 설명합니다."
page_order: 3
page_type: reference

---

# 파일 스토리지 통합

> 이 페이지에서는 클라우드 데이터 수집 지원을 설정하고 S3에서 Braze로 관련 데이터를 동기화하는 방법에 대해 설명합니다.

이 페이지에서는 현재 조기 액세스(EA) 중인 동기화 및 소스 단계를 보여줍니다. 일반 제공 환경의 단계를 보려면 아래의 **일반 제공 환경**을 펼치세요.

## 작동 방식

S3용 클라우드 데이터 수집(CDI)을 사용하여 AWS 계정에 있는 하나 이상의 S3 버킷을 Braze와 직접 통합할 수 있습니다. 새 파일이 S3에 게시되면 SQS에 메시지가 게시되고 Braze 클라우드 데이터 수집이 해당 새 파일을 가져옵니다. 

클라우드 데이터 수집은 다음을 지원합니다:

- JSON 파일
- CSV 파일
- Parquet 파일
- 속성, 커스텀 이벤트, 구매 이벤트, 사용자 삭제 및 카탈로그 데이터

## 필수 조건

통합에는 다음 리소스가 필요합니다:

 - 데이터 저장용 S3 버킷 
 - 새 파일 알림을 위한 SQS 대기열 
 - Braze 액세스를 위한 IAM 역할  

### AWS 정의

먼저, 이 작업에서 사용되는 용어를 정의합니다.

| 용어 | 정의 |
| --- | --- |
| Amazon 리소스 이름(ARN) | ARN은 AWS 리소스에 대한 고유 식별자입니다. |
| ID 및 액세스 관리(IAM) | IAM은 AWS 리소스에 대한 액세스를 안전하게 제어할 수 있는 웹 서비스입니다. 이 튜토리얼에서는 IAM 정책을 만들고 이를 IAM 역할에 할당하여 S3 버킷을 Braze 클라우드 데이터 수집과 통합합니다. |
| Amazon Simple Queue Service(SQS) | SQS는 분산된 소프트웨어 시스템과 구성요소를 통합할 수 있는 호스팅 대기열입니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## AWS에서 클라우드 데이터 수집 설정하기

### 1단계: 소스 버킷 만들기

AWS 계정에서 기본 설정으로 범용 S3 버킷을 생성합니다. S3 버킷은 폴더가 고유한 한 여러 동기화에서 재사용할 수 있습니다.

기본 설정은 다음과 같습니다:

- ACL 사용 안 함
- 모든 공개 액세스 차단
- 버킷 버전 관리 비활성화
- SSE-S3 암호화
  - SSE-S3는 지원되는 유일한 서버 측 암호화 유형입니다. Amazon KMS 암호화는 지원되지 않습니다.

다음 단계에서 동일한 리전에 SQS 대기열을 생성할 것이므로 버킷을 생성한 리전을 기록해 두세요.

### 2단계: SQS 대기열 만들기

생성한 버킷에 오브젝트가 추가되는 시기를 추적할 수 있는 SQS 대기열을 만듭니다. 지금은 기본 구성 설정을 사용하세요. 

SQS 대기열은 전역적으로 고유해야 합니다(예: CDI 동기화에는 하나만 사용할 수 있고 다른 워크스페이스에서 재사용할 수 없음).

{% alert important %}
버킷을 생성한 리전과 동일한 리전에 이 SQS를 생성해야 합니다.
{% endalert %}

이 구성 중에 자주 사용하게 되므로 SQS 대기열의 ARN과 URL을 메모해 두세요.

![대기열에 접근할 수 있는 사람을 정의하기 위한 예제 JSON 오브젝트와 함께 "고급"을 선택합니다.]({% image_buster /assets/img/cloud_ingestion/s3_ARN.png %})

### 3단계: 액세스 정책 설정

액세스 정책을 설정하려면 **고급 옵션**을 선택합니다. 

다음 문장을 대기열의 액세스 정책에 추가하되, `YOUR-BUCKET-NAME-HERE`를 버킷 이름으로, `YOUR-SQS-ARN`을 SQS 대기열 ARN으로, `YOUR-AWS-ACCOUNT-ID`를 AWS 계정 ID로 바꾸세요: 

``` json 
{
  "Sid": "braze-cdi-s3-sqs-publish",
  "Effect": "Allow",
  "Principal": {
    "Service": "s3.amazonaws.com"
  },
  "Action": "SQS:SendMessage",
  "Resource": "YOUR-SQS-ARN",
  "Condition": {
    "StringEquals": {
      "aws:SourceAccount": "YOUR-AWS-ACCOUNT-ID"
    },
    "ArnLike": {
      "aws:SourceArn": "arn:aws:s3:::YOUR-BUCKET-NAME-HERE"
    }
  }
} 
```

### 4단계: S3 버킷에 이벤트 알림 추가하기

1. 1단계에서 만든 버킷에서 **속성** > **이벤트 알림**으로 이동합니다.
2. 구성에 이름을 지정합니다. 선택적으로 Braze가 파일의 하위 집합만 수집하도록 하려면 접두사 또는 접미사를 지정합니다.
3. **대상**에서 **SQS 대기열**을 선택하고 2단계에서 생성한 SQS의 ARN을 입력합니다.

{% alert note %}
S3 버킷의 루트 폴더에 파일을 업로드한 다음 일부 파일을 버킷의 특정 폴더로 이동하면 예기치 않은 오류가 발생할 수 있습니다. 대신 접두사 안에 있는 파일에 대해서만 이벤트 알림을 보내도록 변경하거나, 해당 접두사 밖에 있는 S3 버킷에 파일을 넣지 않도록 하거나, 접두사 없이 통합을 업데이트하여 모든 파일을 수집할 수 있습니다.
{% endalert %}

### 5단계: IAM 정책 만들기

Braze가 소스 버킷과 상호 작용할 수 있도록 IAM 정책을 만듭니다. 시작하려면 계정 관리자로 AWS 관리 콘솔에 로그인합니다. 

1. AWS 콘솔의 IAM 섹션으로 이동하여 탐색 모음에서 **정책**을 선택한 다음 **정책 생성**을 선택합니다.<br><br>![AWS 콘솔의 "정책 생성" 버튼.]({% image_buster /assets/img/create_policy_1_list.png %})<br><br>

2. **JSON** 탭을 열고 **정책 문서** 섹션에 다음 코드 스니펫을 입력합니다. `YOUR-BUCKET-NAME-HERE`를 버킷 이름으로, `YOUR-SQS-ARN-HERE`를 SQS 대기열 이름으로 바꾸세요: 

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetObjectAttributes", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::YOUR-BUCKET-NAME-HERE"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetObjectAttributes", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::YOUR-BUCKET-NAME-HERE/*"]
        },
        {
            "Effect": "Allow",
            "Action": [
                "sqs:DeleteMessage",
                "sqs:GetQueueUrl",
                "sqs:ReceiveMessage",
                "sqs:GetQueueAttributes"
            ],
            "Resource": "YOUR-SQS-ARN-HERE"
        }
    ]
}

```  

{: start="3"}
3. 완료되면 **정책 검토**를 선택합니다.

4. 정책에 이름과 설명을 입력한 다음 **정책 생성**을 선택합니다.  

!["new-policy-name"이라는 이름의 예제 정책.]({% image_buster /assets/img/create_policy_3_name.png %})

![정책에 대한 설명 필드.]({% image_buster /assets/img/create_policy_4_created.png %})

### 6단계: IAM 역할 만들기

AWS에서 설정을 완료하려면 IAM 역할을 만들고 5단계의 IAM 정책을 연결합니다. 

1. IAM 정책을 만든 콘솔의 동일한 IAM 섹션에서 **역할** > **역할 만들기**로 이동합니다. 

!["역할 생성" 버튼.]({% image_buster /assets/img/create_role_1_list.png %})

{: start="2"}
2. AWS에서 신뢰할 수 있는 엔터티 선택기 유형으로 **다른 AWS 계정**을 선택합니다. Braze 계정 ID를 입력합니다. **외부 ID 필요** 체크박스를 선택합니다.
3. Braze에서 **데이터 설정** > **클라우드 데이터 수집** > **소스**로 이동하여 **데이터 소스 추가**를 선택하고 파일 소스 섹션에서 **Amazon S3**를 선택합니다.
4. 자동으로 생성된 **Braze 계정 ID**를 복사합니다. 

![소스 이름 및 S3 연결 세부 정보 섹션이 표시된 "새 소스 추가" 페이지.]({% image_buster /assets/img/braze_account_id.png %})

{: start="6"}
5. AWS에서 계정 ID를 붙여넣고 **다음**을 선택합니다.

![S3 "역할 만들기" 페이지. 이 페이지에는 역할 이름, 역할 설명, 신뢰할 수 있는 엔터티, 정책 및 권한 경계에 대한 필드가 있습니다.]({% image_buster /assets/img/create_role_2_another.png %})<br><br>

{: start="7"}
6. 5단계에서 만든 정책을 역할에 연결합니다. 검색창에서 정책을 검색하고 정책 옆의 체크 표시를 선택하여 연결합니다. 완료되면 **다음**을 선택합니다.

![새 정책 이름이 선택된 역할 ARN.]({% image_buster /assets/img/create_role_3_attach.png %})

역할에 이름과 설명을 입력하고 **역할 만들기**를 선택합니다.

!["new-role-name"이라는 이름의 예제 역할.]({% image_buster /assets/img/create_role_4_name.png %})

{: start="8"}
7. 생성한 역할의 ARN과 생성한 외부 ID를 기록해 두세요. 클라우드 데이터 수집 통합을 생성하는 데 필요합니다.

## Braze에서 클라우드 데이터 수집 설정하기

1. 먼저 Braze 대시보드에서 새 소스를 생성합니다. **데이터 설정** > **클라우드 데이터 수집** > **소스**로 이동하여 **데이터 소스 추가**를 선택한 다음 **Amazon S3**를 선택합니다.
2. 소스의 이름을 지정하고 AWS 설정 프로세스의 정보를 입력하여 새 소스를 생성합니다. 다음을 지정합니다:

  - 역할 ARN
  - 외부 ID
  - 버킷 이름
  - 리전

![자격 증명(AWS 설정 및 Braze 설정) 및 구성 필드가 표시된 S3 연결 세부 정보 섹션.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3. **연결 테스트**를 선택하여 Braze가 버킷에 액세스할 수 있는지 확인합니다. 테스트가 성공하면 **소스에 연결**을 선택합니다. 연결에 실패하면 문제 해결에 도움이 되는 오류 메시지가 표시됩니다.

{: start="4"}
4. 다음으로 새 동기화를 생성합니다. **데이터 설정** > **클라우드 데이터 수집** > **동기화**로 이동하여 **데이터 동기화 생성**을 선택합니다.

![동기화 이름 및 데이터 소스 구성이 표시된 "새 동기화 생성" 페이지.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_3.png %})

{: start="5"}
5. 동기화의 이름을 지정합니다. 그런 다음 활성 S3 소스를 선택하고 동기화를 위한 소스 테이블을 입력합니다. 데이터 유형을 선택하고 **연결 테스트**를 선택합니다.

![데이터 미리보기로 연결을 테스트하는 옵션.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})

6. AWS 설정 프로세스의 나머지 정보를 입력합니다. 다음을 지정합니다:
- SQS URL(새 통합마다 고유해야 함)
- 폴더 경로(선택 사항, 워크스페이스 내 동기화 전체에서 고유해야 함)

7. 데이터 유형을 선택하고 **연결 테스트**를 선택하여 Braze가 수집 가능한 파일 목록을 확인할 수 있는지 검증합니다(파일 내부의 데이터가 아닌 파일 목록만 확인). 성공하면 **다음: 알림**을 선택합니다.
8. 액세스 또는 권한 문제로 인해 동기화가 중단되는 경우 알림을 받을 연락처 이메일을 추가합니다. 선택적으로 사용자 수준 오류 및 동기화 성공에 대한 알림을 설정할 수 있습니다.
9. 동기화를 생성합니다.

{% details 일반 제공 환경 %}

1. 새 통합을 만들려면 **데이터 설정** > **클라우드 데이터 수집**으로 이동하여 **새 데이터 동기화 만들기**를 선택한 다음, 파일 소스 섹션에서 **S3 가져오기**를 선택합니다. 
2. AWS 설정 프로세스의 정보를 입력하여 새 동기화를 생성합니다. 다음을 지정합니다:

  - 역할 ARN
  - 외부 ID
  - SQS URL(새 통합마다 고유해야 함)
  - 버킷 이름
  - 폴더 경로(선택 사항, 워크스페이스 내 동기화 전체에서 고유해야 함)
  - 리전

{: start="3"}
3. 통합의 이름을 지정하고 이 통합의 데이터 유형을 선택합니다. 

{: start="4"}
4. 액세스 또는 권한 문제로 인해 동기화가 중단되는 경우 알림을 받을 연락처 이메일을 추가합니다. 선택적으로 사용자 수준 오류 및 동기화 성공에 대한 알림을 설정할 수 있습니다. 

{: start="5"}
5. 마지막으로 **연결 테스트**를 선택하여 Braze가 버킷에 액세스하고 수집 가능한 파일 목록을 확인할 수 있는지 검증합니다(파일 내부의 데이터가 아닌 파일 목록만 확인). 그런 다음 동기화를 저장합니다. 

{% enddetails %}

## 필수 파일 형식

클라우드 데이터 수집은 JSON, CSV 및 Parquet 파일을 지원합니다. 필수 열은 데이터 유형에 따라 다릅니다: 

- 사용자 데이터(속성, 커스텀 이벤트, 구매 이벤트)는 사용자 식별자와 페이로드를 사용합니다
- 카탈로그 데이터는 카탈로그 식별자를 사용합니다

Braze는 AWS에서 적용하는 것 외에 추가적인 파일 이름 요구 사항을 적용하지 않습니다. 파일 이름은 고유해야 합니다. 고유성을 보장하려면 타임스탬프를 추가하는 것이 좋습니다.

지원되는 모든 파일 형식(속성, 커스텀 이벤트, 구매, 카탈로그 및 사용자 삭제)의 예는 [braze-examples](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage)의 샘플 파일을 참조하세요.

### 사용자 식별자 {#user-identifiers}

사용자 데이터 동기화(속성, 커스텀 이벤트, 구매 이벤트)의 경우, 소스 파일의 각 행에는 정확히 하나의 사용자 식별자와 `PAYLOAD` 열이 필요합니다. 소스 파일에는 서로 다른 식별자 유형의 행이 포함될 수 있지만, 각 개별 행은 하나의 식별자만 사용해야 합니다.

| 식별자 | 설명 |
| --- | --- |
| `EXTERNAL_ID` | 업데이트하려는 사용자를 식별합니다. 이 값은 Braze에서 사용하는 `external_id` 값과 일치해야 합니다. |
| `ALIAS_NAME` 및 `ALIAS_LABEL` | 이 두 열은 사용자 별칭 오브젝트를 만듭니다. `alias_name`은 고유 식별자이고 `alias_label`은 별칭의 유형을 지정합니다. 사용자는 서로 다른 레이블을 가진 여러 별칭을 가질 수 있지만, `alias_label`당 하나의 `alias_name`만 가질 수 있습니다. |
| `BRAZE_ID` | Braze 사용자 식별자입니다. Braze SDK에 의해 생성되며, 클라우드 데이터 수집을 통해 Braze ID로 새 사용자를 생성할 수는 없습니다. 새 사용자를 만들려면 외부 사용자 ID 또는 사용자 별칭을 지정하세요. |
| `EMAIL` | 사용자의 이메일 주소입니다. 동일한 이메일 주소를 가진 프로필이 여러 개 존재하는 경우, 가장 최근에 업데이트된 프로필이 우선적으로 업데이트됩니다. 이메일과 전화번호를 모두 포함하면 Braze는 이메일을 기본 식별자로 사용합니다. |
| `PHONE` | 사용자의 전화번호입니다. 동일한 전화번호를 가진 프로필이 여러 개 존재하는 경우, 가장 최근에 업데이트된 프로필이 우선적으로 업데이트됩니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

식별자 외에도 각 행에는 Braze에서 사용자에게 동기화하려는 필드의 JSON 문자열이 포함된 `PAYLOAD` 열이 있어야 합니다.

{% alert note %}
데이터 웨어하우스 소스와 달리, `UPDATED_AT` 열은 파일 스토리지 동기화에서 필수도 아니고 지원되지도 않습니다.
{% endalert %}

### 카탈로그 식별자 {#catalog-identifiers}

카탈로그 동기화의 경우, 소스 파일에 다음 열이 포함되어야 합니다. 카탈로그 파일은 사용자 데이터 파일과 다른 식별자를 사용합니다.

| 열 | 필수 | 설명 |
| --- | --- | --- |
| `ID` | 예 | 카탈로그 항목의 고유 식별자입니다. Braze에서 항목을 생성, 업데이트 또는 삭제하는 데 사용됩니다. |
| `PAYLOAD` | 예 | 동기화할 카탈로그 필드와 값의 JSON 문자열입니다. Braze의 카탈로그 스키마와 일치해야 합니다. |
| `DELETED` | 아니요 | `true`일 때 일치하는 `ID`의 카탈로그 항목이 Braze의 카탈로그에서 제거됩니다. 생성 또는 업데이트 작업의 경우 이 열을 생략하거나 `false`로 설정합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### 예제

{% tabs %}
{% tab JSON Attributes %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"name\": \"GT896\", \"age\": 74, \"subscriber\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}"}
{"external_id":"s3-qa-1","payload":"{\"name\": \"HSCJC\", \"age\": 86, \"subscriber\": false, \"retention\": {\"previous_purchases\": 0, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600824\"}"}
{"external_id":"s3-qa-2","payload":"{\"name\": \"YTMQZ\", \"age\": 43, \"subscriber\": false, \"retention\": {\"previous_purchases\": 23, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600831\"}"}
{"external_id":"s3-qa-3","payload":"{\"name\": \"5P44M\", \"age\": 15, \"subscriber\": true, \"retention\": {\"previous_purchases\": 7, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600838\"}"}
{"external_id":"s3-qa-4","payload":"{\"name\": \"WMYS7\", \"age\": 11, \"subscriber\": true, \"retention\": {\"previous_purchases\": 0, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600844\"}"}
{"external_id":"s3-qa-5","payload":"{\"name\": \"KCBLK\", \"age\": 47, \"subscriber\": true, \"retention\": {\"previous_purchases\": 11, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600850\"}"}
{"external_id":"s3-qa-6","payload":"{\"name\": \"T93MJ\", \"age\": 47, \"subscriber\": true, \"retention\": {\"previous_purchases\": 10, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600856\"}"}
```  
{% alert important %}
소스 파일의 모든 줄에 유효한 JSON이 포함되어야 하며, 그렇지 않으면 파일이 건너뛰어집니다. 
{% endalert %}
{% endtab %}
{% tab JSON Custom Events %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
```  
{% alert important %}
소스 파일의 모든 줄에 유효한 JSON이 포함되어야 하며, 그렇지 않으면 파일이 건너뛰어집니다. 
{% endalert %}
{% endtab %}
{% tab JSON Purchase Events %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
```  
{% alert important %}
소스 파일의 모든 줄에 유효한 JSON이 포함되어야 하며, 그렇지 않으면 파일이 건너뛰어집니다.
{% endalert %}

{% endtab %}
{% tab CSV Attributes %}
```plaintext  
external_id,payload
s3-qa-load-0-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""SNXIM"", ""age"": 54, ""subscriber"": true, ""retention"": {""previous_purchases"": 19, ""vip"": true}, ""last_visit"": ""2023-08-08T16:03:26.598806""}"
s3-qa-load-1-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""0J747"", ""age"": 73, ""subscriber"": false, ""retention"": {""previous_purchases"": 22, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598816""}"
s3-qa-load-2-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""EP1U0"", ""age"": 99, ""subscriber"": false, ""retention"": {""previous_purchases"": 23, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598822""}"
```
{% endtab %}
{% tab CSV Catalogs  %}
```plaintext  
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```
선택적 `DELETED` 열을 포함합니다. `DELETED`가 `true`일 때 해당 카탈로그 항목은 Braze의 카탈로그에서 제거됩니다. 필수 열의 전체 목록은 [카탈로그 식별자](#catalog-identifiers)를 참조하세요. 삭제 동작에 대해서는 [카탈로그 항목 삭제](#deleting-catalog-items)를 참조하세요.
{% endtab %}

{% endtabs %}  

## 데이터 삭제

S3용 클라우드 데이터 수집은 파일 업로드를 통해 사용자 및 카탈로그 항목 삭제를 지원합니다. 각각에 대해 별도의 동기화 및 파일 형식을 사용하세요.

- **[사용자 삭제](#deleting-users)** – 데이터 유형 **사용자 삭제**로 동기화를 생성하고 사용자 식별자만 포함된 파일(페이로드 없음)을 업로드합니다.
- **[카탈로그 항목 삭제](#deleting-catalog-items)** – 기존 카탈로그 동기화를 사용하고 항목 제거를 표시하기 위해 `deleted`(또는 `DELETED`) 열을 추가합니다.

### 사용자 삭제

S3의 파일을 사용하여 Braze에서 고객 프로필을 삭제하려면:

1. 새 클라우드 데이터 수집 동기화를 생성합니다(다른 동기화와 동일한 [AWS 및 Braze 설정](#setting-up-cloud-data-ingestion-in-aws)).
2. Braze에서 동기화를 구성할 때 **데이터 유형**을 **사용자 삭제**로 설정합니다.
3. 사용자 식별자 열만 포함된 파일을 S3 버킷에 업로드합니다. `PAYLOAD` 열은 포함하지 마세요. 페이로드가 존재하면 우발적인 삭제를 방지하기 위해 동기화가 실패합니다.

파일의 각 행은 다음 중 하나를 사용하여 정확히 한 명의 사용자를 식별해야 합니다:

| 식별자 | 설명 |
| --- | --- |
| `EXTERNAL_ID` | Braze에서 사용되는 `external_id`와 일치합니다. |
| `ALIAS_NAME` 및 `ALIAS_LABEL` | 두 열이 함께 별칭으로 사용자를 식별합니다. |
| `BRAZE_ID` | Braze에서 생성된 사용자 ID(기존 사용자만 해당). |

{% alert important %}
사용자 삭제는 영구적이며 되돌릴 수 없습니다. 제거하려는 사용자만 포함하세요. 자세한 내용은 [클라우드 데이터 수집으로 사용자 삭제]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/delete_users/)를 참조하세요.
{% endalert %}

**예 – JSON (사용자 삭제):**
```jsonl
{"external_id":"user-to-delete-001"}
{"external_id":"user-to-delete-002"}
{"braze_id":"braze-id-from-profile"}
```

**예 – CSV (사용자 삭제):**
```plaintext
external_id
user-to-delete-001
user-to-delete-002
```

동기화가 실행되면 Braze는 버킷의 새 파일을 처리하고 해당 고객 프로필을 삭제합니다.

### 카탈로그 항목 삭제

파일 스토리지를 사용하여 카탈로그에서 항목을 제거하려면:

1. [카탈로그 데이터 동기화]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data/)에 사용하는 동일한 S3 동기화를 사용합니다(데이터 유형 **카탈로그**).
2. CSV 또는 JSON 파일에 선택적 **`deleted`**(또는 **`DELETED`**) 열을 추가합니다.
3. Braze의 카탈로그에서 제거할 카탈로그 항목에 대해 `deleted`를 `true`로 설정합니다.

각 행에는 여전히 `ID` 및 `PAYLOAD`가 필요합니다. 삭제 대상으로 표시된 행의 경우 페이로드는 최소한의 값만 포함해도 됩니다. Braze는 `ID`를 기준으로 항목을 제거합니다.

**예 – JSON (카탈로그 항목 삭제):**
```jsonl
{"id":"85","payload":"{\"product_name\": \"Product 85\", \"price\": 85.85}"}
{"id":"1","payload":"{\"product_name\": \"Product 1\", \"price\": 1.01}","deleted":true}
```

**예 – CSV (카탈로그 항목 삭제):**
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```

동기화가 실행될 때, `deleted: true`가 있는 행은 Braze에서 일치하는 카탈로그 항목이 삭제됩니다. 전체 카탈로그 동기화 및 삭제 동작에 대해서는 [카탈로그 데이터 동기화 및 삭제]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data/)를 참조하세요.

## 알아두어야 할 사항

- S3 소스 버킷에 추가되는 파일은 512&nbsp;MB를 초과하면 안 됩니다. 512&nbsp;MB보다 큰 파일은 오류가 발생하며 Braze에 동기화되지 않습니다.
- 파일당 행 수에 대한 추가 제한은 없지만, 동기화 속도를 개선하기 위해 더 작은 파일을 사용하는 것이 좋습니다. 예를 들어, 500&nbsp;MB 파일은 5개의 별도 100&nbsp;MB 파일보다 수집하는 데 상당히 더 오래 걸립니다.
- 주어진 시간에 업로드되는 파일 수에 대한 추가 제한은 없습니다.
- 파일 내부 또는 파일 간 순서 지정은 지원되지 않습니다. 예상되는 경합 조건을 모니터링하는 경우 주기적으로 업데이트를 일괄 처리하는 것이 좋습니다.

## 문제 해결

### 파일 업로드 및 처리

CDI는 동기화가 생성된 후에 추가된 파일만 처리합니다. 이 과정에서 Braze는 새로 추가되는 파일을 감지하고, 이를 통해 SQS에 새 메시지가 트리거됩니다. 그러면 새 파일을 처리하기 위한 새 동기화가 시작됩니다.

기존 파일을 사용하여 Braze가 버킷에 액세스하고 수집할 파일을 감지할 수 있는지 확인할 수 있지만, 이 파일들은 Braze에 동기화되지 않습니다. CDI가 이를 처리하려면, 동기화하려는 기존 파일을 S3에 다시 업로드해야 합니다. 

### 예기치 않은 파일 오류 처리

많은 수의 오류 또는 실패한 파일이 관찰되는 경우, CDI의 대상 폴더가 아닌 다른 폴더에서 S3 버킷에 파일을 추가하는 다른 프로세스가 있을 수 있습니다.

소스 버킷에 파일이 업로드되었지만 소스 폴더에 없는 경우, CDI는 SQS 알림을 처리하지만 파일에 대해 아무런 작업도 수행하지 않으므로 오류로 표시될 수 있습니다.