---
nav_title: Socios disponibles
article_title: Socios de Currents disponibles
page_order: 2
page_type: reference
description: "Este artículo de referencia describe los socios de datos que puede utilizar para integrarse con Braze Currents y sus casos de uso."
tool: Currents

---

# Socios disponibles

> Esta página enumera los socios de datos que puedes integrar con Braze Currents y describe sus casos de uso. 

{% alert note %}
Las convenciones de nomenclatura para eventos que fluyen para un socio de Braze pueden no coincidir con otros socios. Por ejemplo, el evento de apertura de correo electrónico de Currents en Segment es `Email Opened`, mientras que en Mixpanel es `Email Open`.
{% endalert %}

## Almacenamiento en almacén de datos
[![Curso Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/introduction-to-data-warehouses){: style="float:right;width:120px;border:0;" class="noimgborder"}
El almacenamiento en almacén de datos ofrece una fuente de recopilación de toda la información transmitida desde Currents. Estos socios pueden actuar como almacenes (para el almacenamiento de archivos planos) o utilizarse para alimentar herramientas de inteligencia empresarial y algoritmos de aprendizaje automático, obtener información sobre el rendimiento del marketing y mucho más.

* [Amazon S3][1]
* [Google Cloud Storage][2]
* [Almacenamiento Blob de Microsoft Azure][3]

Tenemos tanta confianza en el poder de Currents y los almacenes de datos juntos, ¡que [nosotros mismos lo utilizamos]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/how_braze_uses_currents/)!

## Datos del cliente

Estas plataformas de datos de clientes recopilan y dirigen información de múltiples fuentes a una variedad de otras ubicaciones para permitirle utilizar los datos Braze de la mejor manera posible.

* [mParticle][6]
* [Segmento][7]
* [Tealium][8]
* [Treasure Data][10]
* [RudderStack][9]
* [Adobe][12]

## Análisis del comportamiento

Estos socios están especializados en análisis de productos e inteligencia empresarial y pueden ayudarle a interactuar con sus usuarios en función de sus acciones.

* [Amplitude][4]

* [Mixpanel][5]

* [Heap][11]



[1]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/amazon_s3/
[2]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/google_cloud_storage_for_currents/
[3]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/microsoft_azure_blob_storage_for_currents/
[4]: {{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_for_currents/
[5]: {{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/
[6]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/mParticle/mparticle_for_currents/
[7]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_for_currents/
[8]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium_for_currents#tealium-for-currents
[9]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/rudderstack/rudderstack_for_currents/
[10]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/treasure_data/treasure_data_for_currents/
[11]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/heap/
[12]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/adobe/adobe_for_currents/