---
nav_title: Suivi des désabonnements Push
article_title: Suivi des désabonnements Push
page_type: solution
description: "Cet article d'aide fournit quelques conseils pour suivre les désabonnements par push."
channel: push
---

# Suivi des désabonnements aux services de push

Les désabonnements par push dépendent des mises à jour du statut push d'un utilisateur par des fournisseurs tels qu'Apple ou Google. Ces mises à jour peuvent être peu fréquentes et imprévisibles. Par conséquent, les désabonnements aux campagnes push ne sont pas pris en compte en tant qu'indicateurs dans l'analyse/analytique des campagnes push. 

Cependant, le suivi manuel des désabonnements push peut encore fournir des informations précieuses sur les réponses des utilisateurs à votre fréquence de notification et à la pertinence du contenu. Voici deux options pour le suivi des désabonnements par push.

## Option 1 : Utiliser les filtres de segmentation

En guise de solution de contournement, vous pouvez créer une segmentation pour identifier les utilisateurs qui ne sont pas activés pour le push, ce qui signifie qu'ils ne sont pas abonnés ou opt-in et qu'ils n'ont pas de [jeton de push en avant-plan]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens). Par exemple, pour connaître le nombre de désabonnements dans votre application Android, vous utiliserez la combinaison des segments suivants : 

- `Background or Foreground Push Enabled for App "TEST (Android)" is false`
- `Has Uninstalled`

![La section Segment Builder avec le filtre "Background or Foreground Push Enabled for App" pour l'application TEST (Android) est fausse, et le filtre "Has Uninstalled" sont sélectionnés pour montrer 2 393 utilisateurs joignables.]({% image_buster /assets/img/push_unsub_segment_example.png %})

Notez que les filtres de segmentation seront approximatifs et ne pourront pas être spécifiquement liés à une date et à une campagne.

## Option 2 : Utiliser un événement personnalisé

{% alert important %}
Sachez que l'enregistrement d'un événement personnalisé pour un changement d'abonnement consommera des [points de données]({{site.baseurl}}/user_guide/data_and_analytics/data_points#consumption-count). Vous pouvez également utiliser des filtres de segmentation pour identifier et cibler les utilisateurs qui ne sont pas équipés de la fonction "push".
{% endalert %}

Pour une solution de contournement différente, nous vous recommandons également de créer un événement personnalisé pour les désabonnements push en fonction du statut de l'utilisateur activé par push ( `true` ou `false` ) afin d'assurer le suivi de ces indicateurs.

_Dernière mise à jour le 13 juin 2024_
