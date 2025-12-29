---
nav_title: Puntos de datos
article_title: Resumen de puntos de datos
page_order: 10
page_type: reference
description: "Este artículo de referencia describe qué son los puntos de datos en Braze y cómo puedes ser consciente de su uso."
search_rank: 6
---

# Puntos de datos

> En Braze, los datos significan acción: cada dato que llega a Braze actualiza la pertenencia a un segmento, puede desencadenar y cancelar la mensajería, está disponible inmediatamente para la personalización de la mensajería, y mucho más. Los puntos de datos te ayudan a definir la información más impactante para tu negocio. Al considerar detenidamente qué información rastrear, te aseguras de que te diriges a los datos de mayor impacto para la experiencia de tus usuarios.

Los puntos de datos se basan en la información registrada en los perfiles de usuario. Puedes encontrar un desglose más detallado de esta definición en tu contrato Braze. Nuestro equipo de Éxito del cliente puede ayudarte a recomendar las mejores prácticas de datos que se ajusten a tus necesidades. 

## Definición

"Puntos de datos" se referirá a una unidad facturable de uso de los Servicios Braze, medida por un inicio de sesión, un final de sesión, un evento personalizado o una compra registrada, así como cualquier atributo establecido en un perfil de usuario final. Para mayor claridad, cada uno de los datos mencionados (como el inicio de sesión, el fin de sesión, el evento personalizado o la compra registrada, así como cualquier atributo) configurado en el perfil de un usuario final en un momento dado contará como un único punto de datos.

Los datos y eventos predeterminados por los Servicios Braze, incluidos, por ejemplo, los tokens de notificaciones push, la información del dispositivo y todos los eventos de seguimiento de la interacción de la campaña, como aperturas de correo electrónico y clics en notificaciones push, *no* se cuentan como puntos de datos.

Consulta la sección [Recuento de consumos](#consumption-count) de este artículo para saber qué datos cuentan para tu asignación de puntos de datos.

## Visualización del uso de punto de datos

Para ver tu uso de punto de datos, ve a **Configuración** > **Facturación** y selecciona la pestaña **Uso total de punto de datos**.

Para más información sobre los componentes del panel de puntos de datos, consulta [Facturación]({{site.baseurl}}/user_guide/administrative/app_settings/subscription_and_usage/).

{% alert tip %}
**No desperdicies puntos de datos. ¡Actualiza sólo los datos cambiantes!**<br><br>
Para minimizar el uso de punto de datos, recomendamos configurar un programa para evitar el envío de los mismos datos invariables y sólo pasar datos nuevos y relevantes a Braze. Braze trabajará contigo para establecer esta mejor práctica durante la incorporación.
{% endalert %}

## Recuento de consumos

En resumen, se acumulan puntos de datos cuando se actualizan los datos del perfil de un usuario o cuando éste realiza acciones específicas. Esencialmente, los puntos de datos son recuentos de cada una de las direcciones `session starts`, `session ends`, `events` y `purchases` de tu usuario.

Puedes encontrar un desglose de cómo Braze acumula puntos de datos en las siguientes secciones. Si alguna vez tienes alguna pregunta sobre los matices de los puntos de datos Braze, tu administrador de cuentas Braze puede responderte.

Las siguientes acciones no registran puntos de datos:
- Eliminar usuarios de Braze
- Utilizar contenido conectado en mensajería
- El estado de suscripción cambia globalmente y en torno a los grupos de suscripción
- Renombrar los ID externos de tus usuarios mediante [llamadas a la API]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/)
- Bloqueo de eventos, atributos o propiedades del evento

### Circunstancias especiales

#### Matrices

Una matriz es una colección ordenada de elementos almacenados dentro de un atributo personalizado. En términos de consumo, actualizar una matriz cuesta un punto de datos por llamada a la API. Si añades valores a una matriz de forma incremental, contará como un punto de datos por valor. 

{% alert tip %}
Si configuras toda la matriz a la vez, contará como un único punto de datos. Como tales, las matrices son una gran herramienta para mantener actualizados los perfiles de usuario con información relevante y reducir costes.
{% endalert %}

#### Atributos personalizados anidados

Los atributos personalizados anidados se refieren a un objeto que define un conjunto de atributos como propiedad de otro atributo. Cada clave del objeto contará como un punto de datos.

{% alert note %}
La actualización de un objeto atributo personalizado a `null` también consume un punto de datos.
{% endalert %}

#### CSV

Los atributos personalizados cargados a través de la importación CSV cuentan para tus puntos de datos. Sin embargo, las importaciones CSV con fines de segmentación (importaciones realizadas con `external_id`, `braze_id`, o `user_alias_name` como único campo) no registrarán puntos de datos.

