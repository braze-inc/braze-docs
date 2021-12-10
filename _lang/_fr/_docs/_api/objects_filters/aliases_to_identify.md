---
nav_title: "Alias pour identifier l'objet"
article_title: Alias API pour identifier l'objet
page_order: 11
page_type: Référence
description: "Cet article explique l'objet nécessaire pour identifier les alias des utilisateurs."
---

# Alias pour identifier la spécification de l'objet

Une requête API avec n'importe quel champ dans l'objet Attributes créera ou mettra à jour un attribut de ce nom avec la valeur donnée sur le profil utilisateur spécifié. Utilisez les noms de champs de profil utilisateur Braze (listés ci-dessous ou tous ceux listés dans le [graphique des champs de profil utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)) pour mettre à jour ces valeurs spéciales sur le profil utilisateur dans le tableau de bord ou ajouter vos propres données d'attributs personnalisés à l'utilisateur.

## Corps de l'objet

```json
{
  "aliases_to_identify" : (requis, tableau d'alias pour identifier l'objet)
  [
    {
      "external_id" : (requis, string) voir ID utilisateur externe ci-dessous,
      // external_ids pour les utilisateurs qui n'existent pas retournera une erreur non fatale.
      // Voir les réponses du serveur pour plus de détails.
      "user_alias" : {
        "alias_name" : (obligatoire, chaîne),
        "alias_label" : (obligatoire, chaîne)
      }
    }
  ]
 } } }
```

Pour plus d'informations sur `alias_name` et `alias_label`, consultez notre documentation [Alias utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)
