---
nav_title: Yotpo
article_title: Yotpo
alias: /fr/partners/yotpo/
description: "Cet article décrit le partenariat entre Braze et Yotpo, une plateforme de marketing e-Commerce leader qui aide des milliers de marques avant-gardistes à accélérer la croissance directe à la consommation."
page_type: partenaire
search_tag: Partenaire
---

# Yotpo

> [Yotpo](https://www.yotpo.com/), la plateforme de marketing e-Commerce leader , aide des milliers de marques avant-gardistes comme Patagonia, Rebecca Minkoff, MVMT, Tweezerman et Bob’s Discount Furniture accélèrent la croissance directe vers le consommateur. L’approche unique de Yotpo intègre des solutions axées sur les données pour les revues, la fidélisation, le marketing par SMS et bien plus encore, permettant aux marques de créer des expériences clients plus intelligentes et plus convertissantes.

Avec l'intégration entre Yotpo et Braze, vous pouvez dynamiquement tirer et afficher les notes des étoiles, les meilleurs commentaires, et le contenu visuel généré par l'utilisateur (UGC) sur les produits dans les courriels et autres canaux de communication au Brésil. Vous pouvez également inclure des données de fidélisation au niveau du client dans les courriels et d'autres méthodes de communication pour créer une interaction plus personnalisée, boostant les ventes et fidélisation.

## Pré-requis

| Exigences                 | Origine | Libellé                                                                                                                                                                                                                                                                           |
| ------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Clé API Yotpo Reviews     | Yotpo   | Cette clé API sera implémentée dans l'extrait de code de contenu connecté. Pour plus d'informations, reportez-vous à [Trouver votre clé d'application Yotpo et votre clé secrète](https://support.yotpo.com/en/article/finding-your-yotpo-app-key-and-secret-key).                |
| Clé API de fidélité Yotpo | Yotpo   | Cette clé API et GUID seront implémentés dans l'extrait de code de contenu connecté. Pour plus d'informations, reportez-vous à [Trouver votre clé d'API Fidélité & Recommandations et GUID](https://support.yotpo.com/en/article/finding-your-loyalty-referrals-api-key-and-guid) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Avant de continuer, confirmez que l'ID de produit Yotpo est le même que le `product_id` qui sera tiré dynamiquement du Brésil. Ceci est obligatoire pour que l'intégration fonctionne.

Pour trouver votre ID de produit Yotpo, effectuez les étapes suivantes :

1. Accéder au site web de votre boutique.
2. Ouvrir la page du produit.
3. Faites un clic droit et sélectionnez **Inspecter**.
4. Appuyez sur <kbd>Control</kbd> + <kbd>F</kbd> et recherchez `yotpo-main` dans le code. La variable `data-product ID` et sa valeur apparaissent dans le div Yotpo.

!\[Inspecter et rechercher la variable yotpo-main pour trouver la variable ID du produit de données\]\[1\]

## Intégrer Yotpo et Braze

Pour intégrer Yotpo et Braze, effectuez les étapes suivantes :

1. Allez sur votre tableau de bord Braze.
2. Sur la page **Campagnes** , cliquez sur **Créer une campagne** et sélectionnez **Courriel**.
3. Sélectionnez votre modèle préféré.
4. Cliquez sur **Modifier le corps de l'e-mail** et ajoutez le snippet [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) correspondant à votre cas d'utilisation :
    - [Afficher la note en étoiles d'un produit et le nombre de commentaires](#star-review-count)
    - [Afficher une évaluation récente de 5 étoiles pour un produit](#five-star-review)
    - [Afficher l'UGC visuel par produit](#visual-ugc)
    - [Afficher le solde de fidélité d'un client dans un e-mail](#loyalty-balance)

### Afficher la note en étoiles d'un produit et le nombre de commentaires {#star-review-count}

Utilisez ce snippet pour fournir le score moyen public et le nombre total d'avis pour un produit qui est inclus dans l'email:

{% raw %}
```liquid
{% connected_content https://api.yotpo.com/products/<YOTPO-API-KEY>/{{event_properties.${product_id}}}/bottomline :save résultat %}      

{% si {{result.response.bottomline.average_score}} ! 0 %}

La note moyenne pour ce produit est :

{{result.response.bottomline.average_score}}/5, basée sur {{result.response.bottomline.total_reviews}} commentaires.

{% else %}                    
{% endif %}
```
{% endraw %}

Remplacez `<YOTPO-API-KEY>` par votre clé API Yotpo. Le `product_id` sera tiré dynamiquement du Brésil. Pour que l'intégration fonctionne, le `product_id` de Braze doit correspondre à l'ID du produit dans Yotpo (généralement l'identifiant du produit parent eCommerce).

!\[Remplacez YOTPO-API-KEY par votre clé API Yotpo Reviews\]\[2\]

### Afficher une évaluation récente de 5 étoiles pour un produit {#five-star-review}

Utilisez ce snippet pour fournir un avis (publié) pour un produit spécifique qui est inclus dans l'e-mail:

{% raw %}
```liquid
{% connected_content https://api.yotpo.com/v1/widget/<YOTPO-API-KEY>/products/{{event_properties.${product_id}}}/commentaires. son?per_page=50&star=5&sort=votes_up :save result %}

{% if {{result.response.reviews[0].score}} == 5 %}

Récent 5 Star Review pour ce produit :

{{result.response.reviews[0].content}}

{% else %}              
{% endif %}
```
{% endraw %}

Remplacez `<YOTPO-API-KEY>` par votre clé API Yotpo. Le `product_id` sera tiré dynamiquement du Brésil. Pour que l'intégration fonctionne, le `product_id` de Braze doit correspondre à l'ID du produit dans Yotpo (généralement l'identifiant du produit parent eCommerce).

Voici à quoi ressemblera le snippet dans votre éditeur de messagerie:

!\[Exemple d'éditeur d'email montrant un snippet pour les commentaires récents de 5 étoiles\]\[3\]

### Afficher l'UGC visuel par produit {#visual-ugc}

Utilisez ce snippet pour récupérer les images qui ont été taguées et publiées dans Yotpo et ajoutez-les à vos e-mails au lieu de l'image d'origine ou en tant que galerie supplémentaire :

{% raw %}
```liquid

{% connected_content https://api.yotpo.com/v1/widget/<YOTPO-API-KEY>/albums/product/{{event_properties.${product_id}}}?per_page=1 :save résultat %}

{% if {{result.response.images[0].tagged_products[0].image_url}} ! null %}

Le contenu visuel du produit : 

<img src="{{result.response.images[0].tagged_products[0].image_url}}" border="0" width="200" height="200" alt="" />

{% else %}

Image retournée NULL

{% endif %}
```
{% endraw %}

Remplacez `<YOTPO-API-KEY>` par votre clé API Yotpo. Le `product_id` sera tiré dynamiquement du Brésil. Pour que l'intégration fonctionne, le `product_id` de Braze doit correspondre à l'ID du produit dans Yotpo (généralement l'identifiant du produit parent eCommerce).

Le snippet ressemblera à ceci :

!\[Exemple d'éditeur d'email montrant snippet d'images publiées dans Yotpo\]\[4\]

### Afficher le solde de fidélité d'un client dans un e-mail {#loyalty-balance}

Utilisez ce snippet pour récupérer le solde des points de fidélité d'un client et utilisez-le dans votre e-mail :

{% raw %}
```liquid
{% connected_content 

https://loyalty.yotpo. om/api/v2/customers? ustomer_email=**{{${email_address}}}**
:method get
:headers {
    "x-guid": "<YOTPO-LOYALTY-GUID>",
    "x-api-key": "<YOTPO-LOYALTY-API-KEY>"
        }
:content_type application/json
:save publication
%}

Vous avez {{publication.points_balance}} points

Seulement {{publication.vip_tier_upgrade_requirements.points_needed}} points de plus pour devenir membre de notre niveau VIP !
```
{% endraw %}

Remplacez `<YOTPO-LOYALTY-GUID>` et `<YOTPO-LOYALTY-API-KEY>` par vos identifiants de fidélité Yotpo, comme expliqué dans les [conditions préalables](#prerequisites) ci-dessus. L' `email_address` est tiré dynamiquement du Brésil. Pour que l'intégration fonctionne, l'email doit être l'adresse email du client qui reçoit l'email.

Le snippet ressemblera à ceci :

!\[Exemple d'éditeur d'e-mail montrant un snippet de la balance de fidélité des clients\]\[5\]

## Foire aux questions {#faq}

#### Que se passe-t-il si je n'ai pas de commentaire 5 étoiles ?

Si vous n'avez pas d'avis 5 étoiles (c.-à-d. si la réponse de terminaison renvoie NULL pour la revue 5 étoiles), alors aucun contenu ne sera affiché.

#### Que se passe-t-il si je n'ai pas d'image publiée pour un produit ?

Si vous n'avez aucune image pour un produit (i.e. si la réponse du point de terminaison renvoie NULL pour l'image du produit), alors aucun contenu ne sera affiché.

#### Puis-je personnaliser l’apparence et l’ambiance ou retirer d’autres champs de données de Yotpo?

Oui ! Pour découvrir les autres points de données et options de personnalisation disponibles, reportez-vous à [Passer un appel API](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/). Il se peut que vous ayez besoin d'aide d'un développeur front-end pour le faire.

{% alert note %}
Yotpo ne prend pas en charge les exigences sur mesure au-delà de ce qui est décrit dans ce guide.
{% endalert %}
[1]: {% image_buster /assets/img/yotpo/image1.png %} [2]: {% image_buster /assets/img/yotpo/image2.png %} [3]: {% image_buster /assets/img/yotpo/image3. ng %} [4]: {% image_buster /assets/img/yotpo/image4.png %} [5]: {% image_buster /assets/img/yotpo/image5.png %}