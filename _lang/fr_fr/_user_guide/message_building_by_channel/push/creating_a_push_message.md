---
nav_title: "Création d'un message push"
article_title: "Création d'une campagne de push"
page_order: 4
page_type: tutorial
description: "Cette page de tutoriel couvre les différents composants impliqués dans la création d'un message Push, y compris la configuration, l'envoi, le ciblage, et plus encore."
channel: push
tool:
  - Campaigns
  
---

# Création d'un message push

> Les notifications push sont idéales pour les appels à l'action urgents, ainsi que pour réengager les utilisateurs qui n'ont pas utilisé l'application depuis un certain temps. Des campagnes push réussies conduisent l'utilisateur directement au contenu et démontrent la valeur de votre appli. Pour voir des exemples de notifications push, consultez nos [études de cas.](https://www.braze.com/customers)

## Étape 1 : Choisissez où créer votre message {#create-new-campaign-push}

{% alert tip %}
Vous ne savez pas s'il faut utiliser une campagne ou un canvas ? Les campagnes sont plus adaptées aux campagnes d'envoi de messages simples et uniques, tandis que les Canevas sont plus adaptés aux parcours utilisateurs en plusieurs étapes.
{% endalert %}

{% tabs %}
{% tab Campaign %}
1. Allez dans **Messagerie** > **Campagnes**, puis sélectionnez **Créer une campagne.**
2. Pour les campagnes ciblant plusieurs canaux, sélectionnez **Multicanal**. Sinon, sélectionnez **Notification push.** Si vous n'êtes toujours pas sûr, reportez-vous à la section **Décider entre une campagne push régulière ou multicanal** ci-dessous.
3. Donnez à votre campagne un nom clair et significatif.
4. Ajoutez des [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) et des [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) si nécessaire. 

{% alert tip %}
Les étiquettes facilitent la recherche de vos campagnes et permettent de créer des rapports. Par exemple, lorsque vous utilisez le [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), vous pouvez filtrer par des étiquettes particulières.
{% endalert %}

{: start="5"}
5\. Ajoutez et nommez autant de variantes que nécessaire pour votre campagne. Vous pouvez choisir des plateformes, des types de messages et des mises en page différents pour chacune de vos variantes ajoutées. Pour en savoir plus sur ce sujet, reportez-vous aux [tests multivariés et aux tests A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% details Deciding between regular or multichannel push campaign %}

Si vous avez l'intention de cibler plusieurs appareils et plateformes, comme toute combinaison de mobile, web, Kindle, iOS et Android, votre sélection à cette étape peut avoir un impact sur la disponibilité de certaines fonctionnalités et paramètres par la suite.

Reportez-vous au tableau de décision suivant avant de créer une campagne multicanal ou de notification push :

\!["Organigramme de sélection du type de campagne. Commencez par décider si vous ciblez plusieurs appareils et plateformes. Dans le cas contraire, vous accédez à l'option "Select Push Notification" (Sélectionner la notification push). Dans l'affirmative, la question suivante est posée : "Quel type d'envoi de messages ?" et les options sont : "Envoi standard", ce qui conduit à un point de décision : "Devez-vous utiliser des paramètres spécifiques à l'appareil ?". Si ce n'est pas le cas, l'écran affiche "Sélectionnez la notification push et utilisez le push rapide". Si c'est le cas, vous passez à la rubrique "Sélectionnez le canal multiple". De retour à " Quel type de message push ? ", si la réponse est " Contenus push ou image Inline ", il oriente vers " Sélectionner multicanale ".]({% image_buster /assets/img_archive/flowchart_quickpush.png %})

Si vous sélectionnez **Notification push** et choisissez de cibler plusieurs appareils et plateformes, vous créez automatiquement une campagne de push rapide. Avec l'appui rapide, certains réglages spécifiques à l'appareil ne sont pas disponibles :

- Boutons d'action push
- Canaux et groupes de notification
- Durée en vie des notifications push (TTL)
- Priorité à l'affichage
- Sons

Avant de continuer, reportez-vous aux [campagnes Quick push]({{site.baseurl}}/quick_push) pour comprendre ce qui est différent pour cette expérience de modification.

{% enddetails %}

{% alert tip %}
Si tous les messages de votre campagne seront similaires ou auront le même contenu, composez votre message avant d'ajouter des variantes supplémentaires. Vous pouvez ensuite choisir **Copier à partir de la variante** dans la liste déroulante **Ajouter une variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}
1. [Créez votre canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) à l'aide du compositeur de canvas.
2. Après avoir configuré votre canvas, ajoutez une étape dans le générateur de canvas. Donnez à votre démarche un nom clair et significatif.
3. Choisissez une [planification des étapes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) et spécifiez un délai si nécessaire.
4. Filtrez votre audience pour cette étape si nécessaire. Vous pouvez encore affiner les destinataires de cette étape en spécifiant des segments et en ajoutant des filtres supplémentaires. Les options d'audience seront vérifiées après le délai au moment de l'envoi des messages.
5. Choisissez votre [comportement en matière d'avancement]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Choisissez les autres canaux de communication que vous souhaitez associer à votre message.

{% endtab %}
{% endtabs %}

## Étape 2 : Sélectionnez les plates-formes de poussée

Ensuite, choisissez la combinaison de plateforme et d'appareil mobile qui doit recevoir le push. Utilisez cette sélection pour limiter la réception/distribution d'une notification push à un ensemble spécifique d'apps.

Il existe plusieurs façons de procéder en fonction de vos sélections antérieures :

| Sélection précédente | Options |
| --- | --- | 
| Campagne de notification push | Sélectionnez une ou plusieurs plateformes et appareils. Si vous choisissez de cibler plusieurs appareils et plateformes, vous créez automatiquement une campagne de push rapide. Vous bénéficiez ainsi d'une expérience de communication optimisée pour l'envoi d'un message pour toutes les plateformes sélectionnées dans un seul et même éditeur. Consultez les [campagnes de push rapide]({{site.baseurl}}/quick_push) pour comprendre ce qui est différent dans cette expérience de modification. |
| Campagne multicanal | Sélectionnez **Ajouter un canal de communication** pour ajouter d'autres plates-formes d'envoi de messages. Les sélections de plateformes étant spécifiques à chaque variante, vous pouvez essayer de tester l'engagement des messages par plateforme.
| Canevas | Dans votre étape Message, sélectionnez **\+ Ajouter plus** pour ajouter des plates-formes de poussée supplémentaires. À l'instar des campagnes multicanal, les sélections de plateformes sont spécifiques à chaque variante. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Étape 3 : Sélectionnez le type de notification (iOS et Android)

Si vous créez une campagne de push rapide, le type de notification est automatiquement défini sur **Push standard** et ne peut pas être modifié.

\![Type de notification avec l'option Standard Push sélectionnée à titre d'exemple.]({% image_buster /assets/img_archive/push_2.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Sinon, pour iOS et Android, sélectionnez votre type de notification :

- Poussée standard
- [Contenus push]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/)
- Image en ligne (Android uniquement)

Si vous souhaitez inclure des images dans votre campagne push, consultez les guides suivants sur la création d'une notification riche pour [iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/) ou [Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/).

## Étape 4 : Composez votre message push

Il est maintenant temps de rédiger votre message d'encouragement ! L'onglet **Composer** vous permet de modifier tous les aspects du contenu et du comportement de votre message.

!onglet Composer de la création d'une notification push.]({% image_buster /assets/img_archive/push_compose.png %})

Le contenu de l'onglet **Composer** varie en fonction du type de notification que vous avez choisi à l'étape précédente, mais il peut inclure l'une des options suivantes :

#### Canal ou groupe de notification (iOS et Android)

Pour plus d'informations sur les options de notification spécifiques à une plateforme, voir [Options de notification iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/) ou [Options de notification Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_options/).

#### Langue

Ajoutez une copie en plusieurs langues à l'aide du bouton **Ajouter des langues**. Nous vous recommandons de sélectionner vos langues avant de rédiger votre contenu afin de pouvoir remplir votre texte à l'endroit voulu dans le Liquid. Pour obtenir la liste complète des langues que vous pouvez utiliser, reportez-vous à la section [Langues prises en charge.]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported)

Si vous ajoutez du texte dans une langue qui s'écrit de droite à gauche, notez que l'aspect final des messages écrits de droite à gauche dépend largement de la manière dont les fournisseurs de services les restituent. Pour connaître les meilleures pratiques en matière d'élaboration de messages de droite à gauche qui s'affichent le plus précisément possible, reportez-vous à la section [Création de messages de droite à gauche.]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/)

#### Titre et corps

{% tabs local %}
{% tab ios %}
Commencez à taper dans la boîte de message et regardez un aperçu apparaître dans la boîte de prévisualisation à gauche. Les messages push doivent être formatés en texte clair. 

Ajoutez un titre en utilisant le champ **Titre**. Pour que votre push soit personnalisé et ciblé, vous pouvez inclure [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/).
{% endtab %}

{% tab android %}
Commencez à taper dans la boîte de message et regardez un aperçu apparaître dans la boîte de prévisualisation à gauche. Les messages push doivent être formatés en texte clair. 

Pour que votre push soit personnalisé et ciblé, vous pouvez inclure [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/).

{% alert important %}
Vous **ne pouvez pas** envoyer un message push Android sans titre. Vous pouvez toutefois saisir un simple espace à la place. Gardez à l'esprit que si votre message ne contient qu'un seul espace, il sera envoyé sous forme de notification push silencieuse. Pour plus d'informations, reportez-vous à la section [Notifications push silencieuses]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android).
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert tip %}
Vous avez besoin d'aide pour créer un texte percutant ? Essayez d'utiliser l'[assistant de rédaction de l'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Saisissez le nom ou la description d'un produit et l'intelligence artificielle générera un texte marketing de type humain à utiliser dans vos messages.

!Lancez le bouton du Copywriter de l'intelligence artificielle, emplacement/localisation du champ Corps du compositeur de push.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_push.png %}){: style="max-width:60%"}
{% endalert %}

#### Image

Lorsqu'elle est prise en charge, l'icône de votre application est automatiquement ajoutée en tant qu'image pour votre notification push. Vous avez également la possibilité d'envoyer des notifications riches, qui permettent de personnaliser davantage vos notifications push en ajoutant du contenu supplémentaire au-delà de la copie.

Pour obtenir des conseils supplémentaires sur l'utilisation d'images dans vos notifications push, consultez les articles suivants :

- [Créez des notifications riches pour iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/)
- [Créez des notifications riches pour Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/)

#### Comportement au clic

Spécifiez ce qui se passe lorsqu'un utilisateur sélectionne le corps d'une notification push avec **On-Click Behavior**. Par exemple, vous pouvez inviter les clients à ouvrir votre application, les rediriger vers une URL Web spécifique ou même ouvrir une page spécifique de votre application à l'aide d'un [lien profond.]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/)

