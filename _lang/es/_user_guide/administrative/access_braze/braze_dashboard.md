---
nav_title: El panel
article_title: El panel de Braze
page_order: 5
page_type: reference
description: "El panel de Braze es tu espacio de trabajo central para crear, gestionar y analizar la interacción con los clientes. Reúne herramientas de mensajería, información sobre la audiencia, segmentación y datos de rendimiento en tiempo real en un solo lugar."

---

# El panel de Braze

> El panel de Braze es tu espacio de trabajo central para crear, gestionar y analizar la interacción con los clientes. Accede a él en[dashboard.braze.com](https://dashboard.braze.com/)  o [dashboard.braze.eu](https://dashboard.braze.eu/).

Utiliza el panel de Braze para planificar campañas, lanzar y gestionar mensajes, explorar información sobre la audiencia, ajustar la segmentación y revisar el rendimiento en tiempo real y las métricas de interacción desde una única interfaz.

## Resumen del panel de control

Cuando inicias sesión, el panel te ofrece una vista centralizada de tus herramientas de interacción y datos:

- **Página de inicio:** Muestra tu [contenido editado recientemente](#pick-up-where-you-left-off) y las métricas clave de rendimiento de un vistazo.
- **Navegación izquierda:** Organiza las herramientas por función (mensajería, audiencia, análisis, configuración).
- **Encabezado global:** Proporciona acceso rápido a la búsqueda, la asistencia técnica, la configuración de idioma, las notificaciones y tu cuenta.

Tu experiencia en el panel está organizada por [espacios de trabajo]({{site.baseurl}}/user_guide/getting_started/workspaces), lo que te ayuda a administrar el contenido de diferentes marcas, regiones o equipos. Puedes [cambiar entre espacios de trabajo](#workspace-switcher) en cualquier momento desde el menú lateral.

## Accede a tu panel

Para empezar, [inicia sesión en tu cuenta de Braze]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account). Tu acceso a las páginas del panel y tu permiso para realizar determinadas acciones se basan en [los permisos de usuario]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) que se te hayan asignado. Si necesitas ayuda con tus permisos, ponte en contacto con los administradores de Braze.

## Navegar por Braze

La navegación de Braze está diseñada para ayudarte a acceder de manera eficiente a las características y el contenido en todos los dispositivos. Hay dos niveles de navegación en el panel de Braze: el encabezado global y la navegación lateral.

El encabezado global casi siempre está visible en la parte superior de la pantalla. Proporciona un acceso rápido a herramientas y configuraciones esenciales, entre los que se incluyen:

- Buscar
- Apoyo y enlaces a la comunidad
- [Idioma del panel]({{site.baseurl}}/user_guide/administrative/access_braze/language/)
- Notificaciones
- Configuración de la cuenta
- [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator/)

### Utiliza la navegación lateral.

El menú vertical de la izquierda organiza las herramientas de Braze por función y mantiene los elementos más utilizados al alcance de la mano. Selecciona un elemento del menú principal para mostrar sus opciones en un diseño vertical apilado. 

![Cambiador de espacio de trabajo en el panel de Braze]({% image_buster /assets/img/workspace_switcher.png %}){: style="max-width:35%;float:right;margin-left:15px"}

#### Cambiar de espacio de trabajo

Situado en la parte superior de la barra de navegación lateral, el selector de espacios de trabajo te permite desplazarte entre los diferentes espacios de trabajo de tu instancia de Braze. El espacio de trabajo activo aparece resaltado.

[Los espacios de trabajo]({{site.baseurl}}/user_guide/getting_started/workspaces) ayudan a organizar el contenido por marca, región, línea de productos o equipo. Cada espacio de trabajo incluye tus propios datos, campañas y configuraciones. Tu acceso puede variar entre los distintos espacios de trabajo. Por ejemplo, es posible que tengas acceso de edición en un espacio de trabajo y acceso de solo lectura en otro.

Para cambiar de espacio de trabajo, selecciona el menú desplegable de espacios de trabajo situado en la parte superior del panel de navegación lateral y elige el espacio de trabajo al que deseas acceder. También puedes [añadir espacios de trabajo favoritos](#adding-favorite-workspaces) para acceder más rápidamente a los que utilizas con más frecuencia.

#### Minimizar la navegación lateral

Para reducir el desorden visual, especialmente durante tareas como el diseño de un Canvas, puedes minimizar el panel de navegación lateral. Pulsa **el menú Minimizar** para contraerlo. Incluso cuando estén minimizados, pasa el cursor por encima de cualquier icono para ver información sobre herramientas con los nombres de los elementos del menú. Esto te ayuda a moverte rápidamente entre las herramientas y mantener tu espacio de trabajo limpio.

![Minimizar y maximizar los iconos del menú]({% image_buster /assets/img/minimize_expand_menu.png %}){: style="max-width:60%;border:none"}

#### Navegación receptiva

La navegación se adapta fácilmente a diferentes tamaños de pantalla. En pantallas más pequeñas, la navegación lateral se contrae automáticamente. Pulsa <i class="fa-solid fa-bars" aria-label="Menú de navegación abierto"></i> para abrir el menú cuando sea necesario. 

![En pantallas más pequeñas, la navegación lateral se contrae automáticamente. Al pulsar el icono del menú se abren las opciones de navegación.]({% image_buster /assets/img/navigation/navigation_small_screens.png %}){: style="max-width: 80%;border:none"}

## Busca en tu panel

La barra de búsqueda global, con su ubicación en el encabezado, es la forma más rápida de encontrar contenido en tu panel de Braze. Selecciona para abrir la interfaz de búsqueda y acceder directamente a lo que necesitas. 

![Búsqueda global abierta sin términos de búsqueda introducidos, que muestra las páginas abiertas recientemente.]({% image_buster /assets/img/navigation/search_recently_opened.png %})

El contenido que has abierto recientemente aparece debajo de la barra de búsqueda. Esto incluye cualquier campaña, Canvas, plantilla o página con la que hayas interactuado recientemente, lo que facilita volver a tu trabajo.

### ¿Qué puede buscar?

Puede buscar los siguientes elementos y acciones:

- Nombres de las campañas
- Nombres en lienzo
- Bloques de contenido
- Nombres de los segmentos
- Nombres de plantillas de correo electrónico
- Páginas dentro de Braze (incluidos sinónimos)

{% alert tip %}
Para buscar un texto exacto, ponga el término de búsqueda entre comillas (""). Por ejemplo, si buscas [«todos los usuarios»], aparecerán todos los elementos que contengan la frase exacta «todos los usuarios» en su nombre.
{% endalert %}

### Tipo de contenido y etiquetas de estado

Cada resultado se etiqueta con una etiqueta que indica su tipo de contenido, como campaña, Canvas o segmento, y su estado (activo, archivado, detenido).

### Filtrar contenido activo y borrador

De forma predeterminada, la búsqueda incluye elementos activos, borradores y archivados. Alternar entre **Mostrar solo activos y borradores** para limitar los resultados.

![La opción "Mostrar sólo activos y borradores".]({% image_buster /assets/img/navigation/show_active_draft_new.png %})

### Atajos de teclado

Puedes desplazarte por los resultados de búsqueda utilizando el teclado.

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

El panel de Braze incluye varias características que te ayudarán a trabajar de forma más eficiente y a acceder rápidamente a las herramientas y el contenido que más utilizas.

### Continuar donde lo dejaste

En la página **de inicio**, el panel muestra las campañas, los lienzos y los segmentos que has editado o creado recientemente. Esto facilita volver al trabajo en curso sin necesidad de buscar. Cada elemento incluye etiquetas que muestran el tipo de contenido y el estado (por ejemplo, borrador, activo o detenido).

![Un borrador de Canvas, un segmento activo y un borrador de campaña en la sección "Continúa donde lo dejaste".]({% image_buster /assets/img/pick_up_where_you_left_off.png %})

Para obtener más información, consulta [el panel de control de inicio]({{site.baseurl}}/user_guide/data_and_analytics/analytics/home_dashboard/#pick-up-where-you-left-off).

### Añadir espacios de trabajo favoritos

Si trabajas en varios espacios de trabajo, puedes marcar tus favoritos para acceder más rápidamente a ellos. Para añadir espacios de trabajo favoritos, [accede a la configuración de tu perfil](#accessing-your-profile-settings), busca la ubicación de **los espacios de trabajo favoritos** en la sección **Perfil de la cuenta** y selecciona los espacios de trabajo que deseas marcar como favoritos. Tus espacios de trabajo favoritos aparecerán en la parte superior del selector de espacios de trabajo para que puedas acceder a ellos rápidamente.

### Accede a la configuración de tu perfil.

Para administrar la configuración de tu cuenta, las preferencias de notificación y la información personal:

1. Selecciona tu icono de perfil en el encabezado global.
2. Selecciona **Administrar tu cuenta** para acceder a tu página de perfil.

Desde tu página de perfil, puedes actualizar tu configuración de correo electrónico, configurar la autenticación de dos factores, ver tus claves de API y gestionar otros detalles de tu cuenta.

## Accesibilidad en el panel

El panel de Braze utiliza colores de marca que cumplen con los estándares WCAG AA en cuanto a contraste de colores. Esto favorece una experiencia inclusiva para todos los usuarios y se ajusta a las mejores prácticas en materia de accesibilidad.

## Compartir comentarios

¿Quieres decirnos qué opinas? Puedes compartir tus comentarios sobre la navegación, la accesibilidad, la usabilidad, el diseño visual y mucho más. Abre el menú **Soporte** técnico en el encabezado global y selecciona **Compartir comentarios**. Revisamos todos los comentarios para ayudar a mejorar tu experiencia con Braze.

## Recursos relacionados

### Tareas administrativas

- [Crear y administrar espacios de trabajo]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/)
- [Administrar usuarios de Braze]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/)
- [Permisos de usuario]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)
- [Equipos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/)

### Tareas clave y próximos pasos

- **Crear campañas**: [Crear una campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/)
- **Crear viajes**: [Crea un Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)
- **Define las audiencias**: [Crear un segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/)
- **Revisar el rendimiento**: [Resumen de análisis]({{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/)
- **Configura la configuración**: [Configuración de la aplicación]({{site.baseurl}}/user_guide/administrative/app_settings/)


