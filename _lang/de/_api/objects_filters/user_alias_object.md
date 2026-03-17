---
nav_title: "Nutzer-Alias Objekt"
article_title: "API Nutzer:innen Alias Objekt"
page_order: 11
page_type: reference
description: "Dieser referenzierte Artikel erklärt die verschiedenen Komponenten des Nutzer:in-Objekts."

---

# Nutzer-Alias Objekt

> Ein Alias dient als alternativer eindeutiger Bezeichner für Nutzer:innen. Mithilfe eines Nutzer-Alias-Objekts können Sie einen konsistenten Bezeichner für Analytics festlegen, der einen bestimmten Nutzer:in sowohl vor als auch nach der Anmeldung bei einer mobilen App oder Website verfolgt. Sie können dieses Objekt auch verwenden, um die von einem Drittanbieter verwendeten Bezeichner zu Ihren Unternehmensnutzer:innen hinzuzufügen, um Ihre Daten extern einfacher abzugleichen.

Das Nutzer-Alias-Objekt besteht aus zwei Teilen: einem `alias_name` für den Bezeichner selbst und einem `alias_label`, der den Typ des Alias angibt. Nutzer:innen können mehrere Aliasnamen mit unterschiedlichen Bezeichnungen haben, aber nur einen `alias_name` pro `alias_label`.

Dieses Objekt wird häufig in allen unseren Endpunkten und oft auch in anderen Objekten verwendet.

## Objektkörper

```json
{
  "user_alias" : {
    "alias_name" : (required, string),
    "alias_label" : (required, string)
  }
}
```

### Beispiel

```json
{
  "user_alias": {
    "alias_name": "john_doe_123",
    "alias_label": "email_id"
  },
  "external_id": "user_456"
}
```