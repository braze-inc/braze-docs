---
nav_title: Incorporación
article_title: Incorporación
page_order: 5
page_type: reference
description: "Este artículo describe cómo utilizar una plantilla de Braze Canvas para crear recorridos de incorporación que promuevan una fuerte adopción inicial y fomenten relaciones duraderas con tus usuarios."
tool: Canvas
---

# Incorporación

> Inicia el viaje de tus usuarios con esta plantilla de incorporación. Esta plantilla está diseñada para promover una fuerte adopción inicial y fomentar relaciones duraderas con tus usuarios. Aprovechando la comunicación personalizada y un conjunto estructurado de mensajes, puedes presentar fácilmente tu marca a tus usuarios e iniciar el comienzo de una relación duradera.

En este artículo, te guiaremos a través de un caso de uso de la plantilla de **Incorporación**, que está pensada para la fase de consideración del ciclo de vida del usuario, para crear un viaje de incorporación sin problemas para los nuevos usuarios. Después de este artículo, habrás personalizado esta plantilla de Braze Canvas con mensajes personalizados para estos nuevos usuarios.

## Requisitos previos

Antes de utilizar esta plantilla, necesitas crear las siguientes [plantillas de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template) para hacer referencia a ellas en el Canvas:

- Un correo electrónico de bienvenida a todos los usuarios de tu aplicación
- Un correo electrónico con consejos sobre cómo utilizar tu aplicación
- Un correo electrónico de respuesta que incluye un cuestionario para el usuario

## Adaptar la plantilla a tus necesidades

Digamos que trabajamos en PantsLabyrinth, y nuestro objetivo es mejorar la interacción con el usuario, generar confianza y fidelización con nuestros usuarios, y animarles a seguir comprometidos. Para ello, queremos centrarnos en elaborar mensajes dirigidos a los nuevos usuarios que aún no han interactuado con la aplicación.

Para acceder a la plantilla de incorporación, al crear un nuevo Canvas, selecciona **Utilizar una plantilla Canvas** > **Plantillas Braze**. Después, junto a **Incorporación**, selecciona **Aplicar plantilla**. Empecemos a personalizar esta plantilla para adaptarla a nuestro caso de uso.

### Paso 1: Configura los detalles

Vamos a ajustar los detalles del Canvas para reflejar nuestro objetivo.

1. Selecciona **Editar** junto al nombre de la plantilla.

\![El título actual y la descripción del Canvas.]({% image_buster /assets/img/canvas_templates/onboarding_old_name_description.png %}){: style="max-width:60%;"}

{:start="2"}
2\. Actualiza el nombre del Canvas para especificar que es para la incorporación de nuevos usuarios.
3\. Actualiza la descripción para especificar que el Canvas mapea un recorrido del usuario que fomenta la confianza y la fidelización de los usuarios.
4\. Añade la etiqueta **Incorporación** para que podamos filtrarla en la página de inicio de Canvas.

\![El nuevo nombre, descripción y etiqueta del Canvas.]({% image_buster /assets/img/canvas_templates/onboarding_new_name_description.png %}){: style="max-width:60%;"}

### Paso 2: Asigna tus eventos de conversión

A continuación, vamos a asignar nuestros eventos de conversión. Los eventos de conversión son un tipo de métrica que puede utilizarse para medir el éxito del Canvas. En **Nombre de evento personalizado**, selecciona **Enviar clic** como evento personalizado.

\![Evento de conversión primaria - A con el tipo de conversión "Realiza evento personalizado" con el nombre de evento personalizado "Clic de correo electrónico". Hay un plazo de conversión de 4 días.]({% image_buster /assets/img/canvas_templates/onboarding1.png %})

Esto significa que los nuevos usuarios tienen hasta cuatro días para hacer clic en el correo electrónico de bienvenida. En este caso, queremos que nuestros nuevos usuarios sientan la urgencia de interactuar con PantsLabyrinth y suscribirse a una entrega recurrente de ropa de temporada.

### Paso 3: Establecer un horario de entrada

