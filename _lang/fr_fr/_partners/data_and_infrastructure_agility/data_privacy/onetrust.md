---
nav_title: OneTrust
article_title: OneTrust
description: "Cet article de référence présente le partenariat entre Braze et OneTrust, un fournisseur de logiciels de confidentialité et de sécurité des données, vous permettant d'utiliser le générateur de flux de travail OneTrust pour créer des flux de travail de sécurité pour votre produit."
alias: /partners/onetrust/
page_type: partner
search_tag: Partner

---

# OneTrust

> [OneTrust](https://www.onetrust.com/) est un fournisseur de logiciels de confidentialité et de sécurité offrant la visibilité dont vous avez besoin pour mieux comprendre votre paysage de confiance, les actions à entreprendre pour exploiter des informations exploitables et l'automatisation pour vous permettre de gagner une longueur d’avance par rapport à la concurrence. 

_Cette intégration est maintenue par OneTrust._

## À propos de l'intégration

L'intégration entre Braze et OneTrust vous permet d'utiliser le générateur de flux de travail OneTrust pour créer des flux de travail de sécurité pour votre produit.
## Conditions préalables

| Exigences | Description |
|---|---|
| Compte OneTrust | Un compte [OneTrust](https://www.onetrust.com/) pour profiter de ce partenariat. |
| Clé API de Braze | Une clé API REST de Braze avec les permissions requises pour l'endpoint que votre action OneTrust utilisera.<br><br>Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
| Instance de Braze | Votre instance Braze peut être obtenue auprès de votre gestionnaire d'onboarding Braze ou sur la [page d'aperçu des API ]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

L'intégration suivante fournit des indications sur la création d'un flux de travail de mise à jour du consentement de l'utilisateur et d'un flux de travail de suppression de l'utilisateur. Pour plus de détails sur les autres endpoints de Braze pris en charge, reportez-vous à [Autres actions prises en charge](#Other-supported-actions).

### Ajouter les identifiants de Braze dans OneTrust

Dans le menu OneTrust **Integrations**, naviguez vers **Credentials** > **Add New** bouton pour faire apparaître l'écran **Select System.**  Dans cet écran, recherchez **Braze**, puis cliquez sur le bouton **Suivant**.

Suivez les invites de l'écran **Enter Credential Details** et fournissez les informations suivantes. Enregistrez vos données d'identification lorsque vous avez terminé.
  - Nom de l’identifiant
  - Définissez le type de connecteur sur **Web App**
  - Nom d'hôte : `<your-braze-instance-url>`
  - **En-tête de la requête** :
    - **Autorisation**: Porteur
    - **Content-Type**: application/json
  - Jeton : `<your-braze-api-key>`

### Ajouter Braze en tant que système

#### Étape 1 : Créer un flux de travail

{% tabs %}
{% tab Mise à jour du consentement de l'utilisateur %}
1. Dans le menu des intégrations OneTrust, naviguez vers **Galerie** > **Braze** > **Ajouter** pour créer un nouveau flux de travail.![]({% image_buster /assets/img/onetrust/onetrust.png %})<br><br>
2. Indiquez un nom et un e-mail de notification dans la boîte de dialogue. Cliquez sur le bouton **Créer**. Lors de la création, vous accéderez au générateur de flux de travail. Votre flux de travail Braze sera initié avec des appels d'API et des actions qui peuvent être utilisés pour traiter les requêtes de suppression. <br><br>
3. Dans le générateur de flux de travail, choisissez l'action que vous souhaitez déclencher dans le flux de travail.<br>![]({% image_buster /assets/img/onetrust/onetrust2.png %})

{% endtab %}
{% tab Suppression d'un utilisateur %}

1. Dans le menu des intégrations OneTrust, naviguez vers **Galerie** > **Braze** > **Ajouter** pour créer un nouveau flux de travail.![]({% image_buster /assets/img/onetrust/onetrust.png %})<br><br>
2. Indiquez un nom et un e-mail de notification dans la boîte de dialogue. Cliquez sur le bouton **Créer**. Lors de la création, vous accéderez au générateur de flux de travail. Votre flux de travail Braze sera initié avec des appels d'API et des actions qui peuvent être utilisés pour traiter les requêtes de suppression. <br><br>
3. Dans le générateur de flux de travail, choisissez l'action que vous souhaitez déclencher dans le flux de travail.<br>![]({% image_buster /assets/img/onetrust/onetrust8.png %})
{% endtab %}
{% endtabs %}

#### Étape 2 : Sélectionnez une action
{% tabs %}
{% tab Mise à jour du consentement de l'utilisateur %}

1. Lorsque vous avez terminé, cliquez sur **Terminé** et choisissez **Ajouter une action**. Notez que l'action que vous choisissez dépend du type de préférence mis à jour et de votre endpoint préféré.
- Pour mettre à jour les préférences d'abonnement globales d'un utilisateur, sélectionnez l'action **POST Suivi des utilisateurs - Attributs.** 
- Pour mettre à jour les préférences d'un utilisateur en matière de groupe d'abonnement, choisissez l'action **POST Suivi des utilisateurs - Attributs** ou l'action **POST Définir le statut du groupe d'abonnement des utilisateurs.** <br>![]({% image_buster /assets/img/onetrust/onetrust4.png %})<br><br>
2. Choisissez l'action souhaitée, sélectionnez vos informations d'identification Braze créées précédemment et cliquez sur **Suivant**.<br>![]({% image_buster /assets/img/onetrust/onetrust5.png %})

{% endtab %}
{% tab Suppression d'un utilisateur %}

1. Lorsque vous avez terminé, cliquez sur **Terminé** et choisissez **Ajouter une action**.
- Pour supprimer un utilisateur de Braze, sélectionnez l'action **POST Suppression de l’utilisateur**.
<br>![]({% image_buster /assets/img/onetrust/onetrust9.png %})<br><br>
2. Choisissez l'action souhaitée, sélectionnez vos informations d'identification Braze créées précédemment et cliquez sur **Suivant**.<br>![]({% image_buster /assets/img/onetrust/onetrust5.png %})

{% endtab %}
{% endtabs %}
#### Étape 3 : Mettre à jour le corps de la requête
{% tabs %}
{% tab Mise à jour du consentement de l'utilisateur %}

1. Mettez à jour le corps du texte pour y inclure toutes les valeurs dynamiques nécessaires. Assurez-vous que le corps de l'action correspond aux [endpoints `/users/track` ](https://www.braze.com/docs/api/endpoints/user_data/post_user_track/) et [`/subscription/status/set`](https://www.braze.com/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status/).
2. Personnalisez le flux de travail avec des paramètres supplémentaires ou une logique conditionnelle pour répondre aux besoins de votre organisation.
3. Une fois la modification terminée, cliquez sur **Terminer**, puis sur **Activer** pour activer le flux de travail.

{% alert note %}
Lorsque vous utilisez les workflows OneTrust pour mettre à jour les préférences des groupes d'abonnement dans Braze, la paramètre `subscription_group_id` doit correspondre à l'ID défini par Braze lors de la création du groupe d'abonnement. Vous pouvez accéder au site `subscription_group_id` d'un groupe d'abonnement en accédant à la page **Groupe d'abonnement** dans le tableau de bord de Braze.
{% endalert %}

![]({% image_buster /assets/img/onetrust/onetrust6.png %})

{% endtab %}
{% tab Suppression d'un utilisateur %}

1. Mettez à jour le corps du texte pour y inclure toutes les valeurs dynamiques nécessaires. Assurez-vous que le corps de l'action correspond à l'[endpoint`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/).
2. Une fois la modification terminée, sélectionnez **Terminer** puis **Activer** pour activer le flux de travail.

![]({% image_buster /assets/img/onetrust/onetrust10.png %})

#### Mise à jour du flux de travail pour les requêtes des personnes concernées
1. Dans le menu **Automatisation des droits à la vie privée**, sélectionnez **Flux de travail.** 
2. Sélectionnez le flux de travail que vous souhaitez mettre à jour avec l'intégration Braze. 
3. Sélectionnez le bouton **Modifier** pour activer la modification.
4. Ensuite, sélectionnez l'étape du flux de travail à laquelle ajouter l'intégration Braze et cliquez sur **Ajouter une connexion**.
5. Ajoutez le flux de travail Braze créé précédemment en tant que sous-tâche système.

{% endtab %}
{% endtabs %}

## Autres actions soutenues

Outre les actions **Suivre les utilisateurs par requête POST - Attributs**, **Définir l’état du groupe d’abonnement des utilisateurs par requête POST** et **Supprimer l’utilisateur par requête POST**, Braze prend en charge d'autres endpoints qui peuvent être utilisés pour créer des workflows personnalisés et servir de sous-tâches dans des workflows existants. 

Pour consulter la liste complète des actions soutenues :
1. Dans OneTrust, cliquez sur **Systèmes** dans votre menu **Intégrations.**  
2. Choisissez le système **Braze**.
3. Accédez à l'onglet **Actions.** 

![][7]


[1]: {% image_buster /assets/img/onetrust/onetrust.png %}
[2]: {% image_buster /assets/img/onetrust/onetrust2.png %}
[3]: {% image_buster /assets/img/onetrust/onetrust3.png %}
[4]: {% image_buster /assets/img/onetrust/onetrust4.png %}
[5]: {% image_buster /assets/img/onetrust/onetrust5.png %}
[6]: {% image_buster /assets/img/onetrust/onetrust6.png %}
[7]: {% image_buster /assets/img/onetrust/onetrust7.png %}
[8]: {% image_buster /assets/img/onetrust/onetrust8.png %}
[9]: {% image_buster /assets/img/onetrust/onetrust9.png %}
[10]: {% image_buster /assets/img/onetrust/onetrust10.png %}
