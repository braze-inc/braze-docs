---
nav_title: 메시지 아카이브
article_title: 메시지 아카이브
alias: "/message_archiving/"
page_order: 0
page_type: reference
description: "이 참조 문서는 메시지 보관, 사용자가 보낸 메시지의 사본을 저장할 수 있는 기능을 다룹니다."

---

# 메시지 보관

> 메시지 보관은 보관 또는 준수 목적으로 사용자에게 전송된 메시지의 사본을 AWS S3 버킷, Azure Blob Storage 컨테이너 또는 Google Cloud Storage 버킷에 저장할 수 있게 해줍니다.

메시지 보관은 추가 기능으로 제공됩니다. 메시지 보관을 시작하려면 Braze 고객 성공 매니저에게 문의하십시오.

## 개요

이 기능이 켜지면 클라우드 스토리지 버킷을 Braze에 연결하고 기본값 데이터 내보내기 대상으로 지정한 경우, Braze는 선택한 채널(이메일, SMS 또는 푸시)을 통해 사용자에게 전송된 각 메시지에 대해 gzipped JSON 파일을 클라우드 스토리지 버킷에 작성합니다. 

이 파일은 [파일 참조](#file-references)에 정의된 필드를 포함하고 사용자에게 전송된 최종 템플릿 메시지를 반영합니다. 캠페인에 정의된 모든 템플릿 값(예: {% raw %}`{{${first_name}}}`{% endraw %})은 사용자의 프로필 정보에 따라 받은 최종 값을 표시합니다. 이렇게 하면 준수, 감사 또는 고객 지원 요구 사항을 충족하기 위해 보낸 메시지의 사본을 보관할 수 있습니다.

여러 클라우드 스토리지 제공업체에 대한 자격 증명을 설정한 경우, 메시지 보관은 기본 데이터 내보내기 대상으로 명시적으로 표시된 제공업체에만 내보내집니다. 명시적인 기본값이 제공되지 않고 AWS S3 버킷이 연결된 경우, 메시지 보관은 해당 버킷에 업로드됩니다.

{% alert important %}
이 기능을 켜면 파일 업로드가 메시지 전송 직전에 수행되어 정확성을 보장하므로 메시지 전달 속도에 영향을 미칩니다. 이로 인해 Braze 전송 파이프라인에 추가 지연이 발생하여 전송 속도에 영향을 미칩니다.
{% endalert %}

JSON은 다음 키 구조를 사용하여 스토리지 버킷에 저장됩니다:

`sent_messages/channel/(one of: md5, e164 phone number, email, or push token)/(campaign_id OR canvas_step_id)/DispatchId.json.gz`

예시 파일은 다음과 같이 보일 수 있습니다:

`sent_messages/email/819baa08d8d7e77e19d4666f5fc6050b/ee965cb2-8934-4b0a-acf1-91c899c2f915/651fd10b282850b39e1169c13975234b.json.gz`

{% alert note %}
**푸시 토큰을 버킷에서 찾는 데 문제가 있습니까?**<br>
Braze는 푸시 토큰을 해시하기 전에 소문자로 변환합니다. 이로 인해 키 경로에서 해시 `32b802170652af2b5624b695f34de089`와 함께 푸시 토큰 `Test_Push_Token12345`이 `test_push_token12345`(으)로 소문자로 변환됩니다.
{% endalert %}

## 메시지 보관 설정

이 섹션에서는 작업 공간에 대한 메시지 보관 설정 방법을 설명합니다. 진행하기 전에 회사에서 메시지 보관을 구매하고 활성화했는지 확인하십시오.

### 1단계: 클라우드 스토리지 버킷을 연결하십시오

아직 하지 않았다면, 클라우드 스토리지 버킷을 Braze에 연결하세요. 단계는 [Amazon S3]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3/), [Azure Blob Storage]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/microsoft_azure_blob_storage_for_currents/) 또는 [Google Cloud Storage]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/google_cloud_storage_for_currents/)에 대한 파트너 설명서를 참조하십시오.

### 2단계: 메시지 보관을 위한 채널 선택

**메시지** 보관 설정 페이지는 어떤 채널이 전송된 메시지의 사본을 클라우드 스토리지 버킷에 저장할지를 제어합니다.

채널을 선택하려면:

1. **설정** > **메시지 보관**.
2. 채널을 선택하세요.
3. 클릭 **저장 changes**.

![메시지 보관 페이지에는 선택할 수 있는 세 가지 채널이 있습니다: 이메일, 푸시, 그리고 SMS.][1]

{% alert note %}
**메시지 보관**이 **설정**에 표시되지 않으면 회사에서 메시지 보관을 구매하고 활성화했는지 확인하세요.
{% endalert %}

## 파일 참조

