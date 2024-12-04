---
nav_title: Controle de tráfego de rede fina
article_title: Controle de tráfego de rede fina para iOS
platform: iOS
page_order: 1
description: "Este artigo aborda a implementação do controle de tráfego de rede fina para o seu app para iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Controle fino do tráfego de rede

## Políticas de processamento de solicitações

A Braze permite que o usuário tenha a opção de controlar o tráfego de rede usando os seguintes protocolos:

### Processamento automático de solicitações

***`ABKRequestProcessingPolicy` valor do enum: `ABKAutomaticRequestProcessing`***

- Esse é o valor **padrão da política de solicitação**.
- O SDK da Braze tratará automaticamente de toda a comunicação com o servidor, incluindo:
    - Envio de eventos personalizados e dados de atributos para os servidores Braze
    - Atualização de cartões de conteúdo e geofences
    - Solicitação de novas mensagens no app
- As solicitações imediatas do servidor são realizadas quando os dados voltados para o usuário são necessários para os recursos do Braze, como mensagens no app.
- Para minimizar a carga do servidor, a Braze realiza descargas periódicas de novos dados de usuários a cada poucos segundos.

Os dados podem ser transferidos manualmente para os servidores Braze a qualquer momento usando o seguinte método:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
[[Appboy sharedInstance] flushDataAndProcessRequestQueue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.flushDataAndProcessRequestQueue()
```

{% endtab %}
{% endtabs %}

### Processamento manual de solicitações

***`ABKRequestProcessingPolicy` valor do enum: `ABKManualRequestProcessing`***

- Esse protocolo é o mesmo que o processamento automático de solicitações, exceto:
    - Os atributos personalizados e os dados de eventos personalizados não são automaticamente enviados ao servidor durante a sessão do usuário.
- A Braze ainda realizará solicitações automáticas de rede para recursos internos, como solicitação de mensagens no app, modelos Liquid em mensagens no app, geofences e monitoramento de localização. Para saber mais, consulte a declaração `ABKRequestProcessingPolicy` em [`Appboy.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h). Quando essas solicitações internas são feitas, os atributos personalizados armazenados localmente e os dados de eventos personalizados podem ser enviados para o servidor Braze, dependendo do tipo de solicitação.

Os dados podem ser transferidos manualmente para os servidores Braze a qualquer momento usando o seguinte método:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
[[Appboy sharedInstance] flushDataAndProcessRequestQueue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.flushDataAndProcessRequestQueue()
```

{% endtab %}
{% endtabs %}

## Definição da política de processamento de solicitações

### Definir política de solicitação na inicialização

Essas políticas podem ser definidas no momento da inicialização do app a partir do método [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24). No dicionário `appboyOptions`, defina `ABKRequestProcessingPolicyOptionKey` conforme mostrado no seguinte snippet:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
NSDictionary *appboyOptions = @{
  // Other entries
  ABKRequestProcessingPolicyOptionKey : @(ABKAutomaticRequestProcessing)
};
```

{% endtab %}
{% tab swift %}

```swift
let appboyOptions: [AnyHashable: Any] = [
  // Other entries
  ABKRequestProcessingPolicyOptionKey: ABKRequestProcessingPolicy.automaticRequestProcessing.rawValue
]
```

{% endtab %}
{% endtabs %}

### Definir política de solicitação em tempo de execução

A política de processamento de solicitações também pode ser definida durante o tempo de execução por meio da propriedade `requestProcessingPolicy` em `Appboy`:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
// Sets the request processing policy to automatic (the default value)
[Appboy sharedInstance].requestProcessingPolicy = ABKAutomaticRequestProcessing;
```

{% endtab %}
{% tab swift %}

```swift
// Sets the request processing policy to automatic (the default value)
Appboy.sharedInstance()?.requestProcessingPolicy = ABKRequestProcessingPolicy.automaticRequestProcessing
```

{% endtab %}
{% endtabs %}

## Desligamento manual da comunicação com o servidor em voo

Se, a qualquer momento, uma comunicação de servidor "em curso" precisar ser interrompida, você deverá chamar o seguinte método:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
[[Appboy sharedInstance] shutdownServerCommunication];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.shutdownServerCommunication();
```

{% endtab %}
{% endtabs %}

Depois de chamar esse método, você deve redefinir o modo de processamento de solicitações para automático. Por isso, recomendamos chamar esse recurso somente se o sistema operacional estiver forçando a interrupção de tarefas em segundo plano ou algo semelhante.

