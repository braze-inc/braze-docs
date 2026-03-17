---
nav_title: 메시지 보관
article_title: 메시지 아카이브
alias: "/message_archiving/"
page_order: 0
page_type: reference
description: "이 참조 문서는 메시지 보관, 사용자가 보낸 메시지의 사본을 저장할 수 있는 기능을 다룹니다."

---

# 메시지 보관

> 메시지 보관 기능을 사용하면 보관 또는 규정 준수 목적으로 사용자에게 전송된 메시지의 사본을 AWS S3 버킷, Azure Blob Storage 컨테이너 또는 Google Cloud Storage 버킷에 저장할 수 있습니다. <br><br> 본 문서에서는 메시지 아카이빙 설정 방법, JSON 페이로드 참조 및 자주 묻는 질문을 다룹니다.

메시지 보관은 추가 기능으로 제공됩니다. 메시지 아카이빙을 시작하려면 Braze 고객 성공 매니저에게 문의하십시오.

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

{% alert note %}
메시지 아카이빙을 위해 커런츠를 설정할 필요가 없으므로, 파트너 설명서의 해당 전제 조건은 건너뛸 수 있습니다.
{% endalert %}

### 2단계: 메시지 보관을 위한 채널 선택

**메시지** 보관 설정 페이지는 어떤 채널이 전송된 메시지의 사본을 클라우드 스토리지 버킷에 저장할지를 제어합니다.

채널을 선택하려면:

1. **설정** > **메시지 보관**.
2. 채널을 선택하세요.
3. **변경 사항 저장**을 선택합니다.

![메시지 보관 페이지에는 선택할 수 있는 세 가지 채널이 있습니다: 바로 이메일, 푸시, 그리고 SMS입니다.]({% image_buster /assets/img/message_archiving_settings.png %})

{% alert note %}
**메시지 보관**이 **설정**에 표시되지 않으면 회사에서 메시지 보관을 구매하고 활성화했는지 확인하세요.
{% endalert %}

## 파일 참조

