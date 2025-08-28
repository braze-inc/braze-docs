---
nav_title: Envoyer des messages de test
article_title: Envoyer des messages de test
page_order: 0
tool: 
  - Campaigns
page_type: reference
description: "Le présent article de référence explique comment envoyer des messages de test sur les différents canaux de Braze et comment incorporer des propriétés d’événement personnalisé ou des attributs utilisateur."

---

# Envoyer des messages de test

> Avant d'envoyer une campagne de communication à vos utilisateurs, nous vous conseillons de procéder à des tests pour vous assurer que la campagne se présente bien et qu'elle fonctionne comme prévu. Vous pouvez créer et envoyer des messages de test pour sélectionner des appareils ou des membres de l’équipe à l’aide des outils du Tableau de bord de Braze.

{% alert important %}
Assurez-vous d’enregistrer le brouillon de votre campagne après l’avoir testée pour éviter de la supprimer. Vous pouvez envoyer des messages de test sans enregistrer le message comme brouillon.
{% endalert %}

## Étape 1 : Identifier vos utilisateurs test

Avant de tester votre campagne de communication, il est important d’identifier vos utilisateurs test. Ces utilisateurs peuvent être soit des ID utilisateur ou des adresses e-mail existants, soit de nouveaux utilisateurs qui sont utilisés exclusivement pour tester les campagnes de communication. 

### Facultatif : Créer un groupe de test de contenu

Un moyen pratique d'organiser vos utilisateurs test consiste à créer un [groupe de test de contenu]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/), qui comprend un groupe d'utilisateurs qui recevront les messages test des campagnes. Vous pouvez ajouter ce groupe de test dans le champ **Ajouter des groupes de test de contenu** sous **Destinataires du test** dans votre campagne, et lancer vos tests sans créer ou ajouter d'utilisateurs test individuels.

## Étape 2 : Envoi de messages de test spécifiques au canal

Pour connaître la marche à suivre pour envoyer des messages de test, reportez-vous à la section suivante pour votre canal respectif.

{% tabs %}
{% tab E-mail %}

1. Rédigez votre message e-mail.
2. Cliquez sur **Aperçu et test.**
3. Sélectionnez l'onglet **Envoi du test** et ajoutez votre e-mail ou votre ID utilisateur dans le champ **Ajouter des utilisateurs individuels**. 
4. Cliquez sur **Envoyer le test** pour envoyer l'e-mail rédigé dans votre boîte de réception.

![Test d’e-mail]({% image_buster /assets/img_archive/testemail.png %}){: style="max-width:40%;" }

{% endtab %}
{% tab Notification push %}

#### Notification push mobile

1. Rédigez votre notification push mobile.
2. Sélectionnez l'onglet **Paramètres** et ajoutez votre e-mail ou votre ID utilisateur dans le champ **Ajouter des utilisateurs individuels**.
3. Cliquez sur **Envoyer le test** pour envoyer votre message rédigé à votre appareil.

![Test de notification push]({% image_buster /assets/img_archive/testpush.png %})

#### Push Web

1. Créez votre push web.
2. Sélectionnez l'onglet **Test**. 
3. Vérifier **Envoyer le test à moi-même.**
4. Cliquez sur **Envoyer le test** pour envoyer votre web push à votre web navigateur.

![Test de notification push web]({% image_buster /assets/img_archive/testwebpush.png %})

Si vous avez déjà accepté des messages push depuis le tableau de bord de Braze, le push apparaîtra dans le coin de votre écran. Sinon, cliquez sur **Autoriser** lorsque vous y êtes invité, et le message s'affichera.

{% endtab %}
{% tab Message in-app %}

Si vous avez les notifications push configurées dans votre application et sur votre appareil de test, vous pouvez envoyer des messages in-app à votre application pour voir à quoi ils ressemblent en temps réel. 

1. Rédigez votre message in-app.
2. Sélectionnez l'onglet **Test** et ajoutez votre e-mail ou votre ID utilisateur dans le champ **Ajouter des utilisateurs individuels**. 
3. Cliquez sur **Envoyer le test** pour envoyer votre message push à votre appareil.

