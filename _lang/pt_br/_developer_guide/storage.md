---
nav_title: Armazenamento
article_title: Armazenamento para iOS
page_order: 3.60
page_type: reference
description: "Saiba mais sobre as diferentes propriedades em nível de dispositivo que são armazenadas pelo Braze SDK."
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Armazenamento

> Saiba mais sobre as diferentes propriedades em nível de dispositivo que são armazenadas pelo Braze SDK.

## Propriedades do dispositivo

Por padrão, o Braze coletará as seguintes propriedades em nível de dispositivo para permitir a personalização de mensagens com base no dispositivo, no idioma e no fuso horário:

{% tabs %}
{% tab Android %}
- `AD_TRACKING_ENABLED`
- `ANDROID_VERSION`
- `CARRIER`
- `IS_BACKGROUND_RESTRICTED`
- `LOCALE`
- `MODEL`
- `NOTIFICIATION_ENABLED`
- `RESOLUTION`
- `TIMEZONE`

{% alert note %}
`AD_TRACKING_ENABLED` e `TIMEZONE` não são coletados se forem `null` ou estiverem em branco. `GOOGLE_ADVERTISING_ID` não é coletado automaticamente pelo SDK e deve ser passado via [`setGoogleAdvertisingId`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html).
{% endalert %}
{% endtab %}

{% tab swift %}
- Operadora de dispositivos (consulte a nota sobre a [depreciação do site`CTCarrier` ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty/carrier))
- Localidade do dispositivo
- Modelo do dispositivo
- Versão do sistema operacional do dispositivo
- Status da autorização push
- Opções do visor push
- Push ativado
- Resolução do dispositivo
- Fuso horário do dispositivo

{% alert note %}
O SDK do Braze não coleta o IDFA automaticamente. Os apps podem, opcionalmente, passar o IDFA para a Braze implementando os métodos diretamente abaixo. Os apps precisam obter a aceitação explícita do rastreamento pelo usuário final por meio da estrutura App Tracking Transparency antes de passar o IDFA para a Braze.

1. Para definir o estado de rastreamento de publicidade, use [`set(adTrackingEnabled:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(adtrackingenabled:)/).
2. Para definir o identificador do anunciante (IDFA), use [`set(identifierForAdvertiser:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/).
{% endalert %}
{% endtab %}

{% tab web %}
- `BROWSER`
- `BROWSER_VERSION`
- `LANGUAGE`
- `OS`
- `RESOLUTION`
- `TIME_ZONE`
- `USER_AGENT`
{% endtab %}
{% endtabs %}

Por padrão, todas as propriedades estão ativadas. No entanto, você pode optar por ativar ou desativar esses recursos manualmente. Lembre-se de que alguns recursos do Braze SDK exigem propriedades específicas (como entrega no horário local e fuso horário), portanto, certifique-se de testar sua configuração antes de liberá-la para a produção.

{% tabs %}
{% tab Android %}
Por exemplo, você pode especificar a versão do sistema operacional Android e a localidade do dispositivo a serem incluídos na lista de permissões. Para saber mais, consulte a seção [`setDeviceObjectAllowlistEnabled()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html) e [`setDeviceObjectAllowlist()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html) métodos. 

```java
new BrazeConfig.Builder()
    .setDeviceObjectAllowlistEnabled(true)
    .setDeviceObjectAllowlist(EnumSet.of(DeviceKey.ANDROID_VERSION, DeviceKey.LOCALE));
```
{% endtab %}

{% tab swift %}
Por exemplo, você pode especificar o fuso horário e a coleção de locais a serem permitidos. Para saber mais, consulte a propriedade [`devicePropertyAllowList`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/devicepropertyallowlist) do objeto `configuration`.

{% subtabs %}
{% subtab swift %}

```swift
configuration.devicePropertyAllowList = [.timeZone, .locale]
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
configuration.devicePropertyAllowList = @[
    BRZDeviceProperty.timeZone,
    BRZDeviceProperty.locale
];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab web %}
Por exemplo, você pode especificar o idioma do dispositivo a ser incluído na lista de permissões. Para saber mais, consulte a opção `devicePropertyAllowlist` para [`InitializationOptions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions).

```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("API-KEY", {
    baseUrl: "BASE-URL",
    devicePropertyAllowlist: [ braze.DeviceProperties.LANGUAGE ] // list of `DeviceProperties` you want to collect
});
```
{% endtab %}
{% endtabs %}

{% alert tip %}
Para saber mais sobre as propriedades do dispositivo coletadas automaticamente, consulte [Coleta de dados do SDK]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/).
{% endalert %}

## Armazenamento de cookies (somente na Web) {#cookies}

Depois de [inicializar o SDK do Web Braze](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize), ele criará e armazenará cookies com uma expiração de 400 dias que se renova automaticamente em novas sessões.

Os seguintes cookies são armazenados:

|Cookie|Descrição|Tamanho|
|---|----|---|---|
|`ab.storage.userId.[your-api-key]`|Usado para determinar se o usuário atualmente registrado foi alterado e para associar eventos ao usuário atual.|Com base no tamanho do valor passado para `changeUser`|
|`ab.storage.sessionId.[your-api-key]`|String gerada aleatoriamente usada para determinar se o usuário está iniciando uma sessão nova ou existente para sincronizar mensagens e calcular a análise de dados da sessão.|~200 bytes|
|`ab.storage.deviceId.[your-api-key]`|String gerada aleatoriamente usada para identificar usuários anônimos e para diferenciar os dispositivos dos usuários e ativar o envio de mensagens com base no dispositivo.|~200 bytes|
|`ab.optOut`|Usado para armazenar a preferência de opt-out do usuário quando `disableSDK` é chamado|~40 bytes|
|`ab._gd`|Criado temporariamente (e depois excluído) para determinar o domínio do cookie de nível raiz, o que permite que o SDK funcione corretamente em subdomínios.|n/a|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Desativação de cookies {#disable-cookies}

Para desativar todos os cookies, use a opção [`noCookies`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) ao inicializar o Web SDK. Isso evitará que você associe usuários anônimos que navegam entre subdomínios e resultará em um novo usuário em cada subdomínio.

```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("API-KEY", {
    baseUrl: "BASE-URL",
    noCookies: true
});
```

Para interromper o rastreamento da Braze em geral ou para limpar todos os dados armazenados do navegador, consulte os métodos do SDK [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disableSDK) e [`wipeData`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#wipedata), respectivamente. Esses dois métodos podem ser úteis se um usuário revogar o consentimento ou se você quiser interromper todas as funcionalidades do Braze depois que o SDK já tiver sido inicializado.
