---
nav_title: Intégration
article_title: Aperçu de l’onboarding d’intégration
page_order: 1
page_type: reference
description: "Le présent article de référence couvre brièvement les étapes d’intégration dont vos ingénieurs ou développeurs ont besoin."

---

# Intégration

> L’intégration avec Braze est un processus de qui en vaut la peine. Mais vous êtes malin. Vous êtes **ici**. Clairement vous le savez déjà. Mais ce que vous ne savez probablement pas, c’est que vous et vos développeurs êtes sur le point de vous lancer ensemble, dans une expertise technique, une planification stratégique et une communication cohérente qui vous aideront à coordonner entre les deux !

{% alert note %} Veuillez noter que le contenu du présent article ne s’applique pas aux e-mails. Consultez le [Guide de configuration des e-mails]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/).{% endalert %}

## Le côté technique du processus d’intégration

Vous pourriez penser « Mes développeurs sont magiques ! » Ils peuvent faire quoi que ce soit, donc je les laisse faire ! » Et c’est certainement vrai ! Mais, il n’y a pas de raison pour laquelle vous ne devriez pas savoir ce qu’ils font. En fait, cela aiderait l’ensemble du processus si vous saviez quand apporter des informations et ce qu’il faut rechercher lorsqu’ils disent « Pouvez-vous m’envoyer la clé API et l’endpoint API ? »."

Qu’est-ce qu’ils font lorsqu’ils intègrent Braze avec votre application ou votre site ? Je suis heureux que vous posiez la question !

### Étape 1 : Ils mettent en œuvre le SDK Braze

Le kit de développement de logiciel Braze (Software Development Kit, SDK) est la façon dont nous envoyons et obtenons des informations sur et depuis votre application ou site. Vos ingénieurs, essentiellement, rassemblent nos applications. Pour ce faire, il faut quelques informations clés :

* Vos [Clés API]({{site.baseurl}}/api/api_key/)
* L’URL de votre [endpoint SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/).
  * Braze n’offre plus d’endpoints personnalisés, donc utilisez les critères d’évaluation SDK prédéfinis. Si vous avez reçu un endpoint personnalisé préexistant, vous pouvez trouver ici les étapes de configuration nécessaires pour l’intégration [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-5-optional-custom-endpoint-setup), [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/overview/) et [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#initializing-the-sdk).

Vous pouvez leur donner ces informations directement, ou vous pouvez leur donner accès à Braze en créant un compte pour eux. 

{% alert warning %}
Assurez-vous que vous et vos développeurs ne changez pas sciemment ou involontairement les identifiants de la société chez Braze, car cela pourrait causer des problèmes au cours du processus de mise en œuvre ou verrouiller un ou plusieurs de vos comptes.
{% endalert %}

### Étape 2 : Ils mettent en œuvre les canaux de messagerie souhaités

Braze a de nombreuses options pour entrer en contact avec vos utilisateurs et chacun nécessite son propre aménagement ou s’adapte au travail comme vous le souhaitez. C’est là que la communication avec vos ingénieurs devient critique.

Assurez-vous de dire à vos développeurs quels canaux vous souhaitez utiliser pour vous assurer que la mise en œuvre est effectuée efficacement et dans le bon ordre.

| Canal | Détails |
|---|---|
| Messages in-app | Nécessite la mise en œuvre du SDK ainsi que les étapes spécifiques à chaque canal. |
| Notification push | Nécessite une mise en œuvre de SDK pour assurer une manipulation adéquate autour des informations d’identification de messagerie et des jetons de notifications push. |
| E-mail | Il s’agit d’un processus entièrement différent. Lisez la section [Email Setup]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/) (Configuration d’e-mail) pour plus de détails sur l’intégration. |
| Cartes de contenu | Pour démarrer avec les [cartes de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/), contactez votre gestionnaire du succès des clients Braze. |
| SMS & MMS | Lisez la section [SMS Setup]({{site.baseurl}}/user_guide/onboarding_with_braze/sms_setup) (Configuration SMS) pour plus de détails sur l’intégration. |
| Webhooks | Nécessite la mise en œuvre du SDK ainsi que des étapes spécifiques à chaque canal. | 
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
Vous pouvez utiliser Braze pour créer des campagnes de communication accessibles sur chaque canal. Vérifiez avec vos développeurs que vous répondez aux normes d’accessibilité lors de la mise en place.
{% endalert %}

