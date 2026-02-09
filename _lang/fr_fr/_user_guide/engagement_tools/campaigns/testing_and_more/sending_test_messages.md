---
nav_title: Envoi de messages de test
article_title: Envoi de messages de test
page_order: 0
tool: 
  - Campaigns
page_type: reference
description: "Le présent article de référence explique comment envoyer des messages de test sur les différents canaux de Braze et comment incorporer des propriétés d’événement personnalisé ou des attributs utilisateur."

---

# Envoi de messages de test

> Avant d'envoyer une campagne de communication à vos utilisateurs, nous vous conseillons de procéder à des tests pour vous assurer que la campagne se présente bien et qu'elle fonctionne comme prévu. Vous pouvez créer et envoyer des messages de test pour sélectionner des appareils ou des membres de l’équipe à l’aide des outils du Tableau de bord de Braze.

{% alert important %}
Assurez-vous d’enregistrer le brouillon de votre campagne après l’avoir testée pour éviter de la supprimer. Vous pouvez envoyer des messages de test sans enregistrer le message comme brouillon.
{% endalert %}

## Étape 1 : Identifier vos utilisateurs test

Avant de tester votre campagne de communication, il est important d’identifier vos utilisateurs test. Ces utilisateurs peuvent être soit des ID utilisateur ou des adresses e-mail existants, soit de nouveaux utilisateurs qui sont utilisés exclusivement pour tester les campagnes de communication. 

### Facultatif : Créer un groupe de test de contenu

Un moyen pratique d'organiser vos utilisateurs test consiste à créer un [groupe de test de contenu]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/), qui comprend un groupe d'utilisateurs qui recevront les messages test des campagnes. Vous pouvez ajouter ce groupe de test au champ **Ajouter des groupes de test de contenu** sous **Destinataires du test** dans votre campagne, et lancer vos tests sans créer ou ajouter d'utilisateurs test individuels.

## Étape 2 : Envoi de messages de test spécifiques au canal

Pour connaître la marche à suivre pour envoyer des messages de test, reportez-vous à la section suivante pour votre canal respectif.

{% tabs local %}
{% tab Banners %}

{% alert important %}
Avant de pouvoir tester les messages des bannières dans Braze, vous devez créer une campagne de communication dans Braze. En outre, vérifiez que le placement que vous souhaitez tester est déjà [placé dans votre application ou votre site web.]({{site.baseurl}}/developer_guide/banners/placements)
{% endalert %}

Après avoir créé votre message de bannière, vous pouvez prévisualiser votre bannière ou envoyer un message de test.

1. Rédigez votre message de bannière.
2. Sélectionnez **Aperçu** pour prévisualiser votre bannière ou envoyer un message test.
3. Pour envoyer un message de test, ajoutez un groupe de test de contenu ou un ou plusieurs utilisateurs individuels en tant que **destinataires du test**, puis sélectionnez **Envoyer le test.** 

Vous pourrez consulter votre message de test sur l'appareil pendant 5 minutes maximum.

![Onglet Aperçu du compositeur de bannières.]({% image_buster /assets/img/banners/preview_banner.png %})

{% alert note %}
Gardez à l'esprit que votre aperçu peut ne pas être identique au rendu final sur l'appareil d'un utilisateur en raison des différences entre les matériels.
{% endalert %}

### Liste de contrôle des tests

- Votre campagne Banner est-elle assignée à un placement ?
- Les images et les médias s'affichent-ils et agissent-ils comme prévu sur les types d'appareils et les tailles d'écran que vous avez ciblés ?
- Vos liens et boutons dirigent-ils l'utilisateur vers l'endroit où il doit se rendre ?
- Le Liquid fonctionne-t-il comme prévu ? Avez-vous pris en compte une valeur d’attribut par défaut si le Liquid ne renvoie aucune information ?
- Votre texte est-il clair, concis et correct ?

{% endtab %}
{% tab Content Card %}

{% alert warning %}
Pour envoyer un test à des [groupes de test de contenu]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) ou à des utilisateurs individuels, la fonction push doit être activée sur vos appareils de test et des jetons push valides doivent être enregistrés pour l'utilisateur test avant l'envoi. Pour les utilisateurs iOS, vous devez appuyer sur la notification push envoyée par Braze pour afficher la carte de contenu test. Ce comportement s’applique uniquement aux tests des cartes de contenu.
{% endalert %}

Après avoir créé votre carte de contenu, vous pouvez en envoyer une de test à votre application pour voir ce à quoi elle ressemblera en temps réel.

