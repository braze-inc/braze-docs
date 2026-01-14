---
nav_title: Intégration
article_title: "Aperçu de l'intégration de l'onboarding"
page_order: 8
page_type: reference
description: "Cet article de référence couvre brièvement les étapes d'intégration requises de la part de vos ingénieurs ou développeurs."

---

# Intégration

> L'intégration avec Braze est un processus qui en vaut la peine. Mais vous êtes intelligent. Vous êtes **ici**. Il est clair que vous le savez déjà. Mais ce que vous ne savez probablement pas, c'est que vous et vos développeurs êtes sur le point d'entreprendre ensemble un voyage qui nécessite une expertise technique, une planification stratégique et une communication cohérente qui vous aidera à coordonner les deux.

{% alert note %}
Notez que le contenu de cet article ne s'applique pas à l'e-mail. Vérifiez cela dans la section [Configuration de l'e-mail.]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/) 
{% endalert %}

## La côte technique du processus d'intégration

Vous vous dites peut-être : "Mes développeurs sont magiques ! Ils peuvent faire n'importe quoi, alors je les laisse faire !" Et c'est probablement le cas, et c'est probablement possible ! Mais il n'y a aucune raison pour que vous ne sachiez pas ce qu'ils font en coulisses. En fait, cela faciliterait l'ensemble du processus si vous saviez quand intervenir avec des informations et ce qu'il faut rechercher lorsqu'ils disent : "Pouvez-vous m'envoyer la clé API et l'endpoint de l'API ?"

Alors, que font-ils lorsqu'ils intègrent Braze à votre application ou à votre site ? Heureux que vous ayez posé la question !

### Étape 1 : Ils mettent en œuvre le SDK de Braze

Le SDK (kit de développement logiciel) de Braze est la façon dont nous envoyons et obtenons des informations vers et depuis votre appli ou votre site. Vos ingénieurs sont essentiellement les garants de la cohérence de nos applications. Pour ce faire, ils ont besoin de quelques informations clés :

* Vos [clés API]({{site.baseurl}}/api/api_key/)
* Votre [endpoint SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/)
  * Braze ne fournit plus d'endpoints personnalisés, utilisez donc les endpoints prédéfinis du SDK. Si vous avez reçu un endpoint personnalisé préexistant, vous trouverez ici les étapes de configuration nécessaires pour l'intégration [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-5-optional-custom-endpoint-setup), [iOS]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) et [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#initializing-the-sdk).

Vous pouvez soit leur communiquer directement ces informations, soit leur donner accès à Braze en leur créant un compte. 

{% alert warning %}
Veillez à ce que vous et vos développeurs ne modifiez pas, sans le savoir ou sans le vouloir, les informations d'identification de l'entreprise dans Braze, car cela pourrait causer des problèmes au cours du processus de mise en œuvre ou bloquer un ou plusieurs d'entre vous hors de leurs comptes.
{% endalert %}

### Étape 2 : Ils mettent en œuvre les canaux d'envoi de messages que vous souhaitez.

Braze propose de nombreuses options pour entrer en contact avec vos utilisateurs, et chacune d'entre elles nécessite sa propre configuration pour fonctionner comme vous le souhaitez. C'est là que la communication avec vos ingénieurs devient essentielle.

Veillez à indiquer à vos développeurs les canaux que vous souhaitez utiliser afin de garantir une mise en œuvre efficace et dans le bon ordre.

| Chaîne | Détails |
|---|---|
| Messages in-app | Nécessite la mise en œuvre du SDK ainsi que ces étapes spécifiques au canal. |
| Pousser | La mise en œuvre du SDK doit permettre de gérer correctement les informations d'identification des messages et les jetons de poussée. |
| e-mail | Il s'agit d'un processus totalement différent. Consultez la section [Configuration de l'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/) pour plus de détails sur l'intégration. |
| Cartes de contenu | Pour commencer à utiliser les [cartes de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/), contactez votre gestionnaire satisfaction client Braze. |
| SMS & MMS | Consultez la section [Configuration du SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/sms/sms_setup/sms_sending/) pour plus de détails sur l'intégration. |
| Webhooks | Nécessite la mise en œuvre du SDK ainsi que des étapes spécifiques à chaque canal. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Vous pouvez utiliser Braze pour créer des campagnes d'envoi de messages accessibles sur chaque canal. Travaillez avec vos développeurs pour vous assurer que vous respectez les normes d'accessibilité dans votre mise en œuvre.
{% endalert %}

### Étape 3 : Ils mettent en place vos données

Braze n'a pas qu'une seule corde à son arc. Il ne s'agit pas seulement d'envoyer des e-mails ou de faire du push. Il s'agit de créer des parcours clients personnalisés et uniques pour chaque utilisateur et chaque client. Les parcours clients sont basés sur leurs actions au sein de votre application ou de votre site, et c'est à vous de les définir ! La tâche suivante de vos développeurs consiste à s'assurer que les actions effectuées au sein de votre app ou de votre site sont reprises par Braze.

Que devez-vous donc faire pour leur transmettre ces informations ?

1. Travaillez avec votre équipe marketing pour définir les campagnes, les objectifs, les attributs et les événements dont vous devez assurer le suivi. Définissez ces cas d'utilisation et partagez-les avec vos équipes.
2. Définissez vos besoins en données personnalisées[(attributs personnalisés]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/), [événements personnalisés]({{site.baseurl}}/user_guide/data/custom_data/custom_events/), etc.).
3. À partir de là, discutez de la manière dont ces données doivent être suivies (déclenchées par le SDK, etc.).
4. Définissez le nombre d'[espaces de travail]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/) dont vous avez besoin. Vos ingénieurs devront savoir comment [tester et configurer]({{site.baseurl}}/user_guide/getting_started/workspaces/) ces espaces de travail.

Une fois que vous avez découvert toutes ces informations, partagez-les avec votre ingénieur. Ils prendront ces informations et mettront en œuvre vos [données personnalisées]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/). Il se peut même que vous deviez [importer certains utilisateurs]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/). Vous devez également connaître les [conventions de dénomination des événements]({{site.baseurl}}/user_guide/data/custom_data/event_naming_conventions/).

