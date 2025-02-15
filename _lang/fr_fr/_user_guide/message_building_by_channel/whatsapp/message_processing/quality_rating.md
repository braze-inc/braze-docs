---
nav_title: Évaluation de la qualité et limites de messagerie
article_title: Évaluation de la qualité et limites de messagerie 
description: "Cet article de référence explique comment Meta influence votre évaluation de la qualité et les limites de messagerie pour le canal WhatsApp."
page_type: partner
search_tag: Partner
page_order: 
channel:
  - WhatsApp
---

# Évaluation de la qualité et limites de messagerie

> Meta influence votre évaluation de qualité et [les limites de messagerie](https://developers.facebook.com/docs/whatsapp/messaging-limits) dès que vous commencez à utiliser le canal WhatsApp, et continuera de les influencer en fonction de votre utilisation de WhatsApp.

## Définitions

| Terme | Définition |
| --- | --- |
| Évaluation de la qualité | Une évaluation basée sur les messages récents que vos clients ont reçus au cours des sept derniers jours. Cette évaluation est déterminée par les commentaires de vos clients, tels que la raison de bloquer votre numéro de téléphone et d'autres problèmes de signalement. Consultez la documentation de Meta pour en savoir plus sur [votre cote de qualité](https://www.facebook.com/business/help/896873687365001).|
| Limite de messagerie | Le nombre maximum de conversations initiées par l'entreprise que vous pouvez commencer avec chacun de vos numéros de téléphone sur une période glissante de 24 heures. |
{: .reset-td-br-1 .reset-td-br-2 }

## Onboarding  

Lorsqu'un nouveau compte WhatsApp Business est créé, Meta utilise une série de facteurs pour déterminer la limite d'envoi initiale. Vous pouvez trouver cette limite dans votre gestionnaire WhatsApp Business, et des détails supplémentaires sur votre page d'aperçu des numéros de téléphone. 

Consultez la documentation de Meta pour en savoir plus sur [vérifier votre limite](https://developers.facebook.com/docs/whatsapp/messaging-limits#checking-your-limit) et [les exigences en matière de numéro de téléphone](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers).

## Débit

Meta commence chaque numéro de téléphone d'entreprise enregistré avec un débit de 80 messages par seconde. Les mises à niveau vers 1 000 messages par seconde peuvent se faire automatiquement ou sur demande. Information. 

Consultez la documentation de Meta pour en savoir plus sur votre [débit](https://developers.facebook.com/docs/whatsapp/cloud-api/overview#throughput).

## Cadencement des modèles

Les modèles marketing récemment créés et les modèles marketing mis en pause qui sont réactivés sont potentiellement soumis à un cadencement. Les critères de sélection de rythme de Meta sont principalement déterminés par l'historique de qualité de votre modèle. Lorsque vous utilisez un modèle de marketing récemment créé ou un modèle de marketing récemment réactivé, les messages seront envoyés normalement jusqu'à ce qu'un seuil non spécifié soit atteint. Une fois ce seuil atteint, les messages suivants utilisant ce modèle seront retenus afin de laisser suffisamment de temps pour les commentaires des clients. 

Consultez la documentation de Meta pour en savoir plus sur le [cadencement des modèles](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/#template-pacing).