[사용자 별칭은]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases) 대체 고유 사용자 식별자 역할을 합니다. 별칭을 사용하여 핵심 사용자 ID와는 다른 차원에서 사용자를 식별할 수 있습니다:

* 특정 사용자가 모바일 앱이나 웹사이트에 로그인하기 전과 후에 모두 팔로우할 분석에 일관된 식별자를 설정합니다.
* 외부에서 데이터를 더 쉽게 조정할 수 있도록 타사 공급업체에서 사용하는 식별자를 Braze 사용자에게 추가하세요.

각 별칭은 식별자 자체의 이름과 별칭의 유형을 나타내는 레이블의 두 부분으로 구성됩니다. 사용자는 레이블이 다른 여러 개의 별칭을 사용할 수 있지만 레이블당 하나의 이름만 사용할 수 있습니다. 

고객 프로필에 대한 사용자 별칭 설정에 대한 자세한 내용은 [사용자 별칭]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)을 참조하세요.

{% if include.platform == "iOS" %}

{% tabs %}
{% tab 목표-C %}

```objc
 [[Appboy sharedInstance].user addAlias:ALIAS_NAME withLabel:ALIAS_LABEL];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.addAlias(ALIAS_NAME, ALIAS_LABEL)
```

{% endtab %}
{% endtabs %}

{% elsif include.platform == "Android" %}

{% tabs %}
{% tab 자바 %}

```java
Braze.getInstance(context).getCurrentUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```

{% endtab %}
{% tab 코틀린 %}

```kotlin
Braze.getInstance(context).currentUser?.addAlias(ALIAS_NAME, ALIAS_LABEL)
```

{% endtab %}
{% endtabs %}

자세한 내용은 [KDoc을](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/index.html#-1106019389%2FFunctions%2F-1725759721) 참조하세요.

{% elsif include.platform == "Web" %}

```javascript
braze.getUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```

{% elsif include.platform == "Swift" %}

```swift
AppDelegate.braze?.user.add(alias: ALIAS_NAME, label: ALIAS_LABEL)
```

{% elsif include.platform == "REST" %}

```json
{
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```

{% endif %}
