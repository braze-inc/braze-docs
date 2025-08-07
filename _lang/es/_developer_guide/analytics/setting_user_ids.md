---
nav_title: Configuración de ID de usuario
article_title: Configuración de ID de usuario a través del SDK de Braze
page_order: 1.1
description: "Aprende a configurar ID de usuario a través del SDK de Braze."

---

# Configuración de los ID de usuario

> Aprende a configurar ID de usuario a través del SDK de Braze. Son identificadores únicos que te permiten hacer un seguimiento de los usuarios en distintos dispositivos y plataformas, importar sus datos a través de [la API de datos de usuario]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) y enviar mensajes dirigidos a través de la [API de mensajería]({{site.baseurl}}/api/endpoints/messaging/). Si no asignas un ID único a un usuario, Braze le asignará en su lugar un ID anónimo; sin embargo, no podrás utilizar estas características hasta que lo hagas.

{% alert note %}
Para los SDK envoltorio que no aparecen en la lista, utiliza en su lugar el método nativo de Android o Swift correspondiente.
{% endalert %}

## Acerca de los usuarios anónimos

{% multi_lang_include anonymous_users/about_anonymous_users.md %}

## Configuración de un ID de usuario

Para configurar un ID de usuario, llama al método `changeUser()` después de que el usuario se identifique inicialmente. Los ID deben ser únicos y seguir nuestras [mejores prácticas de nomenclatura](#naming-best-practices).

Si, en cambio, vas a aplicar hash a un identificador único, asegúrate de normalizar la entrada de tu función hash. Por ejemplo, al codificar una dirección de correo electrónico, elimina los espacios iniciales o finales y ten en cuenta la localización.

{% tabs local %}
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

{% tab WEB %}
Para una implementación estándar del SDK Web, puedes utilizar el siguiente método:

```javascript
braze.changeUser(YOUR_USER_ID_STRING);
```

Si quieres utilizar Google Tag Manager en su lugar, puedes utilizar el tipo de etiqueta **Cambiar usuario** para llamar al [método`changeUser` ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser). Utilízalo siempre que un usuario se conecte o se identifique de otro modo con su identificador único `external_id`.

Asegúrate de introducir el ID único del usuario actual en el campo **ID externo del usuario**, que normalmente se rellena utilizando una variable de capa de datos enviada por tu sitio web.

![Un cuadro de diálogo que muestra los ajustes de configuración de la etiqueta de acción Braze. Las configuraciones incluidas son "tipo de etiqueta" e "ID externo del usuario".]({% image_buster /assets/img/web-gtm/gtm-change-user.png %})
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

{% tab UNIDAD %}
```csharp
AppboyBinding.ChangeUser("YOUR_USER_ID_STRING");
```
{% endtab %}

{% tab UNREAL ENGINE %}
```cpp
UBraze->ChangeUser(TEXT("YOUR_USER_ID_STRING"));
```
{% endtab %}
{% endtabs %}

{% alert warning %}
**No asignes un ID predeterminado estático ni llames a `changeUser()` cuando un usuario cierra la sesión.** Si lo haces, no podrás reactivar la interacción de ningún usuario que haya iniciado sesión previamente en dispositivos compartidos. En lugar de eso, lleva un seguimiento de todos los ID de usuario por separado y asegúrate de que el proceso de cierre de sesión de tu aplicación permite volver a un usuario que haya iniciado sesión previamente. Cuando se inicie una nueva sesión, Braze actualizará automáticamente los datos del nuevo perfil activo.
{% endalert %}

## Alias de usuario

### Cómo funcionan

{% multi_lang_include anonymous_users/about_user_aliases.md %}

### Configuración de un alias de usuario

Un alias de usuario consta de dos partes: un nombre y una etiqueta. El nombre se refiere al propio identificador, mientras que la etiqueta se refiere al tipo de identificador al que pertenece. Por ejemplo, si tienes un usuario en una plataforma de atención al cliente de terceros con el ID externo `987654`, puedes asignarle un alias en Braze con el nombre `987654` y la etiqueta `support_id`, para que puedas hacer su seguimiento en todas las plataformas.

{% tabs local %}
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

{% tab web %}
```javascript
braze.getUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```
{% endtab %}

{% tab rest api %}
```json
{
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```
{% endtab %}
{% endtabs %}

## Mejores prácticas de denominación de ID {#naming-best-practices}

Te recomendamos que crees ID de usuario utilizando el estándar [Identificador Único Universal (UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) ), lo que significa que son cadenas de 128 bits aleatorias y bien distribuidas.

También puedes utilizar un identificador único existente (como un nombre o una dirección de correo electrónico) para generar tus ID de usuario. Si lo haces, asegúrate de implementar [la autenticación SDK]({{site.baseurl}}/developer_guide/authentication/), para evitar la suplantación de identidad de usuarios.

Aunque es esencial que nombres correctamente tus ID de usuario desde el principio, siempre puedes cambiarles el nombre en el futuro utilizando el punto final [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/) punto final.

| Recomendado | No recomendado |
| ------------ | ----------- |
| 123e4567-e89b-12d3-a456-836199333115 | JonDoe829525552 |
| 8c0b3728-7fa7-4c68-a32e-12de1d3ed2d5 | Anna@email.com |
| f0a9b506-3c5b-4d86-b16a-94fc4fc3f7b0 | CompanyName-1-2-19 |
| 2d9e96a1-8f15-4eaf-bf7b-eb8c34e25962 | jon-doe-1-2-19 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert warning %}
Evita compartir detalles sobre cómo creas ID de usuario, ya que esto puede exponer a tu organización a ataques maliciosos o a la eliminación de datos.
{% endalert %}
