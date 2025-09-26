---
nav_title: "Création d’un message de notification push"
article_title: Créer une campagne de notification push
page_order: 4
page_type: tutorial
description: "Cette page de didacticiel couvre les différents composants impliqués dans la création d’un message de notification push, y compris la configuration, l’envoi, le ciblage, etc."
channel: push
tool:
  - Campaigns
  
---

# Créer un message de notification push

> Les notifications push sont idéales pour les appels à l’action urgents, ainsi que pour le ré-engagement des utilisateurs qui n’ont pas utilisé l’application depuis un certain temps. Les campagnes de notifications push réussies amènent l’utilisateur directement au contenu et démontrent la valeur de votre application. Pour voir des exemples de notifications push, consultez nos [études de cas.](https://www.braze.com/customers)

## Étape 1 : Choisir où créer votre message {#create-new-campaign-push}

{% alert tip %}
Vous ne savez pas s'il faut utiliser une campagne ou un canvas ? Les campagnes sont plus adaptées aux campagnes d'envoi de messages simples et uniques, tandis que les Canevas sont plus adaptés aux parcours utilisateurs en plusieurs étapes.
{% endalert %}

{% tabs %}
{% tab Campagne %}
1. Allez dans **Messagerie** > **Campagnes**, puis sélectionnez **Créer une campagne.**
2. Pour les campagnes ciblant plusieurs canaux, sélectionnez **Multicanal**. Sinon, sélectionnez **Notification push.** Si vous n'êtes toujours pas sûr, reportez-vous à la section **Décider entre une campagne push régulière ou multicanal** ci-dessous.
3. Donnez un nom clair et significatif à votre campagne.
4. Ajoutez des [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) et des [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) si nécessaire. 

{% alert tip %}
Les balises facilitent la recherche et l’identification des campagnes, et la création de rapports. Par exemple, lorsque vous utilisez le [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), vous pouvez filtrer les éléments en fonction de certaines étiquettes spécifiques.
{% endalert %}

{: start="5"}
5\. Ajoutez et nommez autant de variantes que nécessaire pour votre campagne. Vous pouvez choisir différentes plates-formes, types de messages et mises en page pour chacune de vos variantes ajoutées. Pour plus d'informations sur ce sujet, consultez [Tests multivariés et A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% details Décider entre une campagne de notifications push ordinaire ou multicanale %}

Si vous avez l'intention de cibler plusieurs appareils et plateformes, comme toute combinaison de mobile, web, Kindle, iOS et Android, votre sélection à cette étape peut avoir un impact sur la disponibilité de certaines fonctionnalités et paramètres par la suite.

Reportez-vous au tableau de décision suivant avant de créer une campagne multicanal ou de notification push :

!["Organigramme pour la sélection du type de campagne". Commencez par déterminer si vous ciblez plusieurs appareils et plateformes. Si ce n’est pas le cas, vous accédez à l'option « Sélectionner Notifications push ». Dans l'affirmative, la question suivante est posée : « Quel type de notifications push ? » et les options sont « Notification push standard », ce qui conduit à un point de décision « Devez-vous utiliser des paramètres spécifiques à l'appareil ? » Si ce n'est pas le cas, cela mène à « Sélectionner la notification push et utiliser la notification push rapide ». Si c'est le cas, vous passez à « Sélectionner Multicanale ». Revenons à « Quel type de notifications push ? », si la réponse est « Contenu push ou image insérée », cela mène à « Sélectionner Multicanale ».]({% image_buster /assets/img_archive/flowchart_quickpush.png %})

Si vous sélectionnez **Notification push** et choisissez de cibler plusieurs appareils et plateformes, vous créez automatiquement une campagne de push rapide. Avec l'appui rapide, certains réglages spécifiques à l'appareil ne sont pas disponibles :

- Boutons d'action push
- Canaux et groupes de notification
- Durée en vie des notifications push (TTL)
- Priorité à l'affichage
- Sons

Avant de continuer, reportez-vous aux [campagnes Quick push]({{site.baseurl}}/quick_push) pour comprendre ce qui est différent pour cette expérience de modification.

{% enddetails %}

{% alert tip %}
Si tous les messages de votre campagne vont être similaires ou avoir le même contenu, composez votre message avant d’ajouter des variantes supplémentaires. Vous pouvez ensuite choisir **Copier à partir de la variante** dans la liste déroulante **Ajouter une variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}
1. [Créez votre canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) à l'aide du compositeur de canvas.
2. Après avoir configuré votre Canvas, ajoutez une étape dans le Créateur de Canvas. Donnez un nom clair et significatif à votre étape.
3. Choisissez un [calendrier par étapes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) et spécifiez un délai si nécessaire.
4. Filtrez votre audience pour cette étape si nécessaire. Vous pouvez affiner davantage les destinataires de cette étape en spécifiant des segments et en ajoutant des filtres supplémentaires. Les options d’audience seront vérifiées après le délai au moment de l’envoi des messages.
5. Choisissez votre [comportement d'avancement]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Choisissez les autres canaux de communication que vous souhaitez associer à votre message.

{% endtab %}
{% endtabs %}

## Étape 2 : Sélectionnez les plates-formes de poussée

Ensuite, choisissez la combinaison de plateforme et d'appareil mobile qui doit recevoir le push. Utilisez cette sélection pour limiter la transmission d’une notification push à un ensemble d’applications spécifiques.

Il existe plusieurs façons de procéder en fonction de vos sélections précédentes :

| Sélection précédente | Options |
| --- | --- | 
| Campagne de notification push | Sélectionnez une ou plusieurs plateformes et appareils. Si vous choisissez de cibler plusieurs appareils et plateformes, vous créez automatiquement une campagne de notification push rapide. Vous bénéficiez ainsi d'une expérience de communication optimisée pour l'envoi d'un message pour toutes les plateformes sélectionnées dans un seul et même éditeur. Consultez les [campagnes de push rapide]({{site.baseurl}}/quick_push) pour comprendre ce qui est différent dans cette expérience de modification. |
| Campagne multicanal | Sélectionnez **Ajouter un canal de communication** pour ajouter d'autres plates-formes d'envoi de messages. Les sélections de plateformes étant spécifiques à chaque variante, vous pouvez essayer de tester l'engagement des messages par plateforme.
| Canvas | Dans votre étape Message, sélectionnez **\+ Ajouter plus** pour ajouter des plates-formes de poussée supplémentaires. À l'instar des campagnes multicanales, les sélections de plateformes sont spécifiques à chaque variante. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Étape 3 : Sélectionner un type de notification (iOS et Android)

Si vous créez une campagne de push rapide, le type de notification est automatiquement défini sur **Push standard** et ne peut pas être modifié.

![Type de notification avec l'option Standard Push sélectionnée à titre d'exemple.]({% image_buster /assets/img_archive/push_2.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Sinon, pour iOS et Android, sélectionnez votre type de notification :

- Notification push standard
- [Contenu push]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/)
- Image en ligne (Android uniquement)

Si vous souhaitez inclure des images dans votre campagne push, consultez les guides suivants sur la création d'une notification riche pour [iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/) ou [Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/).

## Étape 4 : Composer votre message de notification push

Il est maintenant temps d’écrire votre message de notification push ! L'onglet **Composer** vous permet de modifier tous les aspects du contenu et du comportement de votre message.

![Onglet Composer pour la création d'une notification push.]({% image_buster /assets/img_archive/push_compose.png %})

Le contenu de l'onglet **Composer** varie en fonction du type de notification que vous avez choisi à l'étape précédente, mais il peut inclure l'une des options suivantes :

#### Canal ou groupe de notification (iOS et Android)

Pour plus d'informations sur les options de notification spécifiques à une plateforme, voir [Options de notification iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/) ou [Options de notification Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_options/).

#### Langue

Ajoutez un texte en plusieurs langues à l'aide du bouton **Ajouter des langues**. Nous vous recommandons de sélectionner vos langues avant d’écrire votre contenu afin que vous puissiez remplir votre texte dans Liquid. Pour obtenir la liste complète des langues que vous pouvez utiliser, reportez-vous à la section [Langues prises en charge.]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported)

Si vous ajoutez du texte dans une langue qui s'écrit de droite à gauche, notez que l'aspect final des messages écrits de droite à gauche dépend largement de la manière dont les fournisseurs de services les restituent. Pour connaître les meilleures pratiques en matière d'élaboration de messages de droite à gauche qui s'affichent le plus précisément possible, reportez-vous à la section [Création de messages de droite à gauche.]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/)

#### Titre et corps

{% tabs local %}
{% tab ios %}
Commencez à taper dans la boîte de message et voyez un aperçu apparaître dans la fenêtre d’aperçu à gauche. Les messages de notification push doivent être formatés en texte brut. 

Ajoutez un titre en utilisant le champ **Titre**. Pour que votre push soit personnalisé et ciblé, vous pouvez inclure [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/).
{% endtab %}

{% tab android %}
Commencez à taper dans la boîte de message et voyez un aperçu apparaître dans la fenêtre d’aperçu à gauche. Les messages de notification push doivent être formatés en texte brut. 

Pour que votre push soit personnalisé et ciblé, vous pouvez inclure [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/).

{% alert important %}
Vous **ne pouvez pas** envoyer un message push Android sans titre. Vous pouvez toutefois saisir un simple espace à la place. Gardez à l'esprit que si votre message ne contient qu'un seul espace, il sera envoyé sous forme de notification push silencieuse. Pour plus d'informations, reportez-vous à la section [Notifications push silencieuses]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android).
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert tip %}
Besoin d’aide pour créer un texte d’exception ? Essayez d'utiliser l'[assistant de rédaction de l'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Saisissez un nom ou une description du produit et l’IA générera un texte marketing semblant d’origine humaine pour une utilisation dans votre envoi de messages.

![Bouton Lancer le rédacteur IA situé dans le champ Corps du composeur de notification push.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_push.png %}){: style="max-width:60%"}
{% endalert %}

#### Image

Lorsque cela est possible, l’icône de votre application est automatiquement ajoutée en tant qu’image pour votre notification push. Vous avez également la possibilité d’envoyer des notifications enrichies, ce qui permet d’obtenir plus de personnalisation dans vos notifications push en ajoutant du contenu supplémentaire en plus du texte.

Pour plus d’informations sur l’utilisation des images dans vos notifications push, reportez-vous aux articles suivants :

- [Créez des notifications riches pour iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/)
- [Créez des notifications riches pour Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/)

#### Comportement lors du clic

Spécifiez ce qui se passe lorsqu'un utilisateur sélectionne le corps d'une notification push avec **On-Click Behavior**. Par exemple, vous pouvez inviter les clients à ouvrir votre application, les rediriger vers une URL Web spécifique ou même ouvrir une page spécifique de votre application à l'aide d'un [lien profond]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/).

Ici, vous pouvez également configurer des boutons d’invites dans votre notification push, comme :

- Accepter/Refuser
- Oui/Non
- Confirmer/Annuler
- Plus 

#### Options d'envoi

Si un utilisateur a installé votre appli sur plusieurs appareils, par défaut, votre message push est envoyé à tous les appareils auxquels un jeton push valide a été attribué. Si vous le souhaitez, vous pouvez sélectionner l'**appareil le plus récemment utilisé.**

![Case à cocher des options de l'appareil pour n'envoyer ce push qu'à l'appareil le plus récemment utilisé par l'utilisateur.]({% image_buster /assets/img_archive/push_recent_device.png %}){: style="max-width:70%;" }

Il y a une certaine nuance à apporter à ce paramètre. Si cette option est sélectionnée, Braze limitera les envois multiples, sauf lorsqu'une campagne cible plusieurs plateformes, comme iOS et Android. Si l'utilisateur possède votre application à la fois sur un appareil iOS et un appareil Android, il recevra un push pour les deux plateformes. Si l'appareil le plus récemment utilisé par l'utilisateur n'est pas [équipé de la fonction push]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-enabled), le message ne sera pas envoyé.

Pour iOS, vous pouvez limiter encore plus les messages en envoyant uniquement des notifications push sur les appareils iPad ou uniquement vers des appareils iPhone et iPod.

## Étape 5 : Prévisualisez et testez votre message (facultatif)

Le test est sans doute l’une des étapes les plus critiques. Après avoir fini de composer votre message de notification push parfait, testez-le avant de l’envoyer. Sélectionnez l'onglet **Test** pour choisir parmi les options permettant de tester votre message push. Dans **Destinataires du test**, vous pouvez sélectionner un groupe de test de contenu ou des utilisateurs individuels. Vous pouvez également utiliser l'option **Prévisualiser le message en tant qu'utilisateur** pour avoir une idée de l'affichage de votre message sur mobile pour un utilisateur aléatoire, un utilisateur existant, un utilisateur personnalisé ou un utilisateur multilingue.

## Étape 6 : Créer le reste de votre campagne ou de votre Canvas

{% tabs %}
{% tab Campagne %}

Créez le reste de votre campagne ; consultez les sections suivantes pour plus de détails sur la meilleure façon d'utiliser nos outils pour créer des notifications push.

#### Choisir un calendrier ou un déclencheur pour la livraison

Les messages de notification push peuvent être livrés sur la base d’une heure planifiée, d’une action ou d’un déclencheur API. Pour en savoir plus, reportez-vous à la section [Planification de votre campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Pour une livraison basée sur l'action, vous pouvez également définir la durée de la campagne et les [Heures de silence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

C'est également à cette étape que vous pouvez spécifier les contrôles de réception/distribution, par exemple en autorisant les utilisateurs à se [réinscrire]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) pour recevoir la campagne ou en activant les règles de [limite de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Choisir les utilisateurs à cibler

Ensuite, vous devez [cibler les utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) en choisissant des segments ou des filtres pour réduire votre audience. Vous recevez automatiquement un aperçu de ce à quoi ressemble la population approximative du segment à ce moment-là. Des statistiques d’audience détaillées pour les canaux ciblés par votre campagne sont disponibles dans le pied de page. Pour connaître le pourcentage de votre base d'utilisateurs qui est ciblé et la valeur vie client de ce segment, sélectionnez **Afficher les statistiques supplémentaires.**

{% details Pourquoi mon indicateur du nombre total d'utilisateurs joignables ne correspond-il pas à la somme de tous les canaux ? %}

Lorsque vous affichez les Total des utilisateurs accessibles pour votre audience filtrée, il est possible que vous constatiez que la somme des colonnes individuelles est plus petite que le Total des utilisateurs accessibles. Cet écart est généralement dû au fait qu'il y a un certain nombre d'utilisateurs qui se qualifient pour le segment ou les filtres de la campagne, mais qui ne sont pas joignables par push (par exemple, parce qu'ils n'ont pas de [jetons push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens) valides ou actifs).

{% enddetails %}

![Tableau des statistiques détaillées sur l'audience pour les utilisateurs atteignables.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

Gardez à l’esprit que l’appartenance à un segment exact est toujours calculée juste avant l’envoi du message.

Vous pouvez également choisir de n'envoyer votre campagne qu'aux utilisateurs qui ont un [statut d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) spécifique, par exemple ceux qui sont abonnés et ont opté pour le push.

Facultativement, vous pouvez également limiter la livraison à un nombre spécifié d’utilisateurs dans le segment, ou permettre aux utilisateurs de recevoir le même message deux fois dans le cadre d’une campagne récurrente.

##### Campagnes multicanales avec e-mail et notification push

Pour les campagnes multicanales avec e-mail et notifications push, vous pouvez limiter votre campagne pour que seuls les utilisateurs ayant explicitement consenti à recevoir des e-mails reçoivent le message (en excluant les utilisateurs abonnés et désabonnés). Par exemple, si vous avez trois utilisateurs avec un statut d’abonnement différent :

- L'**utilisateur A** est abonné à l'e-mail et dispose de la fonction "push". Cet utilisateur ne reçoit pas les e-mails, mais il recevra les notifications push.
- L'**utilisateur B** est abonné à l'e-mail mais n'est pas autorisé à utiliser la fonction "push". Cet utilisateur recevra les e-mails, mais pas les notifications push.
- **Utilisateur C** est abonné aux e-mails et les notifications push sont activées. Cet utilisateur recevra les e-mails et les notifications push.

Pour ce faire, sous **Résumé de l'audience**, sélectionnez d'envoyer cette campagne aux « utilisateurs abonnés uniquement ». Cette option garantira que seuls les utilisateurs abonnés recevront vos e-mails et Braze enverra uniquement vos notifications push aux utilisateurs pour lesquels la notification push est activée par défaut.

{% alert important %}
Avec cette configuration, n'incluez pas de filtres dans l'étape **Audiences cibles** qui limitent l'audience à un seul canal (par exemple, `Push Enabled = True` ou `Email Subscription = Opted-In`).
{% endalert %}

#### Sélectionner des événements de conversion

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, des [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), après avoir reçu une campagne. Vous avez la possibilité d’autoriser une fenêtre allant jusqu’à 30 jours pendant laquelle une conversion sera comptée si l’utilisateur entreprend l’action spécifiée.

{% endtab %}

{% tab Canvas %}

Si vous ne l’avez pas déjà fait, complétez les sections restantes de votre composant de Canvas. Pour plus de détails sur la manière de créer le reste de votre Canvas, de mettre en œuvre les tests multivariés et la sélection intelligente, et plus encore, reportez-vous à l'étape [Créer votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de notre documentation sur le Canvas.

{% endtab %}
{% endtabs %}

## Étape 7 : Revue et déploiement {#review-and-deploy-push}

Après avoir terminé de créer la fin de votre campagne ou de votre Canvas, réexaminez ses détails. Pour les campagnes, la dernière page vous affichera un résumé de la campagne que vous venez de concevoir. Confirmez tous les détails pertinents, assurez-vous d’avoir testé votre message, puis envoyez-le et regardez les données entrer !

Ensuite, consultez les [rapports de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_reporting/) pour savoir comment vous pouvez accéder aux résultats de votre campagne de push. Pour les notifications push, vous pourrez afficher les statistiques du nombre de messages envoyés, livrés, retournés, ouverts et ouverts directement.