Un message de notification push de test s’affiche en haut de l’écran de votre appareil.

![Test In App]({% image_buster /assets/img_archive/test-in-app.png %})

En cliquant directement sur le message push et en l'ouvrant, vous accéderez à votre application, où vous pourrez consulter le test de votre message in-app. Notez que cette fonctionnalité de test des messages in-app repose sur le fait que l'utilisateur clique sur une notification push de test pour déclencher le message in-app. À ce titre, l'utilisateur doit être éligible à recevoir des notifications push dans l'app concernée pour que la réception/distribution de la notification push de test soit réussie.

#### Résolution des problèmes

* Si votre campagne de messages in-app n'est pas déclenchée par une campagne push, vérifiez la segmentation de la campagne in-app pour confirmer que l'utilisateur correspond à l'audience cible **avant de** recevoir le message push.
* Pour les envois de test sur Android et iOS, les messages in-app qui utilisent le comportement de **demande d'autorisation de push** au clic peuvent ne pas s'afficher sur certains appareils. En guise de solution de rechange :
  * **Android :** Les appareils doivent être équipés d'Android 13 et de notre SDK Android version 21.0.0. Une autre raison peut être que l'appareil sur lequel le message in-app est affiché dispose déjà d'une invite au niveau du système. Il se peut que vous ayez sélectionné l'option **Ne plus demander**. Vous devrez alors réinstaller l'application pour réinitialiser les autorisations de notification avant de procéder à un nouveau test.
  * **iOS :** Nous recommandons à votre équipe de développeurs de revoir la mise en œuvre des notifications push pour votre application et de supprimer manuellement tout code qui demanderait des autorisations push. Pour plus d'informations, consultez la rubrique [Messages in-app d'amorce de notification push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).
* Pour qu'une campagne de messages in-app basée sur des actions fonctionne, les événements personnalisés doivent être enregistrés via le SDK de Braze, et non via les API REST, afin que l'utilisateur puisse recevoir les messages in-app éligibles directement sur son appareil. Les utilisateurs peuvent recevoir le message in-app s'ils effectuent l'événement au cours de la session.

{% endtab %}
{% tab Carte de contenu %}

Après avoir créé votre carte de contenu, vous pouvez en envoyer une de test à votre application pour voir ce à quoi elle ressemblera en temps réel.

1. Rédigez votre carte de contenu.
2. Sélectionnez l'onglet **Test** et sélectionnez au moins un groupe de test de contenu ou un utilisateur individuel pour recevoir ce message de test. 
3. Cliquez sur **Envoyer le test** pour envoyer votre carte de contenu à votre appli.

![Test de carte de contenu]({% image_buster /assets/img/contentcard_test.png %})

{% endtab %}
{% tab SMS/MMS %}

Après avoir créé votre message SMS ou MMS, vous pouvez envoyer un message test à votre téléphone pour voir à quoi il ressemblera en temps réel. 

1. Rédigez votre message SMS ou MMS.
2. Sélectionnez l'onglet **Test** et sélectionnez au moins un groupe de test de contenu ou un utilisateur individuel pour recevoir ce message de test. 
3. Cliquez sur **Envoyer le test** pour envoyer votre message de test.

![Test de carte de contenu]({% image_buster /assets/img/sms_test.png %})

{% endtab %}
{% tab Webhook %}

Après avoir créé votre webhook, vous pouvez effectuer un envoi de test pour vérifier la réponse du webhook. Sélectionnez l'onglet **Test** et sélectionnez **Envoyer un test** pour procéder à un envoi test sur l'URL de webhook fournie. Vous pouvez également sélectionner un utilisateur individuel pour prévisualiser la réponse en tant qu’utilisateur spécifique. 

![Test de carte de contenu]({% image_buster /assets/img/webhook_test.png %})

{% endtab %}
{% endtabs %}

## Tester des campagnes personnalisées 

