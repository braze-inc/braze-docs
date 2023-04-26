---
nav_title: Envoyer des messages de test
article_title: Envoyer des messages de test
page_order: 0
tool: 
  - Campaigns
page_type: reference
description: "Le présent article de référence explique comment envoyer des messages de test sur les différents canaux de Braze et comment incorporer des propriétés de l’événement personnalisées ou des attributs utilisateur."

---

# Envoyer des messages de test

> Avant d’envoyer une campagne de communication à vos utilisateurs, en tant que bonne pratique, vous pouvez la tester pour vous assurer qu’elle semble correcte et fonctionne de la manière prévue. Vous pouvez créer et envoyer des messages de test pour sélectionner des appareils ou des membres de l’équipe à l’aide des outils du Tableau de bord de Braze.

{% alert important %}
Assurez-vous d’enregistrer le brouillon de votre campagne après l’avoir testée pour éviter de la supprimer. Vous pouvez envoyer des messages de test sans enregistrer le message comme brouillon.
{% endalert %}

## Identifier vos utilisateurs test

Avant de tester votre campagne de communication, il est important d’identifier vos utilisateurs test. Ces utilisateurs peuvent être soit des ID utilisateur ou des adresses e-mail existants, soit de nouveaux utilisateurs qui sont utilisés exclusivement pour tester les campagnes de communication. 

### Créer un groupe interne

Vous pouvez également mieux organiser vos utilisateurs test en créant un [Groupe de tests de contenu]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/), qui comprend un groupe d’utilisateurs qui recevront des messages test des campagnes. De cette façon, vous pouvez ajouter ce groupe de tests dans le champ **Add Content Test Groups (Ajouter des groupes de tests de contenu)** sous **Test Recipients (Destinataires de test)** dans votre campagne, et lancer vos tests sans créer ou ajouter des utilisateurs test individuels.

## Envoyer un test spécifique à un canal

Pour connaître la procédure d’envoi des messages de test, reportez-vous à la section suivante pour votre canal.

{% tabs %}
{% tab Email %}

Après avoir rédigé votre e-mail, cliquez sur **Aperçu et test**. Dans cette page, sélectionnez l’onglet **Tester l’envoi** et ajoutez votre adresse e-mail ou votre ID utilisateur dans le champ **Ajouter des utilisateurs individuels**. Lorsque vous êtes prêt, cliquez sur **Envoyer un test** pour envoyer votre e-mail rédigé à votre boîte de réception.

![Test d’e-mail]({% image_buster /assets/img_archive/testemail.png %}){: style="max-width:40%;" }

{% endtab %}
{% tab Push %}

#### Notification push mobile

Après avoir rédigé votre notification push mobile, sélectionnez l’onglet **Paramètres** et ajoutez votre adresse e-mail ou votre ID utilisateur dans le champ **Ajouter des utilisateurs individuels**. Lorsque vous êtes prêt, cliquez sur **Envoyer un test** pour envoyer votre message rédigé à votre appareil.

![Test de notification push]({% image_buster /assets/img_archive/testpush.png %})

#### Push Web

Après avoir créé votre notification push Web, sélectionnez l’onglet **Paramètres**. Cochez **Envoyer le test à moi-même** et cliquez sur **Envoyer un test**.

![Test de notification push Web]({% image_buster /assets/img_archive/testwebpush.png %})

Si vous avez déjà accepté des messages de notification push depuis le tableau de bord de Braze, vous verrez la notification push dans le coin de votre écran. Sinon, cliquez sur **Autoriser** lorsque vous y êtes invité et le message va apparaître.

{% endtab %}
{% tab In-App Message %}

Si vous avez les notifications push configurées dans votre application et sur votre appareil de test, vous pouvez envoyer des messages in-app à votre application pour voir à quoi ils ressemblent en temps réel. 

Après avoir rédigé votre message in-app, sélectionnez l’onglet **Tester** et ajoutez votre adresse e-mail ou votre ID utilisateur dans le champ **Ajouter des utilisateurs individuels**. Lorsque vous êtes prêt, cliquez sur **Envoyer un test**. Un message de notification push de test s’affiche en haut de l’écran de votre appareil. 

![Test in-app]({% image_buster /assets/img_archive/test-in-app.png %})

Cliquer directement et ouvrir le message de notification push vous enverra à votre application dans laquelle vous pourrez visualiser votre test de message in-app. Notez que la fonctionnalité de test du message in-app dépend du fait que l’utilisateur clique sur une notification push pour le déclencher.

{% endtab %}
{% tab Content Card %}

Après avoir créé votre carte de contenu, vous pouvez en envoyer une de test à votre application pour voir ce à quoi elle ressemblera en temps réel. Après avoir rédigé votre carte de contenu, sélectionnez l’onglet **Tester** et sélectionnez au moins un groupe de test de contenu ou un utilisateur individuel pour recevoir ce message de test. 

