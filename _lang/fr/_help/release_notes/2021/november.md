---
nav_title: Novembre
page_order: 2
noindex: true
page_type: update
description: "Cet article contient les notes de version de novembre 2021."
---
 
# Novembre 2021

## Tableau de bord d’utilisation des points de données

Utilisez le tableau de bord **Total Data Points Usage** (Utilisation totale des points de données) pour suivre votre consommation de points de données dans le cadre de votre contrat. Ce tableau de bord fournit des informations sur votre contrat, le cycle de facturation actuel, les données de facturation de l’entreprise et les données de facturation du groupe d’apps. Pour plus d’informations, consultez [Abonnements et Utilisation]({{site.baseurl}}/user_guide/onboarding_with_braze/subscription_and_usage/#total-data-points-dashboard).

## Modification de la régénération des extensions de segment

À compter du 1er février 2022, le paramètre pour régénérer les extensions quotidiennement sera désactivé automatiquement pour les [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) (Extensions de segment) non utilisées. Braze définit les extensions non utilisées comme celles qui répondent aux critères suivants :

- Utilisée dans aucune campagne, ni aucun Canvas ou segment actif
- Utilisée dans aucune campagne, ni aucun Canvas ou segment actif (qu’il soit une ébauche, abandonné ou archivé)
- N’a pas été modifiée depuis plus de 7 jours

Braze informera la personne de contact de la société et le créateur de l’extension lorsque ce paramètre est désactivé. L’option permettant de renouveler les extensions quotidiennement peut être réactivée à tout moment.

## Guides d’implémentation avancés Android

### Cartes de contenu

Ce [Guide d’implémentation]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/implementation_guide/) avancé optionnel couvre les considérations du code de carte de contenu, trois cas d’utilisation personnalisés construits par notre équipe, les extraits de code l’accompagnant et les directives sur la journalisation des impressions, des clics et des rejets.

### Messagerie In-App

Ce [Guide d’implémentation]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/implementation_guide/) avancé optionnel couvre les considérations du code des messages in-app, trois cas d’utilisation personnalisés créés par notre équipe et les extraits de code qui l’accompagnent.

### Notifications push

Ce [Guide d’implémentation]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/implementation_guide/) avancé et optionnel couvre les moyens d’exploiter une sous-classe `FirebaseMessagingService` personnalisée pour tirer le meilleur parti de vos messages push. Il contient également un cas d’usage personnalisé créé par notre équipe, les extraits de code l’accompagnant et des directives concernant l’enregistrement d’analytique.

## Nouveaux partenariats Braze

### Adobe - Plateforme de données client

Reposant sur Adobe Experience Platform, la plateforme de données client (CDP) en temps réel d’Adobe aide les entreprises à rassembler des données connues et anonymes provenant de diverses sources d’entreprise pour créer des profils clients qui peuvent être utilisés afin de fournir des expériences client personnalisées sur tous les canaux et appareils en temps réel.

L’intégration entre Braze et [Adobe]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/adobe/) CDP permet aux marques de connecter et de mapper leurs données Adobe (segments et attributs personnalisés) vers Braze en temps réel. Les marques peuvent ensuite se servir de ces données pour offrir des expériences personnalisées et ciblées à ces utilisateurs. 

### Shopify - eCommerce

[Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify/) est une société leader dans le commerce mondial ; elle fournit des outils fiables pour démarrer, développer, commercialiser et gérer une entreprise de vente en détail, quelle que soit sa taille. L’intégration entre Shopify et Braze permet aux marques de connecter leur boutique Shopify de façon transparente avec Braze pour transmettre certains webhooks Shopify. Exploitez les stratégies cross-canal et les Canvas de Braze pour recibler vos utilisateurs avec des messages sur les paniers abandonnés pour les inciter à finaliser leur achat, ou recibler les utilisateurs en fonction de leurs achats précédents.