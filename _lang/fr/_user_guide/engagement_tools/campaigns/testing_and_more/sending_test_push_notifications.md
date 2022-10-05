---
nav_title: Envoyer des messages de test
article_title: Envoyer des messages de test
page_order: 0
tool: 
  - Campagnes
page_type: reference
description: "Le présent article de référence explique comment envoyer des messages de test sur les différents canaux de Braze et comment incorporer des propriétés de l’événement personnalisées ou des attributs utilisateur."

---

# Envoyer des messages de test

> Le présent article de référence explique comment envoyer des messages de test sur les différents canaux de Braze et comment incorporer des propriétés de l’événement personnalisées ou des attributs utilisateur. 
> <br>
> <br>
> En testant vos campagnes, vous pouvez vous assurer que tout fonctionne bien !

Avant d’envoyer une campagne de messagerie à vos utilisateurs, vous pouvez la tester pour vous assurer qu’elle semble correcte et fonctionne de la manière prévue. Vous pouvez créer et envoyer des messages de test pour sélectionner des appareils ou des membres de l’équipe à l’aide des outils du tableau de bord.

{% alert important %}
Assurez-vous d’enregistrer le brouillon de votre campagne après l’avoir testée pour éviter de la supprimer. Vous pouvez envoyer des messages de test sans enregistrer le message comme brouillon.
{% endalert %}

## Envoyer un test spécifique à un canal

Pour connaître la procédure d’envoi des messages de test, reportez-vous à la section suivante pour votre canal.

{% tabs %}
{% tab Email %}

#### E-mail

Après avoir rédigé votre e-mail, cliquez sur **Preview and Test** (Aperçu et test). Dans cette page, sélectionnez l’onglet **Test Send** (Tester l’envoi) et ajoutez votre adresse e-mail ou votre ID utilisateur dans le champ **Add Individual Users** (Ajouter des utilisateurs individuels). Lorsque vous êtes prêt, cliquez sur **Send Test** (Envoyer un test) pour envoyer votre e-mail rédigé à votre boîte de réception.

![Test d’e-mail]({% image_buster /assets/img_archive/testemail.png %}){: style="max-width:40%;" }

{% endtab %}
{% tab Push %}

#### Notification push mobile

Après avoir rédigé votre notification push mobile, sélectionnez l’onglet **Settings** (Paramètres) et ajoutez votre adresse e-mail ou votre ID utilisateur dans le champ **Add Individual Users** (Ajouter des utilisateurs individuels). Lorsque vous êtes prêt, cliquez sur **Send Test** (Envoyer un test) pour envoyer votre message rédigé à votre appareil.

![Test de notification push]({% image_buster /assets/img_archive/testpush.png %})

#### Notification push Web

Après avoir créé votre notification push Web, sélectionnez l’onglet **Settings** (Paramètres). Cochez **Send Test to Myself** (Envoyer le test à moi-même) et cliquez sur **Send Test** (Envoyer un test).

![Test de notification push Web]({% image_buster /assets/img_archive/testwebpush.png %})

Si vous avez déjà accepté des messages de notification push depuis le tableau de bord de Braze, vous verrez la notification push dans le coin de votre écran. Sinon, cliquez sur **Allow** (Autoriser) lorsque vous y êtes invité et le message va apparaître.

{% endtab %}
{% tab In-App Message %}

#### Message in-app

Si vous avez les notifications push configurées dans votre application et sur votre appareil de test, vous pouvez envoyer des messages in-app à votre application pour voir à quoi ils ressemblent en temps réel. Après avoir rédigé votre message in-app, sélectionnez l’onglet **Test** (Tester) et ajoutez votre adresse e-mail ou votre ID utilisateur dans le champ **Add Individual Users** (Ajouter des utilisateurs individuels). Lorsque vous êtes prêt, cliquez sur **Send Test** (Envoyer un test). Un message de notification push de test s’affiche en haut de l’écran de votre appareil. 

![Test in-app]({% image_buster /assets/img_archive/test-in-app.png %})

