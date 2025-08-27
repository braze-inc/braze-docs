---
nav_title: Rápido
article_title: Rápido
description: "Este artículo de referencia describe la asociación entre Braze y Quickly, una plataforma de marketing de urgencia, que permite acelerar las conversiones en eventos dentro de un recorrido del cliente Braze."
alias: /partners/quikly/
page_type: partner
search_tag: Partner

---

# Rápido

> [Quikly](https://www.quikly.com), una plataforma de marketing de urgencia, aprovecha la psicología para motivar a los consumidores, de modo que las marcas puedan aumentar inmediatamente la respuesta en torno a sus iniciativas de marketing clave.

_Esta integración está mantenida por Quikly._

## Sobre la integración

La asociación entre Braze y Quikly le permite acelerar las conversiones en eventos dentro de un recorrido del cliente Braze. Quikly lo consigue utilizando la psicología de la urgencia para motivar a los consumidores de forma divertida e instantánea. Por ejemplo, las marcas pueden utilizar Quikly para captar inmediatamente nuevos suscriptores de correo electrónico y SMS directamente en Braze o para motivar otros objetivos de marketing clave como la descarga de su aplicación móvil.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Quikly | Se requiere una cuenta de socio de la marca [Quikly](https://www.quikly.com) para beneficiarse de esta asociación. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.track`, `subscription.status.set`, `users.export.ids` y `subscription.status.get`. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze | [La URL de tu punto final REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto final dependerá de la URL Braze de tu instancia. |
| Clave API de Quikly (opcional) | Una clave de API de Quikly proporcionada por tu administrador de éxito de clientes (sólo webhook). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos prácticos

Quikly permite a las marcas acelerar la adquisición por correo electrónico o SMS y motiva a los suscriptores a proporcionar datos propios directamente dentro de Braze. También puedes utilizar Braze para dirigirte a los clientes que han dejado de serlo con una activación de Quikly que reactive y retenga a esa audiencia. Además, los profesionales del marketing pueden utilizar esta integración para incentivar eventos específicos del recorrido del cliente con estructuras de recompensa únicas. 

Por ejemplo:
 - Genera expectación e interacción a lo largo de los días mientras los consumidores se adhieren voluntariamente para tener la oportunidad de conseguir recompensas emocionantes con [Quikly Hype](https://www.quikly.com/urgency-marketing/platform/product-overview/hype). Los datos de origen se transfieren automáticamente a Braze.
 - Acelere la captación de nuevos suscriptores de correo electrónico y SMS mediante ofertas únicas en tiempo real basadas en la velocidad de respuesta del consumidor, su clasificación frente a otros, de forma aleatoria o antes de que se agote el tiempo o las cantidades con [Quikly Swap](https://www.quikly.com/urgency-marketing/platform/product-overview/swap).
 - Motive pasos específicos en el recorrido del cliente con estructuras de recompensa únicas utilizando webhooks.
 - Aplicar atributos o eventos personalizados al perfil del usuario al participar en una activación Quikly.

## Integración

A continuación se describen cuatro integraciones diferentes: adquisición por correo electrónico, adquisición por SMS, atributos personalizados y webhooks. La integración que elija dependerá de su activación de Quikly y de su caso de uso.

{% tabs %}
{% tab Adquisición por correo electrónico %}

### Adquisición por correo electrónico

Si sus activaciones Quikly recogen direcciones de correo electrónico de clientes o datos de perfil, el único paso necesario es proporcionar a Quikly su clave REST API y punto final. Quikly configurará su cuenta de marca para pasar estos datos a Braze. Si hay atributos de usuario adicionales que le gustaría incluir, menciónelo cuando proporcione las credenciales de la API a Quikly.

Aquí tienes un esquema de cómo Quikly ejecuta este flujo de trabajo.
1. Al participar en una activación de Quikly, Quikly programa una búsqueda de usuarios utilizando la [API de exportación]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) para ver si existe un usuario con un determinado `email_address`.
2. Registrar o actualizar el usuario.
  - Si el usuario existe:
    - No cree un nuevo perfil.
    - Si lo desea, Quikly puede registrar un atributo personalizado en el perfil del usuario para indicar que el usuario participó en la activación.
  - Si el usuario no existe:
    - Quikly crea un perfil de sólo alias a través del [punto final]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) Braze [`/users/track`, estableciendo el correo electrónico del usuario como alias de usuario para hacer referencia a ese usuario en el futuro (ya que el usuario no tendrá un ID externo).]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
    - Si lo desea, Quikly puede registrar eventos personalizados para indicar que este perfil participó en la activación de Quikly.

{% details /usuarios/solicitud de seguimiento %}

#### Encabezado de solicitud
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

#### Cuerpo de la solicitud
```
{
  "attributes": [{
    "_update_existing_only": false,
    "user_alias:": {
      "alias_name": "email@example.com",
      "alias_label: "email"
    },
    "email": "email@example.com"
  }]
}
```

{% enddetails %}

{% endtab %}
{% tab Adquisición de SMS %}

### Suscripciones SMS

Las activaciones de Quikly pueden recopilar números de teléfono móvil directamente de los clientes e iniciar una nueva suscripción por SMS. Para habilitar esta integración, proporciona a tu administrador de éxito de clientes de Quikly la dirección `subscription_group_id`. Puedes acceder a la página `subscription_group_id` de un grupo de suscripción navegando a la página **Grupo de suscripción**.

Quikly realizará una búsqueda de suscripciones utilizando el número de teléfono del cliente y lo acreditará automáticamente en la activación si ya existe una suscripción SMS. En caso contrario, se iniciará una nueva suscripción y, una vez verificado el estado de la misma, se abonará al cliente.

Este es el flujo de trabajo completo cuando un cliente proporciona su número de móvil y su consentimiento a través de Quikly:
1. Quikly realiza una búsqueda de suscripciones utilizando el [estado del grupo de suscripción]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) para ver si un determinado `phone` está suscrito a un `subscription_group_id`. Si existe una suscripción, acredite al usuario en la activación de Quikly. No es necesario adoptar ninguna otra medida.
2. Quikly realiza una búsqueda de usuarios utilizando el [endpoint Exportar perfil de usuario por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) para ver si existe un perfil de usuario con un determinado `email_address`. Si no existe ningún usuario, crea un perfil de sólo alias a través del [punto final]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) Braze [`/users/track`, configurando el correo electrónico del usuario como alias de usuario para hacer referencia a ese usuario en el futuro (ya que el usuario no tendrá un ID externo).]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
3. Actualiza el estado de la suscripción utilizando el [punto final Actualizar el estado del grupo de suscripción del usuario.]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)

