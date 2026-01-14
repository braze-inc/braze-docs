## 현재 위치 기록하기

사용자의 현재 위치를 가져오려면 지리적 위치 API의 [`getCurrentPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition) 메서드를 사용합니다. 이렇게 하면 사용자에게 추적을 허용하거나 허용하지 않을지 묻는 메시지가 즉시 표시됩니다(이미 허용하지 않은 경우).

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

이제 데이터가 Braze로 전송되면 SDK는 사용자의 IP 주소를 사용하여 사용자의 국가를 자동으로 감지할 수 있습니다. 자세한 내용은 [setLastKnownLocation()을](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setlastknownlocation) 참조하세요.

## 지속적인 위치 추적

페이지를 로드하는 동안 사용자의 위치를 지속적으로 추적하려면 지리적 위치 API의 [`watchPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition) 메서드를 사용합니다. 이 메서드를 호출하면 사용자에게 추적을 허용할지 허용하지 않을지 묻는 메시지가 즉시 표시됩니다(이미 허용하지 않은 경우).

옵트인하면 이제 위치가 업데이트될 때마다 성공 콜백이 호출됩니다.

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

{% alert important %}
연속 추적을 비활성화하는 방법을 알아보려면 [Mozilla 개발자 문서를](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition) 참조하세요.
{% endalert %}
