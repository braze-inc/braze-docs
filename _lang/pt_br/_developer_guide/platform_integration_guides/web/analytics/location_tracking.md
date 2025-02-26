---
nav_title: Monitoramento de localização
article_title: Monitoramento de localização para a Web
platform: Web
page_order: 5
page_type: reference
description: "Este artigo aborda como ativar o monitoramento de localização para a Web."
tool: Location

---

# monitoramento de localização

> Este artigo aborda como ativar o monitoramento de localização para a Web.

Para definir o local atual de um usuário, use o método [`getCurrentPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition) da API de geolocalização e registre os dados do local no Braze:

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

A chamada de `navigator.geolocation.getCurrentPosition()` solicitará imediatamente a permissão do usuário, a menos que ele já tenha concedido ou negado a permissão. Consulte os [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setlastknownlocation) para obter informações sobre como definir o último local conhecido do usuário.

## Registro de um único local

Quando o Web SDK envia dados para os servidores Braze, o país do usuário será automaticamente detectado a partir do endereço IP, caso não tenha sido definido manualmente pelo seu aplicativo.

### Rastreamento contínuo

Se quiser rastrear continuamente o local de um usuário durante o carregamento de uma página, use o método [`watchPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition) da API de geolocalização. Esse método invocará o retorno de chamada de sucesso sempre que a localização do usuário for atualizada:

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

A chamada de `navigator.geolocation.watchPosition()` solicitará imediatamente a permissão do usuário, a menos que ele já tenha concedido ou negado a permissão. Consulte [os documentos do desenvolvedor da Mozilla](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition) para obter informações sobre como configurar e interromper o monitoramento de localização.