Cliquer directement et ouvrir le message de notification push vous enverra à votre application dans laquelle vous pourrez visualiser votre test de message in-app.

{% endtab %}
{% tab Content Card %}

#### Carte de contenu

Après avoir créé votre carte de contenu, vous pouvez en envoyer une de test à votre application pour voir ce à quoi elle ressemblera en temps réel. Après avoir rédigé votre carte de contenu, sélectionnez l’onglet **Test** (Tester) et sélectionnez au moins un groupe de test de contenu ou un utilisateur individuel pour recevoir ce message de test. 

![Tester une carte de contenu]({% image_buster /assets/img/contentcard_test.png %})

{% endtab %}
{% tab SMS/MMS %}

#### SMS ou MMS

Après avoir créé votre message SMS ou MMS, vous pouvez envoyer un message de test à votre téléphone pour voir ce à quoi il ressemblera en temps réel. Après avoir rédigé votre message, cliquez l’onglet **Test** (Tester) et sélectionnez au moins un groupe de test de contenu ou un utilisateur individuel pour recevoir ce message de test. 

![Tester une carte de contenu]({% image_buster /assets/img/sms_test.png %})

{% endtab %}
{% tab Webhook %}

#### Webhook

Après avoir créé votre webhook, vous pouvez effectuer un envoi de test pour vérifier la réponse du webhook. Sélectionnez l’onglet **Test** (Tester) et sélectionnez **Send Test** (Envoyer un test) pour envoyer un test à l’URL du webhook fourni. Vous pouvez également sélectionner un utilisateur individuel pour prévisualiser la réponse en tant qu’utilisateur spécifique. 

![Tester une carte de contenu]({% image_buster /assets/img/webhook_test.png %})

{% endtab %}
{% tab News Feed %}

#### Carte de fil d’actualité

L’envoi d’un test de carte de fil d’actualité nécessite de configurer un segment d’essai et d’envoyer ensuite une campagne de test.

##### Étape 1 : Créer un segment d’essai spécifié

Une fois que vous avez configuré un segment d’essai, vous pouvez utiliser ces canaux de messagerie. Le processus prend quelques courtes étapes et, s’il est configuré correctement, ne doit être effectué qu’une seule fois.

Allez à la page **Segments** et créez un nouveau segment. Dans le menu déroulant sous **Add Filter** (Ajouter un filtre), localisez les filtres de test au bas de la liste.

![Filtres de test]({% image_buster /assets/img_archive/testmessages1.png %})

Utilisez ces filtres de test pour sélectionner des utilisateurs avec des adresses e-mail spécifiques ou des [ID utilisateur]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/) externes.

![Options de filtre de test]({% image_buster /assets/img_archive/testmessages2.png %})

Ces filtres ont les options suivantes :

1. **Égal** : recherche l’adresse e-mail exacte ou l’ID utilisateur que vous fournissez. Utilisez cette option si vous souhaitez envoyer les campagnes de test uniquement aux appareils associés à un seul e-mail ou ID utilisateur.
2. **N’est pas égal** : utilisez cette option si vous souhaitez exclure un e-mail ou un ID utilisateur particulier des campagnes de test.
3. **Correspond** : trouve les utilisateurs qui ont des adresses e-mail ou des ID d’utilisateur qui correspondent à une partie du terme que vous fournissez. Vous pouvez l’utiliser pour trouver uniquement les utilisateurs disposant d’une adresse « @votresociété.com », ce qui vous permet d’envoyer des messages à tous les membres de votre équipe.

Ces filtres peuvent également être utilisés conjointement pour limiter votre liste d’utilisateurs de test. Par exemple, le segment d’essai peut inclure un filtre d’adresse e-mail qui `matches` à « @braze.com » et un autre filtre qui `does not equal` à « sales@braze.com ». Vous pouvez également sélectionner plusieurs e-mails spécifiques en utilisant l’option `matches` et en séparant les adresses e-mail avec un caractère "\|"(par ex., `matches` "email1@braze.com\|email2@braze.com").

