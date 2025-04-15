---
nav_title: Groupes internes
article_title: Groupes interne
page_order: 10
page_type: reference
description: "Cet article de référence couvre les groupes internes, un excellent moyen de consulter les journaux du SDK ou de l’API de votre dispositif de test lors du test d’intégration SDK."

---

# Groupes internes

> Les groupes internes constituent un excellent moyen de créer et d’organiser des groupes de tests internes ou tiers. Ils fournissent des informations sur vos fichiers SDK ou API et sont utiles lors du test de votre intégration SDK. Vous pouvez créer un nombre illimité de groupes internes personnalisés avec un maximum de 1 000 membres.

Vous devez disposer des [autorisations]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#limited-and-team-role-permissions) **Access Dev Console** pour votre espace de travail afin de créer et de gérer des groupes internes.

{% alert tip %}
Outre cet article, nous vous recommandons également de consulter notre cours d'apprentissage sur l'[assurance qualité et les outils de débogage de](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/) Braze, qui explique comment utiliser les groupes internes pour effectuer vos propres opérations de dépannage et de débogage.
{% endalert %}

## Création d’un groupe

Pour créer un groupe interne, procédez comme suit : 

1. Allez dans **Réglages** > **Groupes internes**.

{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), cette page se trouve sous **Paramètres** > **Console de développement** > **Groupes internes**.
{% endalert %}

{:start="2"}
2\. Cliquez sur **Créer un groupe interne**.
3\. Donnez un nom significatif à votre groupe.
4\. Choisissez un ou plusieurs types de groupes, comme indiqué dans le tableau suivant.

![Création d’un groupe interne à Braze][7]

| Type de groupe     | Cas d’utilisation     |
| :------------- | :------------- |
| Groupe d’événement utilisateur| Utilisé pour vérifier les événements ou les journaux de votre appareil de test.|
| Groupe de tests de contenu | Un concept similaire aux listes de tests. Peut être utilisé pour les notifications push, les e-mails et les messages dans l’application pour envoyer une copie de rendu du message.|
| Groupe initiateur | Envoie automatiquement une copie de l’e-mail à tous les groupes initiateurs lors de l’envoi.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Ajout d’utilisateurs de test

Après avoir créé votre groupe interne, vous pouvez ajouter des utilisateurs de test en tant que membres de ce groupe. Depuis la page de gestion de votre groupe interne, cliquez sur **Ajouter un utilisateur test** et ajoutez-les en bloc en tant qu'utilisateurs identifiés ou anonymes.

![Paramètres du groupe interne lors de la création d’un nouveau groupe interne][8]

| Méthode d’addition | Description |
| :------------- | :------------- |
| Utilisateurs identifiés |Recherchez l’utilisateur par son ID utilisateur externe ou son adresse e-mail.|
|Utilisateurs anonymes| Recherchez par adresse IP. Donnez ensuite un nom pour chaque utilisateur de test ajouté. Il s'agit du nom auquel tous les journaux des événements seront associés sur la page [Journal des événements utilisateurs.]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) |
|Ajouter des utilisateurs en bloc|Copiez et collez une liste d’adresses e-mail ou d’ID externes dans la section fournie. Vous ne pouvez ajouter que des utilisateurs déjà connus dans le tableau de bord. Pour plus d'informations, consultez la section [Importation d'utilisateurs]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Groupes de test de contenu

Semblable à l'envoi d'un test de prévisualisation d'un message, le groupe de test de contenu vous fait gagner du temps et vous permet de lancer simultanément des tests auprès d'une liste prédéfinie d'utilisateurs de Braze. Cette fonctionnalité est disponible pour les messages push, les messages in-app, les SMS, les e-mails et les cartes de contenu dans Braze.

{% alert note %}
Les messages de test [SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/) ne peuvent être envoyés qu'à des numéros de téléphone valides figurant dans la base de données.
{% endalert %}

Vous pouvez sélectionner des utilisateurs individuels de Braze ou autant de groupes internes auxquels envoyer le message. Si votre message comprend un liquide ou une autre personnalisation dynamique, Braze utilisera les attributs disponibles pour chaque utilisateur afin de personnaliser le contenu du message. Pour les utilisateurs qui n’ont aucun attribut, Braze utilisera la valeur par défaut définie.

