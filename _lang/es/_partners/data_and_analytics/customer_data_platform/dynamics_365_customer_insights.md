---
nav_title: Dynamics 365 Customer Insights
article_title: Dynamics 365 Customer Insights
description: "Este artículo de referencia describe la asociación entre Braze y Dynamics 365 Customer Insights, una plataforma líder de datos de clientes empresariales, que le permite exportar segmentos de clientes a Braze para utilizarlos en campañas o Canvases."
alias: /partners/dynamics_365_customer_insights/
page_type: partner
search_tag: Partner
---

# Dynamics 365 Customer Insights
 
> [Dynamics 365 Customer Insights](https://dynamics.microsoft.com/en-gb/ai/customer-insights/) es una plataforma líder de datos de clientes empresariales que ofrece experiencias de cliente personalizadas con una visión de 360 grados de sus clientes.

_Esta integración la mantiene Dynamics 365 Customer Insights._

## Sobre la integración

La integración de Braze y Dynamics 365 Customer Insights le permite exportar segmentos de clientes a Braze para utilizarlos en campañas o Canvases.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Dynamics 365 Customer Insights | Se necesita una cuenta de [Dynamics 365 Customer Insights](https://dynamics.microsoft.com/en-gb/ai/customer-insights/) para aprovechar esta asociación. Necesitará acceso como administrador para ver y editar conexiones dentro de su cuenta de Dynamics 365 Customer Insights para acceder a los plugins necesarios. |
| Clave de API REST de Braze | Se necesita una clave de API REST de Braze con los permisos `users.track` y `users.export.segment`. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Identificadores de perfiles coincidentes | Los perfiles de cliente unificados en los segmentos exportados contienen un campo que representa una dirección de correo electrónico y un Braze `external_id`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Establecer conexión Braze

En Customer Insights, ve a **Admin > Conexiones**. A continuación, seleccione **Añadir conexiones** y elija **Braze** para configurar la conexión. 

1. Dé a su conexión un nombre reconocible en el campo **Nombre para mostrar**. 
2. Elige quién puede utilizar esta conexión. Si dejas este campo en blanco, el valor predeterminado será Administradores. Para más información, consulta [Permitir a los colaboradores utilizar una conexión para las exportaciones](https://docs.microsoft.com/en-us/dynamics365/customer-insights/connections#allow-contributors-to-use-a-connection-for-exports).
3. Proporciona tu clave de API Braze y el punto final REST en el formato `rest.iad-03.braze.com`.
4. Seleccione **Acepto** para confirmar la conformidad de los datos y la privacidad.
5. Seleccione **Conectar** para inicializar la conexión con Braze.
6. Seleccione **Añadirse como usuario de exportación** e introduzca sus credenciales de Customer Insights.
7. Seleccione **Guardar** para completar la conexión.

### Paso 2: Crear un segmento Braze

1. En Braze, ve a **Audiencia** > Segmentos.
2. Crea un segmento de los usuarios que quieres que Microsoft actualice a través de Dynamics 365 Customer Insights.
3. Captura el identificador API del segmento

### Paso 3: Configurar una exportación

Puede configurar esta exportación si tiene acceso a una conexión de este tipo. Para más información, consulta el [resumen de Exportaciones](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#set-up-a-new-export).

1. En Customer Insights, ve a **Datos > Exportaciones**. Para crear una nueva exportación, seleccione **Añadir destino**.
2. En el campo **Conexión para la exportación**, selecciona una conexión para la sección Braze. Si no ves el nombre de esta sección, no hay conexiones de este tipo disponibles para ti.
3. Proporciona el identificador API del segmento en Braze.
4. En la sección **Coincidencia de datos**, en el campo **Correo electrónico**, seleccione el campo que representa la dirección de correo electrónico de un cliente. A continuación, en el campo **Braze Customer ID**, selecciona el campo que representa el Braze ID del cliente. También puedes seleccionar un campo adicional opcional para cotejar los datos.
  a. Si mapeas el `external_id` en Braze con el campo ID de cliente Braze en Customer Insights, los registros existentes se actualizarán en Braze al exportar.
  b. Si mapeas un campo ID diferente que no representa el `external_id` de un registro en Braze, o un campo vacío, se crearán nuevos registros en Braze al exportar.
5. Por último, selecciona los segmentos que quieras exportar y selecciona **Guardar**. 

Tenga en cuenta que guardar una exportación no la ejecuta inmediatamente. Esta exportación se ejecutará con cada [actualización programada](https://docs.microsoft.com/en-us/dynamics365/customer-insights/system#schedule-tab). También puedes [exportar datos a petición](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#run-exports-on-demand). 


### Uso de esta integración

Una vez que tus segmentos se hayan exportado correctamente a Braze, podrás encontrarlos como atributos personalizados en los perfiles de usuario. El atributo personalizado se denominará con el identificador de la API del segmento Braze que se introdujo al configurar la conexión de exportación. Por ejemplo, `"Segment_API_Identifier": "0000-0000-0000"`

Para crear un segmento de estos usuarios en Braze, ve a **Segmentos**, crea un nuevo segmento y selecciona **Atributos personalizados** como filtro. Desde aquí, puedes elegir el atributo personalizado sincronizado con Dynamics 365. Una vez creado el segmento, puede seleccionarlo como filtro de audiencia al crear una campaña o Canvas.

{% alert note %}
Para más información sobre esta integración, visita el [artículo de Microsoft sobre la integración](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-braze) con Braze.
{% endalert %}


