---
nav_title: Envoi de messages de test
article_title: Envoi de messages de test
page_order: 0
tool: 
  - Campaigns
page_type: reference
description: "Cet article de référence explique comment envoyer des messages de test sur les différents canaux de Braze et comment incorporer des propriétés d'événements personnalisés ou des attributs clients."

---

# Envoi de messages de test

> Avant d'envoyer une campagne de communication à vos utilisateurs, nous vous conseillons de procéder à des tests pour vous assurer que la campagne a l'aspect voulu et qu'elle fonctionne comme prévu. Vous pouvez créer et envoyer des messages de test à certains appareils ou membres de l'équipe à l'aide des outils du tableau de bord Braze.

{% alert important %}
Veillez à enregistrer votre projet de campagne après l'avoir testé afin d'éviter de supprimer votre campagne. Vous pouvez envoyer des messages de test sans enregistrer le message en tant que brouillon.
{% endalert %}

## Étape 1 : Identifiez vos utilisateurs test

Avant de tester votre campagne de messages, il est important d'identifier vos utilisateurs test. Il peut s'agir d'ID d'utilisateurs ou d'adresses e-mail existants, ou de nouveaux utilisateurs utilisés exclusivement pour tester les campagnes de communication. 

### En option : Créer un groupe de test de contenu

Un moyen pratique d'organiser vos utilisateurs test consiste à créer un [groupe de test de contenu]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/), qui comprend un groupe d'utilisateurs qui recevront les messages test des campagnes. Vous pouvez ajouter ce groupe de test au champ **Ajouter des groupes de test de contenu** sous **Destinataires du test** dans votre campagne, et lancer vos tests sans créer ou ajouter d'utilisateurs test individuels.

## Étape 2 : Envoi de messages de test spécifiques au canal

Pour connaître la marche à suivre pour envoyer des messages de test, reportez-vous à la section suivante pour votre canal respectif.

{% tabs local %}
{% tab Email %}

1. Rédigez votre message e-mail.
2. Sélectionnez **Prévisualiser et tester**.
3. Sélectionnez l'onglet **Test Send** et ajoutez votre e-mail ou votre ID utilisateur dans le champ **Add individual users.**  
4. Sélectionnez **Envoyer le test** pour envoyer l'e-mail rédigé dans votre boîte de réception.

!Test e-mail]({% image_buster /assets/img_archive/testemail.png %}){: style="max-width:40%;" }

{% endtab %}
{% tab Push %}

#### Poussée mobile

1. Rédigez votre push mobile.
2. Sélectionnez l'onglet **Paramètres** et ajoutez votre e-mail ou votre ID utilisateur dans le champ **Ajouter des utilisateurs individuels**.
3. Sélectionnez **Envoyer le test** pour envoyer votre message rédigé à votre appareil.

\![Test push]({% image_buster /assets/img_archive/testpush.png %})

#### Poussée sur le web

1. Créez votre push web.
2. Sélectionnez l'onglet **Test**. 
3. Sélectionnez **Envoyer le test à moi-même.**
4. Sélectionnez **Envoyer le test** pour envoyer votre push web à votre navigateur web.

\![Test web push]({% image_buster /assets/img_archive/testwebpush.png %})

Si vous avez déjà accepté des messages push depuis le tableau de bord de Braze, le push apparaîtra dans le coin de votre écran. Sinon, cliquez sur **Autoriser** lorsque vous y êtes invité, et le message s'affichera.

{% endtab %}
{% tab In-App Message %}

Si vous avez configuré des notifications push dans votre application et sur votre appareil de test, vous pouvez envoyer des messages in-app de test à votre application pour voir à quoi elle ressemble en temps réel. 

1. Rédigez votre message in-app.
2. Sélectionnez l'onglet **Test** et ajoutez votre e-mail ou votre ID utilisateur dans le champ **Ajouter des utilisateurs individuels**. 
3. Sélectionnez **Envoyer le test** pour envoyer votre message push à votre appareil.

Un message d'envoi de messages de test s'affiche en haut de l'écran de votre appareil.

\![Test In App]({% image_buster /assets/img_archive/test-in-app.png %})

