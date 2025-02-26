---
nav_title: "Objet Alias d’identification"
article_title: Objet Alias d’identification de l’API
page_order: 11
page_type: reference
description: "Cet article explique les alias pour identifier la spécification d’objet."

---

# Objet Alias d’identification

Une demande API contenant l’un des champs de l’objet Attributs créera ou mettra à jour un attribut de ce nom avec la valeur donnée sur le profil utilisateur spécifié. 

Utilisez les noms de champs de profil utilisateur Braze (énumérés comme suit ou tout autre répertorié dans la section pour [Braze user profile fields]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)) pour mettre à jour ces valeurs spéciales sur le profil utilisateur dans le tableau de bord ou ajoutez vos propres données d'attributs personnalisés à l'utilisateur.

## Corps de l’objet

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

- [ID utilisateur externe]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)
- [Alias utilisateurs]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)
