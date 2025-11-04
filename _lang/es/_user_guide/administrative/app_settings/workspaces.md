---
nav_title: Creación y gestión de espacios de trabajo
article_title: Creación y gestión de espacios de trabajo
page_order: 0
page_type: reference
description: "Este artículo explica cómo crear, configurar y administrar tus espacios de trabajo."

---

# Creación y gestión de espacios de trabajo

> Este artículo explica cómo crear, configurar y administrar tus espacios de trabajo. 

## ¿Qué es un espacio de trabajo?

Todo lo que haces en Braze ocurre dentro de un espacio de trabajo. Los espacios de trabajo son un entorno compartido en el que puedes seguir y gestionar la interacción de aplicaciones móviles o sitios web relacionados. Los espacios de trabajo agrupan aplicaciones iguales o muy similares: por ejemplo, las versiones para Android e iOS de tu aplicación móvil. 

## Crear un espacio de trabajo

### Paso 1: Ten un plan

Antes de empezar, asegúrate de haber trabajado con tu equipo y tu administrador de incorporación a Braze para determinar la mejor configuración del espacio de trabajo para tu caso de uso. Para saber más sobre cómo planificar tus espacios de trabajo en Braze, consulta nuestra página [Primeros pasos: Guía de espacios de trabajo]({{site.baseurl}}/user_guide/getting_started/workspaces/).

### Paso 2: Añade tu espacio de trabajo

Puedes crear nuevos espacios de trabajo o cambiar entre espacios de trabajo existentes desde el desplegable de espacios de trabajo de la cabecera global.

1. Selecciona el desplegable del espacio de trabajo y, a continuación, <i class="fa-solid fa-square-plus" style="color: #0b8294;"></i> **Crear espacio de trabajo**.

El desplegable del espacio de trabajo con el botón "Crear espacio de trabajo".]({% image_buster /assets/img/workspaces/workspace_create.png %}){: style="max-width:60%;"}

{:start="2"}
2\. Dale un nombre a tu espacio de trabajo.

{% alert tip %}
Tal vez quieras adoptar una convención de nombres para que otras personas de tu empresa puedan encontrar fácilmente tu espacio de trabajo. Por ejemplo: "Upon Voyage US - Producción" y "Upon Voyage US - Puesta en escena".
{% endalert %}

{:start="3"}
3\. Selecciona **Crear**. Braze puede tardar unos segundos en crear tu espacio de trabajo.

\!["Crear espacio de trabajo" modal con el nombre "Upon Voyage US - Staging".]({% image_buster /assets/img/workspaces/workspace_name.png %}){: style="max-width:60%" }

Accederás a la página **Configuración de la aplicación** para empezar a añadir instancias de la aplicación. Puedes acceder a esta página en cualquier momento desde **Configuración** > Configuración de la aplicación.

Página "Configuración de la aplicación" de Upon Voyage US - Espacio de trabajo con un botón para añadir una aplicación.]({% image_buster /assets/img/workspaces/workspace_empty_state.png %})

### Paso 3: Añade las instancias de tu aplicación

Nos referimos a los diferentes sitios y aplicaciones que se reúnen dentro de un espacio de trabajo como "instancias de la aplicación".

1. En la página **Configuración de la aplicación**, selecciona **\+ Añadir aplicación**.
2. Dale un nombre a tu instancia de la aplicación y selecciona en qué plataforma o plataformas se encuentra esta instancia de la aplicación. Si seleccionas varias plataformas, Braze creará una instancia de la aplicación para cada plataforma.

\!["Añadir nueva aplicación a Upon Voyage US - Staging" modal con opciones para seleccionar los detalles de la aplicación.]({% image_buster /assets/img/workspaces/workspace_add_app.png %}){: style="max-width:60%" }

{:start="3"}
3\. Selecciona **Añadir aplicación** para confirmar.

#### Claves de API de la aplicación

Después de añadir la instancia de tu aplicación, tendrás acceso a su clave de API. La clave de API se utiliza al realizar solicitudes entre la instancia de tu aplicación y la API de Braze. La clave de API también es importante para integrar el SDK de Braze con tu aplicación o sitio web.

Página de configuración de la aplicación Upon Voyage para iOS con campos para la clave de API y el punto final SDK.]({% image_buster /assets/img/workspaces/app_api_key.png %})

