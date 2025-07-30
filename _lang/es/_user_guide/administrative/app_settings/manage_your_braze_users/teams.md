---
nav_title: Equipos
article_title: Equipos
page_order: 4
page_type: reference
description: "Este artículo de referencia explica cómo utilizar Braze Teams en el panel. Aquí puedes aprender a crear equipos, asignar funciones y asignar etiquetas y filtros."

---

# Equipos

> Como administrador de Braze, puedes agrupar a los usuarios de tu panel en Equipos con distintas funciones y permisos de usuario. Esto le permite tener varios grupos de usuarios del cuadro de mandos no relacionados trabajando juntos en un espacio de trabajo separando los tipos de contenido que pueden editarse.

Los equipos pueden configurarse en función de la ubicación de la base de clientes, el idioma y los atributos personalizados, de modo que los miembros del equipo y los que no lo son tengan diferente acceso a las funciones de mensajería y a los datos de clientes. Se pueden asignar filtros y etiquetas de equipo en varias herramientas de participación.

Los equipos no están disponibles en todos los contratos Braze. Si desea acceder a esta función, póngase en [contacto](mailto:success@braze.com) con su gestor de cuenta Braze o consúltenos.

## ¿En qué se diferencian los Equipos de los conjuntos de permisos y funciones?

{% multi_lang_include permissions.md content="Differences" %}

## Creación de equipos

Vaya a **Configuración** > **Equipos internos** y seleccione <i class="fas fa-plus"></i> **Añadir equipo**.

![Añadir un nuevo equipo]({% image_buster /assets/img_archive/adding_a_team.png %})

