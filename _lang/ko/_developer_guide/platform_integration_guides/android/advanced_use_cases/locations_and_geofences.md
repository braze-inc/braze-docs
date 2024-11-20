---
nav_title: 위치 및 지오펜스
article_title: Android 및 FireOS용 위치 및 지오펜스
platform: 
  - Android
  - FireOS
page_order: 6
description: "이 참조 문서에서는 Android 또는 FireOS 애플리케이션에서 위치 및 지오펜스를 구현하는 방법을 다룹니다."
Tool:
  - Location

---

# 위치 및 지오펜스

> [지오펜스]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences#about-locations-and-geofences/)는 일부 Braze 패키지에서만 사용할 수 있습니다. 액세스하려면 [지원 티켓을]({{site.baseurl}}/braze_support/) 만들거나 Braze 고객 성공 관리자와 상담하세요.

Android용 지오펜스를 지원하려면 다음을 수행합니다.

1. 통합은 백그라운드 푸시 알림을 지원해야 합니다.
2. Braze 지오펜스 또는 위치 수집을 활성화해야 합니다.

## 1단계: 업데이트 build.gradle

앱 수준 `build.gradle`에 `android-sdk-location`을 추가합니다. 또한 Google Play 서비스 [설정 가이드](https://developers.google.com/android/guides/setup)를 사용하여 Google Play 서비스 [위치 패키지](https://developers.google.com/android/reference/com/google/android/gms/location/package-summary)를 추가합니다.

```
dependencies {
  implementation "com.braze:android-sdk-location:+"
  implementation "com.google.android.gms:play-services-location:${PLAY_SERVICES_VERSION}"
}
```

## 2단계: 매니페스트 업데이트

`AndroidManifest.xml`에 부팅, 세부 위치 및 백그라운드 위치 권한을 추가합니다.

```xml
<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
```

{% alert important %}
백그라운드 위치 액세스 권한은 Android 10에 추가되었으며 모든 Android 10 이상 기기에서 앱이 백그라운드에 있는 동안 지오펜스가 작동하는 데 필요합니다.
{% endalert %}

`AndroidManifest.xml` 의 `application` 요소에 Braze 부팅 리시버를 추가합니다:

```xml
<receiver android:name="com.braze.BrazeBootReceiver">
  <intent-filter>
    <action android:name="android.intent.action.BOOT_COMPLETED" />
  </intent-filter>
</receiver>
```

## 3단계: Braze 위치 수집 활성화

아직 Braze 위치 수집을 활성화하지 않았다면 `braze.xml` 파일을 업데이트하여 `com_braze_enable_location_collection`을 포함하고 해당 값이 `true`로 설정되어 있는지 확인합니다.

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
Braze Android SDK 버전 3.6.0부터 Braze 위치 수집은 기본적으로 비활성화됩니다.
{% endalert %}

Braze 위치 수집이 활성화된 경우 Braze 지오펜스가 활성화됩니다. 기본 위치 수집을 옵트아웃하고 싶지만 지오펜스를 계속 사용하려면 `braze.xml`에서 `com_braze_geofences_enabled` 키의 값을 `true`로 설정하여 `com_braze_enable_location_collection` 값과 독립적으로 이 기능을 선택적으로 활성화할 수 있습니다.

```xml
<bool name="com_braze_geofences_enabled">true</bool>
```

## 4단계: 최종 사용자로부터 위치 권한 얻기

Android M 이상 버전의 경우 위치 정보를 수집하거나 지오펜스를 등록하기 전에 최종사용자에게 위치 권한을 요청해야 합니다.

다음 호출을 추가하여 사용자가 앱에 위치 권한을 부여할 때 Braze에 알립니다.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).requestLocationInitialization();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).requestLocationInitialization()
```

{% endtab %}
{% endtabs %}

이렇게 하면 SDK가 Braze 서버에 지오펜스를 요청하고 지오펜스 추적을 초기화합니다.

예제 구현은 샘플 애플리케이션의 [`RuntimePermissionUtils.java`](https://github.com/braze-inc/braze-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/util/RuntimePermissionUtils.kt)를 참조하세요.

{% tabs %}
{% tab JAVA %}

```java
public class RuntimePermissionUtils {
  private static final String TAG = BrazeLogger.getBrazeLogTag(RuntimePermissionUtils.class);
  public static final int DROIDBOY_PERMISSION_LOCATION = 40;

