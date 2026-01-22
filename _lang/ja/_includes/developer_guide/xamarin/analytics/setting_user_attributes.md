{% multi_lang_include developer_guide/prerequisites/xamarin.md %}

## ユーザー属性の設定

Braze には、ユーザーに属性を割り当てるメソッドが用意されています。ダッシュボード上のこれらの属性に従って、ユーザーのフィルター処理とセグメント化を行うことができます。

### デフォルトのユーザー属性

Braze によって自動的に収集されるユーザー 属性を設定するには、SDKに付属の設定メソッドを使用します。たとえば、ユーザーの名を設定できます。

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).CurrentUser.SetFirstName("first_name");
```

{% endtab %}
{% tab iOS %}

```csharp
App.braze?.User.SetFirstName("first_name");
```

{% endtab %}
{% endtabs %}

以下の属性がサポートされています。

- 名
- 姓
- 性別
- 生年月日
- 市区町村
- 国
- 電話番号
- メール

### カスタムユーザー属性

Braze は、定義済みのユーザー属性メソッドに加えて、`SetCustomUserAttribute` を使用してアプリケーションのデータを追跡するカスタム属性も提供しています。

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).CurrentUser.SetCustomUserAttribute("custom_attribute_key", true);
```

属性のトラッキングのベストプラクティスとインターフェイスの詳細については、[Android の統合手順]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android)を参照してください。

{% endtab %}
{% tab iOS %}

```csharp
App.braze?.User.SetCustomAttributeWithKey("custom_attribute_key", true);
```

属性のトラッキングのベストプラクティスとインターフェイスの詳細については、[iOS の統合手順]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift)を参照してください。

{% endtab %}
{% endtabs %}