![Tester une carte de contenu]({% image_buster /assets/img/contentcard_test.png %})

{% endtab %}
{% tab SMS/MMS %}

Après avoir créé votre message SMS ou MMS, vous pouvez envoyer un message de test à votre téléphone pour voir ce à quoi il ressemblera en temps réel. Après avoir rédigé votre message, cliquez l’onglet **Tester** et sélectionnez au moins un groupe de test de contenu ou un utilisateur individuel pour recevoir ce message de test. 

![Tester une carte de contenu]({% image_buster /assets/img/sms_test.png %})

{% endtab %}
{% tab Webhook %}

Après avoir créé votre webhook, vous pouvez effectuer un envoi de test pour vérifier la réponse du webhook. Sélectionnez l’onglet **Test (Tester)** et sélectionnez **Send Test (Envoyer un test)** pour envoyer un test à l’URL du webhook fourni. Vous pouvez également sélectionner un utilisateur individuel pour prévisualiser la réponse en tant qu’utilisateur spécifique. 

![Tester une carte de contenu]({% image_buster /assets/img/webhook_test.png %})

{% endtab %}
{% tab News Feed %}

{% alert note %}
Le Fil d’actualité est obsolète. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu : il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

L’envoi d’un test de carte de fil d’actualité nécessite de configurer un segment d’essai et d’envoyer ensuite une campagne de test.

##### Étape 1 : Créer un segment d’essai spécifié

Une fois que vous avez configuré un segment d’essai, vous pouvez utiliser ces canaux de messagerie. Le processus prend quelques courtes étapes et, s’il est configuré correctement, ne doit être effectué qu’une seule fois.

Allez à la page **Segments** et créez un nouveau segment. Dans le menu déroulant sous **Ajouter un filtre**, localisez les filtres de test au bas de la liste.

![Filtres de test]({% image_buster /assets/img_archive/testmessages1.png %})

Utilisez ces filtres de test pour sélectionner des utilisateurs avec des adresses e-mail spécifiques ou des [ID utilisateur]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/) externes.

![Options de filtre de test]({% image_buster /assets/img_archive/testmessages2.png %})

Ces filtres ont les options suivantes :

1. **Égal à** : recherche l’e-mail ou l’ID utilisateur exact que vous fournissez. Utilisez cette option si vous souhaitez envoyer les campagnes de test uniquement aux appareils associés à un seul e-mail ou ID utilisateur.
2. **N’est pas égal à** : exclut un e-mail ou un ID utilisateur particulier des campagnes de test.
3. **Correspond** : trouve les utilisateurs qui ont des adresses e-mail ou des ID d’utilisateur qui correspondent à une partie du terme que vous fournissez. Vous pouvez l’utiliser pour trouver uniquement les utilisateurs disposant d’une adresse « @votresociété.com », ce qui vous permet d’envoyer des messages à tous les membres de votre équipe.

Ces filtres peuvent également être utilisés conjointement pour limiter votre liste d’utilisateurs de test. Par exemple, le segment d’essai peut inclure un filtre d’adresse e-mail qui `matches` à « @braze.com » et un autre filtre qui `does not equal` à « sales@braze.com ». Vous pouvez également sélectionner plusieurs e-mails spécifiques en utilisant l’option `matches` et en séparant les adresses e-mail avec un caractère « \| » (p. ex., `matches` « email1@braze.com\|email2@braze.com »).

Après avoir ajouté les filtres de test à votre segment d’essai, vérifiez que vous n’avez sélectionné que les utilisateurs désirés en cliquant sur **Aperçu** en haut de l’éditeur de segments ou en exportant les données utilisateur de ce segment en CSV. Pour exporter des données utilisateur du segment, cliquez sur la liste déroulante **Données utilisateur** et sélectionnez **Exporter toutes les données utilisateur en CSV**.

![Vérifier le segment d’essai]({% image_buster /assets/img_archive/testmessages3.png %})

> L’exportation des données utilisateur du segment en CSV vous donnera l’image la plus précise de ceux qui dont partie de ce segment. L’onglet **Aperçu** n’affiche qu’un échantillon des utilisateurs dans le segment et peut donc sembler ne pas avoir sélectionné tous les membres prévus. Pour plus d’informations, consultez [Afficher et comprendre les données du segment][7].

Une fois que vous avez confirmé que vous ne ciblez que les utilisateurs qui doivent recevoir le message de test, vous pouvez soit sélectionner ce segment dans une campagne existante que vous souhaitez tester, soit cliquer sur le bouton **Démarrer la campagne** dans le menu du segment.

##### Étape 2 : Envoyer une campagne de test

