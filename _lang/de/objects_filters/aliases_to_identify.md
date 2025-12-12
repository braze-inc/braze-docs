---
nav_title: "Aliasnamen zur Identifizierung des Objekts"
article_title: API-Aliase zur Identifizierung von Objekten
page_order: 11
page_type: reference
description: "In diesem Artikel werden Aliasnamen zur Identifizierung von Objektspezifikationen erläutert."

---

# Aliasnamen zur Identifizierung des Objekts

Eine API-Anfrage mit einem beliebigen Feld im Attribute-Objekt erstellt oder aktualisiert ein Attribut dieses Namens mit dem angegebenen Wert im angegebenen Benutzerprofil. 

Verwenden Sie die Feldnamen des Braze-Benutzerprofils (wie nachfolgend aufgelistet oder alle im Abschnitt für [Braze-Benutzerprofilfelder]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields) aufgelisteten), um diese speziellen Werte im Benutzerprofil im Dashboard zu aktualisieren, oder fügen Sie Ihre eigenen angepassten Attributdaten für den Benutzer hinzu.

## Objektkörper

```json
{
  "aliases_to_identify" : (required, array of aliases to identify object)
  [
    {
      "external_id" : (required, string) see External user ID,
      // external_ids for users that do not exist will return a non-fatal error.
      // See server responses for details.
      "user_alias" : {
        "alias_name" : (required, string) see User aliases,
        "alias_label" : (required, string) see User aliases
      }
    }
  ]
}
```

- [Externe Benutzer-ID]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)
- [Benutzer-Aliase]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)
