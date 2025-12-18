---
nav_title: 메시지 아카이빙
article_title: 메시지 아카이빙
alias: "/message_archiving/"
page_order: 0
page_type: reference
description: "이 참고 문서에서는 사용자에게 보낸 메시징의 사본을 저장할 수 있는 기능인 메시지 보관에 대해 설명합니다."

---

# 메시지 아카이빙

> 메시지 아카이빙을 사용하면 보관 또는 규정 준수 목적으로 사용자에게 보낸 메시징의 사본을 AWS S3 버킷, Azure Blob Storage 컨테이너 또는 Google Cloud Storage 버킷에 저장할 수 있습니다. <br><br> 이 문서에서는 메시지 보관, JSON 페이로드 참조 및 자주 묻는 질문을 설정하는 방법에 대해 설명합니다.

메시지 보관 기능은 추가 기능으로 제공됩니다. 메시지 아카이빙을 시작하려면 Braze 고객 성공 매니저에게 문의하세요.

## 작동 방식

이 기능을 켜면 클라우드 스토리지 버킷을 Braze에 연결하고 기본값 데이터 내보내기 대상으로 표시한 경우, 선택한 채널(이메일, SMS/MMS 또는 푸시)을 통해 사용자에게 전송되는 각 메시지에 대해 Braze가 클라우드 스토리지 버킷에 압축된 JSON 파일을 작성합니다. 

이 파일에는 [파일 참조](#file-references) 아래에 정의된 필드가 포함되며 사용자에게 전송된 최종 템플릿 메시징이 반영됩니다. 캠페인에 정의된 모든 템플릿 값(예: {% raw %}`{{${first_name}}}`{% endraw %})은 사용자의 프로필 정보를 기반으로 사용자가 받은 최종 값을 표시합니다. 이를 통해 규정 준수, 감사 또는 고객 지원 요건을 충족하기 위해 보낸 메시징의 사본을 보관할 수 있습니다.

여러 클라우드 스토리지 공급업체에 대한 자격 증명을 설정한 경우, 메시지 아카이빙은 명시적으로 데이터 내보내기 기본값으로 표시된 공급업체로만 내보내집니다. 명시적인 기본값이 제공되지 않고 AWS S3 버킷이 연결되어 있으면 메시지 아카이빙이 해당 버킷에 업로드됩니다.

{% alert important %}
이 기능을 켜면 정확성을 유지하기 위해 메시지 전송 직전에 파일 업로드가 수행되므로 메시지 전달 속도에 영향을 미칩니다. 메시지 보관으로 인해 발생하는 지연 시간은 클라우드 스토리지 제공업체와 저장된 문서의 처리량 및 크기에 따라 달라집니다.
{% endalert %}

JSON은 다음 키 구조를 사용하여 스토리지 버킷에 저장됩니다:

`sent_messages/{channel, one of: email, push, sms}/{MD5 digest of downcased: email address, push token, or E.164 phone number}/{campaign or Canvas step API ID}/{dispatch ID}.json.gz`

예제 파일은 다음과 같습니다:

`sent_messages/email/819baa08d8d7e77e19d4666f5fc6050b/ee965cb2-8934-4b0a-acf1-91c899c2f915/651fd10b282850b39e1169c13975234b.json.gz`

{% alert note %}
MD5 다이제스트는 알려진 다운케이싱된 이메일 주소, 푸시 토큰 또는 E.164 전화번호를 사용해서만 계산할 수 있습니다. 알려진 MD5 다이제스트는 대소문자가 바뀐 이메일 주소, 푸시 토큰 또는 E.164 전화번호를 얻기 위해 되돌릴 수 없습니다.
{% endalert %}

{% alert tip %}
**버킷에서 푸시 토큰을 찾는 데 문제가 있으신가요?**<br>
Braze는 푸시 토큰을 해시하기 전에 다운케이스합니다. 이렇게 하면 푸시 토큰 `Test_Push_Token12345` 이 키 경로에서 `32b802170652af2b5624b695f34de089` 해시를 사용하여 `test_push_token12345` 으로 다운케이싱됩니다.
{% endalert %}

## 메시지 보관 설정하기

이 섹션에서는 워크스페이스에 대한 메시지 보관 설정 방법을 안내합니다. 계속 진행하기 전에 회사에서 메시지 보관 기능을 구매하고 사용 설정했는지 확인하세요.

### 1단계: 클라우드 스토리지 버킷 연결하기

아직 연결하지 않았다면 클라우드 스토리지 버킷을 Braze에 연결하세요. 단계는 [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/), [Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/) 또는 [Google Cloud Storage에]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/) 대한 파트너 설명서를 참조하세요.

### 2단계: 메시지 보관을 위한 채널 선택하기

