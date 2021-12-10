---
nav_title: "Création d'un message Push"
article_title: Création d'une campagne Push
page_order: 4
page_type: tutoriel
description: "Cette page de tutoriel couvre les différents composants impliqués dans la création d'un message push, y compris la configuration, l'envoi, le ciblage, et plus encore."
channel: Pousser
tool:
  - Campagnes
---

# Création d'un message push

> Les notifications push sont merveilleuses pour les appels temporaires à l'action, ainsi que pour les utilisateurs qui ne sont pas entrés dans l'application depuis un certain temps. <br><br> Des campagnes de push réussies poussent l'utilisateur directement vers le contenu et démontrent la valeur de votre application.

_Pour voir des exemples de notifications push, consultez notre [Études de cas][8]._

## Étape 1 : Créer une nouvelle campagne de push {#create-new-campaign-push}

!\[Create new push campaign\]\[1\]{: style="float:right;max-width:25%;margin-left:15px;"}

Accédez à la page **Campagnes** et créez une nouvelle campagne de push. Cliquez sur __Créer une campagne__ et sélectionnez __Notification Push__. Ou, si vous voulez inclure plusieurs canaux en plus de Push, sélectionnez **Campagne multi-canaux**.

## Étape 2: Nommez votre campagne, choisissez les types de messages et composez votre message

Donnez un nom à votre campagne et sélectionnez la plateforme que vous voulez cibler. Pour les campagnes multi-canaux, cliquez sur **Ajouter un canal de messagerie** pour ajouter des plateformes push supplémentaires.

!\[Select push platform\]\[2\]

!\[Select notification type\]\[3\]{: style="float:right;max-width:50%;margin-left:15px;"}

Pour iOS ou Android, sélectionnez votre type de notification :

- Push standard
- [Envoyer des histoires]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/)
- Image en ligne (Android uniquement)

Si vous voulez inclure des images dans votre campagne de push, reportez-vous aux guides suivants sur la création d'une notification enrichie pour [iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/) ou [Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/).

Maintenant, il est temps d'écrire votre message push ! Commencez à taper dans la boîte de message et regardez un aperçu apparaître dans la zone de prévisualisation à gauche. Les messages push doivent être formatés en texte brut, mais peuvent inclure [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) pour que votre push soit personnalisé et ciblé.

### Étapes supplémentaires de personnalisation du push

#### Langues

Ajouter une copie dans plusieurs langues en utilisant le bouton __Ajouter des langues__. Insérez Liquid dans votre message pour définir des messages et des champs personnalisés dans des langues spécifiques basées sur les préférences de langue d'un client. Consultez des exemples de cas d'utilisation dans notre [bibliothèque de cas d'utilisation liquide]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/#language).

#### Comportement au clic

Spécifiez ce qui se passe lorsqu'un utilisateur clique sur le corps d'une notification push avec **Sur le bouton Comportement**. Par exemple, vous pouvez inviter les clients à ouvrir votre application, rediriger les clients vers une URL Web spécifiée, ou même ouvrir une page spécifique de votre application avec un [lien profond]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/).

Ici, vous pouvez également configurer des invites de boutons dans votre notification push, tels que:

- Oui/Non
- Confirmer/Annuler
- En savoir plus

{% alert note %}
Pour plus d'informations sur les options de notification spécifiques à la plate-forme, voir [Options de notification iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/notification_options_ios/) ou [Options de notification Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/notification_options_android/).
{% endalert %}

### Étape 2b: Prévisualiser et tester votre message

!\[Test push message\]\[7\]{: style="float:right;max-width:30%;margin-left:15px;"}

Le test est sans doute l'une des étapes les plus critiques. Une fois que vous avez fini de composer votre message push parfait, testez-le avant de l'envoyer. Sélectionnez l'onglet **Testez** et utilisez **Aperçu du message en tant qu'utilisateur** pour avoir une idée de la façon dont votre message peut être affiché sur mobile. Utilisez **Envoyer le test** pour vous envoyer une poussée de test et vous assurer que votre message s'affiche correctement.

## Étape 3 : Planifiez votre campagne de messagerie push {#schedule-push-campaign}

Choisissez entre envoyer votre campagne à un moment planifié, une fois que les utilisateurs ont terminé une action, ou via une requête API.

