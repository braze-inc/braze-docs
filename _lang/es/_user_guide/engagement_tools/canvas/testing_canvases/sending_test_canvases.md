---
nav_title: Envío de lienzos de prueba
article_title: Envío de lienzos de prueba
page_order: 1
description: "Este artículo de referencia explica cómo probar un Canvas antes de su lanzamiento y las mejores prácticas."
page_type: reference
tool: Canvas
---

# Envío de lienzos de prueba

> Después de [crear tu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/), hay varias comprobaciones que tal vez quieras realizar antes de lanzarlo, dependiendo de detalles como el tamaño de tu audiencia o el número de filtros de segmentación.

Cuando sea posible, Braze recomienda probar un Canvas antes de lanzarlo. Esta prueba se realizará normalmente en tu entorno Braze. Probar tu Canvas puede implicar duplicarlo, llevar a los usuarios de prueba a través del recorrido del usuario y comprobar si el comportamiento del usuario se ajusta a lo que has esbozado en tu Canvas.

## Paso 1: Crea tu plan de pruebas

Crear un plan de pruebas es esencial antes de empezar a probar tu Canvas. Un plan de pruebas puede ayudarte a identificar y seguir áreas específicas de tu recorrido por Canvas.

Cuando elabores tu plan de pruebas, ten en cuenta las siguientes preguntas:
- ¿Se ha creado al menos un usuario para cada rama y ruta de Canvas?
- ¿Se utilizan segmentos en tu Canvas? 
	- Si se utilizan segmentos, puede haber requisitos previos para que un usuario entre en el Canvas antes de ser elegible para un viaje de usuario.
- ¿Tienen los mensajes del Canvas de prueba algún Liquid en los títulos de los mensajes que tire del ID de usuario o de la dirección de correo electrónico para garantizar que sean fáciles de identificar tanto el mensaje como el usuario a efectos de prueba?

## Paso 2: Identificar usuarios de prueba

A continuación, identifica un conjunto de usuarios de prueba que seguirán los pasos en Canvas sin enviar realmente mensajes a tus usuarios previstos. Los usuarios de prueba pueden ser direcciones de correo electrónico existentes que no se utilicen para servicios reales en tu panel Braze, o bien nuevas direcciones de correo electrónico que se utilicen exclusivamente con fines de prueba. 

## Paso 3: Configura tu Canvas

A continuación, ¡es hora de probar tu Canvas! Para mantener organizados tu Canvas original y la información del Canvas de prueba, crea un duplicado de tu Canvas con fines de prueba.

Hay dos formas de probar tu Canvas. 

- **Método 1:** En el Canvas duplicado, edita la parte **Audiencia de entrada** del creador de Canvas para que sólo sean elegibles para el Canvas los usuarios de prueba. También puedes introducir tu propia dirección de correo electrónico como usuario de prueba añadiendo el filtro de prueba **Dirección de correo electrónico**. En el ejemplo siguiente, hemos limitado el Canvas a dos usuarios de prueba que han utilizado la aplicación por primera vez hace menos de tres días.

\![Un Canvas con una audiencia de entrada de "Utilizó por primera vez estas aplicaciones hace menos de 3 días" y las direcciones de correo electrónico de dos usuarios de prueba.]({% image_buster /assets/img_archive/canvas_test2.png %}){: style="max-width:90%;"}

- **Método 2:** [Obtén una vista previa de tus rutas de usuario]({{site.baseurl}}/preview_user_paths/) seleccionando el botón **Probar Canvas** en el pie de página del constructor de Canvas.

## Paso 4: Inicia tu prueba

Lanza tu Canvas de prueba para que los usuarios puedan empezar a entrar. Completa los comportamientos de usuario en tu aplicación que enviarían a los usuarios a través del recorrido Canvas correspondiente.

Comprueba que tus usuarios de prueba reciben los mensajes previstos de tus pasos en Canvas. Ten en cuenta que es posible que tus usuarios de prueba no reciban ningún mensaje por motivos no limitados a:

- No elegible para el grupo de control global
- Limitaciones de frecuencia
- Pertenencia a un segmento no coincidente
- Mensajes cancelados
- Tokens de notificaciones push asociados a diferentes usuarios

Continúa iterando las pruebas de Canvas para asegurarte de que tu Canvas rinde según lo previsto.

## Consejos generales

### Identifica tus pasos en Canvas

En algunos casos, un usuario puede recibir varios mensajes al pasar por un Canvas. Si el retardo entre pasos se ha reducido significativamente para las pruebas, puede que no siempre esté claro qué mensaje se está desencadenando durante las pruebas. Si te aseguras de que los mensajes de prueba incluyen el nombre del paso o el ID del usuario (utilizando Liquid), será más fácil identificar y confirmar si se ha enviado el mensaje correcto a los usuarios correctos.

### Crear un grupo interno

En lugar de crear usuarios de prueba individuales, puedes crear un [grupo de prueba de contenido]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/), que es un grupo interno cuya finalidad es revisar el contenido de tu mensaje. Incluye un grupo de usuarios que recibirán mensajes de prueba de campañas y Lienzos. A continuación, puedes añadir este grupo de prueba en el campo **Añadir grupos de prueba de contenido**, dentro de **Destinatarios de prueba**.

### Reduce los retrasos

Para que las pruebas sean más eficaces, te sugerimos que reduzcas el tiempo de retardo a minutos o segundos para las pruebas, de modo que puedas ver los mensajes en el momento oportuno. Por ejemplo, deja al menos 2-3 minutos entre pruebas para poder aislar acciones específicas a trayectos específicos de Canvas.

### Aprovecha los bloques de contenido

Si algún contenido se va a repetir en tu marco de pruebas (por ejemplo, Liquid complejo para filtrar usuarios en diferentes pasos en Canvas), prueba a guardar este contenido repetido como un [Bloque de Contenido]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks). Ahora, podrás incluir el Bloque de contenido en cada uno de los pasos en Canvas.

### Utiliza Postman y el punto final Seguimiento de usuarios

Puedes realizar pruebas con Postman y la [Colección Postman de Braze]({{site.baseurl}}/api/postman_collection/). Utiliza el [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para registrar y seguir los eventos personalizados y las compras de tus distintos usuarios de prueba.

Ten en cuenta que el envío de datos a la API de seguimiento de usuarios sólo puede hacerse con un ID externo. Por tanto, es posible que los usuarios de prueba deban añadirse como usuarios de prueba dentro de un grupo interno en el panel de Braze para que puedan investigarse más a fondo los errores específicos. 

#### Pruebas para múltiples ramas

Cuando pruebes un Canvas con varias ramas que se dirigen a los usuarios en función de distintos atributos y eventos, sigue este plan de pruebas:

1. Para cada rama, identifica los atributos y eventos que debe tener el usuario para ser incluido en el recorrido Canvas.
2. Constrúyelos en una carga útil JSON que se publicará utilizando el punto final `/users/track`.

