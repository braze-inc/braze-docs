---
nav_title: Crear páginas de destino
article_title: Crear páginas de destino
description: "Este artículo explica cómo crear y personalizar páginas de destino Braze con el editor de arrastrar y soltar."
page_order: 0
---

# Crear páginas de destino

> Aprende a crear y personalizar una página de destino utilizando el editor de arrastrar y soltar, para que puedas hacer crecer tu audiencia y recopilar preferencias directamente en Braze.

## Crear una página de destino

### Paso 1: Crear un nuevo borrador

Ve a **Mensajería** > **Páginas de destino** y, a continuación, selecciona **Crear página de destino**. También puedes hacer clic en el nombre de una página de destino existente para duplicarla o modificarla.

![La sección de páginas de destino en el panel de Braze.]({% image_buster /assets/img/landing_pages/landing-pages-homepage.png %})

### Paso 2: Introduce los datos de la página

#### Información general

El nombre y la descripción de la página de destino se utilizan para buscar la página en su espacio de trabajo interno. No serán visibles para sus clientes.

#### Detalles del sitio

Configure metaetiquetas para personalizar la apariencia de su página en la pestaña del navegador y optimizarla para los resultados de los motores de búsqueda. Serán visibles para sus clientes.

Te sugerimos que sigas estas buenas prácticas:

| Detalle | Descripción | Recomendaciones |
| --- | --- |
| Título del sitio | El título que aparece en la pestaña del navegador. | Utilice hasta 60 caracteres. |
| Metadescripción | Fragmento de texto que aparece en los resultados de búsqueda. | Utilice entre 140 y 160 caracteres.|
| Favicon | El icono que aparece junto al título del sitio en la pestaña del navegador. | Utilice una relación de aspecto de 1:1 y un tipo de archivo compatible PNG, JPEG o ICO. |
| URL de la página | Esta es la ruta URL a tu página de destino. También se hace referencia a este valor cuando utilizas [etiquetas Liquid de página de destino]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/tracking_users) que puedes incrustar en un mensaje para identificar automáticamente cuando envían tu formulario.| Este valor debe ser único en todo tu espacio de trabajo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Paso 3: Personaliza la página

Si aún no lo has hecho, selecciona **Guardar como borrador**. Para empezar a personalizar tu página, selecciona **Editar página de destino**. El editor de arrastrar y soltar se precargará con una plantilla predeterminada que puedes personalizar para adaptarla a tu caso de uso.

![Un ejemplo de página de destino creada en el editor de arrastrar y soltar.]({% image_buster /assets/img/landing_pages/template.png %})

