---
nav_title: Rapports et informations
article_title: Rapports et informations
description: "Découvrez comment afficher les rapports BrazeAI Decisioning Studio™ dans Braze afin de comprendre l'impact des décisions basées sur l'IA sur vos campagnes."
page_order: 3
---

# Rapports et informations

> Découvrez comment afficher les rapports BrazeAI Decisioning Studio™ dans Braze afin de comprendre l'impact des décisions basées sur l'IA sur vos campagnes. Des indicateurs de performance à la santé des données en passant par les modifications du système, ces rapports vous aident à comprendre les résultats, à résoudre les problèmes et à prendre des décisions avisées en toute confiance.

## Conditions préalables

Avant de pouvoir consulter les rapports Decisioning Studio dans Braze, vous devez :

- Disposer d'un contrat actif pour Braze et BrazeAI Decisioning Studio™. 
- Contactez votre CSM pour qu'il active BrazeAI Decisioning Studio™ en votre nom.
- Disposer d'un agent BrazeAI Decisioning Studio™ en production.

## Afficher les rapports {#view}

Pour afficher les indicateurs d'un agent Decisioning Studio dans Braze, rendez-vous dans **AI Decisioning** > **BrazeAI Decisioning Studio™**, puis sélectionnez un agent.

![Écran d'accueil de BrazeAI Decisioning Studio™ présentant un tableau de bord avec plusieurs fiches de rapport. Chaque fiche montre un type de rapport tel que les performances, les informations, les diagnostics et la chronologie, avec de brèves descriptions et les icônes correspondantes.]( {% image_buster /assets/img/decisioning_studio/reporting_home.png %} )

Vous pouvez y consulter des rapports tels que les performances, les informations, les diagnostics et les chronologies. Pour plus de détails, voir [Rapports disponibles](#available-reports).

## Modifier les dates des rapports

Après avoir [ouvert un rapport](#view), vous pouvez modifier la plage de dates en sélectionnant une nouvelle date de début et de fin dans le menu déroulant du calendrier.

![Sélecteur de plage de dates de BrazeAI Decisioning Studio™ avec un calendrier déroulant. Le calendrier affiche des dates de début et de fin sélectionnables pour personnaliser l'affichage du rapport.]({% image_buster /assets/img/decisioning_studio/reporting_change_date_range.png %}){: style="max-width:50%;"}

Vous pouvez également définir une date de début par défaut ou choisir des dates à exclure systématiquement. Les dates exclues seront filtrées dans tous les rapports de cet agent.

Pour définir ou exclure des dates, sélectionnez <i class="fa-solid fa-gear"></i> **Paramètres**, puis modifiez votre date par défaut ou excluez des dates selon vos besoins.

![Panneau Paramètres ouvert dans BrazeAI Decisioning Studio™ affichant les options permettant de définir une date de début par défaut et d'exclure des dates spécifiques des rapports. Le panneau affiche deux sections intitulées Date de début par défaut et Exclure des dates. Sous Exclure des dates, plusieurs dates s'affichent avec des cases à cocher.]({% image_buster /assets/img/decisioning_studio/reporting_set_exclude_dates.png %})

## Rapports disponibles {#available-reports}

- [Performance]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/performance/) : indicateurs de haut niveau de l'agent comparant les groupes de traitement aux groupes de contrôle, avec les vues **Tendances** et **Arborescence des facteurs**.
- [Informations]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/insights/) : comment les options de recommandation de votre banque d'actions sont générées, y compris les préférences de l'agent et les rapports SHAP.
- [Diagnostics]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/diagnostics/) : santé des données sortantes et entrantes, y compris le volume de recommandations et la surveillance des flux de données.
- [Chronologie]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/timeline/) : un enregistrement visuel des événements clés (exécutions d'agents, modifications de configuration, mises à jour des garde-fous) associé aux indicateurs de performance.