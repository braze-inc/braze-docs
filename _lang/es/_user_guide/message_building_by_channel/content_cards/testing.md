---
nav_title: Prueba
article_title: Probando tarjetas de contenido
page_order: 3
description: "Este artículo de referencia explica cómo previsualizar y probar las tarjetas de contenido, así como algunas buenas prácticas."
channel:
  - content cards
  
---

# Probando tarjetas de contenido

> Es muy importante que pruebes siempre tus tarjetas de contenido antes de enviar tus campañas. Nuestras capacidades de vista previa y de prueba ofrecen dos formas de echar un vistazo a tus tarjetas de contenido. Puedes previsualizar tu mensaje para ayudarte a visualizarlo mientras lo redactas, así como enviarte un mensaje de prueba a ti mismo o al dispositivo de un usuario concreto. Te recomendamos que aproveches ambas.

## Vista previa

Puedes obtener una vista previa de tu tarjeta mientras la compones. Esto debería ayudarte a visualizar cómo será tu mensaje final desde la perspectiva de tu usuario.

En la pestaña **Vista previa** de tu compositor, la vista de tu mensaje podría no ser idéntica a su representación real en el dispositivo del usuario. Te recomendamos que envíes siempre un mensaje de prueba a un dispositivo para asegurarte de que tus medios, copia, personalización y atributos personalizados se generan correctamente.

## Prueba

Para enviar una prueba a [grupos de prueba de contenido]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) o a usuarios individuales, debe habilitarse la función push en tus dispositivos de prueba con tokens de notificaciones push válidos registrados para el usuario de prueba antes del envío. Para los usuarios de iOS, debes tocar la notificación push enviada por Braze para ver la tarjeta de contenido de la prueba. Este comportamiento sólo se aplica a las tarjetas de contenido de prueba.

### Vista previa del mensaje como usuario

También puedes obtener una vista previa de los mensajes desde la pestaña de **Prueba**, como si fueras un usuario. Puedes seleccionar un usuario concreto, un usuario aleatorio o crear un usuario personalizado.

Una vista previa de la tarjeta de contenido en la pestaña "Prueba".]({% image_buster /assets/img/cc-user-preview.png %}){: style="max-width:80%;"}

### Lista de control

- ¿Aparecen las imágenes y los medios y actúan como se espera de ellos?
- ¿Funciona el Liquid como se esperaba? ¿Has previsto un [valor de atributo predeterminado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) para el caso de que Liquid no devuelva información?
- ¿Es tu texto claro, conciso y correcto?
- ¿Tus enlaces dirigen al usuario a donde debe ir?

## Depurar

Una vez enviadas tus tarjetas de contenido, puedes desglosar o depurar cualquier problema desde el [registro de usuarios del evento]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) en la consola para desarrolladores. 

Un caso de uso común es intentar depurar por qué un usuario no puede ver una determinada tarjeta de contenido. Para ello, puedes buscar en **los registros de usuarios del evento** las tarjetas de contenido entregadas al SDK al inicio de la sesión, pero antes de una impresión, y rastrearlas hasta una campaña específica:

1. Ve a **Configuración** > **Registro de usuarios** del evento **.**
2. Localiza y amplía la Solicitud de SDK para tu usuario de prueba.
3. Haz clic en **Datos brutos**.
4. Encuentra la dirección `id` para tu sesión. A continuación se muestra un extracto de ejemplo:

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

5. Utiliza una herramienta de descodificación como [Base64 Decode and Encode](https://www.base64decode.org/) para descodificar el `id` del formato Base64 y encontrar el `campaign_id` asociado. En nuestro ejemplo, el resultado es el siguiente:

    ```
    4861692e-6fce-4215-bd05-3254fb9e9057_$_cc=c3b25740-f113-c047-4b1d-d296f280af4f&mv=6185005b9d9bee79387cce45&pi=cmp
    ```

    Donde `4861692e-6fce-4215-bd05-3254fb9e9057` es el `campaign_id`.<br><br>

6. Ve a la página de **Campañas** y busca `campaign_id`.

\![Busca campaign_id en la página de Campañas]({% image_buster /assets/img_archive/cc_debug.png %}){: style="max-width:80%;"}

A partir de ahí, puedes revisar tu configuración de mensajería y contenido para profundizar y determinar por qué un usuario no puede ver una tarjeta de contenido concreta.

