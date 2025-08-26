---
nav_title: Suscripciones por correo electrónico
article_title: Suscripciones por correo electrónico
page_order: 6
description: "Este artículo de referencia trata los diferentes estados de suscripción de los usuarios, cómo crear y gestionar grupos de suscripción y cómo segmentar a los usuarios en función de sus suscripciones."
channel:
  - email

---

# Suscripciones por correo electrónico

> Conozca los distintos estados de suscripción de los usuarios, cómo crear y gestionar grupos de suscripción y cómo segmentar a los usuarios en función de sus suscripciones.

Este documento es meramente informativo. No pretende proporcionar, ni puede considerarse que proporcione, asesoramiento jurídico en ningún sentido. El envío de correos electrónicos comerciales y transaccionales puede estar sujeto a requisitos legales específicos. Para asegurarse de que lo hace de conformidad con todas las leyes, normas y reglamentos aplicables específicos de su empresa, debe solicitar el asesoramiento de su asesor jurídico y/o equipo de cumplimiento normativo.

## Estados de suscripción {#subscription-states}

Braze tiene tres estados de suscripción global para los usuarios de correo electrónico (enumerados en la tabla siguiente), que son los guardianes finales entre tus mensajes y tus usuarios. Por ejemplo, los usuarios considerados `unsubscribed` no recibirán mensajes dirigidos al estado de suscripción global `subscribed` o `opted-in`.

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

Braze cancelará automáticamente la suscripción de cualquier usuario que se dé de baja manualmente de su correo electrónico a través de un [pie de página personalizado]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer). Si el usuario actualiza su dirección de correo electrónico y la opción **Reinscribir usuarios cuando actualicen su correo** electrónico está activada en los ajustes de **Configuración de envío**, se reanudará el envío normal de correo electrónico.

Si un usuario ha marcado uno o más de sus correos electrónicos como spam, Braze sólo enviará correos electrónicos transaccionales a este usuario. En este caso, los correos electrónicos transaccionales se refieren a la opción seleccionada **Enviar a todos los usuarios, incluidos los usuarios dados de baja**, en el paso **Audiencia** objetivo.

{% alert tip %}
Consulta nuestras buenas prácticas de [calentamiento de IP]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/) para saber cómo reactivar la interacción de tus usuarios con eficacia.
{% endalert %}

### Rebotes y correos electrónicos no válidos

{% multi_lang_include metrics.md metric='Hard Bounce' %} {% multi_lang_include metrics.md metric='Soft Bounce' %} 

Cuando una dirección de correo electrónico rebota duro, el estado de suscripción del usuario no se establece automáticamente en "darse de baja". Si una dirección de correo electrónico rebota duro (como cuando un correo electrónico no es válido o no existe), marcaremos la dirección de correo electrónico del usuario como no válida y no intentaremos enviar más correos electrónicos a esa dirección de correo electrónico. Si ese usuario cambia su dirección de correo electrónico, reanudaremos el envío de correos electrónicos a él, ya que su nuevo correo electrónico puede ser válido. Los rebotes suaves se vuelven a intentar automáticamente durante 72 horas.

### Actualización de los estados de suscripción por correo electrónico

Hay cuatro formas de actualizar el estado de suscripción de correo electrónico de un usuario:

#### Integración de SDK

Utiliza el SDK de Braze para actualizar el estado de suscripción de un usuario.

#### API REST

