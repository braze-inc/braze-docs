---
nav_title: Guía de actualización a iOS 14
article_title: Guía de actualización del SDK de iOS 14
page_order: 7
platform: iOS
description: "En este artículo de referencia se cubre la actualización del SDK de iOS 14 y se destacan cambios como las geovallas, la localización, IDFA y más."
hidden: true
noindex: true
---

# Guía de actualización del SDK de iOS 14

> Esta guía describe los cambios relacionados con Braze introducidos en iOS 14 y los pasos de actualización necesarios para tu integración de SDK Braze iOS. Para obtener una lista completa de las nuevas actualizaciones de iOS 14, consulta la [página de Apple sobre iOS 14](https://www.apple.com/ios/ios-14/).

{% alert tip %}
A partir de iOS 14.5, la recopilación de **IDFA** y el [intercambio de ciertos datos](https://developer.apple.com/app-store/user-privacy-and-data-use/#permission-to-track) requerirán la nueva solicitud de permiso [AppTrackingTransparency](https://developer.apple.com/documentation/apptrackingtransparency) Framework[(Más información](#idfa)).
{% endalert %}

#### Resumen de los cambios de última hora de iOS 14

- Las aplicaciones destinadas a iOS 14 / Xcode 12 deben utilizar nuestra [versión oficial de iOS 14](https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.27.0).
- [iOS ya no admite](https://developer.apple.com/documentation/corelocation/cllocationmanager/3600215-accuracyauthorization) geovallas para los usuarios que elijan el nuevo permiso de _ubicación aproximada_.
- El uso de las características de orientación "Última ubicación conocida" requerirá una actualización a Braze iOS SDK v3.26.1+ para la compatibilidad con el permiso de _ubicación aproximada_. Ten en cuenta que si utilizas Xcode 12, tendrás que actualizarte al menos a la versión 3.27.0.
- A partir de iOS 14.5, la recopilación de IDFA y el [intercambio de ciertos datos](https://developer.apple.com/app-store/user-privacy-and-data-use/#permission-to-track) requieren la nueva solicitud de permiso [AppTrackingTransparency](https://developer.apple.com/documentation/apptrackingtransparency) Framework.
- Si utilizas el campo "Seguimiento de anuncios habilitado" para la segmentación de campañas o el análisis, tendrás que actualizar a Xcode 12 y utilizar el nuevo marco AppTrackingTransparency para informar del estado de adhesión voluntaria de los usuarios.

## Resumen de la actualización

<style>
table th:nth-child(1),
table th:nth-child(2),
table td:nth-child(1),
table td:nth-child(2) {
    min-width:230px;
}
table td {
    word-break: break-word;
}
</style>

|Si tu aplicación utiliza:|Recomendación de actualización|Descripción|
|------|--------|---|
|Xcode 12|**Actualiza a iOS SDK v3.27 o posterior**|Los clientes que utilicen Xcode 12 deben usar v3.27.0+ para ser compatibles. Si tienes algún problema o pregunta relacionados con nuestra compatibilidad con iOS 14, abre una nueva [consulta en GitHub](https://github.com/Appboy/appboy-ios-sdk/issues).|
|Ubicación más reciente| **Actualiza a iOS SDK v3.26.1 o posterior**|Si utilizas la función de localización más reciente y sigues utilizando Xcode 11, deberías actualizarte al menos al SDK de iOS v3.26.1, que es compatible con la nueva característica _de localización aproximada_. Los SDK más antiguos no podrán recopilar la ubicación de forma fiable cuando un usuario actualice a iOS 14 _y_ elija Ubicación aproximada.<br><br>Aunque tu aplicación no esté orientada a iOS 14, es posible que tus usuarios actualicen a iOS 14 y empiecen a utilizar la nueva opción de precisión de ubicación. Las aplicaciones que no se actualicen al SDK de iOS v3.26.1+ no podrán recopilar de forma fiable atributos de ubicación cuando los usuarios faciliten su _ubicación aproximada_ en dispositivos iOS 14.|
|ID de seguimiento de anuncios IDFA| **Puede ser necesaria la actualización a Xcode 12 y al SDK de iOS v3.27**|En algún momento de 2021, Apple empezará a exigir una solicitud de permiso para la recopilación de IDFA. En ese momento, las aplicaciones deberán actualizarse a Xcode 12 y utilizar el nuevo marco `AppTrackingTransparency` para poder seguir recopilando IDFA. Si pasas IDFA al SDK de Braze, también deberás actualizarte a la versión 3.27.0+ en ese momento.<br><br>Las aplicaciones que no utilicen las nuevas API de iOS 14 no podrán recopilar IDFA, y en su lugar recopilarán un ID en blanco (`00000000-0000-0000-0000-000000000000`) después de que Apple empiece a aplicar este cambio en 2021. Para más información sobre si esto se aplica o no a tu aplicación, consulta [los detalles del IDFA](#idfa).|


## Cambios de comportamiento en iOS 14

### Permiso aproximado de ubicación

![Ubicación precisa]({% image_buster /assets/img/ios/ios14-approximate-location.png %}){: style="float:right;max-width:45%;margin-left:15px;"}

#### Resumen

Al solicitar permiso de ubicación, los usuarios tendrán ahora la opción de proporcionar su _ubicación exacta_ (comportamiento anterior), o la nueva _ubicación aproximada_. La ubicación aproximada devolverá un radio mayor en el que se encuentra el usuario, en lugar de sus coordenadas exactas.

#### Geovallas {#geofences}

[iOS ya no admite](https://developer.apple.com/documentation/corelocation/cllocationmanager/3600215-accuracyauthorization) geovallas para los usuarios que elijan el nuevo permiso de _ubicación aproximada_. Aunque no se requieren actualizaciones para tu integración de SDK de Braze, es posible que tengas que ajustar tu [estrategia de marketing basada en la ubicación](https://www.braze.com/blog/geofencing-geo-targeting-beaconing-when-to-use/) para las campañas que dependen de geovallas.

#### Segmentación de ubicación {#location-tracking}

Para seguir recopilando la _última ubicación conocida_ de los usuarios cuando se concede la _ubicación aproximada_, tu aplicación tendrá que actualizarse al menos a la versión 3.26.1 del SDK de Braze para iOS. Ten en cuenta que la ubicación será menos precisa, y según nuestras pruebas ha sido de más de 12.000 metros (7+ millas). Cuando utilices las opciones de localización de _la última ubicación conocida_ en el panel de Braze, asegúrate de aumentar el radio de la ubicación para tener en cuenta las nuevas _ubicaciones aproximadas_ (recomendamos al menos un radio de 1 milla/1,6 km).

Las aplicaciones que no actualicen el SDK de Braze para iOS al menos a la versión 3.26.1 ya no podrán utilizar el seguimiento de ubicación cuando se conceda _una ubicación aproximada_ en dispositivos con iOS 14.

Los usuarios que ya hayan concedido acceso a la ubicación seguirán proporcionando _una ubicación precisa_ tras la actualización.

Ten en cuenta que si utilizas Xcode 12, tendrás que actualizarte al menos a la versión 3.27.0.

Para obtener más información sobre la ubicación aproximada, consulta el video WWDC de Apple [sobre las novedades en materia de ubicación](https://developer.apple.com/videos/play/wwdc2020/10660/).

### IDFA y transparencia en el seguimiento de las aplicaciones {#idfa}

#### Resumen

IDFA (Identificador para Anunciantes) es un identificador proporcionado por Apple para su uso con socios de publicidad y atribución para el seguimiento entre dispositivos y está vinculado al ID de Apple de una persona.

A partir de iOS 14.5, debe mostrarse una nueva solicitud de permiso (lanzada por el nuevo marco `AppTrackingTransparency` ) para recabar el consentimiento explícito del usuario para el IDFA. Esta solicitud de permiso para "rastrearte a través de aplicaciones y sitios web propiedad de otras empresas" se solicitará de forma similar a como se solicita a los usuarios que soliciten su ubicación.

Si un usuario no acepta el mensaje, o si no actualizas al framework `AppTrackingTransparency` de Xcode 12, se devolverá un valor IDFA en blanco (`00000000-0000-0000-0000-000000000000`), y tu aplicación no podrá volver a consultar al usuario.

{% alert important %}
Estas actualizaciones IDFA entrarán en vigor después de que los usuarios finales actualicen su dispositivo a iOS 14.5. Asegúrate de que tu aplicación utilice el nuevo `AppTransparencyFramework` con Xcode 12 si piensas recopilar IDFA.
{% endalert %}

#### Cambios en la colección IDFA de Braze
![IDFA]({% image_buster /assets/img/ios/ios14-idfa.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

1. Braze seguirá permitiendo que las aplicaciones _proporcionen_ el valor IDFA de un usuario al SDK de Braze.

2. La macro de compilación `ABK_ENABLE_IDFA_COLLECTION`, que compilaría condicionalmente en la recopilación automática opcional de IDFA, ya no funcionará en iOS 14 y se eliminó en 3.27.0. 

3. Si utilizas el campo "Seguimiento de anuncios habilitado" para la segmentación de campañas o el análisis, tendrás que actualizar a Xcode 12 y utilizar el nuevo marco AppTrackingTransparency para informar del estado de adhesión voluntaria de tus usuarios. El motivo de este cambio es que en iOS 14, el antiguo campo [`advertisingTrackingEnabled`](https://developer.apple.com/documentation/adsupport/asidentifiermanager/1614148-advertisingtrackingenabled) siempre devolverá No.

4. Si tu aplicación ha utilizado IDFA o IDFV como ID externo de Braze, te recomendamos encarecidamente que dejes de utilizar estos identificadores y utilices un UUID. Para más información sobre la migración de ID externos, consulta nuestros [puntos finales de la API de migración de ID externos]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/).

Lee más información de Apple sobre sus [actualizaciones de privacidad](https://developer.apple.com/app-store/user-privacy-and-data-use/) y el nuevo [framework de transparencia del seguimiento de aplicaciones](https://developer.apple.com/documentation/apptrackingtransparency).

### Autorización push {#push-provisional-auth}

{% alert important %}
En iOS 14 no se incluyen cambios en la Autorización Push Provisional. En una versión beta anterior de iOS 14, Apple introdujo un cambio que desde entonces se ha revertido al comportamiento anterior.
{% endalert %}

## Nuevas características de iOS 14

### Resumen de la recopilación de datos y privacidad de la aplicación {#app-privacy}

Desde el 8 de diciembre de 2020, todos los envíos a la App Store requieren pasos adicionales para cumplir [las nuevas normas de privacidad de las aplicaciones de Apple](https://developer.apple.com/app-store/app-privacy-details/).

#### Cuestionario del portal para desarrolladores de Apple

En el _Portal del Desarrollador de Apple_:
* Se te pedirá que rellenes un cuestionario para describir cómo recopilan datos tu aplicación o los socios de terceros.
  * Se espera que el cuestionario esté siempre actualizado con su versión más reciente en el App Store.
  * El cuestionario puede actualizarse incluso sin presentar una nueva aplicación.
* Se te pedirá que pegues un enlace a la URL de la Política de privacidad de tu aplicación.

Cuando rellenes tu cuestionario, consulta a tu equipo jurídico y considera cómo puede afectar a tus requisitos de divulgación el uso de Braze para los siguientes campos.

#### Recopilación de datos predeterminada de Braze
**Identificadores** \- El SDK de Braze siempre recoge un identificador anónimo del dispositivo. Actualmente está configurado para el dispositivo IDFV (identificador del vendedor).

**Datos de uso**: pueden incluir datos de sesión de Braze, así como cualquier evento o recopilación de atributos que utilices para medir la interacción con el producto.

#### Recopilación de datos opcional
Datos que puedes estar recopilando opcionalmente a través de tu uso de Braze:

**Ubicación** \- Tanto la ubicación aproximada como la ubicación precisa pueden ser recogidas opcionalmente por el SDK de Braze. Estas características están desactivadas por defecto.

**Información de contacto** \- Puede incluir eventos y atributos relacionados con la identidad del usuario.

**Compras** \- Puede incluir eventos y compras registradas en nombre del usuario.

{% alert important %}
Nota: no se trata de una lista exhaustiva. Si recoges manualmente otra información sobre tus usuarios en Braze que se aplique a otras categorías del Cuestionario de privacidad de la aplicación, tendrás que revelarlas también.
{% endalert %}

Para obtener más información sobre esta característica, consulta [Privacidad y uso de datos de Apple](https://developer.apple.com/app-store/user-privacy-and-data-use/).

