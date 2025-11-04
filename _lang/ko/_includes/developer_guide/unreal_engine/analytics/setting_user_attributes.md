## 기본 사용자 속성

### Supported attributes

`UBrazeUser` 객체에 다음 속성을 설정해야 합니다:

- `SetFirstName`
- `SetLastName`
- `SetEmail`
- `SetDateOfBirth`
- `SetCountry`
- `SetLanguage`
- `SetHomeCity`
- `SetPhoneNumber`
- `SetGender`

### 기본 속성 설정

사용자에 대한 기본 속성을 설정하려면, 공유 `UBrazeUser` 객체에서 `GetCurrentUser()` 메서드를 호출하여 앱의 현재 사용자에 대한 참조를 가져옵니다. 그런 다음 사용자 속성을 설정하는 메서드를 호출할 수 있습니다.

```cpp
UBraze->GetCurrentUser([](UBrazeUser* BrazeUser) {
    if (BrazeUser) {
        BrazeUser->SetFirstName(TEXT("Alex"));
    }
});
```

## 사용자 지정 사용자 속성

기본 사용자 속성 외에도, Braze는 여러 가지 데이터 유형을 사용하여 커스텀 속성을 정의할 수 있도록 허용합니다. 각 속성의 세분화 옵션에 대한 자세한 내용은 [사용자 데이터 수집]({{site.baseurl}}/developer_guide/analytics/)을 참조하십시오.

{% tabs local %}
{% tab 문자열 %}
`string` 값으로 커스텀 속성을 설정하려면:

```cpp
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), TEXT("your_attribute_value"));
```
{% endtab %}

{% tab 정수 %}
`integer` 값으로 커스텀 속성을 설정하려면:

```cpp
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), 42);
```
{% endtab %}

{% tab 부동 소수점 %}
Braze는 데이터베이스 내에서 `float` 및 `double` 값을 동일하게 처리합니다. 배정밀도 값으로 커스텀 속성을 설정하려면:

```cpp
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), 3.14);
```
{% endtab %}

{% tab 부울 %}
`boolean` 값으로 커스텀 속성을 설정하려면:

```cpp
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), true);
```
{% endtab %}

{% tab 날짜 %}
`date` 값으로 커스텀 속성을 설정하려면:

```cpp
FDateTime YourDateTime = FDateTime(2023, 5, 10);
UBrazeUser->SetCustomUserAttribute(TEXT("your_attribute_key"), YourDateTime);
```
{% endtab %}

{% tab 배열 %}
`array` 값으로 커스텀 속성을 설정하려면:

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
커스텀 속성 값의 최대 길이는 255자이며, 이보다 긴 값은 잘립니다.
{% endalert %}

## 사용자 구독 설정

사용자를 위한 이메일 또는 푸시 구독을 설정하려면, 다음 메서드를 사용할 수 있습니다.

### 이메일 구독 설정

```cpp
UBraze->GetCurrentUser([](UBrazeUser* BrazeUser) {
    if (BrazeUser) {
        BrazeUser->SetEmailSubscriptionType(EBrazeSubscriptionType::Subscribed);
    }
});
```

### 기여도 데이터 설정

```cpp
UBraze->GetCurrentUser([](UBrazeUser* BrazeUser) {
    if (BrazeUser) {
        BrazeUser->SetPushSubscriptionType(EBrazeSubscriptionType::OptedIn);
    }
});
```
