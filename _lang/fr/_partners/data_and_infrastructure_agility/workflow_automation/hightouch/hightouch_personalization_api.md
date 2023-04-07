---
nav_title: API de personnalisation Hightouch
article_title: API de personnalisation Hightouch
description: "Cet article de référence décrit l’intégration entre Braze et l’API de personnalisation de Hightouch, un service géré pour héberger une API de données à faible latence basée sur n’importe quel ensemble de données dans votre entrepôt de données cloud. Cet article de référence aborde les cas d’utilisation que l’API de personnalisation Hightouch peut résoudre, les données avec lesquelles elle fonctionne, comment la configurer et comment l’intégrer à Braze."
page_type: partner
search_tag: Partenaire
---

# API de personnalisation Hightouch

> [L’API de personnalisation](https://hightouch.com/docs/destinations/personalization-api) Hightouch est un service géré qui vous permet d’héberger une API de données à faible latence basée sur n’importe quel ensemble de données de votre entrepôt de données cloud.

![][3]

L’intégration de Braze et Hightouch vous permet d’utiliser l’API avec le [contenu connecté Braze](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/) pour extraire des données client ou objet à jour vers vos campagnes ou Canvas au moment de l’envoi.

L’API de personnalisation de Hightouch fournit un endpoint REST à utiliser dans votre configuration Braze. Plus précisément, vous pouvez utiliser l’offre de contenu connecté de Braze pour faire une requête GET à l’API de personnalisation afin de récupérer toutes les informations liées à un identifiant particulier. Les données exposées par cette API peuvent représenter des données client, produit ou tout autre objet. 

![][2]

## Conditions préalables

| Condition| Description|
| ---| ---| 
| [Compte Hightouch](https://app.hightouch.com/login) avec API de personnalisation activée | Un compte [Hightouch de niveau Entreprise](https://hightouch.com/pricing) est requis pour profiter de ce partenariat.|
| Cas d’utilisation définis | Avant de paramétrer l’API, vous devez déterminer votre cas d’utilisation pour cette intégration. Consultez la liste suivante pour les cas d’utilisation courants. |
| Données stockées dans un entrepôt de données cloud ou une autre source | Hightouch s’intègre à [plus de 25 sources de données](https://hightouch.com/integrations) |
| Clé API Hightouch | Cela peut être créé dans **Hightouch > Settings (Paramètres) > API keys (Clés API) > Add API key (Ajouter une clé API)**. |
{: .reset-td-br-1 .reset-td-br-2}

{% tabs %}
{% tab Use Cases %}

### Cas d’utilisation

Avant de commencer, il est utile de planifier exactement comment vous souhaitez utiliser l’API de personnalisation.

Parmi les cas d’utilisation courants figurent les situations suivantes :
- **Recommandations produit** afin de rationaliser l’intégration de recommandations produit personnalisées dans les modèles d’e-mails, les campagnes ou les expériences in-app
- **Alimenter les campagnes marketing personnalisées** en enrichissant les points de contact marketing avec des recommandations produit dynamiques
- **Fournir une personnalisation dans l’application ou sur le Web**, par exemple, des résultats de recherche personnalisés, une tarification basée sur la cohorte et des envois de messages, des recommandations d’articles ou les emplacements des magasins les plus proches
- **Recommandations basées sur des données financières ou médicales** : les données financières ont des exigences strictes auxquelles Hightouch répond via ses [politiques strictes de sécurité des données](https://hightouch.com/docs/security/overview#compliance). Avec Hightouch, vous pouvez créer des segments de clients basés sur des données financières ou médicales sans exposer les attributs sous-jacents utilisés dans vos critères de segmentation.

{% endtab %}
{% tab Datasets %}

### Jeux de données

L’API de personnalisation agit comme un cache pour les données sélectionnées dans votre entrepôt, vous devriez donc déjà y avoir les données de recommandation stockées. Si nécessaire, vous pouvez utiliser Hightouch pour le transformer en fonction d’un modèle. Ce type de données comprend :
- Métadonnées utilisateur telles que la région géographique, l’âge ou d’autres informations démographiques
- Actions ou événements de l’utilisateur, y compris les achats passés, les pages consultées, les clics, etc.

{% endtab %}
{% endtabs %}

## Intégration

### Étape 1 : Connecter la source de données à Hightouch

Les [sources](https://hightouch.com/docs/getting-started/concepts#sources) Hightouch sont l’endroit où vivent les données commerciales de votre organisation. Dans ce cas, c’est là que vos données utilisateur sont stockées.
1. Dans Hightouch, allez dans **Sources Overview (Aperçu des sources) > Add Source (Ajouter une source)**. Sélectionnez votre entrepôt de données comme source.<br><br>
2. Saisissez les informations d’identification pertinentes : elles varieront en fonction de la source. 

Pour plus de détails, reportez-vous à la [documentation](https://hightouch.com/docs) source pertinente.

### Étape 2 : Données du modèle

Les modèles Hightouch définissent les données à extraire de votre source. Pour configurer un nouveau modèle, procédez comme suit :

1. Dans Hightouch, allez dans [**Models overview (Présentation des modèles)**](https://app.hightouch.com/models) > **Add model (Ajouter un modèle)** et sélectionnez la source que vous venez de connecter. <br><br>
2. Ensuite, choisissez une [méthode de modélisation](https://hightouch.com/docs/models/creating-models). Étant donné que toutes vos informations doivent être jointes dans un tableau, vous pouvez utiliser le sélecteur de tableau visuel pour les définir. Vous pouvez également écrire du SQL pour inclure uniquement les colonnes que vous souhaitez ou en vous appuyant sur vos modèles de dbt existants, Looker Looks ou classeurs Sigma.<br><br>
3. Avant de continuer, prévisualisez votre modèle pour vous assurer qu’il interroge les données qui vous intéressent. Par défaut, Braze limite l’aperçu aux 100 premiers enregistrements. Une fois que vous avez validé vos données, cliquez sur **Continue (Continuer)**.<br><br>
4. Nommez votre modèle, par exemple « Recommandations de l’utilisateur ».<br><br>
5. Enfin, sélectionnez une clé principale et cliquez sur **Finish (Terminer)**. Une clé principale doit être une colonne avec des identifiants uniques. Il s’agit également du champ que vous utiliserez pour appeler l’API de personnalisation afin de récupérer les recommandations d’un utilisateur particulier.

### Étape 3 : Configurer l’API de personnalisation

La préparation de l’API pour recevoir les demandes se fait en deux étapes :
- Activer l’API de personnalisation dans les régions les plus proches de votre infrastructure
- Créer des synchronisations pour définir les modèles à matérialiser dans le cache géré par Hightouch

Suivez ces instructions pour effectuer les deux :

1. Dans Hightouch, allez dans [**Destinations**](https://app.hightouch.com/destinations) et sélectionnez l’API de personnalisation Hightouch créée pour vous. Si cette destination n’est pas activée, contactez l’[assistance Hightouch](mailto:friends@hightouch.com).<br><br>
2. Ensuite, sélectionnez la région appropriée. La sélection de la région la plus proche de votre infrastructure réduira vos temps de réponse. Si vous ne voyez pas de région proche de votre infrastructure, contactez l’[assistance Hightouch](mailto:friends@hightouch.com).<br><br>
3. Accédez à la [page d’aperçu des **synchronisations**](https://app.hightouch.com/syncs) et cliquez sur le bouton **Add sync (Ajouter une synchronisation)**. Ensuite, sélectionnez le modèle pertinent et la destination que vous avez précédemment configurée.<br><br> 
4. Saisissez un nom de collection alphanumérique. Les collections sont conceptuellement similaires aux tables de base de données. Chacune doit représenter un type de données particulier, comme les clients ou les factures. Les noms de collection doivent être alphanumériques et feront partie de votre endpoint API de personnalisation.<br><br>
5. Ensuite, spécifiez quelle colonne de votre modèle doit servir d’index principal pour les recherches d’enregistrements. Ce champ doit identifier de manière unique chaque enregistrement de la collection et est souvent identique à la clé principale de votre modèle. L’API de personnalisation prend en charge les recherches sur plusieurs indices. Par exemple, vous pouvez souhaiter récupérer les profils client à l’aide de `user_id`, `anonymous_id` ou `email_address`. Pour activer plusieurs indices, contactez l’[assistance Hightouch](mailto:friends@hightouch.com).<br><br>
6. Utilisez le mappeur de champs pour spécifier les colonnes de votre modèle à inclure dans la charge utile de réponse API. Vous pouvez renommer ces champs et utiliser le mappeur avancé pour appliquer des transformations à l’aide du langage du modèle Liquid.<br><br>
7. Sélectionnez le [comportement de suppression](www.hightouch.com/docs/destinations/personalization-api#delete-behavior) approprié pour votre cas d’utilisation.<br><br>
8. Enfin, cliquez sur **Continue (Continuer)**, puis sélectionnez un [calendrier de synchronisation](https://hightouch.com/docs/syncs/schedule-sync-ui).

Hightouch va maintenant synchroniser les données de votre entrepôt avec une base de données gérée et les exposer via l’API de personnalisation.

### Étape 4 : API de personnalisation des appels via le contenu connecté Braze

Une fois que vous avez configuré votre instance API de personnalisation, vous pouvez l’utiliser comme endpoint de contenu connecté Braze. 

L’API est accessible à l’adresse `https://personalization.{region}.hightouch.com`, par exemple `https://personalization.us-west-2.hightouch.com`. 

Les informations sont disponibles à l’aide de cet endpoint `/v1/collections/:collection_name/records/:index_key/:index_value`.

Par exemple, vous pouvez inclure cet extrait de code dans une campagne ou Canvas :

{% raw %}

```liquid
{% connected_content
     https://personalization.us-west-2.hightouch.com/v1/collections/customer/records/id/12345
     :method get
     :headers {
       "Authorization": "Bearer {{YOUR-API-KEY}}"
  }
     :content_type application/json
     :save customer
%}
```
{% endraw %}

Vous pouvez utiliser la modélisation Liquid pour référencer les propriétés renvoyées dans la charge utile JSON et les utiliser dans vos envois de messages.

Pour l’exemple de charge utile ci-dessous :

```json
{
    "user_id": 12345,
    "full_name": "Jane Doe",
    "lifetime_value": 1492.18,
    "churn_risk": 0.04,
    "90_day_summary": {
        "num_songs_listened": 813,
        "top_genres": [
            "house",
            "techno",
            "ambient"
        ],
        "top_artists": [
            "deadmau5",
            "Marsh",
            "Enamour"
        ],
    },
    "recommendations": {
        "concerts": [
            {
                "artist": "Aphex Twin",
                "location": "San Francisco, CA",
                "event_date": "2023-01-31"
            },
            {
                "artist": "Sultan + Shepard",
                "location": "San Francisco, CA",
                "event_date": "2023-02-25"
            }
        ],
        "upcoming_album_release": {
            "title": "Universal Language",
            "artist": "Simon Doty",
            "label": "Anjunadeep",
            "release_date": "2023-04-28"
        }
    },
}
```

Les références Liquid suivantes renverraient cet exemple de données :

| Modèle Liquid | Exemple renvoyé |
| --- | --- |
| {% raw %}`{{artists.recommendations.concerts[0].artist}}`{% endraw %}| Aphex Twin |
| {% raw %}`{{artists.recommendations.concerts[0].location}}`{% endraw %}| San Francisco, Californie |
| {% raw %}`{{artists.recommendations.upcoming_album_release.title}}`{% endraw %}| Langue universelle |
{: .reset-td-br-1 .reset-td-br-2}

## Résolution des problèmes

Si vous avez des questions, contactez l’[assistance Hightouch](mailto:friends@hightouch.com) pour obtenir de l’aide.

[1]: {% image_buster /assets/img/hightouch/cohort5.png %} 
[2]: {% image_buster /assets/img/hightouch/cohort6.png %}  
[3]: {% image_buster /assets/img/hightouch/cohort7.png %}  
