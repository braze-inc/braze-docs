---
nav_title: Editor de arrastrar y soltar
article_title: Creación de páginas de destino de arrastrar y soltar
description: "Este artículo explica cómo crear y personalizar páginas de destino Braze con el editor de arrastrar y soltar."
page_order: 0
alias: /landing_pages/drag_and_drop/
---

# Páginas de destino de arrastrar y soltar

> Con el editor de arrastrar y soltar, puede crear y personalizar una página de destino para aumentar su audiencia y recopilar preferencias directamente en Braze.

{% alert important %}
Las páginas de aterrizaje están actualmente en acceso temprano. Hay un límite de cinco páginas de destino por empresa. Las sesiones de usuario final registradas en las páginas de destino cuentan para el cálculo de tus Usuarios Activos Mensuales (MAU).
{% endalert %}

## Crear una página de destino (arrastrar y soltar)

### Paso 1: Crear una página de destino

Vaya a **Mensajería** > **Páginas de inicio** y seleccione **Crear página de inicio**, o seleccione el nombre de una existente para duplicarla o realizar cambios en ella.

![La página de inicio de "Páginas de destino".][2]{: style="max-width:90%;"}

### Paso 2: Configure los detalles de su página de destino

#### Información general

El nombre y la descripción de la página de destino se utilizan para buscar la página en su espacio de trabajo interno. No serán visibles para sus clientes.

#### Detalles del sitio

Configure metaetiquetas para personalizar la apariencia de su página en la pestaña del navegador y optimizarla para los resultados de los motores de búsqueda. Serán visibles para sus clientes.

Te sugerimos que sigas estas buenas prácticas:

| Detalle | Descripción | Recomendaciones |
| --- | --- |
| Título del sitio | El título que aparece en la pestaña del navegador. | Utilice hasta 60 caracteres. |
| Descripción del sitio | Fragmento de texto que aparece en los resultados de búsqueda. | Utilice entre 140 y 160 caracteres.|
| Favicon | El icono que aparece junto al título del sitio en la pestaña del navegador. | Utilice una relación de aspecto de 1:1 y un tipo de archivo compatible PNG, JPEG o ICO. |
| Tratamiento de URL | Este es el enlace en el que los usuarios harán clic para navegar a su página de destino. | Esto debe ser único. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Paso 3: Personalice su página de destino

Seleccione **Launch Editor** para empezar a diseñar su página de destino en el editor de arrastrar y soltar. El editor se cargará previamente con una plantilla predeterminada que puede personalizar para adaptarla a su caso de uso.

![Plantilla de página de inicio con un formulario para el registro de clientes.][8]{: style="max-width:90%;"}

#### Bloques de arrastrar y soltar

El editor utiliza dos tipos de componentes para la composición de la página de destino: filas y bloques. Todos los bloques deben colocarse en fila.

![La sección del editor "Construir" que contiene "Filas" y "Bloques de formulario".][4]{: style="max-width:30%;"}

#### Bloque de formulario

Utiliza varios componentes de bloque de formulario para registrar atributos de perfil personalizados y estándar y eventos personalizados. El bloque de formulario de campo de entrada puede registrar atributos estándar y personalizados para tus usuarios, y los bloques de formulario de captura de teléfono y captura de correo electrónico pueden capturar campos de teléfono y correo electrónico para los envíos de formulario de tus usuarios. Las acciones de los botones pueden registrarse como atributos personalizados, eventos personalizados o ambos en el envío del formulario. 

