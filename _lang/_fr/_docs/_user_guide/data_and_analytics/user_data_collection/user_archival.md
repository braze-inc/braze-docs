---
nav_title: Définitions d'archivage des utilisateurs
article_title: Archivage de l'utilisateur
page_order: 0
page_type: Référence
description: "Cet article de référence couvre les définitions d'archives des utilisateurs."
---

# Définitions d'archivage de l'utilisateur

Chaque semaine, Braze exécute un processus pour supprimer les utilisateurs inactifs et les utilisateurs dormants des services de Braze.

Ce processus permet de s'assurer que Braze fournit des statistiques précises concernant les publics accessibles aux campagnes. Il sert également en accord avec deux concepts clés du [RGPD][1]:

1. Le principe de limitation du stockage - les données personnelles traitées et stockées ne devraient pas être conservées plus longtemps que nécessaire.
2. Avoir un objectif commercial légitime pour traiter les données à caractère personnel.

C'est-à-dire, Les données à caractère personnel traitées et stockées ne devraient pas être conservées plus longtemps que nécessaire et les données personnelles ne devraient être traitées qu'à des fins commerciales légitimes. Les utilisateurs archivés auront également supprimé leur statut de désinscription conformément au RGPD.

Si vous avez un profil d'utilisateur risque d'être archivé en vertu de ces politiques qui doivent être conservées, enregistrer ensuite un point de données unique à travers notre API REST pour ce profil utilisateur au moins une fois tous les six mois.

## Utilisateurs inactifs

Les « utilisateurs inactifs » sont des utilisateurs qui ne sont pas joignables et qui ont probablement apparié. Les utilisateurs inactifs sont ceux qui répondent à tous ces critères :

- Impossible de recevoir l'e-mail. Par exemple, ils n'ont pas d'adresse e-mail ou sont désabonnés de toutes les listes de courriels.
- Impossible de recevoir les SMS. Par exemple, ils n'ont pas de numéro de téléphone valide ou ils sont désabonnés de tous les groupes d'abonnement SMS.
- Impossible de recevoir push. Par exemple, ils ont désinstallé l'application ou désactivé les autorisations push.
- N'a utilisé aucune application mobile ou visité un site Web dans un groupe d'applications depuis plus de six mois.
- Vous n'avez reçu aucun message d'un groupe d'applications depuis plus de six mois.
- Braze n'a traité aucun point de données pour ce profil utilisateur depuis plus de six mois.

Dans ce cas, ces utilisateurs ne peuvent pas être envoyés par message et ne s'engagent pas avec votre marque. Ces utilisateurs ont effectivement tourné.

## Utilisateurs en sommeil

Les "Utilisateurs Dormants" sont des utilisateurs qui n'ont eu aucune activité au cours des douze derniers mois et:

- N'a utilisé aucune application mobile ou visité un site Web dans un groupe d'applications depuis plus de 12 mois.
- Vous n'avez reçu aucun message d'un groupe d'applications depuis plus de 12 mois.
- Braze n'a traité aucun point de données pour ce profil utilisateur depuis plus de 12 mois.

## Blocage du spam

Braze bloque les utilisateurs individuels avec plus de 5 millions de sessions ("utilisateurs fictifs"), et n'ingère plus leurs événements SDK, car ils sont généralement le résultat d'une intégration incorrecte. Si vous trouvez que cela s'est produit pour un utilisateur légitime, veuillez déposer un ticket avec le support [de Braze]({{site.baseurl}}/braze_support/).

Pour trouver les utilisateurs factices de votre tableau de bord, effectuez les étapes suivantes :

1. Créer un segment []({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).
2. Sélectionnez le filtre `Nombre de sessions` et mettez-le à `plus de 5 000 000`.
3. Exporter le segment via CSV.

Si nécessaire, vous pouvez supprimer les utilisateurs via le point de terminaison de l'API [Utilisateurs Supprimer]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/).

[1]: {{site.baseurl}}/help/dp-technical-assistance/#the-right-to-erasure
