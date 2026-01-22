---
nav_title: 파일 스토리지 통합
article_title: 파일 스토리지 통합
description: "이 페이지에서는 Braze 클라우드 데이터 수집과 S3에서 Braze로 관련 데이터를 동기화하는 방법에 대해 설명합니다."
page_order: 3
page_type: reference

---

# 파일 스토리지 통합

> 이 페이지에서는 클라우드 데이터 수집 지원을 설정하고 S3에서 Braze로 관련 데이터를 동기화하는 방법에 대해 설명합니다.

## 작동 방식

S3용 클라우드 데이터 수집(CDI)을 사용해 AWS 계정에 있는 하나 이상의 S3 버킷을 Braze와 직접 통합할 수 있습니다. 새 파일이 S3에 게시되면 SQS에 메시지가 게시되고 Braze Cloud Data Ingestion이 새 파일을 가져옵니다. 

클라우드 데이터 수집은 다음을 지원합니다:

- JSON 파일
- CSV 파일
- 마루 파일
- 속성, 커스텀 이벤트, 구매 이벤트, 사용자 삭제 및 카탈로그 데이터

## 전제 조건

통합을 위해서는 다음 리소스가 필요합니다:

 - 데이터 저장용 S3 버킷 
 - 새 파일 알림을 위한 SQS 대기줄 
 - Braze 액세스를 위한 IAM 역할  

### AWS 정의

먼저 이 작업에서 사용되는 몇 가지 용어를 정의해 보겠습니다.

| 기간 | 정의 |
| --- | --- |
| 아마존 리소스 이름(ARN) | ARN은 AWS 리소스에 대한 고유 식별자입니다. |
| ID 및 액세스 관리(IAM) | IAM은 AWS 리소스에 대한 액세스를 안전하게 제어할 수 있는 웹 서비스입니다. 이 튜토리얼에서는 IAM 정책을 생성하고 이를 IAM 역할에 할당하여 S3 버킷을 Braze Cloud 데이터 수집과 통합합니다. |
| 아마존 심플 대기줄 서비스(SQS) | SQS는 분산된 소프트웨어 시스템과 구성 요소를 통합할 수 있는 호스팅 대기줄입니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## AWS에서 클라우드 데이터 수집 설정하기

### 1단계: 소스 버킷 만들기

AWS 계정에서 기본값으로 설정된 범용 S3 버킷을 생성하세요. 폴더가 고유한 경우 S3 버킷은 여러 동기화에서 재사용할 수 있습니다.

기본값은 다음과 같습니다:

- ACL 사용 안 함
- 모든 공개 액세스 차단
- 버킷 버전 관리 비활성화하기
- SSE-S3 암호화

다음 단계에서 같은 지역에 SQS 대기줄을 만들 것이므로 버킷을 만든 지역을 기록해 두세요.

### 2단계: SQS 대기줄 만들기

생성한 버킷에 개체가 추가되는 시기를 추적할 수 있는 SQS 대기줄을 만드세요. 지금은 기본값 구성 설정을 사용하세요. 

SQS 대기줄은 전 세계적으로 고유해야 합니다(예: CDI 동기화에는 하나만 사용할 수 있고 다른 워크스페이스에서 재사용할 수 없음).

{% alert important %}
버킷을 만든 지역과 동일한 지역에서 이 SQS를 만들어야 합니다.
{% endalert %}

이 구성 중에 자주 사용하게 되므로 ARN과 SQS의 URL을 메모해 두세요.

대기줄에 액세스할 수 있는 사용자를 정의하려면 예제 JSON 객체와 함께 "진행"을 선택합니다.]({% image_buster /assets/img/cloud_ingestion/s3_ARN.png %})

### 3단계: 액세스 정책 설정

액세스 정책을 설정하려면 **고급 옵션을** 선택합니다. 

대기줄의 액세스 정책에 다음 문을 추가하되, `YOUR-BUCKET-NAME-HERE` 을 버킷 이름으로, `YOUR-SQS-ARN` 을 SQS 대기열 ARN으로, `YOUR-AWS-ACCOUNT-ID` 을 AWS 계정 ID로 바꾸도록 주의하세요: 

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

1. 1단계에서 생성한 버킷에서 **속성** > **이벤트 알림으로** 이동합니다.
2. 구성에 이름을 지정합니다. 선택 사항으로, 파일의 하위 집합만 Braze가 수집하도록 하려면 접두사 또는 접미사를 지정하여 타겟팅하세요.
3. **대상에서** **SQS 대기줄을** 선택하고 2단계에서 생성한 SQS의 ARN을 입력합니다.

{% alert note %}
S3 버킷의 루트 폴더에 파일을 업로드한 다음 일부 파일을 버킷의 특정 폴더로 옮기면 예기치 않은 오류가 발생할 수 있습니다. 대신 접두사 안에 있는 파일에 대해서만 이벤트 알림을 보내도록 변경하거나, 해당 접두사 밖에 있는 S3 버킷에 파일을 넣지 않도록 하거나, 접두사 없이 통합을 업데이트하여 모든 파일을 수집할 수 있습니다.
{% endalert %}

