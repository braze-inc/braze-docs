---
nav_title: Apteligent
article_title: Apteligent
alias: /partners/apteligent/
description: "Este artículo de referencia describe la asociación entre Braze y Apteligent, una aplicación móvil que detalla los informes de colisiones, permitiéndote registrar datos críticos en tu solución Braze existente."
page_type: partner
search_tag: Partner

---

# Apteligent

> [Apteligent](https://www.vmware.com/products/workspace-one/intelligence-consumer-apps.html) es una plataforma de rendimiento de aplicaciones móviles que proporciona herramientas e información a desarrolladores y administradores de productos. 

_Esta integración está mantenida por Apteligent._

## Sobre la integración

La integración de Braze y Apteligent proporciona informes detallados de fallos de iOS, lo que le permite registrar datos críticos en su solución Braze existente, así como segmentar, comprender y comprometerse con los usuarios que han experimentado fallos en la aplicación.

## Requisitos previos 

| Requisito | Descripción |
|---|---|
| Cuenta TestDrive | Se necesita una cuenta de TestDrive para beneficiarse de esta asociación. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert warning %}
Actualmente, esta integración sólo es compatible con iOS.
{% endalert %}

## Integración {#apteligent-ios-integration}

### Paso 1: Registrar un observador

En primer lugar, debe registrar un observador. Asegúrate de que esto esté hecho antes de iniciar Apteligent.

```objc
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(crashDidOccur:)
                                             name:@"CRCrashNotification"
                                           object:nil];
```

### Paso 2: Registro personalizado de análisis de colisiones

El SDK de Apteligent enviará una notificación cuando el usuario cargue la aplicación después de experimentar una falla. La notificación tendrá el nombre de la falla, el motivo y la fecha de ocurrencia.

Al recibir la notificación, registre un evento de colisión personalizado y actualice los atributos del usuario con los análisis de informes de colisiones de Apteligent:

```objc
- (void)crashDidOccur:(NSNotification*)notification {
  NSDictionary *crashInfo = notification.userInfo;
  [[Appboy sharedInstance] logCustomEvent:@"ApteligentCrashEvent" withProperties:crashInfo];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashName" andStringValue:crashInfo[@"crashName"]];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashReason" andStringValue:crashInfo[@"crashReason"]];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashDate" andDateValue:crashInfo[@"crashDate"]];
}
```

Una vez completado, podrá aprovechar la potencia de los análisis de segmentación y compromiso de Braze utilizando la información sobre colisiones que se encuentra en la plataforma Apteligent.

