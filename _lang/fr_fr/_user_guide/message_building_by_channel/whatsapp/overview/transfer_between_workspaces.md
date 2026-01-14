---
nav_title: Transfert entre espaces de travail
article_title: "Transfert de numéros de téléphone et de groupes d'abonnement entre espaces de travail"
page_order: 4
description: "Cet article de référence explique comment transférer votre numéro de téléphone WhatsApp et vos groupes d'abonnement entre les espaces de travail."
page_type: reference
channel:
  - WhatsApp
---

# Transférez les numéros de téléphone WhatsApp et les groupes d'abonnement entre les espaces de travail.

> Cette page explique comment déplacer un numéro de téléphone WhatsApp Business Account (WABA) et son groupe d'abonnement associé d'un espace de travail à un autre au sein de Braze. Ce processus simplifie votre expérience de l'utilisation de WhatsApp avec Braze, et réduit le besoin d'une aide technique.

## Conditions préalables

- Confirmez que vous disposez de l'[autorisation]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) "Gérer les groupes d'abonnements" dans l'espace de travail d'origine et dans le nouvel espace de travail.
- La WABA ne peut pas traverser plusieurs [grappes de Braze]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints). Il est peu probable que cela se produise si vous travaillez au sein d'une seule entreprise. 

## Transfert d'un numéro de téléphone et d'un groupe d'abonnement

### Étape 1 : Archiver le groupe d'abonnement

Pour archiver un groupe d'abonnement WhatsApp, procédez comme suit :

1. Accédez à l'espace de travail dans lequel le groupe d'abonnement existe actuellement.
2. Allez dans **Audience** > **Gestion des subscription groups** et trouvez le groupe d'abonnement associé au numéro de téléphone WhatsApp que vous souhaitez déplacer.
3. Passez la souris sur le statut du groupe d'abonnement et sélectionnez <i class="fa-solid fa-box-archive"></i> **Archive**, ce qui marquera le groupe d'abonnement comme inactif mais ne le supprimera pas.

!bouton "Archive" apparaissant au survol du statut du groupe d'abonnement "Actif".]({% image_buster /assets/img/whatsapp/archive_subscription_group.png %}){: style="max-width:70%;"}

### Étape 2 : Intégrer le numéro de téléphone WhatsApp dans le nouvel espace de travail.

1. Allez dans l'espace de travail où vous souhaitez déplacer le numéro de téléphone WhatsApp.
2. Allez dans **Intégrations partenaires** > **Partenaires technologiques** > **WhatsApp**, puis faites défiler jusqu'à la section **Intégration de l'envoi messages WhatsApp**. 
3. Sélectionnez l'option **Créer un nouveau groupe d'abonnement et un nouveau numéro de téléphone.**
4. Commencez le processus d'intégration, au cours duquel vous pouvez sélectionner le numéro de téléphone dans le groupe d'abonnement archivé.

### Étape 3 : Vérifier l'intégration

1. Une fois l'intégration terminée, confirmez que le numéro de téléphone WhatsApp est désormais associé au groupe d'abonnement dans le nouvel espace de travail.
2. Testez pour confirmer que les messages peuvent être envoyés et reçus via ce numéro de téléphone WhatsApp.

## Considérations

- Si vous devez retransférer le numéro de téléphone WhatsApp vers l'espace de travail d'origine, répétez les étapes. Archivez le groupe d'abonnement dans l'espace de travail de destination, puis intégrez-le dans l'espace de travail d'origine.
- Vous n'avez pas besoin de supprimer le numéro de téléphone WhatsApp de votre gestionnaire Meta Business lors du transfert.