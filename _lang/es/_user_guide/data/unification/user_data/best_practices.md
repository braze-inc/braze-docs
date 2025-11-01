---
nav_title: Buenas prácticas de recogida
article_title: Buenas prácticas de recogida
page_order: 3.1
page_type: reference
description: "El siguiente artículo ayuda a aclarar los distintos métodos y las mejores prácticas para recopilar datos de usuario nuevos y existentes."

---

# Buenas prácticas de recogida

> Saber cuándo y cómo recopilar datos de usuario para usuarios conocidos y desconocidos puede ser todo un reto cuando te planteas el ciclo de vida del perfil de usuario de tus clientes. Este artículo ayuda a aclarar los diferentes métodos y las mejores prácticas para recopilar datos de usuarios nuevos y existentes guiándote a través de un caso de uso.

El siguiente ejemplo es un caso de uso de recopilación de datos por correo electrónico, pero la lógica se aplica a muchos escenarios diferentes de recopilación de datos. En este ejemplo, suponemos que ya has integrado un formulario de registro o una forma de recopilar información del usuario. 

Después de que un usuario proporcione información para que la registres, te recomendamos que compruebes si los datos ya existen en tu base de datos y, cuando sea necesario, crees un perfil de alias de usuario o actualices el perfil de usuario existente.

Si un usuario desconocido visitara tu sitio y, más adelante, creara una cuenta o se identificara a través del registro por correo electrónico, la fusión de perfiles debe tratarse con cuidado. Según el método que utilices para fusionarte, es posible que se sobrescriba la información de usuario de sólo alias o los datos anónimos.

## Captura de datos de usuario a través de un formulario Web

### Paso 1: Comprueba si el usuario existe

Cuando un usuario introduce contenido a través de un formulario Web, comprueba si ya existe un usuario con ese correo electrónico en tu base de datos. Esto puede hacerse de dos maneras:

- **Comprueba la base de datos interna (recomendado):** Si tienes un registro externo o una base de datos que contenga la información del usuario proporcionada y que exista fuera de Braze, haz referencia a ella en el momento del envío por correo electrónico o de la creación de la cuenta para confirmar que la información no se ha capturado ya.
- **[`/users/track` punto final]({{site.baseurl}}/api/endpoints/user_data/post_user_track/):** Utiliza `email` como identificador, y se creará un nuevo perfil de usuario si la dirección de correo electrónico aún no existe.

### Paso 2: Registrar o actualizar usuario

- **Si existe un usuario:**
  - No crees un perfil nuevo.
  - Registra un atributo personalizado (por ejemplo, `newsletter_subscribed: true`) en el perfil del usuario para indicar que ha enviado su correo electrónico a través de una suscripción al boletín. Si existen varios perfiles de usuario de Braze con la misma dirección de correo electrónico, se exportarán todos los perfiles.<br><br>
- **Si un usuario no existe:**
  - Crea un perfil sólo para alias a través del [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Este punto final aceptará un [objeto`user_alias` ]({{site.baseurl}}/api/objects_filters/user_alias_object/) y creará un perfil de sólo alias cuando `update_existing_only` esté configurado como `false`. Establece el correo electrónico del usuario como alias de usuario para hacer referencia a ese usuario en el futuro (ya que el usuario no tendrá un `external_id`).

\![Diagrama que muestra el proceso para actualizar un perfil de usuario de sólo alias. Un usuario envía su dirección de correo electrónico y un atributo personalizado, su código postal, en una página de destino de marketing. Una flecha que apunta desde la colección de la página de destino a un perfil de usuario de sólo alias muestra una solicitud de la API Braze al punto final de Seguimiento de usuarios, con el cuerpo de la solicitud conteniendo el nombre de alias del usuario, la etiqueta de alias, el correo electrónico y el código postal. El perfil tiene la etiqueta "Alias Sólo usuario creado en Braze" con los atributos del cuerpo de la solicitud para mostrar los datos que se reflejan en el perfil recién creado.]({% image_buster /assets/img/user_profile_process3.png %}){: style="max-width:90%;"}

## Captura de correos electrónicos de usuarios a través de un formulario de captura de correo electrónico

Utiliza un formulario de captura de correo electrónico para pedir a los usuarios que envíen su dirección de correo electrónico, que se añadirá a su perfil de usuario. Para más información sobre cómo configurar este formulario, consulta [Formulario de captura de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/).
 
## Identificador de usuarios sólo con alias

Al identificar a los usuarios en el momento de la creación de la cuenta, se puede identificar a los usuarios de sólo alias y asignarles un ID externo a través del [punto final`/users/identify` ]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) fusionando el usuario de sólo alias con el perfil conocido. 

Para comprobar si un usuario es sólo alias, [comprueba si el usuario existe](#step-1-check-if-user-exists) en tu base de datos. 
- Si existe un registro externo, puedes llamar al punto final `/users/identify/`. 
- Si el punto final [`/users/export/id` devuelve un]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) `external_id`, puedes llamar al punto final `/users/identify/`.
- Si el punto final no devuelve nada, no debe hacerse una llamada a `/users/identify/`.

## Capturar datos de usuario cuando ya existe información de usuario de sólo alias

Cuando un usuario crea una cuenta o se identifica mediante el registro por correo electrónico, puedes fusionar los perfiles. Para ver una lista de los campos que se pueden fusionar, consulta [Comportamiento de las actualizaciones de fusión]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior).

### Fusionar perfiles de usuario duplicados

A medida que crecen tus datos de usuario, puedes fusionar perfiles de usuario duplicados desde el panel Braze. Estos perfiles duplicados deben encontrarse utilizando la misma consulta de búsqueda. Para más información sobre cómo duplicar perfiles de usuario, consulta [Fusionar perfiles]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#merge-profiles).

También puedes utilizar el [punto final Fusionar usuarios]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) para fusionar un perfil de usuario en otro. 

{% alert note %}
Una vez fusionados los perfiles de usuario, esta acción no puede deshacerse.
{% endalert %}

## Recursos adicionales
- Consulta nuestro artículo sobre el [ciclo de vida del perfil de usuario]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/) Braze para obtener más información.<br>
- Consulta nuestra documentación sobre la configuración de ID de usuario y la llamada al método `changeUser()` para [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=android), [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#suggested-user-id-naming-convention) y [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=web).

