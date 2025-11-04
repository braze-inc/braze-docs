---
nav_title: Branch para la vinculación en profundidad
article_title: Branch para la vinculación en profundidad
alias: /partners/branch_for_deeplinking/
page_type: partner
description: "Este artículo de referencia describe la asociación entre Braze y Branch y cómo utilizarla para apoyar tus prácticas de vinculación en profundidad."
search_tag: Partner

---

# Branch para la vinculación en profundidad {#branch}

{% multi_lang_include video.html id="PwGKqfwV-Ss" align="right" %}

> [Branch](https://branch.io/), una plataforma de enlace móvil, te ayuda a adquirir, interactuar y medir en todos los dispositivos, canales y plataformas, proporcionando una visión holística de todos los puntos de intervención del usuario.

_Esta integración está mantenida por Branch._

## Sobre la integración

La integración de Braze y Branch te permite ofrecer mejores experiencias a tus clientes, ya que te permite [atribuir]({{site.baseurl}}/partners/message_orchestration/attribution/branch_for_attribution/) correctamente el inicio de su viaje de usuario y conectarlos a través de enlaces profundos a su ubicación prevista.

## Integración

Sigue [la guía de integración de SDK de Branch](https://help.branch.io/developers-hub/docs/native-sdks-overview) para poner en marcha tu integración de Branch. Consulte a continuación otros casos de uso.

### Soporta enlaces universales iOS

Para soportar el envío de enlaces universales iOS como enlaces profundos desde dentro de Braze:

1. Sigue la documentación de Branch para configurar [los enlaces universales](https://help.branch.io/developers-hub/docs/ios-universal-links).
2. Implemente el método [`BrazeDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate)[braze(_:shouldOpenURL:)](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:shouldopenurl:)-6xxc5) en su integración Braze SDK para [enrutar enlaces universales]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/#linking-handling-customization) desde su aplicación.

### Vinculación en profundidad en el correo electrónico

Consulta nuestra documentación sobre [Enlaces universales y Enlaces de aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/)
o consulta [la documentación de Branch](https://help.branch.io/developers-hub/docs/ios-universal-links#apps-that-always-work) para configurar la vinculación en profundidad desde los correos electrónicos enviados a través de Braze.

La vinculación a números de teléfono (añadir `tel` a `href`) no es compatible con la aplicación de Gmail para iOS a menos que el usuario conceda permisos de llamada a la aplicación.

Dependiendo de su ESP, puede ser necesaria una personalización adicional para admitir enlaces universales con seguimiento de clics. Esta información se describe en nuestro artículo específico. También puede consultar las siguientes referencias para obtener más información:

- [SendGrid](https://help.branch.io/using-branch/page/braze-sendgrid)
- [SparkPost](https://help.branch.io/using-branch/page/braze-sparkpost)


