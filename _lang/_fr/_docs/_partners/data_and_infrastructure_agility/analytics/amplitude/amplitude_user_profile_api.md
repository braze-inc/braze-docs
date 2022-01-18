---
nav_title: API de profil d'utilisateur d'Amplitude
article_title: Points de terminaison de l'API du profil utilisateur
page_order: 0
alias: /fr/partners/amplitude_api_endpoints/
page_type: partenaire
description: "L'API de profil d'utilisateur d'Amplitude sert les profils d'utilisateurs d'Amplitude. Cela inclut les propriétés des utilisateurs, les propriétés des utilisateurs calculés, une liste des identifiants de cohortes de cohortes qui incluent l'utilisateur, et des recommandations."
search_tag: Partenaire
---

# Points de terminaison de l'API du profil utilisateur d'Amplitude

> L'API de profil d'utilisateur d'Amplitude sert les profils d'utilisateurs d'Amplitude. Cela inclut les propriétés des utilisateurs, les propriétés des utilisateurs calculés, une liste des identifiants de cohortes de cohortes qui incluent l'utilisateur, et des recommandations.

## Paramètres de terminaison

Le tableau suivant définit les paramètres que vous pouvez utiliser dans vos appels vers l'API du profil de l'utilisateur, ainsi que les paramètres que vous pouvez généralement vous attendre à voir dans les réponses d'Amplitude.

| Paramètre             | Requis                                | Libellé                                                                                                                                                                                                                                                            |
| --------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ID de l'utilisateur` | Optionnel                             | Identifiant de l'utilisateur (id de base de données externe) à consulter, requis à moins que `device_id` ne soit défini.                                                                                                                                           |
| `id de l'appareil`    | Optionnel                             | ID de périphérique (id anonyme) à interroger requis, à moins que `user_id` ne soit défini.                                                                                                                                                                         |
| `get_recs`            | Optionnel<br>(par défaut false) | Renvoie un résultat de recommandation pour cet utilisateur.                                                                                                                                                                                                        |
| `rec_id`              | Optionnel                             | Recommandation(s) à récupérer, requis si `get_recs` est vrai. Plusieurs recommandations peuvent être récupérées en séparant les `rec_ids` par des virgules.                                                                                                        |
| `rec_type`            | Optionnel                             | Remplace le paramètre de contrôle expérimental par défaut et `rec_type=model` retournera des recommandations modélisées et `rec_type=random` retourne des recommandations aléatoires. D'autres options peuvent exister dans le futur.                              |
| `get_amp_props`       | Optionnel<br>(par défaut false) | Renvoie un ensemble complet de propriétés utilisateur pour cet utilisateur, sans incluant les calculs.                                                                                                                                                             |
| `get_cohort_ids`      | Optionnel<br>(par défaut false) | Renvoie une liste de tous les identifiants de cohorte que cet utilisateur fait partie de ceux qui ont été configurés pour être traqués. Par défaut, l'adhésion à la cohorte n'est pas suivie pour les utilisateurs pour aucune cohorte.                            |
| `get_computations`    | Optionnel<br>(par défaut false) | Renvoie une liste de tous les calculs qui sont activés pour cet utilisateur.                                                                                                                                                                                       |
| `comp_id`             | Optionnel                             | Renvoyer un calcul unique qui pourrait être activé pour cet utilisateur. Elle retournera une valeur nulle si elle n'existe pas. Si `get_computations` est vrai, toutes les valeurs seront récupérées, y compris celle-ci (sauf si elle est archivée ou supprimée). |
{: .reset-td-br-1 .reset-td-br-2}