Ici, vous pouvez également configurer des invites sous forme de bouton dans votre notification push, comme par exemple :

- Accepter/Décliner
- Oui/Non
- Confirmer/Annuler
- Plus d'informations 

#### Options d'envoi

Si un utilisateur a installé votre appli sur plusieurs appareils, par défaut, votre message push est envoyé à tous les appareils auxquels un jeton push valide a été attribué. Si vous le souhaitez, vous pouvez sélectionner l'**appareil le plus récemment utilisé.**

!case à cocher des options de l'appareil pour n'envoyer ce push qu'à l'appareil le plus récemment utilisé par l'utilisateur.]({% image_buster /assets/img_archive/push_recent_device.png %}){: style="max-width:70%;" }

Il y a une certaine nuance à apporter à ce paramètre. Si cette option est sélectionnée, Braze limitera les envois multiples, sauf lorsqu'une campagne cible plusieurs plateformes, comme iOS et Android. Si l'utilisateur possède votre application à la fois sur un appareil iOS et un appareil Android, il recevra un push pour les deux plateformes. Si l'appareil le plus récemment utilisé par l'utilisateur n'est pas [équipé de la fonction push]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#foreground-push-enabled), le message ne sera pas envoyé.

Pour iOS, vous pouvez limiter davantage l'envoi de messages en n'envoyant les notifications push qu'aux appareils iPad, ou en ne les envoyant qu'aux appareils iPhone et iPod.

