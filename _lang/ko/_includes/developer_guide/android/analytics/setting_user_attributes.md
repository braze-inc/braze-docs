{% multi_lang_include developer_guide/prerequisites/android.md %}

## 기본 사용자 속성

### 미리 정의된 메서드

Braze는 [`BrazeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/index.html) 클래스 내에서 다음 사용자 속성을 설정하기 위한 미리 정의된 메서드를 제공합니다. 메서드 사양은 [우리 KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/index.html)을 참조하십시오.

- First name
- 성
- 국가
- 언어
- 생년월일
- 이메일
- 성별
- 출생지
- Phone number

{% alert note %}
이름과 성, 국가, 출생지와 같은 모든 문자열 값은 255자로 제한됩니다.
{% endalert %}

### 기본 속성 설정

사용자에 대한 기본 속성을 설정하려면 Braze 인스턴스에서 `getCurrentUser()` 메서드를 호출하여 앱의 현재 사용자에 대한 참조를 가져옵니다. 그런 다음 사용자 속성을 설정하기 위해 메서드를 호출할 수 있습니다.

{% tabs %}
{% tab 자바 %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setFirstName("first_name");
  }
}
```

{% endtab %}
{% tab 코틀린 %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setFirstName("first_name")
}
```

{% endtab %}
{% endtabs %}

### 기본 속성 해제

사용자 속성을 해제하려면 관련 메서드에 `null`을 전달하십시오.

{% tabs %}
{% tab 자바 %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setFirstName(null);
  }
}
```

{% endtab %}
{% tab 코틀린 %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setFirstName(null)
}
```

{% endtab %}
{% endtabs %}

## 사용자 지정 사용자 속성

기본 사용자 속성 외에도 Braze는 여러 가지 데이터 유형을 사용하여 커스텀 속성을 정의할 수 있도록 허용합니다. 각 속성의 세분화 옵션에 대한 자세한 내용은 [사용자 데이터 수집]({{site.baseurl}}/developer_guide/analytics)을 참조하십시오.

### 사용자 지정 속성 설정

{% tabs local %}
{% tab 문자열 %}
`string` 값으로 커스텀 속성을 설정하려면:

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", "your_attribute_value");
  }
}
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", "your_attribute_value")
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab 정수 %}
`int` 값으로 커스텀 속성을 설정하려면:

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_INT_VALUE);
    
    // Integer attributes may also be incremented using code like the following:
    brazeUser.incrementCustomUserAttribute("your_attribute_key", YOUR_INCREMENT_VALUE);
  }
}
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_INT_VALUE)

  // Integer attributes may also be incremented using code like the following:
  brazeUser.incrementCustomUserAttribute("your_attribute_key", YOUR_INCREMENT_VALUE)
}
```

{% endsubtab %}
{% endsubtabs %}

`long` 정수 값으로 커스텀 속성을 설정하려면:

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_LONG_VALUE);
  }
});
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_LONG_VALUE)
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab 부동 소수점 %}
`float` 값으로 커스텀 속성을 설정하려면:

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_FLOAT_VALUE);
  }
});
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_FLOAT_VALUE)
}
```

{% endsubtab %}
{% endsubtabs %}

`double` 값으로 커스텀 속성을 설정하려면:

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_DOUBLE_VALUE);
  }
});
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_DOUBLE_VALUE)
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 부울 %}
`boolean` 값으로 커스텀 속성을 설정하려면:

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_BOOLEAN_VALUE);
  }
});
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_BOOLEAN_VALUE)
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 날짜 %}
{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_DATE_VALUE);
    // This method will assign the current time to a custom attribute at the time the method is called:
    brazeUser.setCustomUserAttributeToNow("your_attribute_key");
    // This method will assign the date specified by SECONDS_FROM_EPOCH to a custom attribute:
    brazeUser.setCustomUserAttributeToSecondsFromEpoch("your_attribute_key", SECONDS_FROM_EPOCH);
  }
});
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_DATE_VALUE)
  // This method will assign the current time to a custom attribute at the time the method is called:
  brazeUser.setCustomUserAttributeToNow("your_attribute_key")
  // This method will assign the date specified by SECONDS_FROM_EPOCH to a custom attribute:
  brazeUser.setCustomUserAttributeToSecondsFromEpoch("your_attribute_key", SECONDS_FROM_EPOCH)
}
```

{% endsubtab %}
{% endsubtabs %}

{% alert warning %}
이 메서드에서 Braze에 전달된 날짜는 [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) 형식(e.g `2013-07-16T19:20:30+01:00`) 또는 `yyyy-MM-dd'T'HH:mm:ss:SSSZ` 형식(e.g `2016-12-14T13:32:31.601-0800`)이어야 합니다
{% endalert %}

{% endtab %}
{% tab 배열 %}

