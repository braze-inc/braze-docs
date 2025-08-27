---
nav_title: Kubit
article_title: Importación de cohortes Kubit
description: "Este artículo de referencia describe la funcionalidad de importación de cohortes de Kubit, una plataforma de análisis de autoservicio sin código que ofrece información instantánea sobre los productos, lo que le permite importar cohortes de usuarios de Kubit y dirigirlas a la mensajería Braze."
page_type: partner
search_tag: Partner
---

# Importación de cohortes Kubit

> Este artículo describe cómo importar cohortes de usuarios de [Kubit](https://kubit.ai/) a Braze. Para más información sobre la integración de Kubit y sus otras funcionalidades, consulta el [artículo principal sobre Kubit]({{site.baseurl}}/partners/data_and_analytics/analytics/kubit/).

## Integración de la importación de datos

### Paso 1: Obtener la clave de importación de datos Braze

En Braze, vaya a **Integraciones de socios** > **Socios tecnológicos** y seleccione **Kubit**. Aquí encontrarás el punto final REST y generarás tu clave de importación de datos Braze. 

Una vez generada, puede crear una nueva clave o invalidar una existente. La clave de importación de datos y el endpoint REST se utilizan en el siguiente paso cuando se configura un postback en el dashboard de Kubit.

![La página de socios tecnológicos de Kubit en Braze.]({% image_buster /assets/img/kubit/kubit.png %}){: style="max-width:90%;"}

### Paso 2: Configurar Braze en Kubit

Proporciona la clave de importación de datos de Braze y el punto final REST de Braze a tu contacto de soporte de Kubit. Ellos configurarán la integración por su parte y te avisarán cuando la integración esté activa.  

### Paso 3: Importar cohortes a Braze

#### Crear una cohorte en Kubit
[Cree una cohorte](https://www.kubit.ai/doc/fundamentals#cohort) en Kubit y defina los criterios de sus usuarios objetivo.<br><br>![]({% image_buster /assets/img/kubit/create_cohort.png %}){: style="max-width:80%;"}

#### Importar usuarios a Braze
Una vez que haya guardado su cohorte, puede importarla a Braze para utilizarla en segmentos Braze. A continuación, estos segmentos pueden utilizarse para crear campañas de correo electrónico o push específicas y lienzos.

Para ello, vaya a su cohorte existente y, en **Control de cohortes**, seleccione **Importar a Braze**.

![]({% image_buster /assets/img/kubit/import_to_braze.png %}){: style="max-width:80%;"}

A continuación, seleccione la cadencia de importación deseada. Las importaciones únicas le permiten importar ahora una sola vez. Las importaciones programadas te permiten importar diaria, semanal o mensualmente a una hora determinada. Ten en cuenta que cada cohorte sólo puede tener un programa de importación de cohortes en vivo. 

![]({% image_buster /assets/img/kubit/import_schedule.png %}){: style="max-width:40%;"}

{% alert important %}
Sólo se añadirán o eliminarán de una cohorte los usuarios que ya existan en Braze. La importación de cohortes no creará nuevos usuarios en Braze.
{% endalert %}

#### Verificar el estado de la importación
Una vez finalizada la importación, se enviará una notificación por correo electrónico a los destinatarios especificados en el calendario de importación. También puedes comprobar el estado de importación de una cohorte en **Programar** en Kubit. El historial de programación mostrará la hora de ejecución de cada importación, el resultado y el número total de usuarios de la cohorte que se importaron a Braze.<br><br>![]({% image_buster /assets/img/kubit/import_history.png %})<br><br>Puede activar manualmente una importación haciendo clic en el icono **Importar a Braze** para ese programa de importación.

### Paso 4: Crear segmentos Braze con cohortes Kubit
Después de importar cohortes a Braze, puede utilizarlas como filtros para crear segmentos Braze e incluirlos en campañas Braze o Canvas. Visite nuestra documentación de segmentos para obtener más información sobre [cómo crear segmentos Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment).

![En el constructor de segmentos Braze, el atributo de usuario "Kubit cohorts" se establece en "includes_value" y muestra una lista de las cohortes disponibles.]({% image_buster /assets/img/kubit/segment_with_kubit_cohorts.png %}){: style="max-width:70%;"}

## Coincidencia de usuarios

Los usuarios identificados pueden coincidir por su `external_id` o `alias`. Los usuarios anónimos pueden ser emparejados por su `device_id`. Los usuarios identificados que fueron creados originalmente como usuarios anónimos no pueden ser identificados por su `device_id`, y deben ser identificados por su `external_id` o `alias`.