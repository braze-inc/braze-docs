---
nav_title: Heap
article_title: "Análisis de Heap"
description: "Este artículo de referencia describe cómo utilizar Braze Currents para analizar automáticamente eventos de interacción con Heap, una plataforma de información digital, que te permite importar datos de Heap a Braze, crear cohortes de usuarios y exportar datos de Braze a Heap para crear segmentos."
page_type: partner
alias: /partners/heap/
search_tag: Partner

---

# Análisis de Heap

> Este artículo describe cómo enviar automáticamente eventos de interacción de Braze a Heap para su análisis. Para más información sobre la integración de Heap y sus otras funcionalidades, como la [sincronización de cohortes de Heap]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/heap/#data-import-integration) con Braze, consulta el [artículo principal sobre Heap]({{site.baseurl}}/partners/data_and_analytics/analytics/heap/heap_cohort_import/).

## Integración de exportación de datos

Utiliza Braze Currents para enviar automáticamente eventos de interacción (por ejemplo, correo electrónico enviado, push enviado) desde Braze a Heap para su análisis.

### Paso 1: Obtener credenciales de Heap

Necesitarás una URL de punto final de webhook para configurar esta integración, que puedes obtener de tu director de cuentas de Heap.

### Paso 2: Configurar Braze Currents

En Braze, ve a **Integraciones de socios** > **Exportación de datos**, haz clic en **Crear nuevo Current** y selecciona **Exportación de Heap**. 

Dale un nombre a tu exportación y pasa a la página **Detalles de Current**. En esta página, introduce el endpoint y el token de portador opcional (si se proporciona).

Tras configurar las credenciales de tu integración, comprueba todos los eventos de interacción con los mensajes, comportamiento del cliente y usuario que quieras exportar a Heap, y haz clic en **Iniciar Current**.

![]({% image_buster /assets/img/heap/heap4.png %}){: style="max-width:90%;"}

