---
nav_title: 파일 스토리지 통합
article_title: 파일 스토리지 통합
description: "이 참조 문서에서는 Braze 클라우드 데이터 수집과 S3에서 Braze로 관련 데이터를 동기화하는 방법을 다룹니다."
page_order: 3
page_type: reference

---

# 파일 스토리지 통합

> 이 문서에서는 클라우드 데이터 수집 지원을 설정하고 S3에서 Braze로 관련 데이터를 동기화하는 방법에 대해 설명합니다.

S3용 클라우드 데이터 수집(CDI)을 사용하여 AWS 계정에 있는 하나 이상의 S3 버킷을 Braze와 직접 통합할 수 있습니다. 새 파일이 S3에 게시되면 SQS에 메시지가 게시되고 Braze 클라우드 데이터 수집이 해당하는 새 파일을 받습니다. 

클라우드 데이터 수집은 JSON, CSV 및 Parquet 파일과 속성, 이벤트, 구매 및 사용자 삭제 데이터를 지원합니다.

통합에는 다음 리소스가 필요합니다:
 - 데이터 저장용 S3 버킷 
 - 새 파일 알림을 위한 SQS 대기열 
 - Braze 액세스를 위한 IAM 역할  


## AWS 정의

먼저 이 작업에서 사용되는 몇 가지 용어를 정의해 봅시다.

| Word | 정의 |
| --- | --- |
| 아마존 리소스 이름(ARN) | ARN은 AWS 리소스에 대한 고유 식별자입니다. |
| ID 및 액세스 관리(IAM) | IAM은 AWS 리소스에 대한 액세스를 안전하게 제어할 수 있는 웹 서비스입니다. 이 튜토리얼에서는 IAM 정책을 만들고 이를 IAM 역할에 할당하여 S3 버킷을 Braze 클라우드 데이터 수집과 통합하는 방법을 설명합니다. |
| 아마존 단순 대기열 서비스(SQS) | SQS는 분산된 소프트웨어 시스템과 구성 요소를 통합할 수 있는 호스팅 대기열입니다. |
{: .reset-td-br-1 .reset-td-br-2 }
 

## AWS에서 클라우드 데이터 수집 설정하기

### 1단계: 소스 버킷 만들기

AWS 계정에서 기본 설정으로 범용 S3 버킷을 생성하세요. 

기본 설정은 다음과 같습니다:
  - ACL 사용 안 함
  - 모든 공개 액세스 차단
  - 버킷 버전 관리 비활성화
  - SSE-S3 암호화

다음 단계에서 같은 지역에 SQS 대기줄을 만들 것이므로 버킷을 만든 지역을 기록해 두세요.

### 2단계: SQS 대기열 만들기

생성한 버킷에 개체가 추가되는 시기를 추적할 수 있는 SQS 대기열을 만듭니다. 지금은 기본 구성 설정을 사용하세요.

{% alert important %}
버킷을 만든 지역과 동일한 지역에서 이 SQS를 만들어야 합니다.
{% endalert %}

이 구성 중에 자주 사용하게 되므로 ARN과 SQS의 URL을 메모해 두세요.
<br><br>![]({% image_buster /assets/img/cloud_ingestion/s3_ARN.png %})
<br><br>

### 3단계: 액세스 정책 설정

액세스 정책을 설정하려면 **고급 옵션**을 선택합니다. 

다음 문장을 대기줄의 액세스 정책에 추가하되, `YOUR-BUCKET-NAME-HERE`을 버킷 이름으로, `YOUR-SQS-ARN`을 SQS 대기열 ARN으로, `YOUR-AWS-ACCOUNT-ID`을 AWS 계정 ID로 바꾸도록 주의하세요 

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

1. 1단계에서 만든 버킷에서 **속성** > **이벤트 알림으로** 이동합니다.

2. 구성에 이름을 지정합니다. 선택 사항으로 Braze가 파일의 하위 집합만 수집하도록 하려면 접두사 또는 접미사를 지정하여 대상을 지정합니다.

3. **대상**에서 **SQS 대기줄**을 선택하고 2단계에서 생성한 SQS의 ARN을 입력합니다.

### 5단계: IAM 정책 만들기

