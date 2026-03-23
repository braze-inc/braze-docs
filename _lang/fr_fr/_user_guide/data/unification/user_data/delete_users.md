---
nav_title: Supprimer les utilisateurs
article_title: Supprimer les utilisateurs
page_order: 4.2
toc_headers: h2
description: "Découvrez comment supprimer un utilisateur individuel ou un segment d'utilisateurs directement depuis le tableau de bord de Braze."
alias: /delete_users/
---

# Supprimer les utilisateurs

> Découvrez comment supprimer un utilisateur individuel ou un segment d'utilisateurs directement depuis le tableau de bord de Braze.

{% alert important %}
La suppression d'utilisateurs est actuellement en accès anticipé. Contactez votre Customer Success Manager si vous souhaitez participer.
{% endalert %}

## Conditions préalables

Pour supprimer des utilisateurs, vous devez être administrateur ou disposer des autorisations **Delete User**.

## À propos de la suppression d'utilisateurs

La suppression d'utilisateurs vous permet de gérer votre base de données en supprimant les profils qui ne sont plus nécessaires, qui ont été créés par erreur ou qui doivent être supprimés pour des raisons de conformité (telles que le RGPD ou le CCPA).

| Considération | Détails |
|---------------|---------|
| Taille maximale | Vous pouvez supprimer jusqu'à 100 millions de profils utilisateurs lorsque vous supprimez un segment. |
| Période d'attente | Toute suppression de segment nécessite un délai d'attente de 7 jours, auquel s'ajoute le temps nécessaire au traitement des suppressions. |
| Limites de tâches | Un seul segment peut être supprimé à la fois, période d'attente de 7 jours incluse. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Suppression d'utilisateurs