Utiliza el [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para actualizar el [atributo`email_subscribe` ]({{site.baseurl}}/api/objects_filters/user_attributes_object) de un usuario determinado.

#### Perfil del usuario

1. Encuentre el usuario a través de **Buscar Usuarios**. 
2. En la pestaña **"Interacción"**, selecciona los botones " **No suscrito"**, " **Suscrito"** o " **Acepto"** para cambiar el estado de suscripción de ese usuario. 

Si está disponible, el perfil de usuario también muestra una marca de tiempo de la última vez que se modificó la suscripción del usuario.

#### Centro de preferencias

El [centro de preferencias](#email-preference-center) Liquid puede incluirse en la parte inferior de sus correos electrónicos, lo que permite a los usuarios optar por recibirlos o no. Braze gestiona las actualizaciones del estado de suscripción desde el centro de preferencias.

### Comprobación del estado de suscripción al correo electrónico

![Perfil de usuario de John Doe con su estado de suscripción por correo electrónico establecido en Suscrito.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Existen dos formas de comprobar el estado de suscripción al correo electrónico de un usuario con Braze:

1. **Exportación de la API REST:** Utiliza los puntos finales [Exportar usuarios por segmento]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) o [Exportar usuarios por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) para exportar perfiles de usuario individuales en formato JSON.
2. **Perfil del usuario:** Busca el perfil del usuario en la página [Buscar usuarios]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/) y, a continuación, selecciona la pestaña **Interacción** para ver y actualizar manualmente el estado de suscripción de un usuario. 

Cuando un usuario actualiza su dirección de correo electrónico, su estado de suscripción se establecerá como suscrito, a menos que la dirección de correo electrónico actualizada ya exista en otra parte de un espacio de trabajo Braze.

## Grupos de suscripción

Los grupos de suscripción son filtros de segmentos que pueden limitar aún más su audiencia a partir de los [estados de suscripción globales](#subscription-states). Puedes añadir hasta 350 grupos de suscripción por espacio de trabajo. Estos grupos le permiten presentar opciones de suscripción más granulares a los usuarios finales.

Por ejemplo, supongamos que envía varias categorías de campañas por correo electrónico (promocionales, boletines o actualizaciones de productos). En ese caso, puede utilizar grupos de suscripción para que sus clientes elijan las categorías de correo electrónico a las que desean suscribirse o darse de baja de forma masiva desde una única página, utilizando un [centro de preferencias de correo electrónico](#email-preference-center). También puede utilizar grupos de suscripción para que sus clientes elijan la frecuencia con la que desean recibir sus correos electrónicos, creando grupos de suscripción para correos diarios, semanales o mensuales.

Utiliza los [puntos finales de Grupo de suscripción]({{site.baseurl}}/api/endpoints/subscription_groups) para gestionar mediante programación los grupos de suscripción que hayas almacenado en el panel de Braze a la página **Grupo de suscripción**.

### Crear un grupo de suscripción

1. Vaya a **Audiencia** > **Suscripciones**.
2. Selecciona **Crear grupo de suscripción por correo electrónico**. 
3. Dale un nombre y una descripción a tu grupo de suscripción.
4. Seleccione **Guardar**. 

Todos los grupos de suscripción se añaden automáticamente a su centro de preferencias.

![Campos para crear un grupo de suscripción.]({% image_buster /assets/img/sub_group_create.png %}){: style="max-width:75%"}

### Segmentar con un grupo de suscripción

Al crear sus segmentos, establezca el nombre del grupo de suscripción como filtro. Esto confirmará que los usuarios que hayan optado por formar parte de su grupo recibirán sus correos electrónicos. Es ideal para boletines mensuales, cupones, niveles de afiliación y mucho más.

![Ejemplo de segmentación de usuarios del segmento "Usuarios caducados" con el filtro de usuarios del grupo de suscripción "Alertas estables".]({% image_buster /assets/img/segment_sub_group.png %}){: style="max-width:90%"}

### Archivar grupos de suscripción

Los grupos de suscripción archivados no se pueden editar y ya no aparecerán en los filtros de segmentos ni en su centro de preferencias. Si intentas archivar un grupo que se está utilizando como filtro de segmento en cualquier correo electrónico, campaña o Canvas, recibirás un mensaje de error que te impedirá archivar el grupo hasta que elimines todos sus usos.

Para archivar tu grupo desde la página **Grupos de suscripción**, haz lo siguiente:

1. Busca tu grupo en la lista de grupos de suscripción. 
2. Selecciona **Archivo** en el menú desplegable <i class="fa-solid fa-ellipsis-vertical"></i>.

Braze no procesará ningún cambio de estado para usuarios en grupos archivados. Por ejemplo, si archivas el "Grupo de suscripción A" mientras Susie está suscrita a él, seguirá "suscrita" a este grupo, aunque haga clic en un enlace para cancelar suscripción (esto no debería importarle a Susie porque el "Grupo de suscripción A" está archivado y no puede enviar ningún mensaje utilizándolo).

#### Ver el tamaño de los grupos de suscripción

Puedes consultar el gráfico **Series temporales de grupos de suscripción** en la página **Grupos de suscripción** para ver el tamaño del grupo de suscripción en función del número de usuarios durante un periodo de tiempo. Estos tamaños de grupos de suscripción también son coherentes con otras áreas de Braze, como el cálculo del tamaño de los segmentos.

![Un ejemplo de gráfico de "Timeseries de grupos de suscripción" del 2 al 11 de diciembre. El gráfico muestra un aumento de ~10 millones en el número de usuarios del 6º al 7º.]({% image_buster /assets/img_archive/subscription_group_graph.png %})

#### Visualización de los grupos de suscripción en los análisis de campaña

Puede ver el número de usuarios que cambiaron su estado de suscripción (suscritos o dados de baja) de una campaña de correo electrónico específica en la página de análisis de esa campaña.

1. En la página **Análisis de** campaña de tu campaña, desplázate hasta la sección **Rendimiento de los mensajes de correo electrónico**.
2. Selecciona la flecha bajo **Grupos de suscripción** para ver el recuento agregado de cambios de estado, tal y como los envían tus clientes.

![La página "Rendimiento de los mensajes de correo electrónico" muestra el recuento agregado de los cambios de estado enviados por los clientes.]({% image_buster /assets/img/campaign_analytics_sub_groups.png %})

## Centro de preferencias de correo electrónico

El centro de preferencias de correo electrónico es una forma sencilla de gestionar qué usuarios reciben determinados grupos de boletines y se encuentra en el panel de control, en **Grupos de suscripción**. Cada grupo de suscripción creado se añade a la lista del centro de preferencias. 

Para obtener más información sobre cómo añadir o personalizar un centro de preferencias, consulte [Centro de preferencias]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/).

## Cambiar las suscripciones de correo electrónico {#changing-email-subscriptions}

En la mayoría de los casos, sus usuarios gestionarán su suscripción por correo electrónico a través de los enlaces de suscripción que se incluyen en los correos electrónicos que reciben. Debe insertar un pie de página conforme a la ley con un enlace para darse de baja al final de cada correo electrónico que envíe. Cuando los usuarios seleccionan la URL de cancelar suscripción en tu pie de página, deben darse de baja y ser llevados a una página de destino que confirme el cambio en su suscripción. Te recomendamos que incluyas esta etiqueta de Liquid: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}.

Tenga en cuenta que cuando un usuario selecciona "Cancelar suscripción a todos los tipos de correo electrónico anteriores" en el centro de preferencias de correo electrónico, se actualiza su estado de suscripción global de correo electrónico a `unsubscribed` y se cancela su suscripción a todos los grupos de suscripción.

### Creación de pies de página personalizados {#custom-footer}

Si no desea utilizar el pie de página predeterminado de Braze en sus mensajes de correo electrónico, puede crear un pie de página personalizado para todo el espacio de trabajo que puede incluir como plantilla en cada mensaje de correo electrónico utilizando el atributo {% raw %}`{{${email_footer}}}`{% endraw %} Liquid.

De este modo, no tendrá que crear un pie de página nuevo para cada plantilla o campaña de correo electrónico que utilice. Para conocer los pasos, consulte [Pie de página de correo electrónico personalizado]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/).

