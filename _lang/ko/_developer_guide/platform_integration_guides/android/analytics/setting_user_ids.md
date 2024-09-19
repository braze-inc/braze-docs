---
nav_title: 사용자 ID 설정
article_title: Android 및 FireOS용 사용자 ID 설정하기
platform: 
  - Android
  - FireOS
page_order: 1
description: "이 참조 문서에서는 Android 또는 FireOS 앱에서 사용자 ID를 설정하는 방법, 권장 사용자 ID 명명 규칙 및 몇 가지 모범 사례를 보여 줍니다."

---
 
# 사용자 ID 설정
 
> 이 참조 문서에서는 Android 또는 FireOS 앱에서 사용자 ID를 설정하는 방법, 권장 사용자 ID 명명 규칙 및 몇 가지 모범 사례를 보여 줍니다.

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

## 추천 사용자 ID 명명 규칙

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

### 사용자 ID 할당하기

사용자 ID를 설정하려면 사용자가 식별되는 즉시(일반적으로 로그인 후) 다음 호출을 수행해야 합니다:

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING)
```

{% endtab %}
{% endtabs %}

{% alert warning %}
**사용자가 로그아웃할 때 `changeUser()` 을 호출하지 마세요. `changeUser()` 은 사용자가 애플리케이션에 로그인할 때만 호출해야 합니다.** `changeUser()` 을 정적 기본값으로 설정하면 사용자가 다시 로그인할 때까지 모든 사용자 활동이 해당 기본 '사용자'와 연결됩니다.
{% endalert %}

또한 사용자가 로그아웃할 때 사용자 ID를 변경하면 이전에 로그인한 사용자를 리인게이지먼트 캠페인으로 타겟팅할 수 없게 되므로 사용자 ID를 **변경하지 않는** 것이 좋습니다. 동일한 디바이스에 여러 명의 사용자가 있을 것으로 예상되지만 앱이 로그아웃 상태일 때 그 중 한 명만 타겟팅하려는 경우, 로그아웃한 상태에서 타겟팅하려는 사용자 ID를 별도로 추적하고 앱의 로그아웃 프로세스의 일부로 해당 사용자 ID로 다시 전환하는 것을 권장합니다.

자세한 내용은 [`changeUser`][4] 문서를 참조하세요.

## 사용자 ID 통합 모범 사례 및 참고 사항

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

## 사용자 앨리어싱

{% multi_lang_include archive/setting_user_ids/aliasing.md platform="Android" %}

[1]: {{site.baseurl}}/api/endpoints/user_data
[2]: {{site.baseurl}}/api/endpoints/messaging/
[4]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html
