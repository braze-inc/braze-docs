---
nav_title: Pila Importación de cohortes
article_title: Pila Importación de cohortes
description: "Este artículo de referencia detalla la integración entre Braze y Heap, una plataforma de insights digitales, que permite importar datos de Heap a Braze, crear cohortes de usuarios, así como exportar datos de Braze a Heap para crear segmentos."
alias: /partners/heap_cohort_import/
page_type: partner
search_tag: Partner

---

# Pila importación de cohortes

> [Heap](https://heap.io/), una plataforma de información digital, te centra en las oportunidades de tu experiencia digital que más afectan a tu negocio, eliminando fricciones, deleitando a tus clientes y acelerando los ingresos.

La integración de Braze y Heap permite [importar datos de Heap a Braze](#data-import-integration), crear cohortes de usuarios, así como [exportar datos de Braze a Heap]({{site.baseurl}}/partners/data_and_analytics/analytics/heap/) para crear segmentos.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Heap | Se necesita una cuenta [Heap](https://heap.io/about) para beneficiarse de esta asociación. |
| Clave de importación de datos Braze | Esto se puede capturar en el panel Braze desde **Integraciones de socios** > **Socios tecnológicos** y luego seleccionar **Heap**. |
| Punto final REST Braze | [La URL de tu punto final REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto final dependerá de la URL Braze de tu instancia. |
| Braze Currents | Para exportar datos de Braze a Heap, necesitarás que [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) esté activado en tu cuenta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos prácticos
- Vuelva a captar a los usuarios que hayan abandonado un embudo: Active los mensajes de reactivación cuando los usuarios abandonen el embudo de compra o suscripción.
- Personaliza la experiencia de la prueba: Identifique los puntos de fricción en su experiencia de prueba y envíe recordatorios en el momento adecuado para volver a atraer a los usuarios durante una prueba y ayudarles a obtener valor.
- Consiga una mayor participación en anuncios y ofertas: Dirija las promociones, actualizaciones y anuncios de nuevos servicios a las audiencias pertinentes.

## Integración de la importación de datos

Utilice la integración de Heap con Braze para sincronizar automáticamente las cohortes definidas en Heap con Braze.

### Paso 1: Obtener la clave de importación de datos Braze

En Braze, vaya a **Integraciones de socios** > **Socios tecnológicos** y seleccione **Heap**. 

En esta página, puedes encontrar tu clave de importación de datos y un punto final REST. Tome nota de estos dos valores y facilíteselos a su gestor de cuenta de Heap para terminar de configurar la integración.

![]({% image_buster /assets/img/heap/heap2.png %}){: style="max-width:90%;"}

### Paso 2: Segmentar usuarios importados en Braze

En Braze, vaya a **Segmentos**, asigne un nombre a su segmento de cohortes de montón y seleccione **Cohortes de montón** como filtro. Desde aquí, puedes elegir qué cohorte de Heap deseas incluir. Una vez creado su segmento de cohorte Heap, puede seleccionarlo como filtro de audiencia al crear una campaña o Canvas.

![En el constructor de segmentos Braze, el filtro de atributos de usuario "Cohorte de montón" se establece en "incluye" y "Cohorte de prueba de montón".]({% image_buster /assets/img/heap/heap1.png %}){: style="max-width:90%;"}

### Uso de esta integración

Para utilizar su segmento Heap, cree una campaña Braze o Canvas y seleccione el segmento como público objetivo.

![En el constructor de campañas Braze, en el paso de segmentación, el filtro "Usuarios objetivo por segmento" se establece en "Cohorte de montón".]({% image_buster /assets/img/heap/heap3.png %}){: style="max-width:90%;"}

{% alert important %}
Sólo se añadirán o eliminarán de una cohorte los usuarios que ya existan en Braze. La importación de cohortes no creará nuevos usuarios en Braze.
{% endalert %}

## Detalles de la integración

La estructura de la carga útil de los datos exportados es la misma que la de los conectores HTTP personalizados, que puede consultarse en el [repositorio de ejemplos de conectores HTTP personalizados](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors).

## Coincidencia de usuarios

Los usuarios identificados pueden coincidir por su `external_id` o `alias`. Los usuarios anónimos pueden ser emparejados por su `device_id`. Los usuarios identificados que fueron creados originalmente como usuarios anónimos no pueden ser identificados por su `device_id`, y deben ser identificados por su `external_id` o `alias`.

