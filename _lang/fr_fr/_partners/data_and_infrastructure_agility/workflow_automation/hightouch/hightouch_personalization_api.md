---
nav_title: API de personnalisation Hightouch
article_title: API de personnalisation Hightouch
description: "Cet article de référence décrit l'intégration entre Braze et l'API de personnalisation de Hightouch, un service géré permettant d'héberger une API de données à faible latence basée sur n'importe quel ensemble de données de votre entrepôt de données cloud. Cet article de référence passe en revue les cas d'utilisation résolus par l'API Hightouch Personalization, les données avec lesquelles elle fonctionne, comment la configurer et comment l'intégrer à Braze."
page_type: partner
search_tag: Partner
---

# API de personnalisation Hightouch

> L'[API de personnalisation](https://hightouch.com/docs/destinations/personalization-api) de Hightouch est un service géré qui vous permet d'héberger une API de données à faible latence basée sur n'importe quel ensemble de données de votre entrepôt de données cloud.

![][3]

L'intégration de Braze et Hightouch vous permet d'utiliser l'API avec [Braze Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/) pour intégrer des données à jour sur les clients ou les objets à vos campagnes ou Canvases au moment de l'envoi.

L'API de personnalisation de Hightouch fournit un endpoint REST à utiliser dans votre configuration Braze. Plus précisément, vous pouvez utiliser l'offre de contenu connecté de Braze pour effectuer une requête GET à l'API de personnalisation afin de récupérer toutes les informations liées à un identifiant particulier. Les données exposées par cette API peuvent représenter des données relatives à un client, à un produit ou à tout autre objet. 

![][2]

## Conditions préalables

