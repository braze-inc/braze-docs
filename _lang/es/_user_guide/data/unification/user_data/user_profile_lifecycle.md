---
nav_title: Ciclo de vida del perfil de usuario
article_title: Ciclo de vida del perfil de usuario
page_order: 2
page_type: reference
description: "Este artículo de referencia describe el ciclo de vida del perfil de usuario Braze, y las distintas formas en que se puede identificar y referenciar un perfil de usuario."

---

# Ciclo de vida del perfil de usuario

> Este artículo describe el ciclo de vida del perfil de usuario Braze y las distintas formas de identificar y hacer referencia a un perfil de usuario. Si quieres comprender mejor el ciclo de vida del cliente, consulta nuestro curso de Braze Learning sobre [Mapeado de los ciclos de vida del usuario](https://learning.braze.com/mapping-customer-lifecycles).

Todos los datos persistentes asociados a un usuario se almacenan en su perfil de usuario. Después de crear un perfil de usuario, ya sea a través de la API o después de que el SDK reconozca a un usuario, puedes asignar una serie de parámetros a ese perfil para identificar y hacer referencia a ese usuario. 

Estos parámetros incluyen:

* `braze_id` (asignado por Braze)
* `external_id`
* `email`
* `phone`
* Cualquier número de alias de usuario personalizados que establezcas

## Perfiles de usuario anónimos

Cualquier usuario sin un `external_id` designado se denomina [usuario anónimo]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/). Por ejemplo, podrían ser usuarios que visitaron tu sitio web pero no se registraron, o usuarios que descargaron tu aplicación móvil pero no crearon un perfil.

Inicialmente, cuando el SDK reconoce a un usuario, se crea un perfil de usuario anónimo con un `braze_id` asociado: un identificador único que Braze asigna automáticamente, que no se puede editar y que es específico del dispositivo. Este identificador puede utilizarse para actualizar el perfil de usuario a través de la [API]({{site.baseurl}}/api/endpoints/user_data/).

## Perfiles de usuario identificados

Después de que un usuario sea reconocible en tu aplicación (proporcionando una forma de ID de usuario o dirección de correo electrónico), te sugerimos que asignes un `external_id` al perfil de ese usuario utilizando el método `changeUser` [(Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html)). Un `external_id` te permite identificar el mismo perfil de usuario en varios dispositivos.

Otras ventajas de utilizar un `external_id` son las siguientes: 

- Proporcionar una experiencia de usuario coherente en múltiples dispositivos y plataformas (por ejemplo, no enviar notificaciones de usuario caducas a la tableta Android de un usuario cuando éste es un usuario fiel de la aplicación para iPhone).
- Mejora la precisión de tus análisis confirmando que los usuarios no están creando un nuevo perfil de usuario cada vez que desinstalan y vuelven a instalar, o instalan la aplicación en un dispositivo diferente.
- Habilita la importación de datos de usuario desde fuentes externas a la aplicación utilizando los [puntos finales de]({{site.baseurl}}/api/endpoints/messaging/) [Datos de usuario]({{site.baseurl}}/api/endpoints/user_data/) y dirígete a los usuarios con mensajes transaccionales utilizando nuestros [puntos finales de mensajería]({{site.baseurl}}/api/endpoints/messaging/).
- Busca usuarios individuales utilizando nuestros [filtros]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) "Pruebas" dentro del segmentador, y en la sección [**Buscar usuarios**]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/) página.

### Consideraciones sobre los ID externos

{% alert warning %}
No asignes un `external_id` a un perfil de usuario antes de poder identificarlo de forma única. Después de identificar a un usuario, no puedes revertirlo a anónimo.
<br><br>
Se puede actualizar un `external_id` utilizando el [punto final`/users/external_ids/rename` ]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/). Sin embargo, cualquier intento de configurar un `external_id` diferente durante la sesión de un usuario creará un nuevo perfil de usuario con el nuevo `external_id` asociado. No se transmitirá ningún dato entre los dos perfiles.
{% endalert %} 

#### Riesgo de utilizar un correo electrónico o un correo con hash como ID externo

Utilizar una dirección de correo electrónico o una dirección de correo electrónico con hash como ID externo de Braze puede simplificar la gestión de identidades en todos tus orígenes de datos; sin embargo, es importante tener en cuenta los riesgos potenciales para la privacidad de los usuarios y la seguridad de los datos.

- **Información adivinable:** Las direcciones de correo electrónico son fáciles de adivinar, lo que las hace vulnerables a los ataques.
- **Riesgo de explotación:** Si un usuario malintencionado altera su navegador web para enviar la dirección de correo electrónico de otra persona como ID externo, podría acceder potencialmente a mensajes confidenciales o a información de la cuenta.

### Qué ocurre cuando identificas a usuarios anónimos

Cuando identificas a usuarios anónimos, pueden darse dos situaciones:

1) **Un usuario anónimo se convierte en un nuevo usuario identificado:** <br>Si el `external_id` aún no existe en Braze, el usuario anónimo se convierte en un nuevo usuario identificado y conserva todos los mismos atributos e historial del usuario anónimo. 

2) **Un usuario anónimo se identifica como un usuario ya existente:** <br>Si el `external_id` ya existe en Braze, entonces este usuario se identificó previamente como usuario en el sistema de alguna otra forma, como a través de otro dispositivo (como una tableta) o de datos de usuario importados. 

En otras palabras, ya tienes un perfil de usuario para este usuario. En esta instancia, Braze hará lo siguiente:
1. Dejar huérfano al usuario anónimo
2. Fusiona [campos específicos del]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior) perfil de usuario que no existan ya en el perfil de usuario identificado desde el perfil anónimo
3. Elimina el perfil de usuario anónimo de tu base de usuarios para que no se infle el recuento de usuarios.