Además, como los cambios de estado de suscripción no registran puntos de datos, la actualización de los campos `email_subscribe`, `push_subscribe`, `subscription_group_id`, o `subscription_state` de tu archivo CSV no incurrirá en gastos.

## Puntos de datos

{% alert note %}
Las tablas siguientes tienen carácter ilustrativo. Para conocer las convenciones de nomenclatura exactas, las mayúsculas y los valores aceptados para determinados campos, consulta la documentación correspondiente a tu método de ingestión.
{% endalert %}

{% tabs %}
{% tab Non-billable %}

#### Puntos de datos no facturables (predeterminados)

<div class="small_table"></div>

| Tipo de datos | Punto de datos |
| --------- | ---------- |
| Datos del perfil | País |
| Datos del perfil | Lengua |
| Datos del perfil | ID de usuario |
| Datos del perfil | Alias de usuario |
| Dispositivos recientes | Número de dispositivos |
| Dispositivos recientes | Vigilancia más reciente |
| Dispositivos recientes | Versión de la aplicación |
| Dispositivos recientes | Dispositivo |
| Dispositivos recientes | SO del dispositivo |
| Configuración de los contactos | Correo electrónico suscrito |
| Configuración de los contactos | Push suscrito |
| Configuración de los contactos | Aplicaciones registradas para push |
| Configuración de los contactos | Grupo de suscripción |
| Campañas recibidas | Dirección de correo electrónico |
| Atribución de instalación | Instalar fuente |
| Atribución de instalación | Campaña |
| Atribución de instalación | Grupo de anuncios |
| Atribución de instalación | Anuncio |
| Varios | Número de contenedor aleatorio |
| Mensajes de Canvas recibidos | Mensajes de Canvas recibidos |
| Interacción con los mensajes | Todos los eventos de interacción (como aperturas, clics, impresiones y rechazos) |
| Twitter | Seguidores |
| Twitter | Siguiendo |
| Twitter | Número de tweets |
| Facebook | Me gusta |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Billable %}

#### Puntos de datos facturables

{% alert important %}
Añadir, eliminar o actualizar los siguientes tipos de datos supondrá un punto de datos facturable.
{% endalert %}

<style>
table th:nth-child(1) {
    width: 20%;
}
table th:nth-child(2) {
    width: 30%;
}
table th:nth-child(3) {
    width: 50%;
}
table td {
    word-break: break-word;
}
</style>

| Tipo de datos | Punto de datos | Notas |
| --------- | ---------- | ----- |
| Datos del perfil | Nombre | |
| Datos del perfil | Apellidos | |
| Datos del perfil | Dirección de correo electrónico | |
| Datos del perfil | Género | |
| Datos del perfil | Grupo de edad | |
| Datos del perfil | País | Cuando se recoge manualmente. No cuenta para el consumo cuando se recoge automáticamente. |
| Datos del perfil | Ciudad | |
| Datos del perfil | Lengua | Cuando se recoge manualmente. No cuenta para el consumo cuando se recoge automáticamente. |
| Datos del perfil | Localización más reciente del dispositivo | |
| Datos del perfil | Huso horario | |
| Datos del perfil | Fecha de nacimiento | |
| Datos del perfil | Bio | |
| Datos del perfil | Número de teléfono | |
| Datos de uso de la aplicación | Inicio de la sesión | |
| Datos de uso de la aplicación | Fin de sesión | |
| Atributos personalizados | Todos los atributos personalizados | |
| Eventos personalizados | Todos los eventos personalizados | |
| Propiedades del evento personalizadas | Todas las propiedades del evento personalizado | Las propiedades del evento personalizado habilitadas para la segmentación con los filtros `X Custom Event Property in Y Days` o `X Purchase Property in Y Days` se contabilizan como puntos de datos independientes, además del punto de datos contabilizado por el propio evento personalizado.
| Compras | Todas las compras | |
| Propiedades de compra | Todas las propiedades de la compra | |
| Amplitud de la cohorte asignada | Todas las asignaciones | |
| Mixpanel asignación de cohorte | Todas las asignaciones | |
| Asignación de cohorte Hightouch | Todas las asignaciones | |
| Asignación de cohorte Appsflyer | Todas las asignaciones | |
| Ubicación más reciente | Todas las ubicaciones más recientes | Entrar o salir de geovallas no registra puntos de datos porque los datos de geovalla no se almacenan contra el perfil de usuario. Las geovallas son controladas por los servicios de ubicación de Apple y Google; Braze sólo recibe una notificación cuando un usuario desencadena una geovalla. |
| Twitter | Nombre de usuario | |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

