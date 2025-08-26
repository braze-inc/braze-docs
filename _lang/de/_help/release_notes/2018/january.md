---
nav_title: Januar
page_order: 12
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für Januar 2018."
---
# Januar 2018

## CSS-Inlining

Sie können jetzt das [CSS-Inlining]({{site.baseurl}}/user_guide/message_building_by_channel/email/css_inline/#css-inlining) für einzelne Nachrichten ein- oder ausschalten, indem Sie die **E-Mail-Einstellungen** aufrufen.

## Neue Filter für Segmente

Sie können nun Segmente mit Hilfe der folgenden Filter erstellen:
- Canvas-Schritt erhalten
- Geöffneter/Klick auf den Canvas-Schritt
- Zuletzt erhaltener spezifischer Canvas-Schritt

{% alert update %}
Ab März 2019 wurde `Received Canvas Step` in `Received Message from Canvas Step` umbenannt, und `Last Received Specific Canvas Step` wurde in `Last Received Message from Specific Canvas Step` umbenannt.
{% endalert %}

## Exportieren von Nutzer:innen über die ID des Geräts

Dieser Endpunkt akzeptiert jetzt einen Bezeichner des Geräts als Parameter, mit dem Sie [anonyme Nutzer:in-Profile exportieren]({{site.baseurl}}/developer_guide/rest_api/export/#users-by-identifier-endpoint) können.

Sie können die ID des Geräts verwenden, um alle Nutzerprofile auf diesem Gerät zu exportieren.

## Engagement-Berichte Update

Zusätzliche Statistiken, wie **Push Öffnungsrate** und **Konversionsrate**, sind jetzt in den [Engagement-Berichten]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#engagement-reports) verfügbar.

## Apple Push-Zertifikate: .p8 Dateien verwenden

Sie können jetzt eine [p8-Datei]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#recommended-option-using-a-p8-file-authentication-tokens) verwenden, wenn Sie ein Apple Push-Zertifikat hochladen, um sicherzustellen, dass Ihre iOS Push-Zugangsdaten nie ablaufen.


