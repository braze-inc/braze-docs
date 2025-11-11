---
nav_title: Crear páginas de destino
article_title: Crear páginas de destino
description: "Este artículo explica cómo crear y personalizar páginas de destino Braze con el editor de arrastrar y soltar."
page_order: 0
---

# Crear páginas de destino

> Aprende a crear y personalizar una página de destino utilizando el editor de arrastrar y soltar, para que puedas hacer crecer tu audiencia y recopilar preferencias directamente en Braze.

## Requisitos previos

Para acceder al constructor de páginas de destino, necesitas [ciertos permisos]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/#prerequisites). Si no tienes acceso, pide ayuda a tu administrador de Braze.

## Crear una página de destino

### Paso 1: Crear un nuevo borrador

Ve a **Mensajería** > **Páginas de destino** y, a continuación, selecciona **Crear página de destino**. También puedes seleccionar el nombre de una página de destino existente para duplicarla o realizar cambios en ella.

La sección de páginas de destino en el panel de Braze.]({% image_buster /assets/img/landing_pages/landing-pages-homepage.png %})

### Paso 2: Introduce los datos de la página

Añade detalles internos y públicos que te ayuden a organizar, marcar y compartir tu página de destino.

#### Datos generales

Introduce un nombre y una descripción para la página de destino. Estos datos se utilizan para buscar la página en tu espacio de trabajo interno. No serán visibles para tus clientes.

#### Detalles del sitio

Configura las metaetiquetas para personalizar cómo aparece tu página en la pestaña del navegador y optimizarla para los resultados de los motores de búsqueda. Serán visibles para tus clientes.

Te sugerimos que sigas estas buenas prácticas:

| Campo | Descripción | Recomendaciones |
| --- | --- |
| Título del sitio | El título que aparece en la pestaña del navegador. | Utiliza hasta 60 caracteres. |
| Meta descripción | Un fragmento de código que se muestra en los resultados de búsqueda. | Utiliza entre 140 y 160 caracteres.|
| Favicon | El icono que aparece junto al título del sitio en la pestaña del navegador. | Utiliza una relación de aspecto de 1:1 y un tipo de archivo compatible PNG, JPEG o ICO. |
| URL de la página | Esta es la ruta URL a tu página de destino. También se hace referencia a este valor cuando utilizas [etiquetas Liquid de página de destino]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/tracking_users) que puedes incrustar en un mensaje para identificar automáticamente cuando envían tu formulario.| Este valor debe ser único en todo tu espacio de trabajo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Paso 3: Personaliza la página

Si aún no lo has hecho, selecciona **Guardar como borrador**. Para empezar a personalizar tu página, selecciona **Editar página de destino**. El editor de arrastrar y soltar se precargará con una plantilla predeterminada que puedes personalizar para adaptarla a tu caso de uso.

Un ejemplo de página de destino creada en el editor de arrastrar y soltar.]({% image_buster /assets/img/landing_pages/template.png %})

El editor utiliza dos tipos de componentes para la composición de la página de destino: bloques básicos y bloques de formulario. Todos los bloques deben colocarse en fila.

La sección "Construir" contiene "Filas" y "Bloques de formulario".]({% image_buster /assets/img/landing_pages/dnd.png %}){: style="max-width:35%;"}

{% tabs %}
{% tab Basic blocks %}

Puedes utilizar estos bloques para añadir contenido y personalizar el diseño de tu página de destino.

| Tipo de bloque   | Descripción |
|-------------|-------------|
| Título       | Un bloque de texto para añadir un encabezamiento o título a tu contenido. Útil para estructurar secciones y mejorar la legibilidad. |
| Párrafo   | Un bloque de texto para descripciones más largas o contexto adicional. Admite formato de texto enriquecido. |
| Botón      | Elemento en el que se puede hacer clic y que dirige a los usuarios a una acción específica, como abrir un enlace o enviar un formulario. |
| Botón de radio | Añade una lista de opciones de las que los usuarios pueden seleccionar una. Cuando se envía, el perfil de usuario registra el atributo personalizado asociado. |
| Imagen       | Un bloque para mostrar imágenes. Puedes subir una imagen o proporcionar una URL para hacer referencia a una fuente externa. |
| Enlace        | Un hipervínculo en el que los usuarios pueden hacer clic para navegar a una URL especificada. Puede incrustarse dentro de un texto o ser independiente. |
| Espaciador      | Un bloque invisible que añade espaciado vertical entre elementos para mejorar el diseño y la legibilidad. |
| Código personalizado | Un bloque que te permite insertar y ejecutar HTML, CSS o JavaScript personalizados para una personalización avanzada. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

