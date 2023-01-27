---
nav_title: Amplitude et Contenu connecté
article_title: Amplitude et Contenu connecté
page_order: 0
description: "Cet article présente le partenariat entre Braze Currents et Amplitude, une plateforme d’aide à la décision et d’analyse de produits."
page_type: partner
tool: Currents
search_tag: Partenaire

---

# Amplitude et Contenu connecté

> L’API des profils utilisateur d’Amplitude est utilisée pour les profils utilisateur Amplitude. Cela inclut les propriétés utilisateur, les propriétés calculées de l’utilisateur, la liste des ID de cohorte pour les cohortes qui incluent l’utilisateur et des recommandations. La liste suivante répertorie les endpoints communs de l'API Amplitude qui peuvent être utilisés avec le contenu connecté.

## Paramètres des endpoints

Le tableau suivant présente les paramètres que vous pouvez utiliser dans vos appels d’API de profil utilisateur.

| Paramètre | Requis | Description |
| --------- | -------- | ----------- |
| `user_id` | Facultatif | ID utilisateur (ID de base de données externe) à interroger, requis, sauf si `device_id` est défini. |
| `device_id` | Facultatif | ID de dispositif (ID anonyme) à interroger, requis, sauf si `user_id` est défini. |
| `get_recs` | Facultatif<br>(Valeurs par défaut est « false » (faux)) | Renvoie un résultat de recommandation pour cet utilisateur. |
| `rec_id` | Facultatif | Recommandation(s) à récupérer, requises si `get_recs` est vrai. Plusieurs recommandations peuvent être récupérées en séparant le `rec_ids` avec des virgules. |
| `rec_type` | Facultatif | Remplace le paramètre de contrôle expérimental par défaut et `rec_type=model` renverra des recommandations modélisées et `rec_type=random` renverra des recommandations aléatoires. D’autres options peuvent être disponibles à l’avenir. |
| `get_amp_props` | Facultatif<br>(Valeurs par défaut est « false » (faux)) | Renvoie un ensemble complet de propriétés utilisateur pour cet utilisateur, sans inclure les calculs. |
| `get_cohort_ids` | Facultatif<br>(Valeurs par défaut est « false » (faux)) | Renvoie la liste de tous les ID de cohorte dont cet utilisateur fait partie et qui ont été configurés pour être suivis. Par défaut, l’adhésion de la cohorte n’est pas suivie pour les utilisateurs, quelle que soit leur cohorte. |
| `get_computations` | Facultatif<br>(Valeurs par défaut est « false » (faux)) | Renvoie une liste de tous les calculs activés pour cet utilisateur. |
| `comp_id` | Facultatif | Renvoie un seul calcul pouvant être activé pour cet utilisateur. Il renvoie une valeur nulle si elle n’existe pas. Si `get_computations` est vrai, toutes les valeurs seront récupérées, y compris celle-ci (sauf si elles sont archivées ou supprimées).|
{: .reset-td-br-1 .reset-td-br-2}

Le tableau suivant couvre les paramètres que vous pouvez généralement voir apparaître dans les réponses d’Amplitude.

| Paramètre de réponse | Description |
| ------------------ | ----------- |
| `rec_id` | L’ID de recommandation demandé. |
| `child_rec_id` | Un ID de recommandation plus détaillé qu’Amplitude peut utiliser en back-end dans le cadre d’une expérience interne pour améliorer la performance du modèle. Dans la plupart des cas, il s’agit d’une même ID que `rec_id`. |
| `items` | Liste des recommandations pour cet utilisateur. |
| `is_control` | Vrai si cet utilisateur fait partie du groupe de contrôle. |
| `recommendation_source` | Nom du modèle utilisé pour générer cette recommandation |
| `last_updated` | Horodatage de la dernière génération et synchronisation de cette recommandation. |
{: .reset-td-br-1 .reset-td-br-2}

## Endpoints courants d’Amplitude

### Obtenir une recommandation

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
        "recommendation_source": "modèle",
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
        "recommendation_source": "modèle",
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

### Obtenir les propriétés utilisateur

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

### Obtenir des ID de cohorte

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

### Obtenir un seul calcul

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

