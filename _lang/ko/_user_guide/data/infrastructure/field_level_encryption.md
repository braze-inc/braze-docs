---
nav_title: 식별자 필드 수준 암호화
article_title: 식별자 필드 수준 암호화
page_order: 2
alias: "/field_level_encryption/"
description: "이 참조 문서에서는 이메일 주소를 암호화하여 Braze에서 공유되는 개인 식별자 정보(PII)를 최소화하는 방법에 대해 설명합니다."
page_type: reference
---

# 식별자 필드 수준 암호화

> 식별자 필드 수준 암호화를 사용하면 AWS 키 관리 서비스(KMS)로 이메일 주소를 원활하게 암호화하여 Braze에서 공유되는 개인 식별 정보(PII)를 최소화할 수 있습니다. 암호화는 민감한 데이터를 읽을 수 없는 암호화된 정보인 암호 텍스트로 대체합니다.

{% alert important %}
식별자 필드 수준 암호화는 추가 기능으로 사용할 수 있습니다. 식별자 필드 수준 암호화를 시작하려면 Braze 계정 매니저에게 문의하세요.
{% endalert %}

## 작동 방식

이메일 주소는 반드시 해시 및 암호화를 거쳐야 Braze에 추가할 수 있습니다. 메시징이 전송되면 해독된 이메일 주소에 대해 AWS KMS로 호출이 이루어집니다. 다음으로, 해시된 이메일 주소가 전달 및 참여 이벤트의 메타데이터에 삽입되어 원래 사용자와 연결됩니다. 이것이 바로 Braze가 이메일 분석을 추적하는 방법입니다. Braze는 포함된 일반 텍스트 이메일 주소를 모두 삭제하고 사용자의 일반 텍스트 이메일 주소를 저장하지 않습니다.

## 전제 조건

식별자 필드 수준 암호화를 사용하려면 이메일 주소를 Braze로 보내기 **전에** 이메일 주소를 [암호화하고](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) [해시할](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html) 수 있는 AWS KMS에 대한 액세스 권한이 있어야 합니다. 

AWS 비밀 키 인증 방법을 설정하려면 다음 단계를 따르세요.

