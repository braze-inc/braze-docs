---
nav_title: Intégration standard de Shopify avec tags tiers
article_title: "Intégration standard de Shopify avec tags tiers"
description: "Cet article de référence explique comment configurer l'intégration standard de Shopify avec un outil d'étiquetage tiers."
page_type: partner
search_tag: Partner
alias: /shopify_standard_integration_third_party_tagging/
page_order: 2
---

# Intégration standard de Shopify avec un outil de tags tiers.

> Cette page vous guide dans l'utilisation d'outils tiers, comme Google Tag Manager, avec l'[intégration standard de Shopify]({{site.baseurl}}/shopify_standard_integration/) pour initialiser et charger le SDK Web de Braze.

Pour les boutiques en ligne Shopify, nous vous recommandons d'utiliser la méthode d'intégration standard de Braze pour prendre en charge les SDK de Braze sur votre site. Toutefois, nous comprenons que vous puissiez préférer utiliser un outil tiers, comme Google Tag Manager. Si vous choisissez d'utiliser un outil tiers avec le connecteur Shopify de Braze, gardez à l'esprit que l'intégration Braze et l'app embed géreront le SDK pendant le processus de paiement.

## Conditions

- **Clé API cohérente entre votre outil tiers et le connecteur Shopify :** La clé API doit être cohérente entre Braze et votre outil tiers. Cela permet d'éviter la création d'utilisateurs en double et de maintenir la compatibilité entre les SDK. 
  - **Emplacement/localisation de la clé API :** Après avoir onboardé le chemin d'intégration standard, l'intégration créera automatiquement une application web Braze nommée "Shopify". Récupérez la clé API au sein de l'intégration qui est utilisée avec la configuration de votre outil tiers. 
- **Des versions de SDK cohérentes entre votre outil tiers et le connecteur Shopify :** La version du SDK doit être `5.4` dans votre outil tiers. L'utilisation d'un numéro de version incorrect peut entraîner des problèmes d'incompatibilité, car certaines méthodes du SDK peuvent ne pas exister dans les anciennes versions.
- **Cohérence du calendrier d'initialisation du SDK :** Dans les paramètres d'intégration standard de Shopify, vous pouvez sélectionner les SDK à initialiser au démarrage de la session ou lors de l'identification d'un compte. Ce paramètre doit être cohérent entre votre outil tiers et Braze. Les incohérences pourraient entraîner des problèmes en aval pour l'utilisateur et la synchronisation des données. 

{% alert note %}
Nous vous recommandons d'utiliser exclusivement la méthode d'intégration standard plutôt que de l'utiliser en tandem avec des gestionnaires d'étiquettes tiers, ce qui peut entraîner des conflits entre le SDK de Braze et les outils tiers. Si vous utilisez un outil tiers, testez-le pour vous assurer que tout fonctionne comme prévu.
{% endalert %}

## Mise en place de l'intégration avec un outil tiers

Si vous ne suivez pas les étapes indiquées, vous risquez d'être confronté à des problèmes inattendus ; veillez donc à les respecter scrupuleusement.

1. Suivez les étapes fournies dans la [configuration de l'intégration standard de Shopify]({{site.baseurl}}/shopify_standard_integration/). Lors de l' [activation des SDK Web]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration/#step-2-enable-braze-web-sdks) de Braze, cochez la case indiquant que vous utilisez un outil tiers pour ajouter le SDK Web de Braze à votre site Shopify.

![La section "Paramètres du SDK de Braze" comporte une case à cocher indiquant que vous utiliserez un outil tiers pour ajouter le SDK Web de Braze.]({% image_buster /assets/img/Shopify/third_party_enable.png %}){: style="max-width:80%;"}

{: start="2"}
2\. Allez dans **Paramètres** > **Paramètres de l'application**, sélectionnez l'application web **Shopify**, puis copiez la **clé API pour Shopify on Web.**
3\. Collez la clé API dans la configuration du SDK web de votre outil tiers et définissez la version du SDK sur `5.4`.

## Capturer les données de Shopify et synchroniser les utilisateurs

Tant que le SDK Web est accessible sur le front-end de votre site Shopify via un outil tiers, l'intégration standard capturera les données de Shopify et synchronisera les utilisateurs comme prévu.

## Considérations et clauses de non-responsabilité

- **Paramètres d'initialisation :** Si vous modifiez vos paramètres d'initialisation via votre outil third-party, la synchronisation des utilisateurs et des données peut être impactée. Par exemple, si vous choisissez d'initialiser votre SDK lorsqu'un formulaire de consentement aux cookies est accepté, Braze ne recevra pas de suivi des utilisateurs anonymes ou des données tant que l'utilisateur n'aura pas donné son consentement. 
- **La définition d'attributs directement par le biais de `dataLayer` n'est pas prise en charge :** Utilisez `window.braze` au lieu de `dataLayer` pour définir les attributs.
- **Utilisateurs potentiels en double :** Si la clé API ne correspond pas entre Braze et votre outil tiers, des utilisateurs en double peuvent être créés.
- **Incompatibilité du SDK :** L'utilisation d'un numéro de version incorrect peut entraîner des problèmes avec les méthodes du SDK.