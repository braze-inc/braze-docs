---
nav_title: Intégration
article_title: Aperçu de l’intégration en cours
page_order: 1
page_type: Référence
description: "Cet article de référence couvre brièvement les étapes d'intégration requises par vos ingénieurs ou développeurs."
---

# Intégration

L'intégration à Braze est un processus utile. « Mais vous êtes intelligent. » vous êtes __ici__. Évidemment, vous le savez déjà!

Mais ce que vous ne savez probablement pas, c'est que vous et vos ingénieurs ou vos développeurs êtes sur le point de partir ensemble pour un voyage qui nécessite une expertise technique, la planification stratégique et la communication cohérente qui vous aideront à vous coordonner entre les deux!

{% alert note %} Veuillez noter que cela ne compte pas pour l'email. Vérifiez cela dans le [Guide de configuration des e-mails]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/).{% endalert %}

## Le côté technique du processus d'intégration

« Mes ingénieurs sont magiques! » Ils peuvent faire quoi que ce soit, donc je ne leur laisse habituellement que ça!" Et ils le sont probablement et probablement peux! Mais il n'y a aucune raison de ne pas savoir ce qu'ils font en coulisse. En fait, Cela aiderait tout le processus si vous saviez quand vous pouvez entrer avec des informations et quoi chercher quand ils disent "Pouvez-vous m'envoyer la clé API et API Endpoint ?".

"Que font-ils quand ils intègrent Braze à mon application ou à mon site?"

Heureusement que vous avez demandé !

### Étape 1 : Ils implémentent le Braze SDK

Le SDK Braze (Software Development Kit) est la façon dont nous envoyons et obtenons des informations depuis et vers votre application ou votre site. Vos ingénieurs lient essentiellement nos applications ensemble. Pour ce faire, ils ont besoin de quelques informations clés :

* [Les clés API]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/api_settings_tab/)
* [Votre point final]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/)
  * Braze ne donne plus de points de terminaison personnalisés, donc veuillez utiliser les [terminaux SDK prédéfinis]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/). Si vous avez reçu un point de terminaison personnalisé préexistant, vous pouvez trouver ici les étapes de configuration impliquées pour [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-5-optional-custom-endpoint-setup), [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/), et l'intégration [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#initializing-the-sdk).

Vous pouvez soit leur donner cette information directement, soit vous pouvez leur donner accès à Braze en créant un compte pour eux.

{% alert warning %}
Veuillez vous assurer que vous et votre ingénieur ne modifiez pas involontairement ou involontairement les informations d'identification de l'entreprise en Brésil, car cela peut causer des problèmes pendant le processus d'implémentation ou bloquer un ou plusieurs de vous hors de vos comptes.
{% endalert %}

### Étape 2 : Ils implémentent les canaux de messagerie désirés

Braze a de nombreuses options pour entrer en contact avec vos clients/utilisateurs et chacun a besoin de sa propre configuration ou de son propre réglage pour fonctionner comme vous le souhaitez. C'est là que la communication avec vos ingénieurs devient cruciale.

Assurez-vous de dire à vos ingénieurs quels canaux vous voulez utiliser pour vous assurer que l'implémentation est effectuée efficacement et dans le bon ordre.

| Chaîne           | Détails du produit                                                                                                                                                                 |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Messages In-App  | Nécessite l'implémentation du SDK ainsi que ces étapes spécifiques à chaque canal.                                                                                                 |
| Flux d'actualité | Cela fonctionne sur une implémentation correcte et est un SDK nécessaire.                                                                                                          |
| Pousser          | Nécessite une implémentation de SDK pour fournir une gestion adéquate des identifiants de messagerie et des jetons de push.                                                        |
| Courriel         | Il s'agit d'un processus totalement différent. Vérifiez cela dans la section [de notre Configuration des E-mails]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/). |
{: .reset-td-br-1 .reset-td-br-2}

### Étape 3 : Ils configurent vos données

Le Braze n'est pas un poney à une seule astuce. Il ne s'agit pas seulement d'envoyer des e-mails ou d'envoyer des push. Il s'agit de créer des trajets personnalisés qui sont uniques pour chaque utilisateur/client. Les trajets clients sont basés sur leurs actions au sein de votre application ou de votre site et vous pouvez les définir ! Cependant, à quoi sert cette définition si vous ne pouvez pas suivre, enregistrer, compiler et agir sur eux. C'est la prochaine tâche de votre ingénieur - assurez-vous que les actions entreprises dans votre application ou votre site sont ramassées par Braze.

Alors, que faut-il faire pour obtenir ces informations ?

1. Travaillez avec votre équipe de marketing pour définir des campagnes, des objectifs, des attributs et des événements que vous devez suivre. Définissez ces cas d'utilisation, partagez les avec vos équipes.
2. Définissez vos exigences de données personnalisées (attributs, événements, etc.).
3. À partir de là, discutez de la manière dont [ces données doivent être suivies]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) (déclenchées via le SDK, etc.).
4. Définissez le nombre de [Groupes d'Applications]({{site.baseurl}}/user_guide/administrative/app_settings/app_group_management/) dont vous avez besoin. Ils auront besoin de savoir comment [tester et configurer ces éléments]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/).

Une fois que vous avez découvert toutes ces informations, partagez-les avec votre ingénieur. Ils prendront ces informations et mettront en œuvre vos [données personnalisées]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/pre-populating_custom_data/). Vous pourriez même avoir besoin de [importer des utilisateurs]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/). Vous devez également être au courant des [conventions de nommage des événements]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

### Étape 4 : Ils personnalisent en fonction de ce que vous voulez

Si vous voulez des choses comme le lancement de l'API-Triggered et le contenu connecté, discutez de cela avec votre contact Braze et vos ingénieurs pour vous assurer que vous serez en mesure d'obtenir des données qui vivent en dehors de votre application et Braze dans vos messages.

### Étape 5 : Vous êtes tous les deux QA de votre implémentation

Travaillez avec votre ingénieur pour vous assurer que tout fonctionne. Envoyez [messages de test]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_push_notifications/), utilisez nos [applications de test pour Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/sample_apps/) et [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/sample_apps/), cochez chaque case avant de commencer à envoyer !

Nous avons même des instructions spécifiques pour [tester votre intégration Android ou FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/test_your_basic_integration/#test-your-basic-integration) et tester [pousser pour iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/testing/).

## Après l'implémentation

Gardez à l'esprit que la ligne de terminaison d'implémentation n'est pas aussi le feu vert pour envoyer un million de messages en même temps ! Envoyer un million de push pourrait casser votre application si chaque client clique sur le même lien en même temps - nous vous recommandons de discuter de votre capacité de configuration interne pour traiter les demandes de Braze avant de cliquer sur ce bouton _Envoyer_. Ensuite, vous pouvez définir votre [limitation de débit]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting) en fonction de cela.

Maintenant que vous êtes plus familier avec le processus d'intégration, consultez l'article suivant pour [des suggestions sur la direction à suivre]({{site.baseurl}}/user_guide/onboarding_with_braze/learning_to_use_braze/)!

Une fois que vous êtes à l'aise avec Braze, pensez à devenir un Marqueflamme de Braze! Avec Braze Firebrands, notre communauté d'engagement de la clientèle, nous construisons une communauté de déménagements et de shakers qui utilisent Braze pour moderniser l'expérience de leurs clients et le marketing. Vous voulez en apprendre plus? [Rejoignez dès maintenant](https://brazefirebrands.splashthat.com/).
