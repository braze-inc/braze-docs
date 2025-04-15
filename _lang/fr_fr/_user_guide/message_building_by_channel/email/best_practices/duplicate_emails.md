---
nav_title: Doublons d’e-mail
article_title: Doublons d’e-mail
page_order: 7
page_type: reference
description: "Cet article décrit les bonnes pratiques pour gérer les e-mails en double."
channel: email

---

# Doublons d’e-mail

> Pour les e-mails en double, si un e-mail se désabonne, d'autres profils (jusqu'à 100 profils) avec cette adresse e-mail sont mis à jour pour refléter le même état d'abonnement. Cela s'applique aux désabonnements et à d'autres modifications de l'état de l'abonnement, telles que l'état global de l'abonnement par e-mail et les statuts des groupes d'abonnement individuels.

## Mises à jour de l'abonnement par e-mail

Braze vérifie automatiquement et supprime les adresses e-mail en double lors de l’envoi d’une campagne e-mail. De cette façon, un e-mail n'est envoyé qu'une seule fois et est "dédupliqué", ce qui vérifie qu'il ne touche pas la même adresse e-mail plusieurs fois, même si plusieurs profils d'utilisateurs partagent une adresse commune.

{% alert tip %}
Assurez-vous de bien connaître les outils que Braze fournit pour [gérer les abonnements aux e-mails des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions) et cibler les campagnes sur les utilisateurs ayant des états d'abonnement particuliers. Ces outils sont essentiels pour se conformer aux [lois anti-spam]({{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations).
{% endalert %}

Si les utilisateurs partagent une adresse e-mail, la mise à jour de l'un de ces utilisateurs propagera les modifications d'abonnement à ces utilisateurs (jusqu'à 100 utilisateurs).

## Comportement d'envoi de message

Parce que la déduplication se produit lorsque les utilisateurs ciblés sont inclus dans le même envoi, les campagnes déclenchées (à l'exception des campagnes déclenchées par API) et les Canvases peuvent entraîner plusieurs envois à la même adresse e-mail (même pendant une période où les utilisateurs pourraient être exclus en raison de leur rééligibilité) si des utilisateurs différents avec des e-mails correspondants enregistrent l'événement déclencheur à des moments différents.

## Exemples

Par exemple, si l'utilisateur A et l'utilisateur B partagent l'email `johndoe@example.com` mais que leur profil est dans un fuseau horaire différent, lorsque l'événement déclencheur de la campagne inclut l'envoi dans le fuseau horaire d'un utilisateur, l'email `johndoe@example.com` recevra deux emails.

Si vous définissez ou mettez à jour l'adresse e-mail de l'utilisateur A avec une autre adresse e-mail partagée par un utilisateur B existant, l'utilisateur A héritera de l'état d'abonnement qui existe déjà de l'utilisateur B, sauf si le paramètre **Réabonner les utilisateurs lorsqu'ils mettent à jour leur e-mail** est activé.

{% alert important %}
Si vous envoyez une campagne API via un appel API (à l’exclusion des campagnes déclenchées par l’API) et que plusieurs utilisateurs dans le segment ont la même adresse e-mail, nous l’enverrons à cette adresse autant de fois que vous l’indiquez dans l’appel. C’est parce que nous supposons que les appels API sont faits intentionnellement.
<br><br>
**Campagnes déclenchées par API**<br>
Notez que les campagnes déclenchées via API peuvent dédupliquer les e-mails ou les envoyer plusieurs fois en fonction de la zone où votre audience est définie. <br>La déduplication peut se produire s'il existe des e-mails en double dans un segment cible ou des e-mails en double en raison d'ID en double dans le [champ destinataire]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) d'un appel déclenché par l'API. <br>-Des e-mails dupliqués se produisent si vous ciblez directement des ID Utilisateur distincts dans le champ destinataire d’un appel déclenché par l’API.
{% endalert %}