  public static void handleOnRequestPermissionsResult(Context context, int requestCode, int[] grantResults) {
    switch (requestCode) {
      case DROIDBOY_PERMISSION_LOCATION:
        // In Android Q, we require both FINE and BACKGROUND location permissions. Both
        // are requested simultaneously.
        if (areAllPermissionsGranted(grantResults)) {
          Log.i(TAG, "Required location permissions granted.");
          Toast.makeText(context, "Required location permissions granted.", Toast.LENGTH_SHORT).show();
          Braze.getInstance(context).requestLocationInitialization();
        } else {
          Log.i(TAG, "Required location permissions NOT granted.");
          Toast.makeText(context, "Required location permissions NOT granted.", Toast.LENGTH_SHORT).show();
        }
        break;
      default:
        break;
    }
  }

  private static boolean areAllPermissionsGranted(int[] grantResults) {
    for (int grantResult : grantResults) {
      if (grantResult != PackageManager.PERMISSION_GRANTED) {
        return false;
      }
    }
    return true;
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
object RuntimePermissionUtils {
  private val TAG = BrazeLogger.getBrazeLogTag(RuntimePermissionUtils::class.java!!)
  val DROIDBOY_PERMISSION_LOCATION = 40

  fun handleOnRequestPermissionsResult(context: Context, requestCode: Int, grantResults: IntArray) {
    when (requestCode) {
      DROIDBOY_PERMISSION_LOCATION ->
        // In Android Q, we require both FINE and BACKGROUND location permissions. Both
        // are requested simultaneously.
        if (areAllPermissionsGranted(grantResults)) {
          Log.i(TAG, "Required location permissions granted.")
          Toast.makeText(context, "Required location permissions granted.", Toast.LENGTH_SHORT).show()
          Braze.getInstance(context).requestLocationInitialization()
        } else {
          Log.i(TAG, "Required location permissions NOT granted.")
          Toast.makeText(context, "Required location permissions NOT granted.", Toast.LENGTH_SHORT).show()
        }
      else -> {
      }
    }
  }

  private fun areAllPermissionsGranted(grantResults: IntArray): Boolean {
    for (grantResult in grantResults) {
      if (grantResult != PackageManager.PERMISSION_GRANTED) {
        return false
      }
    }
    return true
  }
}
```

{% endtab %}
{% endtabs %}

앞의 샘플 코드는 다음을 통해 사용할 수 있습니다:

{% tabs %}
{% tab JAVA %}

```java
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
  if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
    boolean hasAllPermissions = PermissionUtils.hasPermission(getApplicationContext(), Manifest.permission.ACCESS_BACKGROUND_LOCATION)
        && PermissionUtils.hasPermission(getApplicationContext(), Manifest.permission.ACCESS_FINE_LOCATION);
    if (!hasAllPermissions) {
      // Request both BACKGROUND and FINE location permissions
      requestPermissions(new String[]{android.Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.ACCESS_BACKGROUND_LOCATION},
          RuntimePermissionUtils.DROIDBOY_PERMISSION_LOCATION);
    }
  } else {
    if (!PermissionUtils.hasPermission(getApplicationContext(), Manifest.permission.ACCESS_FINE_LOCATION)) {
      // Request only FINE location permission
      requestPermissions(new String[]{android.Manifest.permission.ACCESS_FINE_LOCATION},
          RuntimePermissionUtils.DROIDBOY_PERMISSION_LOCATION);
    }
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
  if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
    val hasAllPermissions = PermissionUtils.hasPermission(applicationContext, Manifest.permission.ACCESS_BACKGROUND_LOCATION)
        && PermissionUtils.hasPermission(applicationContext, Manifest.permission.ACCESS_FINE_LOCATION)
    if (!hasAllPermissions) {
      // Request both BACKGROUND and FINE location permissions
      requestPermissions(arrayOf(android.Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.ACCESS_BACKGROUND_LOCATION),
          RuntimePermissionUtils.DROIDBOY_PERMISSION_LOCATION)
    }
  } else {
    if (!PermissionUtils.hasPermission(applicationContext, Manifest.permission.ACCESS_FINE_LOCATION)) {
      // Request only FINE location permission
      requestPermissions(arrayOf(android.Manifest.permission.ACCESS_FINE_LOCATION),
          RuntimePermissionUtils.DROIDBOY_PERMISSION_LOCATION)
    }
  }
}
```

{% endtab %}
{% endtabs %}

## 5단계: 대시보드에서 지오펜스 활성화

Android에서는 특정 앱에 대해 최대 100개의 지오펜스만 저장하도록 허용합니다. Braze 위치 제품은 사용 가능한 경우 최대 20개의 지오펜스 슬롯을 사용합니다. 앱의 다른 지오펜스 관련 기능이 실수로 또는 원치 않게 중단되는 것을 방지하려면 대시보드에서 개별 앱에 대해 위치 지오펜스를 활성화해야 합니다.

Braze 위치 제품이 올바르게 작동하려면 앱이 사용 가능한 모든 지오펜스 지점을 사용하고 있지 않은지도 확인합니다.

### 위치 페이지에서 지오펜스 사용 설정

![Braze 위치 페이지의 지오펜스 옵션]({% image_buster /assets/img_archive/enable-geofences-locations-page.png %})

### 설정 페이지에서 지오펜스 활성화

![Braze 설정 페이지에 있는 지오펜스 확인란.]({% image_buster /assets/img_archive/enable-geofences-app-settings-page.png %}){: style="max-width:65%;" }

## 6단계: 지오펜스 업데이트 수동 요청(선택 사항)

기본적으로 Braze는 기기의 위치를 자동으로 검색하고 수집된 위치를 기반으로 지오펜스를 요청합니다. 그러나 대신 근거리 Braze 지오펜스를 검색하는 데 사용할 GPS 좌표를 수동으로 제공할 수 있습니다. Braze 지오펜스를 수동으로 요청하려면 자동 Braze 지오펜스 요청을 비활성화하고 요청을 위한 GPS 좌표를 제공해야 합니다.

#### 1부: 자동 지오펜스 요청 비활성화

자동 Braze 지오펜스 요청은 `braze.xml` 파일에서 `com_braze_automatic_geofence_requests_enabled`를 `false`로 설정하여 비활성화할 수 있습니다.

```xml
<bool name="com_braze_automatic_geofence_requests_enabled">false</bool>
```

이 작업은 다음을 통해 런타임에서 수행할 수 있습니다.

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
    .setAutomaticGeofenceRequestsEnabled(false);
Braze.configure(getApplicationContext(), brazeConfigBuilder.build());
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfigBuilder = BrazeConfig.Builder()
    .setAutomaticGeofenceRequestsEnabled(false)
Braze.configure(applicationContext, brazeConfigBuilder.build())
```

