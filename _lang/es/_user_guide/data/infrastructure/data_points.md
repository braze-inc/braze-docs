---
nav_title: Puntos de datos
article_title: Resumen de puntos de datos
page_order: 10
page_type: reference
description: "Este artículo de referencia describe qué son los puntos de datos en Braze y cómo puedes estar al tanto de su uso."
search_rank: 6
---

# Puntos de datos

> En Braze, los datos significan acción: cada dato que llega a Braze actualiza la pertenencia a un segmento, puede desencadenar y cancelar la mensajería, está disponible inmediatamente para la personalización de la mensajería, y mucho más. Los puntos de datos te ayudan a definir la información más impactante para tu negocio. Al considerar cuidadosamente qué información rastrear, te aseguras de que estás apuntando a los datos de mayor impacto para la experiencia de tus usuarios.

Los puntos de datos se basan en la información registrada en los perfiles de usuario. Puedes encontrar un desglose más detallado de esta definición en tu contrato con Braze. Nuestro equipo de éxito del cliente puede ayudarte a recomendar las mejores prácticas de datos que se ajusten a tus necesidades. 

## Definición

"Puntos de datos" hará referencia a una unidad facturable de uso de los servicios de Braze, medida por un inicio de sesión, un fin de sesión, un evento personalizado o una compra registrada, así como cualquier atributo establecido en un perfil de usuario final. Para mayor claridad, cada uno de los datos mencionados (como inicio de sesión, fin de sesión, evento personalizado o compra registrada, así como cualquier atributo) establecido en el perfil de un usuario final en un momento dado contará como un único punto de datos.

Los datos y eventos recopilados de forma predeterminada por los servicios de Braze, incluidos, por ejemplo, los tokens de notificaciones push, la información del dispositivo y todos los eventos de seguimiento de interacción en campañas, como aperturas de correos electrónicos y clics en notificaciones push, *no* se contabilizan como puntos de datos.

Consulta la sección [Recuento de consumo](#consumption-count) de este artículo para saber qué datos cuentan para tu asignación de puntos de datos.

## Visualización del uso de puntos de datos

Para ver tu uso de puntos de datos, ve a **Configuración** > **Facturación** y selecciona la pestaña **Uso total de puntos de datos**.

Para más información sobre los componentes del dashboard de puntos de datos, consulta [Facturación]({{site.baseurl}}/user_guide/administrative/app_settings/subscription_and_usage/).

{% alert tip %}
**¡No desperdicies puntos de datos. Actualiza solo los datos que cambian!**<br><br>
Para minimizar el uso de puntos de datos, recomendamos configurar un programa para evitar el envío de los mismos datos invariables y solo pasar datos nuevos y relevantes a Braze. Braze trabajará contigo para establecer esta práctica óptima durante la incorporación. 
{% endalert %}

## Recuento de consumo

En resumen, los puntos de datos se acumulan cuando se actualizan los datos del perfil de un usuario o cuando este realiza acciones específicas. Esencialmente, los puntos de datos son recuentos de cada uno de los `session starts`, `session ends`, `events` y `purchases` de tus usuarios.

Puedes encontrar un desglose de cómo Braze acumula puntos de datos en las siguientes secciones. Si alguna vez tienes preguntas sobre los matices de los puntos de datos de Braze, tu director de cuentas de Braze puede respondértelas.

Las siguientes acciones no registran puntos de datos:
- Eliminar usuarios de Braze
- Uso de contenido conectado en la mensajería
- Cambios de estado de suscripción a nivel global y en torno a los grupos de suscripción
- Renombrar los ID externos de tus usuarios mediante [llamadas a la API]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/)
- Bloqueo de eventos, atributos o propiedades del evento

### Circunstancias especiales

#### Matrices

Una matriz es una colección ordenada de elementos almacenados dentro de un atributo personalizado. Actualizar una matriz cuesta un punto de datos por llamada a la API, incluso si la matriz no cambia realmente. Por ejemplo, enviar una operación `remove` para un valor que no existe en la matriz igualmente consume un punto de datos. De forma similar, establecer un atributo personalizado en `null` para eliminarlo del perfil consume un punto de datos. Si añades valores a una matriz de forma incremental, contará como un punto de datos por valor. 

{% alert tip %}
En el caso de las matrices simples, si configuras toda la matriz a la vez, contará como un único punto de datos. Como tales, las matrices son una gran herramienta para mantener actualizados los perfiles de los usuarios con información relevante y reducir costes. <br><br> Las matrices de objetos consumen un punto de datos por cada clave que se actualiza. Reduce el consumo innecesario de puntos de datos pasando solo las actualizaciones a Braze.
{% endalert %}

