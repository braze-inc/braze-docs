---
nav_title: Lexer
article_title: Lexer
description: "이 참조 문서에서는 마케터에게 고객 데이터를 제공하여 매출을 촉진하는 경험을 지원하는 고객 데이터 플랫폼인 Lexer와 Braze 간의 파트너십을 간략히 설명합니다."
alias: /partners/lexer/
page_type: partner
search_tag: Partner
---

# Lexer

> 소매업체를 위해 빌드된 고객 데이터 플랫폼인 [Lexer][6]를 통해 강력한 데이터 보강 기능을 가장 직관적인 툴 및 전문가 자문을 결합하여 향상된 고객 경험을 바탕으로 브랜드에서 매출 증대를 촉진할 수 있습니다.

_This integration is maintained by Lexer._

## 통합 정보

Braze와 Lexer의 통합을 통해 두 플랫폼에서 데이터를 동기화할 수 있습니다. Lexer 데이터를 사용하여 가치 있는 Braze 세그먼트를 생성하거나 기존 세그먼트를 Lexer로 가져와 인사이트를 확보하세요. 

## 전제 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| 파트너 계정 | 이 파트너십을 이용하려면 Lexer 계정이 필요합니다. |
| Braze REST API 키 | 모든 `user` 권한( `user.delete`) 및 `segment.list` 권한이 포함된 Braze REST API 키입니다. Lexer가 더 많은 Braze 오브젝트에 대한 지원을 추가함에 따라 권한 세트가 변경될 수 있으므로 지금 더 많은 권한을 부여하거나 향후에 이러한 권한을 업데이트할 수 있습니다.<br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/api/basics/#endpoints). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
| Amazon AWS S3 버킷 및 자격 증명 | 연동을 시작하기 전에 Lexer 허브에 연결된 AWS S3 버킷에 대한 액세스 자격 증명이 있어야 합니다(사용자가 만든 버킷일 수도 있고 Lexer가 대신 만들어서 관리하는 버킷일 수도 있습니다). 이 요구 사항에 대한 안내를 보려면 [Lexer](https://learn.lexer.io/docs/amazon-s3)를 방문하세요. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

Lexer에서 **관리 > 통합**으로 이동하여 **Braze** 타일을 선택한 다음, **Braze 통합**을 클릭합니다. 다음 정보를 입력합니다:
- **Braze REST 엔드포인트**
- **Braze REST API 키**
- **AWS 자격 증명**
  - **AWS S3 버킷 이름**
  - **AWS S3 [버킷 리전][4]**
  - **AWS S3 버킷 경로**: 이 경로는 [S3 버킷을 Braze에 연결할 때][5] 지정한 경로와 일치해야 합니다. Braze에 대해 아무것도 지정하지 않았다면 비워두어야 합니다.
  - **AWS S3 비밀 액세스 키**: 액세스 키 생성]에 대한 자세한 내용은 Amazon을 방문하세요][3].
- **Braze 내보내기 세그먼트 ID**: Lexer로 내보내려는 모든 사용자를 포함하여 Braze에서 생성한 세그먼트의 ID. Lexer로 내보내지 않으려는 사용자가 있는 경우 Braze에서 생성한 세그먼트에서 해당 사용자를 제외할 수 있습니다. 세그먼트 식별자를 찾으려면 Braze에서 원하는 세그먼트를 클릭하고 **세그먼트 API 식별자를** 찾습니다.

![][1]

### AWS S3 옵션 선택(Lexer 관리형 또는 자체 관리형)
Lexer 관리형 버킷을 사용하는 것이 Braze를 Lexer 허브에 연결하는 가장 선호되는 방법이며, 필요한 설정의 양을 줄일 수 있습니다. Lexer는 Braze를 구성하는 데 필요한 일회성 세부 정보를 제공합니다.

이미 S3 버킷을 Braze에 연결하여 다른 용도로 사용하고 있는 경우, 앞의 단계에 따라 이 자체 관리형 버킷에 대한 액세스 권한을 Lexer에 대신 제공해야 합니다.

이 통합은 기존 API 토큰과 비밀번호를 Lexer에 제공하여 Lexer가 사용자를 대신해 이러한 내보내기를 수행하도록 지원하는 방식으로 작동합니다. 또한 이러한 자격 증명과 S3 구성을 사용하여 Braze 데이터를 Lexer로 가져와 두 플랫폼에서 데이터를 자동으로 동기화합니다.

## Braze에 세그먼트 보내기

### 1단계: 활성화 만들기

Lexer Activate는 고객이 세그먼트에 진입하고 나갈 때 속성을 추가하거나 제거하여 Braze 프로필을 자동으로 업데이트합니다.

1. Lexer의 **Lexer 활성화**에서 **새 오디언스 활성화**를 클릭합니다.
2. 이 캠페인에 적합한 Braze 활성화를 선택합니다.
3. 세그먼트를 추가합니다.
4. 오디언스 이름을 업데이트하면 Braze에서 속성 값이 됩니다.
5. 이것이 바로 Braze에서 업데이트할 사용자 지정 속성입니다. 업데이트하려면 [Lexer 지원팀에](support@lexer.io) 문의하세요.
6. 대부분의 사례에서 목록을 유지하려는 경우 적절한 목록 작업을 확인합니다.
7. 이용 약관을 검토하고 **오디언스 전송**을 클릭합니다.

![][7]

### 2단계: 활성화 확인

활성화에서 활성화가 전송된 것으로 확인되면 Braze에서 레코드가 업데이트되기 시작하는 것을 확인할 수 있습니다. 회원님의 프로필은 Lexer로부터 확인 이메일을 받을 때까지 Braze에서 완전히 업데이트되지 않습니다.

### 3단계: 브레이즈 세그먼트 만들기

Braze에서는 이제 Lexer의 오디언스 이름이 `lexer_audience` 커스텀 속성의 값으로 표시됩니다. Braze에서는 속성당 100개의 값으로 제한됩니다.

세그먼트를 생성하려면 **세그먼트 > + 세그먼트 생성**으로 이동하여 필터로 **커스텀 속성**을 선택합니다. 그런 다음, `lexer_audience`를 속성으로 선택하고 원하는 Lexer 오디언스 이름을 선택합니다. 완료되면 오디언스를 **저장합니다**.

이제 새로 생성한 세그먼트를 향후 Braze 캠페인과 캔버스에 추가하여 이러한 최종 사용자를 타겟팅할 수 있습니다.


[1]: {% image_buster /assets/img/lexer/braze_integrate_screen.png %}
[2]: {{site.baseurl}}/api/basics/#company-secret-explanation
[3]:https://aws.amazon.com/premiumsupport/knowledge-center/create-access-key/
[4]:https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html
[5]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3/
[6]:https://lexer.io/
[7]: {% image_buster /assets/img/lexer/lexer.png %}
