---
nav_title: "Amor por correo electrónico"
article_title: Amor por correo electrónico
description: "Aprende a integrar Braze con Email Love, un complemento de Figma que te habilita para diseñar y exportar correos electrónicos HTML receptivos y accesibles directamente desde Figma."
alias: /partners/email_love/
page_type: partner
search_tag: Partner

---

# Amor por correo electrónico

> [Email Love](https://emaillove.com/) es un complemento de Figma que te permite diseñar y exportar correos electrónicos HTML receptivos y accesibles directamente desde Figma. La característica Exportar a Braze de Email Love utiliza la API de Braze para cargar fácilmente tus plantillas de correo electrónico a Braze.

## Requisitos previos

| Requisito            | Descripción                                                      |
|------------------------|------------------------------------------------------------------|
| **Cuenta de correo electrónico Love** | Se necesita una cuenta de Email Love para beneficiarse de esta asociación. |
| **Clave de API REST de Braze** | Una clave de API REST Braze con el permiso completo `Templates` habilitado. Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

## Utilizar Email Love con Braze

### Paso 1: Ejecuta el plugin

Para diseñar tu plantilla de correo electrónico, primero tendrás que cargar el plugin. Para obtener instrucciones más detalladas, consulta la documentación de Email Love para [subir tu correo electrónico a Braze](https://help.emaillove.com/exporting-an-email-design/6rcR6LPWq6BoYseKZf41nS/uploading-your-email-to-braze-/3ZcmGaGz6a8azeZQxWgKzm).

### Paso 2: Crea tu primer marco

En el plugin, selecciona el botón **[+ Sin plantilla seleccionada]** para crear un nuevo marco para el diseño de tu correo electrónico.

### Paso 3: Diseña la plantilla con los componentes preconstruidos de Email Love

Selecciona el marco que has creado y empieza a añadir componentes (cabeceras, bloques de contenido, CTA y pies de página) de la biblioteca **de Activos** del plugin para estructurar tu correo electrónico.

![Componentes preconstruidos de Email Love.]({% image_buster /assets/img/email_love/emaillove1_content.png %})

### Paso 4: Personaliza los componentes

Modifica los componentes utilizando las herramientas de Figma para ajustar el texto, las imágenes, los colores y los elementos de diseño para alinear el diseño de la plantilla con tu marca. Si añades un componente de pie de página, al exportar se incluirá automáticamente un enlace Braze para cancelar suscripción.

![Personaliza los componentes en Figma.]({% image_buster /assets/img/email_love/emaillove2_components.png %})

### Paso 5: Exporta tu plantilla de correo electrónico a Braze

1. Cuando hayas terminado, selecciona el fotograma que quieras exportar. Ten en cuenta que tendrás que utilizar un pie de página de Email Love que contenga un enlace para cancelar suscripción para que la exportación funcione.
2. Selecciona el botón **Exportar** en el plugin y selecciona **Braze** en el menú desplegable.
3. Copia y pega tu clave de API en la casilla **Clave de API de Braze** dentro del plugin Email Love Figma.
4. Selecciona el botón **Establecer clave de API**.
5. Selecciona **Cambiar ID de instancia** y, a continuación, selecciona el ID de tu instancia de Braze.

![Exportar una plantilla a Braze desde el plugin Email Love.]({% image_buster /assets/img/email_love/emaillove3_exportbraze.png %}){: style="max-width:50%;"}

### Paso 6: Edita tu correo electrónico en Braze

En Braze, ve a **Plantillas** > **Editar plantillas** > **Editar mensaje**. Dentro del editor de plantillas, puedes editar el HTML de tu correo electrónico o utilizar el **editor de texto enriquecido** de la pestaña **Clásico**.

## Asistencia y solución de problemas

Para obtener instrucciones más detalladas, consulta la documentación de Email Love sobre la [exportación de un diseño de correo electrónico](https://help.emaillove.com/exporting-an-email-design/6rcR6LPWq6BoYseKZf41nS/uploading-your-email-to-braze-/3ZcmGaGz6a8azeZQxWgKzm). Para obtener más ayuda, ponte en contacto con el equipo de soporte de Email Love.