Vous pouvez supprimer un [utilisateur individuel](#delete-individual) ou un [segment d'utilisateurs](#delete-segment) via le tableau de bord de Braze :

### Suppression d'un utilisateur individuel {#delete-individual}

Pour supprimer un utilisateur individuel de Braze, rendez-vous dans **Audience** > **Rechercher des utilisateurs**, puis recherchez et sélectionnez un utilisateur. Si vous supprimez un profil utilisateur en double, vérifiez que vous avez sélectionné le bon.

![La page « Rechercher des utilisateurs » dans Braze.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:75%;"}

{% alert warning %}
Les suppressions d'utilisateurs individuels sont définitives : les profils ne peuvent pas être récupérés après leur suppression.  
{% endalert %}

Sur la page de profil de l'utilisateur, sélectionnez <i class="fa-solid fa-ellipsis-vertical"></i> **Afficher les options** > **Supprimer l'utilisateur**. Notez que la suppression complète de l'utilisateur dans Braze peut prendre quelques minutes.

![Un utilisateur dans Braze avec le menu à points de suspension vertical ouvert, affichant l'option permettant de supprimer l'utilisateur.]({% image_buster /assets/img/audience_management/deleting_users/delete_user.png %}){: style="max-width:85%;"}

### Suppression d'un segment {#delete-segment}

Si vous ne l'avez pas encore fait, [créez un segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) contenant les profils utilisateurs que vous souhaitez supprimer. Assurez-vous d'inclure tous les profils utilisateurs si vous supprimez des utilisateurs en double.

Dans Braze, rendez-vous dans **Audience** > **Gérer l'audience**, puis sélectionnez l'onglet **Supprimer des utilisateurs**.

![L'onglet « Supprimer des utilisateurs » dans la section « Gérer l'audience » du tableau de bord de Braze.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Sélectionnez **Supprimer des utilisateurs**, choisissez le segment que vous souhaitez supprimer, puis sélectionnez **Suivant**.

![Une fenêtre contextuelle avec le segment sélectionné pour suppression.]({% image_buster /assets/img/audience_management/deleting_users/choose_segment_to_delete.png %}){: style="max-width:75%;"}

Saisissez **DELETE** pour confirmer votre demande, puis sélectionnez **Supprimer les utilisateurs**.

![La page de confirmation avec « DELETE » saisi dans la case de confirmation.]({% image_buster /assets/img/audience_management/deleting_users/confirm_segment_delete.png %}){: style="max-width:75%;"}

Les utilisateurs de ce segment ne seront pas supprimés immédiatement. Ils seront marqués comme étant en attente de suppression pendant les 7 prochains jours. Passé ce délai, ils seront supprimés et vous recevrez un e-mail de notification.

{% alert tip %}
Afin de garantir que ces utilisateurs précis soient supprimés indépendamment des modifications apportées au segment, un filtre de segment appelé **Suppression en attente** est automatiquement créé. Vous pouvez [utiliser ce filtre]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#filters) pour vérifier l'état des suppressions en attente.
{% endalert %}

## Confirmation des suppressions de segments

Braze envoie un e-mail de confirmation indiquant le nombre de profils en attente de suppression.

Pour poursuivre la suppression, connectez-vous à Braze et confirmez la demande de suppression.

Si vous ne confirmez pas dans le délai indiqué dans l'e-mail, la demande de suppression expirera et ne sera pas traitée.

## Annulation des suppressions de segments {#cancel}

Vous disposez de 7 jours pour annuler les suppressions de segments en attente. Pour annuler, rendez-vous dans **Audience** > **Gérer l'audience**, puis sélectionnez l'onglet **Supprimer des utilisateurs**.

![L'onglet « Supprimer des utilisateurs » dans la section « Gérer l'audience » du tableau de bord de Braze.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

À côté d'une suppression de segment en attente, sélectionnez <i class="fa-solid fa-eye"></i> pour ouvrir les détails de l'enregistrement de suppression.

![Une suppression de segment en attente dans l'onglet « Supprimer des utilisateurs ».]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

Dans les détails de l'enregistrement de suppression, sélectionnez **Annuler la suppression**.

![La fenêtre « Détails de l'enregistrement de suppression » dans l'onglet « Supprimer des utilisateurs ».]({% image_buster /assets/img/audience_management/deleting_users/deletion_record_details.png %}){: style="max-width:55%;"}

{% alert tip %}
Lorsqu'une suppression groupée d'utilisateurs est en cours, vous pouvez l'annuler à tout moment. Cependant, les utilisateurs déjà supprimés avant l'annulation ne peuvent pas être restaurés.
{% endalert %}

## Vérification de l'état de suppression {#status}

Vous pouvez vérifier l'état d'une suppression à l'aide des [filtres de segment](#segment-filters), de la page [Gérer l'audience](#manage-audience) ou des [rapports d'événements de sécurité](#security-event-report).

### Filtres de segment

Lorsque vous demandez la suppression d'un segment d'utilisateurs, un [filtre de segment]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#filters) appelé **Suppression en attente** est automatiquement créé. Vous pouvez l'utiliser pour :

- Consulter l'ensemble exact des utilisateurs liés à une date de suppression spécifique.
- Exclure ces utilisateurs des campagnes afin qu'ils ne reçoivent pas de messages avant leur suppression.
- Exporter la liste si vous en avez besoin à des fins de conformité ou d'archivage.

### Gérer l'audience

{% alert note %}
Pour obtenir la liste exacte des utilisateurs qui seront supprimés, utilisez le [filtre de segment Suppression en attente](#segment-filters).
{% endalert %}

Rendez-vous dans **Audience** > **Gérer l'audience**, puis sélectionnez l'onglet **Supprimer des utilisateurs**.

![L'onglet « Supprimer des utilisateurs » dans la section « Gérer l'audience » du tableau de bord de Braze.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Sur cette page, vous trouverez les informations générales suivantes concernant toutes les suppressions en cours et en attente :

| Champ | Description |
|-------|-------------|
| Date de la demande | La date à laquelle la demande a été initialement formulée. Utilisez-la avec le filtre **Suppression en attente** pour obtenir la liste des profils en attente de suppression. |
| Demandeur | L'utilisateur qui a initié la demande de suppression. |
| Nom du segment | Le nom du segment utilisé pour sélectionner les utilisateurs en attente de suppression. |
| État | Indique si la demande de suppression est en attente, en cours ou terminée. |  
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Pour plus de détails sur une demande spécifique, sélectionnez <i class="fa-solid fa-eye"></i> pour afficher les détails de l'enregistrement de suppression. Vous pouvez également [annuler les suppressions de segments en attente](#cancel) depuis cet écran.

![Une suppression de segment en attente dans l'onglet « Supprimer des utilisateurs ».]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

### Rapport sur les événements de sécurité

Vous pouvez également vérifier l'état des suppressions précédentes en téléchargeant un rapport sur les événements de sécurité. Pour en savoir plus, consultez [Paramètres de sécurité]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#security-event-report).

## Foire aux questions {#faq}

### Est-il possible de supprimer des segments comptant plus de 100 millions d'utilisateurs ?

Non. Il n'est pas possible de supprimer des segments comptant plus de 100 millions d'utilisateurs. Si vous avez besoin d'aide pour supprimer un segment de cette taille, contactez l'[Assistance Braze]({{site.baseurl}}/user_guide/administrative/access_braze/support).

### Il semble que je ne puisse pas supprimer 100 millions d'utilisateurs et que je sois limité à 10 millions seulement. S'agit-il d'un bug ?

Non, il ne s'agit pas d'un bug. Certains clients sont soumis à des restrictions quant au nombre d'utilisateurs qu'ils peuvent supprimer pendant le programme d'accès anticipé (EA).

Au fur et à mesure de l'avancement du programme EA, cette capacité est conçue pour augmenter jusqu'à ce que tous les clients puissent supprimer jusqu'à 100 millions d'utilisateurs.

Si vous souhaitez augmenter cette capacité, contactez votre Account Manager Braze. Les demandes sont accordées à la discrétion de l'équipe produit.

### La fusion automatique des utilisateurs a-t-elle une incidence sur la suppression des utilisateurs ?

Si une fusion planifiée inclut des profils utilisateurs en attente de suppression, Braze ignore ces profils et ne les fusionne pas. Pour fusionner ces profils, vous devez d'abord les retirer de la file de suppression.

### Que deviennent les données envoyées aux utilisateurs en attente de suppression ?

Les données envoyées depuis des systèmes externes ou des SDK sont toujours acceptées, mais les utilisateurs seront supprimés selon la planification prévue, quelle que soit leur activité.

### Les Canvas et les campagnes se déclenchent-ils pour les utilisateurs en attente de suppression ?

Oui. Cependant, vous pouvez ajouter un filtre d'inclusion de segment pour exclure tous les utilisateurs concernés à l'aide du [filtre de segment](#segment-filters) **Suppression en attente**.

### Est-il possible de récupérer des profils utilisateurs supprimés ?

La suppression d'utilisateurs individuels est définitive.

Vous pouvez [annuler les suppressions de segments](#cancel) dans les 7 jours suivant la demande. Cependant, les utilisateurs déjà supprimés avant l'annulation ne peuvent pas être restaurés.