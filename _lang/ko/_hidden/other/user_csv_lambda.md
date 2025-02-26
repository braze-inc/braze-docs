---
nav_title: 사용자 속성 CSV 람다 프로세스
permalink: /user_csv_lambda/
description: "다음 문서에서는 사용자 추적 Braze 엔드포인트를 통해 CSV 파일의 사용자 속성 데이터를 Braze에 직접 게시하는 Lambda 프로세스를 쉽게 배포할 수 있는 서버리스 애플리케이션에 대해 설명합니다."
hidden: true
---

# 사용자 속성 CSV를 Braze로 가져오기

> 다음 문서에서는 [사용자 추적 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)를 통해 CSV 파일의 사용자 속성 데이터를 Braze에 직접 게시하는 람다 프로세스를 쉽게 배포할 수 있는 서버리스 애플리케이션을 소개합니다. 이 애플리케이션 통합은 Amperity 파트너와 함께 테스트를 거쳤으며 [GitHub](https://github.com/braze-inc/growth-shares-lambda-user-csv-import)에서 확인할 수 있습니다.

이 프로세스는 구성된 AWS S3 버킷에 CSV 파일을 업로드하는 즉시 시작됩니다. 대용량 파일과 업로드를 처리할 수 있지만 Lambda의 시간 제한으로 인해 10분 후에 기능 실행이 중지됩니다. 그러면 이 프로세스가 다른 Lambda 인스턴스를 실행하여 파일의 나머지 부분 처리를 완료합니다. 함수 타이밍에 대한 자세한 내용은 [예상 실행 시간](#estimated-execution-times)을 확인하세요.

{% alert important %}
이 애플리케이션은 Braze Growth 부서에서 구축하고 유지 관리합니다. 이 애플리케이션의 제작자에게 연락하고 싶은 경우 [GitHub 이슈](https://github.com/braze-inc/growth-shares-lambda-user-csv-import/issues)를 생성하여 피드백이나 문제가 발생할 수 있는 사항을 문의하세요.
{% endalert %}

#### CSV 사용자 속성

업데이트할 사용자 속성은 다음 `.csv` 형식으로 예상됩니다:

```
external_id,attr_1,...,attr_n
userID,value_1,...,value_n
```

첫 번째 열에는 업데이트할 사용자의 외부 ID를 지정해야 하며 다음 열에는 속성 이름과 값을 지정해야 합니다. 지정하는 속성의 수는 다양할 수 있습니다. 처리할 CSV 파일이 이 형식을 따르지 않으면 함수가 실패합니다.  

**CSV 파일 예제:**

```
external_id,Loyalty Points,Last Brand Purchased
abc123,1982,Solomon
def456,578,Hunter-Hayes
```

#### CSV 처리

배열의 모든 값(예: `"['Value1', 'Value2']"`)은 자동으로 구조가 파괴되어 배열의 문자열 표현이 아닌 배열로 API에 전송됩니다.

## 요구 사항

이 람다 함수를 성공적으로 실행하려면 다음이 필요합니다:
- S3 및 Lambda 서비스를 사용하기 위한 **AWS 계정** 
- Braze 서버에 연결하기 위한 Braze **API URL** 
- `/users/track` 엔드포인트에 요청을 보낼 수 있는 **Braze API 키** 
- 업데이트할 사용자 외부 ID 및 속성이 포함된 **CSV 파일** 

{% tabs %}
{% tab API URL %}

API URL 또는 REST 엔드포인트는 Braze API 설명서와 대시보드를 통해 찾을 수 있습니다.

- **API 문서**<br>[API 설명서]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances)에 따라 Braze 인스턴스 URL을 REST 엔드포인트 URL과 일치시키기만 하면 됩니다. 예를 들어 대시보드에 `dashboard-01.braze.com/` URL이 표시되는 경우 REST 엔드포인트는 `https://rest.iad-01.braze.com`이 됩니다. <br><br>
- **대시보드**<br>**설정 관리** 페이지로 이동하여 SDK 엔드포인트를 찾습니다. `sdk`를 `rest`로 바꾸어 REST 엔드포인트를 가져옵니다. 예를 들어 `sdk.iad-01.braze.com`이 표시되는 경우 API URL은 `rest.iad-01.braze.com`입니다

{% endtab %}
{% tab API 키 %}

Braze 서버에 연결하려면 API 키가 필요합니다. 이 고유 식별자를 통해 Braze는 회원님의 신원을 확인하고 데이터를 업로드할 수 있습니다. 

API 키를 받으려면 **설정** > **API 키로** 이동합니다.

{% alert note %}
[이전 탐색]({{site.baseurl}}/navigation)을 사용하는 경우 **개발자 콘솔** > **API 설정**에서 API 키를 찾을 수 있습니다.
{% endalert %}

`/users/track` 엔드포인트에 게시할 수 있는 권한이 있는 API 키가 필요합니다. API 키 중 하나가 해당 엔드포인트를 지원하는 것을 알고 있다면 해당 키를 사용할 수 있습니다. 

새로 만들려면 **새 API 키 만들기**를 클릭합니다. 그런 다음 API 키의 이름을 지정하고 **사용자 데이터** 엔드포인트 그룹의 **users.track**을 선택한 다음 **API 키 저장**을 클릭합니다.

{% endtab %}
{% endtabs %}

## 사용 지침

##### 개요
1. AWS 서버리스 애플리케이션 리포지토리에서 공개적으로 사용 가능한 Braze의 CSV 처리 람다를 배포하세요.
2. 새로 만든 S3 버킷에 사용자 속성이 포함된 CSV 파일을 드롭합니다.
3. 사용자는 자동으로 Braze로 가져옵니다.

#### 배포

사용자 속성 CSV 파일 처리를 시작하려면 처리를 처리할 서버리스 애플리케이션을 배포해야 합니다. 이 애플리케이션은 성공적인 배포를 위해 다음 리소스를 자동으로 생성합니다:

- 람다 함수
- 람다 프로세스가 읽을 수 있는 CSV 파일에 대한 S3 버킷_(참고: 이 람다 기능은 `.csv` 확장자 파일에 대해서만 알림을 수신합니다_)
- S3 버킷을 생성할 수 있는 역할
- Lambda가 새 버킷에서 S3 업로드 이벤트를 수신하도록 허용하는 정책

[애플리케이션](https://console.aws.amazon.com/lambda/home?region=us-east-1#/create/app?applicationId=arn:aws:serverlessrepo:us-east-1:585170621372:applications/braze-user-attribute-import)에 대한 직접 링크를 따라가거나 [AWS 서버리스 애플리케이션 리포지토리를](https://serverlessrepo.aws.amazon.com/applications) 열고 "braze-user-attribute-import"를 검색하세요. 이 애플리케이션을 보려면 `Show apps that create custom IAM roles and resource policies` 확인란을 선택해야 합니다. 애플리케이션은 람다가 새로 생성된 S3 버킷에서 읽을 수 있는 정책을 생성합니다.

**배포**를 클릭하고 AWS가 필요한 모든 리소스를 생성하도록 합니다.

배포를 지켜보고 스택(즉, 필요한 모든 리소스)이 [CloudFormation에서](https://console.aws.amazon.com/cloudformation/) 생성되고 있는지 확인할 수 있습니다. "serverlessrepo-braze-user-attribute-import"라는 스택을 찾습니다. **상태**가 `CREATE_COMPLETE`로 바뀌면 기능을 사용할 준비가 된 것입니다. 스택을 클릭하고 **리소스를** 열어 다양한 리소스가 생성되는 것을 볼 수 있습니다.

다음 리소스가 생성되었습니다:

- [S3 버킷](https://s3.console.aws.amazon.com/s3/) - `braze-user-csv-import-aaa123`이라는 이름의 버킷, 여기서 `aaa123`은 무작위로 생성된 문자열입니다.
- [람다 함수](https://console.aws.amazon.com/lambda/) \- 람다 함수의 이름은 `braze-user-attribute-import`입니다
- [IAM 역할](https://console.aws.amazon.com/iam/) \- 람다가 S3에서 읽고 함수 출력을 기록하도록 허용하는 `braze-user-csv-import-BrazeUserCSVImportRole`이라는 정책

#### 실행

함수를 실행하려면 새로 만든 S3 버킷에 사용자 속성 CSV 파일을 드롭합니다.

## 모니터링 및 로깅

함수가 성공적으로 실행되는지 확인하려면 함수의 실행 로그를 읽으면 됩니다. 콘솔의 람다 목록에서 Braze 사용자 CSV 가져오기 기능을 열고 **모니터**로 이동합니다. 여기에서 함수의 실행 내역을 확인할 수 있습니다. 출력을 읽으려면 **CloudWatch에서 로그 보기**를 클릭합니다. 확인하려는 람다 실행 이벤트를 선택합니다.

## 예상 실행 시간
_2048MB 람다 함수_

| 행 수 | 실행 시간 |
| --------- | ---------- |
| 10k       | 3s         |
| 100k      | 30s        |
| 1M        | 5분      |
| 5M        | 30분     |

## 기존 기능 업데이트하기

이미 애플리케이션을 배포했고 리포지토리에서 새 버전을 사용할 수 있는 경우 처음 배포하는 것처럼 기능을 다시 배포하여 업데이트할 수 있습니다. 즉, Braze API 키와 Braze API URL을 다시 전달해야 합니다. 업데이트는 기능 코드만 덮어씁니다. S3 버킷과 같은 다른 기존 리소스는 수정하거나 삭제하지 않습니다.

## 치명적인 오류

파일을 더 이상 처리할 수 없는 예기치 않은 오류가 발생하는 경우, 프로그램이 파일 처리를 중지한 지점부터 람다를 다시 시작하는 데 사용할 수 있는 이벤트가 기록됩니다( [모니터링 및 로깅](#monitoring-and-logging)에 설명된 CloudWatch를 통해 액세스할 수 있음). 데이터 포인트를 저장하기 위해 동일한 데이터를 다시 가져오지 않는 것이 중요합니다. 이 작업에 대한 지침은 [GitHub 리포지토리](https://github.com/braze-inc/growth-shares-lambda-user-csv-import#fatal-error)에서 찾을 수 있습니다.

{% alert important %}
[심각한오류](https://github.com/braze-inc/growth-shares-lambda-user-csv-import#fatal-error) 또는 [람다 구성](https://github.com/braze-inc/growth-shares-lambda-user-csv-import#lambda-configuration)을 처리하는 방법에 대해 자세히 알아보려면 GitHub 리포지토리를 방문하세요.
{% endalert%}