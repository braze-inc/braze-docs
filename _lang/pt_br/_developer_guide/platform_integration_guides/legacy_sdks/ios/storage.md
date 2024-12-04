---
nav_title: Armazenamento
article_title: Armazenamento para iOS
platform: iOS
page_order: 8.9
page_type: reference
description: "Este artigo de referência descreve as propriedades no nível de dispositivo capturadas pelo Braze iOS SDK."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Armazenamento

Este artigo descreve as diferentes propriedades no nível de dispositivo capturadas ao usar o Braze iOS SDK.

## Propriedades do dispositivo

Por padrão, o Braze coletará as seguintes [propriedades no nível do dispositivo](https://github.com/Appboy/appboy-ios-sdk/blob/16e893f2677af7de905b927505d4101c6fb2091d/AppboyKit/headers/AppboyKitLibrary/Appboy.h#L181) para permitir a personalização de mensagens com base no dispositivo, no idioma e no fuso horário:

* Resolução do dispositivo
* Operadora do dispositivo
* Localidade do dispositivo
* Modelo do dispositivo
* Versão do sistema operacional do dispositivo
* IDFV (opcional com [iOS SDK v5.7.0+](https://github.com/braze-inc/braze-swift-sdk))
* Push ativado
* Fuso horário do dispositivo
* Status da autenticação push
* Rastreamento de anúncios ativado

{% alert note %}
O SDK do Braze não coleta o IDFA automaticamente. Os apps podem, opcionalmente, passar o IDFA para o Braze implementando nosso protocolo `ABKIDFADelegate`. Os apps devem obter a aceitação explícita do usuário final para rastreamento por meio do framework de transparência de rastreamento de apps antes de passar o IDFA para a Braze.
{% endalert %}

Os campos configuráveis do dispositivo são definidos no enum [`ABKDeviceOptions`](https://github.com/Appboy/appboy-ios-sdk/blob/4390e9eac8401bccdb81b053fa54eb87b1f6fcaa/Appboy-tvOS-SDK/AppboyTVOSKit.framework/Headers/Appboy.h#L179). Para desativar ou especificar o campo do dispositivo que você gostaria de incluir na lista de permissões, atribua o bitwise `OR` dos campos desejados a [`ABKDeviceAllowlistKey`](https://github.com/Appboy/appboy-ios-sdk/blob/fed071000722673754da288cace15c1ff8aca432/AppboyKit/include/Appboy.h#L148) no `appboyOptions` de `startWithApiKey:inApplication:withAppboyOptions:`.

Por exemplo, para especificar o fuso horário e o conjunto de locais a serem incluídos na lista de permissões, defina:
```
appboyOptions[ABKDeviceAllowlistKey] = @(ABKDeviceOptionTimezone | ABKDeviceOptionLocale);
```

Por padrão, todos os campos estão ativados. Observe que, sem algumas propriedades, nem todos os recursos funcionarão corretamente. Por exemplo, a entrega no horário local não funcionará sem o fuso horário.

Para ler mais sobre as propriedades do dispositivo coletadas automaticamente, visite nossa [coleta de dados SDK]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/). 
