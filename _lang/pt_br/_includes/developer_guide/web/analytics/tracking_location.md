## Registro do local atual

Para obter o local atual de um usuário, use o método [`getCurrentPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition) da API de geolocalização. Isso solicitará imediatamente que o usuário permita ou não o rastreamento (a menos que já o tenha feito).

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

Agora, quando os dados são enviados ao Braze, o SDK pode detectar automaticamente o país do usuário usando seu endereço IP. Para saber mais, consulte [setLastKnownLocation()](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setlastknownlocation).

## Monitoramento contínuo da localização

Para monitorar continuamente o local de um usuário durante o carregamento de uma página, use o método [`watchPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition) da API de geolocalização. A chamada desse método solicitará imediatamente que o usuário permita ou não o rastreamento (a menos que já o tenha feito).

Se houver aceitação, um retorno de chamada de sucesso será invocado sempre que o local for atualizado.

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
Para saber como desativar o rastreamento contínuo, consulte [os documentos para desenvolvedores da Mozilla](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition).
{% endalert %}
