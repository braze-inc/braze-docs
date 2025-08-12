---
nav_title: Zeotap para Currents
article_title: Zeotap para Currents
description: "Este artículo de referencia describe la asociación entre Braze Currents y Zeotap, una plataforma de datos de los clientes de nueva generación que te ayuda a descubrir y comprender a tu audiencia móvil proporcionando resolución de identidades, información y enriquecimiento de datos."
page_type: partner
tool: Currents
search_tag: Partner
---

# Zeotap para Currents

> [Zeotap](https://zeotap.com/) es una plataforma de datos de clientes de nueva generación que le ayuda a descubrir y comprender a su audiencia móvil proporcionando resolución de identidades, perspectivas y enriquecimiento de datos.

La integración de Braze y Zeotap te permite ampliar la escala y el alcance de tus campañas sincronizando los segmentos de clientes de Zeotap con los perfiles de usuario de Braze. Con [Currents]({{site.baseurl}}/user_guide/data/braze_currents/), también puedes conectar los datos a Zeotap para que sean procesables en todo el stack de crecimiento.

{% alert important %}
El conector HTTP personalizado está actualmente en fase beta. Si te interesa configurar esta integración, ponte en contacto con tu administrador del éxito del cliente.
{% endalert %}

## Requisitos previos

| Requisito | Descripción |
| --- | --- |
|Cuenta Zeotap | Se necesita una [cuenta Zeotap](https://zeotap.com/) para beneficiarse de esta asociación. |
| Currents | Para volver a exportar datos a Zeotap, tienes que tener configurado [Braze Currents]({{site.baseurl}}/user_guide/data/braze_currents/) en tu cuenta. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Aplicación

### Paso 1: Crear una fuente Currents

1. En Zeotap, ve a **Fuentes** en **Integrar**.
2. Selecciona **Crear fuente**.
3. Selecciona **Canales de interacción con los clientes** como categoría.<br><br>![Una ventana "Crear fuente" que enumera diferentes categorías, incluidos los "Canales de interacción con los clientes".]({% image_buster /assets/img/zeotap/cec.png %}){: style="max-width:70%;"}<br><br>
4. Selecciona **Braze** como origen de datos.
5. Introduce un nombre de fuente.
6. Selecciona tu región.<br><br>![Ventana con opciones para seleccionar tu región y entidad de datos.]({% image_buster /assets/img/zeotap/select_region.png %}){: style="max-width:70%;"}<br><br>
7. Selecciona **Crear fuente**.
8. Ve a la pestaña **Detalles de la implementación** y toma nota de la **URL de la API** y de **la clave de escritura**.<br><br>![Detalles de la implementación de Braze Currents que contiene la URL de la API y la clave de escritura.]({% image_buster /assets/img/zeotap/implementation_details.png %})

### Paso 2: Configurar la transmisión de datos en Currents

1. En Braze, ve a **Integraciones de socios** > **Exportación de datos**.
2. Selecciona **Crear nueva corriente** y **Exportar corrientes personalizadas**.<br><br>![El botón "Crear nueva corriente" con un desplegable que contiene "Exportar Currents personalizadas".]({% image_buster /assets/img/zeotap/custom_currents_export.png %}){: style="max-width:60%;"}<br><br>
3. Introduce un nombre de integración y un correo electrónico para ser contactado si se producen errores con la integración.
4. En **Credenciales**, introduce la siguiente información que anotaste en [el Paso 1](#step-1-create-a-currents-source):
- La URL de la API como **punto final**
- La clave de escritura como **token portador**<br><br>![Secciones para introducir detalles de la integración y credenciales.]({% image_buster /assets/img/zeotap/credentials.png %})<br><br>
5. Selecciona los eventos de interacción de mensajes que quieres enviar a Zeotap.<br><br>![La pestaña "Configuración general" con una sección para seleccionar eventos de interacción de mensajes.]({% image_buster /assets/img/zeotap/message_engagement_events.png %})
6. Selecciona **Lanzar Corriente** para guardar los cambios y empezar a enviar eventos a Zeotap.

{% alert important %}
El conector Currents no admite usuarios anónimos (usuarios sin `external_id`).
{% endalert %}

