---
nav_title: 위치 추적
article_title: 웹에서 위치 추적
platform: Web
page_order: 5
page_type: reference
description: "이 문서에서는 웹에서 위치 추적을 활성화하는 방법을 다룹니다."
tool: Location

---

# 위치 추적

> 이 문서에서는 웹에서 위치 추적을 활성화하는 방법을 다룹니다.

사용자의 현재 위치를 설정하려면, 지리적 위치 API의 [`getCurrentPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition) 메서드를 사용하여 위치 데이터를 Braze에 기록합니다:

```javascript
import * as braze from "@braze/web-sdk";
function success(position) {
  var coords = position.coords;
  braze.getUser().setLastKnownLocation(
    coords.latitude,
    coords.longitude,
    coords.accuracy,
    coords.altitude,
    coords.altitudeAccuracy
  );
}

navigator.geolocation.getCurrentPosition(success);
```

`navigator.geolocation.getCurrentPosition()`을 호출하면 사용자가 이미 권한을 부여하거나 거부하지 않은 경우 즉시 사용자로부터 권한을 요청합니다. 사용자의 마지막 알려진 위치를 설정하는 방법에 대한 자세한 내용은 [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setlastknownlocation)를 참조하세요.

## 단일 위치 로깅

웹 SDK가 Braze 서버로 데이터를 전송할 때, 애플리케이션에서 수동으로 설정하지 않은 경우 사용자의 국가는 IP 주소에서 자동으로 감지됩니다.

### 지속적인 추적

페이지가 로드되는 동안 사용자의 위치를 지속적으로 추적하려면 지리 위치 API의 [`watchPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition) 메서드를 사용합니다. 이 메서드는 사용자의 위치가 업데이트될 때마다 성공 콜백을 호출합니다:

```javascript
function success(position) {
  var coords = position.coords;
  braze.getUser().setLastKnownLocation(
    coords.latitude,
    coords.longitude,
    coords.accuracy,
    coords.altitude,
    coords.altitudeAccuracy
  );
}

navigator.geolocation.watchPosition(success);
```

`navigator.geolocation.watchPosition()`을 호출하면 사용자가 이미 권한을 부여하거나 거부하지 않은 경우 즉시 사용자로부터 권한을 요청합니다. 위치 추적 구성 및 중지에 대한 자세한 내용은 [Mozilla 개발자 설명서](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition)를 참조하세요.

