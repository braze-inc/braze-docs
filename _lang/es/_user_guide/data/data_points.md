---
nav_title: Puntos de datos
article_title: Resumen de puntos de datos
page_order: 0
page_type: reference
description: "Este artículo de referencia describe qué puntos de datos hay en Braze y cómo puede ser consciente de su uso."
search_rank: 6
---

# Puntos de datos

> En Braze, los datos significan acción: cada dato que llega a Braze actualiza la pertenencia a un segmento, puede activar y cancelar la mensajería, está disponible inmediatamente para la personalización de la mensajería, y mucho más. Los puntos de datos le ayudan a definir la información más impactante para su negocio. Al considerar cuidadosamente qué información rastrear, se asegura de que está apuntando a los datos de mayor impacto para la experiencia de sus usuarios.

Los puntos de datos definen una estructura de facturación y precios basada en la información registrada en los perfiles de usuario. Nuestro equipo de Éxito del cliente puede ayudarte a recomendar las mejores prácticas de datos que se ajusten a tus necesidades. Puede encontrar un desglose más detallado de esta definición en su contrato Braze. 

## Definición

"Puntos de datos" hará referencia a una unidad facturable de uso de los Servicios Braze, medida por un inicio de sesión, un fin de sesión, un evento personalizado o una compra registrada, así como cualquier atributo establecido en un perfil de usuario final. Para mayor claridad, cada uno de los datos mencionados (como inicio de sesión, fin de sesión, evento personalizado o compra registrada, así como cualquier atributo) establecido en el perfil de un usuario final en un momento dado contará como un único punto de datos.

Los datos y eventos recopilados de forma predeterminada por los Servicios Braze, incluidos, por ejemplo, los tokens push, la información del dispositivo y todos los eventos de seguimiento de participación en campañas, como aperturas de correos electrónicos y clics en notificaciones push, *no* se contabilizan como puntos de datos.

Consulte la sección [Recuento de consumos](#consumption-count) de este artículo para saber qué datos cuentan para su asignación de puntos de datos.

## Visualización del uso de puntos de datos

Para ver tu uso de puntos de datos, ve a **Configuración** > **Facturación** y selecciona la pestaña **Uso total de puntos de datos**.

Para más información sobre los componentes del panel de puntos de datos, consulta [Facturación]({{site.baseurl}}/user_guide/administrative/app_settings/subscription_and_usage/).

{% alert tip %}
**No desperdicies puntos de datos. ¡Actualiza solo los datos cambiantes!**<br><br>
Para minimizar el consumo de puntos de datos, recomendamos configurar un programa para evitar el envío de los mismos datos invariables y sólo pasar datos nuevos y relevantes a Braze. Braze trabajará con usted para establecer esta práctica óptima durante la incorporación.
{% endalert %}

## Recuento de consumos

En resumen, los puntos de datos se acumulan cuando se actualizan los datos del perfil de un usuario o cuando éste realiza acciones específicas. Esencialmente, los puntos de datos son recuentos de cada una de las direcciones `session starts`, `session ends`, `events` y `purchases` de tu usuario.

Puede encontrar un desglose de cómo Braze acumula puntos de datos en las siguientes secciones. Si alguna vez tienes alguna pregunta sobre los matices de los puntos de datos Braze, tu director de cuentas Braze puede responderte.

Las siguientes acciones no consumen puntos de datos:
- Eliminar usuarios de Braze
- Uso de contenidos conectados en la mensajería
- El estado de las suscripciones cambia globalmente y en torno a los grupos de suscriptores
- Renombrar los ID externos de sus usuarios mediante [llamadas a la API]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/)
- Bloqueo de eventos, atributos o propiedades de eventos

### Circunstancias especiales

#### Matrices

Un array es una colección ordenada de elementos almacenados dentro de un atributo personalizado. En términos de consumo, actualizar una matriz cuesta un punto de datos por llamada a la API. Si añade valores a una matriz de forma incremental, contará como un punto de datos por valor. 