{% alert note %}
Debes crear instancias de la aplicación distintas para cada versión de tu aplicación en cada plataforma. Por ejemplo, si tienes versiones gratuita y pro de tu aplicación tanto en iOS como en Android, crea cuatro instancias de la aplicación dentro de tu espacio de trabajo (aplicación gratuita para iOS, aplicación gratuita para Android, aplicación pro para iOS y aplicación pro para Android). Esto te dará cuatro claves de API para utilizar, una para cada instancia de la aplicación.
{% endalert %}

#### Versión en vivo del SDK

La versión del SDK en vivo que se muestra en la página Configuración de la aplicación para una aplicación específica es la versión más alta de la aplicación con al menos el 5% del total de tus sesiones diarias y que tenga al menos 500 sesiones en el último día.

Este campo aparece después de haber integrado el SDK de Braze con tu aplicación o sitio web. Si hay disponible una versión más reciente del SDK de Braze para tu plataforma, se anotará aquí con la etiqueta "Versión más reciente disponible."

\!["Versión del SDK en vivo" sección con un valor de campo de "5.4.0" y un icono que dice que hay una nueva versión disponible.]({% image_buster /assets/img/workspaces/app_live_sdk_version.png %})

### Paso 4: Repite según sea necesario

Repite los pasos 2 y 3 para configurar tantos espacios de trabajo como requiera tu plan. Como mejor práctica, te recomendamos que crees un espacio de trabajo de pruebas para las pruebas de integración y de campaña.

{% alert tip %}
**Añadir un espacio de trabajo de pruebas**<br>Puedes realizar pruebas de aplicación aislando completamente a determinados usuarios de tu instancia de producción. Crea un nuevo espacio de trabajo y, cuando publiques tu aplicación, asegúrate de cambiar la clave de API que utiliza Braze para que coincida con la de tu espacio de trabajo de producción y no con la de tu espacio de trabajo de pruebas.
{% endalert %}

## Administrador de espacios de trabajo

### Añadir favoritos

Puedes añadir espacios de trabajo favoritos para acceder aún más rápido a los espacios de trabajo que más utilizas.

\![Desplegable del espacio de trabajo con la pestaña de "Espacios de trabajo favoritos".]({% image_buster /assets/img/workspaces/workspace_favorites.png %}){: style="max-width:50%;"}

Para añadir espacios de trabajo favoritos:

1. Selecciona el menú desplegable de tu perfil y, a continuación, selecciona **Gestionar tu cuenta**.
2. En la sección **Perfil de cuenta**, localiza el campo **Espacios de trabajo favoritos**.
3. Selecciona tus espacios de trabajo de la lista.
4. Selecciona **Guardar cambios**.

No hay límite en el número de espacios de trabajo que puedes elegir como favoritos, pero te recomendamos que mantengas esta lista corta por comodidad.

### Renombrar espacios de trabajo

Para cambiar el nombre de tu espacio de trabajo:

1. Ve a **Configuración** > Configuración de la aplicación.
2. Pasa el ratón por encima del nombre de tu espacio de trabajo y selecciona <i class="image: /assets/img/braze_icons/pencil-01.svg" style="color: #0b8294;"></i>.
3. Dale un nuevo nombre a tu espacio de trabajo y selecciona <i class="fa-solid fa-square-check" style="color: #0b8294;"></i> **Guardar**.

\![El icono del lápiz que aparece junto al nombre del espacio de trabajo.]({% image_buster /assets/img/workspaces/workspace_rename.gif %}){: style="max-width:50%;"}

### Eliminar espacios de trabajo e instancias de la aplicación

Para eliminar tu espacio de trabajo o instancia de la aplicación:

1. Ve a **Configuración** > Configuración de la aplicación.
2. Selecciona **Eliminar espacio de trabajo** para eliminar el espacio de trabajo correspondiente, o selecciona el icono de la papelera situado junto a la instancia de la aplicación correspondiente.

No puedes eliminar instancias de la aplicación o espacios de trabajo que se estén utilizando actualmente para seleccionar usuarios o que tengan más de 1.000 usuarios. Si intentas hacerlo, recibirás un mensaje de error. Para proceder a eliminarlos, [crea un caso de Soporte]({{site.baseurl}}/user_guide/administrative/access_braze/support/) que incluya un enlace al panel y el nombre de la instancia de la aplicación o del espacio de trabajo que se va a eliminar.