En cliquant directement sur le message push et en l'ouvrant, vous accéderez à votre application, où vous pourrez consulter le test de votre message in-app. Notez que cette fonctionnalité de test des messages in-app repose sur le fait que l'utilisateur clique sur une notification push de test pour déclencher le message in-app. À ce titre, l'utilisateur doit être éligible à recevoir des notifications push dans l'app concernée pour que la réception/distribution de la notification push de test soit réussie.

{% endtab %}
{% tab Content Card %}

Après avoir créé votre carte de contenu, vous pouvez envoyer une carte de contenu test à votre appli pour voir à quoi elle ressemblera en temps réel.

1. Rédigez votre carte de contenu.
2. Sélectionnez l'onglet **Test** et sélectionnez au moins un groupe de test de contenu ou un utilisateur individuel pour recevoir ce message de test. 
3. Sélectionnez **Envoyer le test** pour envoyer votre carte de contenu à votre appli.

!Carte de contenu du test]({% image_buster /assets/img/contentcard_test.png %})

{% endtab %}
{% tab SMS/MMS %}

Après avoir créé votre message SMS ou MMS, vous pouvez envoyer un message test à votre téléphone pour voir à quoi il ressemblera en temps réel. 

1. Rédigez votre message SMS ou MMS.
2. Sélectionnez l'onglet **Test** et sélectionnez au moins un groupe de test de contenu ou un utilisateur individuel pour recevoir ce message de test. 
3. Sélectionnez **Envoyer le test** pour envoyer votre message de test.

!Carte de contenu du test]({% image_buster /assets/img/sms_test.png %})

{% endtab %}
{% tab Webhook %}

Après avoir créé votre webhook, vous pouvez effectuer un envoi test pour vérifier la réponse du webhook. Sélectionnez l'onglet **Test** et sélectionnez **Envoyer un** test pour envoyer un test à l'URL webhook fournie. Vous pouvez également sélectionner un utilisateur individuel pour prévisualiser la réponse en tant qu'utilisateur spécifique. 

!Carte de contenu du test]({% image_buster /assets/img/webhook_test.png %})

{% endtab %}
{% endtabs %}

## Tester des campagnes personnalisées 

Si vous testez des campagnes qui alimentent des données utilisateur ou utilisent des propriétés d'événement personnalisées, vous devrez prendre des mesures supplémentaires ou différentes.

### Test de campagnes personnalisées en fonction des attributs de l'utilisateur

Si vous utilisez la [personnalisation]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/overview/) dans votre message, vous devrez prendre des mesures supplémentaires pour bien prévisualiser votre campagne et vérifier que les données des utilisateurs alimentent correctement le contenu.

Lors de l'envoi d'un message test, veillez à choisir l'option **Sélectionner un utilisateur existant** ou Prévisualiser en tant qu'**utilisateur personnalisé**.

!Test d'un message personnalisé]({% image_buster /assets/img_archive/personalized_testing.png %}){: style="max-width:70%;" }

#### Sélection d'un utilisateur existant

Si vous sélectionnez un utilisateur existant, saisissez l'ID ou l'e-mail de l'utilisateur dans le champ de recherche. Ensuite, utilisez l'aperçu du tableau de bord pour voir comment votre message apparaîtrait à cet utilisateur, et envoyez un message test à votre appareil qui reflète ce que cet utilisateur verrait.

\![Sélectionnez un utilisateur]({% image_buster /assets/img_archive/personalized_testing_select.png %})

#### Sélection d'un utilisateur personnalisé

Si vous prévisualisez en tant qu'utilisateur personnalisé, saisissez le texte des différents champs disponibles pour la personnalisation, tels que le prénom de l'utilisateur et tout attribut personnalisé. Là encore, vous pouvez saisir votre propre adresse e-mail pour envoyer un test à votre appareil.

\![Utilisateur personnalisé]({% image_buster /assets/img_archive/personalized_testing_custom.png %})

### Campagnes de test personnalisées avec des propriétés d'événement personnalisées

