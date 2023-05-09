---
nav_title: Données du segment
article_title: Afficher et comprendre les données de segment
page_order: 2
page_type: reference
description: "Cet article de référence explique la section Segments de votre tableau de bord de Braze, et montre un résumé des statistiques fournies."
tool: 
  - Segments
  - Rapports
  
---
# Données de segment

> Cet article de référence explique la section Segments de votre tableau de bord de Braze, et montre un résumé des statistiques fournies.

## Accès aux données de segment

Le **Segments** page de votre tableau de bord Braze contient un résumé de tous vos segments et vous permet d’examiner les données détaillées pour chacun d’eux. Sur cette page, vous pouvez rechercher et cliquer sur le nom d’un segment pour le modifier et afficher ses données. Pour voir comment créer un segment, consultez [Création d’un segment][3].

![Page Segments][1]

Après avoir cliqué sur le nom d’un segment, vous pouvez voir les statistiques et filtres du segment. Vous pouvez modifier votre segment en ajoutant ou en supprimant des filtres. Assurez-vous d’enregistrer vos modifications !

![Données de segment][2]

Lorsque vous activez le [suivi analytique sur un segment][9], Braze vous permet de voir les sessions, les événements personnalisés et les revenus au fil du temps pour ce segment.

## Statistiques de segment

Vous verrez les statistiques de segment suivantes, qui se mettent à jour en temps réel quand vous ajoutez ou supprimez des filtres :

| Statistique | Description |
| --------- | --- |
| **Total Users (Total des utilisateurs)** | Combien d’utilisateurs votre application a-t-elle au total ? |
| **Selected Users (Utilisateurs sélectionnés)** | Combien d’utilisateurs sont dans votre segment et le pourcentage de votre base d’utilisateurs totale qu’il représente. |
| **Valeur à vie (utilisateurs payants)** | La valeur à vie par utilisateur (Valeur à vie) dans ce segment et la valeur à vie par utilisateur payant dans ce segment. La Valeur à vie est calculée en divisant votre revenu à vie par les utilisateurs à vie. |
| **Emailable (Opt-In)** | « Emailable » fait référence à tous les utilisateurs qui peuvent être contactés par e-mail. Ces utilisateurs ont fourni une adresse e-mail et n’ont pas refusé de recevoir des messages. L’option « Opted In » désigne les utilisateurs qui ont explicitement choisi de s’abonner pour recevoir des e-mails. À cause des [réglementations sur le spam][6], il est souvent conseillé de demander à vos utilisateurs de s’inscrire explicitement via une politique de double abonnement où les utilisateurs doivent cliquer sur un lien dans un e-mail de confirmation initial. Pour encourager plus d’utilisateurs à s’abonner, vous pouvez cibler un message pour [ceux qui n’ont ni accepté (opt-in) ni refusé (opt-out)][5]. |
| **Push activé (Opted In)** | Notification push activée désigne le nombre d’utilisateurs avec au moins un jeton de notification push. Certains utilisateurs peuvent avoir plusieurs jetons de notification push (s’ils ont un iPhone et un iPad par exemple), donc le nombre de notifications push que vous envoyez à ce segment peut être supérieur au nombre d’utilisateurs qui ont la « notification push activé ». L’option « Opted In » désigne le nombre d’utilisateurs qui ont explicitement choisi de recevoir des notifications push. Les utilisateurs doivent toujours s’abonner explicitement pour recevoir des notifications push. |
{: .reset-td-br-1 .reset-td-br-2}

## Utilisation des messages et historique des inscriptions

Si vous faites défiler la page vers le bas, vous verrez les données de segment sur l’utilisation des messages, ainsi que l’historique des inscriptions. Sous la section **Messaging Use (Utilisation des messages)**, vous voyez quelles campagnes ont ciblé ce segment. Sous **Historical Membership (Historique des inscriptions)**, vous voyez comment la taille de ce segment a évolué au fil du temps. Utilisez la liste déroulante pour filtrer l’appartenance au segment par plage de dates.

![Dans Utilisation des messages, vous pouvez voir les campagnes qui utilisent votre segment.][4]
![Utilisez la liste déroulante Historique des inscriptions pour filtrer l’appartenance au segment par plage de dates.][10]

## Aperçu de l’utilisateur

Pour afficher des informations détaillées sur vos segments, cliquez sur **User Data (Données utilisateur)** et sélectionnez **User Preview (Aperçu de l’utilisateur)**.

![Informations spécifiques à l’utilisateur][7]

Sur cette page, vous pouvez afficher un certain nombre d’attributs spécifiques à l’utilisateur, tels que le sexe, l’âge, le nombre de sessions, et s’il accepte de recevoir des notifications push et des e-mails.

![Aperçu de l’utilisateur][8]

[1]: {% image_buster /assets/img_archive/segments.png %}
[2]: {% image_buster /assets/img_archive/A_Tracking.png %}
[3]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[4]: {% image_buster /assets/img_archive/historical_membership1.png %}
[10]: {% image_buster /assets/img_archive/historical_membership2.png %}
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#segmenting-by-user-subscriptions
[6]: {{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations
[7]: {% image_buster /assets/img_archive/preview_users.png %}
[8]: {% image_buster /assets/img_archive/user_preview.png %}
[9]: {{site.baseurl}}/user_guide/data_and_analytics/tracking/segment_analytics_tracking/