---
nav_title: Kognitiv Inspire
article_title: Kognitiv Inspire
description: "Kognitiv Inspire ist ein Kundenbindungssystem, mit dem Sie Ihre Kundenbindungsstrategie umsetzen und auswerten können. Es bietet innovative Funktionen und eine maßgeschneiderte Kommunikation mit den Mitgliedern, um die Effizienz Ihres Programms zu steigern."
alias: /partners/kognitiv/
page_type: partner
search_tag: Partner
---

# Kognitiv Inspire

> [Kognitiv Inspire][1] ist ein Treuetechnologie-System, das durch ergebnisorientierte Treueprogramme, die das Kundenengagement verstärken, die Ausgaben erhöhen und loyales Verhalten belohnen, unvergleichliche Kundenerlebnisse ermöglicht.

Die Integration von Braze und Kognitiv ermöglicht es Ihnen, Ihre Kundenbindungsstrategie zu implementieren und zu evaluieren. Sie bietet Ihnen innovative Funktionen und eine maßgeschneiderte Kommunikation mit Ihren Mitgliedern, um die Effizienz Ihres Programms zu verbessern.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Kognitiv-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Kognitiv-Konto][1]. |
| Kognitiv API-Schlüssel | Ein REST-API-Schlüssel von Kognitiv. Dieses kann auf der Seite **API-Sicherheitstoken** erstellt werden. |
| Braze REST Endpunkt | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von der Braze-URL für Ihre [Instanz]({{site.baseurl}}/api/basics/#endpoints) ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

- **Personalisierte Anmeldung für Treueprogramme**: Fördern Sie die Treue Ihrer Mitglieder mit einer nahtlosen Programmeinschreibung und einer individuellen Begrüßungsnachricht, die über ihren bevorzugten Kanal zugestellt wird.
- **Ausgabe von Belohnungen und Benachrichtigung über das Engagement**: Halten Sie den Funken der Loyalität am Leben, indem Sie Belohnungen und Benachrichtigungen ausgeben, die die Meilensteine jedes Mitglieds feiern.
- **Strategische Einstufung und Segmentierung der Mitglieder**: Ermöglichen Sie ein personalisiertes Engagement, indem Sie Mitglieder auf der Grundlage von Ausgaben, Engagement und einfachen oder komplexen Geschäftsregeln, die auf die spezifischen Bedürfnisse Ihrer Marke zugeschnitten sind, einordnen und segmentieren.
- **Benachrichtigung über die Berechtigung zur Beförderung in Echtzeit**: Geben Sie jedem Mitglied das Gefühl, etwas Besonderes zu sein, indem Sie es sofort über die Teilnahme an exklusiven Werbeaktionen benachrichtigen.

## Integration

Verwenden Sie Kognitiv Webhooks, um Anfragen an Braze zu senden, wenn Treueereignisse eintreten. Die folgenden Beispiele zeigen, wie Sie Kognitiv und Braze verwenden, um eine Belohnung auszustellen, einen Kognitiv-Benutzer in Braze zu registrieren und ihm eine Willkommens-E-Mail zu schicken.

{% raw %}
### Belohnung für die Ausgabe von Braze

Das folgende Kognitiv-Beispiel gibt eine Mitgliederbelohnung aus. Kognitiv Inspire wird dieses Ereignis der Belohnungsausgabe als benutzerdefiniertes Ereignis über Webhooks an Braze übermitteln. Um eine Follow-up-E-Mail zu senden, um die Belohnung mitzuteilen, erstellen Sie eine Kampagne oder ein Canvas, das durch dieses benutzerdefinierte Ereignis ausgelöst wird.

**Webhook URL**: `<braze-api-rest-endpoint>`
**Anfrage Körper**: `Raw Text`

- **HTTP-Methode**: POST
- **Kopfzeilen anfordern**:
  - **Autorisierung**: Träger `<Kognitiv-api-key>`
  - **Inhalt-Typ** application/json

#### Anfragetext

```json
{ 
  "events" : [ 
    { 
    "external_id" : "{{memberId}}", 
    "app_id" : "93ec5a59-3752-4a45-8559-55b61209ba38", 
    "name" : "rewards_issued", 
    "time" : "{{issuedDate}}", 
    "issued_date" : "{{issuedDate}}", 
    "issued_location_name" : "{{issuedLocationName}}", 
    "reward_type" : "{{rewardType}}" 
    } 
  ] 
}
```

### Erstellen Sie einen Benutzer und senden Sie eine Willkommens-E-Mail

Das folgende Kognitiv-Beispiel erstellt einen neuen Benutzer in Braze, wenn er sich bei KLS anmeldet. Um eine Willkommens-E-Mail für diesen Benutzer zu planen, erstellen Sie in Braze eine Kampagne oder ein Canvas, das auf der Grundlage bestimmter benutzerdefinierter Attribute ausgelöst wird.

**Webhook URL**: `<braze-api-rest-endpoint>` <br>
**Anfrage Körper**: `Raw Text`

- **HTTP-Methode**: POST
- **Kopfzeilen anfordern**:
  - **Autorisierung**: Träger `<Kognitiv-api-key>`
  - **Inhalt-Typ** application/json

#### Anfragetext

```json
{ 
  "attributes": [ 
    { 
      "app_id": "93ec5a59-3752-4a45-855b6109ba38", 
      "bio": "Software Architect", 
      "country": "{{memberAddressCO}}", 
      "email": "{{memberEmail}}", 
      "email_subscribe": "opted_in", 
      "external_id": "{{memberId}}", 
      "first_name": "{{memberFirstName}}", 
      "home_city": "{{memberAddressCity}}", 
      "time_zone": "America/Chicago", 
      "total_points_balance": "{{memberPointsAvailable}}", 
      "CreatedKLS": "{{issuedTimestamp}}", 
      "email_contact_allowed" : "{{memberEmailContactAllowed}}", 
      "sms_contact_allowed" : "{{memberSmsContactAllowed}}", 
      "date_joined": "{{issuedDate}}" 
    } 
  ] 
}
```
{% endraw %}

## Dokumentation und Integrationsfunktionen von Kognitiv Inspire

Sobald Sie Braze in Kognitiv Inspire integriert haben, ermöglicht Ihnen Kognitiv den Zugriff auf sein umfangreiches API-Portfolio, modernste Webhook-Funktionen und robuste Datenimport- und -exportfunktionen für einen nahtlosen Massentransfer. Weitere Informationen zu den Funktionen und Integrationsmöglichkeiten von Kognitiv Inspire finden Sie im [Kognitiv-Ressourcenhandbuch][2] oder kontaktieren Sie Kognitiv für eine geführte Demonstration.

### Endpunkte

**REST API-Autorisierung**
- Region USA: `https://app.kognitivloyalty.com/Auth/connect/token`
- Region CA/EMEA: `https://ca.kognitivloyalty.com/Auth/connect/token`
- APAC-Region: `https://aus.kognitivloyalty.com/Auth/connect/token`

**REST API (Basis-URL)**
- Region USA: `https://app.kognitivloyalty.com/api`
- Region CA/EMEA: `https://ca.kognitivloyalty.com/api`
- APAC-Region: `https://aus.kognitivloyalty.com/api`

**Webdienste-Endpunkte (Basis-URL)**
- Region USA: `https://app.kognitivloyalty.com/WS`
- Region CA/EMEA: `https://ca.kognitivloyalty.com/WS`
- APAC-Region: `https://aus.kognitivloyalty.com/WS`

Wenn Sie weitere Informationen zur Konfiguration von Zugriffstoken und SFTP-Endpunkten wünschen, wenden Sie sich für eine Demonstration an Kognitiv.

[1]: http://kognitiv.com
[2]: https://info.kognitivloyalty.com