## Étape 5 : Prévisualisez et testez votre message (facultatif)

Le test est sans doute l'une des étapes les plus critiques. Une fois que vous avez fini de composer votre message push parfait, testez-le avant de l'envoyer. Sélectionnez l'onglet **Test** pour choisir parmi les options permettant de tester votre message push. Dans **Destinataires du test**, vous pouvez sélectionner un groupe de test de contenu ou des utilisateurs individuels. Vous pouvez également utiliser l'option **Prévisualiser le message en tant qu'utilisateur** pour avoir une idée de l'affichage de votre message sur mobile pour un utilisateur aléatoire, un utilisateur existant, un utilisateur personnalisé ou un utilisateur multilingue.

## Étape 6 : Créez le reste de votre campagne ou Canvas

{% tabs %}
{% tab Campaign %}

Créez le reste de votre campagne ; consultez les sections suivantes pour plus de détails sur la meilleure façon d'utiliser nos outils pour créer des notifications push.

#### Choisissez la planification ou le déclencheur de la réception/distribution

Les messages push peuvent être envoyés en fonction d'une heure planifiée, d'une action ou d'un déclencheur API. Pour en savoir plus, reportez-vous à la section [Planification de votre campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Pour la réception/distribution par événement, vous pouvez également définir la durée de la campagne et les heures calmes.

C'est également à cette étape que vous pouvez spécifier les contrôles de réception/distribution, par exemple en autorisant les utilisateurs à se [réinscrire]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) pour recevoir la campagne ou en activant les règles de [limite de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Choisissez les utilisateurs à cibler

