---
nav_title: Adobe para Currents
article_title: Adobe para Currents
alias: /partners/adobe_for_currents/
description: "Este artículo de referencia describe la asociación entre Braze Currents y Adobe, una plataforma de datos de los clientes que permite a las marcas conectar y mapear sus datos de Adobe (atributos personalizados y segmentos) con Braze en tiempo real."
page_type: partner
tool: Currents
search_tag: Partner
---

# Adobe para Currents

> [Adobe](https://www.adobe.com/) es una plataforma de datos de los clientes que permite a las marcas conectar y mapear sus datos de Adobe (atributos personalizados y segmentos) con Braze en tiempo real.

La integración de Braze y Adobe te permite controlar fácilmente el flujo de información entre ambos sistemas. Con [Currents]({{site.baseurl}}/user_guide/data/braze_currents/), también puedes conectar los datos con Adobe para que sean procesables en toda la stack de crecimiento. 

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Currents | Para volver a exportar datos a Adobe, debes tener configurado [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) para tu cuenta. |
| Cuenta de Adobe Experience Platform | Se necesita una [cuenta de Adobe Experience Platform](https://experience.adobe.com/#/platform/home) para aprovechar esta asociación. |
| Permiso para crear un conector | Necesitas permisos para crear una conexión de fuente de streaming para utilizar esta integración. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Crear un esquema XDM en Adobe

1. En Adobe Experience Platform, ve a **Esquemas** > selecciona **Crear esquema** > selecciona **Evento de experiencia** > selecciona **Siguiente**.<br><br>![Página de Adobe Schemas para el esquema llamado "Braze Currents Walk-Through".]({% image_buster /assets/img/adobe/currents_sources.png %})<br><br>
2. Proporciona un nombre y una descripción para tu esquema. 
3. En el panel **Composición**, configura los atributos de tu esquema:
- En **Grupos de campos**, selecciona **Añadir** y, a continuación, añade el grupo de campos **Evento de usuario de Braze Currents**.
- Seleccione **Guardar**.

Para más información sobre los esquemas, consulta la documentación de Adobe sobre la [creación de esquemas](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/tutorials/create-schema-ui).

### Paso 2: Conecta Braze a Adobe Experience Platform

1. En Adobe Experience Platform, ve a **Fuentes** > **Catálogo** > **Automatización del marketing**.
2. Selecciona **Añadir datos** para Braze Currents.
3. Sube el [archivo de muestra Braze Currents](https://github.com/Appboy/currents-examples/blob/master/sample-data/Adobe/adobe_examples.json).<br><br>![Adobe "Añadir página de datos".]({% image_buster /assets/img/adobe/currents_add_data.png %})<br><br>
4. Una vez cargado el archivo, proporciona los detalles de tu flujo de datos, incluida la información sobre tu conjunto de datos y el esquema al que lo estás mapeando. 
    - Si es la primera vez que conectas una fuente Braze Currents, crea un nuevo conjunto de datos y asegúrate de utilizar el esquema que creaste en [el Paso 1](#step-1-create-an-xdm-schema-in-adobe). 
    - Si no es tu primera vez, utiliza cualquier conjunto de datos existente que haga referencia al esquema Braze.
5. Configura el mapeado de tus datos y resuelve los problemas.
    - Cambia el mapeado de `id` de `to _braze.appID` a `_id` en el nivel raíz del esquema.
    - Asegúrate de que `properties.is_amp` está mapeado en `_braze.messaging.email.isAMP`.
    - Elimina el mapeado `time` y `timestamp`, luego selecciona el icono añadir > **Añadir campo calculado** e introduce **tiempo * 1000**. Seleccione **Guardar**.
    - Selecciona **Mapear campo de destino** junto al nuevo campo de origen y mapearlo a **marca de tiempo** en el nivel raíz del esquema. <br><br>![Página de Adobe "Añadir datos" con mapeados.]({% image_buster /assets/img/adobe/currents_mapping.png %})<br><br>
6. Selecciona **Validar** para confirmar que has resuelto los problemas.

{% alert important %}
Las marcas de tiempo de Braze se expresan en segundos. Para reflejar con precisión las marcas de tiempo en Adobe Experience Platform, tus campos calculados deben estar en milisegundos. Para convertir segundos en milisegundos, utiliza el cálculo **tiempo * 1000**.
{% endalert %}

{: start="7"}
7\. Selecciona **Siguiente**, revisa los detalles de tu flujo de datos y, a continuación, selecciona **Finalizar**.<br><br>![Página "Añadir datos" de Adobe sin errores de mapeado.]({% image_buster /assets/img/adobe/currents_no_errors.png %})

### Paso 3: Reúne credenciales

Recoge las siguientes credenciales para introducirlas en Braze, lo que permitirá a Braze enviar datos a Adobe Experience Platform.

| Campo         |Descripción                          |
|---------------|-------------------------------------|
| ID de cliente     | El ID de cliente asociado a tu fuente de Adobe Experience Platform. |
| Secreto de cliente | El secreto de cliente asociado a tu fuente de Adobe Experience Platform. |
| ID de inquilino     | El ID de inquilino asociado a tu fuente de Adobe Experience Platform. |
| Nombre de la zona protegida  | El sandbox asociado a tu fuente de Adobe Experience Platform.   |
| ID de Dataflow   | El ID de flujo de datos asociado a tu fuente de Adobe Experience Platform.   |
| Punto final de transmisión  | El punto final de streaming asociado a tu fuente de Adobe Experience Platform. Braze lo convierte automáticamente en el punto final de transmisión por lotes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Paso 4: Configura Currents para transmitir datos a tu origen de datos

1. En Braze, ve a **Integraciones de socios** > **Exportación de datos** y, a continuación, selecciona **Crear nueva corriente**. 
2. Proporciona lo siguiente:
    - Un nombre para el conector
    - Información de contacto para notificaciones sobre el conector
    - Las credenciales del [Paso 3](#step-3-gather-credentials)
3. Selecciona los eventos que quieres recibir.
4. Configura opcionalmente las exclusiones de campos o transformaciones que desees.
5. Selecciona **Lanzar Corriente**.

