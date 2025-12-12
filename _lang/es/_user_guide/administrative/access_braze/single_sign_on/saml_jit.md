---
nav_title: Aprovisionamiento SAML Just-in-Time
article_title: Aprovisionamiento justo a tiempo SAML
page_order: 1
page_type: tutorial
description: "Este artículo te explicará cómo configurar el aprovisionamiento justo a tiempo SAML para que los nuevos usuarios del panel puedan crear una cuenta Braze en su primer inicio de sesión." 

---

# Aprovisionamiento justo a tiempo SAML 

> El aprovisionamiento justo a tiempo funciona con [SAML SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/) para permitir a los nuevos usuarios del panel crear una cuenta Braze en su primer inicio de sesión. Esto elimina la necesidad de que los administradores creen manualmente una cuenta para un nuevo usuario del panel, elijan sus permisos, le asignen un espacio de trabajo y esperen a que active su cuenta.

Como medida de seguridad, el aprovisionamiento justo a tiempo (JITP) de SAML sólo funciona para usuarios con dominios de correo electrónico que ya existan en tu empresa. La JITP sólo es posible para dominios en los que ya haya al menos un desarrollador confirmado, no suplantación de identidad, en la empresa. 

Por ejemplo, digamos que la cuenta ```jon.smith@decorumsoft.com``` puede utilizar JITP para iniciar sesión en Decorumsoft. La cuenta ```jane.smith@decorumsoft.com``` tiene el mismo dominio y también se le puede permitir el aprovisionamiento. Sin embargo, si intentas utilizar JITP con ```jon.smith@decorumsoft.eu```, no se permitirá el aprovisionamiento porque no hay una cuenta ```decorumsoft.eu``` en el panel Braze de Decorumsoft. 

Para hacer una excepción para una empresa, ponte en contacto con [Soporte]({{site.baseurl}}/braze_support/).

## Requisitos previos

SAML JITP requiere que SAML SSO esté configurado e integrado. No es compatible con Google SSO, y sólo se admite para los flujos de trabajo de iniciar sesión iniciados por el proveedor de identidad (IdP-initiated).

## Configuración del aprovisionamiento justo a tiempo (JITP) de SAML

Haz que un administrador de Braze haga lo siguiente:

1. Ve a **Configuración** > **Configuración de administración** > **Configuración de seguridad**.
2. En la sección **SAML SSO**, alterna la opción **Aprovisionamiento automático de usuarios**.
3. Selecciona un espacio de trabajo predeterminado para añadir un nuevo usuario al panel.
4. Selecciona el conjunto de permisos predeterminado para asignar a ese nuevo usuario del panel. Para saber cómo crear un conjunto de permisos, consulta [Configurar los permisos de usuario]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/).
6. Selecciona **Guardar cambios** en la parte inferior de la página
7. En la configuración de tu proveedor de SSO, añade todos los usuarios que necesiten acceso a Braze al directorio de tu proveedor de SSO.
8. Ahora los usuarios pueden registrarse o iniciar sesión.

## Preguntas más frecuentes

### ¿Cómo desactivo SAML JITP?

Después de configurar JITP, debes [ponerte en contacto con el servicio de asistencia]({{site.baseurl}}/braze_support/) para que lo desactiven.

## Solución de problemas

### El botón de firma única no aparece con Microsoft Entra ID

El campo **URL de inicio de sesión** en el formulario de **Configuración SAML básica** de Microsoft Entra para Braze puede hacer que los usuarios sólo vean una opción de contraseña, y no un botón SSO, con inicio de sesión iniciado por IdP. Para evitar este problema, deja en blanco el campo **URL de inicio de sesión** al configurar Braze en tu centro de administración de Microsoft Entra.