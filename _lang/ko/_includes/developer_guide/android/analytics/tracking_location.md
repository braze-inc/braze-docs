## 현재 위치 기록하기

연속 추적이 비활성화된 경우에도 사용자의 현재 위치를 수동으로 기록할 수 있습니다. [`setLastKnownLocation()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-last-known-location.html) 메서드를 사용하여 사용자의 현재 위치를 수동으로 기록할 수 있습니다.

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

## 지속적인 위치 추적

{% alert important %}
[안드로이드 마시멜로부터는](https://developer.android.com/training/permissions/index.html) 사용자에게 위치 추적에 대한 명시적인 동의 메시지를 표시해야 합니다. 이렇게 하면 다음 세션이 시작될 때 Braze에서 위치 추적을 시작할 수 있습니다. 이는 `AndroidManifest.xml` 에서 위치 권한만 선언하면 되었던 이전 버전의 Android와는 다릅니다.
{% endalert %}

사용자의 위치를 지속적으로 추적하려면 `AndroidManifest.xml` 파일에 다음 권한 중 하나 이상을 추가하여 앱의 위치 데이터 수집 의도를 선언해야 합니다.

|권한|설명|
|---|---|
| `ACCESS_COARSE_LOCATION` | 배터리 효율이 가장 높은 비 GPS 제공업체(예: 홈 네트워크)를 사용합니다. 일반적으로 대부분의 위치 데이터 요구 사항에는 이 정도면 충분합니다. 런타임 권한 모델에서 위치 권한을 부여하면 암묵적으로 정밀한 위치 데이터 수집을 승인하는 것입니다. |
| `ACCESS_FINE_LOCATION`   | 보다 정확한 위치를 파악할 수 있도록 GPS 데이터를 포함합니다. 런타임 권한 모델에서 위치 권한 부여는 미세 위치 액세스 권한도 포함합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

`AndroidManifest.xml` 은 다음과 유사해야 합니다:

```xml
<manifest ... >
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />

    <application ... >
        ...
    </application>
</manifest>
```

## 연속 추적 비활성화하기

컴파일 시간 또는 런타임에 연속 추적을 비활성화할 수 있습니다.

{% tabs local %}
{% tab 컴파일 시간 %}

컴파일 시 지속적인 위치 추적을 비활성화하려면 `braze.xml` 에서 `com_braze_enable_location_collection` 를 `false` 로 설정합니다:

```xml
<bool name="com_braze_enable_location_collection">false</bool>
```

{% endtab %}
{% tab 런타임 %}

런타임에 연속 위치 추적을 선택적으로 비활성화하려면, 다음을 사용합니다. [`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration):

{% subtabs %}
{% subtab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setIsLocationCollectionEnabled(false)
  .build();
Braze.configure(this, brazeConfig);
```
 
{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setIsLocationCollectionEnabled(false)
    .build()
Braze.configure(this, brazeConfig)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}
