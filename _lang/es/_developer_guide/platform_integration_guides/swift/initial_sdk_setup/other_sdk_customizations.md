---
nav_title: Otras personalizaciones del SDK
article_title: Otras personalizaciones del SDK para Swift
platform: Swift
description: "En este documento se cubren los pasos adicionales para configurar el SDK Swift de Braze."
page_order: 3

---

# Otras personalizaciones del SDK para Swift

> El SDK Swift de Braze puede configurarse modificando las propiedades de los miembros del objeto `Braze.Configuration` adjunto a tu instancia de Braze. Ten en cuenta que la configuración sólo puede hacerse antes de inicializar la instancia de Braze con `Braze(configuration:)`.

Para obtener una lista completa de las configuraciones disponibles, consulta la [documentación de la claseBraze.Configuration](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class).

## Nivel de registro Braze

El nivel de registro predeterminado para el SDK Swift de Braze es `.error` en la siguiente tabla. Este nivel es el más mínimo por encima del registro totalmente desactivado.

Consulta la siguiente lista de niveles de registro disponibles:

| Swift       | Objective-C              | Descripción                                                       |
|-------------|--------------------------|-------------------------------------------------------------------|
| `.debug`    | `BRZLoggerLevelDebug`    | Registrar información de depuración + `.info` + `.error`                    |
| `.info`     | `BRZLoggerLevelInfo`     | Registra la información general del SDK (cambios de usuario, etc.) + `.error`. |
| `.error`    | `BRZLoggerLevelError`    | Errores de registro.                                                       |
| `.disabled` | `BRZLoggerLevelDisabled` | No se produce ningún registro.                                                |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Configuración del nivel de registro

El nivel de registro puede asignarse en tiempo de ejecución en tu objeto `Braze.Configuration`:

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
{% tab OBJETIVO-C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:self.APIKey
                                                                  endpoint:self.apiEndpoint];
// Enable logging of general SDK information (such as user changes, etc.)
[configuration.logger setLevel:BRZLoggerLevelInfo];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
```

{% endtab %}
{% endtabs %}

Para conocer el uso completo del [Registrador Braze, consulta la documentación de la clase Registrador](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/logger-swift.class).