다음은 메시지가 전송될 때마다 클라우드 스토리지 버킷에 전달되는 JSON 페이로드의 참조입니다. 우리의 코드 예제 저장소에서 [메시지 아카이브 샘플 파일](https://github.com/braze-inc/braze-examples/tree/main/message-archiving)를 참조하십시오.

{% tabs %}
{% tab 이메일 %}

```json
{
  "version" : 1, //numerical version of the json structure
  "to": ToAddress, ("customer@example.com")
  "subject": SubjectLine ("20% off coupon inside!"),
  "from_name": DisplayName ("Braze"),
  "from_address": FromAddress ("no-reply@braze.com"),
  "html_body": HtmlBody,
  "plaintext_body": PlainTextBody,
  "amp_body": AMPEmailBody,
  "extras": Extra hash—for SendGrid users, this will be passed to SendGrid as Unique Arguments,
  "headers": HashOfHeaders,
  "sent_at": UnixTimestamp,
  "dispatch_id": DispatchIdFromBraze,
  "campaign_id": CampaignApiId, // may not be available
  "canvas_id": CanvasApiId, // may not be available
  "canvas_step_id": CanvasStepApiId, // may not be available
  "canvas_variation_id" : CanvasVariationApiId, // may not be available
  "message_variation_id": MessageVariationApiId, // may not be available,
  "attachments": Array of JSON Objects containing 'bytes' and 'file_name', // may not be available
  "user_id": String,
  "campaign_name": String, // will only be available if the message is from a campaign
  "canvas_name": String, // will only be available if the message is a from Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

이 페이로드에서 언급된 `extras` 필드는 이메일 작성 시 **이메일 추가 항목** 필드에 추가된 키-값 쌍에서 가져온 것입니다. 커런츠로 데이터를 보내려면 [메시지 추가 정보]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/)를 참조하세요.

![]({% image_buster /assets/img_archive/email_extras.png %}){: style="max-width:60%" }

{% endtab %}
{% tab 문자 메시지 %}

```json
{
  "version" : 1 //numerical version of the json structure
  "to": PhoneNumber, ("+15555555555"),
  "body": Body ("Hi there!"),
  "subscription_group": SubscriptionGroupExternalId,
  "provider": StringOfProviderName,
  "media_urls": ArrayOfString,
  "sent_at": UnixTimestamp,
  "dispatch_id": DispatchIdFromBraze,
  "campaign_id": CampaignApiId, // may not be available
  "canvas_id": CanvasApiId, // may not be available
  "canvas_step_id": CanvasStepApiId, // may not be available
  "canvas_variation_id" : CanvasVariationApiId, // may not be available
  "message_variation_id": MessagVariationApiId, // may not be available
  "user_id": String,
  "campaign_name": String, // will only be available if the message is from a campaign
  "canvas_name": String, // will only be available if the message is a from Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

{% endtab %}
{% tab 푸시 %}

```json
{
  "version" : 1, //numerical version of the json structure
  "to": PushToken,
  "payload": JsonOfEntirePushPayload,
  "platform": ios/android/web/kindle,
  "app_id": ApiKeyOfApp,
  "sent_at": UnixTimestamp,
  "dispatch_id": DispatchIdFromBraze,
  "campaign_id": CampaignApiId, // may not be available
  "canvas_id": CanvasApiApiId, // may not be available
  "canvas_step_id": CanvasStepApiId, // may not be available
  "canvas_variation_id" : CanvasVariationApiId, // may not be available
  "message_variation_id": MessagVariationApiId, // may not be available
  "user_id": String,
  "campaign_name": String, // will only be available if the message is from a campaign
  "canvas_name": String, // will only be available if the message is a from Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

{% endtab %}
{% endtabs %}

## 자주 묻는 질문

### 페이로드에 포함되지 않은 템플릿은 무엇입니까?

메시지를 Braze에서 보낸 후에 수행된 수정 사항은 클라우드 스토리지 버킷에 저장된 파일에 반영되지 않습니다. 이것은 클릭 추적을 위해 링크를 래핑하고 추적 픽셀을 삽입하는 것과 같은, 우리의 메일 전달 파트너가 하는 수정 사항을 포함할 것입니다.

### 캠페인 경로에서 "연관되지 않은" 값 아래의 메시지는 무엇입니까?

메시지가 캠페인 또는 캔버스 외부로 전송될 때, 파일 이름의 캠페인 ID는 "연결되지 않음"이 됩니다. 대시보드에서 테스트 메시지를 보낼 때, Braze가 SMS 자동 응답을 보낼 때, 또는 API를 통해 보낸 메시지가 캠페인 ID를 지정하지 않을 때 발생합니다.

### 이 발송에 대한 추가 정보를 어떻게 찾을 수 있습니까?

`external_id` 또는 `dispatch_id`를 `user_id`와 함께 사용하여 템플릿 메시지를 커런츠 데이터와 교차 참조하여 전달된 타임스탬프, 사용자가 메시지를 열었는지 또는 클릭했는지 여부 등과 같은 추가 정보를 찾을 수 있습니다.

### 재시도는 어떻게 처리됩니까?

클라우드 스토리지 버킷에 접근할 수 없는 경우 Braze는 [백오프 지터](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/#Jitter)로 최대 세 번까지 재시도합니다. AWS S3 속도 제한 재시도는 Braze에 의해 자동으로 처리됩니다.

### 내 자격 증명이 유효하지 않으면 어떻게 되나요?

클라우드 스토리지 자격 증명이 언제든지 유효하지 않게 되면 Braze는 클라우드 스토리지 버킷에 메시지를 저장할 수 없으며, 해당 메시지는 손실됩니다. [AWS 자격 증명 오류 알림]({{site.baseurl}}/user_guide/administrative/company_settings/notification_preferences) 환경설정을 구성하여 자격 증명 문제에 대한 경고를 받을 수 있도록 권장합니다.

### 왜 내 아카이브 파일의 "sent_at" 타임스탬프가 커런츠에서 보낸 타임스탬프와 약간 다른가요?

렌더링된 사본은 메시지를 최종 사용자에게 보내기 전에 즉시 업로드됩니다. 클라우드 스토리지 업로드 시간 때문에 렌더링된 사본의 "sent_at" 타임스탬프와 실제 전송 시간 사이에 몇 초의 지연이 있을 수 있습니다.

[1]: {% image_buster /assets/img/message_archiving_settings.png %}