#### Gestión de estados de suscripción para direcciones IP chinas

Si prevé que los destinatarios de sus correos electrónicos tendrán una dirección IP china, no debería confiar únicamente en un enlace de cancelación de suscripción en su correo electrónico para mantener sus listas de `unsubscribed`. En su lugar, ofrezca a los usuarios otras formas de darse de baja fácilmente, como abrir un ticket de soporte a través de su portal de soporte o enviar un correo electrónico a un representante de atención al cliente. 

### Crear una página de cancelación de suscripción personalizada

Cuando los usuarios seleccionan una URL de cancelar suscripción en un correo electrónico, se les lleva a una página de destino predeterminada que confirma el cambio en su suscripción.

Para crear una página de destino personalizada a la que se dirigirá a los usuarios (en lugar de la página predeterminada) al suscribirse:

1. Ve a **Preferencias de correo electrónico** > **Páginas de suscripción y pies de página**.
2. Proporciona el HTML para tu página de destino personalizada. 

Recomendamos incluir un enlace de resuscripción (como {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}) en la página de destino para que los usuarios tengan la opción de volver a suscribirse en caso de que se hayan dado de baja por accidente.

![Envío por correo electrónico personalizado para cancelar suscripción en el panel Página personalizada de cancelación de suscripción.]({% image_buster /assets/img/custom_unsubscribe.png %})

