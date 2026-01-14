{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## 사용자 지정 속성 로깅

Braze는 사용자에게 속성을 할당하는 방법을 제공합니다. 대시보드에서 이러한 속성에 따라 사용자를 필터링하고 세분화할 수 있습니다.

### 기본 사용자 속성

Braze에서 자동으로 수집한 사용자 속성을 설정하려면 소프트웨어 개발 키트와 함께 제공되는 세터 메서드를 사용할 수 있습니다.

```javascript
Braze.setFirstName("Name");
```

지원되는 속성은 다음과 같습니다:

- 이름
- 성
- 성별
- 생년월일
- 출생지
- 국가
- 전화번호
- 언어
- 이메일

이름과 성, 국가, 출생지와 같은 모든 문자열 값은 255자로 제한됩니다.

### 사용자 지정 사용자 속성

Braze는 사전 정의된 사용자 속성 메서드 외에도 애플리케이션의 데이터를 추적할 수 있는 [커스텀 속성]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types)도 제공합니다. 

```javascript
Braze.setCustomUserAttribute("attribute_key", "attribute_value", function(){
    // optional onResult callback
});
```

#### 커스텀 속성 설정 해제하기

```javascript
Braze.unsetCustomUserAttribute("attribute_key", function(){
    // optional onResult callback
});
```

#### 사용자 지정 속성 배열

```javascript

// Adds a string to a custom atttribute string array, or creates that array if one doesn't exist.
Braze.addToCustomUserAttributeArray("my-attribute-array", "new or existing value", optionalCallback);

// Removes a string from a custom attribute string array.


Braze.removeFromCustomUserAttributeArray("my-attribute-array", "existing value", optionalCallback);
```
