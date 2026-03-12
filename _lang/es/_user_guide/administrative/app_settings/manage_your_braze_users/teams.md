---
nav_title: Equipos
article_title: Equipos
page_order: 4
page_type: reference
description: "Este artículo de referencia explica cómo utilizar Braze Teams en el panel. Aquí puedes aprender a crear equipos, asignar roles y asignar etiquetas y filtros."

---

# Equipos

> Como administrador de Braze, puedes agrupar a los usuarios de tu empresa en equipos con diferentes roles y permisos de usuario. Esto te permite tener varios grupos de usuarios de la empresa, sin relación entre sí, trabajando juntos en un mismo espacio de trabajo, separando los tipos de contenido que se pueden editar.

Los equipos se pueden configurar según la ubicación de la base de clientes, el idioma y los atributos personalizados, de modo que los miembros del equipo y los que no lo son tengan un acceso diferente a las características de mensajería y a los datos de clientes. Se pueden asignar filtros y etiquetas de equipo en varias herramientas de participación. No hay límite en cuanto al número de equipos que puedes crear en tu espacio de trabajo.

Los equipos no están disponibles en todos los contratos Braze. Para acceder a esta característica, ponte en contacto con tu director de cuentas de Braze o [contáctanos](mailto:success@braze.com) para una consulta.

## ¿En qué se diferencian los equipos de los conjuntos de permisos y las funciones?

{% multi_lang_include permissions.md content="Differences" %}

## Crear equipos {#creating-teams}

Vaya a **Configuración** > **Equipos internos** y seleccione <i class="fas fa-plus"></i> **Añadir equipo**.

![Ventana para añadir un nuevo equipo.]({% image_buster /assets/img_archive/adding_a_team.png %})

