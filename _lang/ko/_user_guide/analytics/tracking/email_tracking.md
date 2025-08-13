---
nav_title: 이메일 Open Pixel and 클릭 추적
article_title: 이메일 Open Pixel and 클릭 추적
page_order: 1
page_type: reference
description: "이 참조 문서는 오픈 픽셀 및 클릭 추적을 구현하는 방법을 다룹니다."

---

# 이메일 열람 픽셀 클릭 추적

> [Open pixel tracking]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#changing-location-of-tracking-pixel) and click tracking can be turned on or off for each user profile. 이 유연성은 고객 프로필이 더 이상 추적되지 않기를 원할 수 있는 지역 개인정보 보호법을 준수하는 데 도움이 됩니다.

## 오픈 픽셀 또는 클릭 추적 켜기

When either importing or updating a user profile via [API]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields) or [CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv), two fields are available for you to modify:

- `email_open_tracking_disabled`: `true` 또는 `false`를 수락합니다. `false`로 설정하여 이 사용자에게 보내는 모든 향후 이메일에 열람 추적 픽셀을 추가합니다. Available for SparkPost and SendGrid only.
- `email_click_tracking_disabled`: `true` 또는 `false`를 수락합니다. `false`로 설정하여 이 사용자에게 보내는 향후 이메일 내의 모든 링크에 클릭 추적을 추가합니다. Available for SparkPost and SendGrid only.

참고로 이 정보는 이메일 **연락처 설정**의 고객 프로필에 반영되어 있으며, **참여** 탭에 위치해 있습니다.

![Email open and click tracking pixel fields on the Engagement tab of a user's profile]({% image_buster /assets/img_archive/open_click_user_profile.png %}){: style="max-width:60%;"}

