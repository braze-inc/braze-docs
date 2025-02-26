---
nav_title: "Windows 개체"
article_title: Windows 메시징 개체
page_order: 14
page_type: reference
channel: push
platform:
  - Windows Universal
description: "이 참조 문서에서는 Braze에서 사용되는 다양한 Windows 객체를 나열하고 설명합니다."
hidden: true
---
# Windows 개체 사양

`windows_phone8_push` 및 `windows_universal_push` 개체는 [메시징 엔드포인트]({{site.baseurl}}/api/endpoints/messaging)를 통해 Windows Phone 8 푸시 및 Windows Universal 푸시 콘텐츠와 관련된 정보를 정의하거나 요청하는 데 사용됩니다.

## Windows Phone 8 푸시 개체

```json
{
   "push_type": (optional, string) must be "toast",
   "toast_title": (optional, string) the notification title,
   "toast_content": (required, string) the notification message,
   "toast_navigation_uri": (optional, string) page uri to send user to,
   "toast_hash": (optional, object) additional keys and values to send,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be a Windows Phone 8 Push Message)
}
```

## Windows 유니버설 푸시 개체

`push_type`에 대한 옵션에 대한 자세한 내용은 Windows Universal [토스트 템플릿 카탈로그][32]를 참조하세요.

```json
{
   "push_type": (required, string) one of: "toast_text_01", "toast_text_02", "toast_text_03", "toast_text_04", "toast_image_and_text_01", "toast_image_and_text_02", "toast_image_and_text_03", or "toast_image_and_text_04",
   "toast_text1": (required, string) the first line of text in the template,
   "toast_text2": (optional, string) the second line of text (for templates with > 1 line of text),
   "toast_text3": (optional, string) the third line of text (for the *_04 templates),
   "toast_text_img_name": (optional, string) the path for the image for the templates that include an image,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be a Windows Universal Push Message),
   "extra_launch_string": (optional, string) used to add deep linking functionality by passing extra values to the launch string
}
```

[딥링킹][38]용 `extra_launch_string` 매개 변수를 사용하는 방법에 대한 자세한 내용은 [Windows 유니버설로 딥링킹][37]을 참조하세요.

[32]: https://msdn.microsoft.com/en-us/library/windows/apps/hh761494.aspx
[37]: {{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/push_notifications/integration/#step-4-deep-linking-from-push-into-your-app
[38]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking
