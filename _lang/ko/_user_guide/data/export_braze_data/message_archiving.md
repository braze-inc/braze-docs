---
nav_title: 메시지 아카이브
article_title: 메시지 아카이브
alias: "/message_archiving/"
page_order: 0
page_type: reference
description: "이 참조 문서는 메시지 보관, 사용자가 보낸 메시지의 사본을 저장할 수 있는 기능을 다룹니다."

---

# 메시지 보관

> 메시지 보관은 보관 또는 준수 목적으로 사용자에게 전송된 메시지의 사본을 AWS S3 버킷, Azure Blob Storage 컨테이너 또는 Google Cloud Storage 버킷에 저장할 수 있게 해줍니다. <br><br> 이 문서에서는 메시지 보관, JSON 페이로드 참조 및 자주 묻는 질문을 설정하는 방법에 대해 설명합니다.

메시지 보관은 추가 기능으로 제공됩니다. 메시지 보관을 시작하려면 Braze 고객 성공 매니저에게 문의하십시오.

## 작동 방식

When this feature is turned on, if you have connected a cloud storage bucket to Braze and marked it as the default data export destination, Braze will write a gzipped JSON file to your cloud storage bucket for each message sent to a user through your selected channels (email, SMS/MMS, or push). 

이 파일은 [파일 참조](#file-references)에 정의된 필드를 포함하고 사용자에게 전송된 최종 템플릿 메시지를 반영합니다. 캠페인에 정의된 모든 템플릿 값(예: {% raw %}`{{${first_name}}}`{% endraw %})은 사용자의 프로필 정보에 따라 받은 최종 값을 표시합니다. 이를 통해 규정 준수, 감사 또는 고객 지원 요건을 충족하기 위해 보낸 메시지의 사본을 보관할 수 있습니다.

여러 클라우드 스토리지 제공업체에 대한 자격 증명을 설정한 경우, 메시지 보관은 기본 데이터 내보내기 대상으로 명시적으로 표시된 제공업체에만 내보내집니다. 명시적인 기본값이 제공되지 않고 AWS S3 버킷이 연결된 경우, 메시지 보관은 해당 버킷에 업로드됩니다.

{% alert important %}
Turning on this feature will impact the delivery speed of your messages, as the file upload is performed immediately before the message is sent to maintain accuracy. The latency introduced by message archiving will depend on the cloud storage provider and the throughput and size of the saved documents.
{% endalert %}

JSON은 다음 키 구조를 사용하여 스토리지 버킷에 저장됩니다:

`sent_messages/{channel, one of: email, push, sms}/{MD5 digest of downcased: email address, push token, or E.164 phone number}/{campaign or Canvas step API ID}/{dispatch ID}.json.gz`

예시 파일은 다음과 같이 보일 수 있습니다:

`sent_messages/email/819baa08d8d7e77e19d4666f5fc6050b/ee965cb2-8934-4b0a-acf1-91c899c2f915/651fd10b282850b39e1169c13975234b.json.gz`

{% alert note %}
The MD5 digest can only be calculated using a known downcased email address, push token, or E.164 phone number. A known MD5 digest can't be reversed to obtain the downcased email address, push token, or E.164 phone number.
{% endalert %}

{% alert tip %}
**푸시 토큰을 버킷에서 찾는 데 문제가 있습니까?**<br>
Braze는 푸시 토큰을 해시하기 전에 소문자로 변환합니다. 이로 인해 키 경로에서 해시 `32b802170652af2b5624b695f34de089`와 함께 푸시 토큰 `Test_Push_Token12345`가 `test_push_token12345`으로 소문자로 변환됩니다.
{% endalert %}

## 메시지 보관 설정

이 섹션에서는 워크스페이스에 대한 메시지 보관 설정 방법을 안내합니다. 진행하기 전에 회사에서 메시지 보관을 구매하고 활성화했는지 확인하십시오.

### 1단계: 클라우드 스토리지 버킷을 연결하십시오

아직 하지 않았다면, 클라우드 스토리지 버킷을 Braze에 연결하세요. For steps, refer to our partner documentation on [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/), [Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/) or [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/).

### 2단계: 메시지 보관을 위한 채널 선택

**메시지** 보관 설정 페이지는 어떤 채널이 전송된 메시지의 사본을 클라우드 스토리지 버킷에 저장할지를 제어합니다.

채널을 선택하려면:

1. **설정** > **메시지 보관**.
2. 채널을 선택하세요.
3. **변경 사항 저장**을 선택합니다.

![메시지 보관 페이지에는 선택할 수 있는 세 가지 채널이 있습니다: Email, Push, and SMS.]({% image_buster /assets/img/message_archiving_settings.png %})

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

이 페이로드에서 언급된 `extras` 필드는 이메일 작성 시 **이메일 추가 항목** 필드에 추가된 키-값 페어에서 가져온 것입니다. 커런츠로 데이터를 보내려면 [메시지 추가 정보]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/)를 참조하세요.