Le test des campagnes personnalisées avec des [propriétés d'événement personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) diffère légèrement du test des autres types de campagnes décrites. 

{% tabs local %}
{% tab Trigger manually %}

#### Méthode 1 : Déclencher une campagne manuellement

Vous pouvez déclencher la campagne vous-même. Il s'agit d'un moyen efficace de tester des campagnes personnalisées à l'aide de propriétés d'événements personnalisés :

1. Rédigez la copie impliquant les propriétés d'événement. 

!Composition d'un message de test avec des propriétés]({% image_buster /assets/img_archive/testeventproperties-compose.png %})

{: start="2"}
2\. Utilisez la [livraison par événement]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) pour diffuser la campagne au moment où l'événement se produit.

{% alert note %}
Si vous testez une campagne push iOS, vous devez régler le délai sur une minute pour vous laisser le temps de quitter l'application, car iOS ne délivre pas de notifications push pour l'application actuellement ouverte. D'autres types de campagnes peuvent être programmés pour une diffusion immédiate.
{% endalert %}

!Test de réception/distribution du message]({% image_buster /assets/img_archive/testeventproperties-delivery.png %})

{: start="3"}
3\. Ciblez les utilisateurs comme vous le feriez pour les tests en utilisant un filtre de test ou en ciblant votre propre adresse e-mail, et terminez la création de la campagne. 

!Test de ciblage des messages]({% image_buster /assets/img_archive/testeventproperties-target.png %})

{: start="4"}
4\. Allez dans votre application et complétez l'événement personnalisé.

La campagne se déclenchera et affichera le message personnalisé avec la propriété event.

!Exemple de message de test]({% image_buster /assets/img_archive/testeventproperties-message2.png %})

{% endtab %}
{% tab Test message %}

#### Méthode 2 : Envoi d'un message test à vous-même

Par ailleurs, si vous enregistrez des ID utilisateurs personnalisés, vous pouvez également tester la campagne en vous envoyant un message test personnalisé.

1. Rédigez le texte de votre campagne.
2. Sélectionnez l'onglet **Test** et choisissez **Utilisateur personnalisé**. 
3. Ajoutez la propriété d'événement personnalisé au bas de la page, et ajoutez votre ID utilisateur ou votre adresse e-mail dans la case supérieure.
4. Sélectionnez **Envoyer le test** pour recevoir un message personnalisé avec la propriété.

Test de l'utilisation d'un utilisateur personnalisé]({% image_buster /assets/img_archive/testeventproperties-customuser.png %})

{% endtab %}
{% tab Liquid %}

#### Méthode 3 : Utilisation du liquide

Vous pouvez tester les propriétés d'événements personnalisés en saisissant manuellement des valeurs avec Liquid. 

1. Dans l'éditeur de messages, saisissez les valeurs des propriétés d'événement personnalisées.
2. Sélectionnez l'onglet **Aperçu en tant qu'utilisateur** pour vérifier que le message correct s'affiche.

{% endtab %}
{% endtabs %}

## Résolution des problèmes

### Messages in-app

Si votre campagne de messages in-app n'est pas déclenchée par une campagne push, vérifiez la segmentation de la campagne in-app pour confirmer que l'utilisateur correspond à l'audience cible **avant de** recevoir le message push.

Pour les envois de test sur Android et iOS, les messages in-app qui utilisent le comportement de **demande d'autorisation de push** au clic peuvent ne pas s'afficher sur certains appareils. En guise de solution de rechange :
- **Android :** Les appareils doivent être équipés d'Android 13 et de notre SDK Android version 21.0.0. Une autre raison peut être que l'appareil sur lequel le message in-app est affiché dispose déjà d'une invite au niveau du système. Il se peut que vous ayez sélectionné l'option **Ne plus demander**. Vous devrez alors réinstaller l'application pour réinitialiser les autorisations de notification avant de procéder à un nouveau test.
- **iOS :** Nous recommandons à votre équipe de développeurs de revoir la mise en œuvre des notifications push pour votre application et de supprimer manuellement tout code qui demanderait des autorisations push. Pour plus d'informations, consultez la rubrique [Messages in-app de l'amorce de poussée]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

Pour qu'une campagne de messages in-app basée sur des actions fonctionne, les événements personnalisés doivent être enregistrés via le SDK de Braze, et non via les API REST, afin que l'utilisateur puisse recevoir les messages in-app éligibles directement sur son appareil. Les utilisateurs peuvent recevoir le message in-app s'ils effectuent l'événement pendant la session.