### Étape 4 : Ils sont personnalisés en fonction de ce que vous souhaitez.

Si vous voulez des choses comme le lancement déclenché par l'API et le contenu connecté, discutez-en avec votre contact Braze et vos développeurs pour vous assurer que vous serez en mesure d'intégrer dans vos messages des données qui vivent en dehors de votre application et de Braze.

### Étape 5 : Vous assurez tous deux l'assurance qualité de votre mise en œuvre

Travaillez avec votre ingénieur pour vous assurer que tout fonctionne. Envoyez des [messages de test]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages/), utilisez nos [applications de test pour Android]({{site.baseurl}}/developer_guide/references/?tab=android) et nos [applications de test pour iOS]({{site.baseurl}}/developer_guide/references/?tab=swift), vérifiez chaque case avant de commencer l'envoi !

Nous avons même des instructions spécifiques pour [tester votre intégration Android ou FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/test_your_basic_integration/#test-your-basic-integration) et tester le [push pour iOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/testing/).

## Après la mise en œuvre

Gardez à l'esprit que la ligne d'arrivée de la mise en œuvre n'est pas le feu vert pour envoyer un million de messages à la fois. Envoyer un million de push risque de casser votre appli si chaque client clique simultanément sur le même lien. Nous vous recommandons de discuter de la capacité de votre configuration interne à traiter les demandes de Braze avant de cliquer sur le bouton " **Envoyer".**  Vous pouvez ensuite fixer votre [limite de débit sur]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting) cette base.

\![]({% image_buster/assets/img/torchie/firebrands.png %}){: style="max-width:15%;float:right;margin-left:15px;border:none;"}

Une fois que vous serez à l'aise avec Braze, envisagez de devenir un "Firebrand" de Braze ! Avec Braze Firebrands, notre communauté d'engagement client, nous créons une communauté de personnes influentes qui utilisent Braze pour moderniser leur expérience client et leur marketing. Vous souhaitez en savoir plus ? [Rejoignez-nous](https://brazefirebrands.splashthat.com/).
