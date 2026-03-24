---
nav_title: Groupe interne
article_title: Groupes interne
page_order: 10
page_type: reference
description: "Cet article de référence décrit les groupes internes, un excellent moyen d'obtenir des informations sur les journaux SDK ou API de votre appareil de test lorsque vous testez l'intégration SDK."

---

# Groupes internes

> Les groupes internes sont un excellent moyen de créer et d'organiser des groupes de test internes ou tiers. Ils fournissent des informations sur les journaux de votre SDK ou de votre API et sont utiles pour tester l'intégration de votre SDK. Vous pouvez créer un nombre illimité de groupes internes personnalisés comprenant jusqu'à 1 000 utilisateurs.

{% alert tip %}
Nous vous recommandons également de consulter notre cours d'apprentissage sur [les tests et le dépannage de](https://learning.braze.com/path/developer/testing-and-troubleshooting) Braze, qui explique comment utiliser les groupes internes pour effectuer vos propres opérations de dépannage et de débogage.
{% endalert %}

## Conditions préalables

Pour créer et gérer des groupes internes, vous devez disposer de l'[autorisation héritée Access Dev Console]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions) ou [des autorisations granulaires]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions) suivantes :

- Voir les clés API
- Modifier les clés API
- Afficher les groupes internes
- Modifier les groupes internes
- Afficher le journal d'activité des messages
- Journal des événements utilisateurs
- Afficher les identifiants API
- Voir le tableau de bord d'utilisation de l'API
- Voir les limites de l'API
- Voir les alertes d'utilisation de l'API
- Modifier les alertes d'utilisation de l'API
- Modifier le débogueur SDK
- Afficher le débogueur SDK

{% multi_lang_include deprecations/user_permissions.md %}

## Création d'un groupe interne

Pour créer un groupe interne : 

1. Allez dans **Réglages** > **Groupes internes**.
2. Sélectionnez **Créer un groupe interne**.
3. Donnez un nom à votre groupe, par exemple "Groupe de test e-mail".
4. Choisissez un ou plusieurs types de groupes, comme indiqué dans le tableau suivant.

| Type de groupe         | Description                                                                                 |
|--------------------|---------------------------------------------------------------------------------------------|
| **Groupe d’événement utilisateur**   | Veuillez utiliser cette option pour vérifier les événements ou les journaux de votre appareil de test.                                    |
| **Groupe de tests de contenu** | Veuillez utiliser cette fonctionnalité pour les notifications push, les e-mails et les messages in-app afin d'envoyer une copie rendue du message. |
| **Groupe initiateur**         | Envoie automatiquement une copie de l'e-mail à tous les membres du groupe initiateur lors de l'envoi.               |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Un groupe interne nommé « Groupe de test des e-mails ».]({% image_buster /assets/img_archive/internal_group.png %})

### Ajout d’utilisateurs de test

Une fois votre groupe interne créé, veuillez ajouter des utilisateurs test en tant que membres de ce groupe. 

1. Dans la page de gestion de votre groupe interne, sélectionnez **Ajouter des utilisateurs test**.
2. Choisissez parmi les méthodes suivantes pour rechercher et sélectionner vos utilisateurs test.

| Méthode                  | Description                                                                                                                                                                                                                                          |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Ajouter un utilisateur identifié** | Recherchez l'utilisateur par son ID externe, son adresse e-mail, son numéro de téléphone ou son jeton push.                                                                                                                                                           |
| **Ajouter un utilisateur anonyme**  | Recherchez par adresse IP. Veuillez ensuite attribuer un nom à chaque utilisateur test que vous ajoutez. Il s'agit du nom auquel tous les journaux d'événements sont associés sur la page [du journal des événements utilisateurs]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/). |
| **Ajouter des utilisateurs en masse**      | Copiez et collez une liste d'adresses e-mail ou d'ID externes. Veuillez noter que vous ne pouvez ajouter que des utilisateurs déjà enregistrés dans le tableau de bord. Pour plus d'informations, reportez-vous à l'[importation d'utilisateurs]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/).          |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Paramètres internes du groupe lors de la création d'un nouveau groupe interne]({% image_buster /assets/img_archive/internal_group_add_user.png %})

### Groupes de test de contenu

Tout comme l'envoi d'un test de prévisualisation d'un message, le groupe de test de contenu vous permet de gagner du temps et de lancer simultanément des tests sur une liste prédéfinie d'utilisateurs Braze. Ceci est disponible pour les messages in-app, les messages in-app, les SMS, les e-mails et les cartes de contenu dans Braze. Seuls les groupes marqués comme « Groupes de test de contenu » sont disponibles dans la section d'aperçu d'un message.

{% alert note %}
Les messages de test [SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/) ne peuvent être envoyés qu'à des numéros de téléphone valides figurant dans la base de données.
{% endalert %}

Veuillez sélectionner des utilisateurs Braze individuels ou un nombre quelconque de groupes internes auxquels envoyer le message. Si votre message comprend une personnalisation Liquid ou toute autre personnalisation dynamique, Braze utilise les attributs disponibles pour chaque utilisateur afin de personnaliser le contenu du message. Pour les utilisateurs qui ne possèdent aucun attribut, Braze utilise la valeur par défaut définie.

