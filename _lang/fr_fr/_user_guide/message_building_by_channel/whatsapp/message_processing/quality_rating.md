---
nav_title: Cote de qualité et limites des messages
article_title: "Limites de l'évaluation de la qualité et de l'envoi de messages" 
description: "Cet article de référence explique comment Meta influence votre note de qualité et les limites d'envoi de messages pour le canal de communication WhatsApp."
page_type: partner
search_tag: Partner
page_order: 
channel:
  - WhatsApp
---

# Cote de qualité et limites des messages

> Meta influence votre classement de qualité et vos [limites d'envoi de messages](https://developers.facebook.com/docs/whatsapp/messaging-limits) dès le moment où vous commencez à utiliser le canal de communication, et continuera à les influencer en fonction de votre utilisation de WhatsApp.

## Définitions

| Mot | Définition |
| --- | --- |
| Note de qualité | Une évaluation basée sur les messages récents que vos clients ont reçus au cours des sept derniers jours. Cette note est déterminée par les commentaires de vos clients, comme la raison du blocage de votre numéro de téléphone et d'autres problèmes de signalement. Consultez la documentation de Meta pour en savoir plus [sur votre niveau de qualité](https://www.facebook.com/business/help/896873687365001).|
| Limite d'envoi de messages | Le nombre maximum de conversations professionnelles que vous pouvez entamer avec chacun de vos numéros de téléphone sur une période de 24 heures. |
{: .reset-td-br-1 .reset-td-br-2 }

## Onboarding  

Lorsqu'un nouveau compte WhatsApp Business est créé, Meta utilise divers facteurs pour déterminer la limite d'envoi initiale. Vous trouverez cette limite dans votre gestionnaire WhatsApp Business, et des détails supplémentaires sur votre page Informations sur les numéros de téléphone. 

Consultez la documentation de Meta pour en savoir plus sur la [vérification de votre limite](https://developers.facebook.com/docs/whatsapp/messaging-limits#checking-your-limit) et des [exigences en matière de numéro de téléphone](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers).

## Débit

Meta démarre chaque numéro de téléphone professionnel enregistré avec un débit de 80 messages par seconde. Le passage à 1 000 messages par seconde peut se faire automatiquement ou sur demande. Informations. 

Consultez la documentation de Meta pour en savoir plus sur votre [débit](https://developers.facebook.com/docs/whatsapp/cloud-api/overview#throughput).

## Modèles de cadencement

Les modèles de commercialisation récemment créés et les modèles de commercialisation mis en pause qui deviennent non mis en pause sont potentiellement soumis au rythme. Les critères de sélection du rythme de Meta sont principalement basés sur l'historique de la qualité de votre modèle. Lorsque vous utilisez un modèle de marketing récemment créé ou un modèle de marketing récemment désactivé, les messages sont envoyés normalement jusqu'à ce qu'un seuil non spécifié soit atteint. Une fois ce seuil atteint, les messages ultérieurs utilisant ce modèle seront mis en attente afin de laisser suffisamment de temps aux clients pour donner leur avis. 

Consultez la documentation de Meta pour en savoir plus sur la [cadence des modèles](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/#template-pacing).