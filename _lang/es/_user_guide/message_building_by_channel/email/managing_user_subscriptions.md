---
nav_title: Suscripciones por correo electrónico
article_title: Suscripciones por correo electrónico
page_order: 6
description: "Este artículo de referencia cubre los distintos estados de suscripción de los usuarios, cómo crear y gestionar grupos de suscripción, y cómo segmentar a los usuarios en función de sus suscripciones."
channel:
  - email

---

# Suscripciones por correo electrónico

> Conoce los distintos estados de suscripción de los usuarios, cómo crear y gestionar grupos de suscripción, y cómo segmentar a los usuarios en función de sus suscripciones.

Este documento sólo tiene fines informativos. No pretende proporcionar, ni puede considerarse que proporcione, asesoramiento jurídico en ningún sentido. El envío de correos electrónicos transaccionales y de marketing puede estar sujeto a requisitos legales específicos. Para asegurarte de que lo haces cumpliendo todas las leyes, normas y reglamentos aplicables específicos de tu empresa, debes pedir consejo a tu asesor jurídico y/o a tu equipo de cumplimiento normativo.

## Estados de suscripción {#subscription-states}

Braze tiene tres estados de suscripción global para los usuarios de correo electrónico (enumerados en la tabla siguiente), que son los guardianes finales entre tus mensajes y tus usuarios. Por ejemplo, los usuarios considerados `unsubscribed` no recibirán mensajes dirigidos al estado de suscripción global de `subscribed` o `opted-in`.

| Estado | Definición |
| ----- | ---------- |
| Adhesión voluntaria | Un usuario ha confirmado explícitamente que desea recibir correo electrónico. Recomendamos un proceso de adhesión voluntaria explícito para obtener el consentimiento de los usuarios para enviar correos electrónicos. |
| Suscrito | Un usuario no se ha dado de baja ni ha optado explícitamente por recibir correos electrónicos. Este es el estado predeterminado de suscripción cuando se crea un perfil de usuario. |
| Cancelar suscripción | Un usuario se ha dado de baja explícitamente de tus envíos electrónicos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Braze no cuenta los cambios de estado de suscripción en tus puntos de datos, globalmente y en torno a los grupos de suscripción.
{% endalert %}

### Direcciones de correo electrónico canceladas

Braze cancelará suscripción automáticamente a cualquier usuario que se dé de baja manualmente de tu correo electrónico a través de un [pie de página personalizado]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer). Si el usuario actualiza su dirección de correo electrónico y en tus ajustes **de Configuración de envío** está habilitada la opción **Reinscribir usuarios cuando actualicen su correo electrónico**, se reanudará el envío normal de correos electrónicos.

Si un usuario ha marcado uno o más de tus correos electrónicos como correo no deseado, Braze sólo enviará correos electrónicos transaccionales a este usuario. En este caso, los correos electrónicos transaccionales se refieren a la opción seleccionada **Enviar a todos los usuarios, incluidos los usuarios dados de baja**, en el paso **Audiencia** objetivo.

{% alert tip %}
Consulta nuestras mejores prácticas de [calentamiento de IP]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/) para saber cómo reactivar la interacción de tus usuarios con eficacia.
{% endalert %}

### Rebotes y correos electrónicos no válidos

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} {% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} 

Cuando una dirección de correo electrónico rebota duro, el estado de suscripción del usuario no se establece automáticamente en "darse de baja". Si una dirección de correo electrónico rebota duro (como cuando un correo electrónico no es válido o no existe), marcaremos la dirección de correo electrónico del usuario como no válida y no intentaremos enviar más correos electrónicos a esa dirección de correo electrónico. Si ese usuario cambia su dirección de correo electrónico, reanudaremos el envío de correos electrónicos a él, ya que su nuevo correo electrónico puede ser válido. Los rebotes blandos se vuelven a intentar automáticamente durante 72 horas.

### Actualización de los estados de suscripción por correo electrónico

Hay cuatro formas de actualizar el estado de suscripción por correo electrónico de un usuario:

#### Integración de SDK

Utiliza el SDK de Braze para actualizar el estado de suscripción de un usuario.

#### API REST

