---
nav_title: "Suppression d'utilisateurs"
article_title: "Suppression d'utilisateurs"
page_order: 4.2
toc_headers: h2
description: "Découvrez comment supprimer un utilisateur individuel ou un segment d'utilisateurs directement via le tableau de bord Braze." 
---

# Suppression d'utilisateurs

> Découvrez comment supprimer un utilisateur individuel ou un segment d'utilisateurs directement via le tableau de bord Braze.

{% alert important %}
Cette fonctionnalité est actuellement en accès anticipé. Contactez votre gestionnaire de satisfaction client si vous souhaitez participer.
{% endalert %}

## Conditions préalables

Pour supprimer des utilisateurs, vous devez être un administrateur ou disposer des droits de **suppression d'utilisateur**.

## À propos de la suppression d'un utilisateur

La suppression des utilisateurs vous permet de gérer votre base de données en supprimant les profils qui ne sont plus nécessaires, créés par erreur ou dont la suppression est requise pour des raisons de conformité (RGPD ou CCPA, par exemple).

| Considération | Détails |
|---------------|---------|
| Taille maximale | Vous pouvez supprimer jusqu'à 100 millions de profils utilisateurs lors de la suppression d'une segmentation. |
| Période d'attente | Toutes les suppressions de segments nécessitent une période d'attente de 7 jours, à laquelle s'ajoute le temps nécessaire au traitement des suppressions. |
| Limites d'emploi | Un seul segment peut être supprimé à la fois, ce qui inclut la période d'attente de 7 jours. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Suppression d'utilisateurs

Vous pouvez supprimer un [utilisateur individuel](#delete-individual) ou un [segment d'utilisateurs](#delete-segment) via le tableau de bord Braze :

### Suppression d'une personne {#delete-individual}

Pour supprimer un utilisateur individuel de Braze, allez dans **Audience** > **Rechercher des utilisateurs**, puis recherchez et sélectionnez un utilisateur. Si vous supprimez un profil utilisateur en double, vérifiez que vous avez sélectionné le bon.

La page 'Recherche d'utilisateurs' dans Braze.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:75%;"}

{% alert warning %}
Les suppressions effectuées par un seul utilisateur sont permanentes : les fichiers ne peuvent pas être récupérés après leur suppression.  
{% endalert %}

Sur la page de son profil, sélectionnez <i class="fa-solid fa-ellipsis-vertical"></i> **Afficher les options** > **Supprimer l'utilisateur.** Gardez à l'esprit que la suppression complète de l'utilisateur dans Braze peut prendre quelques minutes.

Un utilisateur dans Braze avec le menu des ellipses verticales ouvert, montrant l'option de suppression de l'utilisateur.]({% image_buster /assets/img/audience_management/deleting_users/delete_user.png %}){: style="max-width:85%;"}

### Suppression d'une segmentation {#delete-segment}

Si vous ne l'avez pas encore fait, [créez une segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) contenant les profils utilisateurs que vous souhaitez supprimer. Veillez à inclure tous les profils utilisateurs si vous supprimez des utilisateurs en double.

Dans Braze, allez dans **Audience** > **Gérer l'audience**, puis sélectionnez l'onglet **Supprimer des utilisateurs.** 

L'onglet "Supprimer des utilisateurs" dans la section "Gérer l'audience" du tableau de bord de Braze.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Sélectionnez **Supprimer des utilisateurs**, choisissez le segment à supprimer, puis sélectionnez **Suivant.**

\![Une fenêtre pop-up avec un segment choisi pour la suppression.]({% image_buster /assets/img/audience_management/deleting_users/choose_segment_to_delete.png %}){: style="max-width:75%;"}

Tapez **DELETE** pour confirmer votre demande, puis sélectionnez **Delete users**.

La page de confirmation avec 'DELETE' tapé dans la case de confirmation.]({% image_buster /assets/img/audience_management/deleting_users/confirm_segment_delete.png %}){: style="max-width:75%;"}

Les utilisateurs de ce segment ne seront pas supprimés immédiatement. Au lieu de cela, ils seront marqués comme étant en attente de suppression pendant les 7 prochains jours. Passé ce délai, elles seront supprimées et nous vous enverrons un e-mail pour vous en informer.

{% alert tip %}
Pour s'assurer que ces utilisateurs précis sont supprimés indépendamment des changements de segmentation, un filtre de segmentation appelé **Suppression en attente** est automatiquement créé. Vous pouvez [utiliser ce filtre]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#filters) pour vérifier l'état des suppressions en attente.
{% endalert %}

## Annulation des suppressions de segments {#cancel}

Vous disposez d'un délai de 7 jours pour annuler les segmentations en cours. Pour annuler, allez dans **Audience** > **Gérer l'audience**, puis sélectionnez l'onglet **Supprimer les utilisateurs.** 

L'onglet "Supprimer des utilisateurs" dans la section "Gérer l'audience" du tableau de bord de Braze.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

