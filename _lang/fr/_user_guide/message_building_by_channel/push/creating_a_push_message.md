---
nav_title: "Création d’un message de notification push"
article_title: Créer une campagne de notification push
page_order: 4
page_type: tutorial
description: "Cette page de didacticiel couvre les différents composants impliqués dans la création d’un message de notification push, y compris la configuration, l’envoi, le ciblage, etc."
channel: push
tool:
  - Campagnes
  
---

# Créer un message de notification push

> Les notifications push sont idéales pour les appels à l’action urgents, ainsi que pour le ré-engagement des utilisateurs qui n’ont pas utilisé l’application depuis un certain temps. Les campagnes de notifications push réussies amènent l’utilisateur directement au contenu et démontrent la valeur de votre application.

Pour voir des exemples de notifications push, consultez notre [Études de cas][8].

## Étape 1 : Choisissez où créer votre message {#create-new-campaign-push}

Vous ne savez pas si votre message doit être envoyé via une campagne ou un Canvas ? Les campagnes sont mieux adaptées aux campagnes de communication simples et uniques, tandis que les Canvas sont mieux adaptés aux parcours client en plusieurs étapes.

{% tabs %}
{% tab Campaign %}

**Étapes :**

1. Sur la page **Campaign (Campagne)**, cliquez sur <i class="fas fa-plus"></i>**Create Campaign (Créer une campagne)**.
2. Sélectionnez **Notification Push**, ou, pour les campagnes ciblant plusieurs canaux, sélectionnez **Campagne multicanal**.
3. Donnez un nom clair et significatif à votre campagne.
4. Si nécessaire, ajoutez des [Équipes]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/) et des [Tags.]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/)
   * Les tags facilitent la recherche et l’identification des campagnes, et la création de rapports. Par exemple, lorsque vous utilisez le [Créateur de rapports]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/), vous pouvez filtrer les éléments en fonction de tags spécifiques.
5. Ajoutez et nommez autant de variantes que nécessaire pour votre campagne. Vous pouvez choisir différentes plates-formes, types de messages et mises en page pour chacune de vos variantes ajoutées. Pour plus d’informations sur ce sujet, consultez les [Tests multivariés et A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Si tous les messages de votre campagne vont être similaires ou avoir le même contenu, composez votre message avant d’ajouter des variantes supplémentaires. Vous pouvez ensuite choisir **Copy from Variant (Copier à partir de la variante)** dans le menu déroulant **Add Variant (Ajouter une variante)**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Étapes :**

1. [Créez votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) à l’aide de l’Assistant Canvas.
2. Après avoir configuré votre Canvas, ajoutez une étape dans le Créateur de Canvas. Donnez un nom clair et significatif à votre étape.
3. Choisissez un [calendrier des étapes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) et spécifiez un délai si nécessaire.
4. Filtrez votre audience pour cette étape si nécessaire. Vous pouvez affiner davantage les destinataires de cette étape en spécifiant des segments et en ajoutant des filtres supplémentaires. Les options d’audience seront vérifiées après le délai au moment de l’envoi des messages.
5. Choisissez votre [comportement d’avancement]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Choisissez les autres canaux de communication que vous souhaitez associer à votre message.

{% endtab %}
{% endtabs %}

## Étape 2 : Spécifier les plateformes de livraison

Commencez par choisir la plate-forme qui doit recevoir la notification push : iOS, Android ou Web. Utilisez cette sélection pour limiter la transmission d’une notification push à un ensemble d’applications spécifiques. Pour les campagnes multicanales ou les Canvas, cliquez sur **Ajouter un canal de communication** pour ajouter des plates-formes supplémentaires de notification push. 

Les sélections de plateforme étant spécifiques à chaque variante, vous pouvez tester l’engagement des messages par plateforme.

## Étape 3 : Sélectionner un type de notification (iOS et Android)

Sélectionnez votre type de notification pour iOS et Android :

![Type de notification avec notification push standard sélectionnée comme exemple.][3]{: style="float:right;max-width:40%;margin-left:15px;"}

- Notification push standard
- [Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/)
- Image insérée (Android uniquement)

Si vous souhaitez inclure des images dans votre campagne de notification push, reportez-vous aux guides suivants pour créer une notification riche pour [iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/) ou [Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/).

## Étape 4 : Composer votre message de notification push

Il est maintenant temps d’écrire votre message de notification push ! L’onglet **Compose (Composer)** vous permet de modifier tous les aspects du contenu et du comportement de votre message.

![Onglet Composer de création d’une notification push.]({% image_buster /assets/img_archive/push_compose.png %})

Le contenu de l’onglet **Compose (Composer)** varie en fonction du type de notification que vous avez choisi à l’étape précédente, mais peut inclure l’une des options suivantes :

#### Canal ou groupe de notification (iOS et Android)

Pour plus d’informations sur les options de notification spécifiques à la plate-forme, consultez les [Options de notification iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/notification_options_ios/) ou les [Options de notification Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/notification_options_android/).

#### Langue

Ajouter une copie dans plusieurs langues à l’aide du bouton **Ajouter des langues**. Nous vous recommandons de sélectionner vos langues avant d’écrire votre contenu afin que vous puissiez remplir votre texte dans Liquid. Consultez notre [liste complète des langues disponibles][18].

#### Titre et corps

Commencez à taper dans la boîte de message et voyez un aperçu apparaître dans la fenêtre d’aperçu à gauche. Les messages de notification push doivent être formatés en texte brut. Pour rendre votre notification push personnalisée et ciblée, vous pouvez inclure [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/).

{% alert tip %}
Besoin d’aide pour créer un texte d’exception ? Essayez d’utiliser l’[assistant de rédaction IA]({{site.baseurl}}/user_guide/intelligence/ai_copywriting/). Saisissez un nom ou une description du produit et l’IA générera un texte marketing semblant d’origine humaine pour une utilisation dans votre message.

![Bouton Lancer l’IA de rédaction, situé dans le champ Corps du composeur de notification push.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_push.png %}){: style="max-width:60%"}
{% endalert %}