Introduce el **nombre del equipo**. Si lo deseas, utiliza el campo **Definir equipo** para seleccionar un atributo personalizado, una ubicación o un idioma para definir mejor a qué datos de usuario tiene acceso el equipo. Por ejemplo, un posible caso de uso es realizar [pruebas con Equipos](#testing-with-Teams) creando un Equipo de desarrollo que sólo tenga acceso a los usuarios de prueba, identificados por un atributo personalizado. Otro caso de uso es restringir la comunicación con los usuarios en función del producto.

Si un equipo está definido por un atributo personalizado, un idioma o un país, puedes utilizarlo para filtrar a los usuarios finales por características como campañas, lienzos, tarjetas de contenido, segmentos, etc. Para más información, consulta [Asignar etiquetas de equipo](#tags-and-filters).

## Asignar usuarios a equipos

Los administradores y usuarios limitados de Braze con el permiso de nivel de empresa "Puede administrar la configuración de la empresa" pueden asignar permisos de nivel de equipo a un usuario del panel con acceso limitado. Cuando se asignan a un Equipo, los usuarios del panel sólo pueden leer o escribir datos disponibles para sus Equipos concretos, como el idioma del usuario, la ubicación o el atributo personalizado, según se definió al crear el Equipo.

Para asignar un usuario a un equipo, ve a **Configuración** > **Usuarios de la empresa** y selecciona un usuario que quieras añadir a tu equipo.

A continuación, realiza los siguientes pasos:

1. Seleccione **Editar**.
2. Establezca su función de usuario en **Limitado**.
3. Añádalos al espacio de trabajo correspondiente. 
4. Seleccione el **equipo** al que desea añadir este usuario y asígnele permisos específicos en la columna Permisos de **equipo**.

![]({% image_buster /assets/img/teams.png %})

### Permisos disponibles a nivel de equipo

A continuación se indican todos los permisos disponibles que puedes asignar a nivel de equipo. Cualquier permiso que no aparezca en esta lista sólo se concede a nivel del espacio de trabajo, y estos permisos aparecerán como "--" en la columna de permisos de **Equipos**.

- Acceda a campañas, lienzos, tarjetas, bloques de contenido, banderas de características, segmentos, mediatecas y centros de preferencias.
- Enviar campañas, Canvas
- Publicar tarjetas
- Editar segmentos
- Exportar datos de usuario
- Ver perfiles de usuarios que cumplen las reglas de PII
- Administrar usuarios del dashboard
- Administrar activos de biblioteca de medios

Para ver descripciones de lo que incluye cada permiso de usuario y cómo utilizarlos, consulte nuestra sección [Permisos de usuario]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#editing-user-permissions).

## Asignar etiquetas al equipo {#tags-and-filters}

Puedes asignar un equipo a lienzos, campañas, tarjetas, segmentos, plantillas de correo electrónico y activos de biblioteca de medios con el filtro **Añadir equipo**.
 
![Añadir una etiqueta de equipo a una campaña]({% image_buster /assets/img/teams1.png %}){: style="max-width:70%;"}

- Según las *definiciones* aplicadas al crear el equipo, cuando se asigna un filtro de equipo, la audiencia de esa herramienta de interacción se restringe a los perfiles de usuarios que coinciden con la definición.
- En función de *los permisos* asignados, los miembros del equipo sólo podrán acceder a las herramientas de interacción del panel que tengan configurado el filtro de su equipo. Si tienen permisos limitados o no tienen permisos para el espacio de trabajo, deben añadir un filtro de Equipo a determinados objetos antes de poder guardarlos o lanzarlos. Los miembros del equipo también pueden filtrar Lienzos, campañas, tarjetas y segmentos por Equipo para identificar el contenido relevante para ellos.

### Casos de uso

Considera las dos situaciones siguientes para una especialista en marketing de Braze llamada Michelle. Michelle es miembro de un equipo llamado "Desarrollo". Tiene acceso a todos los permisos a nivel de equipo para el equipo de desarrolladores.

{% tabs %}
{% tab Escenario 1 - Sólo permisos de equipo %}

En este escenario, Michelle es un usuario limitado que no tiene permisos a nivel de espacio de trabajo. Sus permisos son más o menos así:

![]({% image_buster /assets/img_archive/scenario1.png %})

Según los permisos asignados a Michelle, siempre que crea una campaña, sólo puede asignar el equipo "Desarrollador" a esa campaña. No puede lanzar la campaña a menos que el Equipo esté asignado, y no puede ver ni acceder a ninguna otra etiqueta de Equipo.

![]({% image_buster /assets/img_archive/team_permissions_scenario1.gif %})

{% endtab %}
{% tab Escenario 2 - Permisos de equipo y espacio de trabajo %}

En este caso, Michelle sigue siendo miembro del Equipo de Desarrollo, pero también tiene un permiso adicional a nivel de espacio de trabajo.

![]({% image_buster /assets/img_archive/scenario2.png %})

Como Michelle tiene el permiso a nivel de espacio de trabajo de "Acceder a campañas, lienzos, tarjetas, bloques de contenido, indicadores de características, segmentos, mediateca y centros de preferencias", puede ver y asignar otros filtros de equipo a la campaña que crea.

![]({% image_buster /assets/img_archive/team_permissions_scenario2.gif %})

Al igual que en el primer escenario, Michelle debe añadir la etiqueta Equipo de desarrollo a la campaña antes de poder lanzarla.

{% endtab %}
{% endtabs %}

## Pruebas con equipos

Un posible caso de uso de Teams es crear un sistema de aprobación basado en Teams para probar y lanzar contenidos en un entorno de producción.

Para ello, crea un equipo de "Desarrollo" que sólo tenga acceso a los usuarios de prueba. Puedes limitar un Equipo para que sólo acceda a usuarios de prueba si tus usuarios de prueba son identificables por un atributo personalizado. A continuación, añade el atributo personalizado como definición al crear o editar el Equipo (consulta la sección anterior [Creación de equipos](#creating-Teams)). Sus aprobadores deben tener acceso a todos los usuarios.

El proceso general sería el siguiente:

1. El equipo desarrollador crea una campaña y añade la etiqueta de equipo "Desarrollador".
2. El equipo de desarrollo lanza la campaña para poner a prueba a los usuarios.
3. El equipo de aprobación valida el diseño de la campaña local, la promociona y la lanza. Para lanzarla, el equipo de aprobación cambia la etiqueta del equipo de "Desarrollo" a "[Todos los equipos]" y vuelve a lanzar la campaña.

Para cambios en campañas activas:

1. El equipo desarrollador clona la campaña en curso, añade la etiqueta de equipo "Desarrollador" y guarda.
2. El equipo desarrollador realiza ediciones y las comparte con el equipo aprobador.
3. El equipo de aprobación elimina la etiqueta de equipo "Desarrollo", pausa la campaña anterior y lanza la nueva campaña.

## Archivar un equipo existente

Puedes archivar Equipos desde la página **Equipos internos**.

Selecciona uno o varios Equipos para archivar. Si el Equipo no está asociado a ningún objeto dentro de Braze, el Equipo se archivará inmediatamente. Si el Equipo está asociado a un objeto, se te presentará la opción de eliminar el Equipo tras el proceso de archivo o de sustituir el Equipo.

![Archivar un equipo asociado a un objeto en Braze]({% image_buster /assets/img_archive/archive_a_team.png %}){: style="max-width:70%;"}

Los administradores de Braze pueden desarchivar un Equipo seleccionando el Equipo archivado y seleccionando **Desarchivar**.

