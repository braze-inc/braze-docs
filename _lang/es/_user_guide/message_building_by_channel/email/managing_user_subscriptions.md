---
nav_title: Suscripciones por correo electrónico
article_title: Suscripciones por correo electrónico
page_order: 6
description: "Este artículo de referencia trata los diferentes estados de suscripción de los usuarios, cómo crear y gestionar grupos de suscripción y cómo segmentar a los usuarios en función de sus suscripciones."
channel:
  - email

---

# Suscripciones por correo electrónico

> Infórmate sobre los estados de suscripción de los usuarios, cómo crear y gestionar grupos de suscripción y cómo segmentar a los usuarios en función de sus suscripciones.

Este documento es meramente informativo. No pretende proporcionar, ni puede considerarse que proporcione, asesoramiento jurídico en ningún sentido. El envío de correos electrónicos comerciales y transaccionales puede estar sujeto a requisitos legales específicos. Para asegurarse de que lo hace de conformidad con todas las leyes, normas y reglamentos aplicables específicos de su empresa, debe solicitar el asesoramiento de su asesor jurídico y/o equipo de cumplimiento normativo.

## Estados de suscripción {#subscription-states}

Braze tiene tres estados de suscripción global para usuarios de correo electrónico. Estos estados guardan tus mensajes de los usuarios. Por ejemplo, los usuarios del estado `unsubscribed` no reciben mensajes dirigidos a `subscribed` o `opted-in`.

| Estado | Definición |
| ----- | ---------- |
| Adhesión voluntaria | Un usuario ha confirmado explícitamente que desea recibir correo electrónico. Recomendamos un proceso de opt-in explícito para obtener el consentimiento de los usuarios para enviar correos electrónicos. |
| Suscrito | Un usuario no se ha dado de baja ni ha optado explícitamente por recibir correos electrónicos. Este es el estado de suscripción por defecto cuando se crea un perfil de usuario. |
| No suscrito | Un usuario se ha dado de baja explícitamente de tus correos electrónicos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Braze no cuenta los cambios de estado de suscripción en sus puntos de datos, globalmente y en torno a los grupos de suscripción.
{% endalert %}

### Direcciones de correo electrónico dadas de baja

Braze cancela automáticamente la suscripción de cualquier usuario que se dé de baja manualmente a través de un [pie de página personalizado]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer). Si el usuario actualiza su dirección de correo electrónico y se habilita la opción **Reinscribir usuarios cuando actualicen su correo electrónico** en la **Configuración de envío**, se reanudan los envíos normales.

Si un usuario marca uno o varios de tus correos electrónicos como correo no deseado, Braze sólo envía correos electrónicos transaccionales a ese usuario. Los correos electrónicos transaccionales hacen referencia a la opción **Enviar a todos los usuarios, incluidos los usuarios dados de baja**, en **Audiencia objetivo**.

{% alert tip %}
Consulta nuestras buenas prácticas de [calentamiento de IP]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/) para saber cómo reactivar la interacción de tus usuarios con eficacia.
{% endalert %}

### Rebotes y correos electrónicos no válidos

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} {% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} 

Cuando una dirección de correo electrónico rebota duro, Braze no establece automáticamente el estado de suscripción del usuario en "darse de baja". Si una dirección rebota duro (inválida o no existe), Braze la marca como inválida y no intenta más envíos. Si el usuario cambia su dirección de correo electrónico, Braze reanuda el envío. Braze reintenta los rebotes blandos durante 72 horas.

### Actualización de los estados de suscripción por correo electrónico

Hay cuatro formas de actualizar el estado de suscripción de correo electrónico de un usuario:

#### Integración de SDK

Utiliza el SDK de Braze para actualizar el estado de suscripción de un usuario.

#### API REST

