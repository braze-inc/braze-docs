## Controle de tráfego de rede

### Solicitação de políticas de processamento

A Braze permite que o usuário tenha a opção de controlar o tráfego de rede usando os seguintes protocolos:

{% tabs local %}
{% tab automático %}
Por padrão, o valor do enum `RequestPolicy` é definido como `automatic`. Quando definido, as solicitações imediatas do servidor são realizadas quando os dados voltados para o usuário são necessários para os recursos do Braze, como mensagens no app.

O SDK da Braze tratará automaticamente de toda a comunicação com o servidor, incluindo:

- Envio de eventos personalizados e dados de atributos para os servidores Braze
- Atualização de cartões de conteúdo e geofences
- Solicitação de novas mensagens no app

Para minimizar a carga do servidor, a Braze realiza descargas periódicas de novos dados de usuários a cada poucos segundos.
{% endtab %}

{% tab manual %}
Quando o valor do enum `RequestPolicy` é `manual`, ele tem o mesmo desempenho do processamento automático de solicitações, exceto:

- Os atributos personalizados e os dados de eventos personalizados não são automaticamente enviados ao servidor durante a sessão do usuário.
- A Braze ainda realizará solicitações automáticas de rede para recursos internos, como solicitação de mensagens no app, modelos Liquid em mensagens no app, geofences e monitoramento de localização. Para obter mais detalhes, consulte a [documentação](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/api-swift.class/requestpolicy-swift.enum/manual) do site `Braze.Configuration.Api.RequestPolicy.manual`. Quando essas solicitações internas são feitas, os atributos personalizados armazenados localmente e os dados de eventos personalizados podem ser enviados para o servidor Braze, dependendo do tipo de solicitação.
{% endtab %}
{% endtabs %}

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

### Definição da política de processamento de solicitações

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
