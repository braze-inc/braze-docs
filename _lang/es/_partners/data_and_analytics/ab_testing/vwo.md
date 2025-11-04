---
nav_title: VWO
article_title: Integración de VWO con Braze
description: "Aprende a integrar VWO con Braze."
alias: /partners/vwo/
page_type: partner
search_tag: Partner
---

# VWO

> [VWO](https://vwo.com/) es una potente plataforma de experimentación que ayuda a las marcas a mejorar las métricas empresariales clave, habilitando a los equipos para ejecutar programas de optimización de la conversión respaldados por los datos de comportamiento del cliente. Con VWO, puedes unificar los datos de clientes, obtener información sobre su comportamiento, crear hipótesis, realizar pruebas A/B en múltiples plataformas (servidor, Web y móvil), desplegar características, personalizar experiencias y optimizar todo el recorrido del cliente.

Al integrar VWO con Braze, puedes aprovechar los datos de los experimentos de VWO para crear segmentos específicos y entregar campañas personalizadas.

## Requisitos previos

| Requisito     | Descripción |
|-----------------|-------------|
| Cuenta VWO     | Una cuenta VWO con acceso a los datos de experimentación. |
| Cuenta Braze   | Una cuenta Braze activa con el [SDK Braze Web]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) integrado en tu página web. También necesitarás que se habilite la segmentación de propiedades del evento. Para solicitarlo, consulta [Consideraciones](#request-event-property-segmentation). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Integración de VWO con Braze

### Paso 1: Habilitar la integración de Braze en VWO

1. Conéctate a tu cuenta VWO.
2. En el panel VWO, ve a **Configuraciones > Integraciones.** Aquí puedes habilitar las integraciones a nivel de espacio de trabajo, lo que aplica la integración a todas las campañas de prueba futuras de forma predeterminada.

   ![Configuración de la integración VWO]({% image_buster /assets/img/vwo/vwo1_settings.png %})

4. Selecciona la integración Braze para habilitarla.
5. Opcionalmente, puedes habilitar la integración Braze para cualquier campaña existente. Para ello, selecciona una campaña, ve a **Configuración > Integraciones** y habilita Braze.

   ![Habilitar la integración de Braze]({% image_buster /assets/img/vwo/vwo2_enable_braze.png %})

6. Después de habilitar la integración, VWO empezará a enviar datos de experimentos a Braze a nivel de campaña.

### Paso 2: Crear un segmento en Braze con propiedades del evento VWO

1. En el panel de Braze, selecciona **Segmentos** > **\+ Crear segmento**.
3. En la ventana **Crear** **segmento**, introduce un nombre para el segmento y, a continuación, **Crea segmento**.
4. En tu segmento recién creado, selecciona **Filtros** > **Añadir filtro** y, a continuación, elige **Evento personalizado** como tipo de filtro.
6. En el desplegable de filtros, busca **VWO**.
7. Selecciona la propiedad VWO correspondiente y especifica el valor requerido.
8. Si es necesario, configura el número de visitas y el periodo de tiempo. Cuando haya terminado, seleccione **Guardar**.

   ![Creación de segmentos Braze]({% image_buster /assets/img/vwo/vwo3_braze_segment.png %})

9. Para ver el número de usuarios que coinciden con tus criterios de segmentación, selecciona **Calcular estadísticas exactas**.

   ![Estadísticas del segmento Braze]({% image_buster /assets/img/vwo/vwo4_braze_segment_calculate_size.png %})

## Flujo de datos

VWO envía los datos del experimento de la campaña a Braze como un evento personalizado utilizando el siguiente formato:

- **Nombre del evento:** VWO
- **Propiedades del evento:** `vwo_campaign_name`, `vwo_variation_name`

{% alert tip %}
Estas propiedades del evento personalizadas también pueden utilizarse para la segmentación y la orientación.
{% endalert %}

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
         <td>Solicitud para habilitar la segmentación de propiedades del evento para la integración de VWO</td>
      </tr>
      <tr>
         <td><strong>Cuerpo</strong></td>
         <td>
         Hola equipo Braze,<br><br>
         Nos gustaría habilitar la segmentación de propiedades de eventos para los eventos enviados desde nuestra integración VWO&lt;>Braze. Aquí tienes toda la información para asistir:<br><br>
         - <strong>Nombre del evento:</strong> VWO<br>
         - <strong>Propiedades del evento:</strong> <code>vwo_campaign_name</code>, <code>vwo_variation_name</code><br><br>
         Confírmanos una vez habilitadas las propiedades en nuestra cuenta.<br><br>
         Gracias.
         </td>
      </tr>
   </tbody>
   </table>
   {: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Puntos de datos Braze

El evento personalizado enviado desde VWO a Braze -incluidas las propiedades del evento habilitadas para la segmentación- consumirá puntos de datos en tu instancia de Braze.

### Limitaciones

Actualmente, esta integración no admite la sincronización en tiempo real de los datos de las pruebas. Los datos de la prueba pueden tardar hasta 15 minutos en aparecer en Braze.

## Solución de problemas

Si no ves los datos de VWO en Braze:

1. Haz clic con el botón derecho del ratón en la página en la que se está ejecutando tu campaña de prueba y selecciona **Inspeccionar elemento**.
2. En la pestaña **Red**, busca **Braze** para filtrar las llamadas de red para Braze.
3. Las llamadas a la red se rellenan a medida que se carga la página. Puedes recargar la página para ver las llamadas de red.
4. Selecciona una llamada de red para ver más detalles.
5. Ve a la sección **Carga útil de la solicitud** en la pestaña **Carga útil**, donde encontrarás los eventos: que tienen el nombre: **ce**, que indica Evento personalizado.
6. Amplía 0: y datos: para ver n: "VWO" (nombre del evento personalizado) y p: {vwo_campaign_name: "<your vwo campaign name>", vwo_variation_name: "<variation name>"}. Indican que los valores están siendo pushados por VWO a Braze.

 ![Braze Solución de problemas]({% image_buster /assets/img/vwo/vwo5_troubleshooting.png %})

Para obtener ayuda adicional, ponte en contacto con tu administrador del éxito del cliente de VWO.
