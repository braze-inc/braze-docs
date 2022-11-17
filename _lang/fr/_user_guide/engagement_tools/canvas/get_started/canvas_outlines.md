---
nav_title: Grandes lignes du Canvas
article_title: Grandes lignes du Canvas
page_order: 3
page_type: reference
description: "Cet article de référence traite de quatre cas d’utilisation Canvas utiles."
tool: Canvas

---

# Grandes lignes du Canvas

Les Étapes de saisie affichées dans chacune de ces quatre grandes lignes présentent une version précédente d’Étape de saisie Canvas. Pour en savoir plus sur la nouvelle version de l’Étape d’entrée et de l’Assistant d’entrée, consulter [Créer un Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).

## Onboarding : Réservation de restaurant
- **What**: Onboarding des utilisateurs pour leur première réservation
- **When**: Déclenché en début de session
- **Who**: Tous les nouveaux clients
- **Why**: Effectuer un événement personnalisé « réservation terminée »
- **Where**: Notification push, e-mail
- **How**: Canal, contenu (test)

<br>![Onboarding des restaurants][41]

## Vente additionnelle : diffusion de musique
- **What**: Mise à jour des parasites actifs vers l’abonnement premium de base
- **When**: Déclenché après un événement personnalisé de « jalon - 3 heures de musique diffusées »
- **Who**: Tous les clients actifs, mais libres
- **Why**: Effectuer un événement personnalisé « consulter la page de prix"
- **Where**: Notification push, e-mail, Webhook
- **How**: Contenu, remise

<br>![Voyage musical - vente additionnelle][28]

## Abandon du panier : vente au détail de vêtements
- **What**: Rappeler aux clients les achats inachevés
- **When**: Déclenché après l’événement personnalisé « panier abandonné »
- **Who**: Tous les clients enregistrés
- **Why**: Effectuer un achat
- **Where**: Notification push, e-mail
- **How**: Canal, déclencheur (test)

<br>![Abandon du panier - parcours][29]

## Voyage de vacances : compagnie aérienne 
- **What**: Informer les clients des ressources et leur fournir des informations pour les bonnes expériences concernant le vol et la compagnie aérienne
- **When**: Planification quotidienne jusqu’au 1er janvier
- **Who**: Les clients ont effectué une réservation pour un voyage de deux jours via l’application.
- **Why**: Lancer la session
- **Where**: Notification push
- **How**: Canal, cadence (test)

<br>![Parcours de vacances][42]

## Ressources supplémentaires

[![Cours d’apprentissage Braze]{% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/page/courses){: style="float:right;width:120px;border:0;" class="noimgborder"}

L’apprentissage Braze propose plusieurs cours Canvas dédiés, passant en revue des canvas communs. Consultez-les pour obtenir des informations précieuses sur les termes et concepts expliqués dans un mélange de vidéos, cours et exercices interactifs. 
- [Créer des parcours clients avec Canvas](https://learning.braze.com/canvas-course)
- [Canvas utilisateur caduque](https://learning.braze.com/lapsed-user-canvas)
- [Canvas prévu abandonné](https://learning.braze.com/abandoned-intent-canvas)
- [Cas d’utilisation : Onboarding](https://learning.braze.com/onboarding-canvas)
- [Cas d’utilisation de Canvas pour la vente au détail](https://learning.braze.com/canvas-use-cases-for-retail)

[28]:{% image_buster /assets/img_archive/Journey_9.png %}
[29]:{% image_buster /assets/img_archive/Journey_10.png %}
[41]: {% image_buster /assets/img_archive/Journey_8-audience_options.png %}
[42]: {% image_buster /assets/img_archive/Journey_11-audience_options.png %}