### 5단계: IAM 정책 만들기

Braze가 소스 버킷과 상호 작용할 수 있도록 IAM 정책을 만듭니다. 시작하려면 AWS 관리 콘솔에 계정 매니저로 로그인하세요. 

1. AWS 콘솔의 IAM 섹션으로 이동하여 탐색 모음에서 **정책을** 선택한 다음 **정책 만들기를** 선택합니다.<br><br>AWS 콘솔의 "정책 만들기" 버튼을 클릭합니다.]({% image_buster /assets/img/create_policy_1_list.png %})<br><br>

2. **JSON** 탭을 열고 **정책 설명서** 섹션에 다음 코드 스니펫을 입력하고 `YOUR-BUCKET-NAME-HERE` 을 버킷 이름으로, `YOUR-SQS-ARN-HERE` 을 SQS 대기줄 이름으로 바꾸도록 주의하세요: 

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
3\. 완료하면 **정책 검토를** 선택합니다.

4. 정책의 이름과 설명을 입력한 다음 **정책 만들기를** 선택합니다.  

"new-policy-name"이라는 이름의 정책 예시입니다.]({% image_buster /assets/img/create_policy_3_name.png %})

정책의 설명 필드입니다.]({% image_buster /assets/img/create_policy_4_created.png %})

### 6단계: IAM 역할 만들기

AWS에서 설정을 완료하려면 IAM 역할을 만들고 4단계의 IAM 정책을 여기에 첨부합니다. 

1. IAM 정책을 만든 콘솔의 동일한 IAM 섹션에서 **역할** > **역할 만들기로** 이동합니다. 

<br><br>'역할 만들기' 버튼을 클릭합니다.]({% image_buster /assets/img/create_role_1_list.png %})<br><br>

{: start="2"}
2\. Braze 대시보드에서 AWS 계정 ID를 복사합니다. **클라우드 데이터 수집으로** 이동하여 **새 데이터 동기화 만들기를** 선택한 다음 **S3 가져오기를** 선택합니다.

3. AWS에서 신뢰할 수 있는 엔터티 선택기 유형으로 **다른 AWS 계정을** 선택합니다. Braze 계정 ID를 입력합니다. **외부 ID 필요** 확인란을 선택하고 Braze에서 사용할 외부 ID를 입력합니다. 이것은 Braze 대시보드의 커런츠 연결의 **자격 증명** 섹션에서 S3 커런츠 연결을 만들 때 생성된 외부 ID입니다. 완료되면 **다음을** 선택합니다. 

<br><br> S3 "역할 만들기" 페이지. 이 페이지에는 역할 이름, 역할 설명, 신뢰할 수 있는 엔터티, 정책 및 권한 경계에 대한 필드가 있습니다.]({% image_buster /assets/img/create_role_2_another.png %})<br><br>

{: start="4"}
4\. 4단계에서 만든 정책을 역할에 첨부합니다. 검색창에서 정책을 검색하고 정책 옆의 확인 표시를 선택하여 첨부합니다. 완료되면 **다음을** 선택합니다.

<br><br>\![새 정책 이름이 선택된 역할 ARN.]({% image_buster /assets/img/create_role_3_attach.png %})<br><br>

역할에 이름과 설명을 입력하고 **역할 만들기를** 선택합니다.

<br><br>"new-role-name"이라는 이름의 역할 예시입니다.]({% image_buster /assets/img/create_role_4_name.png %})<br><br>

{: start="5"}
5\. 클라우드 데이터 수집 통합을 만드는 데 사용할 것이므로 방금 만든 역할의 ARN과 생성한 외부 ID를 기록해 두세요.

## Braze에서 클라우드 데이터 수집 설정하기

1. 새 데이터 통합을 만들려면 **데이터 설정** > **클라우드 데이터 수집으로** 이동하여 **새 데이터 동기화 만들기를** 선택한 다음, 파일 소스 섹션에서 **S3 가져오기를** 선택합니다. 
2. AWS 설정 프로세스의 정보를 입력하여 새 동기화를 생성합니다. 다음을 지정합니다:

  - 역할 ARN
  - 외부 ID
  - SQS URL(새 통합마다 고유해야 함)
  - 버킷 이름
  - 폴더 경로(선택 사항, 워크스페이스의 모든 동기화에서 고유해야 함)
  - 지역

새 가져오기 동기화를 만들기 위해 S3에 표시된 보안 자격 증명을 입력합니다.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3\. 통합의 이름을 지정하고 이 통합에 사용할 데이터 유형을 선택합니다. 

<br><br>\![사용자 속성을 데이터 유형으로 사용하여 "cdi-s3-as-source-integration"에 대한 동기화 세부 정보를 설정합니다.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_2.png %})<br><br>

{: start="4"}
4\. 액세스 또는 권한 문제로 인해 동기화가 중단된 경우 알림을 받을 연락처 이메일을 추가하세요. 선택 사항으로 사용자 수준 오류 및 동기화 성공에 대한 알림을 설정합니다. 

<br><br> \![동기화 오류 알림에 대한 알림 환경설정 설정하기.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_3.png %})<br><br>

