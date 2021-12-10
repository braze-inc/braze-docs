---
nav_title: Envoi de messages de test
article_title: Envoi de messages de test
page_order: 0
tool:
  - Campagnes
page_type: Référence
description: "Cet article de référence décrit comment envoyer des messages de test à travers les différents canaux de Braze et comment incorporer des propriétés d'événements personnalisés ou des attributs utilisateurs."
---

# Envoi de messages de test

> Cet article de référence décrit comment envoyer des messages de test à travers les différents canaux de Braze et comment incorporer des propriétés d'événements personnalisés et des attributs utilisateurs. <br> <br> En testant vos campagnes, vous pouvez vous assurer que tout est correct !

Avant d'envoyer une campagne de messagerie à vos utilisateurs, vous voudrez peut-être le tester pour vous assurer qu'il a l'air correct et qu'il fonctionne de la manière prévue. Vous pouvez créer et envoyer des messages de test pour sélectionner des appareils ou des membres de l'équipe en utilisant les outils du tableau de bord.

{% alert important %}
Assurez-vous de sauvegarder le brouillon de votre campagne après avoir testé pour éviter de supprimer votre campagne. Vous pouvez envoyer des messages de test sans enregistrer le message en tant que brouillon.
{% endalert %}

## Envoi du test spécifique au canal

Pour les étapes pour envoyer des messages de test, reportez-vous à la section pour votre canal ci-dessous.

{% tabs %}
{% tab Email %}

#### Courriel

Après avoir rédigé votre message e-mail, cliquez sur **Aperçu et Tester**. À partir de cette page, sélectionnez l'onglet **test send** et ajoutez votre adresse e-mail ou votre ID d'utilisateur dans le champ **ajouter des utilisateurs individuels**. Lorsque vous êtes prêt, cliquez sur **envoyer le test** pour envoyer votre e-mail brouillé dans votre boîte de réception.

![Test Email]({% image_buster /assets/img_archive/testemail.png %}){: style="largeur-max-40%;" }

{% endtab %}
{% tab Push %}

#### Push mobile

Après avoir rédigé votre push mobile, sélectionnez l'onglet **Paramètres** et ajoutez votre adresse e-mail ou votre identifiant d'utilisateur dans le champ **Ajouter des utilisateurs individuels**. Lorsque vous êtes prêt, cliquez sur **Envoyer le test** pour envoyer votre message brouillé à votre appareil.

![Tester la Push]({% image_buster /assets/img_archive/testpush.png %})

#### Push Web

Après avoir créé votre push web, sélectionnez l'onglet **Paramètres**. Vérifiez **Envoyer le test à moi-même** et cliquez sur **Envoyer le test**.

![Test Web Push]({% image_buster /assets/img_archive/testwebpush.png %})

Si vous avez déjà accepté les messages push du tableau de bord de Braze, vous verrez apparaître le push dans le coin de votre écran. Sinon, cliquez sur **Autoriser** lorsque vous y êtes invité, et le message apparaîtra.

{% endtab %}
{% tab In-App Message %}

#### Message dans l'application

Si vous avez des notifications push configurées dans votre application et sur votre appareil de test, vous pouvez envoyer des messages de test dans l'application à votre application pour voir à quoi il ressemble en temps réel. Après avoir rédigé votre message dans l'application, sélectionnez l'onglet **Testez** et ajoutez votre adresse e-mail ou votre identifiant d'utilisateur au champ **Ajouter des utilisateurs individuels**. Lorsque vous êtes prêt, cliquez sur **Envoyer le test**. Un message de test push apparaîtra en haut de l'écran de votre appareil.