De plus, si vous prévisualisez le message en tant qu'utilisateur aléatoire, utilisateur personnalisé ou utilisateur existant, vous pouvez envoyer cette version prévisualisée à la place. En décochant la case, vous pouvez envoyer en fonction des attributs de chaque utilisateur plutôt que la version prévisualisée.

Si vous utilisez un pool d'adresses IP pour envoyer un e-mail, veuillez sélectionner le pool à partir duquel l'e-mail sera envoyé en choisissant le pool dans le menu déroulant disponible.

![La section Test de l'éditeur de messages in-app permet de sélectionner le groupe de test de contenu.]({% image_buster /assets/img_archive/content_test_preview.png %}){: style="max-width:60%" }

### Groupes initiateurs

Les groupes initiateurs ne sont pris en charge que pour le canal e-mail. Veuillez ajouter des utilisateurs à un groupe initiateur afin d'envoyer des copies de chaque variante de message d'e-mail à tous les membres du groupe.

Les groupes initiateurs ne sont pas disponibles pour les campagnes API, mais vous pouvez inclure des groupes initiateurs à l'aide d'une entrée déclenchée par l'API dans la campagne. Veuillez utiliser cet outil pour mesurer les indicateurs de livrabilité et conserver une trace du contenu de vos e-mails à des fins historiques et d'archivage. 

Après avoir créé un groupe interne et l'avoir marqué pour qu'il soit utilisé comme groupe initiateur, veuillez le sélectionner à l'étape **« Audiences cibles** » de l'éditeur de campagne ou à l'étape **« Paramètres d'envoi** » dans un canvas. 

Les e-mails d'initiateurs porteront la mention `[SEED]` au début de la ligne d'objet de l'e-mail. Notez que les e-mails d'initiateurs **ne le font pas**:

- Incrmentation des envois dans les analyses du tableau de bord.
- Impact sur l'analyse/analytique de l'e-mail ou le reciblage (si utilisé). 
- Mettre à jour la liste des **campagnes reçues** d'un profil utilisateur.
- Limite de fréquence de l'impact.
- Veuillez tenir compte des limites de débit de réception/distribution ou de leur impact.

#### Comportement d’abonnement

Les envois d'initiateurs sont conçus pour l'assurance qualité et la révision internes, ils contournent donc intentionnellement les vérifications d'abonnement pour les utilisateurs de l'entreprise bénéficiaire. Cela signifie que les utilisateurs disposant d'adresses e-mail valides et faisant partie d'un groupe initiateur reçoivent le message même s'ils ne s'abonnent pas. Cependant, le message doit être configuré pour envoyer des copies d'initiateurs à ce groupe.

{% alert tip %}
Si les membres de votre groupe initiateur signalent qu'ils ne voient pas le message dans leur boîte réception, vérifiez qu'ils figurent dans le groupe interne, que vos lignes d'objet sont différentes et que Gmail n'a pas regroupé les e-mails, ou demandez-leur de vérifier leurs dossiers de courrier indésirable.
{% endalert %}

#### Pour les campagnes

Lors de la composition d'une campagne par e-mail, modifiez vos groupes initiateurs dans la section **« Audiences cibles** » de l'éditeur.

{% alert important %}
Si vous configurez un groupe initiateur pour qu'il soit automatiquement associé à toutes les campagnes, cela ne s'applique qu'aux nouvelles campagnes. Cela ne s'applique pas lorsque vous copiez des campagnes existantes. Veuillez appliquer manuellement les groupes initiateurs souhaités à la campagne copiée dans la section **« Audiences cibles** ».
{% endalert %}

Les groupes initiateurs sont envoyés à chaque variante de courriel une fois et sont délivrés la première fois que votre utilisateur reçoit cette variante particulière. Pour les messages planifiés, il s'agit généralement de la première fois que la campagne est lancée. Pour les campagnes basées sur l'action ou déclenchées par une API, il s'agit du moment où le premier utilisateur reçoit un message.

Si votre campagne est multivariée et que votre variante a un pourcentage d'envoi de 0 %, elle n'est pas envoyée aux groupes initiateurs. De plus, si la variante a déjà été envoyée et n'a pas été mise à jour pour être renvoyée dans **Modifier les groupes initiateurs** à l'étape **Cible**, elle n'est pas renvoyée par défaut.

{% alert note %}
Si vous avez une campagne récurrente et que l'une des variantes est mise à jour, vous pouvez choisir d'envoyer à nouveau uniquement les variantes mises à jour ou toutes les variantes, ou encore de désactiver l'envoi au groupe initiateur lors de la mise à jour.
{% endalert %}

![Le groupe initiateur « Test de diffusion par e-mail » a été sélectionné pour recevoir la campagne d'e-mails Variante 1.]({% image_buster /assets/img_archive/seed_group_campaign.png %})

#### Pour le Canvas

Les groupes initiateurs dans Canvas fonctionnent de manière similaire à toute campagne déclenchée. Braze détecte automatiquement toutes les étapes qui contiennent un message d'e-mail et les envoie lorsque votre utilisateur atteint pour la première fois cette étape particulière.

Si une étape d'e-mail a été mise à jour après l'envoi du groupe initiateur, Braze propose l'option d'envoyer uniquement aux étapes mises à jour, à toutes les étapes ou de désactiver les semences.