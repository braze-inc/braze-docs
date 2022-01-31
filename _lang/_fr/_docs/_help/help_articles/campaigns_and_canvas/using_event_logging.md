---
nav_title: Utiliser la journalisation des événements
article_title: Utiliser la journalisation des événements
page_order: 6
page_type: Solution
description: "Cet article d'aide décrit comment utiliser la journalisation des événements pour résoudre les problèmes avec votre intégration à Braze."
---

# Utiliser la journalisation des événements

Le [Event User Log][1] vous aide à résoudre tous les problèmes liés à votre intégration à Braze.

Deux étapes particulièrement utiles sont mises en place :
* [Un profil anonyme](#setting-up-an-anonymous-profile)
* [Journal des événements](#using-event-logging)

## Mise en place d'un profil anonyme

Pour configurer un profil anonyme, consultez cet article sur [l'ajout d'utilisateurs de test][2].

## Utiliser la journalisation des événements

Utilisez la journalisation des événements pour tester le comportement d'un utilisateur anonyme. Cela peut être particulièrement utile pour identifier l'identifiant de l'utilisateur si l'application en cours de test ne collecte pas les e-mails. Vous pouvez utiliser Braze avec l'adresse IP de votre appareil pour ajouter cet appareil en tant qu'utilisateur de test.

C'est aussi un excellent moyen de trouver des utilisateurs anonymes. Vous pouvez également utiliser ces informations pour vérifier quelles données sont envoyées à Braze et vérifier s'il y a des divergences. De ce point de vue, vous pouvez identifier si les deltas de vos données sont envoyées à Braze. Si une adresse e-mail ou un jeton push est envoyé avec chaque événement enregistré, toutes les données sont envoyées à Braze.

Vous avez encore besoin d'aide ? Ouvrez un ticket de support []({{site.baseurl}}/braze_support/).

_Dernière mise à jour le 27 mars 2019_

[1]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab
[2]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users