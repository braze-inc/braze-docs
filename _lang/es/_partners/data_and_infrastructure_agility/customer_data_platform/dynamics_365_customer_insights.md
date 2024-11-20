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

La integración de Braze y Dynamics 365 Customer Insights le permite exportar segmentos de clientes a Braze para utilizarlos en campañas o Canvases.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Dynamics 365 Customer Insights | Se necesita una cuenta de [Dynamics 365 Customer Insights](https://dynamics.microsoft.com/en-gb/ai/customer-insights/) para aprovechar esta asociación. Necesitará acceso como administrador para ver y editar conexiones dentro de su cuenta de Dynamics 365 Customer Insights para acceder a los plugins necesarios. |
| Clave REST API de Braze | Se requiere una clave Braze REST API con todos los permisos concedidos. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Establecer conexión Braze

En Customer Insights, ve a **Admin > Conexiones**. A continuación, seleccione **Añadir conexiones** y elija **Braze** para configurar la conexión. 

1. Dé a su conexión un nombre reconocible en el campo **Nombre para mostrar**. 
2. Elige quién puede utilizar esta conexión. Si dejas este campo en blanco, el valor predeterminado será Administradores. Para más información, consulta [Permitir a los colaboradores utilizar una conexión para las exportaciones](https://docs.microsoft.com/en-us/dynamics365/customer-insights/connections#allow-contributors-to-use-a-connection-for-exports).
3. Proporcione su clave Braze API para continuar iniciando sesión.
4. Seleccione **Acepto** para confirmar la conformidad de los datos y la privacidad.
5. Seleccione **Conectar** para inicializar la conexión con Braze.
6. Seleccione **Añadirse como usuario de exportación** e introduzca sus credenciales de Customer Insights.
7. Seleccione **Guardar** para completar la conexión. 

### Paso 2: Configurar una exportación

Puede configurar esta exportación si tiene acceso a una conexión de este tipo. Para más información, consulta el [resumen de Exportaciones](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#set-up-a-new-export).

1. En Customer Insights, ve a **Datos > Exportaciones**. Para crear una nueva exportación, seleccione **Añadir destino**.
2. En el campo **Conexión para la exportación**, elija una conexión para la sección Braze. Si no ves el nombre de esta sección, no hay conexiones de este tipo disponibles para ti. 
3. Introduce tu punto final REST en el campo de nombre de host con el siguiente formato: `rest.iad-03.braze.com`.
4. En la sección **Coincidencia de datos**, en el campo **Correo electrónico**, seleccione el campo que representa la dirección de correo electrónico de un cliente. A continuación, en el campo **ID de cliente**, seleccione el campo que representa el ID Braze del cliente. También puede elegir un campo adicional y opcional para los datos coincidentes. 
5. Por último, seleccione **Guardar**. 

Tenga en cuenta que guardar una exportación no la ejecuta inmediatamente. Esta exportación se ejecutará con cada [actualización programada](https://docs.microsoft.com/en-us/dynamics365/customer-insights/system#schedule-tab). También puedes [exportar datos a petición](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#run-exports-on-demand). 

### Mediante esta integración

Una vez que sus segmentos se hayan exportado correctamente a Braze, podrá encontrarlos como atributos personalizados en los perfiles de usuario con el mismo nombre que el segmento encontrado en Dynamics 365 Customer Insights. 

Para crear un segmento de estos usuarios, en Braze, vaya a **Segmentos**, cree un nuevo segmento y seleccione **Atributos personalizados** como filtro. Desde aquí, puedes elegir el atributo personalizado de Dynamics 365. Una vez creado el segmento, puede seleccionarlo como filtro de audiencia al crear una campaña o Canvas.

{% alert note %}
Para más información sobre esta integración, visita el [artículo de Microsoft sobre la integración](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-braze) con Braze.
{% endalert %}

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints