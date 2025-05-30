# 위치 추적

> 이 문서는 Android 또는 FireOS 애플리케이션에 대한 위치 추적을 구성하는 방법을 보여줍니다.

다음 권한 중 하나 이상을 `AndroidManifest.xml` 파일에 추가하여 앱의 위치 데이터 수집 의도를 선언합니다.

```xml
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
```
```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
```

`ACCESS_FINE_LOCATION`에는 사용자 위치를 보고할 때 GPS 데이터가 포함되며 `ACCESS_COARSE_LOCATION`에는 배터리 효율이 가장 높은 사용 가능한 비GPS 공급자(예: 네트워크)의 데이터가 포함됩니다. 대부분의 위치 데이터 사용 사례에는 대략적인 위치로도 충분합니다. 그러나 런타임 권한 모델에서는 사용자로부터 위치 권한을 받으면 세부 위치 데이터를 수집할 수 있는 권한이 암묵적으로 부여됩니다. Android 개발자의 [위치 전략](https://stuff.mit.edu/afs/sipb/project/android/docs/guide/topics/location/strategies.html)을(를) 살펴보고 이러한 위치 권한의 차이점과 사용 방법에 대해 자세히 알아보세요.

{% alert important %}
Android M의 출시와 함께 Android는 설치 시점에서 런타임 권한 모델로 전환되었습니다. Android M 이상을 실행하는 기기에서 위치 추적을 활성화하려면 앱이 사용자로부터 위치 사용 권한을 명시적으로 받아야 합니다(Braze는 수행하지 않음). 위치 권한이 부여되면 Braze는 `braze.xml`에서 위치 수집이 활성화된 경우 다음 세션 시작 시 자동으로 위치 추적을 시작합니다. Android의 이전 버전을 실행하는 기기는 `AndroidManifest.xml`에서 위치 권한만 선언하면 됩니다. 자세한 내용은 Android의 [권한 설명서](https://developer.android.com/training/permissions/index.html)를 참조하십시오.
{% endalert %}

## 자동 위치 추적 비활성화

### 컴파일 시점 옵션

컴파일 시점에 자동 위치 추적을 비활성화하려면 `braze.xml`에서 `com_braze_enable_location_collection`을 `false`로 설정합니다.

```xml
<bool name="com_braze_enable_location_collection">false</bool>
```

### 런타임 옵션

런타임에 자동 위치 추적을 선택적으로 비활성화하려면 [`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration)를 사용합니다.

{% tabs %}
{% tab 자바 %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setIsLocationCollectionEnabled(false)
  .build();
Braze.configure(this, brazeConfig);
```
 
{% endtab %}
{% tab 코틀린 %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setIsLocationCollectionEnabled(false)
    .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

## 수동으로 위치 기록

자동 추적이 비활성화된 경우에도 `BrazeUser`에서 [`setLastKnownLocation()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-last-known-location.html) 메서드를 사용하여 단일 위치 데이터 포인트를 수동으로 기록할 수 있습니다.

{% tabs %}
{% tab 자바 %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setLastKnownLocation(LATITUDE_DOUBLE_VALUE, LONGITUDE_DOUBLE_VALUE, ALTITUDE_DOUBLE_VALUE, ACCURACY_DOUBLE_VALUE);
  }
}
```

{% endtab %}
{% tab 코틀린 %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setLastKnownLocation(LATITUDE_DOUBLE_VALUE, LONGITUDE_DOUBLE_VALUE, ALTITUDE_DOUBLE_VALUE, ACCURACY_DOUBLE_VALUE)
}
```

{% endtab %}
{% endtabs %}

