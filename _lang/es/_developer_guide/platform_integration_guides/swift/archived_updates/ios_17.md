---
nav_title: Guía de actualización a iOS 17
article_title: Guía de actualización a iOS 17
page_order: 7
platform: 
  - iOS
description: "Este artículo contiene información sobre la versión iOS 17 para ayudarte a actualizar tu SDK fácilmente."
hidden: true
noindex: true
---

# Guía de actualización a iOS 17

> ¿Tienes curiosidad por saber cómo se está preparando Braze para el próximo lanzamiento de iOS? Este artículo resume nuestra información sobre la versión 17 de iOS para ayudarte a crear una experiencia fluida para ti y tus usuarios.

## Compatibilidad con iOS 17 y Xcode 15

Tanto el SDK Swift como el SDK Objective-C de Braze son compatibles con Xcode 14 y Xcode 15, y con dispositivos iOS 17.

## Cambios en iOS 17

### Seguimiento de enlaces y eliminación de parámetros UTM

Uno de los cambios importantes de iOS 17 es el bloqueo de los parámetros UTM en Safari. Los parámetros UTM son fragmentos de código que se añaden a las URL y que se utilizan con frecuencia en las campañas de marketing para medir la eficacia del correo electrónico, los SMS y otros canales de mensajería. 

Este cambio no afecta al seguimiento de clics por correo electrónico Braze ni a los envíos de acortamiento de enlaces SMS.

### Transparencia del seguimiento de la aplicación

Apple anunció su compromiso de ampliar el alcance de [la Transparencia del Seguimiento de Anuncios (ATT)](https://support.apple.com/en-us/HT212025), que habilita a los usuarios a controlar si una aplicación puede acceder a su actividad en aplicaciones y sitios web pertenecientes a otras empresas. La versión 17 de iOS contiene dos características clave de ATT: manifiestos de privacidad y firma de código.

#### Manifiestos de privacidad

Apple exige ahora un archivo de manifiesto de privacidad que describa el motivo por el que tu aplicación y los SDK de terceros recopilan datos, junto con sus métodos de recopilación de datos. A partir de iOS 17.2, Apple bloqueará todos los puntos finales de seguimiento declarados en tu aplicación hasta que el usuario final acepte el aviso de ATT.

Braze ha publicado nuestro propio manifiesto de privacidad, junto con nuevas API flexibles que redirigen automáticamente los datos declarados de seguimiento a puntos finales dedicados de `-tracking`. Para más información, consulta [el manifiesto de privacidad de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest).

#### Firma de código

La firma de código permite a los desarrolladores que utilizan un SDK de terceros en su aplicación validar que el mismo desarrollador lo firmó como versiones anteriores en Xcode. 

### SDK de Braze y privacidad

Apple también ha anunciado que publicará una lista de SDK de terceros que se considera "que afectan la privacidad" a finales de 2023. Se espera que estos SDK tengan un impacto especialmente alto en la privacidad de los usuarios por parte de Apple.

A diferencia de los SDK de seguimiento tradicionales, diseñados para supervisar a los usuarios en varios sitios web y aplicaciones, el SDK de Braze se centra en la mensajería de datos propios y en las experiencias de usuario.

Aunque no esperamos que el SDK de Braze se incluya en esta lista, tenemos la intención de seguir de cerca esta situación y publicar las actualizaciones necesarias.
