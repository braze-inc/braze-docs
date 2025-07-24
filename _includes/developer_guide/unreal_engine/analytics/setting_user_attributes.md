## Default User Attributes

### Supported attributes

The following attributes should be set on the `UBrazeUser` object:

- `SetFirstName`
- `SetLastName`
- `SetEmail`
- `SetDateOfBirth`
- `SetCountry`
- `SetLanguage`
- `SetHomeCity`
- `SetPhoneNumber`
- `SetGender`

### Setting default attributes

To set a default attribute for a user, call the `GetCurrentUser()` method on the shared `UBrazeUser` object to get a reference to the current user of your app. Then you can call methods to set a user attribute.

```cpp
UBraze->GetCurrentUser([](UBrazeUser* BrazeUser) {
    if (BrazeUser) {
        BrazeUser->SetFirstName(TEXT("Alex"));
    }
});
```

## Custom User Attributes

In addition to the default user attributes, Braze also allows you to define custom attributes using several different data types. For more information on each attribute's segmentation option, see [User data collection]({{site.baseurl}}/developer_guide/analytics/).

{% tabs local %}
{% tab string %}
To set a custom attribute with a `string` value:

```cpp
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), TEXT("your_attribute_value"));
```
{% endtab %}

{% tab integer %}
To set a custom attribute with an `integer` value:

```cpp
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), 42);
```
{% endtab %}

{% tab floating-points %}
Braze treats `float` and `double` values the same within our database. To set a custom attribute with a double value:

```cpp
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), 3.14);
```
{% endtab %}

{% tab boolean %}
To set a custom attribute with a `boolean` value:

```cpp
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), true);
```
{% endtab %}

{% tab date %}
To set a custom attribute with a `date` value:

```cpp
FDateTime YourDateTime = FDateTime(2023, 5, 10);
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), YourDateTime);
```
{% endtab %}

{% tab array %}
To set a custom attribute with an `array` value:

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
Custom attribute values have a maximum length of 255 characters; longer values will be truncated. 
{% endalert %}

## Setting user subscriptions

To set up an email or push subscription for your users, you can use the following methods.

### Setting email subscription

```cpp
UBraze->GetCurrentUser([](UBrazeUser* BrazeUser) {
    if (BrazeUser) {
        BrazeUser->SetEmailSubscriptionType(EBrazeSubscriptionType::Subscribed);
    }
});
```

### Setting attribution data

```cpp
UBraze->GetCurrentUser([](UBrazeUser* BrazeUser) {
    if (BrazeUser) {
        BrazeUser->SetPushSubscriptionType(EBrazeSubscriptionType::OptedIn);
    }
});
```
