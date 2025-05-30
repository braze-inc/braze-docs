{% multi_lang_include developer_guide/prerequisites/xamarin.md %}

## 사용자 속성 설정

Braze는 사용자에게 속성을 할당하는 방법을 제공합니다. 대시보드에서 이러한 속성에 따라 사용자를 필터링하고 세분화할 수 있습니다.

### 기본 사용자 속성

Braze에서 자동으로 수집한 사용자 속성을 설정하려면 SDK와 함께 제공되는 세터 메서드를 사용할 수 있습니다. 예를 들어 사용자의 이름을 설정할 수 있습니다:

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

지원되는 속성은 다음과 같습니다:

- 이름
- 성
- 성별
- 생년월일
- 출생지
- 국가
- 전화번호
- 이메일

### 사용자 지정 사용자 속성

Braze는 사전 정의된 사용자 속성 메서드 외에도 애플리케이션의 데이터를 추적하기 위해 `SetCustomUserAttribute`를 사용하는 커스텀 속성도 제공합니다.

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).CurrentUser.SetCustomUserAttribute("custom_attribute_key", true);
```

속성 추적 모범 사례 및 인터페이스에 대한 자세한 내용은 [Android 통합 지침]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android)을 참조하세요.

{% endtab %}
{% tab iOS %}

```csharp
App.braze?.User.SetCustomAttributeWithKey("custom_attribute_key", true);
```

속성 추적 모범 사례 및 인터페이스에 대한 자세한 내용은 [iOS 통합 지침]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift)을 참조하세요.

{% endtab %}
{% endtabs %}