En outre, si vous prévisualisez le message en tant qu’utilisateur aléatoire, utilisateur personnalisé ou utilisateur existant, vous pouvez envoyer cette version prévisualisée à la place. Si vous ne cochez pas cette case, vous pouvez envoyer des messages en fonction des attributs de chaque utilisateur par rapport à la version prévisualisée.

Enfin, si vous utilisez un pool d'IP pour envoyer un e-mail, vous pouvez sélectionner le pool d'IP à partir duquel l'e-mail doit être envoyé en sélectionnant le pool dans le menu déroulant disponible.

Seuls les groupes étiquetés comme groupes de test de contenu seront disponibles dans la section de prévisualisation d'un message.

![Test envoyé aux groupes de test de contenu][9]{: style="max-width:50%" }

### Groupes initiateurs

Les groupes initiateurs sont uniquement destinés au canal d’e-mail et vous permettent d’envoyer une copie de chaque variante de message électronique aux membres de ce groupe. Les groupes initiateurs ne sont pas disponibles pour les campagnes API, bien que vous puissiez inclure des groupes initiateurs via une entrée déclenchée par API dans la campagne. Cette fonctionnalité est généralement utilisée avec des partenaires tels que le Return Path ou 250OK pour mesurer les indicateurs de livrabilité. Il peut être utilisé pour conserver un enregistrement du contenu de l’e-mail à des fins d’historique et d’archivage. 

Après avoir créé un groupe interne et l'avoir étiqueté pour qu'il soit utilisé comme groupe initiateur, vous pouvez le sélectionner dans l'étape **Utilisateurs cibles** du compositeur de la campagne ou dans l'étape **Paramètres d'envoi d'** un Canvas. Les e-mails d'initiateurs incluront l'identifiant `[SEED]` au début de leur ligne d’objet. Notez que l'envoi d'e-mails initiateurs n'incrémente pas les envois dans l'analyse du tableau de bord et n'a pas d'impact sur l'analyse des e-mails ou le reciblage. Ils ne mettent pas non plus à jour la liste des **campagnes reçues** d’un profil utilisateur.

{% alert tip %}
Si les membres de votre groupe initiateur signalent qu'ils ne voient pas le message dans leur boîte réception, assurez-vous qu'ils figurent dans le groupe interne, vérifiez que vos lignes d'objet sont différentes et que Gmail n'a pas regroupé les e-mails, ou demandez-leur de vérifier leurs dossiers SPAM.
{% endalert %}

#### Pour les campagnes

Les groupes initiateurs peuvent être modifiés à partir de la page de **ciblage** lors de la composition d'une campagne e-mail.

Les groupes initiateurs sont envoyés à chaque variante de courriel une fois et sont délivrés la première fois que votre utilisateur reçoit cette variante particulière. Pour les messages planifiés, il s'agit généralement de la première fois que la campagne est lancée. Pour les campagnes basées sur des actions ou déclenchées par l’API, il s’agira du moment où le premier utilisateur reçoit un message.

Si votre campagne est multivariée et que votre variante a un pourcentage d’envoi de 0 %, elle ne sera pas envoyée aux groupes initiateurs. En outre, si la variante a déjà été envoyée et n'a pas été modifiée pour être renvoyée dans **Modifier les groupes initiateurs** à l'étape **Cible**, elle ne sera pas renvoyée par défaut.

{% alert note %}
S'il s'agit d'une campagne récurrente et qu'une mise à jour est effectuée sur l'une des variantes, vous avez la possibilité de renvoyer le message uniquement aux variantes mises à jour, à toutes les variantes ou de désactiver l'envoi au groupe initiateur lors de la mise à jour.
{% endalert %}

![Aperçu des groupes initiateurs pour une campagne][11]

#### Pour le Canvas

Les groupes initiateurs de Canvas fonctionnent de la même manière que n'importe quelle campagne déclenchée. Braze détecte automatiquement toutes les étapes qui contiennent un message e-mail  et les envoie lorsque votre utilisateur atteint pour la première fois cette étape particulière.

Si une étape e-mail a été mise à jour après que le groupe initiateur a été envoyé par e-mail, l’option d’envoyer uniquement des étapes mises à jour, toutes les étapes ou de désactiver les initiateurs sera présentée.


[7]: {% image_buster /assets/img_archive/internal_group.png %}
[8]: {% image_buster /assets/img_archive/UserLogs1.png %}
[9]: {% image_buster /assets/img_archive/content_test_preview.png %}
[11]: {% image_buster /assets/img_archive/seed_group_campaign.png %}