Como el objetivo es captar nuevos usuarios de PantsLabyrinth, mantendremos el Canvas basado en acciones. En **Iniciar sesión**, selecciona **Iniciar sesión en cualquier aplicación** para que los usuarios que inicien una sesión en cualquier aplicación puedan entrar en el Canvas.

A continuación, ajusta la **Ventana de entrada** para determinar cuándo pueden entrar los usuarios en el Canvas. Supongamos que a finales de octubre se lanza una suscripción a PantsLabyrinth. Aquí es donde estableceremos la hora de inicio como **2024/10/28 8:00 h**. Opcionalmente, también podemos dejar que los usuarios introduzcan el Canvas en su zona horaria local.

Una ventana de entrada con hora de inicio el 28 de octubre de 2024 a las 8 de la mañana. Los usuarios introducirán este mensaje en su zona horaria local.]({% image_buster /assets/img/canvas_templates/onboarding4.png %})

### Paso 4: Dirígete a tu audiencia

Al dirigirnos a la audiencia adecuada, podemos interactuar eficazmente con nuevos usuarios. Por ejemplo, esta plantilla se dirige a todos los usuarios que utilizaron por primera vez una aplicación hace menos de un día, lo que es correcto para nuestro caso de uso. Así que dejaremos esta sección como está.

### Paso 5: Establecer configuración de envío

Por defecto, este Canvas se envía a los usuarios suscritos o con adhesión voluntaria y sigue las normas de limitación de frecuencia. Mantendremos esta configuración tal como está.

### Paso 6: Personaliza tu Canvas

Ahora, vamos a construir el Canvas personalizando los pasos de la plantilla.

#### Configurar el correo electrónico de bienvenida

1. Selecciona el paso Mensaje llamado "Correo electrónico de bienvenida".
2. Selecciona **Editar mensaje** para sustituir el correo electrónico de la plantilla por nuestro correo de bienvenida.
3. Selecciona **Hecho**.

Ahora, nuestros usuarios recibirán este correo electrónico de bienvenida después de haber iniciado una sesión en nuestra aplicación. Para no abrumar a los usuarios con mensajes repetidos, recomendamos utilizar el paso Retraso como parte del recorrido del usuario.

#### Personaliza la ruta de audiencia

En el paso Ruta de audiencia, llamado **División de la audiencia**, podemos personalizar el filtro para nuestros usuarios comprometidos. En la plantilla, el filtro es **Ha hecho clic en el correo electrónico para el paso Correo electrónico de** bienvenida, lo que significa que los usuarios se dividen en dos grupos: los usuarios que han hecho clic en el correo electrónico de bienvenida y los que no.

Un paso de división de la audiencia con una ruta para los usuarios comprometidos y otra para todos los demás.]({% image_buster /assets/img/canvas_templates/onboarding2.png %}){: style="max-width:70%;"}

Como comercio minorista de ropa online, PantsLabyrinth también tiene un grupo activo de usuarios móviles. Así, en un Canvas de incorporación separado, también podemos seleccionar el siguiente filtro para identificar y dividir a nuestros usuarios móviles en estos segmentos:

- **Ha hecho clic en la tarjeta de contenido para el paso Bienvenido Tarjeta de contenido**
- **Todos los demás**

#### Dirígete a más usuarios con las Rutas de audiencia

A partir del conjunto de usuarios que no han interactuado con nuestra aplicación, podemos dirigirnos aún más a estos usuarios editando el paso "Comprobar clics" y el paso "Winback Nudge".

### Paso 7: Prueba y lanza tu Canvas

Después de probar y revisar nuestro Canvas para asegurarnos de que funciona como esperábamos, selecciona **Lanzar Canvas** para iniciar el Canvas. Ahora podemos ofrecer a nuestros nuevos usuarios una experiencia de incorporación personalizada para fomentar una relación duradera.

{% alert tip %}
Consulta nuestra [Lista de comprobación previa y posterior al lanzamiento]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) para saber qué cosas debes tener en cuenta antes y después de lanzar un Canvas.
{% endalert %}