Utiliza el [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para actualizar el [atributo`email_subscribe` ]({{site.baseurl}}/api/objects_filters/user_attributes_object) de un usuario.

#### Perfil del usuario

1. Encuentre el usuario a través de **Buscar Usuarios**. 
2. En **"Interacción"**, selecciona **"No suscrito"**, " **Suscrito"** o **"Adherido"** para cambiar el estado de suscripción del usuario. 

Si está disponible, el perfil de usuario también muestra una marca de tiempo de la última vez que se modificó la suscripción del usuario.

#### Centro de preferencias

Incluye [el centro de preferencias](#email-preference-center) Liquid en la parte inferior de tus correos electrónicos para que los usuarios puedan adherirse o no. Braze gestiona las actualizaciones del estado de suscripción desde el centro de preferencias.

### Comprobación del estado de suscripción al correo electrónico

![Perfil de usuario para John Doe con su estado de suscripción de correo electrónico establecido en Suscrito.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Puedes comprobar el estado de suscripción al correo electrónico de un usuario de las siguientes formas:

1. **Exportación de la API REST:** Utiliza los puntos finales [Exportar usuarios por segmento]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) o [Exportar usuarios por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) para exportar perfiles de usuario individuales en formato JSON.
2. **Perfil del usuario:** Busca el perfil del usuario en la página [Buscar usuarios]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/) y, a continuación, selecciona la pestaña **Interacción** para ver y actualizar manualmente el estado de suscripción de un usuario.

Cuando un usuario actualiza su dirección de correo electrónico, su estado de suscripción se establecerá como suscrito, a menos que la dirección de correo electrónico actualizada ya exista en otra parte de un espacio de trabajo Braze.

## Grupos de suscripción

Los grupos de suscripción son filtros de segmentos que pueden limitar aún más su audiencia a partir de los [estados de suscripción globales](#subscription-states). Puedes añadir hasta 350 grupos de suscripción por espacio de trabajo. Estos grupos le permiten presentar opciones de suscripción más granulares a los usuarios finales.

Por ejemplo, supongamos que envía varias categorías de campañas por correo electrónico (promocionales, boletines o actualizaciones de productos). En ese caso, puede utilizar grupos de suscripción para que sus clientes elijan las categorías de correo electrónico a las que desean suscribirse o darse de baja de forma masiva desde una única página, utilizando un [centro de preferencias de correo electrónico](#email-preference-center). También puede utilizar grupos de suscripción para que sus clientes elijan la frecuencia con la que desean recibir sus correos electrónicos, creando grupos de suscripción para correos diarios, semanales o mensuales.

Utiliza los [puntos finales de Grupo de suscripción]({{site.baseurl}}/api/endpoints/subscription_groups) para gestionar mediante programación los grupos de suscripción que hayas almacenado en el panel de Braze a la página **Grupo de suscripción**.

### Crear un grupo de suscripción

1. Ve a **Audiencia** > Gestión de grupos de suscripción **.**
2. Selecciona **Crear grupo de suscripción por correo electrónico**. 
3. Dale un nombre y una descripción a tu grupo de suscripción.
4. Seleccione **Guardar**. 

Todos los grupos de suscripción se añaden automáticamente a su centro de preferencias.

![Campos para crear un grupo de suscripción.]({% image_buster /assets/img/sub_group_create.png %}){: style="max-width:75%"}

### Segmentar con un grupo de suscripción

Al crear sus segmentos, establezca el nombre del grupo de suscripción como filtro. Esto confirmará que los usuarios que hayan optado por formar parte de su grupo recibirán sus correos electrónicos. Es ideal para boletines mensuales, cupones, niveles de afiliación y mucho más.

![Ejemplo de segmentación de usuarios en el segmento "Usuarios caducados" con el filtro para usuarios del grupo de suscripción "Correos electrónicos semanales".]({% image_buster /assets/img/segment_sub_group.png %}){: style="max-width:90%"}

### Archivar grupos de suscripción

Los grupos de suscripción archivados no se pueden editar y ya no aparecerán en los filtros de segmentos ni en su centro de preferencias. Si intentas archivar un grupo que se está utilizando como filtro de segmento en cualquier correo electrónico, campaña o Canvas, recibirás un mensaje de error que te impedirá archivar el grupo hasta que elimines todos sus usos.

Para archivar tu grupo desde la página **Grupos de suscripción**, haz lo siguiente:

1. Busca tu grupo en la lista de grupos de suscripción. 
2. Selecciona **Archivo** en el menú desplegable <i class="fa-solid fa-ellipsis-vertical"></i>.

Braze no procesa los cambios de estado de los usuarios de grupos archivados. Por ejemplo, si archivas el grupo de suscripción 1 mientras Alex está suscrito a él, Alex seguirá "suscrito" aunque haga clic en un enlace para cancelar suscripción. Esto no importa porque el grupo de suscripción 1 está archivado y no puedes enviar mensajes utilizándolo.

#### Ver el tamaño de los grupos de suscripción

Puedes consultar el gráfico **Series temporales de grupos de suscripción** en la página **Grupos de suscripción** para ver el tamaño del grupo de suscripción en función del número de usuarios durante un periodo de tiempo. Estos tamaños de grupos de suscripción también son coherentes con otras áreas de Braze, como el cálculo del tamaño de los segmentos.

![Un ejemplo de gráfico de "Timeseries de grupos de suscripción" del 2 al 11 de diciembre. El gráfico muestra un aumento de ~10 millones en el número de usuarios del 6º al 7º.]({% image_buster /assets/img_archive/subscription_group_graph.png %})

#### Visualización de los grupos de suscripción en los análisis de campaña

Puedes ver los recuentos de usuarios que cambiaron su estado de suscripción (suscritos o cancelados) de una campaña de correo electrónico específica en la página de análisis de esa campaña.

1. En la página **Análisis de** campaña de tu campaña, desplázate hasta la sección **Rendimiento de los mensajes de correo electrónico**.
2. Selecciona la flecha bajo **Grupos de suscripción** para ver el recuento agregado de cambios de estado, tal y como los envían tus clientes.

![La página "Rendimiento de los mensajes de correo electrónico" muestra el recuento agregado de los cambios de estado enviados por los clientes.]({% image_buster /assets/img/campaign_analytics_sub_groups.png %})

### Comprobación del grupo de suscripción por correo electrónico de un usuario

- **Perfil del usuario:** Se puede acceder a los perfiles de usuario individuales a través del panel Braze desde la página [Buscar usuarios]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#access-profiles). Aquí puede buscar perfiles de usuario por dirección de correo electrónico, número de teléfono o ID de usuario externo. También puedes ver los grupos de suscripción por correo electrónico de un usuario en la pestaña **Interacción**.
- **API REST Braze:** Utiliza el [punto]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) [final]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) [Listar grupos de suscripción de usuario]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) o [Listar estado del grupo de suscripción de usuario]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) para ver los grupos de suscripción del perfil de usuario individual. 