1. 액세스 키 ID와 비밀 액세스 키를 검색하려면 AWS 키 관리 서비스에 대한 권한 정책을 사용하여 AWS에서 [IAM 사용자 및 매니저 그룹을 만드세요](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-set-up.html#create-an-admin). IAM 사용자에게는 [kms:Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) 및 [kms:GenerateMac](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html) 권한이 있어야 합니다. 자세한 내용은 [AWS KMS 권한을](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) 참조하세요.
2. **사용자 보안 자격 증명 표시를** 선택하여 액세스 키 ID와 비밀 액세스 키를 공개합니다. AWS KMS 키를 연결할 때 입력해야 하므로 자격 증명을 어딘가에 기록해 두거나 **자격 증명 다운로드** 버튼을 선택합니다.
3. 다음 AWS 리전에서 KMS를 설정해야 합니다:
    - **Braze US 클러스터:** `us-east-1`
    - **Braze EU 클러스터:** `eu-central-1`
4. AWS 키 관리 서비스에서 두 개의 키를 만들고 IAM 사용자가 키 사용 권한에 추가되었는지 확인합니다:
    - **[암호화/복호화](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk):** **대칭** 키 유형과 키 **암호화 및 복호화** 사용을 선택합니다.
    - **[해시](https://docs.aws.amazon.com/kms/latest/developerguide/hmac-create-key.html):** **대칭** 키 유형과 **MAC** 키 사용량 **생성 및 확인을** 선택합니다. 주요 사양은 **HMAC_256**. 키를 생성한 후에는 Braze에 입력해야 하므로 HMAC 키 ID를 어딘가에 메모해 두세요.

\![]({% image_buster /assets/img/field_level_encryption_aws_prereq.png %})

## 1단계: AWS KMS 키 연결하기

Braze 대시보드에서 **데이터 설정** > **필드 수준 암호화로** 이동합니다. AWS KMS 설정의 경우 다음을 입력합니다:

- 액세스 키 ID
- 비밀 액세스 키
- HMAC 키 ID (저장 후 업데이트할 수 없음)

## 2단계: 암호화된 필드 선택

다음으로 **이메일 주소를** 선택하여 필드를 암호화합니다. 

필드에 대한 암호화가 켜져 있으면 해독된 필드로 되돌릴 수 없습니다. 즉, 암호화는 영구적인 설정입니다. 이메일 주소에 대한 암호화를 설정할 때는 워크스페이스에 이메일 주소를 가진 사용자가 없는지 확인하세요. 이렇게 하면 작업 공간에 대한 기능을 켤 때 일반 텍스트 이메일 주소가 Braze에 저장되지 않도록 할 수 있습니다.

\![]({% image_buster /assets/img/field_level_encryption.png %})

## 3단계: 사용자 가져오기 및 업데이트하기

식별자 필드 수준 암호화가 켜져 있는 경우, 이메일 주소를 해시하고 암호화한 후 Braze에 추가해야 합니다. 이메일 주소를 해시하기 전에 반드시 소문자로 입력하세요. 자세한 내용은 [사용자 속성 개체를](#user-attributes-object) 참조하세요.

Braze에서 이메일 주소를 업데이트할 때 `email` 이 포함된 곳에는 해시된 이메일 값을 사용해야 합니다. 여기에는 다음이 포함됩니다:

- REST 엔드포인트:
    - `/users/track`
    - `/campaigns/trigger/send`
    - `/canvas/trigger/send`
    - `/transactional/v1/campaigns/{campaign_id}/send`
- CSV를 통해 사용자 추가 또는 업데이트하기

{% alert note %}
이메일 주소로 새 사용자를 만들 때는 사용자의 암호화된 이메일 값과 함께 `email_encrypted` 을 추가해야 합니다. 그렇지 않으면 사용자가 생성되지 않습니다. 마찬가지로 이메일이 없는 기존 사용자에게 이메일 주소를 추가하는 경우 `email_encrypted` 을 추가해야 합니다. 그렇지 않으면 사용자가 업데이트되지 않습니다.
{% endalert %}

## 고려 사항

이러한 기능은 식별자 필드 수준 암호화에서는 지원되지 않습니다:

- 소프트웨어 개발 키트를 통한 이메일 주소 식별 및 캡처
- 인앱 메시지 이메일 캡처 양식
- 이메일 인사이트 사서함 공급자 차트를 포함한 수신자 도메인에 대한 보고
- 정규표현식으로 이메일 주소 필터링하기
- 오디언스 동기화
- Shopify 통합

### 사용자 속성 개체

`/users/track` 엔드포인트에서 식별자 필드 수준 암호화를 사용하는 경우 [사용자 속성 개체에]({{site.baseurl}}/api/objects_filters/user_attributes_object) 대한 이러한 필드 세부 정보에 유의하세요:

- `email` 필드는 이메일의 해시값이어야 합니다.
- `email_encrypted` 필드는 이메일의 암호화된 값이어야 합니다.

## 자주 묻는 질문

### 암호화와 해싱의 차이점은 무엇인가요?

암호화는 데이터를 암호화하고 해독할 수 있는 양방향 기능입니다. 동일한 일반 텍스트 값을 여러 번 암호화하는 경우 AWS의 암호화 알고리즘(AES-256-GCM)은 서로 다른 암호화 값을 생성합니다. 해싱은 일반 텍스트를 해독할 수 없는 방식으로 스크램블링하는 단방향 기능입니다. 해싱은 매번 동일한 값을 산출합니다. 이를 통해 동일한 이메일 주소를 공유하는 여러 사용자의 구독 상태 유지를 지원할 수 있습니다.

### 테스트 전송에 어떤 이메일 주소를 사용해야 하나요?

테스트 전송에서는 일반 텍스트 이메일 주소가 지원됩니다. 특정 사용자에게 이메일이 어떻게 표시되는지 확인하려면 다음과 같이 하세요:

1. **사용자로 메시지 미리 보기를** 선택합니다.
2. **테스트 보내기에서** **현재 미리 보기 사용자의 속성으로 수신자 속성 덮어쓰기를** 선택합니다.

{%raw%}
### 이 이메일 주소 Liquid `{{${email_address}}}` 를 Braze에 추가하면 어떻게 되나요?

Braze는 이메일을 보낼 때 일반 텍스트 이메일 주소를 렌더링합니다. 미리보기에서는 이메일의 암호화된 버전이 표시됩니다. 커스텀 원클릭 URL에서 사용자를 참조하는 경우 사용자의 외부 ID를 사용하는 것이 좋습니다.

`{{${email_address}}}` 는 현재 환경설정 센터 및 탈퇴 페이지에서 지원되지 않습니다.
{%endraw%}

### 커런츠에 어떤 이메일 주소가 표시되나요?

해시된 이메일 주소는 이메일 전달 및 참여 이벤트에 포함됩니다.

### 메시지 보관에 어떤 이메일 주소가 표시되나요?

일반 텍스트 이메일 주소는 메시징 보관에 포함됩니다. 이러한 이메일은 고객의 클라우드 스토리지 제공업체로 직접 전송되며 이메일 본문에 다른 고객 데이터가 포함될 수 있습니다.

### 식별자 필드 수준 암호화로 메일 수신 목록-수신 거부 기능을 구독 관리에 사용할 수 있나요?

아니요. 메일-목록-탈퇴를 사용하면 해독된 일반 텍스트 이메일 주소가 Braze로 전송됩니다. 식별자 필드 수준 암호화를 켜면 원클릭을 포함한 URL 기반 HTTP: 메서드를 지원합니다. 또한 이메일 본문에 원클릭 수신 거부 링크를 포함하는 것이 좋습니다.

### 식별자 필드 수준 암호화는 전화와 같은 다른 식별자를 지원하나요?

아니요. 현재 식별자 필드 수준 암호화는 이메일 주소에 대해서만 지원됩니다.
