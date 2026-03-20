{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## 데이터 추적 비활성화

데이터 수집을 비활성화하려면  `disableSDK`메서드를 사용하십시오. 이 메서드를 호출한 후, Braze 소프트웨어 개발 키트는 Braze 서버로 데이터 전송을 중지합니다.

```javascript
Braze.disableSDK();
```

## 데이터 추적 재개

데이터 수집을 중지한 후 다시 시작하려면  `enableSDK`메서드를 사용하십시오.

```javascript
Braze.enableSDK();
```

## 데이터 삭제

기기에 로컬로 저장된 모든 Braze 소프트웨어 개발 키트 데이터를 삭제하려면  `wipeData`메서드를 사용하십시오. 이 메서드를 호출한 후에는 소프트웨어 개발 키트가 비활성화되며, 다시 인에이블먼트를 수행하려면 .`enableSDK`을 사용해야 합니다.

```javascript
Braze.wipeData();
```

## 플러싱 데이터

Braze 서버로 보류 중인 데이터를 즉시 전송하려면 를 사용하십시오`requestImmediateDataFlush`.

```javascript
Braze.requestImmediateDataFlush();
```

## 광고 추적 인에이블먼트

이 기기에서 광고 추적이 인에이블먼트되었는지 Braze에 알리려면  `setAdTrackingEnabled`메서드를 사용하십시오. 소프트웨어 개발 키트는 이 데이터를 자동으로 수집하지 않습니다.

```javascript
Braze.setAdTrackingEnabled(true, "GOOGLE_ADVERTISING_ID");
```

두 번째 매개변수는 Google 광고 ID이며, Android에서만 사용됩니다.

## 추적 허용 목록 업데이트 (iOS 전용)

추적을 위해 선언된 데이터 유형 목록을 업데이트하려면 를 사용하십시오`updateTrackingPropertyAllowList`. 이것은 Android에서 아무 작업도 수행하지 않습니다.

```javascript
Braze.updateTrackingPropertyAllowList({
  adding: [Braze.TrackingProperty.EMAIL, Braze.TrackingProperty.FIRST_NAME],
  removing: [],
  addingCustomEvents: ["my_custom_event"],
  removingCustomEvents: [],
  addingCustomAttributes: ["my_custom_attribute"],
  removingCustomAttributes: []
});
```

자세한 내용은 [개인정보 처리방침을]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest/) 참조하십시오.
