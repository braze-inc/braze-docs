---
nav_title: Capturer des utilisateurs en train de tourner
article_title: Capturer des utilisateurs en train de tourner
page_order: 1
page_type: tutoriel
description: "Cet article traite de la question de la disparition des utilisateurs et de la manière d'utiliser efficacement les campagnes de Braze pour réengager ces utilisateurs."
tool:
  - Segments
  - Campagnes
---

# Capturer des utilisateurs en cours d'expiration

> Cet article traite de la question de la disparition des utilisateurs et de la manière d'utiliser efficacement les campagnes de Braze pour réengager ces utilisateurs.

Si votre auditoire est en baisse, il est crucial d'essayer de les obturer. Reconnaissant cette nécessité, Braze facilite la mise en place de campagnes automatisées de réengagement récurrent pour capturer les utilisateurs qui sont en train de disparaître. Vous pouvez choisir la période de réengagement et la récurrence qui convient le mieux à votre application, mais pour démontrer, nous allons commencer avec un plan de réengagement de 14 jours.

Pour en savoir plus sur le ciblage des utilisateurs, consultez notre [cours LAB de mise en place de campagne](http://lab.braze.com/campaign-setup-delivery-targeting-conversions)!

## Étape 1 : Segmentation

Tout d'abord, nous allons créer un segment pour cibler les utilisateurs qui n'ont pas utilisé l'application au cours des deux dernières semaines, en utilisant les filtres suivants :

- Dernière application utilisée il y a plus de 2 semaines
- Dernière application utilisée il y a moins de 3 semaines

!\[Détails du segment\]\[1\]

N’oubliez pas de nommer le segment quelque chose de simple et mémorable, comme « Utilisateurs laborieux – 2 Semaines». Puisque nous allons mettre en place la campagne pour qu'elle se répète chaque semaine, Nous voulons nous assurer qu'il y a au moins une semaine d'utilisateurs capturés dans le segment. C'est pourquoi nous avons sélectionné les utilisateurs qui ont utilisé l'application pour la dernière fois il y a deux à trois semaines.

## Étape 2: Création de la campagne

Ensuite, cliquez sur **Créer une campagne** et choisissez le type de campagne que nous enverrons à ce segment. dans cet exemple, nous allons créer une nouvelle [campagne de poussée][6].

!\[Créer une campagne\]\[5\]

Nous allons nommer la campagne **Message à Utilisateurs Lapsed - 2 Semaines** et sélectionner le segment. Ici, nous allons créer le contenu de notre message. Dans cet exemple, nous ne ciblerons que les utilisateurs iOS, mais vous pouvez utiliser Braze pour les notifications push Android et iOS. Plus près de la dernière fois qu'un utilisateur était dans l'application, plus il est important d'être d'actualité et pertinent. Messagerie d'un utilisateur après deux semaines de non-utilisation de l'application, il est important de surfacer le contenu pertinent et de souligner les avantages de l'utilisation de l'application.

!\[Exemple de campagne\]\[2\]

Ensuite, nous créerons un horaire récurrent pour envoyer notre message hebdomadaire le jeudi à 17h45 à l'aide de [livraison locale du fuseau horaire][4] dans les **options de planification basées sur l'heure**. Nous vous recommandons de regarder le graphique de vos sessions aux utilisateurs cibles juste avant les périodes d'utilisation élevées. Cela vous assure que vous tentez de relancer les contacts quand ils sont le plus susceptibles d'utiliser l'application. Vous pourrez modifier cela plus tard et tester votre hypothèse initiale.

!\[Sélectionnez les options de livraison\]\[3\]

Maintenant, vous êtes prêt à envoyer la campagne. Confirmez les paramètres sur la dernière page de l'assistant et cliquez sur **Lancer la Campagne**!
[1]: {% image_buster /assets/img_archive/2weeklapse1.png %} [2]: {% image_buster /assets/img_archive/2weeklapse3. ng %} [3]: {% image_buster /assets/img_archive/2weeklapse4.png %} [5]: {% image_buster /assets/img_archive/2weeklapse2.png %}

[4]: {{site.baseurl}}/help/faqs/#what-does-local-time-zone-delivery-offer
[6]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message