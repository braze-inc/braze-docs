---
nav_title: Januar
page_order: 12
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für Januar 2018."
---
# Januar 2018

## CSS-Inlining

Sie können jetzt das [CSS-Inlining][84] für einzelne E-Mail-Nachrichten ein- oder ausschalten, indem Sie zu Ihren **E-Mail-Einstellungen** gehen.

## Neue Segmentfilter

Sie können jetzt Segmente mit den folgenden Filtern erstellen:
- Canvas-Schritt erhalten
- Geöffnete/geklickte Leinwand Schritt
- Zuletzt erhaltener spezifischer Canvas-Schritt

{% alert update %}
Ab März 2019 wurde `Received Canvas Step` in `Received Message from Canvas Step` umbenannt, und `Last Received Specific Canvas Step` wurde in `Last Received Message from Specific Canvas Step` umbenannt.
{% endalert %}

## Benutzer über die Geräte-ID exportieren

Dieser Endpunkt akzeptiert jetzt eine Gerätekennung als Parameter, mit dem Sie [anonyme Benutzerprofile exportieren][82] können.

Sie können die Geräte-ID verwenden, um alle Benutzerprofile auf diesem Gerät zu exportieren.

## Aktualisierung der Engagementberichte

Zusätzliche Statistiken, wie die **Öffnungsrate von Push-Nachrichten** und die **Konversionsrate**, sind jetzt in den [Engagement-Berichten][81] verfügbar.

## Apple Push-Zertifikate: .p8 Dateien verwenden

Sie können jetzt eine [p8-Datei][80] verwenden, wenn Sie ein Apple Push-Zertifikat hochladen, um sicherzustellen, dass Ihre iOS Push-Anmeldeinformationen nie ablaufen.


[80]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#recommended-option-using-a-p8-file-authentication-tokens
[81]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#engagement-reports
[82]: {{site.baseurl}}/developer_guide/rest_api/export/#users-by-identifier-endpoint
[84]: {{site.baseurl}}/user_guide/message_building_by_channel/email/css_inline/#css-inlining
