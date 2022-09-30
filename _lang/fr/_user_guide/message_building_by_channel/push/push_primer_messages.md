---
nav_title: Messages in-app d’amorce de notification push
article_title: Messages in-app d’amorce de notification push
page_order: 8
page_type: reference
description: "Optimisez votre taux d’abonnement en utilisant les messages in-app d’amorce de notification push"
channel: notification push

---

# Messages in-app d’amorce de notification push

![Messages in-app d’amorce de notification push pour une application de streaming. La notification affiche « Get push notifications from Movie Cannon? » (Voulez-vous recevoir des notifications push de Movie Cannon ?) Les notifications peuvent inclure de nouveaux films, émissions télévisées ou autres avis et peuvent être désactivées à tout moment."][1]{: style="float:right;max-width:40%;margin-left:15px;border:none;"}

Vous n’avez qu’une seule chance de demander aux utilisateurs la permission de les joindre par notification push. L’optimisation de l’inscription aux notifications est donc cruciale pour maximiser la portée de vos messages push.

Pour y parvenir, vous pouvez utiliser des messages in-app pour expliquer le type de messages auquel vos utilisateurs peuvent s’attendre à recevoir s’ils choisissent de s’inscrire, avant de leur montrer l’invite de notification push native. C’est ce qu’on appelle amorce de notification push.

Pour créer un message in-app d’amorce de notification push dans Braze, vous pouvez utiliser le bouton de comportement en cas de clic « Request Push Permission » (Demander l’autorisation de notification push) lors de la création d’un message in-app pour iOS ou Web.

## Conditions préalables

Ce guide utilise un bouton de [comportement en cas de clic](#button-actions) qui n’est pris en charge que par les versions plus récentes du SDK. Notez que certains de ces SDK ne sont pas encore publiés. Consultez les liens suivants pour vérifier la version actuelle :

{% sdk_min_versions ios:5.1.0 android:21.0.0 web:4.0.3 %}

## Étape 1 : Créer un message in-app

[Créez un message in-app][2] comme vous le feriez habituellement. Vous pouvez choisir d’envoyer le message à des applications mobiles, à des navigateurs Web ou aux deux. Toutefois, le comportement en cas de clic pour demander l’autorisation de notifications push n’est disponible que pour iOS et Web. 

Ensuite, sélectionnez un type de message et une mise en page. Pour vous donner suffisamment d’espace pour expliquer les notifications push auxquels vos utilisateurs peuvent s’attendre (et autoriser les boutons), Braze suggère un message plein écran ou modal. Notez que pour un message in-app en plein écran, une image est requise. 

## Étape 2 : Créer votre message

Maintenant, il est temps d’ajouter votre copie ! Rappelez-vous qu’une amorce de notification push a l’objectif de pousser l’utilisateur à activer les notifications push. Dans votre corps de message, nous vous suggérons de mettre en exergue les raisons pour lesquelles vos utilisateurs devraient activer les notifications push. Soyez précis quant au type de notifications que vous souhaitez envoyer et à la valeur qu’ils peuvent fournir.

Par exemple, une application d’actualités peut utiliser l’amorce de notification push suivante :

> Vos actualités vous suivent partout ! Activez les notifications push pour obtenir des alertes pour les nouvelles et sujets majeurs qui comptent pour vous.

Une application de streaming pourrait utiliser ce qui suit :

> Get push notifications from Movie Cannon? (Voulez-vous recevoir des notifications push de Movie Cannon ?) Les notifications peuvent inclure de nouveaux films, émissions télévisées ou autres avis et peuvent être désactivées à tout moment.

Pour les meilleures pratiques et ressources supplémentaires, consultez [Création de demandes d’inscription personnalisées][3].

## Étape 3 : Spécifier le comportement du bouton {#button-actions}

Pour ajouter des boutons à votre message in-app, ajoutez du texte dans les champs de texte **Button 1** et **Button 2** qui sont respectivement les boutons secondaire et principal de votre message in-app. Nous recommandons d’activer les boutons « Allow notifications » (Autoriser les notifications) et « Not now » (Pas maintenant) comme boutons d’amorce, mais il existe de nombreuses invites de bouton différentes que vous pouvez attribuer.

Après avoir ajouté la copie du bouton, spécifiez le comportement en cas de clic pour chaque bouton :

- **Bouton 1 :** Définissez celui-ci sur « Close Message » (Fermer le message). Il s’agit de votre bouton secondaire ou de l’option « Not now » (Pas maintenant).
- **Bouton 2 :** Définissez cette option sur « Request Push Permission » (Demander l’autorisation de notification push). Il s’agit du bouton principal ou de l’option « Allow notifications » (Autoriser les notifications).

![][4]

## Étape 4 : Planifier la livraison

Pour que votre amorce de notification push soit envoyée à un moment pertinent, vous devez planifier votre message in-app en tant que message basé sur une action avec **Perform Custom Event** (Exécuter un événement personnalisé) comme action de déclenchement.

Bien que le moment idéal varie, Braze suggère d’attendre qu’un utilisateur effectue une sorte d’[action à forte valeur](https://www.braze.com/resources/videos/mapping-high-value-actions), indiquant qu’il commence à voir de la valeur dans votre application ou votre site, ou lorsqu’il existe un besoin urgent auquel les notifications push peuvent répondre (par exemple, après qu’il ait passé une commande pour lui offrir des informations sur le suivi de l’expédition). De cette façon, l’invite représente un avantage pour le client plutôt que pour votre marque.

![][5]

## Étape 5 : Utilisateurs cibles

Étant donné que l’objectif d’une campagne de notification push est d’inciter les utilisateurs à s’abonner aux messages push, vous ne voulez pas cibler les utilisateurs qui y sont déjà abonnés. Pour ce faire, ajoutez un segment ou un filtre pour ces utilisateurs, à savoir, `Push Subscription Status is not Opted In`.

Au-delà de cela, vous pouvez décider des segments supplémentaires qui vous semblent les plus appropriés. Par exemple, vous pouvez cibler les utilisateurs qui ont effectué un deuxième achat, les utilisateurs qui viennent de créer un compte pour devenir membre ou même ceux qui visitent votre application plus de deux fois par semaine. Cibler les utilisateurs pour ces segments essentiels augmente la probabilité que les utilisateurs s’abonnent et activent les notifications push.

## Étape 6 : Événements de conversion

Braze propose des paramètres par défaut pour les conversions, mais vous pouvez définir des [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/) en plus des amorces de notification push.

[1]: {% image_buster /assets/img_archive/push_primer_iam.png %}
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/creating_custom_opt-in_prompts/
[4]: {% image_buster /assets/img_archive/push_primer_button_behavior.png %}
[5]: {% image_buster /assets/img_archive/push_primer_trigger.png %}
