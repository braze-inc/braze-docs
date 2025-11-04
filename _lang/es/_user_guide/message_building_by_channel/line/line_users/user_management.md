---
nav_title: Administración de usuarios
article_title: Gestión de usuarios de LINE
page_order: 0
description: "Este artículo trata sobre el ID de usuario de LINE y cómo configurarlo."
page_type: reference
channel:
 - LINE
alias: /line/user_management/
---

# Gestión de usuarios de LINE

> El ID de usuario de LINE se almacena en el atributo del perfil de usuario llamado `native_line_id`, que se utiliza para enviar mensajes a un usuario en el canal LINE. Este artículo explica cómo configurar y encontrar el atributo `native_line_id`.

Los datos de usuario de los clientes se representan en un [perfil de usuario de Braze]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/). Un perfil de usuario almacena información y atributos sobre los usuarios de una empresa, como nombres de pila y direcciones de correo electrónico. 

Cuando envías mensajes LINE a través de Braze, Braze utiliza el atributo `native_line_id` para identificar a qué usuarios enviar el mensaje. Cuando LINE envía eventos webhook Braze, como cuando un usuario sigue un canal o responde a un mensaje, se utiliza `native_line_id` para buscar el perfil de usuario correspondiente.

{% alert note %}
Los ID de usuario de LINE son distintos según el proveedor de LINE. Un usuario concreto tendrá diferentes ID de usuario de LINE para cada proveedor al que siga. Es poco probable que los usuarios conozcan su ID de LINE (a diferencia de su correo electrónico o número de teléfono), ya que cambian para cada marca que siguen.
{% endalert %}

## Configuración de `native_line_id` attibute

Hay una serie de situaciones en las que `native_line_id` se configura en el perfil de usuario, que se describen a continuación.

| Escenario | Si el perfil de usuario existe con `native_line_id` | Resultado |
| --- | --- | --- |
|Un usuario sigue un canal LINE | No| Se crea un perfil de usuario anónimo (será necesario fusionarlo):<br> - `native_line_id` se ajusta al ID de LÍNEA del usuario <br>- `line_id` el alias de usuario se ajusta al ID de LÍNEA del usuario<br>\- El usuario está suscrito al grupo de suscripción Braze del canal |
|Un usuario sigue un canal LINE| Sí | Todos los perfiles de usuario con la dirección `native_line_id`:<br>\- Están suscritos al grupo de suscripción Braze del canal|
|La empresa utiliza la carga CSV de usuarios con una columna n`ative_line_id` | No| Si no existe ningún perfil de usuario para el `external_id` o alias de usuario especificado:<br>- `native_line_id` se ajusta al valor especificado<br> \- Todos los demás atributos especificados en el CSV se establecen en el perfil de usuario|
|La empresa utiliza la carga CSV de usuarios con una columna `native_line_id`  | Sí | Si existe un perfil de usuario para el `external_id` o alias de usuario especificado:<br>- `native_line_id` se ajusta al valor especificado<br>\- Todos los demás atributos especificados en el CSV se establecen en el perfil de usuario<br>\- Varios perfiles tienen el mismo `native_line_id` |
| La empresa utiliza el punto final `/users/track` y especifica el atributo `native_line_id`  | No | Si no existe ningún perfil de usuario para el usuario especificado[(especificado por `external_id`, `user_alias`, `braze_id` o `email`]({{site.baseurl}}/api/objects_filters/user_attributes_object/)):<br>- `native_line_id` se ajusta al valor especificado<br>\- Todos los demás atributos especificados en la solicitud se establecen en el perfil de usuario |
| La empresa utiliza el punto final `/users/track` y especifica el atributo `native_line_id`  | Sí | Si existe un perfil de usuario para el usuario especificado[(especificado por `external_id`, `user_alias`, `braze_id` o `email`]({{site.baseurl}}/api/objects_filters/user_attributes_object/)):<br>- `native_line_id` se ajusta al valor especificado<br>\- Todos los demás atributos especificados en la solicitud se establecen en el perfil de usuario<br>\- Varios perfiles tienen el mismo `native_line_id` |
| La empresa solicita a Braze que ejecute el sincronizador del estado de la suscripción | No | Si LINE devuelve un ID de usuario que no tiene un perfil de usuario correspondiente en Braze, se crea un perfil de usuario anónimo:<br>- `native_line_id` se ajusta al ID de LÍNEA del usuario<br>- `line_id` el alias de usuario se ajusta al ID de LÍNEA del usuario<br>\- El usuario está suscrito al grupo de suscripción Braze del canal<br><br>Ten en cuenta que si más tarde se crea un usuario con el mismo ID de LINE, habrá usuarios duplicados, pero ambos tendrán el estado de suscripción a LINE correcto. La fusión de usuarios puede limpiar tu base de usuarios en estos casos. |
| La empresa solicita a Braze que ejecute el sincronizador del estado de la suscripción | Sí | Si se devuelve un ID de usuario de LINE que tiene un perfil de usuario correspondiente en Braze:<br>\- El usuario está suscrito al grupo de suscripción Braze del canal |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

## Encontrar la `native_line_id`

Al visualizar un perfil de usuario en el panel de Braze, puedes ver si tiene el atributo `native_line_id` configurado yendo a la pestaña **Interacción** > sección **Configuración de contactos** > sección **LINE**.

Si se ha configurado `native_line_id`, se mostrará en **ID de usuario de LÍNEA**. De lo contrario, no aparecerá.

\![Configuración del contacto de línea en la pestaña Interacción.]({% image_buster /assets/img/line/line_contact_settings.png %}){: style="max-width:50%;"}

