---
nav_title: Establecer ID de usuario
article_title: Establece los ID de usuario a través del SDK de Braze
page_order: 1.1
description: "Aprende a configurar los ID de usuario a través del SDK de Braze."

---

# Establecer ID de usuario

> Aprende a configurar los ID de usuario a través del SDK de Braze. Son identificadores únicos que te permiten realizar el seguimiento de los usuarios en distintos dispositivos y plataformas, importar sus datos a través de la [API de datos de usuario]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) y enviar mensajes dirigidos a través de la [API de mensajería]({{site.baseurl}}/api/endpoints/messaging/). Si no asignas un ID único a un usuario, Braze le asignará un ID anónimo; sin embargo, no podrás utilizar estas características hasta que lo hagas.

{% alert note %}
Para los SDK envolventes que no aparecen en la lista, utiliza el método nativo de Android o SWIFT correspondiente.
{% endalert %}

## Acerca de los usuarios anónimos

{% multi_lang_include anonymous_users/about_anonymous_users.md %}

### Prevenir el seguimiento de usuarios anónimos

Si tu caso de uso requiere que no se recopilen datos antes de que un usuario sea identificado, puedes retrasar la inicialización del SDK de Braze hasta que el usuario inicie sesión y un `external_id` esté disponible. Establece un indicador en tu código que cambie a `true` cuando el usuario inicie sesión, y solo inicializa el SDK cuando ese indicador esté establecido.

{% alert warning %}
Solo retrasa la inicialización la **primera vez** que un usuario descarga tu aplicación (antes de que se establezca un `external_id`). Si impides que el SDK se inicialice cada vez que un usuario cierra sesión o inicia una nueva sesión, interferirá con la precarga de activos de mensajes dentro de la aplicación y tarjetas de contenido, lo que puede provocar errores de capacidad de entrega en esas campañas.
{% endalert %}

## Configuración de un ID de usuario

Para establecer un ID de usuario, llama al método `changeUser()` después de que el usuario inicie sesión por primera vez. Los ID deben ser únicos y seguir nuestras [prácticas recomendadas de nomenclatura](#naming-best-practices).

Si, por el contrario, estás realizando un hash de un identificador único, asegúrate de normalizar la entrada de tu función hash. Por ejemplo, al realizar el hash de una dirección de correo electrónico, elimina los espacios iniciales o finales y ten en cuenta la localización.

{% tabs local %}
{% tab WEB %}
Para una implementación estándar del SDK Web, puedes utilizar el siguiente método:

```javascript
braze.changeUser(YOUR_USER_ID_STRING);
```

Si prefieres utilizar Google Tag Manager, puedes usar el tipo de etiqueta **Cambiar usuario** para llamar al [método `changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser). Úsalo cada vez que un usuario inicie sesión o se identifique con su identificador `external_id` único.

Asegúrate de introducir el ID único del usuario actual en el campo **ID externo del usuario**, que normalmente se rellena utilizando una variable de capa de datos enviada por tu sitio web.

![Un cuadro de diálogo que muestra los ajustes de configuración de la etiqueta de acción Braze. Las configuraciones incluidas son «tipo de etiqueta» e «ID de usuario externo».]({% image_buster /assets/img/web-gtm/gtm-change-user.png %})
{% endtab %}

{% tab ANDROID %}
{% subtabs %}
{% subtab JAVA %}
```java
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING);
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab SWIFT %}
{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.changeUser(userId: "YOUR_USER_ID")
```
{% endsubtab %}
{% subtab objective-c %}
```objc
[AppDelegate.braze changeUser:@"YOUR_USER_ID_STRING"];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab CORDOVA %}
```javascript
BrazePlugin.changeUser("YOUR_USER_ID");
```
{% endtab %}

{% tab ROKU %}
```brightscript
m.Braze.setUserId(YOUR_USER_ID_STRING)
```
{% endtab %}

{% tab UNITY %}
```csharp
AppboyBinding.ChangeUser("YOUR_USER_ID_STRING");
```
{% endtab %}

{% tab REACT NATIVE %}
```javascript
Braze.changeUser("YOUR_USER_ID_STRING");
```
{% endtab %}
{% endtabs %}

### Cómo funciona `changeUser()`

Cuando llamas a `changeUser()`, se aplican los siguientes comportamientos:

