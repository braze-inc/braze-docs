---
nav_title: Groupes internes
article_title: Groupe interne
page_order: 10
page_type: reference
description: "Cet article de référence traite des groupes internes, un excellent moyen d'obtenir des informations sur les journaux du SDK ou de l'API de votre appareil de test lorsque vous testez l'intégration SDK."

---

# Groupes internes

> Les groupes internes sont un excellent moyen de créer et d'organiser des groupes de test internes ou tiers. Ils fournissent des informations sur les journaux de votre SDK ou de votre API et sont utiles pour tester l'intégration de votre SDK. Vous pouvez créer un nombre illimité de groupes internes personnalisés comprenant jusqu'à 1 000 utilisateurs.

{% alert tip %}
Nous vous recommandons également de consulter notre cours d'apprentissage sur [les tests et le dépannage de](https://learning.braze.com/path/developer/testing-and-troubleshooting) Braze, qui explique comment utiliser les groupes internes pour effectuer vos propres opérations de dépannage et de débogage.
{% endalert %}

## Conditions préalables

Avant de pouvoir créer et gérer des groupes internes, vous devez disposer de l'[autorisation Access Dev Console]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#limited-and-team-role-permissions) pour votre espace de travail.

## Création d'un groupe interne

Pour créer un groupe interne, procédez comme suit : 

1. Allez dans **Réglages** > **Groupes internes**.
2. Sélectionnez **Créer un groupe interne**.
3. Donnez un nom à votre groupe, par exemple "Groupe de test e-mail".
4. Choisissez un ou plusieurs types de groupes, comme indiqué dans le tableau suivant.

| Type de groupe         | Description                                                                                 |
|--------------------|---------------------------------------------------------------------------------------------|
| **Groupe d'événements utilisateur**   | Utilisé pour vérifier les événements ou les journaux de votre appareil de test.                                    |
| **Groupe de test du contenu** | Peut être utilisé à travers les messages push, les e-mails et les messages in-app pour envoyer une copie rendue du message. |
| **Groupe initiateur**         | Envoi automatique d'une copie de l'e-mail à tous les membres du groupe initiateur lors de l'envoi.               |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

!Un groupe interne nommé "Email test group".]({% image_buster /assets/img_archive/internal_group.png %})

### Ajout d'utilisateurs test

Après avoir créé votre groupe interne, vous pouvez ajouter des utilisateurs test comme membres de ce groupe. 

1. Dans la page de gestion de votre groupe interne, sélectionnez **Ajouter des utilisateurs test**.
2. Choisissez parmi les méthodes suivantes pour rechercher et sélectionner vos utilisateurs test.

