---
nav_title: Aprovisionamiento automático de usuarios
article_title: Aprovisionamiento automático de usuarios
page_order: 10
page_type: reference
description: "Este artículo de referencia explica qué información debe proporcionar para el aprovisionamiento automatizado de usuarios y cómo y dónde utilizar el token generado del Sistema para la gestión de identidades entre dominios (SCIM)."
alias: /scim/automated_user_provisioning/

---

# Aprovisionamiento automático de usuarios

> Utiliza el aprovisionamiento SCIM para crear y administrar automáticamente usuarios Braze a través de la API. Este artículo te explica qué información debes proporcionar, cómo generar tu token SCIM y dónde encontrar tu punto final de la API SCIM.

## Acceder a la configuración de aprovisionamiento SCIM

1. En el panel de Braze, ve a **Configuración** > **Configuración de administración** > **Aprovisionamiento SCIM** y añade un proveedor de identidad.
2. En el paso de aprovisionamiento **de Braze**, selecciona un método de aprovisionamiento y proporciona la configuración de acceso.

![Una página para configurar la integración SCIM con secciones para seleccionar un método de aprovisionamiento y proporcionar configuraciones de acceso.]({% image_buster /assets/img_archive/scim_braze_config.png %}){: style="max-width:70%;"}

{: start="3"}
3\. En el paso de **configuración del IdP**, sigue los pasos dentro de la plataforma para el método de aprovisionamiento que hayas seleccionado.

{% tabs %}
{% tab Okta - Braze app %}

{% alert important %}
La integración de Okta se encuentra actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en el acceso anticipado.
{% endalert %}

## Paso 1: Configurar el aprovisionamiento SCIM

### Paso 1.1: Habilitar SCIM

1. Ve a tu aplicación Braze en Okta.
2. Selecciona la pestaña **General**.
3. En la sección **Configuración de la aplicación**, selecciona **Editar**.
4. En el campo **Aprovisionamiento**, selecciona **SCIM** y, a continuación, **Guardar**.

### Paso 1.2: Configurar la integración SCIM

1. Selecciona la pestaña **Aprovisionamiento**.
2. En **Configuración** > **Integración** > **Conexión SCIM**, selecciona **Editar** y rellena los valores de los campos que aparecen en la tabla de la página **Configurar aprovisionamiento SCIM**.

### Paso 1.3: Prueba las credenciales de la API

Selecciona **Probar credenciales API**. Aparecerá un mensaje de verificación si la integración se ha realizado correctamente y podrás guardarla.

### Paso 1.4: Habilitar el aprovisionamiento a la aplicación

1. En **Aprovisionamiento** > **Configuración** > **A la aplicación** > **Aprovisionamiento a la aplicación**, selecciona **Editar**.
2. Habilita lo siguiente:
    - Crear usuarios
    - Actualizar atributos de usuarios
    - Desactivar usuarios
3. Revisa y configura la sección de mapeado **de atributos** con los mapeados que aparecen en la tabla de la página de **configuración del aprovisionamiento SCIM**.

## Paso 2: Asignar usuarios a la aplicación

1. Selecciona la pestaña **Asignar**.
2. Selecciona **Asignar** y elige una opción.
3. Asigna la aplicación a las personas que deben tener acceso a Braze.
4. Selecciona **Hecho** cuando hayas completado la asignación.

{% endtab %}
{% tab Okta - Custom app integration %}

{% alert important %}
La integración de Okta se encuentra actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en el acceso anticipado.
{% endalert %}

## Paso 1: Configurar el aprovisionamiento SCIM

### Paso 1.1: Habilitar SCIM

1. En Okta, ve a tu aplicación Braze.
2. Selecciona la pestaña **General**.
3. En la sección **Configuración de la aplicación**, selecciona **Editar**.
4. En el campo **Aprovisionamiento**, selecciona **SCIM**.
5. Seleccione **Guardar**.

### Paso 1.2: Configurar la integración SCIM

1. Selecciona la pestaña **Aprovisionamiento**.
2. En **Configuración** > **Integración** > **Conexión SCIM**, selecciona **Editar** y rellena los valores de los campos que aparecen en la tabla de la página **Configurar aprovisionamiento SCIM**.
3. Prueba las credenciales de la API seleccionando **Probar credenciales de la API**.
4. Seleccione **Guardar**.

### Paso 1.3: Habilitar el aprovisionamiento a la aplicación

