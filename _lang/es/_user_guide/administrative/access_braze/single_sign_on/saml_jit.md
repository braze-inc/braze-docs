---
nav_title: Aprovisionamiento SAML justo a tiempo
article_title: Aprovisionamiento justo a tiempo SAML
page_order: 1
page_type: tutorial
description: "Este artículo te guiará a través del proceso de configuración del aprovisionamiento SAML justo a tiempo para permitir que los nuevos usuarios de la empresa creen una cuenta Braze la primera vez que inicien sesión." 

---

# Aprovisionamiento justo a tiempo SAML 

> El aprovisionamiento justo a tiempo funciona con [SAML SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/) para permitir que los nuevos usuarios de la empresa creen una cuenta de Braze la primera vez que inician sesión. Esto elimina la necesidad de que los administradores creen manualmente una cuenta para un nuevo usuario de la empresa, elijan sus permisos, los asignen a un espacio de trabajo y esperen a que activen su cuenta.

Como medida de seguridad, el aprovisionamiento justo a tiempo (JITP) de SAML solo funciona para usuarios con dominios de correo electrónico que ya existen en tu empresa. El JITP solo es posible para dominios en los que ya haya al menos un desarrollador confirmado y que no sea un suplantador de identidad en la empresa. 

Por ejemplo, supongamos que la cuenta```jon.smith@decorumsoft.com```puede utilizar JITP para iniciar sesión en Decorumsoft. La cuenta```jane.smith@decorumsoft.com```tiene el mismo dominio y también se te puede permitir el aprovisionamiento. Sin embargo, si intentas utilizar JITP con ```jon.smith@decorumsoft.eu```, no se permitirá el aprovisionamiento porque no hay una```decorumsoft.eu```cuenta  en el panel de Braze de Decorumsoft. 

Para solicitar una excepción para una empresa, ponte en contacto con [el servicio de asistencia]({{site.baseurl}}/braze_support/).

## Requisitos previos

SAML JITP requiere que SAML SSO esté configurado e integrado. No es compatible con Google SSO y solo es compatible con flujos de trabajo para iniciar sesión iniciados por el proveedor de identidad (IdP).

## Configuración del aprovisionamiento justo a tiempo (JITP) de SAML

Haz que un administrador de Braze haga lo siguiente:

1. Ve a **Configuración** > **Configuración administrativa** > **Configuración de seguridad**.
2. En la sección **SAML SSO**, active la opción **Aprovisionamiento automático de usuarios**.
3. Selecciona un espacio de trabajo predeterminado para añadir un nuevo usuario de la empresa.
4. Selecciona el conjunto de permisos predeterminado que se asignará a ese nuevo usuario de la empresa. Para saber cómo crear un conjunto de permisos, consulte [Configuración de permisos de usuario]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/).
6. Seleccione **Guardar cambios** en la parte inferior de la página
7. En la configuración de su proveedor de SSO, añada todos los usuarios que necesiten acceso Braze al directorio de su proveedor de SSO.
8. Indica a los usuarios que accedan a Braze a través de tu portal IdP para iniciar sesión por primera vez. Después de esto, aparecerá el botón de inicio de sesión único SAML para futuros inicios de sesión.

## Preguntas más frecuentes

### ¿Cómo desactivas SAML JITP?

Después de configurar JITP, debes [ponerte en contacto con el servicio de asistencia técnica]({{site.baseurl}}/braze_support/) para que lo desactiven.

## Solución de problemas

### El botón de inicio de sesión único no aparece con Microsoft Entra ID.

El campo **URL de** **inicio de sesión** del formulario **de configuración SAML básica** de Microsoft Entra para Braze puede hacer que los usuarios solo vean una opción de contraseña, en lugar de un botón de inicio de sesión único (SSO), con el inicio de sesión iniciado por el proveedor de identidad (IdP). Para evitar este problema, deja el campo **URL de inicio de sesión** en blanco al configurar Braze en tu centro de administración de Microsoft Entra.