- Llamar a `changeUser()` con el **mismo** ID de usuario que ya está establecido no tiene efecto en el recuento de sesiones.
- Llamar a `changeUser()` con un ID de usuario **diferente** finaliza automáticamente la sesión actual e inicia una nueva.
- Cuando un usuario anónimo llama a `changeUser()` con un ID de usuario **nuevo** (que aún no existe en Braze), los datos del perfil anónimo se fusionan con el nuevo perfil identificado.
- Cuando un usuario anónimo llama a `changeUser()` con un ID de usuario **existente**, los datos del perfil anónimo no se fusionan con el perfil identificado.

{% alert note %}
Al llamar a `changeUser()` se desencadena un vaciado de datos como parte del cierre de la sesión del usuario actual. El SDK vacía automáticamente cualquier dato pendiente del usuario anterior antes de cambiar al nuevo usuario, por lo que no es necesario solicitar manualmente un vaciado de datos antes de llamar a `changeUser()`.
{% endalert %}

{% alert warning %}
No asignes un ID de usuario único y compartido (por ejemplo, un ID externo predeterminado estático) ni llames a `changeUser()` cuando un usuario cierre sesión. Hacerlo te impedirá volver a interactuar con cualquier usuario que haya iniciado sesión anteriormente en dispositivos compartidos, y todos los datos se registrarán bajo un único ID de usuario, lo que puede provocar que otras características no funcionen como se espera. En su lugar, realiza el seguimiento de todos los ID de usuario por separado y asegúrate de que el proceso de cierre de sesión de tu aplicación permita volver a un usuario que haya iniciado sesión anteriormente. Cuando se inicia una nueva sesión, Braze actualiza automáticamente los datos del perfil recién activo.
{% endalert %}

## Alias de usuario

### Cómo funcionan

{% multi_lang_include anonymous_users/about_user_aliases.md %}

### Configuración de un alias de usuario

Un alias de usuario consta de dos partes: un nombre y una etiqueta. El nombre hace referencia al identificador en sí, mientras que la etiqueta hace referencia al tipo de identificador al que pertenece. Por ejemplo, si tienes un usuario en una plataforma de atención al cliente de terceros con el ID externo `987654`, puedes asignarle un alias en Braze con el nombre `987654` y la etiqueta `support_id`, para poder realizar el seguimiento en todas las plataformas.

{% tabs local %}
{% tab web %}
```javascript
braze.getUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab java %}
```java
Braze.getInstance(context).getCurrentUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```
{% endsubtab %}

{% subtab kotlin %}
```kotlin
Braze.getInstance(context).currentUser?.addAlias(ALIAS_NAME, ALIAS_LABEL)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
```swift
Appboy.sharedInstance()?.user.addAlias(ALIAS_NAME, ALIAS_LABEL)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
 [[Appboy sharedInstance].user addAlias:ALIAS_NAME withLabel:ALIAS_LABEL];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab rest api %}
```json
{
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```
{% endtab %}

{% tab react native %}
```javascript
Braze.addAlias("ALIAS_NAME", "ALIAS_LABEL");
```
{% endtab %}
{% endtabs %}

## Prácticas recomendadas de nomenclatura de ID {#naming-best-practices}

Te recomendamos que crees ID de usuario utilizando el estándar [UUID (Universally Unique Identifier)](https://en.wikipedia.org/wiki/Universally_unique_identifier), es decir, cadenas de 128 bits aleatorias y bien distribuidas.

Como alternativa, puedes realizar un hash de un identificador único existente (como un nombre o una dirección de correo electrónico) para generar tus ID de usuario. Si lo haces, asegúrate de implementar la [autenticación del SDK]({{site.baseurl}}/developer_guide/sdk_integration/authentication/) para evitar la suplantación de identidad de los usuarios.

{% alert warning %}
No utilices un valor fácil de adivinar ni un número incremental para tu ID de usuario. Esto puede exponer a tu organización a ataques maliciosos o a la filtración de datos.

Para mayor seguridad, utiliza la [autenticación del SDK]({{site.baseurl}}/developer_guide/sdk_integration/authentication/).
{% endalert %}

Aunque es fundamental que nombres correctamente tus ID de usuario desde el principio, siempre puedes renombrarlos en el futuro utilizando el punto de conexión [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/).

| Tipos de ID no recomendados | Ejemplo no recomendado |
| ------------ | ----------- |
| ID de perfil visible del usuario o nombre de usuario | JonDoe829525552 |
| Dirección de correo electrónico | Anna@email.com |
| ID de usuario con autoincremento | 123 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert warning %}
Evita compartir detalles sobre cómo creas los ID de usuario, ya que esto podría exponer a tu organización a ataques maliciosos o a la filtración de datos.
{% endalert %}