| Méthode                  | Description                                                                                                                                                                                                                                          |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Ajouter un utilisateur identifié** | Recherchez l'utilisateur par son ID externe, son adresse e-mail, son numéro de téléphone ou son jeton push.                                                                                                                                                           |
| **Ajouter un utilisateur anonyme**  | Recherche par adresse IP. Ensuite, donnez un nom à chaque utilisateur test ajouté. Il s'agit du nom auquel tous les journaux des événements seront associés sur la page [Journal des événements utilisateurs.]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/)  |
| **Ajouter des utilisateurs en masse**      | Copiez et collez une liste d'adresses e-mail ou d'ID externes. Vous ne pouvez ajouter que des utilisateurs déjà connus dans le tableau de bord. Pour plus d'informations, reportez-vous à l'[importation d'utilisateurs]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/).          |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

!Paramètres du groupe interne lors de la création d'un nouveau groupe interne]({% image_buster /assets/img_archive/internal_group_add_user.png %})

### Groupes de test de contenu

Semblable à l'envoi d'un test de prévisualisation d'un message, le groupe de test de contenu vous fait gagner du temps et vous permet de lancer simultanément des tests auprès d'une liste prédéfinie d'utilisateurs de Braze. Ceci est disponible pour les messages in-app, les messages in-app, les SMS, les e-mails et les cartes de contenu dans Braze. Seuls les groupes étiquetés comme groupes de test de contenu seront disponibles dans la section de prévisualisation d'un message.

{% alert note %}
Les messages de test [SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/) ne peuvent être envoyés qu'à des numéros de téléphone valides figurant dans la base de données.
{% endalert %}

Vous pouvez sélectionner des utilisateurs individuels de Braze ou autant de groupes internes auxquels envoyer le message. Si votre message comprend un liquide ou une autre personnalisation dynamique, Braze utilisera les attributs disponibles pour chaque utilisateur afin de personnaliser le contenu du message. Pour les utilisateurs qui n'ont pas d'attributs, Braze utilise la valeur par défaut.

En outre, si vous prévisualisez le message en tant qu'utilisateur aléatoire, utilisateur personnalisé ou utilisateur existant, vous pouvez envoyer cette version prévisualisée à la place. Si vous ne cochez pas cette case, vous pouvez envoyer des messages en fonction des attributs de chaque utilisateur par rapport à la version prévisualisée.

Si vous utilisez un pool d'IP pour envoyer un e-mail, vous pouvez sélectionner le pool d'IP à partir duquel l'e-mail doit être envoyé en sélectionnant le pool dans le menu déroulant disponible.

\![La section Test de l'éditeur de messages in-app pour sélectionner le groupe d'applications.]({% image_buster /assets/img_archive/content_test_preview.png %}){: style="max-width:60%" }

### Groupes initiateurs

Les groupes initiateurs ne sont pris en charge que pour le canal e-mail. Vous pouvez ajouter des utilisateurs à un groupe initiateur pour envoyer des copies de chaque message de variante e-mail à tous les membres du groupe.

Les groupes initiateurs ne sont pas disponibles pour les campagnes API, mais vous pouvez inclure des groupes initiateurs à l'aide d'une entrée déclenchée par l'API dans la campagne. Vous pouvez l'utiliser pour mesurer les indicateurs de livrabilité et pour conserver une trace du contenu de vos e-mails à des fins historiques et d'archivage. 

Après avoir créé un groupe interne et l'avoir étiqueté pour qu'il soit utilisé comme groupe initiateur, vous pouvez le sélectionner dans l'étape **Audiences cibles** de l'éditeur de campagne, ou dans l'étape **Paramètres d'envoi d'** un canvas. 

Les e-mails d'initiateurs porteront la mention `[SEED]` au début de la ligne d'objet de l'e-mail. Notez que les e-mails d'initiateurs **ne le font pas**:

- Incrémente les envois dans l'analyse/analytique du tableau de bord (si utilisé comme adjectif).
- Impact sur l'analyse/analytique des e-mails ou le reciblage (si utilisé). 
- Mettre à jour la liste des **campagnes reçues** d'un profil utilisateur.
- Limite de fréquence de l'impact.
- Tenir compte des limites de débit de réception/distribution ou avoir un impact sur celles-ci.

{% alert tip %}
Si les membres de votre groupe initiateur signalent qu'ils ne voient pas le message dans leur boîte réception, vérifiez qu'ils figurent dans le groupe interne, que vos lignes d'objet sont différentes et que Gmail n'a pas regroupé les e-mails, ou demandez-leur de vérifier leurs dossiers de courrier indésirable.
{% endalert %}

#### Pour les campagnes

Lors de la composition d'une campagne e-mail, vous pouvez modifier vos groupes initiateurs dans la section **Audiences ciblées** de l'éditeur.

Les groupes initiateurs sont envoyés une fois à chaque variante d'e-mail et sont délivrés la première fois que votre utilisateur reçoit cette variante particulière. Pour les messages planifiés, il s'agit généralement de la première fois que la campagne est lancée. Pour les campagnes basées sur des actions ou déclenchées par l'API, il s'agira du moment où le premier utilisateur reçoit un message.

Si votre campagne est multivariée et que votre variante a un pourcentage d'envoi de 0 %, elle ne sera pas envoyée aux groupes initiateurs. En outre, si la variante a déjà été envoyée et n'a pas été modifiée pour être renvoyée dans **Modifier les groupes initiateurs** à l'étape **Cible**, elle ne sera pas renvoyée par défaut.

{% alert note %}
Si vous avez une campagne récurrente et que l'une des variantes est mise à jour, vous pouvez choisir d'envoyer à nouveau uniquement les variantes mises à jour ou toutes les variantes, ou encore de désactiver l'envoi au groupe initiateur lors de la mise à jour.
{% endalert %}

!Le groupe initiateur "Test d'amorçage par e-mail" a été sélectionné pour recevoir la campagne d'e-mail de la variante 1.]({% image_buster /assets/img_archive/seed_group_campaign.png %})

#### Pour la toile

Les groupes initiateurs dans Canvas fonctionnent de la même manière que n'importe quelle campagne déclenchée. Braze détecte automatiquement toutes les étapes qui contiennent un message e-mail et les envoie lorsque l'utilisateur atteint pour la première fois l'étape en question.

Si une étape d'e-mail a été mise à jour après l'envoi du groupe initiateur, l'option de n'envoyer qu'aux étapes mises à jour, à toutes les étapes ou de désactiver les semences sera présentée.