커스텀 속성 배열의 최대 요소 개수 기본값은 25개입니다. 개별 배열의 최대치는 Braze 대시보드의 **데이터 설정** > **커스텀 속성**에서 최대 100개로 늘릴 수 있습니다. 최대 요소 수를 초과하는 배열은 최대 요소 수를 포함하도록 잘립니다. 커스텀 속성 배열과 해당 동작에 대한 자세한 내용은 [배열]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays)에 대한 설명서를 참조하세요.

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    // Setting a custom attribute with an array value
    brazeUser.setCustomAttributeArray("your_attribute_key", testSetArray);
    // Adding to a custom attribute with an array value
    brazeUser.addToCustomAttributeArray("your_attribute_key", "value_to_add");
    // Removing a value from an array type custom attribute
    brazeUser.removeFromCustomAttributeArray("your_attribute_key", "value_to_remove");
  }
});
```
{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  // Setting a custom attribute with an array value
  brazeUser.setCustomAttributeArray("your_attribute_key", testSetArray)
  // Adding to a custom attribute with an array value
  brazeUser.addToCustomAttributeArray("your_attribute_key", "value_to_add")
  // Removing a value from an array type custom attribute
  brazeUser.removeFromCustomAttributeArray("your_attribute_key", "value_to_remove")
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### 커스텀 속성 해제

커스텀 속성을 해제하려면 관련 속성 키를 `unsetCustomUserAttribute` 메서드에 전달하십시오.

{% tabs %}
{% tab 자바 %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.unsetCustomUserAttribute("your_attribute_key");
  }
});
```

{% endtab %}
{% tab 코틀린 %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.unsetCustomUserAttribute("your_attribute_key")
}
```

{% endtab %}
{% endtabs %}

### 커스텀 속성 중첩

커스텀 속성 내에서 속성을 중첩할 수도 있습니다. 다음 예제에서는 중첩 속성이 있는 `favorite_book` 객체가 사용자 프로필의 커스텀 속성으로 설정됩니다. 자세한 내용은 [중첩 커스텀 속성]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support)을 참조하십시오.

{% tabs %}
{% tab 자바 %}
```java
JSONObject favoriteBook = new JSONObject();
try {
  favoriteBook.put("title", "The Hobbit");
  favoriteBook.put("author", "J.R.R. Tolkien");
  favoriteBook.put("publishing_date", "1937");
} catch (JSONException e) {
  e.printStackTrace();
}

braze.getCurrentUser(user -> {
  user.setCustomUserAttribute("favorite_book", favoriteBook);
  return null;
});
```
{% endtab %}

{% tab 코틀린 %}
```kotlin
val favoriteBook = JSONObject()
  .put("title", "The Hobbit")
  .put("author", "J.R.R. Tolkien")
  .put("publishing_date", "1937")

braze.getCurrentUser { user ->
  user.setCustomUserAttribute("favorite_book", favoriteBook)
}
```
{% endtab %}
{% endtabs %}

### REST API 사용

REST API를 사용하여 사용자 속성을 설정하거나 해제할 수도 있습니다. 자세한 정보는 [사용자 데이터 엔드포인트]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data)를 참조하십시오.

## 사용자 구독 설정

사용자에 대한 가입(이메일 또는 푸시)을 설정하려면 각각 `setEmailNotificationSubscriptionType()` 또는 `setPushNotificationSubscriptionType()` 함수를 호출합니다. 이 두 함수 모두 열거형 `NotificationSubscriptionType` 을 인자로 받습니다. 이 유형에는 세 가지 상태가 있습니다:

| 구독 상태 | 정의 |
| ------------------- | ---------- |
| `OPTED_IN` | 구독하고 명시적으로 동의한 경우 |
| `SUBSCRIBED` | 구독 중이지만 명시적으로 옵트인하지 않은 경우 |
| `UNSUBSCRIBED` | 구독 취소 및/또는 명시적 수신 거부 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Android에서 사용자에게 푸시 알림을 보내기 위해 명시적으로 옵트인할 필요는 없습니다. 사용자가 푸시에 등록되면 기본적으로 `OPTED_IN` 대신 `SUBSCRIBED`로 설정됩니다. 가입 및 명시적 옵트인 구현에 대한 자세한 내용은 [사용자 가입 관리]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions)를 참조하세요.
{% endalert %}

### 이메일 구독 설정

{% tabs %}
{% tab 자바 %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setEmailNotificationSubscriptionType(emailNotificationSubscriptionType);
  }
});
```

{% endtab %}
{% tab 코틀린 %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setEmailNotificationSubscriptionType(emailNotificationSubscriptionType)
}
```

{% endtab %}
{% endtabs %}

### 푸시 알림 구독 설정

{% tabs %}
{% tab 자바 %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setPushNotificationSubscriptionType(pushNotificationSubscriptionType);
  }
});
```

{% endtab %}
{% tab 코틀린 %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setPushNotificationSubscriptionType(pushNotificationSubscriptionType)
}
```

{% endtab %}
{% endtabs %}

