---
nav_title: Aprobación y permisos de Canvas
article_title: Aprobación y permisos de Canvas 
page_order: 0.5
alias: "/canvas_approval/"
description: "Este artículo de referencia explica cómo aprobar los lienzos antes de su lanzamiento y describe los permisos de usuario relacionados."
tool: Canvas
---

# Aprobación y permisos en Canvas

> La aprobación del lienzo añade un proceso de revisión a su flujo de trabajo antes del lanzamiento. De este modo, podrá comprobar que cada confirmación está aprobada para lanzar el Canvas.

## Activar la aprobación de Canvas

Para activar el flujo de trabajo de aprobación para Canvas, ve a **Configuración** > **Flujo de trabajo de aprobación** en **Configuración del lugar de trabajo**. Por defecto, esta función está desactivada.

![La configuración del flujo de trabajo de aprobación donde se activa la opción de utilizar el flujo de trabajo de aprobación para campañas y lienzos.][1]

{% alert tip %}
Asegúrese de que dispone de los [permisos de usuario]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions) adecuados para aprobar los lienzos.
{% endalert %}

### Establecer permisos de usuario

Una vez activado el flujo de trabajo de aprobación para Canvas, vaya a **Configuración** > **Usuarios de la empresa** y seleccione **Aprobar y denegar lienzos** para permitir que usuarios específicos aprueben y denieguen lienzos inmediatamente. Este permiso también puede aplicarse a espacios de trabajo o [equipos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/), o añadirse a un [conjunto de permisos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#permission-sets).

Un usuario con este permiso puede realizar cualquiera de las siguientes acciones en el flujo de trabajo Canvas:
- Aprobar pero no lanzar el lienzo
- Lanzar pero no aprobar el lienzo
- Aprobar y poner en marcha el lienzo
- Ni aprobar ni lanzar el Canvas

![Ejemplo de una casilla de verificación no seleccionada para el permiso Aprobar y denegar lienzos, lo que significa que este usuario no tiene permiso para aprobar o denegar lienzos.][3]{: style="max-width:70%" }

{% alert important %}
Para editar una campaña en directo, necesitará el permiso "Aprobar y denegar campañas". El usuario deberá aprobar sus cambios, ya que aún no se dispone de una versión preliminar de las campañas. Este no es el caso de los Lienzos, ya que un usuario puede hacer cambios y guardarlos como borrador, y otro usuario puede aprobar y lanzar el Lienzo.
{% endalert %}

## Uso de autorizaciones

Cuando disponga del permiso "Aprobar y denegar lienzos", tendrá acceso al paso **Resumen** del constructor de lienzos. Esta página proporciona un resumen de los detalles clave de Canvas con la opción de aprobar o denegar estos detalles, incluidos los eventos de conversión, el calendario de entrada y el tipo y la cantidad de componentes de su Canvas. Tenga en cuenta que el estado predeterminado para la aprobación de Canvas es **Pendiente de aprobación**.

Una vez establecidos los estados de aprobación en el paso **Resumen**, cualquier cambio posterior realizado en el lienzo restablecerá todos los estados de aprobación cuando se guarde. Esto se aplica a cualquier cambio realizado tanto en un borrador de Canvas como en un Canvas posterior al lanzamiento. Por ejemplo, si sólo realiza cambios en el público objetivo, el paso **Resumen** revertirá los estados de aprobación de todas las secciones al estado predeterminado, pendiente.

![Un ejemplo del flujo de trabajo de aprobación de Canvas en el que los detalles de Eventos de Conversión y Calendario de Entrada se han marcado como aprobados.][2]{: style="max-width:85%" }

Una vez que cada sección esté aprobada, el botón **Lanzar** estará disponible, y podrás lanzar tu Canvas.

[1]: {% image_buster /assets/img_archive/canvas_approval.png %}
[2]: {% image_buster /assets/img_archive/canvas_approval_summary.png %}
[3]: {% image_buster /assets/img_archive/canvas_approval_user_permissions.png %}