---
nav_title: Crowdin
article_title: Crowdin
description: "Este artículo de referencia describe la asociación entre Braze y Crowdin, una plataforma de software basada en la nube que te permite automatizar la traducción de tus plantillas de correo electrónico y bloques de contenido en Braze."
alias: /partners/crowdin/
page_type: partner
search_tag: Partner

---

# Crowdin

> Crowdin es un software basado en la nube para la gestión de la localización. Con Crowdin, puedes traducir tus aplicaciones para Android e iOS, tu sitio web, las capturas de pantalla de tu tienda y otros contenidos. La traducción puede realizarse a través de tu equipo interno, de una agencia de traducción o utilizando máquinas de traducción automática.

_Esta integración está mantenida por Crowdin._

## Sobre la integración

La integración de Braze y Crowdin te permite traducir plantillas de correo electrónico y bloques de contenido. También puedes sincronizar el contenido de tu cuenta de Braze con tu proyecto de Crowdin y volver a añadir traducciones a Braze.

## Requisitos previos

| Requisito| Descripción|
| ---| ---|
| Cuenta Crowdin | Se necesita una [cuenta Crowdin](https://accounts.crowdin.com/register) para beneficiarse de esta asociación. |
| Proyecto de traducción de Crowdin | Para conectar tu cuenta Braze con Crowdin o Crowdin Enterprise, primero tendrás que registrarte y crear un proyecto de traducción. |
| Clave de API REST de Braze | Una clave Braze REST API con todos los permisos de plantillas y Bloques de contenido. <br><br> Puede crearse en el dashboard de Braze desde **Configuración** > **Claves API**. |
| Punto final SDK de Braze | La URL de tu punto final SDK dependerá de la URL Braze de [tu instancia]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integración

### Paso 1: Configura la aplicación Braze en Crowdin/Crowdin Enterprise

#### Crowdin
Para configurar la aplicación Braze en Crowdin, sigue estos pasos:

1. Ve a la [aplicación Braze en el mercado](https://store.crowdin.com/braze-app).
2. Haz clic en **Instalar** para añadirlo a tu cuenta.
3. Abre el proyecto que creaste para la localización de tu contenido Braze.
4. Ve a **Configuración > pestaña Integraciones.** 
5. En la sección **Aplicaciones**, haz clic en la aplicación Braze.
6. En el cuadro de diálogo, proporciona tus credenciales Braze (clave de API REST de Braze y punto final SDK de Braze).
7. Haz clic en **Iniciar sesión con el conector Braze**. 

#### Crowdin Enterprise
Para configurar la aplicación Braze en Crowdin Enterprise, sigue estos pasos:

1. Ve a la página de inicio **del espacio de trabajo** > **Marketplace**.
2. Haz clic en **Instalar** en la aplicación Braze para añadirla a tu organización.
3. Abre el proyecto que creaste para la localización de tu contenido Braze.
4. Ve a **Aplicaciones > Personalizadas.**
5. Haz clic en la aplicación Braze.
6. En el cuadro de diálogo, proporciona tus credenciales Braze (clave de API REST de Braze y punto final SDK de Braze).
7. Haz clic en **Iniciar sesión con el conector Braze**.

### Paso 2: Añade tu contenido a Crowdin/Crowdin Enterprise

Una vez que proporciones tus credenciales de Braze, verás dos paneles. Selecciona el contenido deseado para sincronizar los archivos de traducción desde tu cuenta Braze y haz clic en **Sincronizar con Crowdin**.

En el modo Editor de Crowdin, el contenido sincronizado desde tu cuenta Braze puede mostrarse a tus traductores como una lista de cadenas o como una vista previa del archivo.

![Una imagen del aspecto del compositor de correo electrónico Crowdin Editor con algunas traducciones básicas añadidas.]({% image_buster /assets/img/crowdin/crowdin_editor_email_preview.png %})

### Paso 3: Añade traducciones a Braze

En cuanto las traducciones estén completas, abre la aplicación Braze en Crowdin, selecciona los archivos traducidos (para cada archivo, puedes elegir todos los idiomas de destino o sólo algunos específicos) en el panel izquierdo, y haz clic en **Sincronizar con Braze**.

![Una imagen de un usuario seleccionando sus archivos de traducción y sincronizándolos con Braze.]({% image_buster /assets/img/crowdin/sync_translations.png %})