En regard d'une segmentation en attente de suppression, sélectionnez <i class="fa-solid fa-eye"></i> pour ouvrir les détails de l'enregistrement de suppression.

Une segmentation est en cours dans l'onglet 'Supprimer des utilisateurs'.]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

Dans les détails de l'enregistrement de suppression, sélectionnez **Annuler suppression**.

La fenêtre 'Détails de l'enregistrement de suppression' dans l'onglet 'Supprimer des utilisateurs'.]({% image_buster /assets/img/audience_management/deleting_users/deletion_record_details.png %}){: style="max-width:55%;"}

{% alert tip %}
Lorsque la suppression en bloc d'utilisateurs est en cours, vous pouvez l'annuler à tout moment. Toutefois, les utilisateurs déjà supprimés avant l'annulation ne peuvent pas être rétablis.
{% endalert %}

## Vérification de l'état de la suppression {#status}

Vous pouvez vérifier l'état d'une suppression à l'aide des [filtres d'](#segment-filters) [audience](#manage-audience), de la page de [gestion de l'audience](#manage-audience) ou des [rapports d'événements de sécurité](#security-event-report).

### Filtres de segmentation

Lorsque vous demandez la suppression d'un segment d'utilisateurs, un [filtre de segment]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#filters) appelé **Suppression en attente** est automatiquement créé. Vous pouvez l'utiliser pour :

- Consultez l'ensemble exact des utilisateurs liés à une date d'exécution de suppression spécifique.
- Excluez ces utilisateurs des campagnes afin qu'ils ne reçoivent pas de messages avant la suppression.
- Exportez la liste si vous en avez besoin pour des raisons de conformité ou d'archivage.

### Gérer l'audience

{% alert note %}
Pour obtenir la liste exacte des utilisateurs qui seront supprimés, utilisez plutôt le [filtre du segment Suppression en attente.](#segment-filters) 
{% endalert %}

Allez dans **Audience** > **Gérer l'audience**, puis sélectionnez l'onglet **Supprimer des utilisateurs.** 

L'onglet "Supprimer des utilisateurs" dans la section "Gérer l'audience" du tableau de bord de Braze.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Sur cette page, vous trouverez les informations générales suivantes pour toutes les suppressions en cours et en attente :

| Champ d'application | Description |
|-------|-------------|
| Date de la demande | La date à laquelle la demande a été faite à l'origine. Utilisez-le avec le filtre **Suppression en cours** pour obtenir la liste des profils en cours de suppression. |
| Demandeur | L'utilisateur qui a initié la demande de suppression. |
| Nom du segment | Nom du segment utilisé pour sélectionner les utilisateurs en attente de suppression. |
| Statut | Indique si la demande de suppression est en attente, en cours ou terminée. |  
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Pour plus de détails sur une demande spécifique, sélectionnez <i class="fa-solid fa-eye"></i> pour afficher les détails de l'enregistrement de suppression. Vous pouvez également y [annuler les suppressions de segments en cours](#cancel).

Une segmentation est en cours dans l'onglet 'Supprimer des utilisateurs'.]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

### Rapport sur les événements de sécurité

Vous pouvez également vérifier l'état des suppressions précédentes en téléchargeant un rapport d'événement de sécurité. Pour plus d'informations, voir [Paramètres de sécurité]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#security-event-report).

## Questions fréquemment posées {#faq}

### Puis-je supprimer des segmentations comptant plus de 100 millions d'utilisateurs ?

Non. Vous ne pouvez pas supprimer les segmentations qui comptent plus de 100 millions d'utilisateurs. Si vous avez besoin d'aide pour supprimer un segment de cette taille, contactez [support@braze.com](mailto:support@braze.com).

### La fusion automatisée des utilisateurs a-t-elle une incidence sur la suppression des utilisateurs ?

Si une fusion planifiée inclut des profils utilisateurs en attente de suppression, Braze ignore ces profils et ne les fusionne pas. Pour fusionner ces profils, vous devez les empêcher d'être supprimés.

### Qu'advient-il des données envoyées aux utilisateurs en attente de suppression ?

Les données envoyées par des systèmes externes ou des SDK sont toujours acceptées, mais les utilisateurs seront supprimés comme prévu, quelle que soit leur activité.

### Les toiles et les campagnes se déclencheront-elles pour les utilisateurs en attente de suppression ?

Oui. Cependant, vous pouvez ajouter un filtre d'inclusion de segment pour exclure tous les utilisateurs avec le [filtre de segment](#segment-filters) **Suppression en attente.** 

### Puis-je récupérer des profils utilisateurs supprimés ?

La suppression d'utilisateurs individuels est permanente.

Vous pouvez [annuler les segmentations](#cancel) dans les 7 jours qui suivent. Toutefois, les utilisateurs déjà supprimés avant l'annulation ne peuvent pas être restaurés.