Si incluye un bloque de formulario, debe incluir al menos un botón con el interruptor activado para **Enviar formulario cuando se hace clic en el botón**. También debe crear otra página de destino para el [estado de confirmación](#confirmation-state).

![Un bloque de formulario que registra a un nuevo cliente y le envía un código de descuento a su correo electrónico.][5]{: style="max-width:70%;"}

#### Estilos de contenedor de página

En la pestaña **Contenedor de página** puede definir los estilos que se aplicarán a todos los bloques de componentes relevantes de su página de destino. Estos estilos se utilizarán en todas las partes de su página excepto cuando los anule con un bloque específico.

Se recomienda configurar los estilos a nivel de contenedor de página antes de personalizar los estilos a nivel de bloque. También puede añadir una imagen de fondo para toda la página.

![El contenedor de la página con opciones para personalizar las imágenes de fondo, los colores, los detalles de los bordes y el estilo del contenido.][6]{: style="max-width:30%;"}

### Paso 4: Previsualice su página de destino

Puedes previsualizar tu página de destino en la pestaña **Vista previa** del editor. Después de guardar su página de destino como borrador, puede visitar la URL yendo a **Páginas de destino** y seleccionando **Copiar URL** junto a su página de destino. También puedes compartir la URL con colaboradores.

![Una página de destino con el menú abierto para mostrar la opción "Copiar URL".][7]{: style="max-width:90%;"}

Cuando estés satisfecho con la página de inicio, selecciona **Publicar página de inicio**.

{% alert important %}
El identificador de URL no puede editarse una vez publicada la página de destino.
{% endalert %}

## Crear una página de destino de confirmación {#confirmation-state}

Si incluye un [formulario](#form-block) en su página de destino, no olvide crear una página de destino de confirmación. Cree otra página de destino para el estado de confirmación y, a continuación, añada el enlace en el campo **Abrir URL web** del botón que envía el formulario.

## Enlace a tu página de inicio

Puedes incluir un enlace a la página de destino en cualquier canal copiando y pegando el enlace en un mensaje Braze o en una campaña de redes sociales.

## Gestión de errores de envío de formularios

Si un usuario introduce un valor de formulario no válido (como caracteres especiales no aceptados), verá un indicador de error genérico que no es personalizable y no podrá enviar el formulario. Puede ver el comportamiento del error en la página de inicio de la vista previa.

## Fusión de usuarios creados desde su página de destino

Cada envío de formulario en una página de destino creará un nuevo perfil de usuario anónimo en Braze. Si ya existe un usuario con la misma dirección de correo electrónico, puede fusionar el nuevo perfil de usuario con el perfil existente mediante el punto final [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merging-unidentified-user) punto final. Para conocer las distintas formas de deduplicar usuarios en Braze, consulte [Duplicar usuarios]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users).

La fusión de usuarios se gestionará automáticamente mediante una etiqueta de Liquid en el futuro. 

## Consideraciones

El tamaño del cuerpo de la página de inicio puede ser de hasta 1 MB.

## Permisos

Necesitas permisos de administrador o todos los permisos siguientes para acceder, crear y publicar páginas de destino:

- Acceder a páginas de inicio
- Crear borradores de página de inicio
- Publicar páginas de inicio

## Niveles del plan

El número de páginas de destino publicadas y dominios personalizados que puedes utilizar depende de tu tipo de plan: gratuito o de pago (incremental).

| Característica                                                                                                   | Grada libre     | Nivel de pago (incremental)     |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| Páginas de destino publicadas                                                                 | Cinco por empresa | 20 adicionales |
| Dominios personalizados          | Uno por empresa | Cinco adicionales |

## Preguntas más frecuentes

### ¿Qué ocurre cuando un usuario envía sus datos en la página de destino?

Cuando un usuario envía un formulario, se crea un nuevo perfil de usuario Braze con los datos de usuario enviados.

### ¿Existen requisitos técnicos para publicar una página de aterrizaje?

No, no hay requisitos técnicos.

### ¿Existe un editor HTML para las páginas de destino?

Puedes editar el HTML de una página de destino utilizando el bloque Código personalizado.

### ¿Hay informes disponibles para las páginas de destino?

No, actualmente no está disponible.

### ¿Puedo crear un webhook dentro de una página de destino?

No, actualmente no es compatible.

### ¿Qué características están en la hoja de ruta de las páginas de destino? {#roadmap}

Tenemos previsto lanzar características adicionales para las páginas de destino, que están en desarrollo. Estos pueden incluir:

* Nueva etiqueta de Liquid para enlazar una página de destino en un canal de mensajería Braze
* Fusión automática de usuarios cuando se envía una página de destino a través de un canal Braze
* Página de informes básicos
* Bloques de formulario arrastrar y soltar para casillas de verificación y desplegables
* Evento estándar de seguimiento y reorientación basado en el envío de formularios

Aunque estas características forman parte de nuestra hoja de ruta, todavía están en desarrollo, y Braze no puede garantizar que alguna o todas estas características estén disponibles de forma general. El acceso a algunas o a todas las características previstas para las páginas de destino puede estar sujeto a tarifas adicionales.

[1]: {% image_buster /assets/img/landing_pages/homepage.gif %}
[2]: {% image_buster /assets/img/landing_pages/create.png %}
[3]: {% image_buster /assets/img/landing_pages/details.png %}
[4]: {% image_buster /assets/img/landing_pages/dnd.png %}
[5]: {% image_buster /assets/img/landing_pages/form.png %}
[6]: {% image_buster /assets/img/landing_pages/page_container.png %}
[7]: {% image_buster /assets/img/landing_pages/url_handle.png %}
[8]: {% image_buster /assets/img/landing_pages/template.png %}