Braze가 소스 버킷과 상호 작용할 수 있도록 IAM 정책을 만듭니다. 시작하려면 계정 관리자로 AWS 관리 콘솔에 로그인합니다. 

1. AWS 콘솔의 IAM 섹션으로 이동하여 탐색 모음에서 **정책**을 선택한 다음 **정책 생성**을 선택합니다.<br><br>![]({{site.baseurl}}/assets/img/create_policy_1_list.png)<br><br>

2. **JSON** 탭을 열고 **정책 문서** 섹션에 다음 코드 스니펫을 입력하고 `YOUR-BUCKET-NAME-HERE` 을 버킷 이름으로, `YOUR-SQS-ARN-HERE` 을 SQS 대기열 이름으로 바꾸도록 주의하세요: 

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
3\. 완료하면 **정책 검토**를 선택합니다.

4. 정책의 이름 및 설명을 입력하고 **정책 만들기**를 선택합니다.  

![]({{site.baseurl}}/assets/img/create_policy_3_name.png)

![]({{site.baseurl}}/assets/img/create_policy_4_created.png)

### 6단계: IAM 역할 만들기

AWS에서 설정을 완료하려면 IAM 역할을 만들고 4단계의 IAM 정책을 여기에 첨부합니다. 

1. IAM 정책을 만든 콘솔의 동일한 IAM 섹션에서 **역할** > **역할 만들기로** 이동합니다. <br><br>![]({{site.baseurl}}/assets/img/create_role_1_list.png)<br><br>

2. Braze 대시보드에서 Braze AWS 계정 ID를 복사합니다. **클라우드 데이터 수집으로** 이동하여 **새 데이터 동기화 만들기를** 클릭하고 **S3 가져오기를** 선택합니다. <br><br>![]({{site.baseurl}}/assets/img/cloud_ingestion/s3_copy_braze_account_id.png)<br><br>

3. AWS에서 신뢰할 수 있는 엔터티 선택기 유형으로 **다른 AWS 계정**을 선택합니다. Braze 계정 ID를 입력하고 **외부 ID 필요** 확인란을 선택한 다음, Braze에서 사용할 외부 ID를 입력합니다. 완료되면 **다음**을 선택합니다. <br><br> ![S3 "역할 만들기" 페이지. 이 페이지에는 역할 이름, 역할 설명, 신뢰할 수 있는 엔터티, 정책 및 권한 경계에 대한 필드가 있습니다.]({{site.baseurl}}/assets/img/create_role_2_another.png)

4. 4단계에서 만든 정책을 역할에 첨부합니다. 검색창에서 정책을 검색하고 정책 옆의 확인 표시를 선택하여 첨부합니다. 완료되면 **다음**을 선택합니다.<br><br>![역할 ARN]({{site.baseurl}}/assets/img/create_role_3_attach.png)<br><br>역할에 이름과 설명을 입력한 다음 **역할 만들기**를 클릭합니다.<br><br>![역할 ARN]({{site.baseurl}}/assets/img/create_role_4_name.png)<br><br>

{: start="5"}
5\. 클라우드 데이터 수집 통합을 만드는 데 사용할 것이므로 방금 만든 역할의 ARN과 생성한 외부 ID를 기록해 두세요.  

## Braze에서 클라우드 데이터 수집 설정하기

1. 새 통합 서비스를 만들려면 **데이터 설정** > **클라우드 데이터 수집**으로 이동하여 **새 데이터 동기화 만들기**를 선택한 다음, 파일 소스 섹션에서 **S3 가져오기**를 선택합니다. 

2. AWS 설정 프로세스의 정보를 입력하여 새 동기화를 생성합니다. 다음을 지정합니다:
- 역할 ARN
- 외부 ID
- SQS URL(새 통합마다 고유해야 함)
- 버킷 이름
- 폴더 경로(선택 사항)
- 지역  

![]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3\. 통합에 이름을 지정하고 이 통합의 데이터 유형을 선택합니다. <br><br>![]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_2.png %})<br><br>

4. 액세스 또는 권한 문제로 인해 동기화가 중단되는 경우 알림을 받을 연락처 이메일을 추가하세요. 선택 사항으로 사용자 수준 오류 및 동기화 성공에 대한 알림을 설정합니다. <br><br> ![]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_3.png %})<br><br>

