---
nav_title: Storyly
article_title: Storyly
description: "Este artículo de referencia describe la asociación entre Braze y Storyly, un SDK ligero, que permite a los propietarios de aplicaciones orientar sus segmentos y alimentar Braze con más datos propios."
alias: /partners/storyly/
page_type: partner
search_tag: Partner

---

# Storyly

> [Storyly](https://www.storyly.io/) es un SDK ligero que lleva historias a tu aplicación o sitio web. Con un estudio de diseño intuitivo, un análisis profundo y una conectividad perfecta, Storyly es una potente herramienta para enriquecer la experiencia de la audiencia. 

_Esta integración está mantenida por Storyly._

## Sobre la integración

La integración de Braze y Storyly te permite utilizar tus segmentos en Braze como audiencia en la plataforma Storyly. Con esta integración, puedes:
- Dirigirte a tus segmentos con historias específicas
- Utilizar los atributos del usuario para personalizar el contenido de tu historia

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Storyly | Se necesita una cuenta de Storyly para beneficiarse de esta asociación. |
| SDK de Storyly | Debes instalar el [SDK de Storyly](https://integration.storyly.io/). |
| Clave de API REST de Braze | Una clave de API REST Braze con los siguientes permisos <br><br> `users.export.ids`<br> `users.export.segments`<br> `segments.list`<br> `segments.details` <br><br> Puede crearse en el dashboard de Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze | [La URL de tu punto final REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto final dependerá de la URL Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos prácticos

Con la integración de Braze y Storyly, los propietarios de aplicaciones pueden mostrar historias a todos los segmentos en Braze y personalizar las historias con atributos de usuario.

Algunos casos de uso comunes son:

__Segmentos objetivo de Braze en Storyly__<br>Una vez finalizada la integración, puedes crear una audiencia Storyly basada en tus segmentos Braze. Puede tratarse de un segmento demográfico o de comportamiento. Por ejemplo, dirígete a los usuarios que viven en una ubicación concreta, a los que realizan una acción específica en tu aplicación o a los interesados en productos concretos con historias específicas para aumentar la conversión.<br>
__Historias personalizadas con atributos de usuario__<br>Los atributos de usuario de Braze también se pueden utilizar en Storyly para generar historias dinámicas. Esto podría incluir el nombre de un usuario, los productos de una cesta o incluso los productos favoritos, proporcionando a los usuarios historias personalizadas únicas. La personalización ayuda a aumentar las tasas de conversión de las historias y la tasa de interacción general.

## Integración de exportación de datos

La integración Braze Storyly se explica en el siguiente video:

{% multi_lang_include video.html id="3-OEqQs48Zw" source="youtube" %}

Asegúrate de que tu integración con Storyly contiene parámetros personalizados. Estos parámetros coincidirán con la propiedad de usuario de Braze `external id`. Aquí se explica la implementación de parámetros personalizados para [iOS](https://integration.storyly.io/ios/personalization-customaudience.html), [Android](https://integration.storyly.io/android/personalization-customaudience.html), [React Native](https://integration.storyly.io/react-native/personalization-customaudience.html), [Flutter](https://integration.storyly.io/flutter/personalization-customaudience.html) y [Web](https://integration.storyly.io/web/personalization-customaudience.html).

También puedes consultar la documentación [de Storyly](https://docs.storyly.io/page/connect-your-braze-audiences-with-storyly) para obtener más información.

### Paso 1: Configura la integración en el panel de Storyly

Crea una integración en **el panel de Storyly > Configuración > Integraciones > Conectar con Braze**. Aquí necesitarás tu clave de API REST de Braze y tu punto final REST de Braze. 

### Paso 2: Obtén tus segmentos 

A continuación, puedes utilizar segmentos Braze para crear una audiencia Storyly. Se puede crear en **el panel de Storyly > Configuración > Audiencias > Nueva audiencia > Crear audiencia con Braze**.

Aquí, habrá dos opciones de sincronización. Selecciona **Sincronización única** para historias de campaña específicas, o **Sincronización diaria** para historias de larga duración.


