---
nav_title: 이메일 오픈 픽셀 및 클릭 추적
article_title: 이메일 오픈 픽셀 및 클릭 추적
page_order: 1
page_type: reference
description: "이 참조 문서에서는 오픈 픽셀 및 클릭 추적을 구현하는 방법에 대해 설명합니다."

---

# 이메일 오픈 픽셀 및 클릭 추적

> 각 고객 프로필에 대해 [오픈 픽셀 추적]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#changing-location-of-tracking-pixel) 및 클릭 추적을 켜거나 끌 수 있습니다. 이러한 유연성은 개별 고객 프로필에서 더 이상 추적을 원하지 않는다고 표시할 수 있는 지역 개인정보 보호법을 준수하는 데 도움이 됩니다.

## 열린 픽셀 또는 클릭 추적 켜기

[API]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields) 또는 [CSV를]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv) 통해 고객 프로필을 가져오거나 업데이트할 때 수정할 수 있는 필드는 두 가지입니다:

- `email_open_tracking_disabled`: 수락 `true` 또는 `false`. `false` 으로 설정하여 향후 이 사용자에게 전송되는 모든 이메일에 열람 추적 픽셀을 추가합니다. SparkPost 및 SendGrid에서만 사용할 수 있습니다.
- `email_click_tracking_disabled`: 수락 `true` 또는 `false`. `false` 으로 설정하여 향후 이 사용자에게 전송되는 이메일 내의 모든 링크에 클릭 추적을 추가합니다. SparkPost 및 SendGrid에서만 사용할 수 있습니다.

참고로 이 정보는 **참여** 탭에 있는 이메일 **연락처 설정의** 고객 프로필에 반영됩니다.

이메일을 열고 고객 프로필의 참여 탭에서 추적 픽셀 필드를 클릭합니다.]({% image_buster /assets/img_archive/open_click_user_profile.png %}){: style="max-width:60%;"}

