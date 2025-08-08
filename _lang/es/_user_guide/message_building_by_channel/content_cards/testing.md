---
nav_title: Pruebas
article_title: Pruebas de las tarjetas de contenido
page_order: 3
description: "Este artículo de referencia explica cómo previsualizar y probar las tarjetas de contenido, así como algunas buenas prácticas."
channel:
  - content cards
  
---

# Pruebas de las tarjetas de contenido

> Es muy importante probar siempre las tarjetas de contenido antes de enviar las campañas. Nuestras funciones de previsualización y prueba ofrecen dos maneras de echar un vistazo a sus tarjetas de contenido. Puedes previsualizar tu mensaje para ayudarte a visualizarlo mientras lo redactas, así como enviar un mensaje de prueba a ti mismo o al dispositivo de un usuario concreto. Le recomendamos que aproveche ambas.

## Vista previa

Puedes previsualizar tu tarjeta mientras la redactas. Esto le ayudará a visualizar el mensaje final desde la perspectiva del usuario.

En la pestaña **Vista previa** de tu compositor, la vista de tu mensaje puede no ser idéntica a su representación real en el dispositivo del usuario. Recomendamos enviar siempre un mensaje de prueba a un dispositivo para asegurarse de que los medios, la copia, la personalización y los atributos personalizados se generan correctamente.

## Probar

Para enviar una prueba a [grupos de prueba de contenido]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) o a usuarios individuales, antes de enviarla debe estar activada la función push en los dispositivos de prueba con tokens push válidos registrados para el usuario de prueba. Los usuarios de iOS deben tocar la notificación push enviada por Braze para ver la tarjeta de contenido de la prueba. Este comportamiento sólo se aplica a las tarjetas de contenido de prueba.

### Vista previa del mensaje como usuario

También puedes previsualizar los mensajes desde la pestaña **Prueba** como si fueras un usuario. Puede seleccionar un usuario específico, un usuario aleatorio o crear un usuario personalizado.

![Una vista previa de la tarjeta de contenido en la pestaña "Prueba".]({% image_buster /assets/img/cc-user-preview.png %}){: style="max-width:80%;"}

### Lista de comprobación

- ¿Aparecen las imágenes y los medios de comunicación y actúan como se esperaba?
- ¿Funciona el Líquido como se esperaba? ¿Ha previsto un [valor de atributo por defecto]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) en caso de que Liquid no devuelva ninguna información?
- ¿Es su texto claro, conciso y correcto?
- ¿Sus enlaces dirigen al usuario a donde debe ir?

## Depurar

Una vez enviadas las tarjetas de contenido, puede desglosar o depurar cualquier problema desde el [registro de usuario de eventos]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) de la consola de desarrollador. 

Un caso de uso común es tratar de depurar por qué un usuario no puede ver una tarjeta de contenido en particular. Para ello, puedes buscar en **los registros de usuarios del evento** las tarjetas de contenido entregadas al SDK al inicio de la sesión, pero antes de una impresión, y rastrearlas hasta una campaña específica:

1. Vaya a **Configuración** > **Registro de usuario de eventos**.
2. Localiza y amplía la Solicitud de SDK para tu usuario de prueba.
3. Haga clic en **Datos brutos**.
4. Busca la dirección `id` para tu sesión. A continuación se muestra un extracto de ejemplo:

    ```json
    [
      {
        "session_id": "D1B051E6-469B-47E2-B830-5A728D1D4AC5",
        "data": {
          "ids": [
            "NDg2MTY5MmUtNmZjZS00MjE1LWJkMDUtMzI1NGZiOWU5MDU3"
          ]
        },
        "name": "cci",
        "time": 1636106490.155
      }
    ]
    ```

5. Utilice una herramienta de descodificación como [Base64 Decode and Encode](https://www.base64decode.org/) para descodificar el `id` del formato Base64 y encontrar el `campaign_id` asociado. En nuestro ejemplo, el resultado es el siguiente:

    ```
    4861692e-6fce-4215-bd05-3254fb9e9057_$_cc=c3b25740-f113-c047-4b1d-d296f280af4f&mv=6185005b9d9bee79387cce45&pi=cmp
    ```

    Donde `4861692e-6fce-4215-bd05-3254fb9e9057` es el `campaign_id`.<br><br>

6. Vaya a la página de **Campañas** y busque `campaign_id`.

![Buscar campaign_id en la página de Campañas]({% image_buster /assets/img_archive/cc_debug.png %}){: style="max-width:80%;"}

A partir de ahí, puede revisar la configuración y el contenido de sus mensajes para determinar por qué un usuario no puede ver una tarjeta de contenido concreta.