1. En **Aprovisionamiento** > **Configuración** > **A la aplicación** > **Aprovisionamiento a la aplicación**, selecciona **Editar**.
2. Habilita lo siguiente:
    - Crear usuarios
    - Actualizar atributos de usuarios
    - Desactivar usuarios
3. Revisa y configura la sección de mapeado **de atributos** con los mapeados que aparecen en la tabla de la página de **configuración del aprovisionamiento SCIM**.

## Paso 2: Asignar usuarios a la aplicación

1. Selecciona la pestaña **Asignar**.
2. Selecciona **Asignar** y elige una opción.
3. Asigna la aplicación a las personas que deben tener acceso a Braze.
4. Selecciona **Hecho**.

{% endtab %}
{% tab Entra ID %}

{% alert important %}
La integración de Entra ID está actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en el acceso anticipado.
{% endalert %}

## Paso 1: Configurar la aplicación de aprovisionamiento SCIM

### Paso 1.1. Accede al centro de administración de Microsoft Entra
Accede a tu centro de administración de Microsoft Entra.

### Paso 1.2: Crea y configura tu aplicación SCIM

1. En el menú de navegación, ve a **Entra ID** > **Aplicaciones de empresa**.
2. Selecciona **Nueva aplicación**.
3. Selecciona **Crear tu propia aplicación**.
4. En el panel, introduce un nombre para tu aplicación.
5. En la sección **¿Qué quieres hacer con tu aplicación?**, selecciona **Integrar aplicación que no encuentras en la galería (No galería)**.
6. Seleccione **Crear**.

### Paso 1.3: Configurar la integración SCIM

1. Ve a la sección **Gestionar** > **Aprovisionamiento** de tu aplicación SCIM.
2. Selecciona **Conecta tu aplicación** o **Nueva configuración** y rellena los valores de los campos que aparecen en la tabla de la página de **configuración del aprovisionamiento SCIM**.

### Paso 1.4: Habilitar el aprovisionamiento a la aplicación

1. Ve a la sección **Gestionar** > **Mapeado de atributos (vista previa)** de tu aplicación SCIM.
2. Selecciona **Aprovisionar usuarios de Microsoft Entra ID**.
3. Revisa y configura la sección **Mapeado de atributos** para que coincida con los atributos que aparecen en la tabla de la página de **configuración del aprovisionamiento SCIM**.
4. Cierra la página de **mapeado de atributos**.

## Paso 2: Asignar usuarios a la aplicación

1. Ve a **Administrar** > **Usuarios y Grupos**.
2. Selecciona **Añadir usuario/grupo**.
3. Selecciona **Ninguno seleccionado** para asignar usuarios a la aplicación.
4. Selecciona el botón **Seleccionar** para confirmar la asignación.

{% endtab %}
{% tab Custom %}

## Paso 1: Configura tus ajustes SCIM

- **Espacio de trabajo predeterminado:** Selecciona el espacio de trabajo en el que deben añadirse por defecto los nuevos usuarios. Si no especificas un espacio de trabajo en tu [solicitud de API SCIM]({{site.baseurl}}/post_create_user_account/), Braze asigna usuarios a este espacio de trabajo.
- **Origen del servicio:** Introduce el dominio de origen de tus peticiones SCIM. Braze lo utiliza en el encabezado `X-Request-Origin` para verificar de dónde proceden las solicitudes.
- **Lista de IP permitidas (opcional):** Puedes restringir las peticiones SCIM a determinadas direcciones IP. Introduce una lista o rango de direcciones IP separadas por comas para permitirlas. El encabezado `X-Request-Origin` de cada solicitud se utiliza para comprobar la dirección IP de la solicitud con la lista permitida.

![Formulario de configuración del aprovisionamiento SCIM con tres campos: Espacio de trabajo predeterminado, origen del servicio y lista opcional de IP permitidas. El botón "Generar token SCIM" está desactivado.]({% image_buster /assets/img/scim_unfilled.png %})

## Paso 2: Generar un token SCIM

Tras rellenar los campos obligatorios, pulsa **Generar to** ken SCIM para generar un token SCIM y ver tu punto final de API SCIM. Asegúrate de copiar el token SCIM antes de salir navegando. **Este token sólo aparece una vez.** 

![Los campos Punto final de la API SCIM y Token SCIM se muestran con valores enmascarados y botones de copia. Debajo del campo token hay un botón "Restablecer token".]({% image_buster /assets/img/scim.png %})

Braze espera que todas las solicitudes SCIM contengan el token de portador de la API SCIM adjunto mediante un encabezado HTTP `Authorization`.

{% endtab %}
{% endtabs %}
