---
nav_title: Usuarios de la empresa
article_title: Administrador de usuarios de la empresa
page_order: 23
page_type: reference
description: "Esta página trata sobre la administración de los usuarios de tu empresa, como añadir y eliminar usuarios, configurar permisos de usuario, crear equipos y administrar la configuración de la empresa."
---

# Administrador de usuarios de la empresa

> Aprenda a gestionar usuarios en su cuenta de empresa, incluyendo añadir, suspender y eliminar usuarios.

{% alert note %}
Varias secciones de esta página remiten a la página **Usuarios de la empresa**. Si utiliza la [navegación más antigua]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/), **Usuarios de la empresa** se llama **Gestionar usuarios** y se encuentra debajo del icono de su cuenta.
{% endalert %}

## Añadir usuarios de la empresa

Debes tener permisos de administrador para añadir usuarios a tu cuenta Braze. 

Para añadir un nuevo usuario:

1. Vaya a **Configuración** > **Usuarios de la empresa**.
2. Selecciona **\+ Añadir nuevo usuario**.
3. Introduce la información que se te pida, incluyendo su correo electrónico, departamento y [rol de usuario]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#creating-a-role).

{% alert tip %}
El departamento que figura en el perfil de un usuario determina los tipos de comunicaciones que recibe de Braze. De este modo, todo el mundo recibe únicamente las comunicaciones y alertas que son relevantes para su uso de Braze.
{% endalert %}

![Campos de datos del usuario.]({% image_buster /assets/img/add_new_user_2.png %}){: style="max-width:60%;"}

{:start="4"}

4. Para los usuarios que no son administradores, seleccione los [permisos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#editing-a-users-permissions) a nivel de empresa y a nivel de espacio de trabajo que desea que tenga este usuario.

![Permisos a nivel del espacio de trabajo con una sección para campos de permisos personalizados.]({% image_buster /assets/img/add_new_user_3.png %})

### Requisitos de la dirección de correo electrónico

Cada dirección de correo electrónico utilizada en una [instancia]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) debe ser única. Esto significa que si intentas añadir una dirección de correo electrónico que ya está asociada a un usuario que tenía o sigue teniendo acceso a un espacio de trabajo de la empresa en esa instancia, verás un mensaje de error. 

Si tu equipo utiliza Gmail y tienes problemas para añadir una dirección de correo electrónico, puedes crear un alias añadiendo un signo más (+) como "+1" o "+prueba" a la dirección de correo electrónico. Por ejemplo, `contractor@braze.com` puede tener un alias de `contractor+1@braze.com`. Los correos electrónicos enviados a `contractor+1@braze.com` seguirán llegando a `contractor@braze.com`, pero el alias se reconocerá como una dirección de correo electrónico única.

### ¿Puedo cambiar la dirección de correo electrónico de mi cuenta de Braze?

Por motivos de seguridad, los usuarios no pueden cambiar la dirección de correo electrónico asociada a la cuenta de Braze. Si un usuario desea actualizar su dirección de correo electrónico, un administrador debe [crearle una nueva cuenta](#adding-braze-users) con su dirección de correo electrónico preferida.

## Asignar acceso y responsabilidades a los usuarios

{% multi_lang_include permissions.md content="Differences" %}

## Suspender usuarios de la empresa

Al suspender a un usuario, su cuenta pasa a un estado inactivo, en el que el usuario ya no puede iniciar sesión, pero se conservan los datos asociados a su cuenta. Solo los administradores pueden suspender o reactivar a los usuarios de la empresa. Ten en cuenta que los usuarios suspendidos pueden seguir recibiendo notificaciones de Braze.

Para suspender a un usuario, ve a **Configuración** > **Usuarios de la empresa**, busca tu nombre de usuario y selecciona<i class="fa-solid fa-user-lock"></i>**Suspender**.

![Opción para suspender a un usuario.]({% image_buster /assets/img_archive/suspend_user.png %})

Los administradores también pueden suspender a un usuario seleccionando su nombre en la lista y seleccionando **Suspender usuario** en el pie de página.

![Suspender a un usuario al editar los detalles del usuario.]({% image_buster /assets/img_archive/suspend_user2.png %}){: style="max-width:70%;"}

## Eliminación de usuarios de la empresa

Para eliminar un usuario, ve a **Configuración** > **Usuarios de la empresa**, busca tu nombre de usuario y selecciona<i class="fa fa-trash-can"></i>**Eliminar usuario**.

![Eliminar un usuario.]({% image_buster /assets/img_archive/delete_user_new.png %})

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

### Impacto de eliminar un usuario del panel de control

Cuando se elimina un usuario del panel, no hay ningún impacto significativo en los activos que creaste dentro del panel, como campañas, segmentos y lienzos. Sin embargo, el campo **Creado por** de estos activos muestra un valor «nulo» en lugar de la dirección de correo electrónico del usuario eliminado.

Si posteriormente se crea un nuevo usuario del panel de Braze con la misma dirección de correo electrónico que el usuario eliminado, Braze no volverá a asociar los activos creados por el usuario eliminado con el nuevo usuario. El nuevo usuario del panel comenzará desde cero y no se le atribuirá la autoría de ningún activo existente en el panel.

## Solución de problemas

### «El correo electrónico ya está en uso» al intentar añadir un usuario

Si intentas añadir un nuevo usuario y recibes un error que indica que el correo electrónico ya está en uso, pero no lo encuentras en tu lista de usuarios, lo más probable es que ese usuario exista en otra instancia del mismo clúster del panel de Braze.

Para crear este nuevo usuario, puedes hacer cualquiera de lo siguiente:

1. Elimina al usuario de la otra instancia antes de poder crearlo en la nueva, o
2. Crea el usuario con una cadena de correo electrónico diferente (como `testing+01@braze.com`) u otro alias de correo electrónico. 

Si no recibes el mensaje de activación en tu buzón de entrada cuando utilizas `testing+01@braze.com`, confirma con tu equipo de TI que puedes aceptar mensajes de ese tipo de dirección de correo electrónico. Algunos administradores filtran los mensajes enviados a direcciones de correo electrónico con un `+`.
