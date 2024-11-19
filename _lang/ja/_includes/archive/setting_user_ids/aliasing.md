[ユーザーエイリアスは]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)、代替の一意なユーザー識別子として機能する。エイリアスを使用して、コアユーザーIDとは異なる次元でユーザーを識別することができる：

* ユーザーがモバイルアプリやWebサイトにログインする前と後の両方をフォローする分析用の一貫した識別子を設定する。
* サードパーティーベンダーが使用している識別子を外部ユーザーに追加することで、外部とのユーザーデータの照合をより簡単に行うことができる。

各エイリアスは、識別子そのものの名前と、エイリアスの種類を示すラベルの2つの部分で構成される。ユーザーは異なるラベルで複数のエイリアスを持つことができるが、1つのラベルにつき1つの名前しか持つことができない。 

ユーザープロファイルに対するユーザーエイリアスの設定については、[ユーザーエイリアスを]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)参照のこと。

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

{% elsif include.platform == "Web" %}

```javascript
braze.getUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```

{% elsif include.platform == "REST" %}

```json
{
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```

{% endif %}
