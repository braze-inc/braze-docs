---
nav_title: E-mails en double
article_title: Les e-mails en double
page_order: 7
page_type: reference
description: "Cet article présente les meilleures pratiques pour gérer les e-mails en double."
channel: email

---

# E-mails en double

> Pour les e-mails dupliqués, si un e-mail se désabonne, les autres profils (jusqu'à 100 profils) avec cette adresse e-mail sont mis à jour pour refléter le même état d'abonnement. Cela s'applique aux désabonnements et aux autres modifications de l'état de l'abonnement, comme l'état de l'abonnement global aux e-mails et les statuts des groupes d'abonnement individuels.

## Mises à jour de l'abonnement par e-mail

Braze vérifie et supprime automatiquement les adresses e-mail en double lors de l'envoi d'une campagne d'e-mailing. De cette manière, un e-mail n'est envoyé qu'une seule fois et est "dédupliqué", ce qui permet de vérifier que le même e-mail n'est pas envoyé plusieurs fois, même si plusieurs profils d'utilisateurs partagent une même adresse.

{% alert tip %}
Assurez-vous de bien connaître les outils que Braze met à votre disposition pour [gérer les abonnements e-mail des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions) et cibler les campagnes sur les utilisateurs ayant un statut d'abonnement particulier. Ces outils sont essentiels pour se conformer aux [lois anti-spam]({{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations).
{% endalert %}

Si les utilisateurs partagent une adresse e-mail, la mise à jour de l'un de ces utilisateurs propagera les modifications de l'abonnement à tous ces utilisateurs (jusqu'à 100 utilisateurs).

## Comportement en matière d'envoi de messages

Étant donné que la déduplication se produit lorsque des utilisateurs ciblés sont inclus dans le même envoi, les campagnes déclenchées (à l'exclusion des campagnes déclenchées par l'API) et les Canvases peuvent donner lieu à plusieurs envois à la même adresse e-mail (même au cours d'une période où les utilisateurs pourraient être exclus en raison de la rééligibilité) si différents utilisateurs dont les e-mails correspondent enregistrent l'événement déclencheur à des moments différents.

## Exemples

Par exemple, si l'utilisateur A et l'utilisateur B partagent l'e-mail `johndoe@example.com` mais que leur profil se trouve dans un fuseau horaire différent, lorsque l'événement déclencheur de la campagne inclut l'envoi dans le fuseau horaire d'un utilisateur, l'e-mail `johndoe@example.com` recevra deux e-mails.

Si vous remplacez l'adresse e-mail de l'utilisateur A par une autre adresse e-mail partagée par l'utilisateur B, l'utilisateur A héritera de l'état d'abonnement de l'utilisateur B, sauf si l'option **Réabonner les utilisateurs lorsqu'ils mettent à jour leur e-mail est** activée.

{% alert important %}
Si vous envoyez une campagne API par le biais d'un appel API (à l'exclusion des campagnes déclenchées par l'API), et que plusieurs utilisateurs sont spécifiés dans l'audience du segment avec la même adresse e-mail, nous l'enverrons à cette adresse autant de fois qu'elle est répertoriée dans l'appel. En effet, nous partons du principe que les appels à l'API sont construits à dessein.
<br><br>
**Campagnes déclenchées par l'API**<br>
Notez que les campagnes déclenchées par l'API déduisent ou envoient des doublons en fonction de l'endroit où l'audience est définie. <br>\- La déduplication peut se produire s'il y a des e-mails en double dans un segment cible ou des e-mails en double en raison d'ID en double dans le [champ du destinataire]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) d'un appel déclenché par l'API. <br>\- Des e-mails seront envoyés en double si vous ciblez directement des ID d'utilisateurs distincts dans le champ du destinataire d'un appel déclenché par l'API.
{% endalert %}