| Condition| Description|
| ---| ---| 
| [Compte Hightouch](https://app.hightouch.com/login) avec l’API de personnalisation activée | Un [compte Hightouch Business Tier](https://hightouch.com/pricing) est nécessaire pour bénéficier de ce partenariat.|
| Cas d'utilisation définis | Avant de configurer l'API, vous devez définir votre cas d'utilisation pour cette intégration. Consultez la liste suivante pour les cas d'utilisation courants. |
| Données stockées dans un entrepôt de données cloud ou une autre source | Hightouch s'intègre à [plus de 25 sources de données](https://hightouch.com/integrations) |
| Clé API Hightouch | Elle peut être créée dans **Hightouch > Paramètres > Clés API > Ajouter une clé API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% tabs %}
{% tab Cas d'utilisation %}

### Cas d'utilisation

Avant de commencer, il est utile de planifier exactement la manière dont vous souhaitez utiliser l'API de personnalisation.

Les cas d'utilisation courants incluent :
- **Recommandations de produits** pour rationaliser l'intégration de recommandations de produits personnalisées dans les modèles d'e-mails, les campagnes ou les expériences intégrées à l'application
- **Promotion de campagnes marketing personnalisées** en enrichissant les points de contact marketing grâce à des recommandations de produits dynamiques
- **Fournir une personnalisation intégrée à l'application ou sur le Web**, par exemple, des résultats de recherche personnalisés, une tarification par cohorte, et l'envoi de messages, des recommandations d'articles ou les emplacements des magasins les plus proches
- **Recommandations basées sur des données financières ou médicales : les données** financières sont soumises à des exigences strictes auxquelles Hightouch répond par le biais de ses politiques de sécurité [des données strictes.](https://hightouch.com/docs/security/overview#compliance) Avec Hightouch, vous pouvez créer des segments de clientèle en fonction de données financières ou médicales sans exposer les attributs sous-jacents utilisés dans vos critères de segmentation.

{% endtab %}
{% tab Ensembles de données %}

### Ensembles de données

L'API de personnalisation fait office de cache pour les données sélectionnées dans votre entrepôt. Les données de recommandation devraient donc déjà y être stockées. Vous pouvez utiliser Hightouch pour le transformer selon un modèle si nécessaire. Ce type de données inclut :
- Les métadonnées de l'utilisateur, telles que la région géographique, l'âge ou d'autres informations démographiques
- Actions ou événements des utilisateurs, y compris les achats précédents, les pages vues, les clics, etc.

{% endtab %}
{% endtabs %}

## Intégration

### Étape 1 : Connecter la source de données à Hightouch

Les [sources](https://hightouch.com/docs/getting-started/concepts#sources) Hightouch sont l'endroit où se trouvent les données commerciales de votre organisation. Dans ce cas, il s'agit de l'endroit où vos données utilisateur sont stockées.
1. Dans Hightouch, accédez à **Aperçu des sources > Ajouter une source**. Sélectionnez votre entrepôt de données comme source.<br><br>
2. Entrez les informations d'identification pertinentes ; elles varient en fonction de la source. 

Pour plus de détails, reportez-vous à la [documentation](https://hightouch.com/docs) de la source correspondante.

### Étape 2 : Données du modèle

Les modèles Hightouch définissent les données à extraire de votre source. Pour configurer un nouveau modèle, procédez comme suit :

1. Dans Hightouch, accédez à [**Aperçu des modèles > Ajouter un**](https://app.hightouch.com/models) **modèle**, puis sélectionnez la source que vous venez de connecter. <br><br>
2. Choisissez ensuite une [méthode de modélisation](https://hightouch.com/docs/models/creating-models). Comme toutes vos informations doivent être réunies dans un seul tableau, vous pouvez utiliser le sélecteur de tableau visuel pour les définir. Vous pouvez également écrire du code SQL pour n'inclure que les colonnes que vous souhaitez ou vous appuyer sur vos modèles DBT, Looker Looks ou Sigma existants.<br><br>
3. Avant de continuer, prévisualisez votre modèle pour vous assurer qu'il interroge les données qui vous intéressent. Par défaut, Braze limite l'aperçu aux 100 premiers enregistrements. Après avoir validé vos données, cliquez sur **Continuer**.<br><br>
4. Donnez un nom à votre modèle, par exemple « Recommandations aux utilisateurs ». «<br><br>
5. Enfin, sélectionnez une clé primaire et cliquez sur **Terminer**. Une clé primaire doit être une colonne contenant des identifiants uniques. C'est également le champ que vous utiliserez pour appeler l'API de personnalisation afin de récupérer les recommandations d'un utilisateur en particulier.

### Étape 3 : Configuration de l'API de personnalisation

La préparation de l'API pour recevoir les requêtes comporte deux étapes :
- Activation de l'API de personnalisation dans les régions les plus proches de votre infrastructure
- Création de synchronisations pour définir quels modèles doivent être matérialisés dans le cache géré par HighTouch

Suivez ces instructions pour effectuer les deux opérations :

1. Dans Hightouch, accédez à [**Destinations**](https://app.hightouch.com/destinations) et sélectionnez l'API de personnalisation Hightouch créée pour vous. Si cette destination n'est pas activée, contactez l'assistance [Hightouch](mailto:friends@hightouch.com).<br><br>
2. Sélectionnez ensuite la région appropriée. La sélection de la région la plus proche de votre infrastructure réduira vos temps de réponse. Si aucune région n'est proche de votre infrastructure, contactez le service d’assistance de [Hightouch](mailto:friends@hightouch.com).<br><br>
3. Accédez à la [page d'aperçu **des synchronisations**](https://app.hightouch.com/syncs) et cliquez sur le bouton **Ajouter une synchronisation**. Sélectionnez ensuite le modèle approprié et la destination que vous avez précédemment configurée.<br><br> 
4. Entrez un nom de collection alphanumérique. Les collections sont conceptuellement similaires aux tables de base de données. Chacune doit représenter un type de données particulier, tel que les clients ou les factures. Les noms des collections doivent être alphanumériques et feront partie intégrante de votre endpoint de l'API de personnalisation.<br><br>
5. Spécifiez ensuite quelle colonne de votre modèle doit servir d'index principal pour les recherches d'enregistrements. Ce champ doit identifier de manière unique chaque enregistrement de la collection et est souvent identique à la clé primaire de votre modèle. L'API de personnalisation prend en charge les recherches sur plusieurs index. Par exemple, vous souhaiterez peut-être récupérer les profils des clients à l'aide des paramètres `user_id`, `anonymous_id` ou `email_address`. Pour activer plusieurs index, contactez le [support Hightouch.](mailto:friends@hightouch.com)<br><br>
6. Utilisez le mappeur de champs pour spécifier quelles colonnes de votre modèle doivent être incluses dans la charge utile de la réponse de l'API. Vous pouvez renommer ces champs et utiliser le mappeur avancé pour appliquer des transformations à l'aide du langage de modèle Liquid.<br><br>
7. Sélectionnez le [comportement de suppression](https://www.hightouch.com/docs/destinations/personalization-api#delete-behavior) adapté à votre cas d'utilisation.<br><br>
8. Enfin, cliquez sur **Continuer**, puis sélectionnez une [planification de synchronisation](https://hightouch.com/docs/syncs/schedule-sync-ui).

Hightouch synchronise désormais les données de votre entrepôt avec une base de données gérée et les expose via l'API de personnalisation.

### Étape 4 : API de personnalisation des appels via Braze Connected Content

Une fois que vous avez configuré votre instance d'API de personnalisation, vous pouvez l'utiliser comme endpoint Braze Connected Content. 

L'API est accessible à l'adresse `https://personalization.{region}.hightouch.com`, par exemple, `https://personalization.us-west-2.hightouch.com`. 

Les informations sont disponibles via cet endpoint `/v1/collections/:collection_name/records/:index_key/:index_value`.

Par exemple, vous pouvez inclure cet extrait de code dans une campagne ou un canvas :

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

Vous pouvez utiliser les modèles Liquid pour référencer les propriétés renvoyées dans la charge utile JSON et les utiliser dans votre envoi de messages.

Pour l'exemple de charge utile ci-dessous :

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
| {% raw %}`{{artists.recommendations.upcoming_album_release.title}}`{% endraw %}| Langage universel |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Résolution des problèmes

Si vous avez des questions, contactez le [service d’assistance de Hightouch](mailto:friends@hightouch.com) pour obtenir de l'aide.

[1]: {% image_buster /assets/img/hightouch/cohort5.png %}
[2]: {% image_buster /assets/img/hightouch/cohort6.png %}  
[3]: {% image_buster /assets/img/hightouch/cohort7.png %}  