{: start="5"}
5\. 마지막으로 연결을 테스트하고 동기화를 저장합니다. 

<br><br>데이터 미리 보기로 연결을 테스트하는 옵션입니다.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})

## 필수 파일 형식

클라우드 데이터 수집은 JSON, CSV, Parquet 파일을 지원합니다. 각 파일에는 지원되는 식별자 열과 페이로드 열이 JSON 문자열로 하나 이상 포함되어야 합니다.

Braze는 AWS에서 시행하는 것 외에 추가적인 파일 이름 요구 사항을 적용하지 않습니다. 파일 이름은 고유해야 합니다. 고유성을 위해 타임스탬프를 추가하는 것이 좋습니다.

### 사용자 식별자

소스 파일에는 하나 이상의 사용자 식별자 열 또는 키가 포함될 수 있습니다. 각 행에는 하나의 식별자만 포함되어야 하지만 소스 파일에는 여러 식별자 유형이 있을 수 있습니다.

| 식별자 | 설명 |
| --- | --- |
| `EXTERNAL_ID` | 업데이트하려는 사용자를 식별합니다. 이 값은 Braze에서 사용된 `external_id` 값과 일치해야 합니다. |
| `ALIAS_NAME` 그리고 `ALIAS_LABEL` | `alias_name` 은 고유 식별자이고 `alias_label` 은 별칭의 유형을 지정해야 하며, 이 두 열은 사용자 별칭 개체를 만듭니다. 사용자는 서로 다른 라벨을 가진 여러 개의 별칭을 지정할 수 있지만 `alias_label` 당 하나의 `alias_name` 만 사용할 수 있습니다. |
| `BRAZE_ID` | Braze 사용자 식별자입니다. 이는 Braze 소프트웨어 개발 키트에 의해 생성되며, 클라우드 데이터 수집을 통해 새로운 사용자 ID를 생성할 수 없습니다. 새 사용자를 만들려면 외부 사용자 ID 또는 사용자 별칭을 지정합니다. |
| `EMAIL` | 사용자의 이메일 주소입니다. 동일한 이메일 주소를 가진 프로필이 여러 개 있는 경우 가장 최근에 업데이트된 프로필이 우선적으로 업데이트됩니다. 이메일과 전화번호를 모두 포함하는 경우 이메일을 기본 식별자로 사용합니다. |
| `PHONE` | 사용자의 전화번호입니다. 동일한 전화번호를 사용하는 프로필이 여러 개 있는 경우 가장 최근에 업데이트된 프로필이 우선적으로 업데이트됩니다. |
|`PAYLOAD` | Braze에서 사용자에게 동기화하려는 필드의 JSON 문자열입니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
데이터 웨어하우스 소스와 달리 `UPDATED_AT` 열은 필요하지도 않고 지원되지도 않습니다.
{% endalert %}

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
ID,PAYLOAD
85,"{""product_name"": ""Product 85"", ""price"": 85.85}" 
1,"{""product_name"": ""Product 1"", ""price"": 1.01}" 
```
{% endtab %}

{% endtabs %}  

지원되는 모든 파일 형식의 예는 [Braze-examples의](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage) 샘플 파일을 참조하세요.  

## 알아두어야 할 사항

- S3 소스 버킷에 추가된 파일은 512MB를 초과하지 않아야 합니다. 512MB보다 큰 파일은 오류가 발생하며 Braze에 동기화되지 않습니다.
- 파일당 행 수에 대한 추가 제한은 없지만, 동기화 실행 속도를 높이려면 더 작은 파일을 사용하는 것이 좋습니다. 예를 들어, 500MB 파일은 100MB 파일 5개보다 수집하는 데 시간이 훨씬 더 오래 걸립니다.
- 주어진 시간에 업로드할 수 있는 파일 수에는 별도의 제한이 없습니다.
- 파일 내 또는 파일 간 주문은 지원되지 않습니다. 예상되는 경합 조건을 모니터링하는 경우 주기적으로 업데이트를 일괄 처리하는 것이 좋습니다.

## 문제 해결

### 파일 업로드 및 처리

CDI는 동기화가 생성된 후에 추가된 파일만 처리합니다. 이 과정에서 Braze는 추가할 새 파일을 찾아 SQS에 새 메시지를 트리거합니다. 그러면 새 파일을 처리하기 위한 새 동기화가 시작됩니다.

기존 파일은 테스트 연결에서 데이터 구조를 검증하는 데 사용할 수 있지만 Braze에 동기화되지는 않습니다. 동기화해야 하는 기존 파일은 CDI가 처리할 수 있도록 S3에 다시 업로드해야 합니다.

### 예기치 않은 파일 오류 처리

많은 수의 오류 또는 실패한 파일이 관찰되는 경우, 다른 프로세스가 CDI의 타겟팅 폴더가 아닌 다른 폴더에 있는 S3 버킷에 파일을 추가하고 있을 수 있습니다.

파일이 소스 버킷에 업로드되었지만 소스 폴더에 없는 경우 CDI는 SQS 알림을 처리하지만 파일에 대해서는 아무런 조치를 취하지 않으므로 오류로 표시될 수 있습니다.
