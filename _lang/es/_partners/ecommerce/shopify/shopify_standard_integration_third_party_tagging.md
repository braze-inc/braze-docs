---
nav_title: Integración estándar de Shopify con etiquetado de terceros
article_title: "Integración estándar de Shopify con etiquetado de terceros"
description: "Este artículo de referencia describe cómo configurar la integración estándar de Shopify con una herramienta de etiquetado de terceros."
page_type: partner
search_tag: Partner
alias: /shopify_standard_integration_third_party_tagging/
page_order: 2
---

# Integración estándar de Shopify con herramienta de etiquetado de terceros

> Esta página te guía a través del uso de herramientas de terceros, como Google Tag Manager, con la [integración estándar de Shopify]({{site.baseurl}}/shopify_standard_integration/) para inicializar y cargar el SDK de la Web de Braze.

Para las tiendas online de Shopify, recomendamos utilizar el método de integración estándar de Braze para admitir los SDK de Braze en tu sitio. Sin embargo, entendemos que prefieras utilizar una herramienta de terceros, como Google Tag Manager. Si decides utilizar una herramienta de terceros con el conector de Shopify de Braze, ten en cuenta que la integración de Braze y la incrustación de la aplicación gestionarán el SDK durante el proceso de pago.

## Requisitos

- **Clave de API coherente entre tu herramienta de terceros y el conector de Shopify:** La clave de API debe ser coherente tanto en Braze como en tu herramienta de terceros. Esto evita la creación de usuarios duplicados y mantiene la compatibilidad entre SDKs. 
  - **Ubicación de la clave de API:** Tras la incorporación de la ruta de integración estándar, la integración creará automáticamente una aplicación Web Braze llamada "Shopify". Recupera la clave de API dentro de la integración que se utiliza con la configuración de tu herramienta de terceros. 
- **Versiones SDK consistentes entre tu herramienta de terceros y el conector de Shopify:** La versión del SDK debe ser `5.4` dentro de tu herramienta de terceros. Utilizar un número de versión incorrecto puede causar problemas de incompatibilidad, ya que algunos métodos del SDK pueden no existir en versiones anteriores.
- **Tiempo de inicialización del SDK coherente:** Dentro de la configuración de integración estándar de Shopify, puedes seleccionar los SDK que se deben inicializar al iniciar la sesión o al iniciar sesión en la cuenta. Esta configuración debe ser coherente entre tu herramienta de terceros y Braze. Las incoherencias podrían provocar problemas posteriores para el usuario y la sincronización de datos. 

{% alert note %}
Recomendamos utilizar exclusivamente el método de integración estándar en lugar de utilizarlo junto con administradores de etiquetas de terceros, lo que puede causar conflictos entre el SDK de Braze y las herramientas de terceros. Si utilizas una herramienta de terceros, haz pruebas para confirmar que todo funciona como se espera.
{% endalert %}

## Configuración de la integración con una herramienta de terceros

Apartarse de los pasos indicados puede provocar problemas inesperados, así que asegúrate de seguirlos al pie de la letra.

1. Sigue los pasos indicados en la [configuración de la integración estándar de Shopify]({{site.baseurl}}/shopify_standard_integration/). Al [habilitar los SDK Braz]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration/#step-2-enable-braze-web-sdks)e Web, marca la casilla que indica que estás utilizando una herramienta de terceros para añadir el SDK Braze Web a tu sitio de Shopify.

![Sección "Configuración del SDK de Braze" con una casilla de verificación para indicar que vas a utilizar una herramienta de terceros para añadir el SDK Web de Braze.]({% image_buster /assets/img/Shopify/third_party_enable.png %}){: style="max-width:80%;"}

{: start="2"}
2\. Ve a **Configuración** > **Configuración de la aplicación**, selecciona la aplicación web **de Shopify** y, a continuación, copia la **clave de API para Shopify en la Web**.
3\. Pega la clave de API en la configuración web del SDK de tu herramienta de terceros y establece la versión del SDK en `5.4`.

## Captura de datos de Shopify y sincronización de usuarios

Siempre que el SDK Web sea accesible en el front-end de tu sitio Shopify a través de una herramienta de terceros, la integración estándar capturará los datos de Shopify y sincronizará a los usuarios como se espera.

## Consideraciones y descargos de responsabilidad

- **Configuración de inicialización:** Si modificas la configuración de inicialización a través de tu herramienta de terceros, la sincronización de usuarios y datos puede verse afectada. Por ejemplo, si decides inicializar tu SDK cuando se acepte un formulario de consentimiento de cookies, Braze no recibirá seguimiento de usuarios anónimos ni datos hasta que el usuario dé su consentimiento. 
- **No es posible configurar los atributos directamente a través de `dataLayer`:** Utiliza `window.braze` en lugar de `dataLayer` para establecer atributos.
- **Usuarios potenciales duplicados:** Si la clave de API no coincide entre Braze y tu herramienta de terceros, pueden crearse usuarios duplicados.
- **Incompatibilidad SDK:** Utilizar un número de versión incorrecto puede causar problemas con los métodos del SDK.