##### Extender texto

{% multi_lang_include span_text.md %}

{% endtab %}
{% tab Form blocks %}

Puedes utilizar estos bloques para crear un formulario que vincule los datos enviados por el usuario con su perfil en Braze. Ten en cuenta que, si utilizas bloques de formulario, también tendrás que crear una página de destino adicional para el estado de confirmación.

Bloque de formulario que registra a un nuevo cliente y le envía un código de descuento a su correo electrónico.]({% image_buster /assets/img/landing_pages/form.png %}){: style="max-width:70%;"}

| Tipo de bloque     | Descripción |
|---------------|-------------|
| Captura de correo electrónico | Un campo de formulario para direcciones de correo electrónico. Cuando se envía, la dirección de correo electrónico se añade al perfil de ese usuario en Braze. |
| Captura telefónica | Un campo de formulario para números de teléfono. Cuando se envía, el usuario queda suscrito a tu grupo de suscripción de SMS o WhatsApp. |
| Campo de entrada   | Un campo de formulario que admite atributos estándar (como nombre y apellidos) o una cadena de atributos personalizada de tu elección. |
| Desplegable      | Los usuarios pueden seleccionar un elemento de una lista predefinida. Puedes añadir a la lista cualquier cadena de atributos personalizada. |
| Casilla de verificación      | Si un usuario marca la casilla, el atributo del bloque se establece en `true`. Si se deja sin marcar, su atributo se establece en `false`. |
| Grupo de casillas de verificación| Los usuarios pueden elegir entre las múltiples opciones presentadas. Los valores se establecen o se añaden a un atributo personalizado de matriz definida. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Después de crear una página de destino con un formulario, asegúrate de incrustar su [etiqueta de Liquid de página de destino]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/tracking_users) en tu mensaje. Con esta etiqueta, Braze puede identificar y actualizar automáticamente los perfiles de usuario existentes cuando envían el formulario.
{% endalert %}

{% endtab %}
{% endtabs %}

#### Estilos de contenedor de página

Puedes configurar los estilos que se aplicarán a todos los bloques de componentes relevantes de tu página de destino desde la pestaña **Contenedor de página**. Estos estilos se utilizarán en todas las partes de tu página, excepto cuando los anules con un bloque específico.

Te recomendamos que configures los estilos a nivel de contenedor de página antes de personalizar los estilos a nivel de bloque. También puedes añadir una imagen de fondo para toda la página.

La sección "Contenedor de página" con opciones para personalizar las imágenes de fondo, los colores, los detalles de los bordes y el estilo del contenido.]({% image_buster /assets/img/landing_pages/page_container.png %}){: style="max-width:40%;"}

#### Receptivo a los dispositivos del usuario

Puedes hacer que tu página de destino sea receptiva al tamaño del dispositivo del usuario apilando verticalmente las columnas en las pantallas más pequeñas. Para habilitarlo, añade una columna a la fila que quieras hacer receptiva y, a continuación, alterna la opción **Apilar verticalmente en pantallas pequeñas** en la sección **Personalizar columnas**.

Cuando está habilitado, también puedes invertir las columnas de apilamiento para controlar el orden vertical del contenido de varias columnas en pantallas más pequeñas. Esto hace que las páginas se vean y se sientan mejor en el móvil sin necesidad de código personalizado.

Alternar "Apilar verticalmente en pantallas pequeñas" en la sección "Personalizar columnas".]({% image_buster /assets/img/landing_pages/device_responsive_toggle.png %}){: style="max-width:50%;"}

#### Campos opcionales y obligatorios