Utiliza el [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para actualizar el [atributo`email_subscribe` ]({{site.baseurl}}/api/objects_filters/user_attributes_object) de un usuario determinado.

#### Perfil de usuario

1. Encuentra al usuario mediante **la Búsqueda de usuarios**. 
2. En la pestaña **"Interacción"**, selecciona los botones " **No suscrito"**, " **Suscrito"** o " **Acepto"** para cambiar el estado de suscripción de ese usuario. 

Si está disponible, el perfil de usuario también muestra una fecha y hora de la última vez que se modificó la suscripción del usuario.

#### Centro de preferencias

El [centro de preferencias](#email-preference-center) Liquid puede incluirse en la parte inferior de tus correos electrónicos, permitiendo a los usuarios optar por recibir o no correos electrónicos. Braze gestiona las actualizaciones del estado de suscripción desde el centro de preferencias.

### Comprobación del estado de la suscripción por correo electrónico

\![Perfil de usuario de John Doe con su estado de suscripción de correo electrónico establecido en Suscrito.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Hay dos formas de comprobar el estado de suscripción al correo electrónico de un usuario con Braze:

1. **Exportación de la API REST:** Utiliza los puntos finales [Exportar]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) [usuarios por]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) [segmento]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) o [Exportar usuarios por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) para exportar perfiles de usuario individuales en formato JSON.
2. **Perfil de usuario:** Busca el perfil del usuario en la página [Buscar usuarios]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/) y, a continuación, selecciona la pestaña **Interacción** para ver y actualizar manualmente el estado de suscripción de un usuario.

Cuando un usuario actualice su dirección de correo electrónico, su estado de suscripción se establecerá como suscrito, a menos que la dirección de correo electrónico actualizada ya exista en otro lugar de un espacio de trabajo Braze.

## Grupos de suscripción

Los grupos de suscripción son filtros de segmentos que pueden filtrar aún más tu audiencia a partir de los [estados de suscripción globales](#subscription-states). Puedes añadir hasta 350 grupos de suscripción por espacio de trabajo. Estos grupos te permiten presentar opciones de suscripción más granulares a los usuarios finales.

Por ejemplo, supongamos que envías varias categorías de campañas por correo electrónico (promocionales, boletines o actualizaciones de productos). En ese caso, puedes utilizar grupos de suscripción para que tus clientes elijan las categorías de correo electrónico a las que quieren suscribirse o cancelar suscripción de forma masiva desde una sola página, utilizando un [centro de preferencias de correo electrónico](#email-preference-center). También puedes utilizar grupos de suscripción para que tus clientes elijan con qué frecuencia quieren recibir tus correos electrónicos, creando grupos de suscripción para correos electrónicos diarios, semanales o mensuales.

Utiliza los [puntos finales de Grupo]({{site.baseurl}}/api/endpoints/subscription_groups) **de suscripción** para gestionar mediante programación los grupos de suscripción que hayas almacenado en el panel de Braze a la página **Grupo de suscripción**.

### Crear un grupo de suscripción

1. Ve a **Audiencia** > Gestión de grupos de suscripción **.**
2. Selecciona **Crear grupo de suscripción por correo electrónico**. 
3. Dale un nombre y una descripción a tu grupo de suscripción.
4. Selecciona **Guardar**. 

Todos los grupos de suscripción se añaden automáticamente a tu centro de preferencias.

\![Campos para crear un grupo de suscripción.]({% image_buster /assets/img/sub_group_create.png %}){: style="max-width:75%"}

### Segmentación con un grupo de suscripción

Cuando crees tus segmentos, establece el nombre del grupo de suscripción como filtro. Esto confirmará que los usuarios que hayan optado por formar parte de tu grupo recibirán tus correos electrónicos. Es ideal para boletines mensuales, cupones, niveles de afiliación y mucho más.

\![Ejemplo de segmentación de usuarios del segmento "Usuarios caducados" con el filtro para usuarios del grupo de suscripción "Correos electrónicos semanales".]({% image_buster /assets/img/segment_sub_group.png %}){: style="max-width:90%"}

### Archivar grupos de suscripción

Los grupos de suscripción archivados no se pueden editar y ya no aparecerán en los filtros de segmentos ni en tu centro de preferencias. Si intentas archivar un grupo que se está utilizando como filtro de segmento en cualquier correo electrónico, campaña o Canvas, recibirás un mensaje de error que te impedirá archivar el grupo hasta que elimines todos sus usos.

Para archivar tu grupo desde la página **Grupos de suscripción**, haz lo siguiente:

1. Busca tu grupo en la lista de grupos de suscripción. 
2. Selecciona **Archivo** en el menú desplegable <i class="fa-solid fa-ellipsis-vertical"></i>.

Braze no procesará ningún cambio de estado de los usuarios de los grupos archivados. Por ejemplo, si archivas el grupo de suscripción 1 mientras Susie está suscrita a él, seguirá "suscrita" a este grupo, aunque haga clic en un enlace para cancelar suscripción (esto no debería importarle a Susie porque el grupo de suscripción 1 está archivado y no puede enviar ningún mensaje utilizándolo).

#### Ver el tamaño de los grupos de suscripción

Puedes consultar el gráfico **Series temporales de grupos de suscripción** en la página **Grupos de suscripción** para ver el tamaño del grupo de suscripción en función del número de usuarios durante un periodo de tiempo. Estos tamaños de grupos de suscripción también son coherentes con otras áreas de Braze, como el cálculo del tamaño de los segmentos.

\![Un ejemplo de gráfico de "Timeseries de grupos de suscripción" del 2 al 11 de diciembre. El gráfico muestra un aumento de ~10 millones en el número de usuarios del 6º al 7º.]({% image_buster /assets/img_archive/subscription_group_graph.png %})

#### Visualización de los grupos de suscripción en los análisis de campaña

Puedes ver el número de usuarios que cambiaron su estado de suscripción (suscritos o cancelados) de una campaña de correo electrónico específica en la página de análisis de esa campaña.

1. En la página **Análisis de** campaña de tu campaña, desplázate hasta la sección **Rendimiento de los mensajes de correo electrónico**.
2. Selecciona la flecha bajo **Grupos de suscripción** para ver el recuento agregado de cambios de estado, tal y como los envían tus clientes.

La página "Rendimiento de los mensajes de correo electrónico" muestra el recuento total de cambios de estado enviados por los clientes.]({% image_buster /assets/img/campaign_analytics_sub_groups.png %})

### Comprobación del grupo de suscripción por correo electrónico de un usuario

- **Perfil de usuario:** Se puede acceder a los perfiles de usuario individuales a través del panel de Braze desde la página [Buscar usuarios]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#access-profiles). Aquí puedes buscar perfiles de usuario por dirección de correo electrónico, número de teléfono o ID externo de usuario. También puedes ver los grupos de suscripción por correo electrónico de un usuario en la pestaña **Interacción**.
- **API REST Braze:** Utiliza el [punto]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) [final]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) [Listar grupos de suscripción de usuario]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) o [Listar estado del grupo de suscripción de usuario]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) para ver los grupos de suscripción del perfil de usuario individual. 