**메시지 보관** 설정 페이지에서는 보낸 메시지의 사본을 클라우드 스토리지 버킷에 저장할 채널을 제어합니다.

채널을 선택하려면 다음과 같이 하세요:

1. **설정** > **메시지 보관으로** 이동합니다.
2. 채널을 선택합니다.
3. **변경 사항 저장을** 선택합니다.

\![메시지 보관 페이지에는 세 가지 채널을 선택할 수 있습니다: 이메일, 푸시 및 SMS.]({% image_buster /assets/img/message_archiving_settings.png %})

{% alert note %}
**설정에** **메시지 보관이** 표시되지 않으면 회사에서 메시지 보관을 구매하여 사용 설정했는지 확인하세요.
{% endalert %}

## 파일 참조

다음은 메시징이 전송될 때마다 클라우드 스토리지 버킷에 전달되는 JSON 페이로드에 대한 참조입니다. [메시지 아카이브 샘플 파일은](https://github.com/braze-inc/braze-examples/tree/main/message-archiving) 코드 예제 리포지토리를 참조하세요.

{% tabs %}
{% tab Email %}

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

이 페이로드에서 참조하는 `extras` 필드는 이메일 작성 시 **이메일 추가** 필드에 추가된 키-값 페어에서 가져온 것입니다. 커런츠에 데이터를 다시 보내려면 [메시지 추가]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/) 기능을 참조하세요.

\![]({% image_buster /assets/img_archive/email_extras.png %}){: style="max-width:60%" }

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
{% tab Push %}

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

### 페이로드에 포함되지 않는 템플릿은 무엇인가요?

메시징이 Braze를 떠난 후 수정한 내용은 클라우드 스토리지 버킷에 저장된 파일에 반영되지 않습니다. 여기에는 클릭 추적을 위해 링크를 래핑하고 추적 픽셀을 삽입하는 등 메일 전달 파트너의 수정 작업이 포함됩니다.

### 캠페인 경로에서 "연결되지 않음" 값 아래의 메시지는 무엇인가요?

메시지가 캠페인 또는 캔버스 외부로 전송되는 경우 파일 이름의 캠페인 ID는 "연결되지 않음"이 됩니다. 이는 대시보드에서 테스트 메시지를 보낼 때, Braze가 SMS/MMS 자동 응답을 보낼 때, 또는 API를 통해 전송된 메시지에 캠페인 ID가 지정되지 않은 경우에 발생합니다.

### 이 전송에 대한 자세한 정보는 어떻게 찾을 수 있나요?

`external_id` 또는 `dispatch_id` 을 `user_id` 과 함께 사용하여 템플릿 메시지를 커런츠 데이터와 상호 참조하여 메시지가 전달된 타임스탬프, 사용자가 메시지를 열었는지 또는 클릭했는지 등의 자세한 정보를 확인할 수 있습니다.

### 재시도는 어떻게 처리되나요?

클라우드 스토리지 버킷에 연결할 수 없는 경우, Braze는 [백오프 지터를](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/#Jitter) 사용하여 최대 3회까지 재시도합니다. AWS S3 속도 제한 재시도는 Braze에서 자동으로 처리합니다.

### 자격 증명이 유효하지 않은 경우 어떻게 되나요?

클라우드 저장소 자격 증명이 어느 시점에서든 유효하지 않게 되면 Braze는 클라우드 저장소 버킷에 메시지를 저장할 수 없으며 해당 메시지는 손실됩니다. 자격 증명 문제에 대한 알림을 받을 수 있도록 Amazon Web Services, Google Cloud Services 또는 Azure(Microsoft Cloud Services)에 대한 [알림 기본 설정을]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/notification_preferences/) 구성하는 것이 좋습니다.

### 아카이브 파일의 `sent_at` 타임스탬프가 커런츠에서 전송된 타임스탬프와 약간 다른 이유는 무엇인가요?

렌더링된 사본은 사용자에게 메시지를 보내기 직전에 업로드됩니다. 클라우드 스토리지 업로드 시간으로 인해 렌더링된 사본의 `sent_at` 타임스탬프와 실제 전송이 발생한 시간 사이에 몇 초의 지연이 발생할 수 있습니다.

### 커런츠 데이터에 사용되는 현재 버킷을 유지하면서 메시지 보관 전용 버킷을 새로 만들 수 있나요?

아니요. 이러한 특정 버킷을 만드는 데 관심이 있으시면 [제품 피드백을]({{site.baseurl}}/user_guide/administrative/access_braze/portal/) 제출하세요.

### 커런츠 데이터 내보내기 구조와 유사하게 기존 버킷의 전용 폴더에 아카이브된 데이터가 기록되나요?

데이터는 버킷의 `sent_messages` 섹션에 기록됩니다. 자세한 내용은 [작동 방식을](#how-it-works) 참조하세요.