| Paramètre de réponse    | Libellé                                                                                                                                                                                                                            |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `rec_id`                | L'identifiant de recommandation qui a été demandé.                                                                                                                                                                                 |
| `enfant_rec_id`         | Un identifiant de recommandation plus détaillé que l'Amplitude peut utiliser sur le backend dans le cadre d'une expérience interne pour améliorer la performance du modèle. Dans la plupart des cas, ce sera le même que `rec_id`. |
| `Eléments`              | Liste des recommandations pour cet utilisateur.                                                                                                                                                                                    |
| `est_control`           | vrai si cet utilisateur fait partie du groupe de contrôle.                                                                                                                                                                         |
| `source_recommandation` | Nom du modèle utilisé pour générer cette recommandation                                                                                                                                                                            |
| `dernier_mise à jour`   | Horodatage de la dernière génération et synchronisation de cette recommandation.                                                                                                                                                   |
{: .reset-td-br-1 .reset-td-br-2}

## Points de terminaison d'amplitude communs

### Obtenir une recommandation

#### Endpoint
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_recs=true&rec_id=testRecId`
{% endraw %}
#### Exemple de réponse
```json
{
  "userData": {
    "recommandations": [
      {
        "rec_id": "testRecId",
        "child_rec_id": "testRecId",
        "éléments": [
          "cookie",
          "craquant",
          "lait de chocolat",
          "Donut",
          "croissant"
        ],
        "is_control": false,
        "recommendation_source": "modèle",
        "last_updated": 1608670720
      }
    ],
    "user_id": "testUser",
    "device_id": "ff-ff-ff-ff-ff-ff-ff-ffffff",
    "amp_props": null,
    "cohort_ids": null
  }
}
```

### Obtenir plusieurs recommandations

#### Endpoint
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_recs=true&rec_id=testRecId,testRecId2`
{% endraw %}
#### Exemple de réponse
```json
{
  "userData": {
    "recommandations": [
      {
        "rec_id": "testRecId",
        "child_rec_id": "testRecId",
        "éléments": [
          "cookie",
          "craquelin",
          "lait de chocolat",
          "Donut",
          "croissant"
        ],
        "is_control": false,
        "recommendation_source": "modèle",
        "last_updated": 1608670720
      },
            {
        "rec_id": "testRecId2",
        "child_rec_id": "testRecId2",
        "éléments": [
          "bulgogi",
          "bibimbap",
          "kimchi",
          "croffles",
          "samgyeopsal"
        ],
        "is_control": false,
        "recommendation_source": "model2",
        "last_updated": 1608670658
      }
    ],
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff-ffffff",
    "amp_props": null,
    "cohort_ids": null
  }
}
```

### Obtenir les propriétés de l'utilisateur

#### Endpoint
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_amp_props=true`
{% endraw %}
#### Exemple de réponse
```json
{
  "userData": {
    "recommandations": null,
    "user_id": "testUser",
    "device_id": "ff-ffffff-ffff-ffff-ffffff",
    "amp_props": {
      "library": "http/1. ",
      "first_used": "2020-01-13",
      "last_used": "2021-03-24",
      "number_property": 12,
      "boolean_property": vrai
    },
    "cohort_ids": null
  }
}
```

### Obtenir les identifiants de cohorte

#### Endpoint
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_cohort_ids=true`
{% endraw %}
#### Exemple de réponse
```json
{
  "userData": {
    "recommandations": null,
    "user_id": "testUser",
    "device_id": "ff-ffff-ffff-ff-ff-ffff-ffff-ffffff",
    "amp_props": null,
    "cohort_ids": ["cohort1", "cohort3", "cohort7"]
  }
}
```

### Obtenir un calcul unique

#### Endpoint
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&comp_id=testCompId`
{% endraw %}
#### Exemple de réponse
```json
{
  "userData": {
    "recommandations": null,
    "user_id": "testUser",
    "device_id": "ff-ffff-ffff-ff-ffff-ffffff-ffffff",
    "amp_props": {
      "computed-prop-2": "3"
    },
    "cohort_ids": null
  }
}
```

### Obtenir tous les calculs

#### Endpoint
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_computations=true`
{% endraw %}
#### Exemple de réponse
```json
{
  "userData": {
    "recommandations": null,
    "user_id": "testUser",
    "device_id": "ff-ffffff-ffff-ffff-ffffff",
    "amp_props": {
      "computed-prop-1": "5000000. ",
      "computed-prop-2": "3"
    },
    "cohort_ids": null
  }
}
```