{% alert warning %}
¡Ten cuidado al borrar espacios de trabajo! Después de borrar un espacio de trabajo, no se puede restaurar.
{% endalert %}

Página de configuración de la aplicación con un botón para eliminar un espacio de trabajo y un icono de papelera para eliminar una aplicación.]({% image_buster /assets/img/workspaces/workspace_delete.png %})

## Preguntas más frecuentes

### ¿Debo crear un nuevo espacio de trabajo cuando publique una aplicación actualizada?

Esto depende de si estás actualizando tu aplicación o creando una completamente nueva.

#### Actualizar tu aplicación

Si vas a actualizar tu aplicación, debes separar las versiones antigua y nueva creando una nueva instancia de la aplicación dentro del mismo espacio de trabajo. De este modo, puedes dirigirte eficazmente a los usuarios de la nueva versión cuando selecciones esa aplicación durante la segmentación. Si quieres enviar mensajes a usuarios que están en la versión antigua, puedes utilizar filtros para [dirigirte a la versión anterior de la aplicación]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features#filtering-by-most-recent-app-versions).

Si creas un nuevo espacio de trabajo, tus usuarios existirán en dos lugares: el antiguo espacio de trabajo y el nuevo espacio de trabajo. También podrían tener el mismo token de notificaciones push. Esto puede hacer que los usuarios reciban un mensaje de marketing destinado sólo a los antiguos usuarios del espacio de trabajo, aunque ya se hayan actualizado.

#### Lanzamiento de una nueva aplicación

Si vas a lanzar una aplicación completamente nueva a la tienda de aplicaciones, debes crear un nuevo espacio de trabajo. Al crear un nuevo espacio de trabajo, todos los datos históricos y perfiles de usuario de la versión anterior de la aplicación no existirán en este nuevo espacio de trabajo. Así, después de que los usuarios existentes se actualicen a la nueva versión de la aplicación, tendrán un nuevo perfil creado sin ninguno de los datos de comportamiento de la antigua aplicación.

### Tengo varias instancias de la aplicación en un espacio de trabajo, ¿cómo puedo asegurarme de que mi mensaje se dirige a una sola aplicación? {#singular-app}

Para asegurarte de que tu mensaje sólo se dirige a una aplicación concreta, añade un segmento que sólo se dirija a los usuarios de las instancias de la aplicación que hayas elegido. Esto es especialmente importante si un usuario puede tener dos tokens de notificaciones push para diferentes instancias de la aplicación en el mismo espacio de trabajo. En este caso, los usuarios podrían recibir una notificación de una aplicación distinta de aquella en la que están. No es una experiencia ideal.

Por defecto, un segmento se dirige a todas las aplicaciones y sitios web del espacio de trabajo. Para configurar un segmento que sólo se dirija a una aplicación o sitio web:

1. Crea un segmento con un nombre significativo. En Braze, utilizamos el formato "Todos los usuarios ({Nombre} {Plataforma})". Por ejemplo, "Todos los usuarios (Upon Voyage iOS)".
2. Para **aplicaciones y sitios web específicos**, selecciona **Usuarios de aplicaciones específicas**.
3. En el desplegable **Aplicaciones específicas**, selecciona tu aplicación o sitio.

Segmento dirigido a usuarios de aplicaciones específicas.]({% image_buster /assets/img/workspaces/users_from_specific_apps_filter.png %})

A continuación, puedes añadir este segmento a tu mensaje y empezar a refinar aún más tu audiencia con segmentos y filtros adicionales, si es necesario.

#### Campañas

Para las campañas, añade tu segmento al paso **Audiencias objetivo** del compositor.

#### Canvas

En Canvas, añade tu segmento a los pasos de tu Mensaje, en la sección **Validaciones de entrega**. Las validaciones de entrega comprueban dos veces que tu audiencia cumple tus criterios de entrega en el envío del mensaje. Recuerda especificar validaciones de entrega para cada paso de Mensaje para asegurarte de que se entregará a la aplicación correcta. No es necesario segmentar en el nivel de entrada.

{% details Expand for steps in the original Canvas workflow %}

En el flujo de trabajo original de Canvas, añade tu segmento al nivel del componente Canvas en la sección **Audiencia**. No es necesario segmentar en el nivel de entrada.

{% enddetails %}


