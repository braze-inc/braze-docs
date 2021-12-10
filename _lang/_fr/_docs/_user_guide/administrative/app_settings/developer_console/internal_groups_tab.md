---
nav_title: Onglet Groupes Internes
article_title: Onglet de groupe interne
page_order: 3
page_type: Référence
description: "Cet article de référence couvre les groupes internes, un excellent moyen d'obtenir un aperçu du SDK de votre périphérique de test ou des journaux d'API lors de la vérification de l'intégration du SDK."
---

# Onglet Groupes internes

Les groupes internes sont un excellent moyen de construire et d'organiser des groupes de tests internes ou tiers et de fournir un aperçu du SDK ou des journaux API disponibles sur votre périphérique de test pendant le test d'intégration SDK. Vous pouvez créer un nombre illimité de groupes internes personnalisés avec jusqu'à 1 000 membres.

{% alert note %}
Vous avez besoin des permissions **Access Dev Console** []({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#limited-and-team-role-permissions) pour que votre groupe d'applications puisse créer et gérer des groupes internes.
{% endalert %}

## Création d'un groupe

Pour créer un groupe interne, effectuez les étapes suivantes :

1. Allez dans la **console de développement** et sélectionnez l'onglet **Groupes internes**.
2. Cliquez sur **Créer un groupe interne**.
3. Donnez à votre groupe un nom significatif.
4. Choisissez un ou plusieurs types de groupe (définis ci-dessous).


!\[Groupe interne\]\[7\]

| Type de groupe                       | Cas d'utilisation                                                                                                                                       |
|:------------------------------------ |:------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Groupe d'événements de l'utilisateur | Utilisé pour vérifier les événements ou les logs depuis votre appareil de test.                                                                         |
| Groupe de test de contenu            | Un concept similaire aux listes de test. Peut être utilisé à travers les messages push, e-mail et dans l'application pour envoyer une copie du message. |
| Groupe de graines                    | Envoie automatiquement une copie de l'e-mail à tous les membres du groupe de graines lors de l'envoi.                                                   |
{: .reset-td-br-1 .reset-td-br-2}

### Ajout d'utilisateurs de test

Après avoir créé votre groupe interne, vous pouvez ajouter des utilisateurs de test en tant que membres de ce groupe. À partir de la page de gestion de votre groupe interne, cliquez sur **Ajouter un utilisateur de test** et ajoutez-les en bloc, en tant qu'utilisateurs identifiés, ou en tant qu'utilisateurs anonymes.

!\[Logs de l'utilisateur 1\]\[8\]

| Méthode d'ajout                  | Libellé                                                                                                                                                                                                                                                                                                                      |
|:-------------------------------- |:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Utilisateurs identifiés          | Recherchez l'utilisateur par son ID d'utilisateur externe ou son adresse e-mail.                                                                                                                                                                                                                                             |
| Utilisateurs anonymes            | Recherche par adresse IP. Ensuite, fournissez un nom pour chaque utilisateur de test qui est ajouté. C'est le nom auquel tous les journaux d'événements seront associés sur la page [Event User Log]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/).                         |
| Ajouter des utilisateurs en bloc | Copiez et collez une liste d'adresses e-mail ou d'identifiants externes dans la section fournie. Vous ne pouvez ajouter que des utilisateurs déjà connus dans le tableau de bord. Pour plus d'informations, reportez-vous à [User Import]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/). |
{: .reset-td-br-1 .reset-td-br-2}

### Groupes de test de contenu

Similaire à l'envoi d'un test de prévisualisation d'un message, le groupe de test de contenu vous fait gagner du temps et vous permet de lancer des tests à une liste prédéfinie d'utilisateurs de Braze simultanément. Cette fonctionnalité est disponible pour les messages push, dans l'application, les SMS, les courriels et les cartes de contenu au Brésil.

{% alert note %}
[SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/) les messages de test ne peuvent être envoyés qu'à des numéros de téléphone valides dans la base de données.
{% endalert %}

Vous pouvez sélectionner des utilisateurs individuels de Braze ou autant de groupes internes à envoyer le message que vous voulez. Si votre message inclut une quelconque personnalisation Liquid ou une autre personnalisation dynamique, Braze utilisera les attributs disponibles pour chaque utilisateur pour personnaliser le contenu du message. Pour les utilisateurs qui n'ont pas d'attributs, Braze utilisera la valeur par défaut.

De plus, si vous prévisualisez le message en tant qu'utilisateur aléatoire, utilisateur personnalisé ou utilisateur existant, vous pouvez envoyer cette version prévisualisée. Effacer la case à cocher vous permet d'envoyer en fonction des attributs de chaque utilisateur par rapport à la version prévisualisée.

Enfin, si vous utilisez un pool d'IP pour envoyer des e-mails, vous pouvez sélectionner le groupe d'adresses IP depuis lequel vous souhaitez envoyer le courriel en sélectionnant le pool dans le menu déroulant disponible.

Seuls les groupes étiquetés comme groupes de test de contenu seront disponibles dans la section d'aperçu d'un message.

!\[Paramètres du groupe de test de contenu\]\[9\]{: style="max-width:50%" }

### Groupes de graines

Les groupes de graines sont uniquement destinés au canal de courriel et vous permettent d'envoyer une copie de chaque message de variante de courriel aux membres de ce groupe. Les groupes de graines ne sont pas disponibles pour les campagnes de l'API, bien que vous puissiez inclure des groupes de graines via une entrée déclenchée par une API dans la campagne. Cette fonctionnalité est généralement utilisée avec des partenaires tels que le chemin de retour ou 250OK pour mesurer les métriques de livraison. Il peut être utilisé pour conserver un enregistrement du contenu du courrier électronique à des fins historiques et d'archives.

Une fois que vous avez créé un groupe interne et que vous l'avez tagué pour être utilisé comme groupe de graines, vous pouvez le sélectionner à partir de l'étape **Utilisateurs cibles** du compositeur de la campagne, ou sur l'étape **Envoyer les paramètres** dans un Canvas. Les e-mails de seed auront l'identifiant `[SEED]`, ajouté au début de la ligne objet de l'email. Veuillez noter que les courriels de Seed envoyés ne sont pas incrémentés dans les analyses du tableau de bord, et qu'ils ne mettent pas à jour la liste **Campagne Reçue** d'un profil utilisateur.

{% alert tip %}
Si les membres de votre groupe de graines ne voient pas le message dans leur boîte de réception, assurez-vous qu'ils sont répertoriés dans le groupe interne, vérifiez que vos lignes d'objet sont différentes et que Gmail n'a pas fourni les courriels ensemble, ou demandez-leur de vérifier leurs dossiers SPAM.
{% endalert %}

#### Pour les campagnes

Les groupes de Seed peuvent être modifiés à partir de la page **Ciblage** lors de la rédaction d'une campagne e-mail.

Les groupes de graines envoient une fois à chaque variante de courriel et sont livrés la première fois que votre utilisateur reçoit cette variante particulière. Pour les messages programmés, c'est généralement la première fois que la campagne démarre. Pour les campagnes basées sur l'action ou sur l'API, ce sera le moment où le premier utilisateur recevra un message.

Si votre campagne est multivariée et que votre variante a un pourcentage d'envoi de 0%, elle ne sera pas envoyée aux groupes de graines. De plus, si la variante a déjà été envoyée et n'a pas été mise à jour pour être renvoyée dans **Modifier les groupes de semences** à l'étape **Cible** elle ne sera pas renvoyée par défaut.

{% alert note %}
S'il y a une campagne récurrente et qu'une mise à jour est effectuée sur l'une des variantes, vous avez la possibilité de réenvoyer uniquement aux variantes mises à jour, toutes les variantes, ou de désactiver l'envoi du groupe de graines lors de la mise à jour.
{% endalert %}

!\[Campagne de groupe de grains\]\[11\]

#### Pour la toile

Les groupes de semences de Canvas travaillent de la même manière que ceux de toute campagne déclenchée. Braze détecte automatiquement toutes les étapes qui contiennent un message e-mail et les enverra lorsque votre utilisateur aura atteint la première étape de cette étape.

Si une étape de courriel a été mise à jour après que le groupe de graines ait été envoyé, l'option d'envoyer uniquement aux étapes mises à jour, toutes les étapes, ou désactiver les graines seront présentées.
[7]: {% image_buster /assets/img_archive/internal_group.png %} [8]: {% image_buster /assets/img_archive/UserLogs1. ng %} [9]: {% image_buster /assets/img_archive/content_test_preview.png %} [11]: {% image_buster /assets/img_archive/seed_group_campaign.png %}
