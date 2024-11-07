---
nav_title: 사용자 ID 설정
article_title: Windows 유니버설용 사용자 ID 설정
platform: Windows Universal
page_order: 1
description: "이 참조 문서에서는 Windows 유니버설 플랫폼에서 사용자 아이디를 설정하는 방법에 대해 설명합니다."
hidden: true
---

# 사용자 ID 설정
{% multi_lang_include archive/windows_deprecation.md %}

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

사용자가 식별되는 즉시(일반적으로 로그인 후) 다음 호출을 수행하여 사용자 ID를 설정해야 합니다.

```csharp
Appboy.SharedInstance.ChangeUser(YOUR_USER_ID_STRING);
```

{% alert warning %}
**사용자가 로그아웃할 때 `changeUser()`를 호출하지 마세요. `changeUser()`는 사용자가 애플리케이션에 로그인할 때만 호출해야 합니다.** `changeUser()`를 정적 기본값으로 설정하면 사용자가 다시 로그인할 때까지 모든 사용자 활동이 해당 기본값 "사용자"와 연결됩니다.
{% endalert %}

또한 사용자가 로그아웃할 때 사용자 ID를 변경하면 이전에 로그인한 사용자를 리인게이지먼트 캠페인으로 타겟팅할 수 없게 되므로 사용자 ID를 변경하지 않는 것이 좋습니다. 여러 사용자가 동일한 기기를 사용할 것으로 예상되지만 앱에서 로그아웃한 상태일 때 사용자 중 한 명만을 타겟팅하려는 경우, 로그아웃 상태에서 타겟팅하려는 사용자 ID를 별도로 추적하고 앱의 로그아웃 프로세스의 일환으로 해당 사용자 ID로 전환하는 방법을 권장합니다.

## 추천 사용자 ID 명명 규칙

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## 사용자 ID 통합 모범 사례 및 참고 사항

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

[1]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[2]: {{site.baseurl}}/developer_guide/rest_api/messaging/
[6]: http://developer.android.com/reference/java/util/Locale.html#default_locale "Android 개발자 문서 - 현지화"
