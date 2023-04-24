---
nav_title: Yotpo
article_title: Yotpo
alias: /partners/yotpo/
description: "Cet article présente le partenariat entre Braze et Yotpo, une plateforme leader de marketing de commerce en ligne qui aide des milliers de marques avant-gardistes à accélérer la croissance des ventes directes au consommateur."
page_type: partner
search_tag: Partenaire
---

# Yotpo

> [Yotpo](https://www.yotpo.com/), plateforme leader de marketing de commerce en ligne, aide des milliers de marques avant-gardistes à accélérer la croissance des ventes directes au consommateur. L’approche de la plateforme unique de Yotpo intègre des solutions basées sur les données pour les évaluations, la fidélisation, le marketing par SMS, et plus encore, permettant aux marques de créer des expériences client plus intelligentes et ciblées sur les conversions.

Grâce à l’intégration de Braze et de Yotpo, vous pouvez extraire et afficher de manière dynamique les meilleures évaluations, les meilleurs avis et le contenu visuel généré par les utilisateurs (CGU) sur les produits dans les e-mails et autres canaux de communication de Braze. Vous pouvez également inclure les données de fidélisation des clients dans les e-mails et autres méthodes de communication pour créer une interaction plus personnalisée, ce qui stimule les ventes et la fidélisation.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Yotpo | Un compte Yotpo est requis pour profiter de ce partenariat. |
| Clé d’API des avis Yotpo | Cette API sera mise en œuvre dans l’extrait de code du Contenu connecté.<br><br>Pour plus d’informations, reportez-vous à [trouver votre clé d’application Yotpo et votre clé secrète](https://support.yotpo.com/en/article/finding-your-yotpo-app-key-and-secret-key). |
| Clé d’API de fidélisation Yotpo | Cette clé d’API et le GUID seront mis en œuvre dans l’extrait de code du Contenu connecté.<br><br>Pour plus d’informations, reportez-vous à [trouver votre clé d’API et votre GUID de fidélisation et de recommandation](https://support.yotpo.com/en/article/finding-your-loyalty-referrals-api-key-and-guid)|
{: .reset-td-br-1 .reset-td-br-2}

Avant de continuer, confirmez que l’ID du produit Yotpo est le même que le `product_id` qui sera extrait dynamiquement de Braze. Celui-ci est obligatoire pour que l’intégration fonctionne. 

Pour trouver votre ID du produit Yotpo, procédez comme suit :

1. Accédez au site Web de votre boutique.
2. Ouvrez la page du produit.
3. Cliquez avec le bouton droit de la souris et sélectionnez **Inspecter**.
4. Appuyez sur <kbd>Ctrl</kbd> + <kbd>F</kbd> et recherchez `yotpo-main` dans le code. La variable `data-product ID` et sa valeur apparaissent dans le div Yotpo.

![Inspecter et rechercher yotpo-main pour trouver la variable data-product-id][1]

## Intégration

Pour intégrer Yotpo et Braze, procédez comme suit :

1. Accédez à votre Tableau de bord de Braze.
2. Sur la page **Campaign (Campagne)**, cliquez sur **Create Campaign (Créer une campagne)** et sélectionnez **Email**.
3. Sélectionnez votre modèle préféré.
4. Cliquez sur **Edit email body (Modifier le corps de l’e-mail)** et ajoutez l’extrait de code de [Contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) pour votre cas d’utilisation :
    - [Afficher le classement par étoiles et le nombre d’avis d’un produit](#star-review-count)
    - [Afficher un récent avis 5 étoiles pour un produit](#five-star-review)
    - [Afficher le CGU visuel par produit](#visual-ugc)
    - [Afficher le solde de fidélisation d’un client dans un e-mail](#loyalty-balance)

### Afficher le classement par étoiles et le nombre d’avis d’un produit {#star-review-count}

Utilisez cet extrait de code pour fournir la note moyenne publique et le nombre total d’avis pour un produit qui est inclus dans l’e-mail :

{% raw %}
```liquid
{% connected_content https://api.yotpo.com/products/<YOTPO-API-KEY>/{{event_properties.${product_id}}}/bottomline :save result %}      

{% if {{result.response.bottomline.average_score}} != 0 %}

The average rating for this product is:

{{result.response.bottomline.average_score}}/5, based on {{result.response.bottomline.total_reviews}} reviews.

{% else %}                    
{% endif %}
```
{% endraw %}

Remplacez `<YOTPO-API-KEY>` avec votre clé d’API d’avis Yotpo. Le `product_id` sera extrait dynamiquement de Braze. Pour que l’intégration fonctionne, le `product_id` dans Braze doit correspondre à l’ID du produit dans Yotpo (généralement l’ID du produit parent du commerce en ligne).

![Remplacez YOTPO-API-KEY par votre clé d’API d’avis Yotpo][2]

### Afficher un récent avis 5 étoiles pour un produit {#five-star-review}

Utilisez cet extrait de code pour fournir le meilleur avis (publié) d’un produit spécifique inclus dans l’e-mail :

{% raw %}
```liquid
{% connected_content https://api.yotpo.com/v1/widget/<YOTPO-API-KEY>/products/{{event_properties.${product_id}}}/reviews.json?per_page=50&star=5&sort=votes_up :save result %}

{% if {{result.response.reviews[0].score}} == 5 %}

Recent 5 Star Review for this product:

{{result.response.reviews[0].content}}

{% else %}              
{% endif %}
```
{% endraw %}

Remplacez `<YOTPO-API-KEY>` avec votre clé d’API d’avis Yotpo. Le `product_id` sera extrait dynamiquement de Braze. Pour que l’intégration fonctionne, le `product_id` dans Braze doit correspondre à l’ID du produit dans Yotpo (généralement l’ID du produit parent du commerce en ligne).

Voici un exemple d’extrait de code dans l’éditeur d’e-mail :

![Exemple d’éditeur d’e-mail montrant l’extrait de code pour les récents avis 5 étoiles][3]

### Afficher le CGU visuel par produit {#visual-ugc}

Utilisez cet extrait de code pour récupérer les images Yotpo balisées et publiées et les ajouter à vos e-mails à la place de l’image de stock ou comme galerie supplémentaire :

{% raw %}
```liquid

{% connected_content https://api.yotpo.com/v1/widget/<YOTPO-API-KEY>/albums/product/{{event_properties.${product_id}}}?per_page=1 :save result %}

{% if {{result.response.images[0].tagged_products[0].image_url}} != null %}

The Visual content of the product: 

<img src="{{result.response.images[0].tagged_products[0].image_url}}" border="0" width="200" height="200" alt="" />

{% else %}

Image return NULL

{% endif %}
```
{% endraw %}

Remplacez `<YOTPO-API-KEY>` avec votre clé d’API d’avis Yotpo. Le `product_id` sera extrait dynamiquement de Braze. Pour que l’intégration fonctionne, le `product_id` dans Braze doit correspondre à l’ID du produit dans Yotpo (généralement l’ID du produit parent du commerce en ligne).

Exemple d’extrait de code :

![Exemple d’éditeur d’e-mail montrant un extrait de code d’images publiées dans Yotpo][4]

### Afficher le solde de fidélisation d’un client dans un e-mail {#loyalty-balance}

Utilisez cet extrait de code pour récupérer le solde des points de fidélisation d’un client et l’utiliser dans votre e-mail :

{% raw %}
```liquid
{% connected_content 

https://loyalty.yotpo.com/api/v2/customers?customer_email=**{{${email_address}}}**
:method get
:headers {
    "x-guid": "<YOTPO-LOYALTY-GUID>",
    "x-api-key": "<YOTPO-LOYALTY-API-KEY>"
        }
:content_type application/json
:save publication
%}

You have {{publication.points_balance}} points

Only {{publication.vip_tier_upgrade_requirements.points_needed}} more points to become part of our VIP Tier!
```
{% endraw %}

Remplacez `<YOTPO-LOYALTY-GUID>` et `<YOTPO-LOYALTY-API-KEY>` par vos identifiants de fidélisation Yotpo. Le `email_address` est extrait dynamiquement de Braze. Pour que l’intégration fonctionne, l’e-mail doit être l’adresse e-mail du client qui reçoit l’e-mail.

Exemple d’extrait de code :

![Exemple d’éditeur d’e-mail montrant un extrait de code du solde des points de fidélisation du client][5]

## Foire aux Questions {#faq}

#### Que faire si je n’ai pas d’avis 5 étoiles ?

Si vous n’avez pas d’avis 5 étoiles (c.-à-d. si la réponse de l’endpoint renvoie NULL pour l’avis 5 étoiles), aucun contenu ne sera affiché.

#### Que faire si je n’ai pas d’image publiée pour un produit ?

Si vous n’avez pas d’image du produit (c.-à-d. si la réponse de l’endpoint renvoie NULL pour l’image du produit), aucun contenu ne sera affiché.

#### Puis-je personnaliser l’aspect et la convivialité, ou extraire d’autres champs de données de Yotpo ?

Oui ! Pour découvrir les autres points de données et les options de personnalisation disponibles, reportez-vous à la section [Effectuer un appel API]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/). Pour ce faire, vous aurez peut-être besoin de l’aide d’un développeur front-end.

{% alert note %}
Yotpo ne prend pas en charge les exigences personnalisées au-delà de ce qui est décrit dans ce guide.
{% endalert %}

[1]: {% image_buster /assets/img/yotpo/image1.png %}
[2]: {% image_buster /assets/img/yotpo/image2.png %}
[3]: {% image_buster /assets/img/yotpo/image3.png %}
[4]: {% image_buster /assets/img/yotpo/image4.png %}
[5]: {% image_buster /assets/img/yotpo/image5.png %}