## Centro de preferencias de correo electrónico

El centro de preferencias de correo electrónico te permite gestionar qué usuarios reciben los boletines del grupo de suscripción. Encuéntralo en el panel, en **Grupos de suscripción**. Cada grupo de suscripción creado se añade a la lista del centro de preferencias. 

Para obtener más información sobre cómo añadir o personalizar un centro de preferencias, consulte [Centro de preferencias]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/).

## Cambiar las suscripciones de correo electrónico {#changing-email-subscriptions}

En la mayoría de los casos, los usuarios gestionan su suscripción por correo electrónico a través de enlaces incluidos en los correos que reciben. Inserta un pie de página conforme a la ley con un enlace para cancelar suscripción al final de cada correo electrónico. Cuando los usuarios seleccionan la URL de cancelar suscripción, Braze les cancela la suscripción y muestra una página de destino confirmando el cambio. Incluye esta etiqueta de Liquid: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}.

Cuando un usuario selecciona "Cancelar suscripción a todos los tipos de correos electrónicos anteriores" en el centro de preferencias, Braze establece su estado global de suscripción al correo electrónico en `unsubscribed` y lo cancela de todos los grupos.

### Creación de pies de página personalizados {#custom-footer}

Si no quieres utilizar el pie de página predeterminado, crea un pie de página de correo electrónico personalizado para todo el espacio de trabajo y ponlo como plantilla en cada correo electrónico utilizando {% raw %}`{{${email_footer}}}`{% endraw %}.

