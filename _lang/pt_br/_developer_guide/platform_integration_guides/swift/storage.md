---
nav_title: Armazenamento
article_title: Armazenamento para iOS
platform: Swift
page_order: 8.9
page_type: reference
description: "Este artigo de referência descreve as propriedades em nível de dispositivo capturadas pelo Braze iOS Swift SDK."
---

# Armazenamento

> Este artigo descreve as diferentes propriedades em nível do dispositivo capturadas ao usar o Braze iOS Swift SDK.

## Propriedades do dispositivo

Por padrão, o Braze coletará as seguintes [propriedades no nível do dispositivo](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty) para permitir a personalização de mensagens com base no dispositivo, no idioma e no fuso horário:

* Operadora de dispositivos (consulte a nota sobre a [depreciação do site`CTCarrier` ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty/carrier))
* Localidade do dispositivo
* Modelo do dispositivo
* Versão do sistema operacional do dispositivo
* Status da autorização push
* Opções do visor push
* Push ativado
* Resolução do dispositivo
* Fuso horário do dispositivo

{% alert note %}
O SDK do Braze não coleta o IDFA automaticamente. Os apps podem, opcionalmente, passar o IDFA para a Braze implementando os métodos diretamente abaixo. Os apps precisam obter a aceitação explícita do rastreamento pelo usuário final por meio da estrutura App Tracking Transparency antes de passar o IDFA para a Braze.

1. Para definir o estado de rastreamento de publicidade, use [`set(adTrackingEnabled:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(adtrackingenabled:)/).
2. Para definir o identificador do anunciante (IDFA), use [`set(identifierForAdvertiser:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/).
{% endalert %}

Os campos configuráveis do dispositivo são definidos no enum [`Braze.Configuration.DeviceProperty`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty). Para desativar ou especificar o campo do dispositivo que você gostaria de incluir na lista de permissões, adicione os campos à propriedade [`devicePropertyAllowList`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/devicepropertyallowlist) do objeto `configuration`.

Por exemplo, para especificar o fuso horário e a coleção de locais a serem permitidos, defina:

{% tabs %}
{% tab swift %}

```swift
configuration.devicePropertyAllowList = [.timeZone, .locale]
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
configuration.devicePropertyAllowList = @[
    BRZDeviceProperty.timeZone,
    BRZDeviceProperty.locale
];
```

{% endtab %}
{% endtabs %}

Por padrão, todos os campos estão ativados. Observe que, sem algumas propriedades, nem todos os recursos funcionarão corretamente. Por exemplo, a entrega no horário local não funcionará sem o fuso horário.

Para ler mais sobre as propriedades do dispositivo coletadas automaticamente, visite nossa [coleta de dados SDK]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/).

