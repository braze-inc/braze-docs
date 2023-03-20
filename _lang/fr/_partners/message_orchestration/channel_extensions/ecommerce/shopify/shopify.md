---
nav_title: Aperçu
article_title: "Shopify"
description: "Cet article de référence présente le partenariat entre Braze et Shopify, une société de commerce international, qui vous permet de connecter de manière harmonieuse votre boutique Shopify à Braze pour faire passer certains webhooks Shopify dans Braze. Exploitez les stratégies cross-canal de Braze et Canvas pour inciter les clients à compléter leurs achats, ou pour recibler les utilisateurs en fonction de leurs achats précédents."
page_type: partner
search_tag: Partenaire
alias: "/shopify_overview/"
page_order: 0
---

# Shopify

> [Shopify](https://www.shopify.com/) est une société leader dans le commerce mondial. Elle fournit des outils fiables pour démarrer, développer, commercialiser et gérer une entreprise de vente en détail, quelle que soit sa taille. Shopify améliore le commerce pour tous les utilisateurs avec une plateforme et des services conçus pour assurer la fiabilité tout en offrant une meilleure expérience d’achat pour les consommateurs où qu’ils soient. 

L’intégration de Shopify et de Braze permet aux marques de connecter leur boutique Shopify de manière harmonieuse pour transmettre certains événements et clients Shopify dans Braze. Tirez parti des stratégies cross-canales de Braze et de Canvas pour attirer de nouveaux prospects, envoyer des messages à de nouveaux clients ou recibler vos utilisateurs avec des envois de messages non utilisés pour les inciter à finaliser leur achat

## Conditions préalables

Tous les clients de Braze souhaitant utiliser l’intégration Shopify doivent signer le formulaire de commande Shopify de Braze. Contactez votre responsable de compte pour plus de détails.

Cette intégration crée des profils d’utilisateurs alias si nous ne sommes pas en mesure de faire correspondre les données Shopify avec l’e-mail ou le numéro de téléphone ([voir ici pour plus de détails sur le rapprochement des utilisateurs Shopify]({{site.baseurl}}/shopify_processing/#shopify-user-syncing)). Consultez vos équipes de développement au sujet des impacts en aval et de la nécessité de fusionner ces profils d’utilisateurs dans le cadre de votre cycle de vie des utilisateurs avant d’activer l’intégration. 

| Condition | Description |
| ----------- | ----------- |
| Boutique Shopify | Vous devez avoir une boutique [Shopify](https://www.shopify.com) active.<br><br>Notez que, pour le moment, vous ne pouvez connecter qu’une boutique Shopify par groupe d’apps. |
| Segmentation de propriété d’événement activée | Pour vous assurer que vous pouvez segmenter les propriétés de vos événements Shopify, vous devez travailler avec votre gestionnaire du succès des clients ou avec [l’assistance de Braze]({{site.baseurl}}/braze_support/) pour confirmer que la segmentation des propriétés d’événements est activée pour votre tableau de bord. |
| Prise en charge des attributs personnalisés imbriqués | Ceux-ci seront activés avec l’intégration à Shopify.<br><br>Vous aurez accès à cette fonctionnalité pour recevoir les attributs personnalisés d’abonnement au marketing Shopify. |
| Autorisations utilisateur | Vous devez être soit un :<br>• Propriétaire de magasin<br> • Membre du personnel<br>• Membre avec tous les paramètres **Généraux** et de la **Boutique en ligne**, ainsi que ces autorisations d'administration supplémentaires sélectionnées :<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Manage settings<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Voir les applications développées par le personnel et les collaborateurs<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Gérer et installer des applications et des canaux |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Intégration

Grâce à l’intégration clé en main de Shopify dans Braze, vous pouvez :
- Connecter de manière harmonieuse votre boutique Shopify à Braze
- Autoriser Braze à accepter et traiter les données des utilisateurs de Shopify
- Synchroniser les profils d’utilisateur de Shopify dans Braze
- Collecter les abonnements par courriel et par SMS sur votre boutique Shopify pour les synchroniser avec Braze

#### Intégration SDK Web via Shopify ScriptTag (facultatif)

Braze vous permet également d'intégrer notre [intégration SDK Web]({{site.baseurl}}/scripttag_web_sdk_integration/) via ScriptTag dans votre boutique Shopify. Cette intégration nécessite les [prérequis](#prerequisites) ci-dessus, ainsi que ceux qui se trouvent sur la page d'intégration de [ScriptTag]({{site.baseurl}}/scripttag_web_sdk_integration/#prerequisites).

L'implémentation de notre SDK Web via ScriptTag permet de suivre les éléments suivants :
  - [Suivi des utilisateurs anonymes]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#anonymous-user-profiles) pour suivre l’activité des clients dans votre magasin
  - Suivi des [utilisateurs actifs par mois]({{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#monthly-active-users) étant donné que le SDK Web est capable de suivre les données de session des visiteurs de votre boutique
  - Option pour obtenir les données utilisateur Shopify qui compteront dans votre consommation de [point de données]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points#data-points)
  - Option pour activer [messages dans le navigateur]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) comme canal sur votre boutique Shopify
