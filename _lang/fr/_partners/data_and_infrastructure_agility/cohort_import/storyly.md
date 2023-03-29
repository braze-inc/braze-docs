---
nav_title: Storyly
article_title: Storyly
description: "Cet article de référence décrit le partenariat entre Braze et Storyly, un SDK léger qui permet aux propriétaires d’applications de cibler leurs segments et de fournir à Braze davantage de données first-party."
alias: /partners/storyly/
page_type: partner
search_tag: Partenaire

---

# Storyly

> [Storyly](https://www.storyly.io/) est un SDK léger qui apporte du contenu à votre application ou site web. Avec un studio de conception intuitif, des analyses pertinentes et une connectivité transparente, Storyly est un outil puissant pour enrichir l'expérience de l’audience. 

L’intégration Braze et Storyly vous permet d’utiliser vos segments dans Braze en tant qu’audience sur la plateforme Storyly. Grâce à cette intégration, vous pouvez :
- Ciblez vos segments avec du contenu spécifique
- Utilisez les attributs des utilisateurs pour personnaliser le contenu de vos articles

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Storyly | Un compte Storyly est requis pour profiter de ce partenariat. |
| SDK Storyly | Vous devez installer le [SDK Storyly](https://integration.storyly.io/). |
| Clé d’API REST Braze | Une clé API REST Braze avec les autorisations suivantes <br><br> `users.export.ids`<br> `users.export.segments`<br> `segments.list`<br> `segments.details` <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Endpoint REST de Braze | [URL de votre endpoint REST][1]. Votre endpoint dépendra de l’URL Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2}

## Cas d’utilisation

Grâce à l'intégration de Braze et Storyly, les propriétaires d'applications peuvent montrer des histoires à tous les segments dans Braze et personnaliser les histoires avec les attributs des utilisateurs.

Parmi les cas d’utilisation courants figurent les situations suivantes :

__Cibler les segments Braze dans Storyly__<br>Une fois l'intégration terminée, vous pouvez créer une audience Storyly basée sur vos segments Braze. Il peut s'agir d'un segment démographique ou comportemental. Par exemple, ciblez les utilisateurs qui vivent dans un endroit précis, ceux qui effectuent une action spécifique sur votre application, ou ceux qui s'intéressent à des produits spécifiques avec du contenu spécifique pour augmenter la conversion.<br>
__Contenu spécifique avec les attributs utilisateur__<br>Les attributs utilisateur de Braze sont également utilisables dans Storyly pour générer des histoires dynamiques. Il peut s'agir d’un nom d'utilisateur, de produits dans un panier ou même de produits favoris, ce qui permet de fournir aux utilisateurs finaux du contenu personnalisé unique. La personnalisation permet d'augmenter les taux de conversion du contenu et le taux d'engagement global du contenu.

## Intégration de l’exportation de données

L'intégration de Braze Storyly est expliquée dans la vidéo suivante :

{% multi_lang_include video.html id="3-OEqQs48Zw" source="youtube" %}

Assurez-vous que votre intégration Storyly contient des paramètres personnalisés. Ces paramètres seront mis en correspondance avec la propriété utilisateur `external id` de Braze. La mise en œuvre des paramètres personnalisés est expliquée ici pour [iOS](https://integration.storyly.io/ios/personalization-customaudience.html), [Android](https://integration.storyly.io/android/personalization-customaudience.html), [React Native](https://integration.storyly.io/react-native/personalization-customaudience.html), [Flutter](https://integration.storyly.io/flutter/personalization-customaudience.html) et [Web](https://integration.storyly.io/web/personalization-customaudience.html).

Reportez-vous à la documentation [Storyly](https://help.storyly.io/en/articles/6354805-connect-your-braze-audiences-with-storyly) pour plus d’informations.

### Étape 1 : Configurer l'intégration sur le tableau de bord de Storyly

Une intégration doit être créée dans le **Storyly Dashboard > Settings > Integrations > Connect with Braze (Tableau de bord de Storyly > Paramètres > Intégrations > Connexion avec Braze)**. Ici, vous aurez besoin de votre clé API REST de Braze et de l’endpoint REST de Braze. 

### Étape 2 : Obtenez vos segments 

Ensuite, vous pouvez utiliser les segments Braze pour créer une audience Storyly. Celle-ci peut être créée dans le **Storyly Dashboard > Settings > Audiences > New Audience > Create Audience with Braze (Tableau de bord Storyly > Paramètres > Audiences > Nouvelle audience > Créer une audience avec Braze)**.

Ici, il y aura deux options de synchronisation. Sélectionnez **One-time sync (Synchronisation unique)** pour des histoires de campagne spécifiques, ou **Daily Sync (Synchronisation quotidienne)** pour du contenu à long terme.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints