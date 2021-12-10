---
nav_title: Données du segment
article_title: Visualisation et compréhension des données du segment
page_order: 2
page_type: Référence
description: "Cet article de référence explique la section segments de votre tableau de bord Braze et comprend un résumé des statistiques fournies."
tool:
  - Segments
  - Rapports
---

# Visualisation et compréhension des données du segment

> Cet article de référence explique la section segments de votre tableau de bord Braze et comprend un résumé des statistiques fournies.

## Accès aux données du segment

La page **Segments** de votre tableau de bord Braze contient un résumé de tous vos segments et vous permet d'examiner des données détaillées pour chacun. Sur cette page, recherchez et cliquez sur le nom d'un segment pour modifier et afficher ses données. Pour apprendre comment créer un segment, consultez [Créer un segment][3].

!\[Page Segments\]\[1\]

Après avoir cliqué sur le nom d'un segment, vous pourrez voir les statistiques et les filtres de segments. Vous pouvez modifier votre segment en ajoutant ou en supprimant des filtres. N'oubliez pas d'enregistrer les modifications !

!\[Données de Segment \]\[2\]

Lorsque vous activez [le suivi analytique pour un segment][9], Braze vous permettra de voir les sessions, les événements personnalisés et les revenus au fil du temps par ce segment.

## Statistiques du segment

Vous verrez les statistiques de segment suivantes, qui se mettent à jour en temps réel au fur et à mesure que vous ajoutez ou supprimez des filtres :

| Statistique                     | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Nombre total d'utilisateurs** | Combien d'utilisateurs votre application a au total.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Utilisateurs sélectionnés**   | Combien d'utilisateurs sont dans votre segment et quel est le pourcentage de votre base d'utilisateurs totale.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **LTV (Paying Users)**          | La valeur à vie par utilisateur (LTV) dans ce segment et la valeur à vie par utilisateur payant dans ce segment. LTV est calculée en divisant vos revenus à vie par les utilisateurs à vie.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Emailable (Opted In)**        | Le courrier électronique se réfère à tous les utilisateurs qui peuvent être contactés par e-mail. Ces utilisateurs ont fourni une adresse e-mail et n'ont pas opté pour cette option. Opted In se réfère aux utilisateurs qui ont explicitement choisi de recevoir des courriels. En raison de [réglementations anti-spam][6], C'est souvent une bonne idée de demander à vos utilisateurs d'opter explicitement en implémentant une politique de double opt-in où les utilisateurs doivent cliquer sur un lien dans un e-mail de confirmation initiale. Pour encourager plus d'utilisateurs à s'inscrire, vous pouvez cibler un message sur [ceux qui n'ont pas choisi ou non][5].                                     |
| **Push activé (Opted In)**      | Pousser activé se réfère au nombre d'utilisateurs avec au moins un jeton push. Certains utilisateurs peuvent avoir plusieurs jetons push (par ex. s'ils possèdent un iPhone et un iPad), ainsi le nombre de notifications push que vous envoyez à ce segment peut être plus grand que le nombre d'utilisateurs "push" activés. Opted In désigne le nombre d'utilisateurs qui ont explicitement opté pour les notifications push. Sous iOS et Windows, les utilisateurs doivent toujours opter explicitement pour que vous leur envoyiez des pushes. En raison de la façon dont les autorisations sont accordées sur Android, les utilisateurs n'ont pas toujours besoin d'opter explicitement pour recevoir des pushes. |
{: .reset-td-br-1 .reset-td-br-2}

## Utilisation des messages et adhésion historique

Si vous faites défiler la page, vous verrez des données de segment sur l'utilisation des messages et l'adhésion historique. Dans la section **Messagerie** , consultez les campagnes et les éléments du flux d'actualités qui ont ciblé ce segment. Sous **Adhésion historique**, vous voyez comment la taille de ce segment a changé au fil du temps. Utilisez la liste déroulante pour filtrer l'adhésion aux segments par plage de dates.

!\[Under Messaging Use, consultez les campagnes dans lesquelles votre segment est utilisé.[4] ![Utilisez le menu déroulant Adhésion historique pour filtrer l'adhésion au segment par plage de dates.\]\[10\]

## Aperçu de l'utilisateur

Pour afficher des informations détaillées et spécifiques à l'utilisateur sur vos segments, cliquez sur **Données utilisateur** et sélectionnez **Aperçu utilisateur**.

!\[Infos spécifiques à l'utilisateur\]\[7\]

Sur cette page, vous pouvez voir un certain nombre d'attributs spécifiques à l'utilisateur, tels que le sexe, âge, nombre de sessions, et s'ils ont choisi de faire des push et des emails.

!\[Aperçu de l'utilisateur\]\[8\]
[1]: {% image_buster /assets/img_archive/segments.png %} [2]: {% image_buster /assets/img_archive/A_Tracking.png %} [4]: {% image_buster /assets/img_archive/historical_membership1. ng %} [10]: {% image_buster /assets/img_archive/historical_membership2. ng %} [7]: {% image_buster /assets/img_archive/preview_users.png %} [8]: {% image_buster /assets/img_archive/user_preview.png %}

[3]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#segmenting-by-user-subscriptions
[6]: {{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations
[9]: {{site.baseurl}}/user_guide/data_and_analytics/tracking/segment_analytics_tracking/