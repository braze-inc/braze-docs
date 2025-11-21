---
nav_title: Baidu integration
article_title: Baidu Push Notification Integration for Android
platform: Android
permalink: /baidu_integration/
description: "This article shows how to set up a Baidu Android integration."
hidden: true
---
# Baidu integration
{% multi_lang_include archive/baidu_deprecation.md %}

Braze can send push notifications to Android devices using [Baidu Cloud Push]({% image_buster /assets/img_archive/baidu_app_console.png %}). Note that using Baidu Cloud Push **does not** require you to distribute your apps via the Baidu App Store.

## Step 1: Create a Baidu account

To create a Baidu account, visit the [Baidu Portal](https://www.baidu.com/) and click **登录** (Log in) to bring up a dialog that will allow you to log in or create a new account.

![]({% image_buster /assets/img_archive/baidu_portal.png %})

To create a new account, at the bottom of the login dialog, click **立即注册** (new account).

![]({% image_buster /assets/img_archive/baidu_login_dialog.png %}){: style="max-width:70%;"}

Enter your username, phone number, and password into the account creation page. Next, click the receive verification code button. You will now receive an SMS message from Baidu containing a verification code. Lastly, accept the license agreement and click **注册** (create account) to register. If these setup steps fail, try to register via Baidu Cloud login as described in this [login article](https://www.adchina.io/how-to-open-a-baidu-account-outside-china/).

![Baidu Sign-up Page]({% image_buster /assets/img_archive/baidu_signup.png %}){: style="max-width:80%;"}

## Step 2: Register as a Baidu developer

Next, you must register as a Baidu developer. First, visit the [Baidu developer portal](http://developer.baidu.com/) and choose **注册** (create new developer account) to begin registration.

![]({% image_buster /assets/img_archive/baidu_dev_portal.png %})

On the registration page, choose your account type (个人 for personal, 公司 for business) and developer type (developer is preselected and correct for most cases). Enter your name, a bio, and phone number with country code in parenthesis (For example, (1)xxxxxxxxxx). Click **发送验证码** (send verification code) and enter the verification code in the following line. The next two fields, developer website, and developer logo, are optional. Accept the license agreement and click **提交** (submit) to submit. You now have a Baidu developer account.

![]({% image_buster /assets/img_archive/baidu_dev_reg.png %})

## Step 3: Register your application with Baidu

To register your application with Baidu, visit the [Baidu project portal](http://developer.baidu.com/console#app/project) and click **创建工程** (create project).

![]({% image_buster /assets/img_archive/baidu_project.png %})

On the following page, enter your application name. The following two checkboxes are to activate additional Baidu services. In most cases, these should be left blank.

![]({% image_buster /assets/img_archive/baidu_app_name.png %})

Upon setting up your application, you will be taken to a console that displays information about your app, including the API Key. Next, navigate to **云推送** (cloud push) in the sidebar. On the following page, click **推送设置** (set up push).

![]({% image_buster /assets/img_archive/baidu_app_console.png %})

![]({% image_buster /assets/img_archive/baidu_continue.png %})

On the following page, enter your app package name (for example, `com.braze.sample`) and specify whether to cache messages and, if so, how long (in hours). This indicates to Baidu how long to continue to attempt sending messages to offline users. Click **保存设置** (save settings) to save.

![]({% image_buster /assets/img_archive/baidu_configure_cloud.png %})

## Step 4: Add Baidu to your application

Visit the [Baidu push SDK portal](http://developer.baidu.com/wiki/index.php?title=docs/cplat/push/sdk/clientsdk) and download the latest Baidu Cloud Push Android SDK.

![]({% image_buster /assets/img_archive/baidu_sdk.png %})

Inside the SDK, you will find the push service jar and platform-specific native libraries. Integrate these into your project. Make sure your app targets the highest SDK version currently supported by Baidu. This documentation is current for Baidu Cloud push Android SDK version `4.6.2.38`.

Add the following required Baidu permissions to your application's `AndroidManifest.xml`.

```xml
    <uses-permission android:name="android.permission.READ_PHONE_STATE" />
    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
    <uses-permission android:name="android.permission.WRITE_SETTINGS" />
    <uses-permission android:name="android.permission.VIBRATE" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.DISABLE_KEYGUARD" />
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
```

Baidu's library contains broadcast receivers that handle incoming push messages. Declare the internal Baidu receivers in your application's `AndroidManifest.xml` inside the `<application>` element.

```xml
  <!-- 用于接收系统消息以保证 PushService 正常运行 -->
      <receiver
        android:name="com.baidu.android.pushservice.PushServiceReceiver"
        android:process=":bdservice_v1">
        <intent-filter>
          <action android:name="android.intent.action.BOOT_COMPLETED"/>
          <action android:name="android.net.conn.CONNECTIVITY_CHANGE"/>
          <action android:name="com.baidu.android.pushservice.action.notification.SHOW"/>
          <action android:name="com.baidu.android.pushservice.action.media.CLICK"/>
        </intent-filter>
      </receiver>
      <!-- Push 服务接收客户端发送的各种请求-->
      <!-- 注意:RegistrationReceiver 在 2.1.1 及之前版本有拼写失误,为 RegistratonReceiver ,用 新版本 SDK 时请更改为如下代码-->
      <receiver
        android:name="com.baidu.android.pushservice.RegistrationReceiver"
        android:process=":bdservice_v1">
        <intent-filter>
          <action android:name="com.baidu.android.pushservice.action.METHOD"/>
          <action android:name="com.baidu.android.pushservice.action.BIND_SYNC"/>
        </intent-filter>
        <intent-filter>
          <action android:name="android.intent.action.PACKAGE_REMOVED"/>
          <data android:scheme="package"/>
        </intent-filter>
      </receiver>
      <!-- Push 服务 -->
      <!-- 注意:在 4.0 (包含)之后的版本需加上如下所示的 intent-filter action -->
      <service
        android:name="com.baidu.android.pushservice.PushService"
        android:exported="true"
        android:process=":bdservice_v1">
        <intent-filter >
          <action android:name="com.baidu.android.pushservice.action.PUSH_SERVICE"/>
        </intent-filter>
      </service>
```

You will also need to create a broadcast receiver that listens for incoming push messages and notifications. Declare your receiver in your application's `AndroidManifest.xml` inside the `<application>` element. This receiver will need to extend `com.baidu.android.pushservice.PushMessageReceiver` and implement methods that receive event updates from the Baidu push service.

```xml
      <receiver android:name=".MyPushMessageReceiver">
        <intent-filter>
          <action android:name="com.baidu.android.pushservice.action.MESSAGE"/>
          <action android:name="com.baidu.android.pushservice.action.RECEIVE"/>
          <action android:name="com.baidu.android.pushservice.action.notification.CLICK"/>
        </intent-filter>
      </receiver>
```

In your main activity's `onCreate()` method, add the following line, which will register your application with Baidu and begin listening for incoming push messages. Make sure to replace "Your-API-Key" with your project's Baidu API Key.

```
PushManager.startWork(getApplicationContext(), PushConstants.LOGIN_TYPE_API_KEY, "Your-API-Key");
```

Finally, you will need to register your users with Braze. In the `onBind()` method of the Baidu broadcast receiver you created in this step, send the `channelId` to Braze using `Braze.registerAppboyPushMessages(channelId)`.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).setRegisteredPushToken(channelId);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).setRegisteredPushToken(channelId)
```

{% endtab %}
{% endtabs %}

## Step 5: Registering push opens

Baidu supports sending extra key-value pairs with push messages in JSON format. Your broadcast receiver's `public void onNotificationClicked(Context context, String title, String description, String customContentString)` method will be called whenever a user clicks an incoming push message. The parameter `customContentString` contains the extras in JSON format. All messages from Braze will contain the following two key-value pairs:

  ```json
  {
    "source": "Appboy",
    "cid": "your-campaign-Id"
  }
  ```

Whenever `onNotificationClicked` is called your Baidu receiver, your receiver should send an [Intent](http://developer.android.com/reference/android/content/Intent.html) to your application containing `customContentString`. Your application will log the click to Braze using the `customContentString`.

The following sample code passes `customContentString` to Braze and logs a click:

{% tabs %}
{% tab JAVA %}

  ```java
  String customContentString = intent.getStringExtra(ChinaPushMessageReceiver.NOTIFICATION_CLICKED_KEY);
  BrazeNotificationUtils.logBaiduNotificationClick(mApplicationContext, customContentString);
  ```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val customContentString = intent.getStringExtra(ChinaPushMessageReceiver.NOTIFICATION_CLICKED_KEY)
BrazeNotificationUtils.logBaiduNotificationClick(context, customContentString)
```

{% endtab %}
{% endtabs %}

## Step 6: Extras

Aside from reserved keys used by Braze, the parameter `customContentString` will also contain all user-defined custom key-value pairs. To extract your key-value pairs, wrap `customContentString` in a JSONObject and retrieve your extras:

{% tabs %}
{% tab JAVA %}

```java
try {
  JSONObject myExtras = new JSONObject(customContentString);
  String myValue = myExtras.optString("my_key", null);
} catch (Exception e) {
  Log.e(TAG, "Caught an exception processing customContentString");
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
try {
  val myExtras = JSONObject(customContentString)
  val myValue = myExtras.optString("my_key", null)
} catch (e: Exception) {
  Log.e(TAG, "Caught an exception processing customContentString", e)
}
```

{% endtab %}
{% endtabs %}

## Step 7: Set up Baidu keys

You need to input your Baidu API Key and Baidu Secret Key into the Braze dashboard. Both keys are available from the Baidu application console.

On the **Manage Settings** page, select your Android China app and enter your Baidu API Key and Baidu Secret Key in the push notifications section.

![]({% image_buster /assets/img_archive/baidu_api_key.png %} "APIKey"){: style="max-width:80%;"}

## Additional resources

- [Baidu portal](https://www.baidu.com/)
- [Baidu developer portal](http://developer.baidu.com/)
- [Baidu project portal](http://developer.baidu.com/console#app/project)
- [Baidu push SDK portal](http://developer.baidu.com/wiki/index.php?title=docs/cplat/push/sdk/clientsdk)
- [Baidu integration docs](http://developer.baidu.com/wiki/index.php?title=docs/frontia/guide-android/overview)