El editor utiliza dos tipos de componentes para la composición de la página de destino: [bloques básicos](#basic-blocks) y [bloques de formulario](#form-blocks). Todos los bloques deben colocarse en fila.

![La sección "Construir" que contiene "Filas" y "Bloques de formulario".]({% image_buster /assets/img/landing_pages/dnd.png %}){: style="max-width:35%;"}

#### Bloques básicos

Puedes utilizar estos bloques para añadir contenido y personalizar el diseño de tu página de destino.

| Tipo de bloque   | Descripción |
|-------------|-------------|
| Título       | Un bloque de texto para añadir un encabezamiento o título a tu contenido. Útil para estructurar secciones y mejorar la legibilidad. |
| Párrafo   | Un bloque de texto para descripciones más largas o contexto adicional. Admite formato de texto enriquecido. |
| Botón      | Elemento en el que se puede hacer clic y que dirige a los usuarios a una acción específica, como abrir un enlace o enviar un formulario. |
| Imagen       | Un bloque para mostrar imágenes. Puedes subir una imagen o proporcionar una URL para hacer referencia a una fuente externa. |
| Enlace        | Un hipervínculo en el que los usuarios pueden hacer clic para navegar a una URL especificada. Puede incrustarse dentro de un texto o ser independiente. |
| Espaciador      | Un bloque invisible que añade espacio vertical entre los elementos para mejorar el diseño y la legibilidad. |
| Código personalizado | Un bloque que te permite insertar y ejecutar HTML, CSS o JavaScript personalizados para una personalización avanzada. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Bloques de forma

Puedes utilizar estos bloques para crear un formulario que vincule los datos enviados por el usuario con su perfil en Braze. Ten en cuenta que, si utilizas bloques de formulario, también tendrás que crear una página de destino adicional para el estado de confirmación.

![Un bloque de formulario que registra a un nuevo cliente y le enviará un código de descuento a su correo electrónico.]({% image_buster /assets/img/landing_pages/form.png %}){: style="max-width:70%;"}

| Tipo de bloque     | Descripción |
|---------------|-------------|
| Captura de correo electrónico | Un campo de formulario para direcciones de correo electrónico. Cuando se envía, la dirección de correo electrónico se añade al perfil de ese usuario en Braze. |
| Captura telefónica | Un campo de formulario para números de teléfono. Cuando se envía, el usuario queda suscrito a tu grupo de suscripción de SMS o Whatsapp. |
| Campo de entrada de datos   | Un campo de formulario que admite atributos estándar (como nombre y apellidos) o una cadena de atributos personalizada de tu elección. |
| Desplegable      | Los usuarios pueden seleccionar un elemento de una lista predefinida. Puedes añadir a la lista cualquier cadena de atributos personalizada. |
| Casilla de verificación      | Si un usuario marca la casilla, el atributo del bloque se establece en `true`. Si se deja sin marcar, su atributo se establece en `false`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Después de crear una página de destino con un formulario, asegúrate de incrustar su [etiqueta de Liquid de página de destino]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/tracking_users) en tu mensaje. Con esta etiqueta, Braze puede identificar y actualizar automáticamente los perfiles de usuario existentes cuando envían el formulario.
{% endalert %}

#### Estilos de contenedor de página

En la pestaña **Contenedor de página** puede definir los estilos que se aplicarán a todos los bloques de componentes relevantes de su página de destino. Estos estilos se utilizarán en todas las partes de su página excepto cuando los anule con un bloque específico.

Se recomienda configurar los estilos a nivel de contenedor de página antes de personalizar los estilos a nivel de bloque. También puede añadir una imagen de fondo para toda la página.

![La sección "Contenedor de página" con opciones para personalizar las imágenes de fondo, los colores, los detalles de los bordes y el estilo del contenido.]({% image_buster /assets/img/landing_pages/page_container.png %}){: style="max-width:30%;"}

### Paso 4: Crear una página de confirmación

Si has añadido un [formulario](#form-block) a tu página de destino en el paso anterior, crea una página de destino adicional para el estado de confirmación y, a continuación, añade el enlace **Abrir URL web** al botón que envía el formulario. De lo contrario, continúa con el siguiente paso.

### Paso 5: Vista previa de la página

Puedes previsualizar tu página de destino en la pestaña **Vista previa** del editor. Después de guardar su página de destino como borrador, puede visitar la URL yendo a **Páginas de destino** y seleccionando **Copiar URL** junto a su página de destino. También puedes compartir la URL con colaboradores.

![Una página de destino con el menú abierto para mostrar la opción "Copiar URL".]({% image_buster /assets/img/landing_pages/copy-url.png %})

Cuando estés listo, selecciona **Publicar página de destino**.

## Gestión de errores de envío de formularios

Si un usuario introduce un valor de formulario no válido (como caracteres especiales no aceptados), verá un indicador de error genérico que no es personalizable y no podrá enviar el formulario. Puedes ver el comportamiento del error en la vista previa de la página de destino.

## Ver análisis

Para analizar la eficacia de tu página de destino, ve a **Mensajería** > **Páginas de destino** y, a continuación, selecciona una página de destino que hayas publicado. Aquí puedes hacer un seguimiento del número de visitas, clics y tasas de envío de tu página de destino.

![La sección de análisis de una página de destino.]({% image_buster /assets/img/landing_pages/analytics.png %})
