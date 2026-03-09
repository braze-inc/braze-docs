---
nav_title: Supprimer les utilisateurs
article_title: Supprimer les utilisateurs
page_order: 4.2
toc_headers: h2
description: "Découvrez comment supprimer un utilisateur individuel ou un segment d'utilisateurs directement depuis le tableau de bord de Braze."
alias: /delete_users/
hidden: true
---

# Supprimer les utilisateurs

> Découvrez comment supprimer un utilisateur individuel ou un segment d'utilisateurs directement depuis le tableau de bord de Braze.

{% alert important %}
L'accès anticipé à cette fonctionnalité est temporairement suspendu. Veuillez contacter votre gestionnaire de la satisfaction client pour obtenir de plus amples informations.
{% endalert %}

## Conditions préalables

Il est nécessaire d'être administrateur pour supprimer des utilisateurs.

## À propos de la suppression d'utilisateurs

La suppression d'utilisateurs vous permet de gérer votre base de données en supprimant les profils utilisateurs qui ne sont plus nécessaires, qui ont été créés par erreur ou qui doivent être supprimés pour des raisons de conformité (telles que le RGPD ou le CCPA).

| Considération | Détails |
|---------------|---------|
| Taille maximale | Vous pouvez supprimer jusqu'à 100 millions de profils utilisateurs lorsque vous supprimez un segment. |
| Période d'attente | Toute suppression de segment nécessite un délai d'attente de 7 jours, auquel s'ajoute le temps nécessaire au traitement des suppressions. |
| Limites de travail | Un seul segment peut être supprimé à la fois, ce qui inclut la période d'attente de 7 jours. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Suppression d'utilisateurs

