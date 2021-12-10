---
nav_title: Utiliser la journalisation des événements
article_title: Utiliser la journalisation des événements
page_order: 6
page_type: Solution
description: "Cet article d'aide décrit comment utiliser la journalisation des événements pour résoudre les problèmes avec votre intégration à Braze."
---

# Utiliser la journalisation des événements

Le journal des utilisateurs des événements vous aide à résoudre tous les problèmes liés à votre intégration à Braze.

Deux étapes particulièrement utiles sont :
* [Mise en place d'un profil anonyme](#setting-up-an-anonymous-profile)
* [Configuration de la journalisation des événements](#using-event-logging)

## Mise en place d'un profil anonyme

Pour plus d'informations sur la mise en place d'un profil anonyme à tester au Brésil, consultez le [Journal des utilisateurs d'événements][46] ou la section [Test User][51] du Guide de l'utilisateur.

## Utiliser la journalisation des événements

Utilisez Event Logging pour tester à quoi ressemble un utilisateur anonyme. Cela peut également être utile lorsque l'application que vous testez ne collecte pas d'e-mail et que vous avez du mal à trouver l'ID d'utilisateur. Vous pouvez utiliser Braze avec l'adresse IP de votre appareil pour ajouter cet appareil en tant qu'utilisateur de test.

C'est un excellent moyen de trouver des utilisateurs anonymes. Vous pouvez également utiliser ces informations pour vérifier quelles données sont envoyées à Braze et vérifier les éventuelles anomalies. De ce point de vue, vous pouvez également identifier si les deltas de vos données sont envoyés à Braze. Si une adresse e-mail ou un jeton push est envoyé avec chaque événement enregistré qui indique que toutes les données sont envoyées à Braze.

Vous avez encore besoin d'aide ? Ouvrez un ticket de support []({{site.baseurl}}/braze_support/).

_Dernière mise à jour le 27 mars 2019_

[46]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[51]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users
