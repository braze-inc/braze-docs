1. Ve a **Plantillas** > **Bloques de contenido**. Haz clic en <i class="fas fa-plus"></i> **Crear bloque de contenido** y selecciona **Arrastrar y soltar bloque de contenido**.

{% if include.location == "dnd" %}

{:start="2"}
2\. Arrastra y suelta los [bloques de editor]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/) para construir un bloque de contenido de arrastrar y soltar.
3\. Arrastra y suelta un bloque de formato de la pestaña **Filas** en el editor para crear el diseño de tu Bloque de contenido. <br><br> ![]({% image_buster /assets/img_archive/dnd_content_block_composer.png %})<br><br>
4\. Añade bloques de contenido arrastrando y soltando según necesites para crear tus campañas de correo electrónico.
5\. Después de crear tu bloque de contenido, haz clic en **Listo**.
6\. Dale un nombre a tu bloque de contenido. Este nombre se rellenará automáticamente como parte de la **etiqueta de Liquid del bloque de contenido**.
7\. (opcional) Añade una descripción.
8\. Haz clic en **Iniciar bloque de contenido**.

{% elsif include.location == "html" %}

{:start="2"}
2\. Introduce tu HTML en la pestaña **HTML**, o construye tu bloque de contenido en la pestaña **Clásico**. <br><br> ![]({% image_buster /assets/img_archive/html_content_block_composer.png %})<br><br>
4\. Después de crear tu bloque de contenido, haz clic en **Listo**.
5\. Introduce un nombre para tu bloque de contenido. Este nombre se rellenará automáticamente como parte de la **etiqueta de Liquid del bloque de contenido**.
6\. (opcional) Añade una descripción.
7\. Haz clic en **Iniciar bloque de contenido**.

{% endif %}