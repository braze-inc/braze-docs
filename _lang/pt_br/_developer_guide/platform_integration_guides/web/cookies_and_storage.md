---
nav_title: Cookies e armazenamento
article_title: Cookies e armazenamento para a Web
platform: Web
page_order: 15
page_type: reference
description: "Este artigo de referência descreve os diferentes cookies usados pelo Braze Web SDK."

---

# Cookies e armazenamento

> Este artigo descreve os diferentes cookies usados pelo Braze Web SDK.

Antes de continuar lendo, note que o Braze Web SDK não armazenará nenhum dado no navegador (cookies ou outro tipo de informação) até que seu site [inicialize](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) o SDK.

Além disso, esses valores estão sujeitos a alterações e não devem ser acessados diretamente por meio de sua integração. Em vez disso, consulte nossa [documentação sobre JavaScript](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html) para nossas interfaces de APIs públicas.

{% multi_lang_include archive/web-v4-rename.md %}

## Cookies {#cookies}

Esta seção contém informações sobre como definir e gerenciar cookies no Braze Web SDK. O Braze Web SDK foi desenvolvido para oferecer o máximo de flexibilidade, conformidade legal e relevância no envio de mensagens.

Quando o Braze cria cookies, eles são armazenados com um prazo de validade de 400 dias que é renovado automaticamente em novas sessões.

### Desativação de cookies {#disable-cookies}

Para desativar todos os cookies, use a opção [`noCookies`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) ao inicializar o Web SDK.
A desativação dos cookies impedirá a associação de usuários anônimos que navegam em subdomínios e resultará em um novo usuário em cada subdomínio.

```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("API-KEY", {
    baseUrl: "BASE-URL",
    noCookies: true
});
```

Para interromper o rastreamento da Braze em geral ou para limpar todos os dados armazenados do navegador, consulte os métodos do SDK [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disableSDK) e [`wipeData`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#wipedata), respectivamente. Esses dois métodos podem ser úteis se um usuário revogar o consentimento ou se você quiser interromper todas as funcionalidades do Braze depois que o SDK já tiver sido inicializado.

### Lista de cookies

|Cookie|Descrição|Tamanho|
|---|----|---|---|
|`ab.storage.userId.[your-api-key]`|Usado para determinar se o usuário atualmente registrado foi alterado e para associar eventos ao usuário atual.|Com base no tamanho do valor passado para `changeUser`|
|`ab.storage.sessionId.[your-api-key]`|String gerada aleatoriamente usada para determinar se o usuário está iniciando uma sessão nova ou existente para sincronizar mensagens e calcular a análise de dados da sessão.|~200 bytes|
|`ab.storage.deviceId.[your-api-key]`|String gerada aleatoriamente usada para identificar usuários anônimos e para diferenciar os dispositivos dos usuários e ativar o envio de mensagens com base no dispositivo.|~200 bytes|
|`ab.optOut`|Usado para armazenar a preferência de opt-out do usuário quando `disableSDK` é chamado|~40 bytes|
|`ab._gd`|Criado temporariamente (e depois excluído) para determinar o domínio do cookie de nível raiz, o que permite que o SDK funcione corretamente em subdomínios.|n/a|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Propriedades do dispositivo

Por padrão, o Braze coletará as seguintes propriedades em nível de dispositivo para permitir a personalização de mensagens com base no dispositivo, no idioma e no fuso horário:

* BROWSER
* BROWSER_VERSION
* LANGUAGE
* OS
* RESOLUTION
* TIME_ZONE
* USER_AGENT

Você pode desativar ou especificar as propriedades que deseja coletar, definindo a opção de inicialização `devicePropertyAllowlist` como uma lista de [`DeviceProperties`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.deviceproperties.html). 

```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("API-KEY", {
    baseUrl: "BASE-URL",
    devicePropertyAllowlist: [ braze.DeviceProperties.LANGUAGE ] // list of `DeviceProperties` you want to collect
});
```

Por padrão, todos os campos estão ativados. Observe que, sem algumas propriedades, nem todos os recursos funcionarão corretamente. Por exemplo, a entrega no horário local não funcionará sem o fuso horário.

Para saber mais sobre as propriedades do dispositivo coletadas automaticamente, consulte as [opções de coleta de dados do SDK]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/). 


