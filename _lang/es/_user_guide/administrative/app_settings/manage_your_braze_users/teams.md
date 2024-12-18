---
nav_title: Equipos
article_title: Equipos
page_order: 4
page_type: reference
description: "Este artículo de referencia explica cómo utilizar los equipos Braze en el panel. Aquí puedes aprender a crear equipos, asignar funciones y asignar etiquetas y filtros."

---

# Equipos

> Como administrador de Braze, puede agrupar a los usuarios de su cuadro de mandos en equipos con distintas funciones y permisos de usuario. Esto le permite tener varios grupos de usuarios del cuadro de mandos no relacionados trabajando juntos en un espacio de trabajo separando los tipos de contenido que pueden editarse.

Los equipos pueden configurarse en función de la ubicación de la base de clientes, el idioma y los atributos personalizados, de modo que los miembros del equipo y los que no lo son tengan diferente acceso a las funciones de mensajería y a los datos de los clientes. Se pueden asignar filtros y etiquetas de equipo en varias herramientas de participación.

Los equipos no están disponibles en todos los contratos Braze. Si desea acceder a esta función, póngase en [contacto](mailto:success@braze.com) con su gestor de cuenta Braze o consúltenos.

## Creación de equipos

Vaya a **Configuración** > **Equipos internos** y seleccione <i class="fas fa-plus"></i> **Añadir equipo**.

{% alert note %}
Si utiliza la [navegación anterior]({{site.baseurl}}/navigation), **Equipos internos** se encuentra en **Gestionar configuración** > **Gestionar equipos**.
{% endalert %}

![Añadir un nuevo equipo][68]