{: start="5"}
5\. 마지막으로 연결을 테스트하고 동기화를 저장합니다. <br><br>![]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})


## 필수 파일 형식

클라우드 데이터 수집은 JSON, CSV 및 Parquet 파일을 지원합니다. 각 파일에는 지원되는 식별자 열이 하나 이상 포함되어야 하며 페이로드 열은 JSON 문자열로 포함되어야 합니다. 

- 사용자 식별자. 소스 파일에는 하나 이상의 사용자 식별자 열 또는 키가 포함될 수 있습니다. 각 행에는 하나의 식별자만 포함되어야 하지만 소스 파일에는 여러 식별자 유형이 있을 수 있습니다. 
    - `EXTERNAL_ID` - 업데이트하려는 사용자를 식별합니다. 이 값은 Braze에서 사용하는 `external_id` 값과 일치해야 합니다. 
    - `ALIAS_NAME` 및 `ALIAS_LABEL` \- 이 두 열은 사용자 별칭 개체를 만듭니다. `alias_name`은 고유 식별자이고 `alias_label`은 별칭의 유형을 지정합니다. 사용자는 여러 레이블이 있는 여러 별칭을 가질 수 있지만 `alias_label`당 하나의 `alias_name`만 가질 수 있습니다.
    - `BRAZE_ID` - Braze 사용자 식별자입니다. 이것은 Braze SDK에 의해 생성되었으며, 새로운 사용자는 Braze ID를 통해 클라우드 데이터 수집을 사용하여 생성될 수 없습니다. 새 사용자를 만들려면 외부 사용자 ID 또는 사용자 별칭을 지정합니다.
    - `EMAIL` - 사용자의 이메일 주소. 동일한 이메일 주소를 가진 여러 프로필이 존재하는 경우, 가장 최근에 업데이트된 프로필이 업데이트 우선순위가 됩니다. 이메일과 전화번호를 모두 포함하면 이메일을 기본 식별자로 사용하겠습니다.
    - `PHONE` - 사용자의 전화번호입니다. 동일한 전화번호를 가진 여러 프로필이 존재하는 경우, 가장 최근에 업데이트된 프로필이 업데이트에 우선됩니다. 
- `PAYLOAD` - Braze에서 사용자에게 동기화하려는 필드의 JSON 문자열입니다.

{% alert note %}
데이터 웨어하우스 소스와 달리 `UPDATED_AT` 열은 필요하지 않으며 지원되지도 않습니다.
{% endalert %}

{% alert note %}
S3 소스 버킷에 추가된 파일은 512MB를 초과하지 않아야 합니다. 512MB보다 큰 파일은 오류가 발생하며 Braze에 동기화되지 않습니다.
{% endalert %}

{% tabs %}
{% tab JSON 속성 %}
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
{% tab JSON 사용자 지정 이벤트 %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
```  
{% alert important %}
소스 파일의 모든 줄에 유효한 JSON이 포함되어야 하며, 그렇지 않으면 파일이 건너뛰어집니다.
{% endalert %}
{% endtab %}
{% tab JSON 구매 이벤트 %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
```  
{% alert important %}
소스 파일의 모든 줄에 유효한 JSON이 포함되어야 하며, 그렇지 않으면 파일이 건너뛰어집니다.
{% endalert %}

{% endtab %}
{% tab CSV 속성 %}
``` csv  
external_id,payload
s3-qa-load-0-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""SNXIM"", ""age"": 54, ""subscriber"": true, ""retention"": {""previous_purchases"": 19, ""vip"": true}, ""last_visit"": ""2023-08-08T16:03:26.598806""}"
s3-qa-load-1-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""0J747"", ""age"": 73, ""subscriber"": false, ""retention"": {""previous_purchases"": 22, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598816""}"
s3-qa-load-2-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""EP1U0"", ""age"": 99, ""subscriber"": false, ""retention"": {""previous_purchases"": 23, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598822""}"
```
{% endtab %}
{% endtabs %}  

지원되는 모든 파일 형식의 예는 [braze-examples](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage)의 샘플 파일을 참조하세요.  
