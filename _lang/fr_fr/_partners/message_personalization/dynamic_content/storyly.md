---
nav_title: Storyly
article_title: Storyly
description: "Cet article de référence présente le partenariat entre Braze et Storyly, un SDK léger, qui permet aux propriétaires d'applications de cibler leurs segments et d’alimenter Braze avec davantage de données first-party."
alias: /partners/storyly/
page_type: partner
search_tag: Partner

---

# Storyly

> [Storyly](https://www.storyly.io/) est un SDK léger qui intègre des récits à votre application ou site web. Avec un studio de conception intuitif, des analyses pertinentes et une connectivité homogène, Storyly est un outil puissant pour enrichir l'expérience de l'audience. 

_Cette intégration est maintenue par Storyly._

## À propos de l'intégration

L'intégration entre Braze et Storyly vous permet d'utiliser vos segments dans Braze comme audience dans la plateforme Storyly. Grâce à cette intégration, vous pouvez :
- Ciblez vos segmentations avec des histoires spécifiques
- Utilisez les attributs de l'utilisateur pour personnaliser le contenu de votre histoire.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Storyly | Un compte Storyly est nécessaire pour profiter de ce partenariat. |
| Storyly SDK | Vous devez installer le [SDK de Storyly.](https://integration.storyly.io/) |
| Clé API REST de Braze | Une clé API REST de Braze avec les autorisations suivantes <br><br> `users.export.ids`<br> `users.export.segments`<br> `segments.list`<br> `segments.details` <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| Endpoint REST de Braze | [L'URL de votre endpoint REST.][1] Votre endpoint dépendra de l'URL de Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d'utilisation

Grâce à l'intégration de Braze et de Storyly, les propriétaires d'apps peuvent montrer des histoires à tous les segments dans Braze et personnaliser les histoires avec des attributs d'utilisateur.

Les cas d'utilisation les plus courants sont les suivants :

__Cibler les segments Braze dans Storyly__<br>Une fois l'intégration terminée, vous pouvez créer une audience Storyly basée sur vos segments Braze. Il peut s'agir d'un segment démographique ou comportemental. Par exemple, ciblez les utilisateurs qui habitent dans un emplacement/localisation spécifique, ceux qui effectuent une action précise sur votre appli, ou ceux qui s'intéressent à des produits spécifiques avec des histoires précises pour augmenter la conversion.<br>
__Histoires personnalisées avec les attributs de l'utilisateur__<br>Les attributs des utilisateurs de Braze sont également utilisables dans Storyly pour générer des histoires dynamiques. Il peut s'agir du nom d'un utilisateur, de produits dans un panier ou même de produits favoris, offrant ainsi aux utilisateurs des histoires personnalisées uniques. La personnalisation permet d'augmenter les taux de conversion des stories et le taux d'engagement global des stories.

## Intégration de l'exportation des données

L'intégration de Braze Storyly est expliquée dans la vidéo suivante :

{% multi_lang_include video.html id="3-OEqQs48Zw" source="youtube" %}

Assurez-vous que votre intégration Storyly contient des paramètres personnalisés. Ces paramètres seront adaptés à la propriété de l'utilisateur de Braze `external id`. La mise en œuvre des paramètres personnalisés est expliquée ici pour [iOS](https://integration.storyly.io/ios/personalization-customaudience.html), [Android](https://integration.storyly.io/android/personalization-customaudience.html), [React Native](https://integration.storyly.io/react-native/personalization-customaudience.html), [Flutter](https://integration.storyly.io/flutter/personalization-customaudience.html) et [Web](https://integration.storyly.io/web/personalization-customaudience.html).

Vous pouvez également vous référer à la documentation de [Storyly](https://docs.storyly.io/page/connect-your-braze-audiences-with-storyly) pour plus d'informations.

### Étape 1 : Paramétrer l'intégration sur le tableau de bord de Storyly.

Une intégration doit être créée dans le **tableau de bord de Storyly > Paramètres > Intégrations > Connexion avec Braze.** Ici, vous aurez besoin de votre clé API REST de Braze et de l'endpoint REST de Braze. 

### Étape 2 : Obtenez vos segmentations 

Ensuite, vous pouvez utiliser des segments de Braze pour créer une audience Storyly. Celle-ci peut être créée dans le **tableau de bord de Storyly > Paramètres > Audiences > Nouvelle audience > Créer une audience avec Braze**.

Ici, il y a deux options de synchronisation. Sélectionnez la **synchronisation ponctuelle** pour les articles de campagne spécifiques, ou la **synchronisation quotidienne** pour les articles à long terme.


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints