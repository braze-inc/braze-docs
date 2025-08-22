---
nav_title: Gestion du consentement
article_title: Gestion du consentement
page_order: 10
page_type: reference
description: "Cet article de référence fournit des conseils sur la manière de gérer le consentement avec Braze."
---

# Gestion du consentement

> Cet article de référence fournit des conseils sur la manière de gérer le consentement de vos utilisateurs à l'aide de Braze.

Braze ne peut pas fournir de conseils spécifiques sur l'interprétation des lois et des règlements, ni offrir des orientations sur la gestion des consentements, car cela dépendra de l'interprétation de la loi par votre équipe juridique. Cependant, nous proposons une gamme d'outils pour la gestion des abonnements et des consentements.

Votre approche doit dépendre de la rigueur exigée par votre équipe juridique sur la base de son interprétation de la loi. Voici quelques options à envisager, de la plus stricte à la moins stricte :

- **Teams :** Utilisez les [Teams de Braze]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) pour une véritable gouvernance. Il s'agit d'ajouter un attribut personnalisé à tous les profils utilisateurs pour indiquer leur statut de consentement, la date de leur consentement ou les deux. Vous devez ensuite migrer toutes les campagnes et les Teams vers l'équipe désignée et ajuster les autorisations des utilisateurs sur le tableau de bord en conséquence.
- **Attribut du profil utilisateur :** Ajoutez un attribut de consentement à tous les profils utilisateurs. Cet attribut indique si l'utilisateur a donné son consentement ou non. À l'avenir, vous pourrez alors inclure un segment d'utilisateurs ayant consenti (par exemple, `consent = true`) à toutes vos campagnes et Canvases.
- **Groupes d'abonnement spécifiques à un canal :** Manipulez les groupes d'abonnement pour des canaux spécifiques (notifications push, e-mail, etc.) afin de gérer le consentement. Dans un premier temps, marquez les utilisateurs comme étant désabonnés de ces canaux et ne les marquez comme étant abonnés qu'après qu'ils aient donné leur consentement.

{% alert important %}
Consultez votre équipe juridique pour déterminer l'approche appropriée pour la conformité de votre organisation avec les exigences en matière de gestion du consentement.
{% endalert %}

