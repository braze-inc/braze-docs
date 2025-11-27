[ユーザーエイリアス]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)は、代替の一意のユーザー識別子として機能します。エイリアスを使用して、コアユーザーIDとは異なる次元でユーザーを識別することができる：

* モバイルアプリやウェブサイトにログインする前と後の両方で、特定のユーザーを追跡するアナリティクス用の一貫した識別子を設定します。
* 外部とのデータの照合をより簡単に行うためには、サードパーティベンダーが使用する識別子を Braze ユーザーに追加します。

各エイリアスは、識別子そのものの名前と、エイリアスの種類を示すラベルの2つの部分で構成される。ユーザーは異なるラベルで複数のエイリアスを持つことができるが、1つのラベルにつき1つの名前しか持つことができない。 

ユーザープロファイルにユーザーエイリアスを設定する方法について詳しくは、[[ユーザーエイリアス]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)] を参照してください。

{% if include.platform == "iOS" %}

{% tabs %}
{% tab OBJECTIVE-C %}

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
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).currentUser?.addAlias(ALIAS_NAME, ALIAS_LABEL)
```

{% endtab %}
{% endtabs %}

詳細については、[KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/index.html#-1106019389%2FFunctions%2F-1725759721) をご覧ください。

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