![Tester dans l'application]({% image_buster /assets/img_archive/test-in-app.png %})

En cliquant directement et en ouvrant le message push, vous serez envoyé à votre application, où vous pourrez voir votre test de message dans l'application.

{% endtab %}
{% tab Content Card %}

#### Carte de contenu

Après avoir créé votre Carte de Contenu, vous pouvez envoyer une Carte de Contenu de test à votre application pour voir à quoi elle ressemblera en temps réel. Après avoir rédigé votre carte de contenu, sélectionnez l'onglet __Testez__ et sélectionnez au moins un groupe de test de contenu ou un utilisateur individuel pour recevoir ce message de test.

![Tester la carte de contenu]({% image_buster /assets/img/contentcard_test.png %})

{% endtab %}
{% tab SMS/MMS %}

#### SMS/MMS

Après avoir créé votre message SMS/MMS, vous pouvez envoyer un message de test à votre téléphone pour voir à quoi il ressemblera en temps réel. Après avoir rédigé votre message, sélectionnez l'onglet __Testez__ et sélectionnez au moins un groupe de test de contenu ou un utilisateur individuel pour recevoir ce message de test.

![Tester la carte de contenu]({% image_buster /assets/img/sms_test.png %})

{% endtab %}
{% tab Webhook %}

#### Webhook

Après avoir créé votre webhook, vous pouvez effectuer un test d'envoi pour vérifier la réponse du webhook. Sélectionnez l'onglet __test__ et sélectionnez __envoyer le test__ pour envoyer un test à l'URL du webhook fournie. Vous pouvez également sélectionner un utilisateur individuel pour prévisualiser la réponse en tant qu'utilisateur spécifique.

![Tester la carte de contenu]({% image_buster /assets/img/webhook_test.png %})

{% endtab %}
{% tab News Feed %}

#### Carte de flux d'actualités

L'envoi d'une carte de test News Feed nécessite que vous mettiez en place un segment de test et que vous envoyiez ensuite une campagne de test.

##### Étape 1 : Créer un segment de test désigné

Une fois que vous avez configuré un segment de test, vous pouvez utiliser ces canaux de messagerie. Le processus prend quelques étapes courtes et, s'il est correctement configuré, ne devra être fait qu'une seule fois.

Allez à la page **Segments** et créez un nouveau segment. Dans le menu déroulant sous **Ajouter un filtre**, localisez les filtres de test en bas de la liste.

![Tester les filtres]({% image_buster /assets/img_archive/testmessages1.png %})

Utilisez ces filtres de test pour sélectionner des utilisateurs avec des adresses e-mail spécifiques ou des [identifiants d'utilisateurs externes]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/).

![Options de filtre de test]({% image_buster /assets/img_archive/testmessages2.png %})

Ces filtres ont les options suivantes :

1. **Equals** - Recherche une correspondance exacte de l'e-mail ou de l'identifiant utilisateur que vous fournissez. Utilisez ceci si vous voulez seulement envoyer les campagnes de test à des appareils associés à un seul e-mail ou identifiant d'utilisateur.
2. **Ne correspond pas à** - Utilisez ceci si vous voulez exclure un e-mail ou un identifiant utilisateur particulier des campagnes de test.
3. **Matches** - Trouve les utilisateurs qui ont des adresses e-mail ou des identifiants d'utilisateur qui correspondent à une partie du terme de recherche que vous fournissez. Vous pouvez l'utiliser pour trouver uniquement les utilisateurs avec une adresse "@yourcompany.com", vous permettant d'envoyer des messages à tous les membres de votre équipe.

Ces filtres peuvent également être utilisés en conjonction pour affiner votre liste d'utilisateurs de test. Par exemple, le segment de test pourrait inclure un filtre d'adresse e-mail `correspondant à` "@braze. om" et un autre filtre que `ne correspond pas à` "sales@braze.com". Vous pouvez également sélectionner plusieurs e-mails spécifiques en utilisant l'option `correspond à` et en séparant les adresses e-mail avec un caractère "\|" (e. . `correspond à` "email1@braze.com\|email2@braze.com").

Après avoir ajouté les filtres de test à votre segment de test, vérifiez que vous n'avez sélectionné que les utilisateurs que vous avez voulu en cliquant sur **Aperçu** en haut de l'éditeur de segment ou en exportant les données utilisateur de ce segment vers CSV. Pour exporter les données utilisateur du segment, cliquez sur le menu déroulant **Données utilisateur** et sélectionnez **CSV Exporter toutes les données utilisateur**.

![Vérifier le segment de test]({% image_buster /assets/img_archive/testmessages3.png %})

> Exporter les données utilisateur du segment vers CSV vous donnera l'image la plus précise de qui tombe sous ce segment. L'onglet **Aperçu** n'est qu'un exemple d'utilisateurs dans le segment et peut donc ne pas avoir sélectionné tous les membres prévus. Pour plus d'informations, consultez [Voir et comprendre les données du segment][7].

Une fois que vous avez confirmé que vous ne visez que les utilisateurs que vous souhaitez recevoir le message de test. vous pouvez soit sélectionner ce segment dans une campagne existante que vous voulez tester, soit cliquer sur le bouton **Démarrer la campagne** dans le menu du segment.

##### Étape 2 : Envoyer une campagne de test

Pour envoyer des cartes de test de flux d'actualités, vous devez cibler votre segment de test précédemment créé. Commencez par créer une campagne multicanal et suivez les étapes habituelles. Lorsque vous atteignez l'étape **Utilisateurs cibles** , sélectionnez votre segment de test comme indiqué ci-dessous.

![Groupe de test]({% image_buster /assets/img_archive/test_segment.png %})

Terminez la confirmation de votre campagne et lancez-la pour tester vos cartes de flux d'actualités.

> Assurez-vous de cocher la case intitulée « Autoriser les utilisateurs à redevenir éligibles pour recevoir une campagne » dans la section __Planifier__ de l'assistant de campagne si vous avez l'intention d'utiliser une seule campagne pour vous envoyer un message de test plus d'une fois.

{% endtab %}
{% endtabs %}

## Campagne personnalisée avec les attributs de l'utilisateur

Si vous utilisez [la personnalisation][26] dans votre message, vous devrez prendre des mesures supplémentaires pour prévisualiser correctement votre campagne et vérifier que les données utilisateur sont correctement remplies.

Lors de l'envoi d'un message de test, assurez vous de choisir soit l'option de **Sélectionner l'utilisateur existant** ou de prévisualiser en tant que **Utilisateur Personnalisé**.

!\[Testing a personalized message\]\[23\]{: style="max-width:70%;" }

Si vous sélectionnez un utilisateur existant, entrez l'ID d'utilisateur ou l'email d'un utilisateur de l'application spécifique dans le champ de recherche. Ensuite, utilisez l'aperçu du tableau de bord pour voir comment votre message apparaîtrait à cet utilisateur, et envoyer un message de test à votre appareil qui reflète ce que cet utilisateur verrait.

!\[Sélectionnez un utilisateur\]\[24\]

Si vous prévisualisez en tant qu'utilisateur personnalisé, entrez du texte pour différents champs disponibles pour la personnalisation, tels que le prénom de l'utilisateur et les attributs personnalisés. Une fois de plus, vous pouvez entrer votre propre adresse e-mail pour envoyer un test à votre appareil.

!\[Utilisateur personnalisé\]\[25\]

## Campagne personnalisée avec des propriétés d'événement personnalisées

Le test des campagnes [personnalisées][20] avec [propriétés d'événement personnalisées][19] diffère légèrement du test des autres types de campagnes décrits ci-dessus. La façon la plus robuste de tester des campagnes personnalisées en utilisant des propriétés d'événement personnalisées est de déclencher la campagne vous-même. Commencez par écrire la copie de la propriété de l'événement:

!\[Composing Test Message with Properties\]\[15\]

Ensuite, utilisez [la distribution basée sur l'action][21] pour livrer la campagne lorsque l'événement se produit.

{% alert note %}
Si vous testez une campagne Push iOS, vous devez définir le délai à 1 minute pour vous laisser le temps de quitter l'application car iOS ne délivre pas de notifications push pour l'application actuellement ouverte. D'autres types de campagnes peuvent être configurées pour être livrées immédiatement.
{% endalert %}

!\[Test Message Delivery\]\[16\]

Comme décrit ci-dessus, cibler les utilisateurs comme vous le feriez pour tester soit en utilisant un filtre de test, soit en ciblant votre propre adresse e-mail et en finissant la création de la campagne.

!\[Test Message Targeting\]\[17\]

Allez dans votre application et complétez l'événement personnalisé, et la campagne se déclenchera, et vous devriez voir le message personnalisé avec la propriété de l'événement:

!\[Exemple de message de test\]\[18\]

Alternativement, si vous enregistrez des identifiants d'utilisateur personnalisés, vous pouvez également tester la campagne en vous envoyant un message de test personnalisé. Après avoir écrit la copie de votre campagne, sélectionnez l'onglet **Test** et choisissez **Utilisateur personnalisé**. Ajouter la propriété événement personnalisé en bas de la page, ajoutez votre ID d'utilisateur ou votre adresse e-mail à la case supérieure, et cliquez sur **Envoyer le test**.

Vous devriez recevoir un message personnalisé avec la propriété.

!\[Testing using Customized User\]\[22\]
[13]: {% image_buster /assets/img_archive/test-push-for-in-app.png %} [15]: {% image_buster /assets/img_archive/testeventproperties-compose.png %} [16]: {% image_buster /assets/img_archive/testeventproperties-delivery. ng %} [17]: {% image_buster /assets/img_archive/testeventproperties-target.png %} [18]: {% image_buster /assets/img_archive/testeventproperties-message. NG %} [22]: {% image_buster /assets/img_archive/testeventproperties-customuser.png %} [23]: {% image_buster /assets/img_archive/personalized_testing. ng %} [24]: {% image_buster /assets/img_archive/personalized_testing_select.png %} [25]: {% image_buster /assets/img_archive/personalized_testing_custom.png %}

[7]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/viewing_and_understanding_segment_data/#user-preview
[19]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/#custom-event-properties
[20]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/personalized_messaging/#personalized-messaging
[21]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/
[26]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/overview/