다음은 메시지가 전송될 때마다 클라우드 스토리지 버킷으로 전달되는 JSON 페이로드에 대한 참조입니다. 우리의 코드 예제 저장소에서 [메시지 아카이브 샘플 파일](https://github.com/braze-inc/braze-examples/tree/main/message-archiving)를 참조하십시오.

{% tabs %}
{% tab Email %}

```json
{
  "version": 1, //numerical version of the JSON structure
  "to": ToAddress, ("customer@example.com")
  "subject": SubjectLine ("20% off coupon inside!"),
  "from_name": DisplayName ("Braze"),
  "from_address": FromAddress ("no-reply@braze.com"),
  "html_body": HtmlBody,
  "plaintext_body": PlainTextBody,
  "amp_body": AMPEmailBody,
  "extras": Hash of key-value pairs from Email Extras configured in the email editor,
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
  "canvas_name": String, // will only be available if the message is from Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

이`extras`필드는 HTML 편집기에서 이메일을 작성할 때 **'이메일 추가** 정보' 필드에 구성된 키-값 페어를 포함합니다. 이메일 추가 기능은 모든 이메일 서비스 제공업체(SendGrid 및 Sparkpost 포함)에서 작동하며, 사용 중인 제공업체와 관계없이 보관된 메시지에 포함됩니다. 이메일 추가 기능 설정에 대한 자세한 내용은 [이메일 캠페인 생성을]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#adding-email-extras) 참조하십시오. 커런츠로 데이터를 보내려면 [메시지 추가 정보]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/)를 참조하세요.

![]({% image_buster /assets/img_archive/email_extras.png %}){: style="max-width:60%" }

{% endtab %}
{% tab SMS/MMS %}

```json
{
  "version": 1 //numerical version of the JSON structure
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
  "canvas_name": String, // will only be available if the message is from Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

{% endtab %}
{% tab Push %}

```json
{
  "version": 1, //numerical version of the JSON structure
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

### 페이로드 구조 변형 푸시

{% alert important %}
푸시 알림 아카이브의 최상위`payload`필드에는 기기로 전송된 전체 제공자 페이로드가 포함됩니다. 이 JSON 내에서 (APN용) 또는`data``notification``aps`(FCM용)과 같은 키는 메시지 유형, 플랫폼 및 구성에 따라 크게 달라질 수 있습니다.
{% endalert %}

메시지 아카이빙은 메시지 페이로드 자체를 캡처하지만, FCM 또는 APN으로 전송되는 전달 메타데이터는 포함하지 않습니다. 전달 메타데이터에는 다음이 포함됩니다:

- 기기 토큰
- 우선순위 설정
- 유지 시간(TTL)
- ID 접기
- APN 헤더
- 만료 타임스탬프
- 기타 전달 설정 필드

이 필드들은 푸시 제공자에게 전달 지침 역할을 합니다. 일반적으로 메시지 내용의 일부로 간주되지 않습니다.

For example:

- **iOS 푸시 알림은** 리치 알림(리치`aps.alert`알림은  와  `title`등의 필드를 `body`포함하는 객체)과 단순 알림(단순`aps.alert`알림은 문자열)에 따라 구조가 다를 수 있습니다.
- **Android 푸시 알림**(예: FCM)은 커스텀 키가 포함된 데이터 메시지를 사용합니다. 페이로드 구조는 메시지 구성에 따라 푸시 버튼, 캐러셀 또는 추가 메타데이터와 같은 다양한 선택적 필드를 포함할 수 있습니다.

또한, 대시보드에서 수행하는 테스트 전송은 실제 운영 환경의 메시지와 다른 페이로드 구조를 생성할 수 있습니다.

JSON 페이로드 형식은 메시지마다 다를 수 있으며 시간이 지남에 따라 변경될 수 있습니다. 아카이브된 푸시 페이로드를 구문 분석할 때 고정된 구조를 가정하거나 동일한 필드가 항상 존재할 것이라고 기대하지 마십시오. 다양한 페이로드 형식을 처리하는 유연한 구문 분석 로직을 구현합니다.

{% endtab %}
{% endtabs %}

## 자주 묻는 질문

### 페이로드에 포함되지 않은 템플릿은 무엇입니까?

메시지가 Braze를 떠난 후 수정한 내용은 클라우드 저장소 버킷에 저장된 파일에 반영되지 않습니다. 여기에는 클릭 추적을 위한 링크 래핑 및 추적 픽셀 삽입과 같은 메일 전송 파트너의 수정 사항이 포함됩니다.

### 캠페인 경로에서 "연관되지 않은" 값 아래의 메시지는 무엇입니까?

메시지가 캠페인 또는 캔버스 외부로 전송될 때, 파일 이름의 캠페인 ID는 "연결되지 않음"이 됩니다. This will happen when you send test messages from the dashboard, when Braze sends SMS/MMS auto-responses, or when messages sent through the API do not specify a campaign ID.

### 이 발송에 대한 추가 정보를 어떻게 찾을 수 있습니까?

템플릿 메시지를 당사 커런츠 데이터와 교차`user_id`참조하여 추가 정보를 확인하려면  또는`external_id`  을`dispatch_id`  와 함께 사용할 수 있습니다. 예를 들어 메시지 전달 타임스탬프, 사용자가 메시지를 열었는지 또는 클릭했는지 등의 정보를 확인할 수 있습니다.

### 재시도는 어떻게 처리됩니까?

클라우드 스토리지 버킷에 연결할 수 없는 경우, Braze는 [백오프 지터를](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/#Jitter) 사용하여 최대 세 번 재시도합니다. AWS S3 사용량 제한 재시도는 Braze에 의해 자동으로 처리됩니다.

### 내 자격 증명이 유효하지 않으면 어떻게 되나요?

클라우드 저장소 자격 증명이 어느 시점에서든 유효하지 않은 경우, Braze는 클라우드 저장소 버킷에 메시지를 저장할 수 없으며 해당 메시지는 손실됩니다. Amazon Web Services, Google Cloud Services 또는 Azure(Microsoft Cloud Services)의 [알림 설정을]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/notification_preferences/) 구성하여 자격 증명 관련 문제 발생 시 알림을 수신하시기 바랍니다.

### 아카이브 파일의 `sent_at` 타임스탬프가 Currents에서 전송된 타임스탬프와 약간 다른 이유는 무엇인가요?

렌더링된 사본은 사용자에게 메시지를 보내기 직전에 업로드됩니다. 클라우드 스토리지 업로드 시간으로 인해 렌더링된 사본의 `sent_at` 타임스탬프와 실제 전송이 발생한 시간 사이에 몇 초의 지연이 발생할 수 있습니다.

### Can I create a new bucket specifically for message archiving while keeping the current bucket used for Currents data?

No. If you're interested in creating these specific buckets, submit [product feedback]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).

### Is archived data written to a dedicated folder in an existing bucket, similar to how Currents data exports are structured?

The data is written to a `sent_messages` section of the bucket. Refer to [How it works](#how-it-works) for more details.

### 메시지 아카이빙을 사용하여 파일을 서로 다른 작업 공간으로 그룹화할 수 있나요?

아니요. 메시지 아카이빙은 작업 공간을 기준으로 파일을 그룹화하는 기능을 지원하지 않습니다. 대신 캠페인 또는 캔버스 단계 API ID가 속한 작업 공간을 확인한 후, 해당 정보를 기준으로 그룹화할 수 있습니다.
