---
nav_title: El panel de control
article_title: El panel de Braze
page_order: 5
page_type: reference
description: "El panel de Braze es tu espacio de trabajo central para crear, gestionar y analizar la interacción con los clientes. Reúne en un solo lugar herramientas de mensajería, información sobre la audiencia, segmentación y datos de rendimiento en tiempo real."

---

# El panel de Braze

> El panel de Braze es tu espacio de trabajo central para crear, gestionar y analizar la interacción con los clientes. Accede a ella en [dashboard.braze.com](https://dashboard.braze.com/) o en [dashboard.braze.eu](https://dashboard.braze.eu/).

Utiliza el panel de Braze para planificar campañas, lanzar y administrar mensajes, explorar la información de la audiencia, ajustar la segmentación y revisar el rendimiento en tiempo real y las métricas de interacción desde una única interfaz.

## Resumen del panel de control

Cuando te conectas, el panel proporciona una vista centralizada de tus herramientas de interacción y datos:

- **Página de inicio:** Muestra tus [contenidos editados recientemente](#pick-up-where-you-left-off) y las métricas clave de rendimiento de un vistazo
- **Navegación izquierda:** Organiza las herramientas por función (mensajería, audiencia, análisis, configuración)
- **Cabecera global:** Proporciona acceso rápido a la búsqueda, asistencia, configuración de idioma, notificaciones y a tu cuenta.

Tu experiencia en el panel está organizada por [espacios de trabajo]({{site.baseurl}}/user_guide/getting_started/workspaces), que te ayudan a gestionar contenidos para diferentes marcas, regiones o equipos. Puedes [cambiar entre espacios de trabajo](#workspace-switcher) en cualquier momento desde la navegación lateral.

## Accede a tu panel de control

Para empezar, [inicia sesión en tu cuenta Braze]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account). Tu acceso a las páginas del panel y el permiso para realizar determinadas acciones se basan en [los permisos de usuario]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) que tengas asignados. Si necesitas ayuda con tus permisos, ponte en contacto con los administradores de Braze.

## Navegar por Braze

La navegación Braze está diseñada para ayudarte a acceder eficientemente a características y contenidos en todos los dispositivos. Hay dos niveles de navegación en el panel de Braze: cabecera global y navegación lateral.

La cabecera global casi siempre está visible en la parte superior de la pantalla. Proporciona un acceso rápido a las herramientas y configuraciones esenciales, incluyendo:

- Buscar
- Apoyo y enlaces comunitarios
- [Idioma del panel de control]({{site.baseurl}}/user_guide/administrative/access_braze/language/)
- Notificaciones
- Configuración de la cuenta
- [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator/)

### Utiliza la navegación lateral

El menú vertical de la izquierda organiza las herramientas Braze por función y mantiene al alcance de la mano los elementos que más utilizas. Selecciona un elemento del menú principal para mostrar sus opciones en un diseño vertical apilado. 

![Conmutador de espacio de trabajo en el panel de Braze]({% image_buster /assets/img/workspace_switcher.png %}){: style="max-width:35%;float:right;margin-left:15px"}

#### Conmutador de espacios de trabajo

Situado en la parte superior de la navegación lateral, el conmutador de espacios de trabajo te permite moverte entre los distintos espacios de trabajo de tu instancia de Braze. Se resalta el espacio de trabajo activo.

[Los espacios de trabajo]({{site.baseurl}}/user_guide/getting_started/workspaces) ayudan a organizar el contenido por marca, región, línea de producto o equipo. Cada espacio de trabajo incluye sus propios datos, campañas y configuraciones. Tu acceso puede variar según el espacio de trabajo. Por ejemplo, puedes tener acceso de edición en un espacio de trabajo y acceso de sólo visualización en otro.

Para cambiar de espacio de trabajo, selecciona el desplegable de espacios de trabajo en la parte superior de la navegación lateral y elige el espacio de trabajo al que quieres acceder. También puedes [añadir espacios de trabajo favoritos](#adding-favorite-workspaces) para acceder más rápidamente a los que utilizas con más frecuencia.

#### Minimiza la navegación lateral

Para reducir el desorden visual, especialmente durante tareas como el diseño de un Canvas, puedes minimizar el panel de navegación lateral. Pulsa **el menú Minimizar** para contraerlo. Incluso cuando esté minimizado, pasa el ratón por encima de cualquier icono para ver información sobre herramientas con los nombres de los elementos del menú. Esto te ayuda a pasar rápidamente de una herramienta a otra manteniendo limpio tu espacio de trabajo.

![Minimizar y maximizar los iconos del menú]({% image_buster /assets/img/minimize_expand_menu.png %}){: style="max-width:60%;border:none"}

#### Navegación receptiva

La navegación se adapta fácilmente a diferentes tamaños de pantalla. En las pantallas más pequeñas, la navegación lateral se contrae automáticamente. Pulsa <i class="fa-solid fa-bars" aria-label="Abrir menú de navegación"></i> para abrir el menú cuando sea necesario. 

![En las pantallas más pequeñas, la navegación lateral se contrae automáticamente. Tocando el icono del menú se abren las opciones de navegación.]({% image_buster /assets/img/navigation/navigation_small_screens.png %}){: style="max-width: 80%;border:none"}

## Busca en tu panel

La barra de búsqueda global, situada en la cabecera, es la forma más rápida de encontrar contenido en todo tu panel Braze. Selecciona esta opción para abrir la interfaz de búsqueda y saltar directamente a lo que necesitas. 

![Búsqueda global abierta sin introducir términos de búsqueda, mostrando las páginas abiertas recientemente.]({% image_buster /assets/img/navigation/search_recently_opened.png %})

Tus contenidos abiertos recientemente aparecen debajo de la barra de búsqueda. Esto incluye cualquier campaña, Canvas, plantilla o página con la que hayas interactuado recientemente, lo que facilita volver a tu trabajo.

### ¿Qué puede buscar?

Puede buscar los siguientes elementos y acciones:

- Nombres de las campañas
- Nombres en lienzo
- Bloques de contenido
- Nombres de los segmentos
- Nombres de plantillas de correo electrónico
- Páginas dentro de Braze (incluyendo sinónimos)

{% alert tip %}
Para buscar un texto exacto, ponga el término de búsqueda entre comillas (""). Por ejemplo, buscar ["todos los usuarios"] devolverá todos los elementos que contengan la frase exacta "todos los usuarios" en su nombre.
{% endalert %}

### Tipo de contenido y etiquetas de estado

Cada resultado se etiqueta con una etiqueta que indica su tipo de contenido -como campaña, Canvas o segmento- y su estado (activo, archivado, detenido).

### Filtrar contenido activo y borrador

Por predeterminado, la búsqueda incluye elementos activos, borradores y archivados. Utiliza el botón alternativo **Mostrar sólo activos y borradores** para limitar los resultados.

![La opción "Mostrar sólo activos y borradores".]({% image_buster /assets/img/navigation/show_active_draft_new.png %})

### Atajos de teclado

Puedes desplazarte por los resultados de la búsqueda utilizando el teclado.

<style>
  div.small_table + table {
    max-width: 60%;
  }
table th:nth-child(1),
table th:nth-child(2),
table td:nth-child(1),
table td:nth-child(2), {
    width:20%;
}
table td {
    word-break: break-word;
}
</style>

<div class="small_table"></div>

| Acción                      | Atajo de teclado                                                             |
| --------------------------- | ----------------------------------------------------------------------------- |
| Abrir el menú de búsqueda        | {::nomarkdown} <ul> <li> Mac: <kbd>⌘</kbd> + <kbd>K</kbd> </li> <li>Windows: <kbd>Ctrl</kbd> + <kbd>K</kbd> </li> </ul> {:/}  |
| Desplazarse entre los resultados de búsqueda | <kbd>⬆</kbd> / <kbd>⬇</kbd>  |
| Seleccionar un resultado de búsqueda      | <kbd>Entrar</kbd>    |
| Cerrar el menú de búsqueda       | <kbd>Esc</kbd>  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Consejos

El panel de Braze incluye varias características que te ayudarán a trabajar de forma más eficiente y a acceder rápidamente a las herramientas y contenidos que más utilizas.

### Continuar donde lo dejaste

En la página **de inicio**, el panel muestra tus campañas, lienzos y segmentos editados o creados recientemente. Esto facilita volver al trabajo en curso sin necesidad de buscar. Cada elemento incluye etiquetas que muestran el tipo de contenido y el estado (como borrador, activo o detenido).

![Un borrador de Canvas, un segmento activo y un borrador de campaña en la sección "Continúa donde lo dejaste".]({% image_buster /assets/img/pick_up_where_you_left_off.png %})

Para más información, consulta [Panel de inicio]({{site.baseurl}}/user_guide/data_and_analytics/analytics/home_dashboard/#pick-up-where-you-left-off).

### Añadir espacios de trabajo favoritos

Si trabajas en varios espacios de trabajo, puedes marcar como favoritos los que utilices con más frecuencia para acceder a ellos más rápidamente. Para añadir espacios de trabajo favoritos, [accede a la configuración de tu perfil](#accessing-your-profile-settings), localiza el campo **Espacios de trabajo favoritos** en la sección **Perfil de cuenta** y selecciona los espacios de trabajo que quieras añadir como favoritos. Tus espacios de trabajo favoritos aparecerán en la parte superior del conmutador de espacios de trabajo para un acceso rápido.

### Accede a la configuración de tu perfil

Para administrar configuración de tu cuenta, preferencias de notificación e información personal:

1. Selecciona el icono de tu perfil en la cabecera global.
2. Selecciona **Gestionar tu cuenta** para acceder a la página de tu perfil.

Desde la página de tu perfil, puedes actualizar la configuración de tu correo electrónico, configurar la autenticación de dos factores, ver tus claves de API y administrar otros detalles de la cuenta.

## Accesibilidad en el panel de control

El panel de Braze utiliza colores de marca que cumplen las normas WCAG AA de contraste de colores. Esto favorece una experiencia inclusiva para todos los usuarios y se ajusta a las mejores prácticas de accesibilidad.

## Compartir opiniones

¿Quieres decirnos lo que piensas? Puedes compartir tus opiniones sobre navegación, accesibilidad, usabilidad, diseño visual y mucho más. Abre el menú **Soporte** en la cabecera global y selecciona **Compartir opiniones**. Revisamos todos los comentarios para ayudar a mejorar tu experiencia Braze.

## Recursos relacionados

### Tareas administrativas

- [Crea y administra espacios de trabajo]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/)
- [Administrar usuarios Braze]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/)
- [Permisos de usuario]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)
- [Equipos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/)

### Tareas clave y próximos pasos

- **Construye campañas**: [Crear una campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/)
- **Crea viajes**: [Construye un Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)
- **Define las audiencias**: [Crear un segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/)
- **Revisar el rendimiento**: [Resumen de análisis]({{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/)
- **Configura los ajustes**: [Configuración de la aplicación]({{site.baseurl}}/user_guide/administrative/app_settings/)