Pour envoyer des tests de cartes de fil d’actualité, vous devez cibler votre segment d’essai précédemment créé. Commencez par créer une campagne multicanale et suivez les étapes habituelles. Lorsque vous atteignez l’étape **Utilisateurs cibles**, sélectionnez votre segment d’essai comme illustré sur l’image suivante.

![Segment d’essai]({% image_buster /assets/img_archive/test_segment.png %})

Achevez de confirmer votre campagne et lancez-la pour tester vos cartes de fil d’actualité.

>  Assurez-vous de cocher la case intitulée « Autoriser les utilisateurs à devenir rééligibles pour recevoir la campagne » dans la partie **Planification** de l’assistant de campagne si vous avez l’intention d’utiliser une campagne unique pour vous envoyer un message de test à plusieurs reprises.

{% endtab %}
{% endtabs %}

## Campagne personnalisée avec attributs utilisateur

Si vous utilisez la [personnalisation][26] dans votre message, vous devrez prendre des mesures supplémentaires pour prévisualiser correctement votre campagne et vérifier que les données utilisateur sont correctement renseignées.

Lorsque vous envoyez un message de test, assurez-vous de choisir soit l’option **Sélectionner un utilisateur existant** ou aperçu en tant que **Utilisateur personnalisé**.

![Tester un message personnalisé][23]{: style="max-width:70%;" }

Si vous sélectionnez un utilisateur existant, saisissez l’ID utilisateur ou l’e-mail de l’utilisateur spécifique dans le champ de recherche. Utilisez ensuite l’aperçu du tableau de bord pour voir comment votre message s’affiche à cet utilisateur et envoyer un message test à votre appareil qui reflète ce que l’utilisateur verra.

![Sélectionner un utilisateur][24]

Si vous prévisualisez en tant qu’utilisateur personnalisé, saisissez du texte pour différents champs disponibles à la personnalisation, comme le prénom de l’utilisateur et les attributs personnalisés. Une fois encore, vous pouvez saisir votre propre adresse e-mail pour envoyer un test à votre appareil.

![Utilisateur personnalisé][25]

## Campagne personnalisée avec des propriétés de l’événement personnalisées

Tester les campagnes [personnalisées][20] avec [propriétés de l’événement personnalisées][19] diffère légèrement du test des autres types de campagnes décrites. La façon la plus robuste de tester les campagnes personnalisées à l’aide des propriétés de l’événement personnalisées est de déclencher vous-même la campagne. Commencez par écrire le texte impliquant la propriété de l’événement :

![Composer un message de test avec des propriétés][15]

Puis utilisez la [livraison par événement][21] pour envoyer la campagne lorsque l’événement se produit. 

{% alert note %}
Si vous testez une campagne de notification push iOS, vous devez régler le délai à 1 minute pour vous laisser le temps de quitter l’application car iOS n’envoie pas de notifications push à une application actuellement ouverte. D’autres types de campagnes peuvent être définis pour être envoyés immédiatement.
{% endalert %}

![Tester la livraison d’un message][16]

Ciblez les utilisateurs comme vous le feriez pour tester à l’aide d’un filtre de test ou en ciblant votre propre adresse e-mail et terminez la création de la campagne.

![Tester le ciblage d’un message][17]

Accédez à votre application et finalisez l’événement personnalisé. La campagne se déclenchera, et vous devriez voir le message personnalisé avec la propriété de l’événement :

![Tester l’exemple de message][18]

Sinon, si vous enregistrez des ID utilisateur personnalisés, vous pouvez également tester la campagne en envoyant un message de test personnalisé à vous-même. Après avoir écrit le texte de votre campagne, sélectionnez l’onglet **Test** et choisissez **Customized User (Utilisateur personnalisé)**. Ajoutez la propriété de l’événement personnalisée au bas de la page, ajoutez votre ID utilisateur ou votre adresse e-mail à la boîte supérieure, puis cliquez sur **Send Test (Envoyer un test)**. Vous devriez recevoir un message personnalisé avec la propriété.

![Tester en utilisant un utilisateur personnalisé][22]

[7]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#user-preview
[13]: {% image_buster /assets/img_archive/test-push-for-in-app.png %}
[15]: {% image_buster /assets/img_archive/testeventproperties-compose.png %}
[16]: {% image_buster /assets/img_archive/testeventproperties-delivery.png %}
[17]: {% image_buster /assets/img_archive/testeventproperties-target.png %}
[18]: {% image_buster /assets/img_archive/testeventproperties-message.PNG %}
[19]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/#custom-event-properties
[20]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/personalized_messaging/#personalized-messaging
[21]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/
[22]: {% image_buster /assets/img_archive/testeventproperties-customuser.png %}
[23]: {% image_buster /assets/img_archive/personalized_testing.png %}
[24]: {% image_buster /assets/img_archive/personalized_testing_select.png %}
[25]: {% image_buster /assets/img_archive/personalized_testing_custom.png %}
[26]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/overview/