```json
// Impression de la carte de contenu
// Carte de contenu cliquée
// Carte de contenu rejetée
{
  "card_id": (string) identifiant de la carte de contenu qui a été consultée/cliquée/ignorée,
  "app_id": (string) identifiant de l'application sur laquelle l'action de l'utilisateur s'est produite,
  "campaign_id": (string) id de la campagne si provenant d'une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) id de la variation du message si provenant d'une campagne,
  "canvas_id": (string) id du Canvas s'il provient d'un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) id de la variation Canvas dans laquelle se trouve l'utilisateur s'il provient d'un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l'utilisateur s'il provient d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message s'il provient d'un Canvas,
  "canvas_step_name": (string) nom de l'étape pour ce message s'il provient d'un Canvas,
  "send_id": (string) id du message si spécifié pour la campagne (voir Send Identifier sous REST API Parameter Definitions),
  "platform": (string) plateforme de l'appareil (iOS, Android, web, etc.),
  "os_version": (string) version du système d'exploitation de l'appareil utilisé pour l'action,
  "device_model": (string) modèle matériel de l'appareil
}
```

### Événements de fil d’actualité

```json
// Impression de la carte de fil d’actualité
{
  "card_id": (string) identifiant de la carte qui a été visualisée,
  "app_id": (string) identifiant de l'application sur laquelle l'action de l'utilisateur s'est produite,
  "platform": (string) plateforme de l'appareil (iOS, Android, web, etc.),
  "os_version": (string) version du système d'exploitation de l'appareil utilisé pour l'action,
  "device_model": (string) modèle matériel de l'appareil
}
// Clics sur la carte de fil d’actualité
{
  "card_id": (string) identifiant de la carte qui a été cliquée,
  "app_id": (string) identifiant de l'application sur laquelle l'action de l'utilisateur s'est produite,
  "platform": (string) plateforme de l'appareil (iOS, Android, web, etc.),
  "os_version": (string) version du système d'exploitation de l'appareil utilisé pour l'action,
  "device_model": (string) modèle matériel de l'appareil
}
// Impression du fil d'actualité
{
  "app_id": (string) identifiant de l'application sur laquelle l'action de l'utilisateur s'est produite,
  "platform": (string) plateforme de l'appareil (iOS, Android, web, etc.),
  "os_version": (string) version du système d'exploitation de l'appareil utilisé pour l'action,
  "device_model": (string) modèle matériel de l'appareil
}
```

### Événements de désinstallation

```json
// Désinstallation
{
  "app_id": (string) identifiant de l'application sur laquelle l'action de l'utilisateur s'est produite
}
```

### Événements de conversion

```json
// Événements de conversion de campagne
{
  "campaign_id": (string) id de la campagne,
  "campaign_name": (string) nom de la campagne,
  "conversion_behavior_index": (int) index du comportement de conversion,
  "conversion_behavior": (string) chaîne de caractères encodée en JSON décrivant le comportement de conversion,
  "message_variation_id": (string) id de la variation du message,
  "send_id": (string) id du message si spécifié pour la campagne (voir Send Identifier sous REST API Parameter Definitions)
}
// Événements de conversion Canvas
{
  "canvas_id": (string) id du Canvas s'il provient d'un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) id de la variation Canvas dans laquelle se trouve l'utilisateur s'il provient d'un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l'utilisateur s'il provient d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message s'il provient d'un Canvas,
  "canvas_step_name": (string) nom de l'étape pour ce message s'il provient d'un Canvas,
  "conversion_behavior_index": (int) index du comportement de conversion,
  "conversion_behavior": (string) chaîne de caractères encodée en JSON décrivant le comportement de conversion
}
```

### Événements d’entrée Canvas

```json
// Entrée Canvas
{
  "canvas_id": (string) id du Canvas s'il provient d'un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) id de la variation Canvas dans laquelle se trouve l'utilisateur s'il provient d'un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l'utilisateur s'il provient d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message s'il provient d'un Canvas,
  "canvas_step_name": (string) nom de l'étape pour ce message s'il provient d'un Canvas,
  "in_control_group": (boolean) si l'utilisateur était inscrit dans le groupe de contrôle pour un Canvas
}
```

### Événements d’inscription à la campagne

```json
// Inscription au groupe de contrôle de campagne
{
  "campaign_id": (string) id de la campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) id de la variation du message,
  "send_id": (string) id du message si spécifié pour la campagne (voir Send Identifier sous REST API Parameter Definitions)
}
```
[support]: {{site.baseurl}}/braze_support/
