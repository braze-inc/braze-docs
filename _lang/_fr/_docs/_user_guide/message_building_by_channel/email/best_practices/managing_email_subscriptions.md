---
nav_title: Gestion des abonnements par e-mail
article_title: Gestion des abonnements par e-mail
page_order: 7
page_type: Référence
description: "Cet article couvre les meilleures pratiques de gestion des abonnements aux e-mails, tels que la désinscription, l'invalidité ou les courriels en double."
channel: Email
---
   
# Gestion des abonnements aux e-mails

Assurez-vous d'être familier avec les outils que Braze fournit pour la gestion [des abonnements aux emails des utilisateurs et des campagnes de ciblage sur les utilisateurs avec des états d'abonnement particuliers][22]. Ces outils sont essentiels au respect des [lois anti-spam][23].

## Adresses e-mail désabonnées

Braze désabonnera automatiquement tout utilisateur qui se désabonnera manuellement de votre e-mail via un pied de page personnalisé ou marquera un email comme spam. Ces utilisateurs ne seront pas ciblés par des e-mails futurs. Pour en savoir plus sur la façon de configurer votre pied de page personnalisé, visitez cette [documentation]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions).

Si un utilisateur se désabonne et change ultérieurement son e-mail, son nouvel e-mail sera également désabonné. En d'autres termes, une fois qu'un identifiant d'utilisateur externe est associé à une désinscription, les futures adresses e-mail pour cet identifiant d'utilisateur seront également désabonnées.

## Bounces et e-mails non valides

Les rebonds difficiles peuvent se produire si l'email est invalide ou n'existe pas. Dans ce cas, Braze marquera l'adresse e-mail de l'utilisateur comme non valide et n'essaiera pas d'envoyer d'autres courriels à cette adresse e-mail. Si cet utilisateur change son adresse e-mail, alors nous recommencerons à leur envoyer des courriels car leur nouvel e-mail peut être valide. Les rejets de Soft Bounces sont automatiquement rétentés pendant 72 heures.

## E-mails en double

Braze vérifie automatiquement et supprime les adresses e-mail en double lorsqu'une campagne de courriel est envoyée. De cette façon, un email n'est envoyé qu'une seule fois et est "dupé" qui assure qu'il ne frappe pas le même email plusieurs fois, même si plusieurs profils d'utilisateurs partagent une adresse commune.

Parce que la déduplication se produit lorsque les utilisateurs ciblés sont inclus dans le même expédition, les campagnes déclenchées (excluant les campagnes déclenchées par l'API, voir ci-dessous) peut entraîner des envois multiples à la même adresse de courriel (même dans un délai où les utilisateurs pourraient être exclus en raison de leur rééligibilité) si des utilisateurs différents avec des emails correspondants enregistrent l'événement de déclenchement à différents moments.

{% alert important %}
Si vous envoyez une campagne API via un appel API (excluant les campagnes déclenchées par l'API), et plusieurs utilisateurs sont spécifiés dans le segment public avec la même adresse e-mail, nous l'enverrons à cette adresse car plusieurs fois sont listés dans l'appel. C'est parce que nous supposons que les appels API sont construits de manière ciblée. <br><br> __Campagnes déclenchées par l'API__<br> Notez que les campagnes déclenchées par l'API vont déduper ou envoyer des doublons __selon l'endroit où l'audience est définie__. <br>- __Deduping__ se produira s'il y a des e-mails en double dans un segment cible ou des e-mails en double en raison d'IDs en double dans le [champ destinataire]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) d'un appel déclenché par l'API. <br>- __E-mails dupliqués__ se produira si vous ciblez directement des identifiants utilisateur séparés dans le [champ destinataire]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) d'un appel déclenché par API.
{% endalert %}

[22]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
[23]: {{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations
