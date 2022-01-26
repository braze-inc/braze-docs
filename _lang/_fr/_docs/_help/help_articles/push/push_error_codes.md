---
nav_title: Messages d'erreurs Push courants
article_title: Messages d'erreurs Push courants
page_order: 0
page_type: Solution
description: "Cet article d'aide couvre les messages d'erreur courants liés à la Push pour iOS et Android, et vous guide à travers des solutions potentielles."
channel: Pousser
platform:
  - iOS
  - Android
---

# Messages d'erreurs de push courants

Consultez les messages d'erreur courants ci-dessous :

{% tabs %}
{% tab Android %}
### Push bounce: MismatchSenderId
`MismatchSenderId` indique un échec d'authentification.  Google Cloud Messaging (GCM) s'authentifie avec quelques éléments clés de données : senderID et GCM API key.  Ils devraient tous deux être validés pour exactitude. Pour plus d'informations, consultez la [documentation publique](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html) à propos de ce problème.

Les échecs courants peuvent inclure :
- Mauvais [expéditeurID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase)
- Inscription multiple s'ils s'enregistrent avec un autre service push avec un ID d'expéditeur différent

### Envoi rebondi : Inscription invalidée
`Invalidation de l'enregistrement` peut se produire lorsqu'un jeton de push est malformé. Les échecs courants peuvent inclure quand :
- Les gens passent manuellement les jetons d'enregistrement de Braze, mais n'appelez pas `getToken()`. Par exemple, ils peuvent passer l'ID de l'instance entière. Le jeton dans le message d'erreur ressemble à `&#124;ID&#124;1&#124;:[jeton ordinaire]`.
- Les gens s'inscrivent à plusieurs services. Nous attendons actuellement que les intentions d'inscription "push" arrivent à l'ancienne, donc si les gens s'enregistrent à plusieurs endroits et que nous attrapons des intentions d'autres services, nous pouvons obtenir des jetons de push mal formés.

### Push bounced: Non enregistré
`Non enregistré` signifie généralement que l'application a été supprimée de l'appareil (i.e. Signal de Braze pour Désinstaller). Cela peut également se produire si plusieurs inscriptions se produisent et qu'une seconde inscription invalide le jeton push reçu par Braze.

{% endtab %}
{% tab iOS %}

### Push bounced: Erreur lors de l'envoi vers un mauvais jeton push

Cette erreur peut survenir pour plusieurs raisons :
- Le jeton de push ne nous est pas envoyé correctement dans `[[Appboy sharedInstance] registerPushToken:]`
    - Vérifiez le jeton dans le **Journal d'activité des messages**. Il devrait en général ressembler à une longue chaîne de lettres et de chiffres. (ex: `6e407a9be8d07f0cdeb9e714733a89445f57a89ec890d63867c482a483506fa6`) Si ce n'est pas le cas, vérifiez le code impliqué dans l'envoi d'erreurs de jeton push de Braze.<br><br>
- Environnement de provisioning mal assorti :
    - Si vous vous enregistrez avec un certificat de développement et que vous essayez d'envoyer avec un certificat de production, vous pouvez voir cette erreur.
    - Braze ne prend en charge que les certificats universels pour les environnements de production. Tester Push sur les environnements de développement avec un certificat universel ne fonctionnera pas.
    - Ce rapport envoie des rebondissements en production mais pas en développement.<br><br>
- Profil de provisioning mal assorti :
    - Cela peut se produire si votre certificat ne correspond pas à celui qui a été utilisé pour obtenir le jeton. Si cela est suspect, les prochaines étapes incluent :
        - Veiller à ce que le certificat de poussée soit utilisé pour envoyer des push depuis le tableau de bord Braze et le profil de provisioning soient configurés correctement.
        - Recréer la certification APNS puis recréer le profil de provisioning une fois que le certificat APNS est configuré sur l' `app_id`. Cela peut parfois résoudre des problèmes plus visibles.

### Push bounce: service de feedback APNS supprimé

Cela se produit généralement lorsque quelqu'un désinstalle. Braze interroge le service de rétroaction APNS chaque nuit pour obtenir une liste de jetons non valides. Pour plus d'informations, reportez-vous à l'article [d'Apple Communication avec les APN](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html).


{% endtab %}
{% endtabs %}

_Dernière mise à jour le 24 janvier 2021_