Esto te permite evitar crear un pie de página nuevo para cada plantilla de correo electrónico o campaña de correo electrónico. Para ver los pasos, consulta [Pie de página de correo electrónico personalizado]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/).

#### Gestión de estados de suscripción para direcciones IP chinas

Si prevés direcciones IP chinas, no confíes únicamente en un enlace de cancelar suscripción para mantener las listas `unsubscribed`. Proporcionar vías alternativas para cancelar suscripción, como un ticket de soporte o un correo electrónico del representante del cliente. 

### Crear una página de cancelación de suscripción personalizada

Cuando los usuarios seleccionan una URL para cancelar suscripción, Braze muestra una página de destino predeterminada que confirma el cambio.

Para crear una página de destino personalizada (en lugar de la predeterminada) que se muestra tras suscribirse:

1. Ve a **Preferencias de correo electrónico** > **Páginas de suscripción y pies de página**.
2. Proporciona el HTML para tu página de destino personalizada. 

Incluye un enlace de cancelación de suscripción (como {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}) para que los usuarios puedan volver a suscribirse si se dieron de baja por accidente.

![Página personalizada para cancelar suscripción con una vista previa "¡Lamento verte marchar!".]({% image_buster /assets/img/custom_unsubscribe.png %})

### Crear una página de adhesión voluntaria personalizada

Utiliza una página de adhesión voluntaria personalizada para que los usuarios reconozcan y controlen sus preferencias de notificación antes de la suscripción. Esta comunicación adicional puede ayudar a las campañas de correo electrónico a mantenerse fuera de las carpetas de correo no deseado.

1. Vaya a **Configuración** > **Preferencias de correo electrónico**.
2. Selecciona **Páginas de suscripción y Pies de página**.
3. Personaliza el estilo en la sección **Página de adhesión voluntaria personalizada** para ver cómo indica a tus usuarios que se han suscrito.

Los usuarios llegan a esta página a través de la etiqueta {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %}.

{% alert tip %}
Utiliza un proceso de doble adhesión voluntaria para mejorar el alcance. Braze envía un correo electrónico de confirmación adicional en el que el usuario confirma sus preferencias de notificación mediante un enlace. Tras la confirmación, el usuario queda adherido voluntariamente.
{% endalert %}

![Correo electrónico de adhesión voluntaria personalizado con el mensaje "Me alegra ver que sigues queriendo saber de nosotros".]({% image_buster /assets/img/custom_optin.png %})

## Suscripciones y segmentación de campañas {#subscriptions-and-campaign-targeting}

De forma predeterminada, Braze dirige campañas con mensajes push o de correo electrónico a usuarios suscritos o con adhesión voluntaria. Cámbialo en **Audiencia objetivo** seleccionando el desplegable junto a **Enviar a estos usuarios:**.

Braze admite tres estados de segmentación:

- Usuarios suscritos o inscritos (por defecto).
- Sólo los usuarios que se hayan registrado.
- Todos los usuarios, incluidos los que se han dado de baja.

{% alert important %}
Es tu responsabilidad cumplir las [leyes aplicables]({{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations) sobre correo no deseado cuando utilices estas configuraciones de orientación.
{% endalert %}

## Segmentación por suscripciones de usuarios {#segmenting-by-user-subscriptions}

Utiliza los filtros "Estado de suscripción por correo electrónico" y "Estado de suscripción push" para segmentar a los usuarios por estado de suscripción.

Utilízalo para dirigirte a usuarios que no han optado ni por la adhesión ni por la exclusión, y fomenta una adhesión voluntaria explícita. Crea un segmento con el filtro "El estado de la suscripción por correo electrónico/ push es suscrito" y envía campañas a los usuarios que están suscritos pero no han optado por la suscripción.

![Estado de suscripción al correo electrónico utilizado como filtro de segmento.]({% image_buster /assets/img_archive/not_optin.png %})