Ensuite, vous devez [cibler les utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) en choisissant des segments ou des filtres pour réduire votre audience. Vous obtiendrez automatiquement un aperçu de ce à quoi ressemble actuellement cette segmentation approximative de la population. Des statistiques détaillées sur l'audience des canaux ciblés par votre campagne sont disponibles dans le pied de page. Pour connaître le pourcentage de votre base d'utilisateurs qui est ciblé et la valeur vie client de ce segment, sélectionnez **Afficher les statistiques supplémentaires.**

{% multi_lang_include target_audiences.md %}

{% details Why does my Total Reachable Users metric not match the sum of all channels? %}

Lorsque vous affichez le nombre total d'utilisateurs joignables pour votre audience filtrée, vous pouvez remarquer que la somme des colonnes individuelles est inférieure au nombre total d'utilisateurs joignables. Cet écart est généralement dû au fait qu'il y a un certain nombre d'utilisateurs qui se qualifient pour le segment ou les filtres de la campagne, mais qui ne sont pas joignables par push (par exemple, parce qu'ils n'ont pas de [jetons push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens) valides ou actifs).

{% enddetails %}

!Tableau des statistiques d'audience détaillées pour les utilisateurs joignables.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

N'oubliez pas que l'appartenance exacte à un segment est toujours calculée juste avant l'envoi du message.

Vous pouvez également choisir de n'envoyer votre campagne qu'aux utilisateurs qui ont un [statut d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) spécifique, par exemple ceux qui sont abonnés et ont opté pour le push.

Vous pouvez également limiter la réception/distribution à un nombre déterminé d'utilisateurs au sein du segment, ou permettre aux utilisateurs de recevoir le même message deux fois lors d'une répétition de la campagne.

##### Campagnes multicanal avec e-mail et push

Pour les campagnes multicanal ciblant à la fois l'e-mail et les canaux push, vous pouvez limiter votre campagne de manière à ce que seuls les utilisateurs ayant explicitement opté pour le message le reçoivent (à l'exclusion des utilisateurs abonnés ou désabonnés). Par exemple, supposons que vous ayez trois utilisateurs ayant des statuts d'abonnement différents :

- L'**utilisateur A** est abonné à l'e-mail et dispose de la fonction "push". Cet utilisateur ne reçoit pas l'e-mail mais recevra le push.
- L'**utilisateur B** est abonné à l'e-mail mais n'est pas autorisé à utiliser la fonction "push". Cet utilisateur recevra l'e-mail mais ne recevra pas le push.
- L'**utilisateur C** est abonné à l'e-mail et dispose de la fonction "push". Cet utilisateur recevra à la fois l'e-mail et le push.

Pour ce faire, sous **Résumé de l'audience**, sélectionnez d'envoyer cette campagne aux "utilisateurs ayant opté pour l'abonnement uniquement". Cette option garantira que seuls les utilisateurs ayant opté pour l'option recevront votre e-mail, et Braze n'enverra votre push qu'aux utilisateurs dont le push est activé par défaut.

{% alert important %}
Avec cette configuration, n'incluez pas de filtres dans l'étape **Audiences cibles** qui limitent l'audience à un seul canal (par exemple, `Foreground Push Enabled = True` ou `Email Subscription = Opted-In`).
{% endalert %}

#### Choisissez des événements de conversion

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, des [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), après avoir reçu une campagne. Vous avez la possibilité d'autoriser une fenêtre de 30 jours maximum pendant laquelle une conversion sera comptabilisée si l'utilisateur effectue l'action spécifiée.

{% endtab %}

{% tab Canvas %}

Si vous ne l'avez pas encore fait, complétez les sections restantes de votre composante Canvas. Pour plus de détails sur la manière de créer le reste de votre Canvas, de mettre en œuvre les tests multivariés et la sélection intelligente, et plus encore, reportez-vous à l'étape [Créer votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de notre documentation sur le Canvas.

{% endtab %}
{% endtabs %}

## Étape 7 : Examiner et déployer {#review-and-deploy-push}

Une fois que vous avez fini de créer la dernière partie de votre campagne ou de votre Canvas, passez en revue ses détails. Pour les campagnes, la dernière page vous donnera un résumé de la campagne que vous venez de concevoir. Confirmez tous les détails pertinents, assurez-vous d'avoir testé votre message, puis envoyez-le et regardez les données affluer !

Ensuite, consultez les [rapports de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_reporting/) pour savoir comment vous pouvez accéder aux résultats de votre campagne de push. Pour les notifications push, vous pourrez consulter les statistiques relatives au nombre de messages envoyés, délivrés, ayant fait l'objet d'un rebond, ouverts et directement ouverts.