Introduce el **nombre del equipo**. Si lo deseas, utiliza el campo **Definir equipo** para seleccionar un atributo personalizado, una ubicación o un idioma para definir con mayor precisión a qué datos de usuario tiene acceso el equipo. Por ejemplo, un posible caso de uso es realizar [pruebas con Teams](#test-with-teams) creando un equipo de desarrollo que solo tenga acceso a usuarios de prueba, identificados por un atributo personalizado. Otro caso de uso es restringir la comunicación con los usuarios en función del producto.

Si un equipo se define por un atributo personalizado, idioma o país, puedes utilizar el equipo para filtrar a los usuarios finales para características como campañas, lienzos, tarjetas de contenido, segmentos y mucho más. Para obtener más información, consulta [Asignar etiquetas de equipo](#tags-and-filters).

## Asignar usuarios a equipos

Los administradores de Braze y los usuarios con permisos limitados que tengan el permiso a nivel de empresa «Puede administrar la configuración de la empresa» pueden asignar permisos a nivel de equipo a un usuario de la empresa con acceso limitado. Cuando se asignan a un equipo, los usuarios de la empresa solo pueden leer o escribir datos disponibles para sus equipos concretos, como el idioma del usuario, la ubicación o los atributos personalizados, tal y como se definió al crear el equipo.

Para asignar un usuario a un equipo, ve a **Configuración** > **Usuarios de la empresa** y selecciona el usuario que deseas añadir a tu equipo.

A continuación, realiza los siguientes pasos:

1. En la sección **Permisos a nivel del espacio de trabajo**, agrega al usuario al espacio de trabajo adecuado si aún no está incluido.

![Permisos a nivel del espacio de trabajo con el conjunto de permisos Plantilla de banner.]({% image_buster /assets/img/team_level_permissions.png %})

{: start="2"}
2\. Selecciona **\+ Añadir permisos a nivel de equipo** y, a continuación, selecciona el **equipo** al que deseas añadir a este usuario.
3\. Asigna permisos específicos desde la sección Permisos **del equipo**.

![Permisos de plantillas de páginas de destino a nivel de equipo.]({% image_buster /assets/img/teams.png %})

### Permisos disponibles a nivel de equipo

A continuación se enumeran todos los permisos disponibles que puedes asignar a nivel de equipo. Cualquier permiso que no aparezca en esta lista sólo se concede a nivel del espacio de trabajo, y estos permisos aparecerán como "--" en la columna de permisos de **Equipos**.

{% tabs %}
{% tab Granular permissions %}

{% multi_lang_include alerts/important_alerts.md alert="granular permissions ea" %}

- Ver campañas
- Editar campañas
- Archivar campañas
- Ver Canvas
- Editar Canvas
- Archivar Canvas
- Ver las reglas de limitación de frecuencia
- Editar reglas de limitación de frecuencia
- Ver priorización de mensajes
- Editar priorización de mensajes
- Ver bloques de contenido
- Editar bloque de contenido
- Archivar bloques de contenido
- Lanzar bloques de contenido
- Ver las feature flags
- Editar conmutador de características
- Archiva feature flags
- Ver grupo de control global
- Ver segmentos
- Editar segmentos
- Ver plantillas IAM
- Editar plantillas IAM
- Archivar plantillas IAM
- Ver plantillas de correo electrónico
- Editar plantilla de correo electrónico
- Archivar plantillas de correo electrónico
- Ver plantillas webhook
- Editar plantillas webhook
- Archivar plantillas webhook
- Ver plantillas de enlaces
- Editar plantillas de enlaces
- Ver activos de la biblioteca de medios
- Editar activos de la biblioteca de medios
- Eliminar activos de la biblioteca de medios
- Ver ubicaciones
- Editar ubicaciones
- Ubicación de los archivos
- Ver códigos promocionales
- Editar códigos promocionales
- Códigos promocionales de las exportaciones
- Ver centros de preferencia
- Editar centros de preferencia
- Lanzar campañas
- Lanzar Canvas
- Exportar datos de usuario
- Ver perfiles de usuarios que cumplen las reglas de PII
- Ver usuarios del panel de control
- Editar usuarios del panel
- Aprobar campañas
- Aprobar Canvas
- Editar plantillas de Canvas
- Ver plantillas de Canvas
- Archivar plantillas de Canvas
- Publicar páginas de inicio
- Editar plantillas de páginas de destino
- Editar borradores de páginas de destino
- Ver páginas de inicio
- Archiva plantillas de páginas de inicio
- Ver informes
- Crear informes
- Editar informes

{% endtab %}
{% tab Legacy permissions %}

- Acceda a campañas, lienzos, tarjetas, bloques de contenido, banderas de características, segmentos, mediatecas y centros de preferencias.
- Enviar campañas, Canvas
- Iniciar y administrar tarjetas de contenido
- Editar segmentos
- Exportar datos de usuario
- Ver perfiles de usuarios que cumplen las reglas de PII
- Administrar usuarios del dashboard
- Administrar activos de biblioteca de medios
- Aprobar y denegar campañas
- Aprobar y denegar Canvas
- Crear y editar plantillas de Canvas
- Ver plantillas de Canvas
- Archivar plantillas de Canvas
- Editar plantillas de páginas de destino
- Ver plantillas de páginas de inicio
- Archiva plantillas de páginas de inicio

{% endtab %}
{% endtabs %}

Para ver descripciones de lo que incluye cada permiso de usuario y cómo utilizarlos, consulte nuestra sección [Permisos de usuario]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#editing-user-permissions).

## Asignar etiquetas al equipo {#tags-and-filters}

Puedes asignar un equipo a lienzos, campañas, tarjetas, segmentos, plantillas de correo electrónico y activos de la biblioteca multimedia con el filtro **Añadir equipo**.
 
![Añadir una etiqueta de equipo a una campaña.]({% image_buster /assets/img/teams1.png %}){: style="max-width:70%;"}

- Según las *definiciones* aplicadas cuando se creó el equipo, cuando se asigna un filtro de equipo, la audiencia de esa herramienta de interacción se limita a los perfiles de usuario que coinciden con la definición.
- En función de *los permisos* asignados, los miembros del equipo solo podrán acceder a las herramientas de interacción del panel de control que tengan configurado el filtro de su equipo. Si tienen permisos limitados o nulos en el espacio de trabajo, deben añadir un filtro de equipo a determinados objetos antes de poder guardarlos o iniciarlos. Los miembros del equipo también pueden filtrar lienzos, campañas, tarjetas y segmentos por equipo para identificar el contenido relevante para ustedes.

### Ejemplos

Considera las dos situaciones siguientes para una especialista en marketing de Braze llamada Michelle. Michelle es miembro de un equipo llamado «Desarrollo». Tienes acceso a todos los permisos de nivel de equipo para el equipo de desarrollo.

{% tabs %}
{% tab Scenario 1 - Only Team permissions %}

En este escenario, Michelle es un usuario con permisos limitados que no tiene permisos a nivel del espacio de trabajo. Sus permisos son más o menos así:

![Permisos personalizados sin permisos a nivel del espacio de trabajo y 16 permisos basados en equipos.]({% image_buster /assets/img_archive/scenario1.png %})

Según los permisos asignados a Michelle, cada vez que creas una campaña, solo puedes asignar el equipo «Desarrollo» a esa campaña. No puede lanzar la campaña a menos que se asigne el equipo, y no puede ver ni acceder a ninguna otra etiqueta del equipo.

![Menú desplegable de etiquetas del equipo de campaña que solo muestra la etiqueta del equipo «Desarrollo».]({% image_buster /assets/img_archive/team_permissions_scenario1.gif %})

{% endtab %}
{% tab Scenario 2 - Team permissions and workspace permissions %}

En este escenario, Michelle sigue siendo miembro del equipo de desarrollo, pero también tiene un permiso adicional a nivel de espacio de trabajo.

![Permisos personalizados con un permiso a nivel de espacio de trabajo y 15 permisos basados en equipos.]({% image_buster /assets/img_archive/scenario2.png %})

Dado que Michelle tiene permiso a nivel del espacio de trabajo para «Acceder a campañas, lienzos, tarjetas, bloques de contenido, indicadores de características, segmentos, biblioteca multimedia y centros de preferencias», puede ver y asignar otros filtros del equipo a la campaña que creas.

![Menú desplegable de etiquetas del equipo de campaña con varias etiquetas de equipo]({% image_buster /assets/img_archive/team_permissions_scenario2.gif %})

Al igual que en el primer escenario, Michelle debe añadir la etiqueta «Equipo de desarrollo» a la campaña antes de poder lanzarla.

{% endtab %}
{% endtabs %}

## Prueba con equipos

Un posible caso de uso de Teams es crear un sistema de aprobación basado en Teams para probar y lanzar contenido en un entorno de producción.

Para ello, crea un equipo de «Desarrollo» que solo tenga acceso a los usuarios de prueba. Puedes limitar un equipo para que solo acceda a usuarios de prueba si estos son identificables mediante un atributo personalizado. A continuación, añade el atributo personalizado como definición al crear o editar el equipo (consulta la sección anterior [Creación de equipos](#creating-Teams)). Sus aprobadores deben tener acceso a todos los usuarios.

El proceso general sería el siguiente:

1. El equipo de desarrollo crea una campaña y añade la etiqueta «Equipo de desarrollo».
2. El equipo de desarrollo lanza la campaña para probar a los usuarios de prueba.
3. El equipo de aprobación valida el diseño de la campaña local, la promociona y la lanza. Para lanzarla, el equipo de aprobación cambia la etiqueta del equipo de «Desarrollo» a «[Todos los equipos]» y vuelve a lanzar la campaña.

Para cambios en campañas activas:

1. El equipo de desarrollo clona la campaña en curso, añade la etiqueta «Equipo de desarrollo» y guarda los cambios.
2. El equipo de desarrollo realiza modificaciones y las comparte con el equipo de aprobación.
3. El equipo de aprobadores elimina la etiqueta del equipo de «Desarrollo», pausa la campaña anterior y lanza la nueva campaña.

## Archivar un equipo existente

Puedes archivar equipos desde la página **Equipos internos**.

Selecciona uno o varios equipos para archivar. Si el equipo no está asociado a ningún objeto dentro de Braze, se archivará inmediatamente. Si el equipo está asociado a un objeto, se te ofrecerá la opción de eliminar el equipo tras el proceso de archivo o sustituirlo.

![Archivar un equipo asociado a un objeto en Braze]({% image_buster /assets/img_archive/archive_a_team.png %}){: style="max-width:70%;"}

Los administradores de Braze pueden desarchivar un equipo seleccionando el equipo archivado y seleccionando **Desarchivar**.