---
nav_title: Groupes internes
article_title: Groupes interne
page_order: 3
page_type: reference
description: "Cet article de référence couvre les groupes internes, un excellent moyen de consulter les journaux du SDK ou de l’API de votre dispositif de test lors du test d’intégration SDK."

---

# Groupes internes

> Cet article de référence couvre les groupes internes et la manière de les créer et de les utiliser. En plus de cet article, nous vous recommandons également de consulter notre cours d’apprentissage Braze [Outils d’assurance qualité et de débogage](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/), qui explique comment utiliser les groupes internes pour effectuer votre propre débogage et résoudre vous-même les problèmes.

Les groupes internes constituent un excellent moyen de construire et d’organiser des groupes de tests internes ou tiers. Ils fournissent des informations sur vos fichiers SDK ou API et sont utiles lors du test de votre intégration SDK. Vous pouvez créer un nombre illimité de groupes internes personnalisés avec un maximum de 1 000 membres.

{% alert note %}
Vous avez besoin des autorisations d’**accès à la Dev Console**[]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#limited-and-team-role-permissions) pour que votre groupe d’apps crée et gère des groupes internes.
{% endalert %}

## Création d’un groupe

Pour créer un groupe interne, procédez comme suit : 

1. Allez sur la **Developer Console** et sélectionnez l’onglet **Groupes internes (Internal Groups)**. 
2. Cliquez sur **Create Internal Group (Créer un groupe interne)**.
3. Donnez un nom significatif à votre groupe.
4. Choisissez un ou plusieurs types de groupes, comme indiqué dans le tableau suivant.

![Création d’un groupe interne à Braze][7]

| Type de groupe     | Cas d’utilisation     |
| :------------- | :------------- |
| Groupe d’événement utilisateur| Utilisé pour vérifier les événements ou les journaux de votre appareil de test.|
| Groupe de tests de contenu | Un concept similaire aux listes de tests. Peut être utilisé pour les notifications push, les e-mails et les messages in-app pour envoyer une copie de rendu du message.|
| Groupe initiateur | Envoie automatiquement une copie de l’e-mail à tous les groupes initiateurs lors de l’envoi.|
{: .reset-td-br-1 .reset-td-br-2}

### Ajout d’utilisateurs de test

Après avoir créé votre groupe interne, vous pouvez ajouter des utilisateurs de test en tant que membres de ce groupe. Sur votre page Internal Group's management (Gestion du groupe interne), cliquez sur **Add Test User (Ajouter un utilisateur test)** et ajoutez-les en bloc, en tant qu’utilisateurs identifiés ou en tant qu’utilisateurs anonymes.

![Paramètres du groupe interne lors de la création d’un nouveau groupe interne][8]

| Méthode d’addition | Description |
| :------------- | :------------- |
| Utilisateurs identifiés |Recherchez l’utilisateur par son ID utilisateur externe ou son adresse e-mail.|
|Utilisateurs anonymes| Recherchez par adresse IP. Donnez ensuite un nom pour chaque utilisateur de test ajouté. Il s’agit du nom auquel tous les journaux d’événements seront associés sur la page [Event User Log (Journal d’événements utilisateurs)]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/).|
|Ajouter des utilisateurs en bloc|Copiez et collez une liste d’adresses e-mail ou d’ID externes dans la section fournie. Vous ne pouvez ajouter que des utilisateurs déjà connus dans le tableau de bord. Pour plus d’informations, consultez [Importation d’utilisateurs]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/).|
{: .reset-td-br-1 .reset-td-br-2}

### Groupes de tests de contenu

Tout comme l’envoi d’un test d’aperçu d’un message, le groupe Content test de contenu vous fait gagner du temps et vous permet de lancer des tests à une liste prédéfinie des utilisateurs de Braze simultanément. Cette fonctionnalité est disponible pour les notifications push, les messages in-app, les SMS, les e-mails et les cartes de contenu dans Braze.

{% alert note %}
Les messages de test [SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/) ne peuvent être envoyés qu’à des numéros de téléphone valides dans la base de données.
{% endalert %}

Vous pouvez sélectionner des utilisateurs Braze individuels ou autant de groupes internes que vous le souhaitez pour envoyer le message. Si votre message inclut Liquid ou toute autre personnalisation dynamique, Braze utilisera les attributs disponibles pour chaque utilisateur individuel afin de personnaliser le contenu du message. Pour les utilisateurs qui n’ont aucun attribut, Braze utilisera la valeur par défaut définie.

