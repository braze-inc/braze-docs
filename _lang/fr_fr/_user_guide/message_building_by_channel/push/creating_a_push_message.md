---
nav_title: Créer un message push
article_title: Créer une campagne push
page_order: 4
page_type: tutorial
description: "Cette page de didacticiel couvre les différents composants impliqués dans la création d'un message de notification push, y compris la configuration, l'envoi, le ciblage, etc."
channel: push
tool:
  - Campaigns
  
---

# Créer un message push

> Les notifications push sont idéales pour les appels à l'action urgents, ainsi que pour le ré-engagement des utilisateurs qui n'ont pas utilisé l'application depuis un certain temps. Les campagnes de notifications push réussies amènent l'utilisateur directement au contenu et démontrent la valeur de votre application. Pour voir des exemples de notifications push, consultez nos [études de cas](https://www.braze.com/customers).

## Étape 1 : Choisir où créer votre message {#create-new-campaign-push}

{% alert tip %}
Vous hésitez entre une campagne et un Canvas ? Les campagnes sont plus adaptées aux campagnes de communication uniques et ciblées, tandis que les Canvas conviennent mieux aux parcours utilisateur en plusieurs étapes.
{% endalert %}

{% tabs %}
{% tab Campaign %}
1. Allez dans **Messagerie** > **Campagnes**, puis sélectionnez **Créer une campagne**.
2. Pour les campagnes ciblant plusieurs canaux, sélectionnez **Multicanal**. Sinon, sélectionnez **Notification push**. Si vous avez encore des doutes, consultez la section **Choisir entre une campagne push classique ou multicanal** ci-dessous.
3. Donnez un nom clair et significatif à votre campagne.
4. Ajoutez des [équipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) et des [étiquettes]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) si nécessaire. 

{% alert tip %} 
Les étiquettes facilitent la recherche et l'identification des campagnes, et la création de rapports. Par exemple, lorsque vous utilisez le [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), vous pouvez filtrer les éléments en fonction de certaines étiquettes spécifiques.
{% endalert %}

{: start="5"}
5. Ajoutez et nommez autant de variantes que nécessaire pour votre campagne. Vous pouvez choisir différentes plateformes, types de messages et mises en page pour chacune de vos variantes. Pour plus d'informations sur ce sujet, consultez [Tests multivariés et A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% details Choisir entre une campagne push classique ou multicanal %}

Si vous avez l'intention de cibler plusieurs appareils et plateformes, comme toute combinaison de mobile, web, Kindle, iOS et Android, votre sélection à cette étape peut avoir un impact sur la disponibilité de certaines fonctionnalités et paramètres par la suite.

Reportez-vous au tableau de décision suivant avant de créer une campagne multicanal ou de notification push :

!["Organigramme pour la sélection du type de campagne. Commencez par déterminer si vous ciblez plusieurs appareils et plateformes. Si ce n'est pas le cas, vous accédez à l'option « Sélectionner Notification push ». Dans l'affirmative, la question suivante est posée : « Quel type de notification push ? » et les options sont « Notification push standard », ce qui conduit à un point de décision « Devez-vous utiliser des paramètres spécifiques à l'appareil ? » Si ce n'est pas le cas, cela mène à « Sélectionner la notification push et utiliser la notification push rapide ». Si c'est le cas, vous passez à « Sélectionner Multicanal ». Pour revenir à la question « Quel type de message push ? », si la réponse est « Contenu push ou Image en ligne », cela redirige vers « Sélectionner Multicanal »."]({% image_buster /assets/img_archive/flowchart_quickpush.png %})

Si vous sélectionnez **Notification push** et choisissez de cibler plusieurs appareils et plateformes, vous créez automatiquement une campagne de push rapide. Avec le push rapide, certains paramètres spécifiques à l'appareil ne sont pas disponibles :

- Boutons d'action push
- Canaux et groupes de notification
- Durée de vie des notifications push (TTL)
- Priorité d'affichage
- Sons