!\[Schedule\]\[4\]

{% tabs %}
  {% tab Scheduled Delivery %}
Utilisez [Livraison planifiée]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/scheduled_delivery/) pour spécifier l'heure à laquelle vous voulez que votre campagne soit envoyée, soit immédiatement ou à une date ultérieure (vous pouvez également considérer l'heure locale d'un utilisateur dans votre programme).

Vous ne savez pas quel est le meilleur moment pour envoyer votre campagne? Utilisez [Timing Intelligent]({{site.baseurl}}/user_guide/intelligence/intelligent_timing/) pour envoyer votre campagne quand un utilisateur est le plus susceptible de vous engager. Braze effectue ce calcul en se basant sur une analyse statistique des interactions de l'utilisateur avec votre application.

Les messages peuvent également être configurés pour se reproduire sur une base journalière, hebdomadaire (optionnellement sur certains jours) ou mensuelle.

{% endtab %}
{% tab Action-Based Delivery %}

Utilisez [Action-Based Delivery]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/) pour spécifier le temps qu'un message enverra après qu'un utilisateur prenne une action particulière. Configurer les messages à envoyer immédiatement ou après un délai (vous pouvez également considérer l'heure locale d'un utilisateur dans votre planification).

{% endtab %}
{% tab API-Triggered Delivery %}
Utilisez [la distribution déclenchée par l'API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/api_triggered_delivery/) pour des cas d'utilisation transactionnelle plus avancés.

{% endtab %}
{% endtabs %}

{% alert warning %}
Sauf si vous cochez la case intitulée « Autoriser les utilisateurs à redevenir éligibles pour recevoir une campagne» dans la partie __Planifier__ de l'assistant de campagne, chaque utilisateur ne recevra le contenu d'une campagne qu'une seule fois, et seuls les nouveaux utilisateurs qui satisfont aux critères recevront la campagne sur les livraisons subséquentes.
{% endalert %}

## Step 4: Target users

À l'étape **Utilisateurs cibles** de la configuration de la campagne, choisissez le public cible pour votre campagne.

!\[Options de ciblage\]\[25\]

Dans la section Options de ciblage, vous trouverez quelques options pour qui vous pouvez envoyer votre campagne à :

1. __Membres d'un segment créé précédemment.__ Pour faire cela, sélectionnez un segment dans la liste déroulante sous **Utilisateurs cibles par segment**. <br><br>
2. __Utilisateurs qui tombent en plusieurs segments précédemment créés.__ Pour ce faire, ajoutez plusieurs segments à partir du menu déroulant sous **Utilisateurs cibles par segment**. L'audience cible résultante sera les utilisateurs dans le premier segment *et* le second segment *et* le troisième segment, etc. <br><br>
3. __Utilisateurs d'un ou de plusieurs segments précédemment créés qui tombent également sous des filtres supplémentaires.__ Après avoir d'abord sélectionné vos segments, affinez encore davantage votre public sous la section **Filtres Supplémentaires**. Ceci est démontré dans la capture d'écran ci-dessous, qui cible les utilisateurs qui sont dans le segment des 10 messages non lus *et* sont dans le segment Utilisateurs actifs, *et* ont fait un achat il y a moins de 30 jours. <br><br>
4. __Utilisateurs qui tombent sous une série de filtres (et ne sont pas définis par des segments préexistants).__ Cela signifie que vous n'avez pas besoin de cibler une campagne sur un segment préexistant. Au lieu de cela, faire une audience ad hoc lors de la création de la campagne en utilisant uniquement les filtres supplémentaires et non en sélectionnant des segments sous **Utilisateurs cibles par segment**. Cela vous permettra d'ignorer la création de segment lors de l'envoi de campagnes à un public unique.

Des statistiques détaillées sur les auditoires des canaux ciblés par votre campagne sont disponibles dans le pied de page. Pour voir quel pourcentage de votre base d'utilisateurs est ciblé et la valeur à vie de ce segment, cliquez sur **Afficher des statistiques supplémentaires**.

{% détails Pourquoi mes utilisateurs réalisables ont-ils l'air plus petit que ce qui devrait être le cas ? %}

Lorsque vous cliquez sur **Afficher les statistiques supplémentaires** et afficher le nombre total d'utilisateurs accessibles pour votre public filtré, vous remarquerez peut-être qu'il est plus petit que la somme des autres colonnes. Cet écart est généralement dû au fait qu'il y a un certain nombre d'utilisateurs qui se qualifient pour le segment ou les filtres dans la campagne, mais ne sont pas accessibles par push (par exemple, parce qu'ils n'ont pas de jetons de poussée [valides ou actifs]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens)).

{% enddetails %}

!\[Pied de page des utilisateurs atteignables\]\[24\]

Gardez à l'esprit que l'adhésion exacte au segment est toujours calculée juste avant l'envoi du message.

### Campagnes multi-canaux avec push et email

Pour les campagnes multicanaux ciblant à la fois les canaux push et email, vous voudrez peut-être limiter votre campagne de sorte que seuls les utilisateurs qui sont explicitement inscrits recevront le message (excluant les utilisateurs abonnés ou désabonnés). Par exemple, dites que vous avez trois utilisateurs de différents statuts d'opt-in :

- **L'utilisateur A** est abonné à l'e-mail et est push activé. Cet utilisateur ne reçoit pas l'email mais recevra le push.
- **L'utilisateur B** est opté pour l'email mais n'est pas poussé activé. Cet utilisateur recevra l'email mais ne recevra pas le push.
- **L'utilisateur C** est opté pour l'email et est push activé. Cet utilisateur recevra à la fois l'email et le push.

Pour ce faire, sous **Résumé de l'audience**, sélectionnez pour envoyer cette campagne à "utilisateurs opted-in seulement". Cette option vous assurera que seuls les utilisateurs optés recevront votre courriel. et Braze enverra uniquement votre push aux utilisateurs qui sont activés par défaut.

{% alert important %}
Avec cette configuration, n'incluez aucun filtre dans l'étape **Utilisateurs cibles** qui limitent l'audience à un seul canal (e. ., `Push Activé = True` ou `Abonnement par courriel = Opted-In`).
{% endalert %}

## Étape 5 : Choisissez les événements de conversion

Braze vous permet de vérifier si les utilisateurs effectuent des actions spécifiques (Conversion Events) après avoir reçu une campagne. Vous pouvez spécifier l'une des actions suivantes en tant qu'"Événement de conversion":

- Ouvre l'application
- Effectue un achat
  - Cela peut être un achat générique ou un article spécifique
- Effectue un événement spécifique personnalisé

Vous avez la possibilité d'autoriser un événement de conversion dans un délai approprié pour votre campagne. La fenêtre de conversion pour un événement de conversion peut varier de 5 minutes à 30 jours. L'événement comptera comme une conversion s'il a lieu pendant la période spécifiée.

!\[Événement de conversion\]\[15\]

## Étape 6 : Réviser et déployer {#review-and-deploy-push}

La page finale vous donnera un résumé de la campagne que vous venez de concevoir. En cliquant sur **Lancer la campagne** vous pourrez l'envoyer. Confirmez tous les détails pertinents et regardez les données rouler !

!\[Page de confirmation\]\[5\]

## Données des résultats {#results-data-push}

Braze vous montrera le nombre de messages envoyés et ouverts au fil du temps pour chaque campagne de push que vous déployez, comme indiqué ci-dessous:

!\[Results\]\[6\]

Pour les notifications push, vous serez en mesure de voir les statistiques du nombre de messages envoyés, distribués, rebondis, ouverts, et directement ouverts.
[1]: {% image_buster /assets/img_archive/new_campaign_push.png %} [2]: {% image_buster /assets/img_archive/push_1.png %} [3]: {% image_buster /assets/img_archive/push_2. ng %} [4]: {% image_buster /assets/img_archive/schedule.png %} [5]: {% image_buster /assets/img_archive/confirmation_page. ng %} [6]: {% image_buster /assets/img_archive/push-results-statistics.png %} [7]: {% image_buster /assets/img_archive/push_3.png %} [15]: {% image_buster /assets/img_archive/conversion_event_selection. ng %} [24]: {% image_buster /assets/img_archive/multi_channel_footer.png %} [25]: {% image_buster /assets/img_archive/target_segmenter.png %}

[8]: https://www.braze.com/customers 