Si vous testez des campagnes qui alimentent les données de l'utilisateur ou utilisent des propriétés d'événement personnalisées, vous devrez prendre des mesures supplémentaires ou différentes.

### Test de campagnes personnalisées en fonction des attributs de l'utilisateur

Si vous utilisez la [personnalisation]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/overview/) dans votre message, vous devrez prendre des mesures supplémentaires pour bien prévisualiser votre campagne et vérifier que les données des utilisateurs alimentent correctement le contenu.

Lors de l'envoi d'un message test, veillez à choisir l'option **Sélectionner un utilisateur existant** ou **Prévisualiser en tant qu'utilisateur personnalisé**.

![Test d'un message personnalisé]({% image_buster /assets/img_archive/personalized_testing.png %}){: style="max-width:70%;" }

#### Sélection d'un utilisateur existant

Si vous sélectionnez un utilisateur existant, saisissez l’ID utilisateur ou l’e-mail de l’utilisateur spécifique dans le champ de recherche. Utilisez ensuite l’aperçu du tableau de bord pour voir comment votre message s’affiche à cet utilisateur et envoyer un message test à votre appareil qui reflète ce que l’utilisateur verra.

![Sélectionnez un utilisateur]({% image_buster /assets/img_archive/personalized_testing_select.png %})

#### Sélection d'un utilisateur personnalisé

Si vous prévisualisez en tant qu'utilisateur personnalisé, saisissez le texte des différents champs disponibles pour la personnalisation, tels que le prénom de l'utilisateur et tout attribut personnalisé. Une fois encore, vous pouvez saisir votre propre adresse e-mail pour envoyer un test à votre appareil.

![Utilisateur personnalisé]({% image_buster /assets/img_archive/personalized_testing_custom.png %})

### Campagnes de test personnalisées avec des propriétés d'événement personnalisées

Le test des campagnes personnalisées avec des [propriétés d'événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/#custom-event-properties) diffère légèrement du test des autres types de campagnes décrites. La manière la plus robuste de tester des campagnes personnalisées à l'aide de propriétés d'événements personnalisés consiste à déclencher vous-même la campagne en procédant comme suit :

1. Rédigez la copie impliquant les propriétés d'événement. ![Composition d'un message de test avec les propriétés]({% image_buster /assets/img_archive/testeventproperties-compose.png %})
2. Utilisez la [livraison par événement]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) pour diffuser la campagne au moment où l'événement se produit.

{% alert note %}
Si vous testez une campagne de notification push iOS, vous devez régler le délai à 1 minute pour vous laisser le temps de quitter l’application car iOS n’envoie pas de notifications push à une application actuellement ouverte. D’autres types de campagnes peuvent être définis pour être envoyés immédiatement.
{% endalert %}

![Test de réception/distribution des messages]({% image_buster /assets/img_archive/testeventproperties-delivery.png %})

{: start="3"}
3\. Ciblez les utilisateurs comme vous le feriez pour les tests en utilisant un filtre de test ou en ciblant votre propre adresse e-mail, et terminez la création de la campagne. 

![Test du message de ciblage]({% image_buster /assets/img_archive/testeventproperties-target.png %})

{: start="4"}
4\. Accédez à votre application et finalisez l’événement personnalisé.

La campagne se déclenchera et affichera le message personnalisé avec la propriété event.

![Exemple de message de test]({% image_buster /assets/img_archive/testeventproperties-message.PNG %})

Sinon, si vous enregistrez des ID utilisateur personnalisés, vous pouvez également tester la campagne en envoyant un message de test personnalisé à vous-même.

1. Rédigez le texte de votre campagne.
2. Sélectionnez l'onglet **Test** et choisissez **Utilisateur personnalisé**. 
3. Ajoutez la propriété d'événement personnalisé au bas de la page, et ajoutez votre ID utilisateur ou votre adresse e-mail dans la case supérieure.
4. Cliquez sur **Envoyer le test** pour recevoir un message personnalisé avec la propriété.

![Test à l'aide d'un utilisateur personnalisé]({% image_buster /assets/img_archive/testeventproperties-customuser.png %})

