{% if include.location == "dnd" %}

1. Ve a **Plantillas** > **Bloques de contenido**. Selecciona <i class="fas fa-plus"></i> **Crear bloque de contenido** y selecciona **Arrastrar y soltar bloque de contenido**.
2. Arrastra y suelta los [bloques de editor]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/) para construir un bloque de contenido de arrastrar y soltar. 
3. Arrastra y suelta un bloque de formato de la pestaña **Filas** en el editor para crear el diseño de tu Bloque de contenido. <br><br> ![Compositor de bloques de contenido arrastrar y soltar.]({% image_buster /assets/img_archive/dnd_content_block_composer.png %})<br><br>
4. Añade bloques de contenido arrastrando y soltando según necesites para crear tus campañas de correo electrónico.
5. Después de crear tu bloque de contenido, selecciona **Hecho**.
6. Dale un nombre a tu bloque de contenido. Este nombre se rellenará automáticamente como parte de la **etiqueta de Liquid del bloque de contenido**.
7. (Opcional) Añade una descripción.
8. Selecciona la pestaña **Vista previa** para ver cómo aparecerá tu Bloque de contenido. Opcionalmente, selecciona **Copiar enlace de vista previa** para generar y copiar un enlace de vista previa compartible que muestre el aspecto que tendrá el correo electrónico para un usuario aleatorio. El enlace durará siete días antes de que sea necesario regenerarlo.<br><br> ![Pestaña "Vista previa" para el compositor de bloques de contenido de arrastrar y soltar.]({% image_buster /assets/img_archive/dnd_content_block_preview_link.png %})<br><br>
9. Selecciona **Lanzar bloque de contenido**.

{% elsif include.location == "html" %}

1. Ve a **Plantillas** > **Bloques de contenido**. Selecciona <i class="fas fa-plus"></i> **Crear bloque de contenido** y selecciona **Bloque de contenido HTML**.
2. Introduce tu HTML en la pestaña **HTML**, o construye tu bloque de contenido en la pestaña **Clásico**. <br><br> ![Compositor de bloques de contenido HTML]({% image_buster /assets/img_archive/html_content_block_composer.png %})<br><br>
4. Después de crear tu bloque de contenido, selecciona **Hecho**.
5. Introduce un nombre para tu bloque de contenido. Este nombre se rellenará automáticamente como parte de la **etiqueta de Liquid del bloque de contenido**.
6. (Opcional) Añade una descripción.
7. Selecciona la pestaña **Vista previa** para ver cómo aparecerá tu Bloque de contenido. Opcionalmente, selecciona **Copiar enlace de vista previa** para generar y copiar un enlace de vista previa compartible que muestre el aspecto que tendrá el correo electrónico para un usuario aleatorio. El enlace durará siete días antes de que sea necesario regenerarlo.<br><br> ![Pestaña "Vista previa" del compositor del bloque de contenido HTML.]({% image_buster /assets/img_archive/content_block_html_preview_link.png %})<br><br>
8. Selecciona **Lanzar bloque de contenido**.

{% endif %}