---
nav_title: "Benutzer-Alias-Objekt"
article_title: API-Benutzer-Alias-Objekt
page_order: 11
page_type: reference
description: "Dieser Referenzartikel erklärt die verschiedenen Komponenten des Benutzer-Aliasobjekts."

---

# Benutzer-Alias-Objekt

> Ein Alias dient als alternativer eindeutiger Benutzeridentifikator. Mithilfe eines Benutzer-Aliasobjekts können Sie einen konsistenten Identifikator für Analysen festlegen, der einen bestimmten Benutzer sowohl vor als auch nach der Anmeldung bei einer mobilen App oder Website verfolgt. Sie können dieses Objekt auch verwenden, um Ihren Braze-Benutzern die von einem Drittanbieter verwendeten Identifikatoren hinzuzufügen, damit Sie Ihre Daten leichter extern abgleichen können.

Das Benutzer-Alias-Objekt besteht aus zwei Teilen: einem `alias_name` für den Bezeichner selbst und einem `alias_label`, der den Typ des Alias angibt. Benutzer können mehrere Aliasnamen mit unterschiedlichen Bezeichnungen haben, aber nur einen `alias_name` pro `alias_label`.

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