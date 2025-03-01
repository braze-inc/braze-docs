---
nav_title: Entfernen von Benutzern über API
article_title: Entfernen von Benutzern über API
page_order: 0

page_type: reference
description: "Dieser Hilfeartikel beschreibt die Auswirkungen des Entfernens eines Benutzerprofils über die Braze REST API."
tool: Dashboard
platform: API
---

# Entfernen von Benutzern über API

Wenn Sie [einen Benutzer über die Braze REST API entfernen][1], werden die folgenden Daten gelöscht (nulled):
- Alle Attribute, die der Benutzer hatte
- E-Mail-Adresse
- Telefonnummer
- Externe Benutzer-ID 
- Geschlecht
- Land
- Sprache

Wenn Sie [einen Benutzer über die Braze REST API entfernen][1], treten die folgenden Ereignisse ein:
- Das Benutzerprofil wird gelöscht (nulled).
- Die Anzahl der [Lifetime-Benutzer][2] wird aktualisiert, um die neu entfernten Benutzer zu berücksichtigen.	
- Der entfernte Benutzer wird weiterhin für den aggregierten Conversion-Prozentsatz gezählt. Benutzerdefinierte Ereignis- und Kaufzählungen werden für entfernte Benutzer nicht aktualisiert.

## Mehrere Profile mit einer gemeinsamen E-Mail-Adresse

Nehmen wir an, Sie möchten mehrere Benutzerprofile zusammenführen, die dieselbe E-Mail-Adresse haben. 

Um diese Benutzerprofile zusammenzuführen:

 1. Identifizieren Sie alle Benutzer mit doppelten E-Mail-Adressen. 
 2. Exportieren Sie alle Attribute eines einzelnen Profils. 
 3. Importieren Sie diese Attribute entweder über API oder CSV in das Benutzerprofil. 
 4. Entfernen Sie die Benutzer über die API und löschen Sie damit diese doppelten Benutzer und die oben beschriebenen Daten.

_Zuletzt aktualisiert am 13\. September 2023_

[1]: {{site.baseurl}}/api/endpoints/user_data/#user-delete-endpoint/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#lifetime-users