Avant de continuer, consultez les [campagnes de push rapide]({{site.baseurl}}/quick_push) pour comprendre ce qui diffère dans cette expérience de modification.

{% enddetails %}

{% alert tip %}
Si tous les messages de votre campagne vont être similaires ou avoir le même contenu, composez votre message avant d'ajouter des variantes supplémentaires. Vous pouvez ensuite choisir **Copier à partir de la variante** dans la liste déroulante **Ajouter une variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}
1. [Créez votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) à l'aide du compositeur de Canvas.
2. Après avoir configuré votre Canvas, ajoutez une étape dans le générateur de Canvas. Donnez un nom clair et significatif à votre étape.
3. Choisissez une [planification d'étape]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) et spécifiez un délai si nécessaire.
4. Filtrez votre audience pour cette étape si nécessaire. Vous pouvez affiner davantage les destinataires de cette étape en spécifiant des segments et en ajoutant des filtres supplémentaires. Les options d'audience seront vérifiées après le délai, au moment de l'envoi des messages.
5. Choisissez votre [comportement d'avancement]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Choisissez les autres canaux de communication que vous souhaitez associer à votre message.

{% endtab %}
{% endtabs %}

## Étape 2 : Sélectionner les plateformes push

Ensuite, choisissez la combinaison de plateforme et d'appareil mobile qui doit recevoir le push. Utilisez cette sélection pour limiter la distribution d'une notification push à un ensemble d'applications spécifiques.

Il existe plusieurs façons de procéder en fonction de vos sélections précédentes :

| Sélection précédente | Options |
| --- | --- | 
| Campagne de notification push | Sélectionnez une ou plusieurs plateformes et appareils. Si vous choisissez de cibler plusieurs appareils et plateformes, vous créez automatiquement une campagne de push rapide. Vous bénéficiez ainsi d'une expérience de modification optimisée pour rédiger un message pour toutes les plateformes sélectionnées dans un seul éditeur. Consultez les [campagnes de push rapide]({{site.baseurl}}/quick_push) pour comprendre ce qui diffère dans cette expérience de modification. |
| Campagne multicanal | Sélectionnez **Ajouter un canal de communication** pour ajouter des plateformes push supplémentaires. Les sélections de plateformes étant spécifiques à chaque variante, vous pouvez tester l'engagement des messages par plateforme.
| Canvas | Dans l'étape Message, sélectionnez **+ Ajouter** pour ajouter des plateformes push supplémentaires. À l'instar des campagnes multicanales, les sélections de plateformes sont spécifiques à chaque variante. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Étape 3 : Sélectionner un type de notification (iOS et Android)

Si vous créez une campagne de push rapide, le type de notification est automatiquement défini sur **Push standard** et ne peut pas être modifié.

![Type de notification avec l'option Push standard sélectionnée à titre d'exemple.]({% image_buster /assets/img_archive/push_2.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Sinon, pour iOS et Android, sélectionnez votre type de notification :

- Push standard
- [Contenu push]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/)
- Image en ligne (Android uniquement)

Si vous souhaitez inclure des images dans votre campagne push, consultez les guides suivants sur la création d'une notification enrichie pour [iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/) ou [Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/).

## Étape 4 : Composer votre message push

Il est maintenant temps de rédiger votre message push ! L'onglet **Rédiger** vous permet de modifier tous les aspects du contenu et du comportement de votre message.

![Onglet Rédiger de la création d'une notification push.]({% image_buster /assets/img_archive/push_compose.png %})

Le contenu de l'onglet **Rédiger** varie en fonction du type de notification que vous avez choisi à l'étape précédente, mais il peut inclure l'une des options suivantes :

#### Canal ou groupe de notification (iOS et Android)

Pour plus d'informations sur les options de notification spécifiques à une plateforme, consultez [Options de notification iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/) ou [Options de notification Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_options/).

#### Langue

Ajoutez du texte en plusieurs langues à l'aide du bouton **Ajouter des langues**. Nous vous recommandons de sélectionner vos langues avant de rédiger votre contenu afin de pouvoir insérer votre texte aux bons endroits dans Liquid. Pour obtenir la liste complète des langues disponibles, consultez la section [Langues prises en charge]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

Si vous ajoutez du texte dans une langue qui s'écrit de droite à gauche, notez que l'aspect final des messages de droite à gauche dépend largement de la manière dont les fournisseurs de services les restituent. Pour connaître les bonnes pratiques en matière de rédaction de messages de droite à gauche qui s'affichent le plus fidèlement possible, consultez la section [Création de messages de droite à gauche]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

#### Titre et corps

{% tabs local %}
{% tab ios %}
Commencez à saisir du texte dans la zone de message et observez l'aperçu qui apparaît dans la fenêtre de prévisualisation à gauche. Les messages push doivent être formatés en texte brut. 

Ajoutez un titre en utilisant le champ **Titre**. Pour personnaliser et cibler votre push, vous pouvez inclure du [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/).
{% endtab %}

{% tab android %}
Commencez à saisir du texte dans la zone de message et observez l'aperçu qui apparaît dans la fenêtre de prévisualisation à gauche. Les messages push doivent être formatés en texte brut. 

Pour personnaliser et cibler votre push, vous pouvez inclure du [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/).

{% alert important %}
Il **n'est pas possible** d'envoyer un message push Android sans titre. Cependant, vous pouvez saisir un espace à la place. Gardez à l'esprit que si votre message ne contient qu'un seul espace, il sera envoyé sous forme de notification push silencieuse. Pour plus d'informations, consultez la section [Notifications push silencieuses]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android).
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert tip %}
Besoin d'aide pour créer un texte percutant ? Essayez l'[assistant de rédaction IA]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Saisissez un nom ou une description de produit et l'IA générera un texte marketing au ton naturel, prêt à être utilisé dans vos messages.

![Bouton Lancer l'assistant de rédaction IA, situé dans le champ Corps de l'éditeur push.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_push.png %}){: style="max-width:60%"}
{% endalert %}

#### Image

Lorsque cela est possible, l'icône de votre application est automatiquement ajoutée en tant qu'image pour votre notification push. Vous avez également la possibilité d'envoyer des notifications enrichies, qui permettent davantage de personnalisation en ajoutant du contenu supplémentaire au-delà du texte.

Pour plus d'informations sur l'utilisation des images dans vos notifications push, consultez les articles suivants :

- [Créer des notifications enrichies pour iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/)
- [Créer des notifications enrichies pour Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/)

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### Comportement au clic

Précisez ce qui se produit lorsqu'un utilisateur sélectionne le corps d'une notification push à l'aide de l'option **Comportement au clic**. Par exemple, vous pouvez inviter les clients à ouvrir votre application, les rediriger vers une URL web spécifique ou même ouvrir une page spécifique de votre application à l'aide d'un [lien profond]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/).

Vous pouvez également configurer des boutons d'invite dans votre notification push, comme :

- Accepter/Refuser
- Oui/Non
- Confirmer/Annuler
- Plus 

#### Options d'envoi

Si un utilisateur a installé votre application sur plusieurs appareils, par défaut, votre message push est envoyé à tous les appareils auxquels un jeton de notification push valide a été attribué. Si vous le souhaitez, vous pouvez sélectionner **Appareil le plus récemment utilisé**.

![Case à cocher des options d'appareil pour n'envoyer cette notification push qu'à l'appareil le plus récemment utilisé par l'utilisateur.]({% image_buster /assets/img_archive/push_recent_device.png %}){: style="max-width:70%;" }


Par défaut, Braze envoie les messages à chaque appareil de l'utilisateur disposant d'un jeton de notification push valide. Pour iOS, vous pouvez affiner davantage votre portée en choisissant d'envoyer les notifications uniquement aux appareils iPad, ou uniquement aux appareils iPhone et iPod.

Si vous le souhaitez, vous pouvez définir la destination du push sur **Appareil le plus récemment utilisé**. 

##### Appareil le plus récemment utilisé

« Le plus récemment utilisé » est un statut technique, et non comportemental. Comme Braze envoie par défaut à tous les appareils, passer à ce paramètre réduit considérablement votre portée et repose entièrement sur le statut du seul appareil disposant du jeton le plus récent.

![Case à cocher des options d'appareil pour n'envoyer cette notification push qu'à l'appareil le plus récemment utilisé par l'utilisateur.]({% image_buster /assets/img_archive/push_recent_device.png %}){: style="max-width:70%;" }

L'appareil le plus récemment utilisé est déterminé par l'appareil dont le jeton de notification push a été mis à jour le plus récemment, et non par l'appareil ayant eu la session la plus récente. 
* Si le jeton de notification push d'un nouvel appareil est ajouté à un profil utilisateur via l'API, cet appareil est immédiatement considéré comme le plus récemment utilisé, même si l'utilisateur n'a pas encore démarré de session dessus. 
* Si l'appareil le plus récemment utilisé d'un utilisateur n'est pas [activé pour le push]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#foreground-push-enabled), le message ne sera pas envoyé du tout.

Des envois multiples peuvent tout de même se produire si une campagne cible différentes plateformes, comme iOS et Android. Si un utilisateur possède l'application sur les deux, il peut recevoir un push pour chaque plateforme.

Pour iOS, vous pouvez limiter davantage l'envoi en n'envoyant les notifications push qu'aux appareils iPad, ou uniquement aux appareils iPhone et iPod.

## Étape 5 : Prévisualiser et tester votre message (facultatif)

Le test est sans doute l'une des étapes les plus importantes. Après avoir fini de composer votre message push parfait, testez-le avant de l'envoyer. Sélectionnez l'onglet **Test** pour choisir parmi les options de test de votre message push. Dans **Destinataires du test**, vous pouvez sélectionner un groupe de test de contenu ou des utilisateurs individuels. Vous pouvez également utiliser l'option **Prévisualiser le message en tant qu'utilisateur** pour avoir un aperçu de l'affichage de votre message sur mobile pour un utilisateur aléatoire, un utilisateur existant, un utilisateur personnalisé ou un utilisateur multilingue.

## Étape 6 : Créer le reste de votre campagne ou de votre Canvas

{% tabs %}
{% tab Campaign %}

Créez le reste de votre campagne ; consultez les sections suivantes pour plus de détails sur la meilleure façon d'utiliser nos outils pour créer des notifications push.

#### Choisir un calendrier ou un déclencheur de distribution

Les messages push peuvent être distribués selon une heure planifiée, une action ou un déclencheur API. Pour en savoir plus, consultez la section [Planification de votre campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Pour une livraison par événement, vous pouvez également définir la durée de la campagne et les [heures calmes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

C'est également à cette étape que vous pouvez spécifier les contrôles de distribution, par exemple en autorisant les utilisateurs à devenir [rééligibles]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) pour recevoir la campagne ou en activant les règles de [limite de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Choisir les utilisateurs à cibler

Ensuite, vous devez [cibler les utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) en sélectionnant des segments ou des filtres pour restreindre votre audience. Vous recevez automatiquement un aperçu de la taille approximative de la population de ce segment. Des statistiques d'audience détaillées pour les canaux ciblés par votre campagne sont disponibles dans le pied de page. Pour connaître le pourcentage de votre base d'utilisateurs ciblé et la valeur vie client de ce segment, sélectionnez **Afficher les statistiques supplémentaires**.

{% multi_lang_include target_audiences.md %}

{% details Pourquoi mon indicateur Total des utilisateurs accessibles ne correspond-il pas à la somme de tous les canaux ? %}

Lorsque vous consultez le Total des utilisateurs accessibles pour votre audience filtrée, il est possible que la somme des colonnes individuelles soit inférieure au Total des utilisateurs accessibles. Cet écart est généralement dû au fait qu'un certain nombre d'utilisateurs se qualifient pour le segment ou les filtres de la campagne, mais ne sont pas joignables par push (par exemple, parce qu'ils ne disposent pas de [jetons de notification push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens) valides ou actifs).

{% enddetails %}

![Tableau des statistiques d'audience détaillées pour les utilisateurs accessibles.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

Gardez à l'esprit que l'appartenance exacte à un segment est toujours calculée avant l'envoi du message.

Vous pouvez également choisir de n'envoyer votre campagne qu'aux utilisateurs ayant un [statut d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) spécifique, par exemple ceux qui sont abonnés et ont opté pour le push.

Facultativement, vous pouvez aussi limiter la distribution à un nombre spécifié d'utilisateurs dans le segment, ou permettre aux utilisateurs de recevoir le même message deux fois dans le cadre d'une campagne récurrente.

##### Campagnes multicanales avec e-mail et notification push

Pour les campagnes multicanales ciblant à la fois les canaux e-mail et push, vous pouvez limiter votre campagne pour que seuls les utilisateurs ayant explicitement consenti reçoivent le message (en excluant les utilisateurs abonnés ou désabonnés). Par exemple, si vous avez trois utilisateurs avec des statuts d'abonnement différents :

- L'**utilisateur A** est abonné à l'e-mail et le push est activé. Cet utilisateur ne reçoit pas l'e-mail, mais recevra la notification push.
- L'**utilisateur B** a consenti à l'e-mail mais le push n'est pas activé. Cet utilisateur recevra l'e-mail, mais pas la notification push.
- L'**utilisateur C** a consenti à l'e-mail et le push est activé. Cet utilisateur recevra à la fois l'e-mail et la notification push.

Pour ce faire, sous **Résumé de l'audience**, sélectionnez d'envoyer cette campagne aux « utilisateurs ayant consenti uniquement ». Cette option garantit que seuls les utilisateurs ayant consenti recevront vos e-mails, et Braze n'enverra vos notifications push qu'aux utilisateurs pour lesquels le push est activé par défaut.

{% alert important %}
Avec cette configuration, n'incluez pas de filtres dans l'étape **Audiences cibles** qui limitent l'audience à un seul canal (par exemple, `Foreground Push Enabled = True` ou `Email Subscription = Opted-In`).
{% endalert %}

#### Sélectionner des événements de conversion

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, des [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), après avoir reçu une campagne. Vous avez la possibilité d'autoriser une fenêtre allant jusqu'à 30 jours pendant laquelle une conversion sera comptabilisée si l'utilisateur effectue l'action spécifiée.

{% endtab %}

{% tab Canvas %}

Si vous ne l'avez pas déjà fait, complétez les sections restantes de votre composant Canvas. Pour plus de détails sur la manière de créer le reste de votre Canvas, de mettre en œuvre les tests multivariés et la sélection intelligente, et plus encore, consultez l'étape [Créer votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de notre documentation Canvas.

{% endtab %}
{% endtabs %}

## Étape 7 : Vérifier et déployer {#review-and-deploy-push}

Après avoir terminé la création de votre campagne ou de votre Canvas, vérifiez-en les détails. Pour les campagnes, la dernière page vous fournit un résumé de la campagne que vous avez conçue. Confirmez tous les détails pertinents, assurez-vous d'avoir testé votre message, puis envoyez-le et observez les données affluer !

Ensuite, consultez les [rapports push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_reporting/) pour savoir comment accéder aux résultats de votre campagne push. Pour les notifications push, vous pourrez consulter les statistiques du nombre de messages envoyés, distribués, rejetés, ouverts et ouverts directement.