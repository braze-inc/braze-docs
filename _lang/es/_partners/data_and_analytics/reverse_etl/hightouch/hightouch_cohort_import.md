---
nav_title: Importación de cohortes Hightouch
article_title: Importación de cohortes Hightouch
description: "Este artículo de referencia describe la funcionalidad de importación de cohortes de Hightouch, una plataforma para sincronizar los datos de sus clientes desde su almacén a las herramientas empresariales."
page_type: partner
search_tag: Partner

---
# Importación de cohortes Hightouch

> Este artículo describe cómo importar cohortes de usuarios de [Hightouch](https://hightouch.io) a Braze para que pueda enviar campañas específicas basadas en datos que sólo pueden existir en su almacén. Para más información sobre la integración de Hightouch y sus otras funcionalidades, consulte el [artículo principal sobre Hightouch]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/hightouch/hightouch/).

## Integración de la importación de datos

### Paso 1: Obtener la clave de importación de datos Braze
En Braze, vaya a **Integraciones de socios** > **Socios tecnológicos** y seleccione **Hightouch**. 

Aquí encontrarás tu punto final REST y generarás tu clave de importación de datos Braze. Una vez generada la clave, puede crear una nueva o invalidar una existente.<br><br>![]({% image_buster /assets/img/hightouch/data_import_key.png %}){: style="max-width:90%;"} 

### Paso 2: Añadir cohortes Braze como destino en Hightouch
Vaya a la página **Destino** en su espacio de trabajo Hightouch, busque **Cohortes Braze** y haga clic en **Continuar**. A partir de ahí, tome su punto final REST y la clave de importación de datos y haga clic en **Continuar**.<br><br>![]({% image_buster /assets/img/hightouch/cohort1.png %}){: style="max-width:90%;"}

### Paso 3: Sincronizar un modelo (o público) en Braze Cohorts
En Hightouch, usando tu [modelo](https://hightouch.io/docs/getting-started/create-your-first-sync/#create-a-model) o [audiencia](https://hightouch.io/docs/audiences/usage/) creada, crea una nueva sincronización. A continuación, seleccione el destino Braze Cohorts que creó en el paso anterior. Por último, en la configuración de destino de las cohortes Braze, seleccione el identificador con el que desea comparar y decida si desea que Hightouch cree una nueva cohorte Braze o actualice una existente.<br><br>![]({% image_buster /assets/img/hightouch/cohort2.png %}){: style="max-width:90%;"}

{% alert important %}
Sólo se añadirán o eliminarán de una cohorte los usuarios que ya existan en Braze. La importación de cohortes no creará nuevos usuarios en Braze.
{% endalert %}

### Paso 4: Crear un segmento Braze a partir del público personalizado Hightouch
En Braze, vaya a **Segmentos**, cree un nuevo segmento y seleccione **Cohortes Hightouch** como filtro. Desde aquí, puedes elegir qué cohorte Hightouch deseas incluir. Una vez creado su segmento de cohorte Hightouch, puede seleccionarlo como filtro de audiencia al crear una campaña o Canvas.<br><br>![]({% image_buster /assets/img/hightouch/cohort3.png %}){: style="max-width:90%;"}

### Uso de esta integración
Para utilizar su segmento Hightouch, cree una campaña Braze o Canvas y seleccione el segmento como público objetivo.<br><br>![]({% image_buster /assets/img/hightouch/cohort4.png %}){: style="max-width:90%;"}

## Coincidencia de usuarios

Los usuarios identificados pueden coincidir por su `external_id` o `alias`. Los usuarios anónimos pueden ser emparejados por su `device_id`. Los usuarios identificados que fueron creados originalmente como usuarios anónimos no pueden ser identificados por su `device_id`, y deben ser identificados por su `external_id` o `alias`.

