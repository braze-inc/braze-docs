---
nav_title: Census
article_title: Census
description: "Este artículo de referencia describe la asociación entre Braze y Census, una plataforma de integración de datos que le permite crear dinámicamente segmentos de usuarios específicos con datos de su almacén en la nube."
alias: /partners/census/
page_type: partner
search_tag: Partner

---

# Census

> [Census](https://www.getcensus.com/) es una plataforma de activación de datos que conecta almacenes de datos en la nube como Snowflake y BigQuery con Braze. Los equipos de marketing pueden liberar la potencia de sus datos de origen para crear segmentos de audiencia dinámicos, sincronizar los atributos de los clientes para personalizar las campañas y mantener actualizados todos sus datos en Braze. Ahora es más fácil que nunca actuar con datos fiables y procesables, sin necesidad de cargar archivos CSV ni hacer favores de ingeniería.

La integración de Braze y Census permite importar dinámicamente audiencias o datos de productos a Braze para enviar campañas personalizadas. Por ejemplo, puede crear una cohorte en Braze para "Suscriptores de boletines con CLV > 1000" para dirigirse a clientes de alto valor o "Usuarios activos en los últimos 30 días" para dirigirse a usuarios específicos para probar una próxima función beta.

## Requisitos previos

| Requisito | Descripción |
| --- | --- |
| Cuenta Census | Es necesario tener una [cuenta en el Census](https://www.getcensus.com/) para beneficiarse de esta asociación. |
| Clave REST API de Braze | Una clave de API REST de Braze con todos los permisos de datos de usuario (excepto `users.delete`) y permisos de `segments.list`. El conjunto de permisos puede cambiar a medida que Census añada compatibilidad con más objetos Braze, por lo que es posible que desee conceder más permisos ahora o planificar la actualización de estos permisos en el futuro. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze  | La URL de su punto final REST. Tu punto final dependerá de la [URL Braze de tu instancia]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). |
| Almacén de datos y modelo de datos | Antes de comenzar la integración, debe tener un almacén de datos configurado en Census y definir un modelo del subconjunto de datos que desea sincronizar con Braze. Visite [la documentación del Censo](https://docs.getcensus.com/destinations/braze) para obtener una lista de las fuentes de datos disponibles y orientación sobre la creación de modelos. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Integración

### Paso 1: Crear conexión de servicio Braze

Para integrar Census en la plataforma Census, vaya a la pestaña **Conexiones** y seleccione **Nuevo destino** para crear una nueva conexión de servicio Braze.

En el mensaje que aparece, asigne un nombre a esta conexión e indique la URL del punto final de Braze y la clave de la API REST de Braze (y, opcionalmente, la clave de importación de datos para sincronizar cohortes).

![]({% image_buster /assets/img/census/add_service.png %}){: style="max-width:60%;"}

### Paso 2: Crear una sincronización del censo

Para sincronizar clientes con Braze, debe crear una sincronización. Aquí definirá dónde sincronizar los datos y cómo desea que se asignen los campos entre las dos plataformas.

1. Vaya a la pestaña **Sincronizaciones** y seleccione **Nueva sincronización**.<br><br> 
2. En el compositor, seleccione el modelo de datos fuente de su almacén de datos.<br><br>
3. Configure dónde se sincronizará el modelo. Seleccione **Braze** como destino y el [tipo de objeto compatible](#supported-objects) que desea sincronizar.<br>![En la pregunta "Selecciona un destino", se selecciona "Braze" como conexión y se enumeran varios objetos.]({% image_buster /assets/img/census/census_2.png %}){: style="max-width:80%;"}<br><br>
4. Seleccione qué regla de sincronización desea aplicar**(Actualizar o Crear** es la opción más común, pero puede elegir reglas más avanzadas para gestionar la eliminación de datos, por ejemplo).<br><br>
5. A continuación, para la coincidencia de registros, elija una clave de sincronización para [asignar](#supported-objects) su objeto Braze a un campo del modelo.<br>![En la pregunta "Selecciona una clave de sincronización", "ID usuario externo" de Braze coincide con "user_id" en la fuente.]({% image_buster /assets/img/census/census_1.png %}){: style="max-width:80%;"}<br><br>
6. Por último, asigne los campos de datos del censo a los campos Braze equivalentes.<br>![Censo mapeado]({% image_buster /assets/img/census/census_3.png %}){: style="max-width:80%;"}<br><br>
7. Confirma los detalles y crea la sincronización. 

Una vez ejecutada la sincronización, encontrarás los datos del usuario en Braze. Ahora puede crear y añadir un segmento Braze a futuras campañas Braze y Canvases para dirigirse a estos usuarios. 

{% alert note %}
Al utilizar la integración de Census y Braze, Census sólo enviará los deltas (datos cambiantes) en cada sincronización a Braze.
{% endalert %}

## Objetos compatibles

El censo admite actualmente la sincronización de los siguientes objetos Braze:

| Nombre del objeto | Comportamientos de sincronización |
| --- | --- |
| Usuario | Actualizar, Crear, Reflejar, Borrar |
| Cohorte | Actualizar, Crear, Reflejar | 
| Catálogo | Actualizar, Crear, Reflejar |
| Pertenencia a un grupo de suscripción | Espejo |
| Evento | Añada |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Además, Census admite el envío de [datos estructurados](https://docs.getcensus.com/destinations/braze#supported-objects) a Braze: 
- Tokens de notificaciones push de usuario: Para enviar tokens de notificaciones push, tus datos deben estructurarse como una matriz de objetos con 2-3 valores: `app_id`, `token`, y uno opcional `device_id`.
- Atributos personalizados anidados: Se admiten tanto objetos como matrices. En abril de 2022, esta característica todavía está en acceso anticipado. Es posible que tenga que ponerse en contacto con su gestor de cuenta Braze para obtener acceso.

