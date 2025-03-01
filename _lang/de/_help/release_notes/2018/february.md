---
nav_title: Februar
page_order: 11
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für Februar 2018."
---
# Februar 2018

## Anzahl der iOS-Push-Badges

Sie können jetzt [die Anzahl der Ausweise][89] innerhalb des Push Composers von Braze [aktualisieren][89].
Für jede Push-Nachricht können Sie angeben, welche Anzahl von Ausweisen diese Benachrichtigung auslöst.

## Exportieren von Benutzern über API unter Verwendung von E-Mail-Adressen

Sie können jetzt [Benutzerprofildaten über API exportieren][88], indem Sie E-Mail-Adressen angeben.
Dieser Export umfasst alle mit dieser E-Mail-Adresse verbundenen Profile.

## E-Mail-Vorlagen-APIs

Sie können jetzt [E-Mail-Vorlagen über die API][87] erstellen und aktualisieren. Jede Vorlage hat eine **email_template_id**, die in anderen API-Aufrufen referenziert werden kann.

## Berechtigungen für REST-API-Schlüssel

Sie können jetzt [mehrere REST-API-Schlüssel][86] erstellen und die Zugriffsberechtigungen für jeden einzelnen konfigurieren. Jeder Schlüssel kann so konfiguriert werden, dass er Zugang zu bestimmten Endpunkten gewährt.

Sie können auch eine [Whitelist von IP-Adressen][85] und Subnetzen festlegen, die REST-API-Anfragen für einen bestimmten REST-API-Schlüssel stellen dürfen.

[85]: {{site.baseurl}}/developer_guide/rest_api/basics/#api-ip-whitelisting
[86]: {{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys
[87]: {{site.baseurl}}/developer_guide/rest_api/email_templates/#email-templates
[88]: {{site.baseurl}}/developer_guide/rest_api/export/#user-export
[89]: {{site.baseurl}}/help/best_practices/utilizing_badge_count/#utilizing-badge-count