Puedes elegir si un campo de formulario es obligatorio u opcional. Los campos obligatorios deben rellenarse antes de enviar el formulario. El usuario puede dejar en blanco o deseleccionar los campos opcionales.

Por ejemplo, para imponer la captura del consentimiento antes del envío del formulario, puedes activar la **entrada de campo Obligatorio** para establecer una casilla de verificación obligatoria con el texto de exención de responsabilidad adecuado.

Un campo de formulario de casilla de verificación con la opción "Campo de entrada obligatoria" alternada.]({% image_buster /assets/img/landing_pages/lp-optional-required.png %}){: style="max-width:50%;"}

### Paso 4: Crea una página de confirmación (opcional)

Si tu página de destino no incluye un formulario, continúa con el siguiente paso.

Si tu página de destino incluye un [formulario](#form-blocks), crea una segunda página de destino que sirva como experiencia de confirmación. Esta página debe dar las gracias a los usuarios o proporcionar un siguiente paso tras el envío del formulario.

Para enlazar la página de confirmación:
- Selecciona el botón **Enviar** de tu formulario
- Utiliza la acción **Abrir URL web** para enlazar con tu página de confirmación

Si no incluyes una página de confirmación, es posible que los usuarios no sepan que su formulario se ha enviado correctamente. Incluye siempre una experiencia de confirmación para completar el viaje.

{% alert note %}
Si tu página de confirmación se abre en una pestaña nueva, un usuario que vuelva a la página de destino original y reenvíe con información actualizada puede sobrescribir el envío anterior, lo que daría lugar a datos incoherentes.
{% endalert %}

### Paso 5: Vista previa de la página

Puedes previsualizar tu página de destino en la pestaña **Vista previa** del editor. Después de guardar tu página de destino como borrador, puedes visitar la URL yendo a **Páginas de destino** y seleccionando **Copiar URL** junto a tu página de destino. También puedes compartir la URL con colaboradores.

Una página de destino con el menú abierto para mostrar la opción "Copiar URL".]({% image_buster /assets/img/landing_pages/copy-url.png %})

Antes de publicar, asegúrate:

- No has superado el límite de páginas de destino publicadas de tu plan
- Cada página basada en un formulario enlaza con una [página de confirmación](#step-4-create-a-confirmation-page) mediante la acción **Abrir URL Web** 
- Todos los campos obligatorios de la página (como la ruta URL y el título) están completos

Cuando estés listo, selecciona **Publicar página de destino**.

## Utilizar plantillas

Utiliza plantillas de páginas de destino para crear plantillas para tus próximas campañas. Se puede acceder a estas plantillas y gestionarlas tanto en el editor de páginas **de** destino como en la sección **Plantillas** del panel**(Plantillas** > **Plantillas de páginas de destino**). Las plantillas de las páginas de destino requieren un nombre y, opcionalmente, una descripción. 

## Plantillas de administrador

Puedes previsualizar, archivar, editar o duplicar plantillas de páginas de destino. Al editar una página de destino, también puedes guardarla como plantilla, realizar cambios en la plantilla o eliminar el contenido de la página de destino. 

Un desplegable con opciones para guardar, cambiar y eliminar una página de destino.]({% image_buster /assets/img/landing_pages/manage-lp-template.png %}){: style="max-width:60%;"}

## Ver análisis

Para analizar la eficacia de tu página de destino, ve a **Mensajería** > **Páginas de destino** y, a continuación, selecciona una página de destino que hayas publicado. Aquí puedes hacer un seguimiento del número de visitas, clics y tasas de envío de tu página de destino.

La sección de análisis de una página de destino.]({% image_buster /assets/img/landing_pages/analytics.png %})

## Tratamiento de errores de envío de formularios {#handling-form-submission-errors}

Si un usuario intenta enviar un formulario al que le faltan datos o no los admite, verá un mensaje de error genérico y no podrá enviarlo.

Causas frecuentes:

- Los campos obligatorios se dejan en blanco
- Los caracteres especiales se utilizan en las entradas de texto
- No se ha seleccionado una casilla obligatoria

Los mensajes de error que se muestran a los usuarios no se pueden personalizar. Obtén una vista previa de tu página de destino para confirmar el comportamiento de los campos antes de publicarla. 
