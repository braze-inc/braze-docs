---
nav_title: Amplitude et contenu connecté
article_title: Amplitude et contenu connecté
page_order: 0
alias: /partners/amplitude_api_endpoints/
page_type: partner
description: "L'API de profil utilisateur d'Amplitude sert les profils des utilisateurs d'Amplitude. Cela inclut les propriétés utilisateur, les propriétés utilisateur calculées, une liste des identifiants de cohortes auxquelles l'utilisateur appartient, ainsi que des recommandations."
search_tag: Partner

---

# Amplitude et contenu connecté

> L'API du profil utilisateur d'Amplitude sert les profils des utilisateurs d'Amplitude. Cela inclut les propriétés utilisateur, les propriétés utilisateur calculées, une liste des identifiants de cohortes auxquelles l'utilisateur appartient, ainsi que des recommandations. Vous trouverez ci-dessous une liste des endpoints communs de l'API Amplitude qui peuvent être utilisés avec le contenu connecté.

## Paramètres de l'endpoint

Le tableau suivant présente les paramètres que vous pouvez utiliser dans vos appels à l'API profil utilisateur.

| Paramètres | Exigée | Description |
| --------- | -------- | ----------- |
| `user_id` | En option | ID de l'utilisateur (ID externe de la base de données) à interroger, obligatoire sauf si `device_id` est défini. |
| `device_id` | En option | ID de l'appareil (ID anonyme) à interroger, obligatoire sauf si `user_id` est défini. |
| `get_recs` | En option<br>(Valeur par défaut : false) | Renvoyer un résultat de recommandation pour cet utilisateur. |
| `rec_id` | En option | Recommandation(s) à récupérer, obligatoire si `get_recs` est vrai. Vous pouvez rechercher plusieurs recommandations en séparant les adresses `rec_ids` par des virgules. |
| `rec_type` | En option | Remplace le paramètre de contrôle expérimental par défaut et `rec_type=model` renvoie des recommandations modélisées et `rec_type=random` des recommandations aléatoires. D'autres options pourraient exister à l'avenir. |
| `get_amp_props` | En option<br>(Valeur par défaut : false) | Renvoyer un ensemble complet de propriétés pour cet utilisateur, à l'exclusion des calculs. |
| `get_cohort_ids` | En option<br>(Valeur par défaut : false) | Renvoie une liste de tous les ID de cohorte dont cet utilisateur fait partie et qui ont été configurés pour faire l'objet d'un suivi. Par défaut, l'appartenance à une cohorte n'est pas suivie pour les utilisateurs, quelle que soit la cohorte. |
| `get_computations` | En option<br>(Valeur par défaut : false) | Retourne une liste de tous les calculs activés pour cet utilisateur. |
| `comp_id` | En option | Renvoyer un calcul unique qui pourrait être activé pour cet utilisateur. Il renverra une valeur nulle s'il n'existe pas. Si `get_computations` est vrai, toutes les valeurs seront récupérées, y compris celle-ci (à moins qu'elle ne soit archivée ou supprimée).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Le tableau suivant couvre les paramètres que vous pouvez le plus souvent vous attendre à voir dans les réponses d'Amplitude.

| Paramètre de réponse | Description |
| ------------------ | ----------- |
| `rec_id` | L’ID de recommandation qui a été demandé. |
| `child_rec_id` | Une id de recommandation plus détaillée qu'Amplitude peut utiliser sur le backend dans le cadre d'une expérience interne visant à améliorer les performances du modèle. Dans la plupart des cas, ce sera la même chose que `rec_id`. |
| `items` | Liste des recommandations pour cet utilisateur. |
| `is_control` | true si cet utilisateur fait partie du groupe de contrôle. |
| `recommendation_source` | Nom du modèle utilisé pour générer cette recommandation |
| `last_updated` | Date à laquelle cette recommandation a été générée et synchronisée pour la dernière fois. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Points d'extrémité de l'Amplitude commune

### Obtenez une recommandation

#### Endpoint
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_recs=true&rec_id=testRecId`
{% endraw %}
#### Exemple de réponse
```json
{
  "userData": {
    "recommendations": [
      {
        "rec_id": "testRecId",
        "child_rec_id": "testRecId",
        "items": [
          "cookie",
          "cracker",
          "chocolate milk",
          "donut",
          "croissant"
        ],
        "is_control": false,
        "recommendation_source": "model",
        "last_updated": 1608670720
      }
    ],
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
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
    "recommendations": [
      {
        "rec_id": "testRecId",
        "child_rec_id": "testRecId",
        "items": [
          "cookie",
          "cracker",
          "chocolate milk",
          "donut",
          "croissant"
        ],
        "is_control": false,
        "recommendation_source": "model",
        "last_updated": 1608670720
      },
            {
        "rec_id": "testRecId2",
        "child_rec_id": "testRecId2",
        "items": [
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
    "device_id": "ffff-ffff-ffff-ffff",
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
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": {
      "library": "http/1.0",
      "first_used": "2020-01-13",
      "last_used": "2021-03-24",
      "number_property": 12,
      "boolean_property": true
    },
    "cohort_ids": null
  }
}
```

### Obtenir les ID des cohortes

#### Endpoint
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_cohort_ids=true`
{% endraw %}
#### Exemple de réponse
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
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
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
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
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": {
      "computed-prop-1": "5000000.0",
      "computed-prop-2": "3"
    },
    "cohort_ids": null
  }
}
```

