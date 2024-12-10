---
nav_title: Outras personalizações do SDK
article_title: Outras personalizações do SDK para Swift
platform: Swift
description: "Este documento abrange etapas adicionais para configurar o Braze Swift SDK."
page_order: 3

---

# Outras personalizações do SDK para Swift

> O Braze Swift SDK pode ser configurado modificando as propriedades dos membros do objeto `Braze.Configuration` anexado à sua instância da Braze. Note que a configuração só pode ser feita antes da inicialização da instância da Braze com `Braze(configuration:)`.

Consulte uma lista completa das configurações disponíveis na [documentação da classe Braze.Configuration](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class).

## Nível de log da Braze

O nível de log padrão para o Braze Swift SDK é `.error` no gráfico a seguir. Esse nível é o nível mais mínimo acima do registro totalmente desativado.

Consulte a seguinte lista de níveis de registro disponíveis:

| Rápido       | Objective C              | Descrição                                                       |
|-------------|--------------------------|-------------------------------------------------------------------|
| `.debug`    | `BRZLoggerLevelDebug`    | Registre informações de depuração + `.info` + `.error`                    |
| `.info`     | `BRZLoggerLevelInfo`     | Registre informações gerais do SDK (alterações de usuário, etc.) + `.error`. |
| `.error`    | `BRZLoggerLevelError`    | Erros de registro.                                                       |
| `.disabled` | `BRZLoggerLevelDisabled` | Não ocorre nenhum registro.                                                |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Definição do nível de registro

O nível de registro pode ser atribuído em tempo de execução no seu objeto `Braze.Configuration`:

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
// Enable logging of general SDK information (such as user changes, etc.)
configuration.logger.level = .info
let braze = Braze(configuration: configuration)
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:self.APIKey
                                                                  endpoint:self.apiEndpoint];
// Enable logging of general SDK information (such as user changes, etc.)
[configuration.logger setLevel:BRZLoggerLevelInfo];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
```

{% endtab %}
{% endtabs %}

Para uso total do Braze Logger, consulte a [documentação da classe Logger](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/logger-swift.class).

