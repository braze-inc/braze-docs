---
nav_title: Gestion des abonnements aux e-mails
article_title: Gestion des abonnements aux e-mails
page_order: 7
page_type: reference
description: "Le présent article couvre les meilleures pratiques de gestion des abonnements aux e-mails, notamment pour les utilisateurs non-inscrits, non valides ou dupliqués."
channel: email

---
   
# Gestion des abonnements aux e-mails

Assurez-vous de connaitre les outils fournis par Braze pour la [gestion des abonnements des utilisateurs aux e-mails][22] et le ciblage des utilisateurs avec des statuts d’abonnement spécifiques via des campagnes. Ces outils sont essentiels pour la conformité avec les [lois anti-spam][23].

## Adresses e-mail désabonnées

Braze désabonne automatiquement tout utilisateur qui se désabonne manuellement à vos e-mails via un [lien en pied de page personnalisé]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions) ou en marquant votre message comme indésirable. Ces utilisateurs ne seront pas ciblés par des futurs e-mails.

Si un utilisateur se désabonne et change son adresse e-mail ultérieurement, sa nouvelle adresse e-mail sera également désabonnée. En d’autres termes, une fois qu’un ID utilisateur externe est associé à un désabonnement, les adresses e-mail futures associées à cet ID Utilisateur seront également désabonnées.

{% alert tip %}
Reportez-vous aux bonnes pratiques de [réchauffement d’adresses IP]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ip_warming/) pour obtenir des conseils sur la manière de réengager efficacement vos utilisateurs !
{% endalert %}

## Adresses e-mails non valides et messages non délivrés

Des hard bounces peuvent se produire si l’adresse e-mail n’est pas valide ou n’existe pas. Dans ce cas, Braze marquera l’adresse e-mail de l’utilisateur comme étant invalide et ne tentera pas d’envoyer d’autres e-mails à cette adresse e-mail. Si l’utilisateur change son adresse e-mail, nous recommencerons à lui envoyer des e-mails puisque sa nouvelle adresse sera sans doute valide. Les « soft bounces » sont automatiquement réessayés pendant 72 heures.

## Doublons d’e-mail

Braze vérifie automatiquement et supprime les adresses e-mail en double lors de l’envoi d’une campagne e-mail. De cette façon, un e-mail n’est envoyé qu’une seule fois et est « dédupliqué », pour garantir qu’il n’est pas envoyé plusieurs fois à la même adresse, même si plusieurs profils d’utilisateurs partagent une adresse commune. 

Comme la déduplication se produit lorsque les utilisateurs ciblés sont inclus dans la même répartition, les campagnes déclenchées (à l’exception des campagnes déclenchées par l’ API) peuvent entraîner plusieurs envois à la même adresse e-mail (même dans une période où les utilisateurs peuvent être exclus pour cause rééligibilité) si des utilisateurs différents ayant la même adresse e-mail effectuent l’événement déclencheur à des moments différents. 

{% alert important %}
Si vous envoyez une campagne API via un appel API (à l’exclusion des campagnes déclenchées par l’API) et que plusieurs utilisateurs dans le segment ont la même adresse e-mail, nous l’enverrons à cette adresse autant de fois que vous l’indiquez dans l’appel. C’est parce que nous supposons que les appels API sont faits intentionnellement. 
<br><br>
**Campagnes déclenchées par API**<br>
Notez que les campagnes déclenchées via API peuvent dédupliquer les e-mails ou les envoyer plusieurs fois : cela dépend de la définition du public. <br>-La déduplication se produit s’il y a des e-mails en double dans un segment cible ou des e-mails dupliqués en raison de doublons d’ID dans le [champ destinataire]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) d’un appel déclenché par API. <br>-Des e-mails dupliqués se produisent si vous ciblez directement des ID Utilisateur distincts dans le champ destinataire d’un appel déclenché par l’API. 
{% endalert %}

[22]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
[23]: {{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations
