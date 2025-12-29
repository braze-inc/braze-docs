---
nav_title: "Messages d'erreur courants relatifs à la poussée"
article_title: "Messages d'erreur communs à Push"
page_order: 22
page_type: reference
description: "Cet article couvre les messages d'erreur courants liés au push pour iOS et Android, et vous guide à travers les solutions potentielles."
channel: push
platform:
- iOS
- Android
---

# Messages d'erreur courants relatifs à la poussée

> Cette page présente les messages d'erreur les plus courants pour l'envoi de messages.

{% tabs %}
{% tab Android %} 
### La poussée a rebondi : MismatchSenderId
`MismatchSenderId` indique un échec de l'authentification. Firebase Cloud Messaging (FCM) s'authentifie à l'aide de quelques données clés : l'identifiant de l'expéditeur et la clé API FCM.  L'exactitude de ces deux éléments doit être validée. Pour plus d'informations, consultez la [documentation Android](https://firebase.google.com/docs/cloud-messaging/http-server-ref#error-codes) à ce sujet.

Les défaillances les plus courantes sont les suivantes
- Mauvais [identifiant de l'expéditeur]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase)
- Enregistrement multiple s'ils s'enregistrent auprès d'un autre service push avec un senderID différent

### La poussée a rebondi : InvalidRegistration
`InvalidRegistration` peut se produire lorsqu'un jeton de poussée est malformé. Les défaillances les plus courantes sont les suivantes
- Les gens passent les jetons d'enregistrement de Braze manuellement mais n'appellent pas `getToken()`. Par exemple, ils peuvent transmettre l'intégralité de l'ID de l'instance. Le jeton figurant dans le message d'erreur ressemble à `&#124;ID&#124;1&#124;:[regular token]`.  
- Les gens s'inscrivent auprès de plusieurs services. Nous nous attendons actuellement à ce que les intentions d'enregistrement push arrivent à l'ancienne, de sorte que si les gens s'enregistrent à plusieurs endroits et que nous recevons des intentions d'autres services, nous pouvons obtenir des jetons push malformés.

### La poussée a rebondi : Non Enregistré
`NotRegistered` signifie généralement que l'application a été supprimée de l'appareil (comme notre signal de désinstallation). Cela peut également se produire en cas d'enregistrement multiple et si un deuxième enregistrement invalide le jeton de poussée reçu par Braze.

{% endtab %}
{% tab iOS %}

### La poussée a rebondi : BadToken

L'erreur `BadToken` peut se produire pour plusieurs raisons :
- Le jeton de poussée ne nous est pas envoyé correctement en `[[Appboy sharedInstance] registerPushToken:]`
	- Vérifiez le jeton dans le [journal d'activité des messages.]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) Il doit généralement ressembler à une longue chaîne de caractères et de chiffres (comme `6e407a9be8d07f0cdeb9e714733a89445f57a89ec890d63867c482a483506fa6`). Si ce n'est pas le cas, vérifiez le code impliqué dans l'envoi des erreurs de jetons de poussée de Braze.<br><br>
- Environnement de provisionnement inadapté :
	- Si vous vous enregistrez avec un certificat de développement et que vous essayez d'envoyer avec un certificat de production, vous pouvez voir cette erreur.  
	- Braze ne prend en charge les certificats universels que pour les environnements de production. Le test de push sur des environnements de développement avec un certificat universel ne fonctionnera pas. 
	- Ce rapport envoie des rebonds en production mais pas en développement.<br><br>
- Profil de provisionnement inadapté :
	- Cela peut se produire si votre certificat ne correspond pas à celui qui a été utilisé pour obtenir le jeton. En cas de suspicion, les étapes suivantes sont les suivantes :
		- S'assurer que le certificat de push utilisé pour envoyer des push depuis le tableau de bord de Braze et le profil de provisionnement sont configurés correctement.
		- Recréer la certification APN puis recréer le profil de provisionnement après la configuration du certificat APN sur le site `app_id`. Cela permet parfois de résoudre des problèmes plus visibles.

### La poussée a rebondi : Suppression du service de retour d'information de l'APN

Cela se produit généralement lorsque quelqu'un désinstalle. Chaque nuit, Braze interroge le service de retour d'information de l'APN pour obtenir la liste des jetons non valides. Pour plus d'informations, reportez-vous au document d'Apple intitulé [Communiquer avec les APN](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html).

{% endtab %}
{% endtabs %}