Si tanto el usuario anónimo como el usuario conocido tienen nombre de pila, se mantiene el nombre de pila del usuario conocido. Si el usuario conocido tiene un valor nulo y el usuario anónimo tiene un valor, el valor del usuario anónimo se fusiona en el perfil del usuario conocido si el valor entra dentro de estos [campos específicos del perfil de usuario]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior).

Para obtener información sobre cómo configurar un `external_id` con un perfil de usuario, consulta nuestra documentación[(iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=swift), [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=android), [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=web)).

## Alias de usuario

Para referirte a los usuarios mediante identificadores distintos del Braze `external_id`, configura alias de usuario contra un perfil de usuario. Cualquier alias configurado contra un perfil de usuario actuará como complemento del `braze_id` o `external_id` del usuario, en lugar de sustituirlo. No hay límite en el número de alias que puedes establecer en un perfil de usuario.

Cada alias funciona como un par clave-valor que consta de dos partes: un `alias_label`, que define la clave del alias, y un `alias_name`, que define el valor. Un `alias_name` para cualquier etiqueta única debe ser único en toda tu base de usuarios (igual que con `external_id`). Si intentas actualizar un segundo perfil de usuario con una combinación de etiqueta y nombre preexistente, el perfil de usuario no se actualizará.

### Actualización de alias de usuario

Un alias puede actualizarse con un nuevo nombre para una etiqueta determinada después de configurarla, ya sea utilizando nuestros [puntos finales de Datos de usuario]({{site.baseurl}}/developer_guide/rest_api/user_data/#new-user-alias-endpoint) o pasando un nuevo nombre a través del SDK. El alias de usuario será visible al exportar los datos de ese usuario.

\![Dos perfiles de usuario diferentes para usuarios distintos con la misma etiqueta de alias de usuario pero nombres de alias diferentes]({% image_buster /assets/img_archive/Braze_User_aliases.png %})

### Etiquetar usuarios anónimos

Los alias de usuario también te permiten etiquetar a usuarios anónimos con un identificador. Por ejemplo, si un usuario proporciona a tu sitio de comercio electrónico su dirección de correo electrónico pero aún no se ha registrado, la dirección de correo electrónico puede utilizarse como alias para ese usuario anónimo. Estos usuarios pueden ser exportados utilizando sus alias o referenciados por la API.

### Comportamiento de los alias en los perfiles de usuario anónimos

Si un perfil de usuario anónimo con un alias es reconocido posteriormente con un `external_id`, será tratado como un perfil de usuario identificado normal, pero conservará su alias existente y podrá seguir siendo referenciado por ese alias.

### Configuración de alias en perfiles de usuario conocidos

También se puede establecer un alias de usuario en un perfil de usuario conocido para hacer referencia a un usuario conocido mediante otro ID externo conocido. Por ejemplo, un usuario puede tener un ID de herramienta de inteligencia empresarial (como un ID de Amplitude) que desees referenciar dentro de Braze.

Para obtener información sobre cómo configurar un alias de usuario, consulta nuestra documentación para cada plataforma[(iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#aliasing-users), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#aliasing-users), [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#aliasing-users)).

Diagrama del ciclo de vida del perfil de usuario en Braze. Cuando se llama a changeUser() para un usuario anónimo, ese usuario se convierte en un Usuario identificado y los datos se migran a su perfil de usuario identificado. El usuario identificado tiene un ID Braze y un ID externo. En este punto, si se llama a changeUser() de un segundo usuario anónimo, se fusionarán los campos de datos de usuario que no existan ya en el Usuario identificado. Si el Usuario Identificado tiene un alias añadido a su perfil de usuario existente, no se verá afectado ningún dato, pero se convertirá en un Usuario Identificado con alias. Si se llama a changeUser() a un tercer usuario anónimo con la misma etiqueta de alias que el usuario identificado, pero con un nombre de alias distinto, los campos que no existan en el usuario identificado se fusionarán y se mantendrá la etiqueta de alias en el perfil del usuario identificado.]({% image_buster /assets/img_archive/Braze_User_flowchart.png %})

{% alert tip %}
¿Te cuesta imaginarte cómo podría ser el ciclo de vida del perfil de usuario de tus clientes? Visita [Mejores prácticas]({{site.baseurl}}/user_guide/data/user_data_collection/best_practices/) para ver las mejores prácticas de recopilación de datos de usuario.
{% endalert %}

## Caso de uso avanzado

Puedes establecer un nuevo alias de usuario para perfiles de usuario identificadores existentes a través de nuestro SDK y nuestra API utilizando los [puntos finales de Datos de usuario]({{site.baseurl}}/developer_guide/rest_api/user_data/#new-user-alias-endpoint). Sin embargo, los alias de usuario no pueden configurarse a través de la API para un perfil de usuario desconocido existente.

Los alias de usuario también se fusionan en el proceso. Sin embargo, si tanto el usuario que va a quedar huérfano como el usuario de destino tienen un alias con la misma etiqueta, sólo se mantiene el alias del usuario de destino.

Desinstalar y volver a instalar una aplicación generará un nuevo `braze_id` anónimo para ese usuario.

### Solución de problemas con ID de usuario

Todos los ID de usuario pueden utilizarse para encontrar e identificar usuarios dentro de tu panel para realizar pruebas. Para encontrar a tu usuario en el panel de Braze, consulta [Añadir usuarios de prueba]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users).

{% alert important %}
Braze prohibirá o bloqueará a los usuarios con más de 5.000.000 de sesiones ("usuarios ficticios") y dejará de ingerir sus eventos SDK, ya que estos usuarios son generalmente el resultado de una mala integración. Si descubres que esto le ha ocurrido a un usuario legítimo, ponte en contacto con tu director de cuentas Braze.
{% endalert %}