#### Image

Lorsque cela est possible, l’icône de votre application est automatiquement ajoutée en tant qu’image pour votre notification push. Vous avez également la possibilité d’envoyer des notifications enrichies, ce qui permet d’obtenir plus de personnalisation dans vos notifications push en ajoutant du contenu supplémentaire en plus du texte.

Pour plus d’informations sur l’utilisation des images dans vos notifications push, reportez-vous aux articles suivants :

- [Créer des notifications enrichies pour iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/)
- [Créer des notifications enrichies pour Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/)

#### Comportement on-click

Spécifiez ce qui se passe lorsqu’un utilisateur clique sur le corps d’une notification push avec **Comportement lors du clic**. Par exemple, vous pouvez inviter les clients à ouvrir votre application, les rediriger vers une URL Web spécifiée ou même ouvrir une page spécifique de votre application avec un [lien profond]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/).

Ici, vous pouvez également configurer des boutons d’invites dans votre notification push, comme :

- Accepter/Refuser
- Oui/Non
- Confirmer/Annuler
- Plus 

#### Options de l’appareil

Si vous le souhaitez, vous pouvez choisir d’envoyer uniquement votre notification push vers l’appareil utilisé le plus récemment utilisé par l’utilisateur. S’il [ne permet pas les notifications push]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-enabled), le message ne sera pas envoyé.

Pour iOS, vous pouvez limiter encore plus les messages en envoyant uniquement des notifications push sur les appareils iPad ou uniquement vers des périphériques iPhone et iPod.

### Étape 4a : Prévisualiser et tester votre message

![Tester un message de notification push][7]{: style="float:right;max-width:30%;margin-left:15px;"}

Le test est sans doute l’une des étapes les plus critiques. Après avoir fini de composer votre message de notification push parfait, testez-le avant de l’envoyer. Sélectionnez l’onglet **Test** et utilisez **Aperçu du message en tant qu’utilisateur** pour voir comment votre message peut s’afficher sur mobile. Utilisez **Envoyer un test** pour vous envoyer un test de notification push et vous assurer que votre message s’affiche correctement.

## Étape 5 : Créez le reste de votre campagne ou de votre Canvas.

{% tabs %}
{% tab Campaign %}

Créez le reste de votre campagne. Consultez les sections suivantes pour plus de détails sur la manière de mieux utiliser nos outils pour créer des notifications push.

#### Choisir un calendrier ou un déclencheur pour la livraison

