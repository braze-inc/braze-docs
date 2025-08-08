---
nav_title: Aprovisionamiento justo a tiempo SAML
article_title: Aprovisionamiento justo a tiempo SAML
page_order: 1
page_type: tutorial
description: "Este artículo le mostrará cómo configurar el aprovisionamiento justo a tiempo SAML para permitir que los nuevos usuarios del panel creen una cuenta Braze en su primer inicio de sesión." 

---

# Aprovisionamiento justo a tiempo SAML 

> El aprovisionamiento justo a tiempo funciona con [SAML SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/) para permitir que los nuevos usuarios del panel creen una cuenta Braze en su primer inicio de sesión. Esto elimina la necesidad de que los administradores creen manualmente una cuenta para un nuevo usuario del cuadro de mandos, elijan sus permisos, lo asignen a un espacio de trabajo y esperen a que active su cuenta.

## Requisitos previos

Esta característica requiere que SAML SSO esté configurado e integrado, y no es compatible con Google SSO.

## Configuración del aprovisionamiento justo a tiempo SAML

Haz que un administrador de Braze haga lo siguiente:

1. Vaya a **Configuración** > **Configuración de seguridad**.
2. En la sección **SAML SSO**, active la opción **Aprovisionamiento automático de usuarios**.
3. Seleccione un espacio de trabajo predeterminado para añadir un nuevo usuario del cuadro de mandos.
4. Seleccione el conjunto de permisos predeterminado que se asignará a ese nuevo usuario del cuadro de mandos. Para saber cómo crear un conjunto de permisos, consulte [Configuración de permisos de usuario]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/).
6. Seleccione **Guardar cambios** en la parte inferior de la página
7. En la configuración de su proveedor de SSO, añada todos los usuarios que necesiten acceso Braze al directorio de su proveedor de SSO.
8. Ahora los usuarios pueden registrarse o iniciar sesión.
