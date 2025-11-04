---
nav_title: Mixpanel
article_title: Importación de cohortes de Mixpanel
description: "Este artículo de referencia describe la funcionalidad de importación de cohortes de Mixpanel, una plataforma de análisis empresarial, que permite importar cohortes de Mixpanel a Braze para crear segmentos de Braze que se pueden utilizar para dirigirse a usuarios en futuras campañas o lienzos de Braze."
page_type: partner
search_tag: Partner
---

# Importación de cohortes de Mixpanel

> Este artículo describe cómo importar cohortes de usuarios de [Mixpanel](https://mixpanel.com/) a Braze. Para obtener más información sobre la integración de Mixpanel y sus otras funcionalidades, consulte el [artículo principal sobre Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/).

## Integración de la importación de datos

Cualquier integración que establezca contará para el volumen de puntos de datos de su cuenta.

{% alert important %}
En cumplimiento de las políticas de retención de datos de Mixpanel, los eventos enviados antes del 1 de enero de 2010 se eliminarán durante la importación.
{% endalert %}

### Paso 1: Obtener la clave de importación de datos Braze

En Braze, vaya a **Integraciones de socios** > **Socios tecnológicos** y seleccione **Mixpanel**. Aquí encontrarás el punto final REST y generarás tu clave de importación de datos Braze. 

Una vez generada, puede crear una nueva clave o invalidar una existente. La clave de importación de datos y el endpoint REST se utilizan en el siguiente paso al configurar un postback en el dashboard de Mixpanel.<br><br>![]({% image_buster /assets/img_archive/currents-mixpanel-edit.png %})

### Paso 2: Configurar la integración Braze en Mixpanel

En Mixpanel, ve a **Gestión de datos > Integraciones.** A continuación, selecciona la pestaña de integración Braze y haz clic en **Conectar**. En el mensaje que aparece, introduzca la clave de importación de datos Braze y el punto final REST, y haga clic en **Continuar**.

![]({% image_buster /assets/img_archive/mixpanel2.png %}){: style="max-width:50%;"}

### Paso 3: Exportar una cohorte de Mixpanel a Braze

En Mixpanel, vaya a **Gestión de datos > Cohortes**. Seleccione la cohorte que desea enviar a Braze y, a continuación, seleccione **Exportar a Braze**. Por último, selecciona una sincronización única o una sincronización dinámica. Seleccionando sincronización dinámica sincronizará su cohorte Braze cada 15 minutos para que coincida con los usuarios en Mixpanel. 

![]({% image_buster /assets/img_archive/mixpanel3.png %}){: style="max-width:50%;"}

{% alert important %}
Sólo se añadirán o eliminarán de una cohorte los usuarios que ya existan en Braze. La importación de cohortes no creará nuevos usuarios en Braze.
{% endalert %}

### Paso 4: Segmentar usuarios en Braze

En Braze, para crear un segmento de estos usuarios, ve a **Audiencia** > **Segmentos**, asigna un nombre a tu segmento y selecciona **Mixpanel_Cohorts** como filtro. A continuación, utilice la opción "incluye" y elija la cohorte que creó en Mixpanel. 

![En el creador de segmentos Braze, el filtro de atributos de usuario "cohortes de Mixpanel" se establece en "incluye" y "cohorte de Braze".]({% image_buster /assets/img_archive/mixpanel1.png %})

Después de guardarlo, puede hacer referencia a este segmento durante la creación de Canvas o campañas en el paso de segmentación de usuarios.

## Coincidencia de usuarios

Los usuarios identificados pueden coincidir por su `external_id` o `alias`. Los usuarios anónimos pueden ser emparejados por su `device_id`. Los usuarios identificados que fueron creados originalmente como usuarios anónimos no pueden ser identificados por su `device_id`, y deben ser identificados por su `external_id` o `alias`.