---
nav_title: 사용자 ID 설정
article_title: Braze SDK를 통해 사용자 ID 설정하기
page_order: 1.2
description: "Braze SDK를 통해 사용자 ID를 설정하는 방법을 알아보세요."

---

# 사용자 ID 설정

> Braze SDK를 통해 사용자 ID를 설정하는 방법을 알아보세요. 이는 여러 디바이스와 플랫폼에서 사용자를 추적하고, [사용자 데이터 API를]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) 통해 데이터를 가져오고, [메시징 API를]({{site.baseurl}}/api/endpoints/messaging/) 통해 타겟팅된 메시지를 보낼 수 있는 고유 식별자입니다. 사용자에게 고유 ID를 할당하지 않으면 Braze에서 익명 ID를 대신 할당하지만, 할당할 때까지는 이러한 기능을 사용할 수 없습니다.

{% alert note %}
목록에 없는 래퍼 SDK의 경우 관련 네이티브 Android 또는 Swift 메서드를 대신 사용하세요.
{% endalert %}

## 익명 사용자 정보

{% multi_lang_include 익명 사용자/about_anonymous_users.md %}

## 사용자 ID 설정

사용자 ID를 설정하려면 사용자가 처음 로그인한 후 `changeUser()` 메서드를 호출합니다. 아이디는 고유해야 하며 [명명 모범 사례를](#naming-best-practices) 따라야 합니다.

대신 고유 식별자를 해싱하는 경우 해싱 함수의 입력을 정규화해야 합니다. 예를 들어 이메일 주소를 해시할 때는 앞뒤 공백을 모두 제거하고 현지화를 고려하세요.

{% tabs local %}
{% tab 안드로이드 %}
{% subtabs %}
{% subtab JAVA %}
```java
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING);
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab SWIFT %}
{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.changeUser(userId: "YOUR_USER_ID")
```
{% endsubtab %}
{% subtab objective-c %}
```objc
[AppDelegate.braze changeUser:@"YOUR_USER_ID_STRING"];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 웹 %}
표준 웹 SDK 구현의 경우 다음 방법을 사용할 수 있습니다:

```javascript
braze.changeUser(YOUR_USER_ID_STRING);
```

대신 Google 태그 관리자를 사용하려면 **사용자** 태그 유형 **변경을** 사용하여 [`changeUser` 메서드를](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser) 호출할 수 있습니다. 사용자가 로그인하거나 고유한 `external_id` 식별자로 식별될 때마다 사용합니다.

일반적으로 웹사이트에서 전송한 데이터 레이어 변수를 사용하여 채워지는 **외부 사용자 ID** 필드에 현재 사용자의 고유 ID를 입력해야 합니다.

![Braze 작업 태그 구성 설정을 보여주는 대화상자. 포함된 설정은 '태그 유형'과 '외부 사용자 ID'입니다.]({% image_buster /assets/img/web-gtm/gtm-change-user.png %})
{% endtab %}

{% tab CORDOVA %}
```javascript
BrazePlugin.changeUser("YOUR_USER_ID");
```
{% endtab %}

{% tab ROKU %}
```brightscript
m.Braze.setUserId(YOUR_USER_ID_STRING)
```
{% endtab %}

{% tab UNITY %}
```csharp
AppboyBinding.ChangeUser("YOUR_USER_ID_STRING");
```
{% endtab %}

{% tab 언리얼 엔진 %}
```cpp
UBraze->ChangeUser(TEXT("YOUR_USER_ID_STRING"));
```
{% endtab %}
{% endtabs %}

{% alert warning %}
**사용자가 로그아웃할 때 정적 기본 ID를 할당하거나 `changeUser()` 으로 전화하지 마세요.** 이렇게 하면 공유 디바이스에서 이전에 로그인한 사용자를 다시 참여시킬 수 없습니다. 대신 모든 사용자 ID를 개별적으로 추적하고 앱의 로그아웃 프로세스에서 이전에 로그인한 사용자로 다시 전환할 수 있도록 하세요. 새 세션이 시작되면 Braze는 새로 활성화된 프로필의 데이터를 자동으로 새로 고칩니다.
{% endalert %}

## 사용자 별칭

### 작동 방식

{% multi_lang_include 익명_사용자/about_user_aliases.md %}

### 사용자 별칭 설정

사용자 별칭은 이름과 레이블의 두 부분으로 구성됩니다. 이름은 식별자 자체를 가리키고 레이블은 식별자가 속한 식별자 유형을 가리킵니다. 예를 들어 타사 고객 지원 플랫폼에 외부 ID `987654` 를 가진 사용자가 있는 경우, Braze에서 이름 `987654` 과 레이블 `support_id` 을 사용하여 별칭을 할당하면 여러 플랫폼에서 해당 사용자를 추적할 수 있습니다.

{% tabs local %}
{% tab Android %}
{% subtabs %}
{% subtab java %}
```java
Braze.getInstance(context).getCurrentUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```
{% endsubtab %}

{% subtab kotlin %}
```kotlin
Braze.getInstance(context).currentUser?.addAlias(ALIAS_NAME, ALIAS_LABEL)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
```swift
Appboy.sharedInstance()?.user.addAlias(ALIAS_NAME, ALIAS_LABEL)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
 [[Appboy sharedInstance].user addAlias:ALIAS_NAME withLabel:ALIAS_LABEL];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 웹 %}
```javascript
braze.getUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```
{% endtab %}

{% tab rest API %}
```json
{
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```
{% endtab %}
{% endtabs %}

## ID 이름 지정 모범 사례 {#naming-best-practices}

무작위로 잘 분산된 128비트 문자열인 [UUID(범용 고유 식별자)](https://en.wikipedia.org/wiki/Universally_unique_identifier) 표준을 사용하여 사용자 ID를 생성하는 것이 좋습니다.

또는 기존 고유 식별자(예: 이름 또는 이메일 주소)를 해시하여 사용자 ID를 대신 생성할 수도 있습니다. 이 경우 사용자 사칭을 방지할 수 있도록 [SDK 인증을]({{site.baseurl}}/developer_guide/authentication/) 구현해야 합니다.

처음부터 사용자 ID의 이름을 올바르게 지정하는 것이 중요하지만, 나중에 언제든지 [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/) 엔드포인트를 사용하여 언제든지 이름을 변경할 수 있습니다.

| 추천 | 권장하지 않음 |
| ------------ | ----------- |
| 123e4567-e89b-12d3-a456-836199333115 | JonDoe829525552 |
| 8c0b3728-7fa7-4c68-a32e-12de1d3ed2d5 | Anna@email.com |
| f0a9b506-3c5b-4d86-b16a-94fc4fc3f7b0 | CompanyName-1-2-19 |
| 2d9e96a1-8f15-4eaf-bf7b-eb8c34e25962 | jon-doe-1-2-19 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert warning %}
사용자 아이디를 만드는 방법에 대한 세부 정보를 공유하면 조직이 악의적인 공격이나 데이터 삭제에 노출될 수 있으므로 공유하지 마세요.
{% endalert %}