En outre, si vous prévisualisez le message en tant qu’utilisateur aléatoire, utilisateur personnalisé ou utilisateur existant, vous pouvez envoyer cette version prévisualisée à la place. En décochant la case, vous pouvez envoyer le message en fonction des attributs de chaque utilisateur et non de la version prévisualisée.

Enfin, si vous utilisez un pool IP pour envoyer un e-mail, vous pouvez sélectionner le pool IP que vous souhaitez envoyer par e-mail en sélectionnant le pool dans la liste déroulante disponible.

Seuls les groupes marqués comme groupes de test de contenu seront disponibles dans la section d’aperçu d’un message.

![Test envoyé aux groupes de test de contenu][9]{: style="max-width:50%" }

### Groupes initiateurs

Les groupes initiateurs sont uniquement destinés au canal d’e-mail et vous permettent d’envoyer une copie de chaque variante de message électronique aux membres de ce groupe. Les groupes initiateurs ne sont pas disponibles pour les campagnes API, bien que vous puissiez inclure des groupes initiateurs via une entrée déclenchée par API dans la campagne. Cette fonctionnalité est généralement utilisée avec des partenaires tels que le Return Path ou 250OK pour mesurer les indicateurs de délivrabilité. Il peut être utilisé pour conserver un enregistrement du contenu de l’e-mail à des fins d’historique et d’archivage. 

Une fois que vous avez créé un groupe interne et que vous l’avez marqué comme un groupe initiateur, vous pouvez le sélectionner dans l’étape **Utilisateurs cibles** du générateur de campagne, ou dans l’étape **Envoyer les paramètres** dans un Canvas. Les e-mails initiateurs porteront l’identifiant `[SEED]`, ajouté au début de la ligne d’objet de l’e-mail. Notez que les e-mails initiateurs envoyés ne sont pas incrémentés dans l’analyse de tableau de bord et ne mettent pas à jour la liste de profil d’utilisateur d’une **campagne reçue**.

{% alert tip %}
Si les membres du groupe initiateur ne voient pas le message dans leur boîte de réception, assurez-vous qu’ils sont répertoriés dans le groupe interne, vérifiez que vos lignes d’objet sont différentes et que Gmail n’a pas regroupé les e-mails, ou demandez-leur de vérifier leurs dossiers SPAM.
{% endalert %}

#### Pour les campagnes

Les groupes initiateurs peuvent être modifiés à partir de la page **Targeting** (Ciblage) lors de la composition d’une campagne d’e-mail.

Les groupes initiateurs sont envoyés à chaque variante de courriel une fois et sont délivrés la première fois que votre utilisateur reçoit cette variante particulière. Pour les messages planifiés, il s’agit généralement de la première fois que la campagne démarre. Pour les campagnes basées sur des actions ou déclenchées par l’API, il s’agira du moment où le premier utilisateur reçoit un message.

Si votre campagne est multivariée et que votre variante a un pourcentage d’envoi de 0 %, elle ne sera pas envoyée aux groupes initiateurs. De plus, si la variante a déjà été envoyée et n’a pas subi de mise à jour pour être renvoyée dans **Edit Seed Groups** (Modifier les groupes Initiateurs) dans l’étape **Target** (Cible), elle ne sera pas renvoyée par défaut.

{% alert note %}
S’il existe une campagne récurrente et qu’une mise à jour est effectuée sur l’une des variantes, vous avez la possibilité de renvoyer uniquement les variantes mises à jour, toutes les variantes ou de désactiver l’envoi de groupe initiateur lors de la mise à jour.
{% endalert %}

![Aperçu des groupes initiateurs pour une campagne][11]

#### Pour le Canvas

Les groupes initiateurs dans le Canvas travaillent de manière similaire à celle de toute campagne déclenchée. Braze détecte automatiquement toutes les étapes qui contiennent un message e-mail  et les envoie lorsque votre utilisateur atteint pour la première fois cette étape particulière.

Si une étape e-mail a été mise à jour après que le groupe initiateur a été envoyé par e-mail, l’option d’envoyer uniquement des étapes mises à jour, toutes les étapes ou de désactiver les initiateurs sera présentée.


[7]: {% image_buster /assets/img_archive/internal_group.png %}
[8]: {% image_buster /assets/img_archive/UserLogs1.png %}
[9]: {% image_buster /assets/img_archive/content_test_preview.png %}
[11]: {% image_buster /assets/img_archive/seed_group_campaign.png %}
