---
nav_title: Digioh
article_title: Digioh
description: "Este artículo de referencia describe la asociación entre Braze y Digioh, una plataforma de encuestas para crear ventanas emergentes, formularios, encuestas y centros de preferencias de comunicación que impulsan la interacción a través de tus campañas Braze."
alias: /partners/digioh/
page_type: partner
search_tag: Partner

---

# Digioh

> [Digioh](https://www.digioh.com/) apoya el crecimiento de la lista, la captura de datos propios y el uso de esos datos en las campañas de Braze.

_Esta integración está mantenida por Digioh._

## Sobre la integración

La integración de Braze y Digioh te permite utilizar un constructor de arrastrar y soltar para crear formularios de marca, ventanas emergentes, centros de preferencias, páginas de destino y cuestionarios que te conecten con tus clientes. Digioh te ayuda a configurar la integración y puede crear, diseñar y lanzar tu primera campaña.

!["Crea centros de preferencias de correo electrónico y comunicaciones flexibles con Digioh"]({% image_buster /assets/img/digioh/pref_pop_examples.png %}){: style="border:0"}

## Requisitos previos

| Requisito | Descripción |
|---|---|
|Cuenta Digioh | Se necesita una [cuenta Digioh](https://www.digioh.com/) para beneficiarse de esta asociación. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br> Puede crearse en el dashboard de Braze desde **Configuración** > **Claves API**. |
| Punto final de la API Braze `/users/track/`  | La URL de tu punto final REST con los detalles de `/users/track/` añadidos. Tu punto final dependerá de la [URL Braze de tu instancia]({{site.baseurl}}/api/basics/#endpoints).<br><br>Por ejemplo, si tu punto final de la API REST es `https://rest.iad-01.braze.com`, tu punto final de `/users/track/` será `https://rest.iad-01.braze.com/users/track/`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integración 

Para integrar Digioh, primero debes configurar el conector Braze. Una vez completado, tendrás que aplicar la integración a un lightbox (widget). Visita [Digioh](https://help.digioh.com/knowledgebase/digioh-integration-basics/) para leer más sobre los fundamentos de la integración.

### Paso 1: Crear integración Digioh 

En Digioh, haz clic en la pestaña **Integraciones** y luego en el botón **Nueva integración**. Selecciona **Braze** en el desplegable **Integración** y dale un nombre a la integración. 

!["Selecciona la integración correcta en el desplegable"]({% image_buster /assets/img/digioh/2.png %}){: style="max-width:50%;"}

A continuación, introduce la clave de API REST de Braze y tu punto final de API Braze `/users/track/`. 

Por último, utiliza la sección de mapeado de campos para mapear campos personalizados adicionales más allá del correo electrónico y el nombre. El siguiente fragmento de código muestra un ejemplo de carga útil. Cuando hayas terminado, selecciona **Crear integración**.

```json
{
    "attributes" : [
         {
           "external_id": "[EMAIL_MD5]",
           "email" : "[EMAIL]"
         }
     ]
}
```

### Paso 2: Crear una caja de luz Digioh

Utiliza el [editor de diseño de](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/) Digioh para crear una caja de luz (widget). <br>
¿Te interesa ver una galería de formas de aprovechar el editor de diseño? Visita la [galería de temas de](https://www.digioh.com/theme-gallery) Digioh.

### Paso 3: Aplicar integración

Para aplicar esta integración a una [caja de luz](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/) de Digioh, ve a la página **Cajas** y selecciona el enlace **Añadir** o **Editar** en la columna **Integraciones**. También puede añadirse desde la sección **Integración** del editor.

!["Añadir la integración a un lightbox"]({% image_buster /assets/img/digioh/3.png %}){: style="max-width:90%"}

Aquí, selecciona **Añadir integración**, elige la integración que desees y **Guardar**. Digioh pasará ahora tus clientes potenciales captados a Braze en tiempo real.