{% endtab %}
{% endtabs %}

#### 2부: GPS 좌표로 Braze 지오펜스 수동 요청

Braze 지오펜스는 [`requestGeofences()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-geofences.html) 메서드를 통해 수동으로 요청됩니다.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(getApplicationContext()).requestGeofences(latitude, longitude);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(applicationContext).requestGeofences(33.078947, -116.601356)
```

{% endtab %}
{% endtabs %}

{% alert important %}
지오펜스는 세션당 한 번만 요청할 수 있으며, SDK를 통해 자동으로 요청하거나 이 메서드를 사용하여 수동으로 요청할 수 있습니다.
{% endalert %}

## 푸시하여 동기화

Braze는 백그라운드 푸시를 사용하여 지오펜스를 기기와 동기화합니다. 이 기능은 앱의 일부로 추가 통합이 필요하지 않으므로 대부분의 경우 코드 변경이 필요하지 않습니다.

그러나 애플리케이션이 중지된 경우 백그라운드 푸시를 받으면 백그라운드에서 애플리케이션이 실행되고 `Application.onCreate()` 메서드가 호출됩니다. 커스텀 `Application.onCreate()` 구현이 있는 경우 자동 서버 호출 및 백그라운드 푸시로 트리거하지 않으려는 기타 작업을 연기해야 합니다.

