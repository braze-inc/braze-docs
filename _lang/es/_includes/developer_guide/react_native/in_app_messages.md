{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Tipos de mensajes

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## Modelo de datos

El modelo de mensajes dentro de la aplicación está disponible en el SDK de React Native. Braze tiene cuatro tipos de mensajes dentro de la aplicación que comparten el mismo modelo de datos: **deslizamiento hacia arriba**, **modal**, **completo** y **HTML completo**.

### Mensajes

El modelo de mensajes dentro de la aplicación proporciona la base para todos los mensajes dentro de la aplicación.

|Propiedad          | Descripción                                                                                                            |
|------------------|------------------------------------------------------------------------------------------------------------------------|
|`inAppMessageJsonString` | La representación JSON del mensaje.                                                                                |
|`message`         | El texto del mensaje.                                                                                                      |
|`header`          | La cabecera del mensaje.                                                                                                    |
|`uri`             | La URI asociada a la acción de hacer clic en el botón.                                                                       |
|`imageUrl`        | La URL de la imagen del mensaje.                                                                                                 |
|`zippedAssetsUrl` | Los activos comprimidos preparados para mostrar contenido HTML.                                                                    |
|`useWebView`      | Indica si la acción de hacer clic en el botón debe redirigirse utilizando una vista Web.                                            |
|`duration`        | La duración de la visualización del mensaje.                                                                                          |
|`clickAction`     | El tipo de acción de clic del botón. Los tipos son: `URI`, y `NONE`.                                     |
|`dismissType`     | El tipo de cierre del mensaje. Los dos tipos son: `SWIPE` y `AUTO_DISMISS`.                                                 |
|`messageType`     | El tipo de mensaje dentro de la aplicación admitido por el SDK. Los cuatro tipos son: `SLIDEUP`, `MODAL`, `FULL` y `HTML_FULL`.          |
|`extras`          | El diccionario de extras de mensajes. Valor predeterminado: `[:]`.                                                                   |
|`buttons`         | La lista de botones del mensaje dentro de la aplicación.                                                                             |
|`toString()`      | El mensaje como representación de una cadena.                                                                                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para una referencia completa del modelo de mensajes dentro de la aplicación, consulta la documentación de [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/index.html) e [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage).

### Botones de acción

Se pueden añadir botones a los mensajes dentro de la aplicación para realizar acciones y registrar análisis. El modelo de botón proporciona la base para todos los botones de mensajes dentro de la aplicación.

|Propiedad          | Descripción                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------------------------|
|`text`            | El texto del botón.                                                                                                     |
|`uri`             | La URI asociada a la acción de hacer clic en el botón.                                                                            |
|`useWebView`      | Indica si la acción de hacer clic en el botón debe redirigirse utilizando una vista Web.                                                 |
|`clickAction`     | El tipo de acción de clic que se procesa cuando el usuario hace clic en el botón. Los tipos son: `URI`, y `NONE`. |
|`id`              | El ID del botón del mensaje.                                                                                               |
|`toString()`      | El botón como representación de una cadena.                                                                                      |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para una referencia completa del modelo de botones, consulta la documentación de [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html) e [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/button).
