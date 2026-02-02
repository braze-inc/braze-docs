---
nav_title: Kameleoon
article_title: Kameleoon
description: "Aprende a integrar Kameleoon con Braze"
alias: /partners/kameleoon/
page_type: partner
search_tag: Partner
---

# Kameleoon

>[Kameleoon](https://www.kameleoon.com) es una solución de optimización con capacidades de experimentación, personalización basada en IA y gestión de características en una única plataforma unificada.

## Requisitos previos

Antes de empezar, necesitarás lo siguiente:

| Requisito | Descripción |  
| --- | --- |  
| Cuenta Kameleoon | Se necesita una cuenta Kameleoon para beneficiarse de esta asociación.|  
| Cuenta Braze| Una cuenta Braze activa con el [SDK Braze Web]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) integrado en tu página web. También necesitarás que se habilite la segmentación de propiedades del evento. Para solicitarlo, consulta [Consideraciones](#considerations).|  
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplos

Kameleoon envía eventos personalizados a Braze para identificar a los usuarios que participan en campañas de experimentación y personalización, habilitando una orientación más precisa y mensajes personalizados.

## Integración de Kameleoon

Esta integración se ejecuta como un rastreador JavaScript a través de engine.js de Kameleoon. Se puede habilitar rápidamente desde la plataforma de Kameleoon.

### Paso 1: Ir a la página de integraciones de Kameleoon

En tu aplicación Kameleoon, selecciona **Admin** y luego **Integraciones** en la barra lateral.

![El panel de administración de la plataforma Kameleoon.]({% image_buster /assets/img/kameleoon/img_1.png %}){: style="max-width:70%;"}

### Paso 2: Instala la herramienta Braze

Por defecto, la herramienta Braze no está instalada. Busca el icono Braze y selecciona **Instalar la herramienta**. ![Un cuadrado gris con una flecha apuntando hacia abajo.]({% image_buster /assets/img/kameleoon/img_2.png %})

Selecciona los proyectos para los que deseas activar la herramienta Braze, de modo que los datos de Kameleoon se reporten correctamente a Braze.

![El icono de la herramienta Braze en Kameloon.]({% image_buster /assets/img/kameleoon/img_3.png %})

Tras configurar la herramienta, selecciona **Validar**, con lo que se cerrará el panel de configuración. A continuación, verás un botón **alternante** junto al icono de la herramienta Braze, que incluye el número de proyectos en los que está configurada la herramienta.

![La herramienta Braze alternada "Activada" en Kameleoon.]({% image_buster /assets/img/kameleoon/img_4.png %})

{% alert important %}  
Esta característica está en fase beta. Únete al [Programa Beta de Kameleoon](https://help.kameleoon.com/account-and-team-management/join-beta-program/) para empezar a utilizar esta integración.  
{% endalert %}  
    
### Paso 3: Asociar Braze a las campañas de Kameleoon

#### En el editor Gráfico/Código

Para finalizar tu experimento, selecciona el paso **Integraciones** para configurar Braze como herramienta de seguimiento y, a continuación, selecciona **Braze**.

![El panel de Integraciones en Kameleoon muestra todas las integraciones disponibles, incluida la integración activa Braze.]({% image_buster /assets/img/kameleoon/img_5.png %})

Braze se mencionará en el resumen antes de salir en vivo. Kameleoon transmitirá automáticamente los datos a Braze, y podrás utilizarlos para el análisis y la segmentación directamente en Braze.

##### Creación de personalización

En la página **Creación de personalización**, puedes seleccionar Braze entre las herramientas de elaboración de informes para personalizar tus informes.

![La sección Herramientas de elaboración de informes muestra integraciones como Heap, Mixpanel, Clarity, con Braze seleccionado.]({% image_buster /assets/img/kameleoon/img_6.png %})

##### Creación de la bandera de características

Configura la integración en el entorno de la bandera de características en la sección **Integraciones**. Habilítala para los entornos en los que quieras que esté activa.

![La página Bandera de características en Kameleoon con las integraciones disponibles. Hay dos conmutadores para cada socio, "Reglas de entrega" y "Experimentos de características".]({% image_buster /assets/img/kameleoon/img_7.png %})

##### Página de resultados

Una vez establecido Braze como herramienta de elaboración de informes para un experimento, puedes seleccionarlo (o deseleccionarlo) en la página de resultados de Kameleoon, en el menú **Configuración del experimento**.

{% alert note %}  
Esta integración requiere una [implementación híbrida](https://developers.braze-presentation.preview.kameleoon.net/core-concepts/hybrid-experimentation?language=en#sending-exposure-events-to-third-party-analytics) y sólo es compatible con SDKs Web.
{% endalert %}

![El panel lateral de la página de resultados en Kameleoon.]({% image_buster /assets/img/kameleoon/img_8.png %}){: style="max-width:50%;" }

Aparecerán las herramientas de informe asociadas al experimento. Selecciona **Editar** para modificar esta selección.

### Paso 4: Analiza y aprovecha tus datos de Kameleoon en Braze

Una vez configurada la integración, Kameleoon enviará a Braze eventos personalizados denominados `kameleoon_exposure` con propiedades como **Nombre del experimento**, **ID del experimento**, **Nombre de la variación**, **ID de la variación**.

![El registro de usuarios del evento personalizado en Braze, mostrando un ejemplo de carga útil del evento que ha recibido Braze de Kameleoon.]({% image_buster /assets/img/kameleoon/img_9.png %})

A continuación, puedes ver estos datos en los Eventos personalizados, crear informes de eventos personalizados para identificar la exposición de la campaña Kameleoon y habilitar la segmentación basada en las propiedades del evento. Puedes utilizar eventos personalizados al crear campañas y Lienzos posteriores o vinculados mediante [rutas de acción]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/#action-groups), [desencadenantes basados en acciones]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery) o creando [segmentos]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/)

Además, se podrá acceder a estos eventos a través de [los objetos de eventos personalizados de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) para poder realizar informes y análisis exhaustivos.

## Consideraciones

### Solicitar segmentación de propiedades del evento

Antes de poder utilizar la segmentación de propiedades de eventos, necesitarás habilitarla en Braze. Utiliza la siguiente plantilla para ponerte en contacto con tu CSM de Braze o con el equipo de soporte para obtener acceso.

   <table>
   <thead>
      <tr>
         <th>Campo</th>
         <th>Detalles</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td><strong>Asunto</strong></td>
         <td>Solicitud para habilitar la segmentación de propiedades del evento para la integración con Kameleoon</td>
      </tr>
      <tr>
         <td><strong>Cuerpo</strong></td>
         <td>
         Hola equipo Braze,<br><br>
         Nos gustaría habilitar la segmentación de propiedades de eventos para los eventos enviados desde nuestra integración Kameleoon&lt;>Braze. Aquí tienes toda la información para asistir:<br><br>
         - <strong>Nombre del evento:</strong> Kameleoon<br>
         - <strong>Propiedades del evento:</strong> <code>kameleoon_campaign_name</code>, <code>kameleoon_variation_name</code><br><br>
         Confírmanos una vez habilitadas las propiedades en nuestra cuenta.<br><br>
         Gracias.
         </td>
      </tr>
   </tbody>
   </table>
   {: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Puntos de datos Braze

El evento personalizado enviado desde Kameleoon a Braze -incluidas las propiedades del evento habilitadas para la segmentación- registrará puntos de datos en tu instancia de Braze.