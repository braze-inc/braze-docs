---
nav_title: Controle de tráfego de rede fina
article_title: Controle de tráfego de rede fina para iOS
platform: Swift
page_order: 2
description: "Este artigo aborda a implementação do controle de tráfego de rede fina para o Swift SDK."

---

# Controle fino do tráfego de rede

## Políticas de processamento de solicitações

A Braze permite que o usuário tenha a opção de controlar o tráfego de rede usando os seguintes protocolos:

### Processamento automático de solicitações

***`RequestPolicy` valor do enum: `automatic`***

Esse é o valor **padrão da política de solicitação**. Com esse valor, as solicitações imediatas do servidor são realizadas quando os dados voltados para o usuário são necessários para os recursos do Braze, como mensagens no app.

O SDK da Braze tratará automaticamente de toda a comunicação com o servidor, incluindo:
- Envio de eventos personalizados e dados de atributos para os servidores Braze
- Atualização de cartões de conteúdo e geofences
- Solicitação de novas mensagens no app

Para minimizar a carga do servidor, a Braze realiza descargas periódicas de novos dados de usuários a cada poucos segundos.

### Processamento manual de solicitações

***`RequestPolicy` valor do enum: `manual`***

Esse protocolo é o mesmo que o processamento automático de solicitações, exceto:
- Os atributos personalizados e os dados de eventos personalizados não são automaticamente enviados ao servidor durante a sessão do usuário.
- A Braze ainda realizará solicitações automáticas de rede para recursos internos, como solicitação de mensagens no app, modelos Liquid em mensagens no app, geofences e monitoramento de localização. Para obter mais detalhes, consulte a [documentação](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/api-swift.class/requestpolicy-swift.enum/manual) do site `Braze.Configuration.Api.RequestPolicy.manual`. Quando essas solicitações internas são feitas, os atributos personalizados armazenados localmente e os dados de eventos personalizados podem ser enviados para o servidor Braze, dependendo do tipo de solicitação.

### Limpeza manual dos dados de usuários

Os dados podem ser transferidos manualmente para os servidores Braze a qualquer momento usando o seguinte método:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.requestImmediateDataFlush()
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
[AppDelegate.braze requestImmediateDataFlush];
```

{% endtab %}
{% endtabs %}
## Definição da política de processamento de solicitações

### Definir política de solicitação na inicialização

Essas políticas podem ser definidas no momento da inicialização do app, quando você inicializa a configuração do Braze. No objeto `configuration`, defina o parâmetro [`Braze.Configuration.Api.RequestPolicy`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/api-swift.class/requestpolicy-swift.enum)) conforme mostrado no trecho de código a seguir:

{% tabs %}
{% tab swift %}

```swift
configuration.api.requestPolicy = .automatic
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
configuration.api.requestPolicy = BRZRequestPolicyAutomatic;
```

{% endtab %}
{% endtabs %}


