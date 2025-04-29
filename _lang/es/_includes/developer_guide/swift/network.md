## Control del tráfico en la red

### Solicitar políticas de tramitación

Braze permite al usuario la opción de controlar el tráfico de red utilizando los siguientes protocolos:

{% tabs local %}
{% tab automático %}
El valor predeterminado de la enumeración `RequestPolicy` es `automatic`. Cuando se establece, se realizan solicitudes inmediatas al servidor cuando se requieren datos orientados al usuario para características de Braze, como mensajes dentro de la aplicación.

El SDK de Braze gestionará automáticamente toda la comunicación con el servidor, que incluye lo siguiente:

- Transmisión de datos de eventos y atributos personalizados a servidores Braze
- Actualización de tarjetas de contenido y geovallas
- Solicitar nuevos mensajes dentro de la aplicación

Para minimizar la carga del servidor, Braze realiza descargas periódicas de nuevos datos de usuario cada pocos segundos.
{% endtab %}

{% tab manual %}
Cuando el valor de la enumeración `RequestPolicy` es `manual`, se realiza lo mismo que el procesamiento automático de solicitudes, excepto:

- Los atributos personalizados y los datos de eventos personalizados no se envían automáticamente al servidor durante toda la sesión de usuario.
- Braze seguirá realizando solicitudes automáticas de red para características internas, como la solicitud de mensajes dentro de la aplicación, la plantilla Liquid en los mensajes dentro de la aplicación, las geovallas y el seguimiento de ubicación. Para más detalles, consulta la [documentación](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/api-swift.class/requestpolicy-swift.enum/manual) de `Braze.Configuration.Api.RequestPolicy.manual`. Cuando se realizan estas solicitudes internas, los atributos personalizados almacenados localmente y los datos de eventos personalizados pueden enviarse al servidor Braze, dependiendo del tipo de solicitud.
{% endtab %}
{% endtabs %}

### Purgar manualmente los datos de usuario

Los datos pueden vaciarse manualmente en los servidores de Braze en cualquier momento utilizando el siguiente método:

{% tabs %}
{% tab swift %}
```swift
AppDelegate.braze?.requestImmediateDataFlush()
```
{% endtab %}
{% tab OBJETIVO-C %}
```objc
[AppDelegate.braze requestImmediateDataFlush];
```
{% endtab %}
{% endtabs %}

### Configuración de la política de procesamiento de solicitudes

Estas políticas pueden establecerse al inicio de la aplicación, cuando inicializas la configuración de Braze. En el objeto `configuration`, establece el parámetro [`Braze.Configuration.Api.RequestPolicy`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/api-swift.class/requestpolicy-swift.enum)) como se muestra en el siguiente fragmento de código:

{% tabs %}
{% tab swift %}
```swift
configuration.api.requestPolicy = .automatic
```
{% endtab %}
{% tab OBJETIVO-C %}
```objc
configuration.api.requestPolicy = BRZRequestPolicyAutomatic;
```
{% endtab %}
{% endtabs %}