Après avoir ajouté les filtres de test à votre segment d’essai, vérifiez que vous n’avez sélectionné que les utilisateurs désirés en cliquant sur **Preview** (Aperçu) en haut de l’éditeur de segments ou en exportant les données utilisateur de ce segment en CSV. Pour exporter des données utilisateur du segment, cliquez sur la liste déroulante **User Data** (Données utilisateur) et sélectionnez **CSV Export All User Data** (Exporter toutes les données utilisateur en CSV).

![Vérifier le segment d’essai]({% image_buster /assets/img_archive/testmessages3.png %})

> L’exportation des données utilisateur du segment en CSV vous donnera l’image la plus précise de ceux qui dont partie de ce segment. L’onglet **Preview** (Aperçu) n’affiche qu’un échantillon des utilisateurs dans le segment et peut donc sembler ne pas avoir sélectionné tous les membres prévus. Pour plus d’informations, consultez [Afficher et comprendre les données du segment][7].

Une fois que vous avez confirmé que vous ne ciblez que les utilisateurs qui doivent recevoir le message de test, vous pouvez soit sélectionner ce segment dans une campagne existante que vous souhaitez tester, soit cliquer sur le bouton **Start Campaign** (Démarrer la campagne) dans le menu du segment.

##### Étape 2 : Envoyer une campagne de test

Pour envoyer des tests de cartes de fil d’actualité, vous devez cibler votre segment d’essai précédemment créé. Commencez par créer une campagne multicanale et suivez les étapes habituelles. Lorsque vous atteignez l’étape **Target Users** (Utilisateurs cibles), sélectionnez votre segment d’essai comme illustré sur l’image suivante.

![Segment d’essai]({% image_buster /assets/img_archive/test_segment.png %})

Achevez de confirmer votre campagne et lancez-la pour tester vos cartes de fil d’actualité.

>  Assurez-vous de cocher la case intitulée « Autoriser les utilisateurs à devenir rééligibles pour recevoir la campagne » dans la partie **Planification** de l’assistant de campagne si vous avez l’intention d’utiliser une campagne unique pour vous envoyer un message de test à plusieurs reprises.

{% endtab %}
{% endtabs %}

## Campagne personnalisée avec attributs utilisateur

Si vous utilisez la [personnalisation][26] dans votre message, vous devrez prendre des mesures supplémentaires pour prévisualiser correctement votre campagne et vérifier que les données utilisateur sont correctement renseignées.

Lorsque vous envoyez un message de test, assurez-vous de choisir soit l’option **Select Existing User** (Sélectionner un utilisateur existant) ou aperçu en tant que **Custom User** (Utilisateur personnalisé).

![Tester un message personnalisé][23]{: style="max-width:70%;" }

Si vous sélectionnez un utilisateur existant, saisissez l’ID utilisateur ou l’e-mail d’un utilisateur de l’application spécifique dans le champ de recherche. Utilisez ensuite l’aperçu du tableau de bord pour voir comment votre message s’affiche à cet utilisateur et envoyer un message test à votre appareil qui reflète ce que l’utilisateur verra.

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

Accédez à votre application et effectuez l’événement personnalisé et la campagne se déclenchera. Vous devriez voir le message personnalisé avec la propriété de l’événement :

![Tester l’exemple de message][18]

Sinon, si vous enregistrez des ID utilisateur personnalisés, vous pouvez également tester la campagne en envoyant un message de test personnalisé à vous-même. Après avoir écrit le texte de votre campagne, sélectionnez l’onglet **Test** et choisissez **Customized User** (Utilisateur personnalisé). Ajoutez la propriété de l’événement personnalisée au bas de la page, ajoutez votre ID utilisateur ou votre adresse e-mail à la boîte supérieure, puis cliquez sur **Send Test** (Envoyer un test). 

Vous devriez recevoir un message personnalisé avec la propriété.

![Tester en utilisant un utilisateur personnalisé][22]

[7]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/viewing_and_understanding_segment_data/#user-preview
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