{% alert tip %}
Si fija toda la matriz a la vez, contará como un único punto de datos. Como tales, las matrices son una gran herramienta para mantener actualizados los perfiles de los usuarios con información relevante y reducir costes.
{% endalert %}

#### Atributos personalizados anidados

Los atributos personalizados anidados se refieren a un objeto que define un conjunto de atributos como propiedad de otro atributo. Cada clave del objeto contará como un punto de datos.

{% alert note %}
La actualización de un objeto de atributo personalizado en `null` también consume un punto de datos.
{% endalert %}

#### CSV

Los atributos personalizados cargados a través de la importación CSV cuentan para sus puntos de datos. Sin embargo, las importaciones CSV con fines de segmentación (importaciones realizadas con `external_id`, `braze_id`, o `user_alias_name` como único campo) no consumirán puntos de datos.

Además, como los cambios de estado de suscripción no consumen puntos de datos, la actualización de los campos `email_subscribe`, `push_subscribe`, `subscription_group_id`, o `subscription_state` en su archivo CSV no incurrirá en cargos.

## Puntos de datos

{% alert note %}
Las tablas siguientes tienen carácter ilustrativo. Para conocer las convenciones de nomenclatura exactas, las mayúsculas y los valores aceptados para determinados campos, consulta la documentación correspondiente a tu método de ingestión.
{% endalert %}

{% tabs %}
{% tab No facturable %}

#### Puntos de datos no facturables (por defecto)

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
| Atribución de instalación | Instalar fuente |
| Atribución de instalación | Campaña |
| Atribución de instalación | Grupo de anuncios |
| Atribución de instalación | Anuncio |
| Varios | Número de contenedor aleatorio |
| Mensajes recibidos en Canvas | Mensajes recibidos en Canvas |
| Interacción con los mensajes | Todos los eventos de interacción (como aperturas, clics, impresiones y rechazos) |
| X | Seguidores |
| X | Siguiendo |
| X | Número de tweets |
| Facebook | Me gusta |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Facturable %}

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
| Datos del perfil | Apellido | |
| Datos del perfil | Dirección de correo electrónico | |
| Datos del perfil | Género | |
| Datos del perfil | Grupo de edad | |
| Datos del perfil | País | Cuando se recoge manualmente. No cuenta para el consumo cuando se recoge automáticamente. |
| Datos del perfil | Localidad | |
| Datos del perfil | Idioma | Cuando se recoge manualmente. No cuenta para el consumo cuando se recoge automáticamente. |
| Datos del perfil | Localización más reciente del dispositivo | |
| Datos del perfil | Zona horaria | |
| Datos del perfil | Fecha de nacimiento | |
| Datos del perfil | Bio | |
| Datos del perfil | Número de teléfono | |
| Datos de uso de la aplicación | Inicio de la sesión | |
| Datos de uso de la aplicación | Fin de la sesión | |
| Atributos personalizados | Todos los atributos personalizados | |
| Eventos personalizados | Todos los eventos personalizados | |
| Propiedades personalizadas de los eventos | Todas las propiedades de eventos personalizados | Las propiedades de eventos personalizados habilitadas para la segmentación con los filtros `X Custom Event Property in Y Days` o `X Purchase Property in Y Days` se contabilizan como puntos de datos independientes, además del punto de datos contabilizado por el propio evento personalizado.
| Compras | Todas las compras | |
| Propiedades de la compra | Todas las propiedades de la compra | |
| Asignación de cohortes de amplitud | Todas las asignaciones | |
| Asignación de cohortes Mixpanel | Todas las asignaciones | |
| Asignación de cohortes Hightouch | Todas las asignaciones | |
| Asignación de cohortes Appsflyer | Todas las asignaciones | |
| Ubicación más reciente | Todas las ubicaciones más recientes | Entrar o salir de geovallas no consume puntos de datos porque los datos de geovalla no se almacenan contra el perfil de usuario. Las geocercas son controladas por los servicios de localización de Apple y Google; Braze sólo recibe una notificación cuando un usuario activa una geocerca. |
| X | Nombre de usuario | |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

