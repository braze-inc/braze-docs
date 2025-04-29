---
nav_title: Usuarios
article_title: Gestión de usuarios Braze
page_order: 0
page_type: reference
description: "En este artículo de referencia se explica cómo gestionar los usuarios de la cuenta de empresa, incluidas la adición, la suspensión y la eliminación de usuarios."

---

# Gestión de usuarios Braze

> Aprenda a gestionar usuarios en su cuenta de empresa, incluyendo añadir, suspender y eliminar usuarios.

{% alert note %}
Varias secciones de esta página remiten a la página **Usuarios de la empresa**. Si utiliza la [navegación más antigua]({{site.baseurl}}/navigation), **Usuarios de la empresa** se llama **Gestionar usuarios** y se encuentra debajo del icono de su cuenta.
{% endalert %}

## Añadir usuarios Braze

Debes tener permisos de administrador para añadir usuarios a tu cuenta Braze. 

Para añadir un nuevo usuario:

1. Vaya a **Configuración** > **Usuarios de la empresa**.
2. Haga clic en **\+ Añadir nuevo usuario**.
3. Introduce la información que se te pida, incluyendo su correo electrónico, departamento y [rol de usuario]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#creating-a-role).

{% alert tip %}
El departamento que figura en el perfil de un usuario determina los tipos de comunicaciones que recibe de Braze. De este modo, todo el mundo recibe únicamente las comunicaciones y alertas que son relevantes para su uso de Braze.
{% endalert %}

![][2]

{:start="4"}

4. Para los usuarios que no son administradores, seleccione los [permisos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#editing-a-users-permissions) a nivel de empresa y a nivel de espacio de trabajo que desea que tenga este usuario.

![][3]

### Requisitos de la dirección de correo electrónico

Cada dirección de correo electrónico utilizada en una [instancia]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) debe ser única. Esto significa que si intentas añadir una dirección de correo electrónico que ya está asociada a un usuario que tenía o sigue teniendo acceso a un espacio de trabajo de la empresa en esa instancia, verás un mensaje de error. 

Si tu equipo utiliza Gmail y tienes problemas para añadir una dirección de correo electrónico, puedes crear un alias añadiendo un signo más (+) como "+1" o "+prueba" a la dirección de correo electrónico. Por ejemplo, `contractor@braze.com` puede tener un alias de `contractor+1@braze.com`. Los correos electrónicos enviados a `contractor+1@braze.com` seguirán llegando a `contractor@braze.com`, pero el alias se reconocerá como una dirección de correo electrónico única.

### ¿Puedo cambiar la dirección de correo electrónico de mi cuenta de Braze?

Por razones de seguridad, los usuarios no pueden cambiar la dirección de correo electrónico asociada a su cuenta Braze. Si un usuario desea actualizar su dirección de correo electrónico, un administrador debe [crearle una nueva cuenta](#adding-braze-users) con su dirección de correo electrónico preferida.

## Suspender a los usuarios de Braze

Al suspender a un usuario, su cuenta pasa a un estado inactivo, en el que el usuario ya no puede iniciar sesión, pero se conservan los datos asociados a su cuenta. Sólo los administradores pueden suspender o anular la suspensión de los usuarios de Braze.

Para suspender a un usuario, ve a **Configuración** > **Usuarios de la empresa**, busca su nombre de usuario y selecciona <i class="fa-solid fa-user-lock"></i> **Suspender**.

![Suspender un usuario][4]

Los administradores también pueden suspender a un usuario seleccionando su nombre en la lista y haciendo clic en **Suspender usuario** en el pie de página.

![Suspender un usuario al editar los detalles del usuario.][5]

## Asignar acceso y responsabilidades a los usuarios

{% multi_lang_include permissions.md content="Diferencias" %}

## Eliminar usuarios de Braze

Para eliminar un usuario, vaya a **Configuración** > **Usuarios de la empresa**, busque su nombre de usuario y seleccione <i class="fa fa-trash-can"></i> **Eliminar usuario**.

![Eliminar un usuario][34]

Una vez eliminado un usuario, Braze no conserva ninguno de los siguientes datos de cuenta:

- Cualquier atributo que el usuario tuviera
- Dirección de correo electrónico
- Número de teléfono
- ID de usuario externo
- Género
- País
- Idioma
- Otros datos similares

Braze conservará los siguientes datos de la cuenta:

- Atributos personalizados o datos de prueba asociados a su cuenta
- Campañas o Lienzos creados por ellos (pero el nombre del usuario no aparecerá en ellos, como por ejemplo en la columna **Último editado por** )

[1]: {% image_buster /assets/img/add_new_user_1.png %}
[2]: {% image_buster /assets/img/add_new_user_2.png %}
[3]: {% image_buster /assets/img/add_new_user_3.png %}
[4]: {% image_buster /assets/img_archive/suspend_user.png %}
[5]: {% image_buster /assets/img_archive/suspend_user2.png %}
[27]: {% image_buster /assets/img/add-user.gif %} "Añadir un nuevo proceso de usuario"
[34]: {% image_buster /assets/img_archive/delete_user_new.png %}