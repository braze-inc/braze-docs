---
nav_title: "Nutzer:innen über API entfernen"
article_title: "Nutzer:innen über API entfernen"
page_order: 0

page_type: reference
description: "Dieser Hilfeartikel beschreibt die Auswirkungen des Entfernens eines Nutzerprofils über die Braze REST API."
tool: Dashboard
platform: API
---

# Nutzer:innen über API entfernen

Wenn Sie [einen Nutzer:innen über die Braze REST API entfernen]({{site.baseurl}}/api/endpoints/user_data/#user-delete-endpoint/), werden die folgenden Daten gelöscht (nulled):
- Alle Attribute, die der Benutzer hatte
- E-Mail-Adresse
- Telefonnummer
- Externe Benutzer-ID 
- Geschlecht
- Land
- Sprache

Wenn Sie [einen Nutzer:innen über die Braze REST API entfernen]({{site.baseurl}}/api/endpoints/user_data/#user-delete-endpoint/), treten die folgenden Ereignisse ein:
- Das Profil des Nutzers:in ist gelöscht (nulled).
- Die Anzahl der [Lifetime-Benutzer]({{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#lifetime-users) wird aktualisiert, um die neu entfernten Nutzer:innen zu berücksichtigen.	
- Der entfernte Nutzer:innen wird weiterhin für die aggregierte Konversion gezählt. Angepasste Events und Kauf-Events werden für entfernte Nutzer:innen nicht aktualisiert.

## Mehrere Profile mit einer gemeinsamen E-Mail Adresse

Angenommen, Sie möchten mehrere Nutzerprofile zusammenführen, die dieselbe E-Mail Adresse haben. 

So führen Sie diese Nutzerprofile zusammen:

 1. Identifizieren Sie alle Nutzer:innen mit doppelten E-Mail-Adressen. 
 2. Exportieren Sie alle Attribute eines einzelnen Profils. 
 3. Importieren Sie diese Attribute in das Nutzerprofil entweder über API oder CSV. 
 4. Entfernen Sie die Nutzer:innen über die API und löschen Sie damit diese doppelten Nutzer:innen und die oben genannten Daten.

_Zuletzt aktualisiert am 13\. September 2023_