1. Rédigez votre carte de contenu.
2. Sélectionnez l'onglet **Test** et sélectionnez au moins un groupe de test de contenu ou un utilisateur individuel pour recevoir ce message de test. 
3. Sélectionnez **Envoyer le test** pour envoyer votre carte de contenu à votre appli.

![Tester une carte de contenu]({% image_buster /assets/img/contentcard_test.png %})

### Aperçu

Vous pouvez prévisualiser votre carte au fur et à mesure que vous la composez dans l'onglet **Aperçu.**  Cela devrait vous aider à visualiser à quoi ressemblera votre message final du point de vue de l’utilisateur.

{% alert note %}
Dans l'onglet **Aperçu** de votre compositeur, l'affichage de votre message peut ne pas être identique à son rendu réel sur l'appareil de l'utilisateur. Nous vous recommandons d’envoyer toujours un message test à un appareil pour vérifier que votre support, votre texte, votre personnalisation et vos attributs personnalisés sont générés correctement.
{% endalert %}

### Liste de contrôle des tests

- Les images et les données s’affichent-elles et se comportent-elles comme prévu ?
- Le Liquid fonctionne-t-il comme prévu ? Avez-vous prévu une [valeur d'attribut par défaut]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) si le liquide ne renvoie aucune information ?
- Votre texte est-il clair, concis et correct ?
- Vos liens dirigent-ils l’utilisateur vers les bons endroits ?

### Débogage

Après l'envoi de vos cartes de contenu, vous pouvez résoudre ou déboguer tout problème à partir du [journal des événements utilisateurs]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) sur la console de développement. 

C’est notamment utile pour comprendre pourquoi un utilisateur n’arrive pas à voir une carte de contenu spécifique. Pour ce faire, vous pouvez rechercher dans les **journaux des événements utilisateurs** les cartes de contenu transmises au SDK au début de la session, mais avant une impression, et les rattacher à une campagne spécifique :

1. Sélectionnez **Paramètres** > **Journal des événements utilisateurs**.
2. Localisez et développez la demande SDK pour votre utilisateur test.
3. Cliquez sur **Données brutes**.
4. Trouvez le `id` pour votre session. Voici un échantillon d’exemple :

    ```json
    [
      {
        "session_id": "D1B051E6-469B-47E2-B830-5A728D1D4AC5",
        "data": {
          "ids": [
            "NDg2MTY5MmUtNmZjZS00MjE1LWJkMDUtMzI1NGZiOWU5MDU3"
          ]
        },
        "name": "cci",
        "time": 1636106490.155
      }
    ]
    ```
    
{: start="5"}
5\. Utilisez un outil de décodage comme [Base64 Decode and Encode](https://www.base64decode.org/) pour décoder le `id` du format Base64 et trouver le `campaign_id` associé. Dans notre exemple, cela donne les résultats suivants :

    ```
    4861692e-6fce-4215-bd05-3254fb9e9057_$_cc=c3b25740-f113-c047-4b1d-d296f280af4f&mv=6185005b9d9bee79387cce45&pi=cmp
    ```

    Where `4861692e-6fce-4215-bd05-3254fb9e9057` is the `campaign_id`.<br><br>

6. Rendez-vous sur la page des **campagnes** et recherchez le site `campaign_id`.

![Recherchez campaign_id sur la page des campagnes]({% image_buster /assets/img_archive/cc_debug.png %}){: style="max-width:80%;"}

Ensuite, vous pouvez examiner les paramètres et le contenu de vos messages pour déterminer pourquoi un utilisateur ne voit pas une carte de contenu particulière.

{% endtab %}
{% tab Email %}

1. Rédigez votre message e-mail.
2. Sélectionnez **Prévisualiser et tester**.
3. Sélectionnez l'onglet **Test Send** et ajoutez votre e-mail ou votre ID utilisateur dans le champ **Add individual users.**  
4. Sélectionnez **Envoyer le test** pour envoyer l'e-mail rédigé dans votre boîte de réception.

![Test e-mail]({% image_buster /assets/img_archive/testemail.png %}){: style="max-width:40%;" }

{% endtab %}
{% tab In-app message %}

{% alert warning %}
Pour envoyer un test à des [groupes de test de contenu]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) ou à des utilisateurs individuels, la fonction push doit être activée sur vos appareils de test avant l'envoi. Par exemple, vous devez avoir activé le push sur votre appareil iOS pour pouvoir appuyer sur la notification avant l'affichage du message de test. {% endalert %}

Si vous avez les notifications push configurées dans votre application et sur votre appareil de test, vous pouvez envoyer des messages in-app à votre application pour voir à quoi ils ressemblent en temps réel. 

1. Rédigez votre message in-app.
2. Sélectionnez l'onglet **Test** et ajoutez votre e-mail ou votre ID utilisateur dans le champ **Ajouter des utilisateurs individuels**. 
3. Sélectionnez **Envoyer le test** pour envoyer votre message push à votre appareil.

Un message de notification push de test s’affiche en haut de l’écran de votre appareil.

![Test in-app]({% image_buster /assets/img_archive/test-in-app.png %})

{% alert important %}
Les envois test peuvent entraîner l'envoi de plusieurs messages in-app à chaque destinataire.
{% endalert %}

En cliquant directement sur le message push et en l'ouvrant, vous accéderez à votre application, où vous pourrez consulter le test de votre message in-app. Notez que cette fonctionnalité de test des messages in-app repose sur le fait que l'utilisateur clique sur une notification push de test pour déclencher le message in-app. À ce titre, l'utilisateur doit être éligible à recevoir des notifications push dans l'app concernée pour que la réception/distribution de la notification push de test soit réussie.

### Aperçu

Vous pouvez prévisualiser votre message in-app au fur et à mesure que vous le composez dans l'onglet **Aperçu.**  Cela devrait vous aider à visualiser à quoi ressemblera votre message final du point de vue de l’utilisateur. Vous pouvez prévisualiser l'aspect de votre message pour un utilisateur aléatoire, un utilisateur spécifique ou un utilisateur personnalisé. Vous pouvez également prévisualiser les messages pour les appareils mobiles ou les tablettes.

![Onglet Compose (Composer) lors de la création d’un message in-app montrant l’aperçu de son apparence. Aucun utilisateur n’étant sélectionné, la section du corps affiche Liquid tel quel après son ajout.]({% image_buster /assets/img/in-app-message-preview.png %})

Braze dispose de trois générations de messages in-app disponibles. Vous pouvez affiner les appareils auxquels vos messages doivent envoyés, en fonction de la génération qu’ils prennent en charge.

![Passage d'une génération à l'autre lors de la prévisualisation d'un message in-app.]({% image_buster /assets/img/iam-generations.gif %}){: height="50%" width="50%"}

{% alert warning %}
Dans l **'aperçu**, l'affichage de votre message peut ne pas être identique à son rendu réel sur l'appareil de l'utilisateur. Nous vous recommandons toujours d’envoyer un message test à un appareil pour vous assurer que vos données, le texte, la personnalisation et les attributs personnalisés se génèrent correctement.
{% endalert %}

### Liste de contrôle des tests

- Les images et les données s’affichent-elles et se comportent-elles comme prévu ?
- Le Liquid fonctionne-t-il comme prévu ? Avez-vous prévu une [valeur d'attribut par défaut]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) si le liquide ne renvoie aucune information ?
- Votre texte est-il clair, concis et correct ?
- Vos boutons dirigent-ils l’utilisateur à l’endroit correct ?

### Scanner d'accessibilité

Pour soutenir les meilleures pratiques en matière d'accessibilité, Braze analyse automatiquement le contenu des messages in-app créés à l'aide de l'éditeur HTML traditionnel par rapport aux normes d'accessibilité. Ce scanner permet d'identifier les contenus susceptibles de ne pas répondre aux normes[WCAG (](https://www.w3.org/WAI/standards-guidelines/wcag/)Web Content Accessibility Guidelines). Les WCAG sont un ensemble de normes techniques internationalement reconnues, élaborées par le World Wide Web Consortium (W3C) pour rendre le contenu des sites web plus accessible aux personnes handicapées.

![Résultats de l'analyse d'accessibilité]({% image_buster /assets/img/Accessibilty_Scanner_IAM.png %})

{% alert note %}
L'analyseur d'accessibilité des messages in-app ne fonctionne que sur les messages créés avec du HTML personnalisé.
{% endalert %}

#### Fonctionnement

Le scanner s'exécute automatiquement sur les messages HTML personnalisés et évalue l'ensemble de votre message HTML par rapport à l'[ensemble des règles WCAG 2.1 AA.](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.1&currentsidebar=%23col_customize&levels=aaa) Pour chaque problème signalé, il indique

- L'élément HTML spécifique concerné
- Une description du problème d'accessibilité
- Un lien vers un contexte supplémentaire ou des conseils de remédiation

#### Comprendre les tests d'accessibilité automatisés

{% multi_lang_include accessibility/automated_testing.md %}

{% endtab %}
{% tab LINE %}

1. Créez votre message LINE.
2. Sélectionnez l'onglet **Test** et sélectionnez au moins un groupe de test de contenu ou un utilisateur individuel pour recevoir ce message de test.
3. Sélectionnez **Envoyer le test** pour envoyer votre message.

![Envoi de messages sur la ligne de test.]({% image_buster /assets/img/line/test_preview.png %})

{% endtab %}
{% tab Push %}

#### Notification push mobile

1. Rédigez votre notification push mobile.
2. Sélectionnez l'onglet **Test** et ajoutez votre e-mail ou votre ID utilisateur dans le champ **Ajouter des utilisateurs individuels**.
3. Sélectionnez **Envoyer le test** pour envoyer votre message rédigé à votre appareil.

![Test de notification push]({% image_buster /assets/img_archive/testpush.png %})

#### Push Web

1. Créez votre push web.
2. Sélectionnez l'onglet **Test**. 
3. Sélectionnez **Envoyer le test à moi-même.**
4. Sélectionnez **Envoyer le test** pour envoyer votre push web à votre navigateur web.

![Test de notification push Web]({% image_buster /assets/img_archive/testwebpush.png %})

Si vous avez déjà accepté des messages push depuis le tableau de bord de Braze, le push apparaîtra dans le coin de votre écran. Sinon, cliquez sur **Autoriser** lorsque vous y êtes invité, et le message s'affichera.

{% endtab %}
{% tab SMS/MMS and RCS %}

Après avoir créé votre message SMS, MMS ou RCS, vous pouvez envoyer un message test à votre téléphone pour voir à quoi il ressemblera en temps réel. 

1. Rédigez votre message SMS, MMS ou RCS.
2. Sélectionnez l'onglet **Test** et sélectionnez au moins un groupe de test de contenu ou un utilisateur individuel pour recevoir ce message de test. 
3. Sélectionnez **Envoyer le test** pour envoyer votre message de test.

![Tester une carte de contenu]({% image_buster /assets/img/sms_test.png %})

{% endtab %}
{% tab Webhook %}

Après avoir créé votre webhook, vous pouvez effectuer un envoi de test pour vérifier la réponse du webhook. Sélectionnez l'onglet **Test** et sélectionnez **Envoyer un test** pour procéder à un envoi test sur l'URL de webhook fournie. Vous pouvez également sélectionner un utilisateur individuel pour prévisualiser la réponse en tant qu’utilisateur spécifique. 

![Tester une carte de contenu]({% image_buster /assets/img/webhook_test.png %})

{% endtab %}
{% tab WhatsApp %}

1. Créez votre message WhatsApp.
2. Sélectionnez l'onglet **Test** et sélectionnez au moins un groupe de test de contenu ou un utilisateur individuel pour recevoir ce message de test.
3. Initiez une fenêtre de conversation en envoyant un message WhatsApp au numéro de téléphone associé au groupe d'abonnement que vous utilisez pour ce message. Le numéro de téléphone associé est répertorié dans l'alerte de l'onglet **Test.** 
4. Sélectionnez **Envoyer le test** pour envoyer votre message.

![Testez le message WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp_test.png %})

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

![Sélectionner un utilisateur]({% image_buster /assets/img_archive/personalized_testing_select.png %})

#### Sélection d'un utilisateur personnalisé

Si vous prévisualisez en tant qu'utilisateur personnalisé, saisissez le texte des différents champs disponibles pour la personnalisation, tels que le prénom de l'utilisateur et tout attribut personnalisé. Une fois encore, vous pouvez saisir votre propre adresse e-mail pour envoyer un test à votre appareil.

![Utilisateur personnalisé]({% image_buster /assets/img_archive/personalized_testing_custom.png %})

#### Personnaliser un utilisateur existant

Vous pouvez modifier des champs individuels d'un utilisateur aléatoire ou existant pour vous aider à tester le contenu dynamique de votre message. Sélectionnez **Modifier** pour convertir l'utilisateur sélectionné en un utilisateur personnalisé que vous pouvez modifier.

![L'onglet "Prévisualisation en tant qu'utilisateur" avec un bouton "Modifier".]({% image_buster /assets/img_archive/edit_user_preview.png %}){: style="max-width:50%;"}

### Campagnes de test personnalisées avec des propriétés d'événement personnalisées

Le test des campagnes personnalisées avec des [propriétés d'événement personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) diffère légèrement du test des autres types de campagnes décrites. 

{% tabs local %}
{% tab Trigger manually %}

#### Méthode 1 : Déclencher une campagne manuellement

Vous pouvez déclencher la campagne vous-même. Il s'agit d'un moyen efficace de tester des campagnes personnalisées à l'aide de propriétés d'événements personnalisés :

1. Rédigez la copie impliquant les propriétés d'événement. 

![Composer un message de test avec des propriétés]({% image_buster /assets/img_archive/testeventproperties-compose.png %})

{: start="2"}
2\. Utilisez la [livraison par événement]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) pour diffuser la campagne au moment où l'événement se produit.

{% alert note %}
Si vous testez une campagne push iOS, vous devez régler le délai sur une minute pour vous laisser le temps de quitter l'application, car iOS ne délivre pas de notifications push pour l'application actuellement ouverte. D’autres types de campagnes peuvent être définis pour être envoyés immédiatement.
{% endalert %}

![Tester la livraison d’un message]({% image_buster /assets/img_archive/testeventproperties-delivery.png %})

{: start="3"}
3\. Ciblez les utilisateurs comme vous le feriez pour les tests en utilisant un filtre de test ou en ciblant votre propre adresse e-mail, et terminez la création de la campagne. 

![Tester le ciblage d’un message]({% image_buster /assets/img_archive/testeventproperties-target.png %})

{: start="4"}
4\. Accédez à votre application et finalisez l’événement personnalisé.

La campagne se déclenchera et affichera le message personnalisé avec la propriété event.

![Tester l’exemple de message]({% image_buster /assets/img_archive/testeventproperties-message2.png %})

{% endtab %}
{% tab Test message %}

#### Méthode 2 : Envoi d'un message test à vous-même

Sinon, si vous enregistrez des ID utilisateur personnalisés, vous pouvez également tester la campagne en envoyant un message de test personnalisé à vous-même.

1. Rédigez le texte de votre campagne.
2. Sélectionnez l'onglet **Test** et choisissez **Utilisateur personnalisé**. 
3. Ajoutez la propriété d'événement personnalisé au bas de la page, et ajoutez votre ID utilisateur ou votre adresse e-mail dans la case supérieure.
4. Sélectionnez **Envoyer le test** pour recevoir un message personnalisé avec la propriété.

![Tester en utilisant un utilisateur personnalisé]({% image_buster /assets/img_archive/testeventproperties-customuser.png %})

{% endtab %}
{% tab Liquid %}

#### Méthode 3 : Utilisation de Liquid

Vous pouvez tester les propriétés d'événements personnalisés en saisissant manuellement des valeurs avec Liquid. 

1. Dans l'éditeur de messages, saisissez les valeurs des propriétés d'événement personnalisées.
2. Sélectionnez l'onglet **Aperçu en tant qu'utilisateur** pour vérifier que le message correct s'affiche.

{% endtab %}
{% endtabs %}

## Résolution des problèmes

### in-app Messages

Si votre campagne de messages in-app n'est pas déclenchée par une campagne push, vérifiez la segmentation de la campagne in-app pour confirmer que l'utilisateur correspond à l'audience cible **avant de** recevoir le message push.

Pour les envois de test sur Android et iOS, les messages in-app qui utilisent le comportement de **demande d'autorisation de push** au clic peuvent ne pas s'afficher sur certains appareils. En guise de solution de rechange :
- **Android :** Les appareils doivent être équipés d'Android 13 et de notre SDK Android version 21.0.0. Une autre raison peut être que l'appareil sur lequel le message in-app est affiché dispose déjà d'une invite au niveau du système. Il se peut que vous ayez sélectionné l'option **Ne plus demander**. Vous devrez alors réinstaller l'application pour réinitialiser les autorisations de notification avant de procéder à un nouveau test.
- **iOS :** Nous recommandons à votre équipe de développeurs de revoir la mise en œuvre des notifications push pour votre application et de supprimer manuellement tout code qui demanderait des autorisations push. Pour plus d'informations, consultez la rubrique [Messages in-app d'amorce de notification push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

Pour qu'une campagne de messages in-app basée sur des actions fonctionne, vous devez enregistrer des événements personnalisés via le SDK de Braze, et non via les API REST, afin que les utilisateurs puissent recevoir des messages in-app éligibles directement sur leur appareil. Les utilisateurs reçoivent le message in-app s'ils effectuent l'événement au cours de la session.