#### Atributos personalizados anidados

Los atributos personalizados anidados se refieren a un objeto que define un conjunto de atributos como propiedad de otro atributo. Cada clave del objeto contará como un punto de datos.

{% alert note %}
Actualizar un objeto de atributo personalizado a `null` también consume un punto de datos.
{% endalert %}

#### CSV

Los atributos personalizados cargados a través de la importación CSV cuentan para tus puntos de datos. Sin embargo, las importaciones CSV con fines de segmentación (importaciones realizadas con `external_id`, `braze_id` o `user_alias_name` como único campo) no registrarán puntos de datos.

Además, como los cambios de estado de suscripción no registran puntos de datos, la actualización de los campos `email_subscribe`, `push_subscribe`, `subscription_group_id` o `subscription_state` en tu archivo CSV no generará cargos.

## Puntos de datos

{% alert note %}
Las tablas siguientes tienen carácter ilustrativo. Para conocer las convenciones de nomenclatura exactas, las mayúsculas y los valores aceptados para determinados campos, consulta la documentación correspondiente a tu método de ingestión.
{% endalert %}

{% tabs %}
{% tab Non-billable %}

#### Puntos de datos no facturables (predeterminado)

<div class="small_table"></div>

| Tipo de datos | Punto de datos |
| --------- | ---------- |
| Datos del perfil | País |
| Datos del perfil | Idioma |
| Datos del perfil | ID de usuario |
| Datos del perfil | Alias de usuario |
| Dispositivos recientes | Número de dispositivos |
| Dispositivos recientes | Reloj más reciente |
| Dispositivos recientes | Versión de la aplicación |
| Dispositivos recientes | Dispositivo |
| Dispositivos recientes | Sistema operativo del dispositivo |
| Configuración de contacto | Correo electrónico suscrito |
| Configuración de contacto | Push suscrito |
| Configuración de contacto | Aplicaciones registradas para push |
| Configuración de contacto | Grupo de suscripción |
| Campañas recibidas | Dirección de correo electrónico |
| Atribución de instalación | Fuente de instalación |
| Atribución de instalación | Campaña |
| Atribución de instalación | Grupo de anuncios |
| Atribución de instalación | Anuncio |
| Varios | Número de contenedor aleatorio |
| Mensajes recibidos en Canvas | Mensajes recibidos en Canvas |
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
Añadir, eliminar o actualizar los siguientes tipos de datos generará un punto de datos facturable.
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
| Datos del perfil | Apellido | |
| Datos del perfil | Dirección de correo electrónico | |
| Datos del perfil | Género | |
| Datos del perfil | Grupo de edad | |
| Datos del perfil | País | Cuando se recoge manualmente. No cuenta para el consumo cuando se recoge automáticamente. |
| Datos del perfil | Ciudad | |
| Datos del perfil | Idioma | Cuando se recoge manualmente. No cuenta para el consumo cuando se recoge automáticamente. |
| Datos del perfil | Configuración regional más reciente del dispositivo | |
| Datos del perfil | Zona horaria | |
| Datos del perfil | Fecha de nacimiento | |
| Datos del perfil | Bio | |
| Datos del perfil | Número de teléfono | |
| Datos de uso de la aplicación | Inicio de sesión | |
| Datos de uso de la aplicación | Fin de sesión | |
| Atributos personalizados | Todos los atributos personalizados | |
| Eventos personalizados | Todos los eventos personalizados | |
| Propiedades de eventos personalizados | Todas las propiedades de eventos personalizados | Las propiedades de eventos personalizados habilitadas para la segmentación con los filtros `X Custom Event Property in Y Days` o `X Purchase Property in Y Days` se contabilizan como puntos de datos independientes, además del punto de datos contabilizado por el propio evento personalizado.
| Compras | Todas las compras | |
| Propiedades de la compra | Todas las propiedades de la compra | |
| Asignación de cohortes de Amplitude | Todas las asignaciones | |
| Asignación de cohortes de Mixpanel | Todas las asignaciones | |
| Asignación de cohortes de Hightouch | Todas las asignaciones | |
| Asignación de cohortes de Appsflyer | Todas las asignaciones | |
| Ubicación más reciente | Todas las ubicaciones más recientes | Entrar o salir de geovallas no registra puntos de datos porque los datos de geovalla no se almacenan en el perfil de usuario. Las geovallas son monitorizadas por los servicios de ubicación de Apple y Google; Braze solo recibe una notificación cuando un usuario activa una geovalla. |
| Twitter | Nombre de usuario | |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}