![]({% image_buster /assets/img_archive/email_extras.png %}){: style="max-width:60%" }

{% endtab %}
{% tab SMS/MMS %}

```json
{
  "version" : 1 //numerical version of the json structure
  "to": PhoneNumber, ("+15555555555"),
  "body": Body ("Hi there!"),
  "subscription_group": SubscriptionGroupExternalId,
  "provider": StringOfProviderName,
  "media_urls": ArrayOfString, // indicates a message is MMS
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
  "platform": one of "android_push" | "ios_push" | "kindle_push" | "web_push",
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
  "canvas_name": String, // will only be available if the message is from a Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

{% endtab %}
{% endtabs %}

## 자주 묻는 질문

### 페이로드에 포함되지 않은 템플릿은 무엇입니까?

메시지가 Braze를 떠난 후 수정한 내용은 클라우드 저장소 버킷에 저장된 파일에 반영되지 않습니다. 여기에는 클릭 추적을 위한 링크 래핑 및 추적 픽셀 삽입과 같은 메일 전송 파트너의 수정 사항이 포함됩니다.

### 캠페인 경로에서 "연관되지 않은" 값 아래의 메시지는 무엇입니까?

메시지가 캠페인 또는 캔버스 외부로 전송될 때, 파일 이름의 캠페인 ID는 "연결되지 않음"이 됩니다. This will happen when you send test messages from the dashboard, when Braze sends SMS/MMS auto-responses, or when messages sent through the API do not specify a campaign ID.

### 이 발송에 대한 추가 정보를 어떻게 찾을 수 있습니까?

`external_id` 또는 `dispatch_id` 을 `user_id` 과 함께 사용하여 템플릿 메시지를 커런츠 데이터와 상호 참조하여 전송된 타임스탬프, 사용자가 메시지를 열었는지 또는 클릭했는지 여부 등 자세한 정보를 확인할 수 있습니다.

### 재시도는 어떻게 처리됩니까?

클라우드 스토리지 버킷에 연결할 수 없는 경우, Braze는 [백오프 지터를](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/#Jitter) 사용하여 최대 세 번 재시도합니다. AWS S3 사용량 제한 재시도는 Braze에 의해 자동으로 처리됩니다.

### 내 자격 증명이 유효하지 않으면 어떻게 되나요?

클라우드 저장소 자격 증명이 어느 시점에서든 유효하지 않은 경우, Braze는 클라우드 저장소 버킷에 메시지를 저장할 수 없으며 해당 메시지는 손실됩니다. 자격 증명 문제에 대한 알림을 받을 수 있도록 Amazon Web Services, Google Cloud Services 또는 Azure(Microsoft 클라우드 서비스)에 대한 [알림 환경설정을]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/notification_preferences/) 구성하는 것이 좋습니다.

### 아카이브 파일의 `sent_at` 타임스탬프가 Currents에서 전송된 타임스탬프와 약간 다른 이유는 무엇인가요?

렌더링된 사본은 사용자에게 메시지를 보내기 직전에 업로드됩니다. 클라우드 스토리지 업로드 시간으로 인해 렌더링된 사본의 `sent_at` 타임스탬프와 실제 전송이 발생한 시간 사이에 몇 초의 지연이 발생할 수 있습니다.

### Can I create a new bucket specifically for message archiving while keeping the current bucket used for Currents data?

No. If you're interested in creating these specific buckets, submit [product feedback]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).

### Is archived data written to a dedicated folder in an existing bucket, similar to how Currents data exports are structured?

The data is written to a `sent_messages` section of the bucket. Refer to [How it works](#how-it-works) for more details.

