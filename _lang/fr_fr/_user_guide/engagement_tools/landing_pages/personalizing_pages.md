---
nav_title: "Personnalisation des pages d'atterrissage"
article_title: "Personnalisation des pages d'atterrissage"
description: "Cet article explique comment personnaliser les pages d'atterrissage de Braze à l'aide de l'éditeur par glisser-déposer."
page_order: 4
---

# Personnalisation des pages d'atterrissage

> Utilisez la personnalisation liquide dans les pages d'atterrissage pour adapter dynamiquement le contenu grâce aux données du profil utilisateur. Par exemple, vous pouvez personnaliser les titres en fonction de différents attributs de l'utilisateur sans avoir à gérer plusieurs pages d'atterrissage statiques.

{% alert important %}
La personnalisation liquide pour les pages d'atterrissage n'est disponible que sur le niveau Pro des pages d'atterrissage. Actuellement, le [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) et les [codes de promotion]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes) ne sont pas pris en charge avec la personnalisation liquide dans les pages de destination.
{% endalert %}

## Insertion du liquide

Dans l'éditeur par glisser-déposer, vous pouvez insérer la personnalisation des liquides à la fois dans l'éditeur et dans les paramètres de la page ou du bloc dans le panneau de droite. Pour obtenir des instructions sur la mise en œuvre de Liquid, consultez notre [documentation]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#using-liquid-1) dédiée à [Liquid.]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#using-liquid-1)

L'éditeur de pages d'atterrissage avec la personnalisation des liquides a été ajouté.]({% image_buster /assets/img/landing_pages/lp_liquid_.png %})

## Prévisualisation et test

Lorsque vous prévisualisez une page de destination dans l'éditeur, vous pouvez afficher la page en tant qu'utilisateur aléatoire, utilisateur existant ou utilisateur personnalisé.

Cependant, lorsque vous prévisualisez la page de destination à partir du tableau de données ou de la page de **détails de la page de destination**, vous ne pourrez la visualiser qu'en tant qu'utilisateur aléatoire.

## Considérations relatives à la personnalisation

Pour maintenir des performances optimales avec les pages d'atterrissage personnalisées, notez les limites de taille suivantes :

- **Enregistrer une page d'atterrissage :** Si la taille dépasse 500 Ko, vous pouvez recevoir un message d'avertissement indiquant que la page a dépassé nos limites de taille, ce qui peut empêcher sa publication.
- **Rendu avec personnalisation Liquid :** La taille totale ne doit pas dépasser 1 Mo. Dans le cas contraire, la page peut être automatiquement dépubliée par Braze.

### Évitez de dépublier les pages d'atterrissage

Si votre page dépasse ces limites de taille, vous recevrez un e-mail vous informant qu'elle risque d'être dépubliée si elle continue à dépasser la limite. Lorsque le seuil est atteint, la page est automatiquement dépubliée et vous recevez une notification.

Pour éviter que votre page ne dépasse les limites de taille ou ne connaisse des temps de chargement lents, veillez à utiliser la personnalisation Liquid qui :

- Ne passe pas en boucle ou ne fait pas référence à de grands ensembles de données.
- ne repose pas sur une logique mathématique ou conditionnelle poussée au sein du bloc Liquid.

## Pages de repli

Si vos utilisateurs tentent d'accéder à une page qui a été dépubliée, ils verront un message indiquant que la page ne peut pas être chargée actuellement. Les raisons pour lesquelles une page n'a pas été publiée sont les suivantes :

- Liquid complexe ou cassé, ce qui peut entraîner des temps de rendu longs
- Problèmes liés au réseau des utilisateurs
- Dépassement de la taille maximale des pages d'atterrissage