### Étape 3 : Ils configurent vos données

Braze a plus d’un tour dans son sac. Il ne s’agit pas seulement d’envoyer des e-mails ou d’envoyer des notifications push. Il s’agit de créer des parcours client personnalisés uniques pour chaque utilisateur et chaque client. Les parcours client reposent sur leurs actions au sein de votre application ou site et vous pouvez les définir. C’est la prochaine tâche de vos développeurs : s’assurer que les actions prises au sein de votre application ou site sont récupérées par Braze.

Que devez-vous faire pour obtenir ces informations ?

1. Travaillez avec votre équipe marketing pour définir les campagnes, les objectifs, les attributs et les événements que vous devez suivre. Définissez ces exemples d’utilisation, partagez-les avec vos équipes.
2. Définissez vos exigences de données personnalisées ([attributs personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/), [événements personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/), etc.).
3. À partir de là, discutez de la manière dont les données doivent être suivies (déclenchées par le SDK, etc.).
4. Définir du nom de [groupe d'apps]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/app_group_management/) dont vous avez besoin. Vos ingénieurs devront savoir comment [tester et configurer]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/) ces groupes d'apps.

Une fois que vous avez découvert toutes ces informations, partagez-les avec votre ingénieur. Il prendra ces informations et mettra en œuvre vos [données personnalisées]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/pre-populating_custom_data/). Vous pourriez même devoir [importer certains utilisateurs]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/). Vous devez également connaître les [conventions de dénomination des événements]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

### Étape 4 : Ils personnalisent en fonction de ce que vous voulez

Si vous souhaitez obtenir des éléments tels que le lancement déclenché par les API et le contenu connecté, discutez avec votre contact Braze et vos développeurs pour vous assurer que vous pourrez obtenir des données qui sortent de votre application et de Braze dans vos messages.

### Étape 5 : Vous faites ensemble l’AQ de votre mise en œuvre

Travaillez avec votre ingénieur pour vous assurer que tout fonctionne. Envoyer des [messages de test]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/), utilisez notre [applications de test pour Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/sample_apps/) et [applications de test pour iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/sample_apps/), vérifiez tout avant de commencer à envoyer !

Nous avons même des instructions spécifiques pour [tester votre intégration Android ou FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/test_your_basic_integration/#test-your-basic-integration) et des tests [de notification push pour iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/testing/).

## Après la mise en œuvre

N’oubliez pas que la ligne d’arrivée de la mise en œuvre n’est pas un feu vert pour envoyer un million de messages en même temps ! Envoyer un million de notifications push peut casser votre application si chaque client clique sur le même lien à la fois -nous vous recommandons de discuter de la capacité de votre installation interne pour traiter les demandes de Braze avant de cliquer sur le bouton **Envoyer**. Ensuite, vous pouvez définir [limitation du taux]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting) sur la base de cela.

Maintenant que vous connaissez le processus d’intégration, consultez [Apprendre à utiliser Braze]({{site.baseurl}}/user_guide/onboarding_with_braze/learning_to_use_braze/) pour des suggestions sur l’endroit où aller ensuite !

![]({% image_buster/assets/img/torchie/firebrands.png %}){: style="max-width:15%;float:right;margin-left:15px;border:none;"}

Lorsque vous êtes l’aise avec Braze, envisagez de devenir une Braze Firebrand ! Avec Braze Firebrands, notre communauté d’engagement client, nous construisons une communauté de personnes engagées utilisant Braze pour moderniser leur expérience client et leur marketing. Vous souhaitez en savoir plus ? [Inscrivez-vous maintenant](https://brazefirebrands.splashthat.com/).