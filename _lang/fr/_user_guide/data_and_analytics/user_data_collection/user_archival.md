---
nav_title: Définitions des archives utilisateur
article_title: Archives utilisateur
page_order: 0
page_type: reference
description: "Cet article de référence couvre les définitions d’archives utilisateur."

---
# Définitions des archives utilisateur

Chaque semaine, Braze exécute un processus visant à supprimer les utilisateurs inactifs et dormants dans les services Braze.

Ce processus garantit que Braze fournit des statistiques précises sur les publics accessibles à la campagne. Il permet aussi de se conformer à deux concepts clés du [RGPD][1]:

1. Le principe de limitation du stockage -les données personnelles traitées et stockées ne doivent pas être conservées plus longtemps que nécessaire
2. Il faut avoir un objectif commercial légitime pour traiter les données personnelles.

C’est-à-dire que les données à caractère personnel traitées et conservées ne doivent être conservées plus longtemps que nécessaire et que les données personnelles ne doivent être traitées qu’à des fins professionnelles légitimes. Les utilisateurs archivés auront également leur statut de désabonnement supprimé conformément au RGPD.

Si vous avez un profil utilisateur que vous souhaitez conserver mais qui risque d’être archivé en vertu de ces politiques enregistrez un point de données unique via notre API REST pour ce profil d’utilisateur au moins une fois tous les six mois.

## Utilisateurs actifs

Braze définit un « utilisateur actif » pendant une période donnée comme tout utilisateur qui a une session dans cette période. 

Si un utilisateur perd la connectivité, nous mettrons les données de session en cache localement et les enverrons lorsque l’utilisateur retrouve une connexion réseau. Ces sessions seront également appliquées au nombre d’utilisateurs actifs. De plus, si votre application a un processus d’inscription, Braze comptera tous les utilisateurs comme actifs, qu’ils soient enregistrés ou non.

Si vous définissez des ID utilisateur pour identifier les utilisateurs lorsqu’un nouvel utilisateur se connecte, il sera compté comme un utilisateur actif séparé. Les utilisateurs mis à jour via l’API seront également comptés comme utilisateurs actifs dans la période où ils ont été mis à jour.

## Utilisateurs inactifs

Les utilisateurs inactifs sont des utilisateurs qui ne sont pas joignables et qui sont probablement churnés. Les utilisateurs inactifs sont ceux qui répondent à tous ces critères :

- Ne peuvent pas recevoir un e-mail. Par exemple, ils n’ont pas d’adresse e-mail ou ils sont désabonnés à toutes les listes de diffusion.
- Ne peuvent pas recevoir de SMS. Par exemple, ils n’ont pas de numéro de téléphone valide, ou ils sont désabonnés de tous les groupes d’abonnement SMS.
- Ne peuvent pas recevoir des notifications push. Par exemple, ils ont désinstallé l’application ou désactivé la notification push dans les permissions.
- N’ont utilisé aucune application mobile ou visité un site Internet dans un groupe d’apps depuis plus de six mois.
- N’ont reçu aucun message d’un groupe d’apps depuis plus de six mois.
- Braze n’a traité aucun point de données pour ce profil utilisateur depuis plus de six mois.

Dans ce cas, ces utilisateurs ne peuvent pas être recevoir de communications et ils ne s’engagent pas avec votre marque. Dans les faits, ces utilisateurs ont churné.

## Utilisateurs dormants

Les utilisateurs dormants sont des utilisateurs qui n’ont pas eu d’activité au cours des douze derniers mois et :

- N’ont utilisé aucune application mobile ou n’ont pas visité un site Internet dans un groupe d’apps depuis plus de 12 mois.
- N’ont reçu aucun message d’un groupe d’apps depuis plus de 12 mois.
- Braze n’a traité aucun point de données pour ce profil utilisateur depuis plus de 12 mois.

## Filtrage du spam

Braze bloque les utilisateurs individuels avec plus de 5 millions de sessions ( « utilisateurs factices »), et n’ingère plus leurs événements SDK, car ils sont généralement le résultat d’une intégration incorrecte. Si vous constatez que cela s’est produit pour un utilisateur légitime, créez un ticket de [support]({{site.baseurl}}/braze_support/) Braze.

Pour trouver les utilisateurs factices dans votre tableau de bord, procédez comme suit :

1. Créez un [segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).
2. Sélectionnez le filtre `Session Count` et de l’appliquer à `more than 5,000,000`.
3. Exportez le segment via CSV.

Si nécessaire, vous pouvez supprimer les utilisateurs via le endpoint de l’API[Users Delete]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/).

[1]: {{site.baseurl}}/dp-technical-assistance/#the-right-to-erasure