### Crear una página de adhesión voluntaria personalizada

En lugar de suscribir inmediatamente a un usuario a sus campañas de correo electrónico, la creación de una página de opt-in personalizada puede dar a sus usuarios la oportunidad de reconocer y controlar sus preferencias de notificación. Esta comunicación adicional también puede ayudar a sus campañas de correo electrónico a mantenerse fuera de la carpeta de spam, ya que sus usuarios habrán optado por ser incluidos. 

1. Vaya a **Configuración** > **Preferencias de correo electrónico**.
2. Selecciona **Páginas de suscripción y Pies de página**.
3. Personaliza el estilo en la sección **Página de adhesión voluntaria personalizada** para ver cómo indica a tus usuarios que se han suscrito.

{% alert tip %}
Braze recomienda utilizar un proceso de doble adhesión voluntaria para facilitar la difusión de tu correo electrónico. Este proceso envía un correo electrónico de confirmación adicional en el que el usuario confirmaría de nuevo sus preferencias de notificación a través de un enlace en el correo electrónico. En este punto, se considera que el usuario ha aceptado.
{% endalert %}

## Suscripciones y segmentación de campañas {#subscriptions-and-campaign-targeting}

Por defecto, las campañas con mensajes push o de correo electrónico se dirigen a los usuarios suscritos o con adhesión voluntaria. Puedes cambiar esta preferencia de segmentación al editar una campaña yendo al paso **Audiencia objetivo** y seleccionando el desplegable junto a **Enviar a estos usuarios:**.

Braze admite tres estados de segmentación:

- Usuarios suscritos o inscritos (por defecto).
- Sólo los usuarios que se hayan registrado.
- Todos los usuarios, incluidos los que se han dado de baja.

{% alert important %}
Es tu responsabilidad cumplir las [leyes aplicables]({{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations) sobre correo no deseado cuando utilices estas configuraciones de orientación.
{% endalert %}

## Segmentación por suscripciones de usuarios {#segmenting-by-user-subscriptions}

Los filtros "Estado de suscripción por correo electrónico" y "Estado de suscripción push" te permiten segmentar a tus usuarios según su estado de suscripción.

Esto puede ser útil si quieres dirigirte a usuarios que no han optado ni por la adhesión ni por la exclusión y animarles a que opten explícitamente por la adhesión voluntaria al correo electrónico o push. En ese caso, crearía un segmento con un filtro para "Estado de suscripción de correo electrónico/envío es suscrito" y las campañas a este segmento irían a los usuarios que están suscritos, pero no han optado por ello.

![Estado de la suscripción al correo electrónico utilizado como filtro de segmento.]({% image_buster /assets/img_archive/not_optin.png %})