Introduce el **nombre del equipo**. Si lo desea, utilice el campo **Definir equipo** para seleccionar un atributo personalizado, una ubicación o un idioma para definir mejor a qué datos de usuario tiene acceso el equipo. Por ejemplo, un posible caso de uso es realizar [pruebas con equipos](#testing-with-teams) creando un equipo de desarrollo que sólo tenga acceso a los usuarios de prueba, identificados por un atributo personalizado. Otro caso de uso es restringir la comunicación con los usuarios en función del producto.

Si un equipo se define por un atributo personalizado, idioma o país, puede utilizar el equipo para filtrar usuarios finales para funciones como campañas, lienzos, tarjetas de contenido, segmentos, etc. Para más información, consulta [Asignar etiquetas de equipo](#tags-and-filters).

## Asignación de usuarios a equipos

Los administradores de Braze y los usuarios limitados con el permiso a nivel de empresa "Puede gestionar la configuración de la empresa" pueden asignar permisos a nivel de equipo a un usuario del cuadro de mandos con acceso limitado. Cuando se asignan a un equipo, los usuarios del cuadro de mandos sólo pueden leer o escribir datos disponibles para sus equipos concretos, como el idioma del usuario, la ubicación o el atributo personalizado, tal y como se definieron al crear el equipo.

Para asignar un usuario a un equipo, vaya a **Configuración** > **Usuarios de la empresa** y seleccione un usuario que desee añadir a su equipo.

{% alert note %}
Si utiliza la [navegación antigua]({{site.baseurl}}/navigation), puede encontrar esta página seleccionando el icono de su cuenta y seleccionando **Gestionar usuarios**.
{% endalert %}

A continuación, realiza los siguientes pasos:

1. Seleccione **Editar**.
2. Establezca su función de usuario en **Limitado**.
3. Añádalos al espacio de trabajo correspondiente. 
4. Seleccione el **equipo** al que desea añadir este usuario y asígnele permisos específicos en la columna Permisos de **equipo**.

![][2]

### Permisos disponibles a nivel de equipo

A continuación se indican todos los permisos disponibles que puede asignar a nivel de equipo. Cualquier permiso que no aparezca en esta lista sólo se concede a nivel del espacio de trabajo, y estos permisos aparecerán como "--" en la columna de permisos de **Equipos**.

- Acceda a campañas, lienzos, tarjetas, bloques de contenido, banderas de características, segmentos, mediatecas y centros de preferencias.
- Enviar campañas, Canvas
- Publicar tarjetas
- Editar segmentos
- Exportar datos de usuario
- Ver perfiles de usuarios que cumplen las reglas de PII
- Administrar usuarios del dashboard
- Administrar activos de biblioteca de medios

Para ver descripciones de lo que incluye cada permiso de usuario y cómo utilizarlos, consulte nuestra sección [Permisos de usuario]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#editing-user-permissions).

## Asignar etiquetas de equipo {#tags-and-filters}

Puede asignar un equipo a lienzos, campañas, tarjetas, segmentos, plantillas de correo electrónico y activos de la biblioteca multimedia con el filtro **Añadir equipo**.
 
![Añadir una etiqueta Equipo a una campaña][3]{: style="max-width:70%;"}

- En función de las *definiciones* aplicadas cuando se creó el equipo, cuando se asigna un filtro de equipo, la audiencia de esa herramienta de participación se restringe a los perfiles de usuario que coinciden con la definición.
- En función de *los permisos* asignados, los miembros del equipo sólo podrán acceder a las herramientas de participación del cuadro de mandos que tengan configurado su filtro de equipo. Si tienen permisos limitados o no tienen permisos para el espacio de trabajo, deben añadir un filtro de equipo a determinados objetos antes de poder guardarlos o lanzarlos. Los miembros del equipo también pueden filtrar los lienzos, las campañas, las tarjetas y los segmentos por equipo para identificar el contenido relevante para ellos.

### Casos de uso

Considera las dos situaciones siguientes para una especialista en marketing de Braze llamada Michelle. Michelle es miembro de un equipo llamado "Desarrollo". Tiene acceso a todos los permisos a nivel de equipo para el equipo de Desarrollo.

{% tabs %}
{% tab Escenario 1: Solo permisos de equipo %}

En este escenario, Michelle es un usuario limitado que no tiene permisos a nivel de espacio de trabajo. Sus permisos son más o menos así:

![]({% image_buster /assets/img_archive/scenario1.png %})

Según los permisos asignados a Michelle, cada vez que crea una campaña, sólo puede asignar el equipo de "Desarrollo" a esa campaña. No puede lanzar la campaña a menos que el equipo esté asignado, y no puede ver ni acceder a ninguna otra etiqueta de equipo.

![]({% image_buster /assets/img_archive/team_permissions_scenario1.gif %})

{% endtab %}
{% tab Escenario 2: Permisos de equipo y permisos de espacio de trabajo %}

En este caso, Michelle sigue siendo miembro del equipo de Desarrollo, pero también tiene un permiso adicional a nivel de espacio de trabajo.

![]({% image_buster /assets/img_archive/scenario2.png %})

Como Michelle tiene el permiso a nivel de espacio de trabajo de "Acceder a campañas, lienzos, tarjetas, bloques de contenido, indicadores de características, segmentos, biblioteca multimedia y centros de preferencias", puede ver y asignar otros filtros de equipo a la campaña que crea.

![]({% image_buster /assets/img_archive/team_permissions_scenario2.gif %})

Al igual que en el primer escenario, Michelle debe añadir la etiqueta Equipo de desarrollo a la campaña antes de poder lanzarla.

{% endtab %}
{% endtabs %}

## Pruebas con equipos

Un posible caso de uso para los equipos es crear un sistema de aprobación basado en equipos para probar y lanzar contenidos en un entorno de producción.

Para ello, cree un equipo de "Desarrollo" que sólo tenga acceso a los usuarios de prueba. Puede limitar un equipo para que sólo acceda a usuarios de prueba si sus usuarios de prueba son identificables por un atributo personalizado. A continuación, añada el atributo personalizado como definición al crear o editar el equipo (consulte la sección anterior [Creación de equipos](#creating-teams)). Sus aprobadores deben tener acceso a todos los usuarios.

El proceso general sería el siguiente:

1. El equipo de desarrollo crea una campaña y añade la etiqueta de equipo "Desarrollo".
2. El equipo de desarrollo lanza la campaña para probar a los usuarios.
3. El equipo de aprobación valida el diseño de la campaña local, la promociona y la lanza. Para lanzarla, el equipo de aprobación cambia la etiqueta de equipo de "Desarrollo" a "[Todos los equipos]" y vuelve a lanzar la campaña.

Para cambios en campañas activas:

1. El equipo de desarrollo clona la campaña en curso, añade la etiqueta de equipo "Desarrollo" y guarda.
2. El equipo de desarrollo realiza modificaciones y las comparte con el equipo de aprobación.
3. El equipo de aprobación elimina la etiqueta de equipo "Desarrollo", pausa la campaña anterior y lanza la nueva campaña.

## Archivar un equipo existente

Puede archivar equipos desde la página **Equipos internos**.

Seleccione uno o varios equipos para archivar. Si el equipo no está asociado a ningún objeto dentro de Braze, el equipo se archivará inmediatamente. Si el equipo está asociado a un objeto, se le presentará la opción de eliminar el equipo tras el proceso de archivo o de sustituir el equipo.

![Archivar un equipo asociado a un objeto en Braze][86]{: style="max-width:70%;"}

Los administradores de Braze pueden desarchivar un equipo seleccionando el equipo archivado y seleccionando **Desarchivar**.

## ¿En qué se diferencian los equipos de los conjuntos de permisos y funciones?

Consulta [Usuarios de la empresa]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/) para ver un desglose de las diferencias entre equipos, conjuntos de permisos y funciones.

[2]: {% image_buster /assets/img/teams.png %}
[3]: {% image_buster /assets/img/teams1.png %}
[68]: {% image_buster /assets/img_archive/adding_a_team.png %}
[86]: {% image_buster /assets/img_archive/archive_a_team.png %}