Vous pouvez supprimer un [utilisateur individuel](#delete-individual) ou un [segment d'utilisateurs](#delete-segment) via le tableau de bord de Braze :

### Suppression d'une personne {#delete-individual}

Pour supprimer un utilisateur individuel de Braze, veuillez vous rendre dans **Audience** > **Rechercher des utilisateurs**, puis recherchez et sélectionnez un utilisateur. Si vous supprimez un profil utilisateur en double, veuillez vérifier que vous avez sélectionné le bon.

![La page « Recherche d'utilisateurs » dans Braze.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:75%;"}

{% alert warning %}
Les suppressions d'utilisateurs individuels sont définitives : les profils utilisateurs ne peuvent pas être récupérés après leur suppression.  
{% endalert %}

Sur leur page de profil utilisateur, veuillez sélectionner<i class="fa-solid fa-ellipsis-vertical"></i>**Afficher les options** > **Supprimer l'utilisateur**. Veuillez noter que la suppression complète de l'utilisateur dans Braze peut prendre quelques minutes.

![Un utilisateur dans Braze avec le menu à points de suspension vertical ouverts, affichant l'option permettant de supprimer l'utilisateur.]({% image_buster /assets/img/audience_management/deleting_users/delete_user.png %}){: style="max-width:85%;"}

### Suppression d'un segment {#delete-segment}

Si vous ne l'avez pas encore fait, [veuillez créer un segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) contenant les profils utilisateurs que vous souhaitez supprimer. Veuillez vous assurer d'inclure tous les profils utilisateurs si vous supprimez des utilisateurs en double.

Dans Braze, veuillez vous rendre dans **Audience** > **Gérer l'audience**, puis sélectionnez l'onglet **Supprimer des utilisateurs**.

![L'onglet « Supprimer des utilisateurs » dans la section « Gérer l'audience » du tableau de bord de Braze.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Veuillez sélectionner **« Supprimer des utilisateurs** », choisissez le segment que vous souhaitez supprimer, puis sélectionnez **« Suivant** ».

![Une fenêtre contextuelle s'affiche avec le segment sélectionné pour suppression.]({% image_buster /assets/img/audience_management/deleting_users/choose_segment_to_delete.png %}){: style="max-width:75%;"}

Veuillez saisir **DELETE** pour confirmer votre demande, puis sélectionner **Supprimer les utilisateurs**.

![La page de confirmation avec « SUPPRIMER » saisi dans la case de confirmation.]({% image_buster /assets/img/audience_management/deleting_users/confirm_segment_delete.png %}){: style="max-width:75%;"}

Les utilisateurs de ce segment ne seront pas supprimés immédiatement. Au lieu de cela, ils seront marqués comme étant en attente de suppression pendant les 7 prochains jours. Après cette période, elles seront supprimées et nous vous enverrons un e-mail pour vous en informer.

{% alert tip %}
Afin de garantir que ces utilisateurs précis soient supprimés indépendamment des modifications apportées aux segments, un filtre de segment appelé **« Suppression en attente** » est automatiquement créé. Vous pouvez [utiliser ce filtre]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#filters) pour vérifier le statut des suppressions en attente.
{% endalert %}

## Confirmation des suppressions de segments

Braze envoie un e-mail de confirmation indiquant le nombre de profils en attente de suppression.

Pour poursuivre la suppression, veuillez vous connecter à Braze et confirmer la demande de suppression.

Si vous ne confirmez pas dans le délai indiqué dans l'e-mail, la demande de suppression expirera et ne sera pas traitée.

## Annulation des suppressions de segments {#cancel}

Vous disposez de 7 jours pour annuler les suppressions de segments en attente. Pour annuler, veuillez vous rendre dans **Audience** > **Gestionnaire de l'audience**, puis sélectionner l'onglet **Supprimer des utilisateurs**.

![L'onglet « Supprimer des utilisateurs » dans la section « Gérer l'audience » du tableau de bord de Braze.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

À côté d'une suppression de segment en attente, veuillez sélectionner<i class="fa-solid fa-eye"></i>pour ouvrir les détails de l'enregistrement de suppression.

![Une suppression de segment en attente dans l'onglet « Supprimer des utilisateurs ».]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

Dans les détails de l'enregistrement de suppression, veuillez sélectionner **Annuler la suppression**.

![La fenêtre « Détails de la suppression » dans l'onglet « Supprimer des utilisateurs ».]({% image_buster /assets/img/audience_management/deleting_users/deletion_record_details.png %}){: style="max-width:55%;"}

{% alert tip %}
Lorsque la suppression groupée d'utilisateurs est en cours, vous avez la possibilité de l'annuler à tout moment. Cependant, les utilisateurs déjà supprimés avant l'annulation ne peuvent pas être restaurés.
{% endalert %}

## Vérification du statut de suppression {#status}

Vous pouvez vérifier l'état d'une suppression à l'aide [des filtres de segment](#segment-filters), de la page [de gestion de l'audience](#manage-audience) ou [des rapports d'événements de sécurité](#security-event-report).

### Filtres de segment

Lorsque vous demandez la suppression d'un segment d'utilisateurs, un [filtre de segment]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#filters) appelé **« Suppression en attente** » est automatiquement créé. Vous pouvez l'utiliser pour :

- Veuillez consulter l'ensemble exact des utilisateurs liés à une date de suppression spécifique.
- Veuillez exclure ces utilisateurs des campagnes afin qu'ils ne reçoivent pas de messages avant leur suppression.
- Veuillez exporter la liste si vous en avez besoin à des fins de conformité ou d'archivage.

### Gestion de l'audience

{% alert note %}
Pour obtenir la liste exacte des utilisateurs qui seront supprimés, veuillez utiliser le [filtre de segment de suppression en attente](#segment-filters).
{% endalert %}

Veuillez vous rendre dans **Audience** > **Gestionnaire de l'audience**, puis sélectionnez l'onglet **Supprimer des utilisateurs**.

![L'onglet « Supprimer des utilisateurs » dans la section « Gérer l'audience » du tableau de bord de Braze.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Sur cette page, vous trouverez les informations générales suivantes concernant toutes les suppressions en cours et en attente :

| Champ | Description |
|-------|-------------|
| Date de la demande | La date à laquelle la demande a été initialement formulée. Veuillez l'utiliser avec le filtre **Suppression en attente** pour obtenir la liste des profils en attente de suppression. |
| Demandeur | L'utilisateur qui a initié la demande de suppression. |
| Nom du segment | Le nom du segment utilisé pour sélectionner les utilisateurs en attente de suppression. |
| État | Indique si la demande de suppression est en attente, en cours ou terminée. |  
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Pour plus de détails sur une demande spécifique, veuillez sélectionner<i class="fa-solid fa-eye"></i>pour afficher les détails de l'enregistrement de suppression. Vous pouvez également [annuler](#cancel) ici [les suppressions de segments en attente](#cancel).

![Une suppression de segment en attente dans l'onglet « Supprimer des utilisateurs ».]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

### Rapport sur les événements de sécurité

Vous pouvez également vérifier l'état des suppressions précédentes en téléchargeant un rapport sur les événements de sécurité. Pour plus d'informations, veuillez consulter [les paramètres de sécurité]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#security-event-report).

## Foire aux Questions {#faq}

### Est-il possible de supprimer des segments comptant plus de 100 millions d'utilisateurs ?

Non. Il n'est pas possible de supprimer des segments comptant plus de 100 millions d'utilisateurs. Si vous avez besoin d'aide pour supprimer un segment de cette taille, veuillez contacter [support@braze.com](mailto:support@braze.com).

### Il semble que je ne puisse pas supprimer 100 millions d'utilisateurs et que je sois limité à la suppression de 10 millions seulement. S'agit-il d'un bug ?

Non, il ne s'agit pas d'un bug. Certains clients sont soumis à des restrictions quant au nombre d'utilisateurs qu'ils peuvent supprimer pendant le programme d'accès anticipé (EA).

Au fur et à mesure de l'avancement du programme EA, cette capacité est conçue pour augmenter jusqu'à ce que tous les clients puissent supprimer jusqu'à 100 millions d'utilisateurs.

Si vous souhaitez augmenter cette capacité, veuillez contacter votre gestionnaire de compte Braze. Les demandes sont accordées à la discrétion de l'équipe produit.

### La fusion automatique des utilisateurs a-t-elle une incidence sur la suppression des utilisateurs ?

Si une fusion de planification inclut des profils utilisateurs en attente de suppression, Braze ignore ces profils et ne les fusionne pas. Pour fusionner ces profils, il est nécessaire de les retirer de la suppression.

### Que deviennent les données transmises aux utilisateurs en attente de suppression ?

Les données envoyées depuis des systèmes externes ou des SDK sont toujours acceptées, mais les utilisateurs seront supprimés selon la planification, quelle que soit leur activité.

### Les canevas et les campagnes seront-ils des déclencheurs pour les utilisateurs en attente de suppression ?

Oui. Cependant, vous pouvez ajouter un filtre d'inclusion de segment pour exclure tous les utilisateurs avec le [filtre de segment](#segment-filters) **Suppression en attente**.

### Est-il possible de récupérer des profils utilisateurs supprimés ?

La suppression d'utilisateurs individuels est définitive.

Vous pouvez [annuler les suppressions de segments](#cancel) dans les 7 jours suivant leur exécution. Cependant, les utilisateurs déjà supprimés avant l'annulation ne peuvent pas être restaurés.
