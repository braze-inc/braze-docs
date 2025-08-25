---
nav_title: Integration von API-Partnern
alias: /api_partner_integration/
hidden: true
---

# Integration von API-Partnern

> Erfahren Sie mehr über die Anforderungen für Partner API Integrationen, wie z.B. die Syntax für `User-Agent` Header.

{% alert important %}
Bisher mussten Partner ihren Namen in das Partnerfeld ihrer API-Anfragen eintragen. Diese Formatierung wird nicht mehr unterstützt und eine `User-Agent` Kopfzeile ist jetzt erforderlich.
{% endalert %}

## Benutzer-Agenten

Sie müssen einen `User-Agent` Header einfügen, der die Quelle des Datenverkehrs eindeutig identifiziert. Auf diese Weise können unsere gemeinsamen Kund:innen den Partnerverkehr in den Berichten über die API-Nutzung von Braze sehen, und die Ingenieure von Braze können Integrationen identifizieren, die nicht den Best Practices entsprechen. Im Allgemeinen sollten Sie nur einen einzigen Nutzer:in für Ihren gesamten Datenverkehr verwenden.

### Syntax

Ihr `User-Agent` Header muss dem folgenden Format entsprechen (das dem [RFC 7231](https://datatracker.ietf.org/doc/html/rfc7231#page-46) Standard ähnelt):

```bash
User-Agent: partner-OrganizationName-ProductName/ProductVersion
```

Ersetzen Sie Folgendes:

| Platzhalter | Beschreibung |
|-------------|-------------|
| `OrganizationName` | Der Name Ihrer Organisation, formatiert in Pascal-Schrift. |
| `ProductName` | Der Name Ihres Produkts, formatiert in Pascal-Schrift. |
| `ProductVersion` | Die Versionsnummer Ihres Produkts. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Beispiele

Zum Beispiel wäre der folgende Nutzer:in der Snowflake Cloud Data Ingestion der richtige Agent:

```bash
User-Agent: partner-Snowflake-CloudDataIngestion/179
```

Dies wäre jedoch falsch, da es die Quelle des Datenverkehrs nicht eindeutig identifiziert:

```bash
User-Agent: axios/1.4.0
``` 
