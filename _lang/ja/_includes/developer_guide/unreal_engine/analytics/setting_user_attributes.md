## デフォルトユーザー属性

### サポートされている属性

`UBrazeUser` オブジェクトでは、以下の属性を設定する必要があります。

- `SetFirstName`
- `SetLastName`
- `SetEmail`
- `SetDateOfBirth`
- `SetCountry`
- `SetLanguage`
- `SetHomeCity`
- `SetPhoneNumber`
- `SetGender`

### デフォルト属性の設定

ユーザーにデフォルト属性を設定するには、共有`UBrazeUser` オブジェクトの`GetCurrentUser()` メソッドを呼び出し、アプリの現在のユーザーへの参照を取得する。そして、ユーザー属性を設定するメソッドを呼び出すことができる。

```cpp
UBraze->GetCurrentUser([](UBrazeUser* BrazeUser) {
    if (BrazeUser) {
        BrazeUser->SetFirstName(TEXT("Alex"));
    }
});
```

## カスタムユーザー属性

デフォルトのユーザー属性に加え、Brazeではいくつかのデータタイプを使用してカスタム属性を定義することができる。各属性のセグメンテーションオプションの詳細については、[ユーザーデータ収集を]({{site.baseurl}}/developer_guide/analytics/)参照のこと。

{% tabs local %}
{% tab ストリング %}
`string` 、カスタム属性を設定する：

```cpp
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), TEXT("your_attribute_value"));
```
{% endtab %}

{% tab 整数 %}
`integer` 、カスタム属性を設定する：

```cpp
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), 42);
```
{% endtab %}

{% tab 浮動小数点 %}
Braze では、データベース内での `float` 値と `double` 値の扱いが同じです。カスタム属性に2倍の値を設定する：

```cpp
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), 3.14);
```
{% endtab %}

{% tab ブーリアン %}
`boolean` 、カスタム属性を設定する：

```cpp
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), true);
```
{% endtab %}

{% tab 日付 %}
`date` 、カスタム属性を設定する：

```cpp
FDateTime YourDateTime = FDateTime(2023, 5, 10);
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), YourDateTime);
```
{% endtab %}

{% tab 配列 %}
`array` 、カスタム属性を設定する：

```cpp
// Setting a custom attribute with an array value
TArray<FString> Values = {TEXT("value1"), TEXT("value2")};
UBrazeUser->SetCustomAttributeArray(TEXT("array_name"), Values);

// Adding to a custom attribute with an array value
UBrazeUser->AddToCustomAttributeArray(TEXT("array_name"), TEXT("value3"));

// Removing a value from an array type custom attribute
UBrazeUser->RemoveFromCustomAttributeArray(TEXT("array_name"), TEXT("value2"));
```
{% endtab %}
{% endtabs %}

{% alert important %}
カスタム属性値の最大長は 255 文字です。これより長い値は切り捨てられます。
{% endalert %}

## ユーザーサブスクリプションの設定

ユーザーにメールまたはプッシュサブスクリプションを設定するには、以下の方法を使用できる。

### サブスクリプションの設定

```cpp
UBraze->GetCurrentUser([](UBrazeUser* BrazeUser) {
    if (BrazeUser) {
        BrazeUser->SetEmailSubscriptionType(EBrazeSubscriptionType::Subscribed);
    }
});
```

### アトリビューション・データの設定

```cpp
UBraze->GetCurrentUser([](UBrazeUser* BrazeUser) {
    if (BrazeUser) {
        BrazeUser->SetPushSubscriptionType(EBrazeSubscriptionType::OptedIn);
    }
});
```