Les messages de notification push peuvent être livrés sur la base d’une heure planifiée, d’une action ou d’un déclencheur API. Pour en savoir plus, consultez la section [Planifier votre campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Pour une livraison par événement, vous pouvez également définir la durée de la campagne et les [Heures calmes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

Cette étape permet également de spécifier les contrôles de livraison, comme permettre aux utilisateurs de devenir [rééligibles]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) pour recevoir la campagne ou activer les règles de [limite de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Choisir les utilisateurs à cibler

Ensuite, vous devez [cibler des utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/) en choisissant des segments ou des filtres pour limiter votre audience. Vous recevez automatiquement un aperçu de ce à quoi ressemble la population approximative du segment à ce moment-là. Des statistiques d’audience détaillées pour les canaux ciblés par votre campagne sont disponibles dans le pied de page. Pour voir quel pourcentage de votre base d’utilisateurs est ciblé et la valeur à vie pour ce segment, cliquez sur **Afficher les statistiques supplémentaires**.

{% details Pourquoi mon indicateur Total Reachable Users n’est pas égal à la somme de tous mes canaux ? %}

Lorsque vous affichez les Total des utilisateurs accessibles pour votre audience filtrée, il est possible que vous constatiez que la somme des colonnes individuelles est plus petite que le Total des utilisateurs accessibles. Cette différence est généralement due au fait qu’il existe un certain nombre d’utilisateurs qui remplissent les conditions requises pour le segment ou les filtres de la campagne, mais qui ne sont pas accessibles par le biais de notifications push (par exemple, parce qu’ils ne possèdent pas de [jetons de notification push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens) valides ou actifs).

{% enddetails %}

![Tableau des statistiques d’audience détaillées pour les utilisateurs accessibles.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

Gardez à l’esprit que l’appartenance à un segment exact est toujours calculée juste avant l’envoi du message.

Vous pouvez également choisir d’envoyer votre campagne uniquement aux utilisateurs qui ont un [statut de souscription]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) donné, tels que ceux qui sont enregistrés et sont abonnés aux notifications push.

Facultativement, vous pouvez également limiter la livraison à un nombre spécifié d’utilisateurs dans le segment, ou permettre aux utilisateurs de recevoir le même message deux fois dans le cadre d’une campagne récurrente.

##### Campagnes multicanales avec e-mail et notification push

Pour les campagnes multicanales avec e-mail et notifications push, vous pouvez limiter votre campagne pour que seuls les utilisateurs ayant explicitement consenti à recevoir des e-mails reçoivent le message (en excluant les utilisateurs abonnés et désabonnés). Par exemple, si vous avez trois utilisateurs avec un statut d’abonnement différent :

- **L’utilisateur A** est abonné aux e-mails et la notification push est activée. Cet utilisateur ne reçoit pas les e-mails, mais il recevra les notifications push.
- L’**utilisateur B** a consenti explicitement aux e-mails, mais la notification push n’est pas activée. Cet utilisateur recevra les e-mails, mais pas les notifications push.
- L’**utilisateur C** a consenti explicitement aux e-mails et la notification push est activée. Cet utilisateur recevra les e-mails et les notifications push.

Pour ce faire, sous **Audience Summary (Synthèse de l’audience)**, sélectionnez pour envoyer cette campagne uniquement aux « utilisateurs ayant explicitement consenti ». Cette option garantira que seuls les utilisateurs abonnés recevront vos e-mails et Braze enverra uniquement vos notifications push aux utilisateurs pour lesquels la notification push est activée par défaut.

{% alert important %}
Avec cette configuration, n’incluez pas de filtres dans l’étape **Utilisateurs cible** qui limitent l’audience à un seul canal (par ex. `Notifications push activées = True` or `Inscription aux e-mails = Abonné`).
{% endalert %}

#### Sélectionner des événements de conversion

Braze vous permet de suivre à quelle fréquence les utilisateurs effectuent des actions spécifiques, des [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/), après avoir reçu une campagne. Vous avez la possibilité d’autoriser une fenêtre allant jusqu’à 30 jours pendant laquelle une conversion sera comptée si l’utilisateur entreprend l’action spécifiée.

{% endtab %}

{% tab Canvas %}

Si vous ne l’avez pas déjà fait, complétez les sections restantes de votre composant de Canvas. Pour plus d’informations sur la manière de mettre en place le reste de votre Canvas, d’implémenter un test multivarié et une sélection intelligente, référez-vous à l’étape [Construire votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de notre documentation Canvas.

{% endtab %}
{% endtabs %}

## Étape 6 : Revue et déploiement {#review-and-deploy-push}

Après avoir terminé de construire la fin de votre campagne ou de votre Canvas, réexaminez ses détails. Pour les campagnes, la dernière page vous affichera un résumé de la campagne que vous venez de concevoir. Confirmez tous les détails pertinents, assurez-vous d’avoir testé votre message, puis envoyez-le et regardez les données entrer !

Ensuite, consultez [Push reporting]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_reporting/) (Communication de notification push) pour découvrir comment accéder aux résultats de votre campagne de notification push. Pour les notifications push, vous pourrez afficher les statistiques du nombre de messages envoyés, livrés, retournés, ouverts et ouverts directement.

[1]: {% image_buster /assets/img_archive/new_campaign_push.png %}
[2]: {% image_buster /assets/img_archive/push_1.png %}
[3]: {% image_buster /assets/img_archive/push_2.png %}
[4]: {% image_buster /assets/img_archive/schedule.png %}
[5]: {% image_buster /assets/img_archive/confirmation_page.png %}
[6]: {% image_buster /assets/img_archive/push-results-statistics.png %}
[7]: {% image_buster /assets/img_archive/push_3.png %}
[8]: https://www.braze.com/customers
[15]: {% image_buster /assets/img_archive/conversion_event_selection.png %}
[18]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported
[24]: {% image_buster /assets/img_archive/multi_channel_footer.png %}
[25]: {% image_buster /assets/img_archive/target_segmenter.png %} 