## Centro de preferencias de correo electrónico

El centro de preferencias de correo electrónico es una forma sencilla de gestionar qué usuarios reciben determinados grupos de boletines y se encuentra en el panel, en **Grupos de suscripción**. Cada grupo de suscripción que crees se añade a la lista del centro de preferencias. 

Para saber más sobre cómo añadir o personalizar un centro de preferencias, consulta [Centro de preferencias]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/).

## Cambiar las suscripciones de correo electrónico {#changing-email-subscriptions}

En la mayoría de los casos, tus usuarios gestionarán su suscripción por correo electrónico a través de enlaces de suscripción que se incluyen en los correos electrónicos que reciben. Debes insertar un pie de página conforme a la ley con un enlace para cancelar suscripción al final de cada correo electrónico que envíes. Cuando los usuarios seleccionan la URL de cancelar suscripción en tu pie de página, deben darse de baja y ser llevados a una página de destino que confirme el cambio en su suscripción. Te recomendamos que incluyas esta etiqueta de Liquid: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}.

Ten en cuenta que cuando un usuario selecciona "Cancelar suscripción a todos los tipos de correo electrónico anteriores" en el centro de preferencias de correo electrónico, se actualiza su estado de suscripción global de correo electrónico a `unsubscribed` y se cancela su suscripción a todos los grupos de suscripción.

### Crear pies de página personalizados {#custom-footer}

Si no quieres utilizar el pie de página predeterminado de Braze en tus correos electrónicos, puedes crear un pie de página personalizado para todo el espacio de trabajo, que puedes incluir como plantilla en cada correo electrónico utilizando el atributo {% raw %}`{{${email_footer}}}`{% endraw %} Liquid.

De este modo, no tendrás que crear un pie de página nuevo para cada plantilla de correo electrónico o campaña de correo electrónico que utilices. Para conocer los pasos, consulta [Pie de página de correo electrónico personalizado]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/).

