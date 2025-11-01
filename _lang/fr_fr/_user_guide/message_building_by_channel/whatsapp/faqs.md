---
nav_title: FAQ
article_title: FAQ sur WhatsApp
page_order: 10
description: "Cet article aborde certaines des questions les plus fréquemment posées lors de l'implémentation des campagnes WhatsApp."
page_type: FAQ
channel:
  - WhatsApp

---

# Questions fréquemment posées

> Sur cette page, nous tenterons de répondre à vos questions les plus pointues sur WhatsApp !<br><br>Cette FAQ n'a pas pour but de fournir des conseils juridiques et ne peut être considérée comme telle. L'utilisation du canal WhatsApp est soumise à des exigences spécifiques de Meta Platforms, Inc. Pour vous assurer que vous utilisez le canal WhatsApp conformément à toutes les exigences applicables et à toutes les lois auxquelles vous pouvez être spécifiquement soumis, vous devez demander l'avis de votre conseiller juridique.

## Thèmes de la FAQ
- [Comptes professionnels WhatsApp](#whatsapp-business-accounts)
- [Numéro de téléphone du compte business de WhatsApp](#whatsapp-business-account-phone-numbers)
- [Gestion des abonnements et des demandes d'adhésion](#opt-in-and-subscription-management) 
- [Limites de l'envoi de messages](#messaging-limits) 
- [Modèles WhatsApp](#whatsapp-templates)
- [Livrabilité](#deliverability) 
- [Divers](#miscellaneous)

### Comptes professionnels WhatsApp 

#### Comment créer un compte professionnel WhatsApp ? 
Nous vous recommandons de créer votre compte professionnel WhatsApp (WABA) via le flux d'inscription intégré dans le tableau de bord de Braze. 

#### J'ai déjà un compte professionnel Meta. Ai-je toujours besoin d'un compte professionnel WhatsApp ? 
Oui, vous devez toujours créer un compte professionnel WhatsApp. Nous vous recommandons de [placer votre WABA sous votre compte commercial Meta principal.]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/) 

#### Comment puis-je accéder à mon compte professionnel WhatsApp ? 
Après avoir complété le flux d'inscription intégré, vous pouvez accéder à votre compte sur business.facebook.com en naviguant vers la [section WhatsApp.](https://business.facebook.com/wa/manage/home) 

#### Puis-je connecter plusieurs WABA à Braze ? 
Oui, vous pouvez ajouter jusqu'à 10 comptes WhatsApp Business par espace de travail, et chaque compte business peut être imbriqué sous un gestionnaire de compte Meta Business différent.

Diagramme de l'écosystème Braze et WhatsApp, montrant comment les espaces de travail et les comptes WhatsApp Business se connectent les uns aux autres : vous pouvez connecter un groupe d'abonnement à un numéro de téléphone, plusieurs comptes WhatsApp Business à un espace de travail, et un espace de travail à plusieurs portefeuilles Meta Business.]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %}) 

### Numéros de téléphone des comptes business de WhatsApp 

#### Ai-je besoin d'un numéro de téléphone pour mon compte WhatsApp business ? 
Oui, vous avez besoin d'un numéro auquel vous avez accès. Il vous sera demandé de vérifier votre numéro de téléphone avec l'authentification à 2 facteurs lorsque vous passerez par le flux d'inscription intégré. Le numéro de téléphone ne peut pas être utilisé pour d'autres comptes WhatsApp (professionnels ou personnels).

#### Quels types de numéros de téléphone sont pris en charge par WhatsApp ? 
Pour plus d'informations, reportez-vous aux exigences de Meta en matière de [numéros de téléphone](https://developers.facebook.com/docs/whatsapp/phone-numbers). 

#### Puis-je utiliser un seul numéro de téléphone pour plusieurs WABA ? 
Non. Un numéro de téléphone ne peut pas être partagé entre plusieurs WABA. 

#### Ai-je besoin d'un type de numéro de téléphone spécifique pour envoyer des messages à des pays spécifiques ? 
Non. WhatsApp vous permet d'envoyer des messages aux utilisateurs finaux à partir de n'importe quel numéro de téléphone pris en charge dans n'importe quel pays. Pour plus d'informations, reportez-vous aux exigences de Meta en matière de [numéros de téléphone](https://developers.facebook.com/docs/whatsapp/phone-numbers). 

#### Dois-je utiliser un numéro de téléphone spécifique pour envoyer des messages vers certains pays ?
Non. Avec WhatsApp, n'importe quel numéro de téléphone pris en charge peut envoyer des messages à des utilisateurs finaux dans n'importe quel pays pris en charge.

### Gestion des abonnements et des demandes d'adhésion 

#### Dois-je recueillir un abonnement pour envoyer des messages marketing aux utilisateurs finaux sur WhatsApp ? 
Oui, WhatsApp exige des entreprises qu'elles [recueillent un consentement explicite (opt-in)](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) pour envoyer des messages marketing aux utilisateurs finaux.

#### Puis-je envoyer de manière proactive des messages aux utilisateurs finaux sur WhatsApp pour recueillir leur consentement par abonnement ? 
Si vous choisissez d'envoyer des messages proactifs aux utilisateurs finaux, votre premier message à l'initiative de l'entreprise doit demander à l'utilisateur s'il souhaite recevoir des messages marketing de votre entreprise et doit être conforme aux exigences de Meta en matière d' [obtention de l'abonnement](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). Gardez à l'esprit que WhatsApp surveillera la réputation de votre entreprise sur le canal, la meilleure pratique recommandée est donc d'être explicite avec les utilisateurs finaux et de n'envoyer que des messages qu'ils ont indiqué vouloir recevoir.
 
#### Dois-je collecter le numéro de téléphone de l'utilisateur final lorsque je recueille son abonnement ? 
Vous devez disposer du numéro de téléphone de l'utilisateur final dans son profil Braze pour lui envoyer des messages. 
- Si vous disposez déjà de leur numéro, il n'est pas nécessaire de le collecter lors de l'abonnement. 
- Si vous ne disposez pas du numéro de l'utilisateur final, votre méthode d'abonnement doit inclure la capture du numéro de téléphone. 

#### Comment mettre à jour l'état de l'abonnement des utilisateurs finals qui se sont abonnés ? 
La gestion des abonnements du canal WhatsApp fonctionne de manière similaire à celle des autres canaux de Braze. Pour plus d'informations, reportez-vous à la section [Gestion des abonnements des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/).  

#### Si je dispose déjà d'une liste d'utilisateurs qui ont choisi de recevoir des messages marketing sur WhatsApp, comment puis-je mettre à jour leur statut d'abonnement dans Braze ? 
Vous pouvez mettre à jour leur statut d'abonnement via l'[importation d'utilisateurs]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#importing-custom-data). 

#### Quelles méthodes dois-je utiliser pour collecter les abonnements ? 
Braze recommande de se référer aux [lignes directrices de Meta pour les méthodes d'abonnement](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) afin de rester en conformité. Consultez la ressource suivante pour obtenir des [idées et des suggestions sur les canaux et les abonnements de](https://docs.google.com/document/d/1rNKnKN2oIn-e9bXdYEvnwdlzlCsEOKs-xREcdVvPBE8/edit) Braze.

#### Le double abonnement est-il nécessaire pour WhatsApp ? 
Non, le double abonnement n'est pas nécessaire. 

#### Comment mes utilisateurs peuvent-ils s'abonner aux messages WhatsApp ? 
Vos utilisateurs peuvent se désabonner de deux manières :
1. Configurez un message WhatsApp entrant avec un mot d'exclusion spécifique et utilisez un webhook pour mettre à jour l'état de l'abonnement de l'utilisateur.
2. Ajoutez une réponse rapide d'abonnement dans le modèle WhatsApp, avec un webhook correspondant à mettre à jour. 

### Limites de l'envoi de messages 

#### Quelles sont les limites de l'envoi des messages ? 
Les limites d'envoi des messages sont un concept de renforcement de l'intégrité de WhatsApp. Ils déterminent le nombre maximum de conversations initiées par les entreprises que chaque numéro de téléphone peut entamer au cours d'une période mobile de 24 heures. Il existe quatre niveaux de limites d'envoi de messages : 1k, 10k, 100k et illimité.

#### Comment augmenter ma limite d'envoi de messages ? 
WhatsApp augmentera votre limite d'envoi de messages si vous remplissez les conditions suivantes :
1. L'[état du numéro de téléphone](https://www.facebook.com/business/help/896873687365001) est **connecté** 
2. La [qualité des numéros de téléphone](https://www.facebook.com/business/help/896873687365001) est **moyenne** ou **élevée**
3. Au cours des sept derniers jours, vous avez engagé X conversations ou plus avec des utilisateurs uniques, X étant votre limite actuelle d'envoi de messages divisée par 2. 

Ainsi, pour passer de 100k à illimité, vous devez envoyer au moins 50 000 conversations à l'initiative des entreprises sur une période de 7 jours. 

#### Combien de temps faut-il pour augmenter mes limites d'envoi de messages ? 
Si toutes les conditions précédentes sont remplies, vous pouvez faire passer votre limite d'envoi de messages de 1k à illimité en 4 jours. 

#### Où puis-je voir ma limite d'envoi de messages actuelle ? 
Vous pouvez vérifier vos limites d'envoi de messages actuelles dans le **gestionnaire WhatsApp > tableau de bord aperçu > onglet Informations.**  

#### Que se passe-t-il si j'essaie d'envoyer des messages alors que j'ai déjà atteint ma limite d'envoi de messages ?
Si vous essayez d'envoyer une campagne ou un canvas à un nombre d'utilisateurs uniques supérieur à votre limite actuelle, les messages ne seront pas envoyés. Braze continuera à tenter de renvoyer les messages si/quand votre limite d'envoi de messages augmente, et ce pendant une journée au maximum. 

#### Ma limite d'envoi de messages peut-elle diminuer ?
Oui, si l'évaluation de la qualité de votre numéro de téléphone tombe trop bas, vous risquez de voir WhatsApp diminuer votre limite de messages. Braze vous recommande de vous abonner et d'être informé des mises à jour de WhatsApp relatives à la qualité, notamment les mises à jour du statut de votre numéro de téléphone et du niveau de limite d'envoi des messages. Vous pouvez vous abonner aux notifications directement dans le tableau de bord du gestionnaire WhatsApp. 

#### Quelle est la limite de débit de Meta ?
Meta a sa propre limite de débit, distincte de la limite d'envoi de messages de WABA. La limite par défaut prise en charge par l'API en nuage est de 80 messages par seconde. Si vous pensez que vos campagnes dépasseront cette limite, vous pouvez [demander](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/#throughput) à ce qu'elle soit augmentée. Meta vous recommande de soumettre cette demande au moins trois jours avant l'envoi de la campagne.

### Modèles WhatsApp 

#### Qu'est-ce qu'un modèle WhatsApp ? 
WhatsApp exige que tous les messages initiés par les entreprises commencent par utiliser un modèle approuvé. Le modèle comprend le texte du message, ainsi que des médias enrichis optionnels tels que des images, des appels à l'action et des boutons de réponse rapide. Une fois que WhatsApp a approuvé les modèles, ceux-ci peuvent être utilisés pour composer un message WhatsApp dans Braze. 

#### Où puis-je créer, modifier et gérer mes modèles WhatsApp ? 
Vous créerez, modifierez, gérerez et soumettrez des modèles pour approbation directement dans le gestionnaire WhatsApp. Une fois que votre WABA est connecté à Braze, vous verrez tous vos modèles dans le tableau de bord avec un indicateur d'état. Si un modèle est rejeté, vous le soumettrez à nouveau directement par l'intermédiaire du gestionnaire WhatsApp. **Les modèles ne peuvent pas être créés ou modifiés directement dans Braze.**

#### Combien de temps faut-il à WhatsApp pour examiner une demande de modèle ? 
La procédure d'approbation peut prendre jusqu'à 24 heures, mais les modèles sont souvent traités en quelques heures ou minutes. 

#### Combien de modèles puis-je avoir à la fois ? 
La limite de votre modèle de message dépend du statut de vérification de votre entreprise. Vous pouvez vérifier votre limite sur la page **Gestionnaire WhatsApp > Modèles de messages.**  

#### Comment personnaliser les modèles modèles et médias dans Braze ? 
WhatsApp permet d'insérer des paramètres variables dans les modèles de messages. Les messages ne peuvent pas commencer ou se terminer par un paramètre variable. Les paramètres variables peuvent être alimentés par la logique liquide de la plateforme Braze. Reportez-vous à la [composition d'un message WhatsApp dans Braze]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#step-2-compose-your-whatsapp-message) pour en savoir plus sur les paramètres variables. 

#### Mon modèle a été rejeté. Braze peut-il m'aider à la faire approuver ? 
L'équipe de Braze n'a pas de visibilité sur les rejets de modèles. Vous devez travailler directement avec votre gestionnaire WhatsApp Business pour modifier et soumettre à nouveau le modèle. Veillez à fournir un modèle type si nécessaire. Vérifiez que votre modèle respecte les politiques [commerciales](https://www.whatsapp.com/legal/commerce-policy/?fbclid=IwAR3bzN3LTZ-7kO-wnO7X3smtPKGy0asxaFod-U1Ub8B9JUpnrfy1_y7LpAQ) de Meta.

#### Le média enrichi peut-il être ciblé ou personnalisé dans Braze ? 
Les images peuvent être téléchargées à partir de la bibliothèque multimédia mais ne peuvent pas être ciblées de manière dynamique. Pour les URL, la dernière partie du lien peut être remplie dynamiquement à l'aide de Liquid. 

### Livrabilité 

#### Pourquoi un message ne serait-il pas envoyé ? 
Il existe plusieurs raisons pour lesquelles un message n'est pas envoyé, notamment des problèmes de réseau ou la mise hors tension de l'appareil. 

#### Si un message n'est pas envoyé, serai-je facturé ? 
Non. Si un message n'est pas envoyé, vous ne serez pas facturé. 

#### Que se passe-t-il si un utilisateur final bloque mon activité ? 
Si un utilisateur final bloque votre entreprise, les messages ultérieurs que vous tenterez d'envoyer ne seront pas délivrés et vous ne serez pas facturé. 

#### Que se passe-t-il si un utilisateur final signale un message ? 
Si un utilisateur final signale un message, vous pouvez toujours lui envoyer des messages ultérieurs. Toutefois, le signalement peut avoir une incidence sur la qualité de votre classement sur la chaîne. 

#### Si un utilisateur final bloque ou signale mon entreprise, son statut d'abonnement sera-t-il mis à jour dans Braze ? 
Non. Leur statut d'abonnement à Braze ne sera pas mis à jour. 

### Divers

#### Braze prend-il en charge les cas d'utilisation d'assistance à la clientèle tels que les chatbots et le chat assisté par un humain pour WhatsApp ? 
Nous ne prenons pas en charge les chatbots ou le chat assisté par un humain au sein de Braze ou par le biais d'intégrations directes. 

Si vous utilisez déjà WhatsApp comme canal d'assistance à la clientèle, nous vous recommandons de conserver votre configuration actuelle et de créer un nouveau WABA via Braze pour l'envoi de messages marketing. Cette WABA nécessitera un nouveau numéro de téléphone. 

#### Comment puis-je "combler le fossé" entre mes messages d'assistance à la clientèle et mes messages marketing via Braze ? 
Vous pouvez utiliser les propriétés de WhatsApp Liquid pour transférer le contenu des messages WhatsApp entrants (y compris le corps du message et les URL des médias) de Braze vers d'autres plateformes, y compris tout outil de communication individualisée. Pour plus de détails, consultez nos [tags de personnalisation soutenus]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/). 

Pour envoyer des informations dans Braze, par exemple pour indiquer qu'un utilisateur est dans une conversation d'assistance active, vous pouvez enregistrer un attribut personnalisé (tel qu'un booléen "a un chat d'assistance existant = vrai/faux") et l'utiliser comme critères de segmentation dans leurs campagnes marketing. Vous pouvez également créer un lien profond entre deux fils de discussion pour diriger les utilisateurs vers le fil d'assistance à partir du fil marketing et inversement. 

#### Braze conserve-t-il les réponses des utilisateurs ? 
Les messages ne sont stockés que le temps nécessaire à leur traitement. Pour accéder aux messages des utilisateurs, utilisez Currents. 

#### Comment les numéros de téléphone des utilisateurs doivent-ils être stockés dans Braze ? 
Les numéros de téléphone des utilisateurs doivent être enregistrés au [formatE.164 ]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/#formatting).

#### Quels sont les modèles et médias pris en charge dans les modèles WhatsApp ? 
Vous pouvez ajouter des images, des appels à l'action (URL ou numéro de téléphone) et des boutons de réponse rapide aux modèles WhatsApp. Vous pouvez ajouter ces éléments lorsque vous créez des modèles directement dans WhatsApp. 

#### Puis-je importer des numéros de téléphone d'utilisateurs ? 
Oui. Vous pouvez [importer des numéros de téléphone d'utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/). 

#### Qu'est-ce que la vérification des entreprises ? 
La vérification de l'entreprise est un concept WhatsApp utilisé pour s'assurer que la marque est une entreprise légitime. Elle peut être complétée dans le gestionnaire WhatsApp. La vérification des entreprises est également nécessaire pour l'envoi de messages. Sans vérification de l'entreprise, les utilisateurs ne peuvent envoyer que 250 utilisateurs finaux uniques par période de 24 heures. 

#### Qu'est-ce qu'un compte professionnel officiel ? 
OBA vous donne la coche verte à côté de votre nom d'affichage et est facultatif. Vous pouvez demander un compte professionnel officiel après avoir effectué les vérifications nécessaires. Notez que la vérification commerciale et un compte commercial officiel sont des concepts WhatsApp différents. 

#### Quels sont les indicateurs disponibles dans le tableau de bord de Braze ? 
Vous pouvez voir les destinataires uniques, les envois, les livraisons, les lectures et les échecs dans le tableau de bord de Braze. Notez que les reçus de lecture de l'utilisateur final doivent être activés pour que Braze suive les lectures. Vous pouvez également mettre en place des événements de conversion pour suivre les performances de la campagne, comme pour les autres canaux. 

#### Qu'est-ce qu'une conversation WhatsApp ? 
WhatsApp est un canal axé sur l'envoi de messages dans les deux sens et s'ancre donc sur les conversions (au lieu du nombre de messages individuels). Une conversion est un fil de 24 heures entre une entreprise et un utilisateur final.

- **Conversation à l'initiative de l'entreprise**: Une conversion dans laquelle l'utilisateur commence par envoyer un modèle de message approuvé à l'utilisateur final. Dès que l'entreprise envoie un message, elle entame la fenêtre de 24 heures.
- **Conversation initiée par l'utilisateur**: Une conversion où l'utilisateur final envoie un message à l'entreprise. Lorsque l'entreprise envoie un message en réponse, la fenêtre de 24 heures commence.

#### Quels sont les facteurs qui influencent l'évaluation de la qualité d'un numéro de téléphone et que se passe-t-il lorsque mon évaluation de la qualité devient trop basse ? 
Les facteurs qui influencent l'évaluation de la qualité des numéros de téléphone sont notamment le blocage d'une entreprise par un utilisateur final (et les raisons qu'il donne lorsqu'il bloque une entreprise) et le signalement d'une entreprise par un utilisateur final. 

Lorsque l'évaluation de la qualité est faible, le statut du numéro de téléphone passe de **Connecté** à **Marqué**. Si la qualité ne s'améliore pas au bout de sept jours, le statut redevient " **Connecté".** Toutefois, la limite d'envoi de messages diminuera jusqu'au niveau suivant. Par exemple, un numéro de téléphone qui avait une limite de 100 000 messages a maintenant une limite de 10 000 messages.
