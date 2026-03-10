---
nav_title: Sélection intelligente
article_title: Sélection intelligente
page_order: 1.0
description: "Cet article décrit la sélection intelligente, une fonctionnalité qui analyse les performances d'une campagne ou d'un Canvas récurrent deux fois par jour et ajuste automatiquement le pourcentage d'utilisateurs recevant chaque variante de message."
search_rank: 10
toc_headers: h2
---

# Sélection intelligente {#intelligent-selection}

> La sélection intelligente est une fonctionnalité qui analyse les performances d'une campagne ou d'un Canvas récurrent deux fois par jour et ajuste automatiquement le pourcentage d'utilisateurs recevant chaque variante de message.

## À propos de la sélection intelligente

Une variante qui semble mieux performer sera envoyée à plus d'utilisateurs, tandis que les variantes sous-performantes seront ciblées vers moins d'utilisateurs. Chaque ajustement est effectué à l'aide d'un [algorithme statistique](https://en.wikipedia.org/wiki/Multi-armed_bandit) qui garantit que Braze ajuste pour de réelles différences de performance et non par hasard.

![Section test A/B d'une campagne avec la sélection intelligente activée.]({% image_buster /assets/img/intelligent_selection1.png %})

La sélection intelligente :
- examine de manière répétée les données de performance et déplace progressivement le trafic de la campagne vers les variantes gagnantes ;
- vérifie que davantage d'utilisateurs reçoivent votre meilleure variante sans sacrifier la confiance statistique ;
- écarte les variantes sous-performantes et identifie les variantes performantes plus rapidement qu'un [test A/B traditionnel]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) ;
- teste plus fréquemment avec une plus grande confiance que vos utilisateurs verront votre meilleur message.

La sélection intelligente fonctionne mieux pour les campagnes qui envoient plus d'une fois. Pour les campagnes à envoi unique, nous recommandons un [test A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) traditionnel.

## Prérequis

Avant d'ajouter la sélection intelligente à votre campagne, assurez-vous que :

- votre campagne s'envoie selon un planning récurrent (les envois uniques ne sont pas pris en charge) ;
- vous avez ajouté au moins deux variantes de message ;
- vous avez défini un événement de conversion pour mesurer les performances entre variantes ;
- la fenêtre de rééligibilité est de 24 heures ou plus (les fenêtres plus courtes ne sont pas prises en charge, car elles affecteraient l'intégrité de la variante de contrôle).

Pour un Canvas : l'étape Message contient au moins deux variantes et au moins un événement de conversion.

Pour les étapes d'ajout aux campagnes et Canvas, la durée d'exécution, la répartition des variantes et la FAQ, consultez la version complète de cet article dans le sommaire à gauche ou l'aide du tableau de bord Braze.