#### Gestión de estados de suscripción para direcciones IP chinas

Si prevés que los destinatarios de tu correo electrónico tendrán una dirección IP china, no debes confiar únicamente en un enlace para cancelar suscripción en tu correo electrónico para mantener tus listas `unsubscribed`. En lugar de eso, proporciona formas alternativas para que los usuarios puedan cancelar la suscripción fácilmente, como abrir un ticket de soporte a través de tu portal de soporte o enviar un correo electrónico a un representante de atención al cliente. 

### Crear una página personalizada para cancelar suscripción

Cuando los usuarios seleccionan una URL de cancelar suscripción en un correo electrónico, se les lleva a una página de destino predeterminada que confirma el cambio en su suscripción.

Para crear una página de destino personalizada a la que se dirigirá a los usuarios (en lugar de la página predeterminada) al suscribirse:

1. Ve a **Preferencias de correo electrónico** > **Páginas de suscripción y pies de página**.
2. Proporciona el HTML para tu página de destino personalizada. 

Recomendamos incluir un enlace de cancelación de suscripción (como {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}) en la página de destino para que los usuarios tengan la opción de volver a suscribirse en caso de que se hayan dado de baja por accidente.

\![Página personalizada para cancelar suscripción con una vista previa "¡Lamento verte marchar!".]({% image_buster /assets/img/custom_unsubscribe.png %})

### Crear una página de adhesión voluntaria personalizada

En lugar de suscribir inmediatamente a un usuario a tus campañas de correo electrónico, crear una página de adhesión voluntaria personalizada puede dar a tus usuarios la oportunidad de reconocer y controlar sus preferencias de notificación. Esta comunicación adicional también puede ayudar a que tus campañas de correo electrónico se mantengan fuera de la carpeta de correo no deseado, ya que tus usuarios habrán optado por la adhesión voluntaria. 

1. Ve a **Configuración** > **Preferencias de correo electrónico**.
2. Selecciona **Páginas de suscripción y Pies de página**.
3. Personaliza el estilo en la sección **Página de adhesión voluntaria personalizada** para ver cómo indica a tus usuarios que se han suscrito.

Los usuarios serán dirigidos a esta página a través de la etiqueta {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %}.

{% alert tip %}
Braze recomienda utilizar un proceso de doble adhesión voluntaria para facilitar la difusión de tu correo electrónico. Este proceso envía un correo electrónico de confirmación adicional en el que el usuario confirmaría de nuevo sus preferencias de notificación mediante un enlace en el correo electrónico. En ese momento, se considera que el usuario ha dado su adhesión voluntaria.
{% endalert %}

\![Envío por correo electrónico de adhesión voluntaria personalizado con el mensaje "Me alegra ver que sigues queriendo saber de nosotros".]({% image_buster /assets/img/custom_optin.png %})

## Suscripciones y segmentación de campañas {#subscriptions-and-campaign-targeting}

Por defecto, las campañas con mensajes push o de correo electrónico se dirigen a los usuarios suscritos o con adhesión voluntaria. Puedes cambiar esta preferencia de segmentación al editar una campaña yendo al paso **Audiencia objetivo** y seleccionando el desplegable junto a **Enviar a estos usuarios:**.

Braze admite tres estados de focalización:

- Usuarios suscritos o con adhesión voluntaria (predeterminado).
- Sólo usuarios con adhesión voluntaria.
- Todos los usuarios, incluidos los que se han cancelado la suscripción.

{% alert important %}
Es tu responsabilidad cumplir las [leyes]({{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations) aplicables [sobre correo no deseado]({{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations) cuando utilices estas configuraciones de orientación.
{% endalert %}

## Segmentación por suscripciones de usuarios {#segmenting-by-user-subscriptions}

Los filtros "Estado de suscripción por correo electrónico" y "Estado de suscripción push" te permiten segmentar a tus usuarios según su estado de suscripción.

Esto puede ser útil si quieres dirigirte a usuarios que no han optado ni por la adhesión ni por la exclusión y animarles a que opten explícitamente por la adhesión voluntaria al correo electrónico o push. En ese caso, crearías un segmento con un filtro para "El estado de suscripción al correo electrónico/ push es suscrito" y las campañas a este segmento irán a los usuarios que estén suscritos, pero no hayan optado por la adhesión voluntaria.

\![Estado de suscripción al correo electrónico utilizado como filtro de segmentos.]({% image_buster /assets/img_archive/not_optin.png %})

