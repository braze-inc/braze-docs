---
nav_title: Envío de lienzos de prueba
article_title: Envío de lienzos de prueba
page_order: 1
description: "Este artículo de referencia trata sobre cómo probar un Canvas antes de su lanzamiento y las mejores prácticas."
page_type: reference
tool: Canvas
---

# Envío de lonas de prueba

> Después de [crear tu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/), hay varias comprobaciones que puedes querer realizar antes de lanzarlo, dependiendo de detalles como el tamaño de tu audiencia o el número de filtros de segmentación.

Cuando sea posible, Braze recomienda probar un Canvas antes de lanzarlo. Esta prueba se realizará normalmente en su entorno Braze. Probar su Canvas puede implicar duplicarlo, llevar a los usuarios de prueba a través del recorrido del usuario y comprobar si el comportamiento del usuario se alinea con lo que ha esbozado en su Canvas.

## Paso 1: Crea tu plan de pruebas

Crear un plan de pruebas es esencial antes de empezar a probar tu Canvas. Un plan de pruebas puede ayudar a identificar y realizar un seguimiento de áreas específicas de su recorrido por Canvas.

Cuando elabores tu plan de pruebas, ten en cuenta las siguientes preguntas:
- ¿Se ha creado al menos un usuario para cada rama y ruta de Canvas?
- ¿Se utiliza algún segmento en su Canvas? 
	- Si se utilizan segmentos, puede haber requisitos previos para que un usuario entre en el Canvas antes de ser elegible para un viaje de usuario.
- ¿Tienen los mensajes del lienzo de pruebas algún tipo de líquido en los títulos de los mensajes que recurra al ID de usuario o a la dirección de correo electrónico para garantizar que sean fáciles de identificar tanto el mensaje como el usuario con fines de prueba?

## Paso 2: Identificar a los usuarios de prueba

A continuación, identifique un conjunto de usuarios de prueba que seguirán los pasos del lienzo sin enviar mensajes a los usuarios previstos. Los usuarios de prueba pueden ser direcciones de correo electrónico existentes que no se utilicen para servicios reales en el panel de control de Braze, o bien nuevas direcciones de correo electrónico que se utilicen exclusivamente con fines de prueba. 

## Paso 3: Configura tu Canvas

A continuación, ¡es hora de probar tu Canvas! Para mantener organizados tu Canvas original y la información del Canvas de prueba, crea un duplicado de tu Canvas con fines de prueba.

Hay dos formas de probar tu Canvas. 

- **Método 1:** En el lienzo duplicado, edite la parte **Audiencia de entrada** del constructor del lienzo para que sólo los usuarios de prueba sean elegibles para el lienzo. También puede introducir su propia dirección de correo electrónico como usuario de prueba añadiendo el filtro de prueba **Dirección de correo electrónico**. En el ejemplo siguiente, hemos limitado el Canvas a dos usuarios de prueba que han utilizado la aplicación por primera vez hace menos de tres días.

![Un Canvas con una audiencia de entrada de "Utilizó por primera vez estas aplicaciones hace menos de 3 días" y las direcciones de correo electrónico de dos usuarios de prueba.]({% image_buster /assets/img_archive/canvas_test2.png %}){: style="max-width:90%;"}

- **Método 2:** [Previsualice sus rutas de usuario]({{site.baseurl}}/preview_user_paths/) seleccionando el botón **Probar lienzo** en el pie de página del constructor de lienzos.

## Paso 4: Inicia tu prueba

Lance su Canvas de prueba para que los usuarios puedan empezar a entrar. Completa los comportamientos de usuario en tu aplicación que enviarían a los usuarios a través del recorrido Canvas correspondiente.

Compruebe que los usuarios de prueba reciben los mensajes previstos de los pasos de Canvas. Tenga en cuenta que sus usuarios de prueba pueden no recibir un mensaje debido a razones no limitadas a:

- No elegible para el grupo de control global
- Limitaciones de frecuencia
- Pertenencia a un segmento no coincidente
- Mensajes cancelados
- Tokens push asociados a diferentes usuarios

Continúe iterando las pruebas de Canvas para asegurarse de que su Canvas funciona como se pretende.

## Consejos generales

### Identifique sus pasos en el lienzo

En algunos casos, un usuario puede recibir varios mensajes al pasar por un Canvas. Si el retardo entre pasos se ha reducido significativamente para las pruebas, puede que no siempre esté claro qué mensaje se está activando durante las pruebas. Asegurarse de que los mensajes de prueba incluyen el nombre del paso o el ID de usuario (utilizando Liquid) facilitará la identificación y confirmación de si se ha enviado el mensaje correcto a los usuarios correctos.

### Crear un grupo interno

En lugar de crear usuarios de prueba individuales, puede crear un [Grupo de Prueba de Contenido]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/), que es un Grupo Interno cuyo propósito es revisar el contenido de su mensaje. Incluye un grupo de usuarios que recibirán mensajes de prueba de campañas y Lienzos. A continuación, puede añadir este grupo de prueba en el campo **Añadir grupos de prueba de contenido** en **Destinatarios de prueba**.

### Reducir el tiempo de retraso

Para que las pruebas sean más eficaces, te sugerimos que reduzcas el tiempo de retraso a minutos o segundos para las pruebas, de modo que puedas ver los mensajes en el momento oportuno. Por ejemplo, deje pasar al menos 2 ó 3 minutos entre las pruebas para poder aislar acciones específicas en trayectos concretos de Canvas.

### Aprovechar los bloques de contenido

Si algún contenido se va a repetir en su marco de pruebas (por ejemplo, Líquido complejo para filtrar usuarios en diferentes pasos de Canvas), intente guardar este contenido repetido como un [Bloque de Contenido]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks). Ahora, podrás incluir el Bloque de Contenido a lo largo de los pasos individuales de Canvas.

### Utilizar Postman y el punto final Seguimiento de usuarios

Puede ejecutar pruebas con Postman y [Braze Postman Collection]({{site.baseurl}}/api/postman_collection/). Utilice el [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para registrar y realizar un seguimiento de los eventos y compras personalizados de sus distintos usuarios de prueba.

Tenga en cuenta que el envío de datos a la API de seguimiento de usuarios sólo puede realizarse con un ID externo. Por lo tanto, es posible que los usuarios de prueba deban añadirse como usuarios de prueba dentro de un grupo interno en el cuadro de mandos de Braze para poder investigar más a fondo errores específicos. 

#### Pruebas para múltiples ramas

Cuando esté probando un Canvas con múltiples ramas que se dirigen a los usuarios en función de diferentes atributos y eventos, siga este plan de pruebas:

1. Para cada rama, identifique los atributos y eventos que el usuario debe tener para ser incluido en el recorrido Canvas.
2. Constrúyelos en una carga útil JSON que se publicará utilizando el punto final `/users/track`.

