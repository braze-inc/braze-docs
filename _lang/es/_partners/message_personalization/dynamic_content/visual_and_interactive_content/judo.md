---
nav_title: Judo
article_title: Judo
description: "Este artículo de referencia describe la asociación entre Braze y Judo, una plataforma de interfaz de usuario sin código basada en servidor que le permite añadir contexto y seguimiento de ubicación a sus aplicaciones para iOS y Android."
alias: /partners/judo/
page_type: partner
search_tag: Partner

---

# Judo

> [Judo](https://judo.app) es una plataforma de interfaz de usuario basada en servidor que permite a los editores ofrecer experiencias de usuario enriquecidas y atractivas dentro de la aplicación sin necesidad de actualizarla.

_Esta integración la mantiene Judo._

## Sobre la integración

La integración de Braze y Judo proporciona experiencias a medida en sus campañas y lienzos. En lugar de una experiencia de página de destino sencilla y con plantillas, una campaña Braze puede incorporar contenido que incluya varias pantallas, modales, vídeo, fuentes personalizadas y ajustes de compatibilidad, como el modo oscuro y la accesibilidad, creados sin código y desplegados sin actualizaciones de la aplicación. Los datos de Braze también pueden utilizarse para apoyar el contenido personalizado en una Experiencia Judo. Los eventos del usuario y los datos de la experiencia pueden retroalimentarse a Braze para la atribución y la orientación.

## Requisitos previos

| Requisito | Descripción |
|---|---|
| Cuenta de Judo | Se necesita una cuenta [Judo](https://www.judo.app/) para beneficiarse de esta asociación. |
| Judo SDK | El SDK de Judo debe integrarse en tus aplicaciones [iOS](https://github.com/judoapp/judo-ios/) y/o [Android](https://github.com/judoapp/judo-android). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos prácticos

**Incorporación**: Los editores de aplicaciones que utilizan Judo construyen y despliegan experiencias de incorporación nativas y enriquecidas. Estas experiencias pueden ser ahora uno de los elementos de un proceso de incorporación multicanal personalizado coordinado a través de Braze. Las experiencias pueden personalizarse y actualizarse rápidamente sin necesidad de actualizar la aplicación para probar la eficacia de diferentes flujos dentro de la aplicación.

**Conversión**: Los editores de aplicaciones pueden utilizar los datos de Braze para crear una experiencia rica y personalizada dentro de la aplicación para impulsar las compras dentro de la aplicación, las suscripciones de pago o la comercialización contextual utilizando los ganchos de integración en Judo. El acceso a estas experiencias puede activarse a través de campañas de marketing de compromiso creadas en Braze.

**Contenido basado en eventos**: Una de las principales aplicaciones del judo en los deportes y el entretenimiento es la creación de experiencias enriquecedoras que sirvan de preestreno, promoción y recapitulación de acontecimientos. Esta capacidad tiene amplias aplicaciones en otros verticales para contenidos estacionales y basados en noticias. Vincular mensajes para promocionar o destacar eventos de manera oportuna con experiencias enriquecidas dentro de la aplicación permite a los editores impulsar la participación siendo contextualmente relevantes.

## Integración de SDK en paralelo

Judo ofrece bibliotecas adicionales que automatizan parte del esfuerzo necesario para integrar los SDK de Judo y Braze en sus aplicaciones móviles. 

### Paso 1: Instalar la biblioteca de integración Judo-Braze

Instala y configura la biblioteca de integración Judo-Braze en tus aplicaciones. Esto activará automáticamente el seguimiento de eventos.

- [Instalación en iOS
instrucciones](https://github.com/judoapp/judo-braze-ios/wiki#installation)
- [Instalación en Android
instrucciones](https://github.com/judoapp/judo-braze-android/wiki#installation).

### Paso 2: Configurar la mensajería integrada en la aplicación

Este paso consistirá en crear implementaciones personalizadas de `ABKInAppMessageControllerDelegate` y `IInAppMessageManagerListener` para iOS y Android.

Consulte la documentación de configuración de mensajes incluida en la aplicación para cada una de las bibliotecas de integración:

- [Mensajería en la aplicación de iOS
Configurar](https://github.com/judoapp/judo-braze-ios/wiki#in-app-messaging-setup)
- [Mensajería dentro de la aplicación Android
Configurar](https://github.com/judoapp/judo-braze-android/wiki#in-app-messaging-setup).

## Mediante esta integración

Una vez finalizada la integración del lado de la aplicación, puede probarla ejecutando una campaña de mensajes Braze in-app de prueba para una Judo Experience a fin de verificar que funciona como se espera.

### Paso 1: Crear una campaña de mensajes in-app con código personalizado

Desde la plataforma Braze, cree una campaña de mensajes Braze in-app con un tipo de mensaje **de Código personalizado**. A continuación, seleccione **Carga HTML** como tipo personalizado. Asegúrate de rellenar el contenido del mensaje con los campos básicos de mensajería in-app; este contenido no se mostrará al usuario.

![Una imagen del aspecto del panel cuando se selecciona el tipo de mensaje "Código personalizado".]({% image_buster /assets/img/judo/braze-campaign-select-custom-type.png %})

A continuación, utilice el siguiente fragmento HTML mínimo para satisfacer la validación del formulario: 
```
<a href="appboy://close">X</a>
```

Tenga en cuenta que esto no se mostrará en producción en su dispositivo ya que Judo reescribirá y reemplazará esto con una Experiencia Judo.

![Una imagen que muestra el código de validación del formulario añadido al paso de composición de tu campaña.]({% image_buster /assets/img/judo/braze-html-boilerplate.png %})

### Paso 2: Establecer un par clave-valor para Judo
![Esta imagen muestra el par clave-valor necesario para esta integración, siendo la "clave" "judo-experiencia" y el "valor" tu enlace de Judo.]({% image_buster /assets/img/judo/braze-campaign-extras-judo-experience.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Establezca un [par clave-valor personalizado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) en la campaña con una clave de `judo-experience`. Proporcione la URL de la Experiencia Judo que desea mostrar aquí. La biblioteca de integración Judo-Braze detectará este par clave-valor en el controlador y lo utilizará para inyectar su experiencia Judo en lugar de la interfaz de mensajes estándar de la aplicación Braze.
<br><br>
### Paso 3: Finalización de la campaña

Por último, complete la campaña, configurando un desencadenante para la campaña y seleccionando usuarios a través de Segmentos en las secciones **Entrega** y **Usuario objetivo**. Visita nuestro [artículo]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/) sobre mensajes dentro de la aplicación para conocer los distintos componentes de un mensaje Braze dentro de la aplicación.