Para admitir los flujos de trabajo de suscripción por SMS de opt-in doble existentes, Quikly puede enviar un evento personalizado a Braze en lugar del flujo de trabajo anterior. En ese caso, en lugar de actualizar el estado de la suscripción directamente, el [evento personalizado activa el proceso de doble opt-in]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/) y el estado de la suscripción se controla periódicamente para verificar que el usuario ha optado plenamente antes de acreditarlo en la activación de Quikly.

{% alert important %}
Braze aconseja que, al crear nuevos usuarios a través del punto final `/users/track`, haya un retraso de unos 2 minutos antes de añadir usuarios al grupo de suscripción correspondiente para dar tiempo a Braze a crear completamente el perfil de usuario.
{% endalert %}

{% details Solicitud detallada /subscription/status/set  %}
#### Encabezado de solicitud
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

#### Cuerpo de la solicitud
```
{
  "subscription_group_id": "the-id-of-the-subscription-group",
    "subscription_status": "subscribed",
    "phone": "+13135551212"
  }]
}
```

{% enddetails %}

{% endtab %}
{% tab Atributos personalizados %}
### Atributos personalizados

Dependiendo de tu implementación de Braze, puede que quieras que los eventos dentro de la activación de Quikly pasen en cascada a través de Braze para su posterior procesamiento. Por ejemplo, es posible que desee aplicar un atributo de usuario personalizado basado en qué nivel o incentivo se logró en la activación de Quikly, lo que le permite mostrar la tarjeta de contenido relevante cuando abren su aplicación o inician sesión en su sitio web. Quikly trabajará con usted directamente para implementar estas integraciones.

{% endtab %}
{% tab Webhooks %}
### Webhooks
Utilice webhooks para activar incentivos para eventos específicos en el recorrido del cliente. Por ejemplo, si tiene un evento Braze para cuando un usuario inicia sesión en su aplicación, activa las notificaciones push o utiliza su localizador de tiendas, puede utilizar un webhook para activar una oferta personalizada para ese usuario basada en la configuración de una activación Quikly específica. Ejemplos de tácticas incluyen recompensar al primer número X de usuarios que realizan una acción (como iniciar sesión en su aplicación) con una oferta personalizada o proporcionar una oferta que disminuye en valor a medida que transcurre más tiempo para motivar una respuesta inmediata.

### Crear un webhook Quikly en Braze

Para crear una plantilla de webhook Quikly para futuras campañas o Canvases, navega a **Plantillas** > **Plantillas de webhook** en la plataforma Braze. 

Si desea crear una campaña webhook Quikly única o utilizar una plantilla existente, seleccione **Webhook** en Braze al crear una nueva campaña.

Seleccione **Plantilla en blanco** e introduzca lo siguiente para la URL del webhook y el cuerpo de la solicitud:
- **URL del webhook**: https://api.quikly.com/webhook/braze
- **Cuerpo de la solicitud**: Pares clave/valor JSON

#### Encabezados de solicitud y método

Quikly requiere un `HTTP Header` para la autorización.

- **Método HTTP**: POST
- **Encabezado de solicitud**:
  - **Autorización**: Portador [PARTNER_AUTHORIZATION_HEADER]
  - **Content-Type**: application/json

#### Cuerpo de la solicitud

Seleccione ***Pares clave/valor JSON*** y añada los siguientes pares:
{% raw %}
```
"q_scope": "your-activations-scope-id"
"event": "your-event-identifier"
"email": {{${email_address}}
```
{% endraw %}

### Vista previa de su solicitud

Previsualiza tu petición en el panel de **previsualización** o navega hasta la pestaña `Test`, donde puedes seleccionar un usuario al azar, un usuario existente o personalizar el tuyo propio para probar tu webhook.

{% alert important %}
Recuerda guardar tu plantilla antes de salir de la página. <br>Las plantillas webhook actualizadas pueden encontrarse en la lista **Plantillas webhook guardadas** al crear una nueva [campaña webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}

{% endtab %}
{% endtabs %}

## Soporte
Ponte en contacto con tu administrador de éxito de clientes de Quikly si tienes alguna pregunta.


