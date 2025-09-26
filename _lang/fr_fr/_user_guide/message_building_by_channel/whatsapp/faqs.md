---
nav_title: FAQ
article_title: FAQ WhatsApp
page_order: 80
description: "Cet article aborde certaines des questions les plus fréquemment posées lors de la configuration des campagnes WhatsApp."
page_type: FAQ
channel:
  - WhatsApp

---

# Foire aux questions

> Sur cette page, nous allons essayer de répondre à vos questions les plus exigeantes concernant WhatsApp !<br><br>Le présent article n’est pas destiné à fournir, et ne peut être considéré comme fournissant des conseils juridiques. L’utilisation du canal WhatsApp est soumise à des exigences spécifiques de Meta Platforms, Inc. Pour vous assurer que vous utilisez le canal WhatsApp conformément à toutes les exigences applicables et à toutes les lois auxquelles vous pouvez spécifiquement être soumis, vous devez demander conseil à votre conseiller juridique.

## Rubriques de la FAQ
- [Comptes WhatsApp Business](#whatsapp-business-accounts)
- [Numéro de téléphone du compte business de WhatsApp](#whatsapp-business-account-phone-numbers)
- [Abonnements et gestion des abonnements](#opt-in-and-subscription-management) 
- [Limites d’envoi de messages](#messaging-limits) 
- [Modèles WhatsApp](#whatsapp-templates)
- [Livrabilité](#deliverability) 
- [Divers](#miscellaneous)

### Comptes WhatsApp Business 

#### Comment créer un compte professionnel WhatsApp ? 
Nous vous recommandons de créer votre compte professionnel WhatsApp (WABA) via le flux d’inscription intégré dans le tableau de bord de Braze. 

#### J’ai déjà un compte commercial Meta. Ai-je encore besoin d’un compte professionnel WhatsApp ? 
Oui, vous devez toujours créer un compte professionnel WhatsApp. Nous vous recommandons de [placer votre WABA sous votre compte commercial Meta principal]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/). 

#### Comment puis-je accéder à mon compte professionnel WhatsApp ? 
Après avoir complété le flux d'inscription intégré, vous pouvez accéder à votre compte sur business.facebook.com en naviguant vers la [section WhatsApp.](https://business.facebook.com/wa/manage/home) 

#### Puis-je connecter plusieurs WABAs à Braze ? 
Oui, vous pouvez ajouter jusqu'à 10 comptes WhatsApp Business par espace de travail, et chaque compte business peut être imbriqué sous un gestionnaire de compte Meta Business différent.

![Diagramme de l'écosystème Braze et WhatsApp, montrant comment les espaces de travail et les comptes WhatsApp Business se connectent les uns aux autres : vous pouvez connecter un groupe d'abonnement à un numéro de téléphone, plusieurs comptes WhatsApp Business à un espace de travail, et un espace de travail à plusieurs portefeuilles Meta Business.]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %}). 

### Numéros de téléphone du compte professionnel WhatsApp 

#### Ai-je besoin d’un numéro de téléphone pour mon compte professionnel WhatsApp ? 
Oui, vous avez besoin d’un numéro auquel vous avez accès. Il vous sera demandé de vérifier votre numéro de téléphone avec l’authentification à deux facteurs lorsque vous parcourez le flux d’inscription intégré. Le numéro de téléphone ne peut pas être utilisé pour d’autres comptes WhatsApp (professionnels ou personnels).

#### Quels types de numéros de téléphone sont pris en charge par WhatsApp ? 
Pour plus d'informations, reportez-vous aux exigences de Meta en matière de [numéros de téléphone](https://developers.facebook.com/docs/whatsapp/phone-numbers). 

#### Puis-je utiliser un numéro de téléphone sur plusieurs WABAs ? 
Non. Un numéro de téléphone ne peut pas être partagé dans plusieurs WABAs. 

#### Ai-je besoin d’un type spécifique de numéro de téléphone pour envoyer des messages à des pays spécifiques ? 
Non. WhatsApp vous permet d’envoyer des messages aux utilisateurs finaux depuis n’importe quel numéro de téléphone pris en charge dans n’importe quel pays. Pour plus d'informations, reportez-vous aux exigences de Meta en matière de [numéros de téléphone](https://developers.facebook.com/docs/whatsapp/phone-numbers). 

#### Dois-je utiliser un numéro de téléphone spécifique à un pays pour envoyer dans certains pays ?
Non. Avec WhatsApp, tout numéro de téléphone pris en charge peut être envoyé aux utilisateurs finaux dans n’importe quel pays pris en charge.

### Abonnements et gestion des abonnements 

#### Dois-je prendre un abonnement pour envoyer des messages marketing aux utilisateurs finaux sur WhatsApp ? 
Oui, WhatsApp exige des entreprises qu'elles [recueillent un consentement explicite (opt-in)](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) pour envoyer des messages marketing aux utilisateurs finaux.

#### Puis-je communiquer de manière proactive avec les utilisateurs finaux sur WhatsApp pour recueillir le consentement à prendre un abonnement ? 
Si vous choisissez d'envoyer des messages proactifs aux utilisateurs finaux, votre premier message à l'initiative de l'entreprise doit demander à l'utilisateur s'il souhaite recevoir des messages marketing de votre entreprise et doit être conforme aux exigences de Meta en matière d' [obtention de l'abonnement](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). Gardez à l’esprit que WhatsApp surveillera votre réputation d’entreprise sur le canal, de sorte que la meilleure pratique recommandée soit explicite avec les utilisateurs finaux et n’envoie que des messages qu’ils ont indiqués qu’ils souhaitent recevoir.
 
#### Dois-je recueillir le numéro de téléphone de l’utilisateur final lorsque je récupère un abonnement ? 
Vous devez avoir le numéro de téléphone des utilisateurs finaux sur le profil Braze pour les envoyer. 
- Si vous avez déjà leur numéro, vous n’avez pas besoin de le récupérer lors de leur abonnement. 
- Si vous n’avez pas le numéro d’utilisateur final, votre méthode d’abonnement doit inclure la capture du numéro de téléphone. 

#### Comment mettre à jour le statut de souscription des utilisateurs finaux qui s’abonnent ? 
La gestion des abonnements de WhatsApp Channel fonctionne de la même manière que dans les autres canaux de Braze. Pour plus d'informations, reportez-vous à la section [Gestion des abonnements des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/).  

#### Si j’ai déjà une liste d’utilisateurs qui ont choisi de recevoir des messages marketing sur WhatsApp, comment puis-je mettre à jour leur statut d’abonnement à Braze ? 
Vous pouvez mettre à jour leur statut d'abonnement via l'[importation d'utilisateurs]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#importing-custom-data). 

#### Quelles méthodes dois-je utiliser pour recueillir des compléments ? 
Braze recommande de se référer aux [lignes directrices de Meta pour les méthodes d'abonnement](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) afin de rester en conformité. Consultez la ressource suivante pour obtenir [des idées et des suggestions sur les canaux et les abonnements](https://docs.google.com/document/d/1rNKnKN2oIn-e9bXdYEvnwdlzlCsEOKs-xREcdVvPBE8/edit) de la part de Braze.

#### L’abonnement double est-il requis pour WhatsApp ? 
Non, il n’est pas nécessaire d’effectuer un double abonnement. 

#### Comment mes utilisateurs peuvent-ils se désabonner des messages WhatsApp ? 
Vos utilisateurs peuvent se désabonner de deux manières :
1. Configurez un message WhatsApp entrant avec un mot de désabonnement spécifique et utilisez un webhook pour mettre à jour le statut de l’abonnement utilisateur.
2. Ajoutez une réponse rapide de désabonnement au modèle WhatsApp, avec un webhook correspondant à mettre à jour. 

### Limites d’envoi de messages 

#### Quelles sont les limites d’envoi de messages ? 
Les limites d’envois de messages sont un concept de renforcement de l’intégrité WhatsApp. Ils déterminent le nombre maximum de conversations initiées par les entreprises, chaque numéro de téléphone pouvant commencer par une période de 24 heures. Il existe quatre niveaux de limites d'envoi de messages : 1k, 10k, 100k et illimité.

#### Comment puis-je augmenter ma limite d’envoi de messages ? 
WhatsApp augmentera votre limite d’envoi de messages si vous remplissez les conditions suivantes :
1. L'[état du numéro de téléphone](https://www.facebook.com/business/help/896873687365001) est **connecté** 
2. La [qualité des numéros de téléphone](https://www.facebook.com/business/help/896873687365001) est **moyenne** ou **élevée**
3. Au cours des sept derniers jours, vous avez initié X ou plus avec des utilisateurs uniques, où X correspond à votre limite d’envoi de messages actuelle divisée par 2 

Donc, pour passer de 100 000 à illimité, vous devez envoyer au moins 50 000 conversations initiées par l’entreprise sur une période de 7 jours. 

#### Combien de temps faut-il pour augmenter mes limites d’envoi de messages ? 
Si toutes les conditions précédentes sont remplies, vous pouvez augmenter votre limite d’envoi de messages de 1 000 à illimité en 4 jours. 

#### Où puis-je voir ma limite d’envoi de messages actuelle ? 
Vous pouvez vérifier vos limites d'envoi de messages actuelles dans le **gestionnaire WhatsApp > tableau de bord aperçu > onglet Informations.**  

#### Que se passe-t-il si je tente d’envoyer des messages lorsque j’ai déjà atteint ma limite d’envoi de messages ?
Si vous essayez d’envoyer une campagne ou un Canvas à des utilisateurs plus uniques que votre limite actuelle, les messages ne seront pas envoyés. Braze continuera à tenter de renvoyer les messages si/lorsque votre limite d’envoi de messages augmente pendant un jour maximum. 

#### Ma limite d’envoi de messages peut-elle diminuer ?
Oui, si votre note de qualité de numéro de téléphone chute trop bas, vous risquez de réduire votre limite d’envoi de messages. Braze vous recommande d’être abonné et d’être informé des mises à jour de qualité de WhatsApp, y compris des mises à jour de votre numéro de téléphone et de votre niveau de limite d’envoi de messages. Vous pouvez vous abonner aux notifications directement dans le tableau de bord WhatsApp Manager. 

#### Quelle est la limite de débit de Meta ?
Meta a sa propre limite de débit, distincte de la limite d'envoi de messages de WABA. La limite par défaut prise en charge par l'API Cloud est de 80 messages par seconde. Si vous pensez que vos campagnes dépasseront cette limite, vous pouvez [demander](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/#throughput) à ce qu'elle soit augmentée. Meta vous recommande de soumettre cette demande au moins trois jours avant l'envoi de la campagne.

### Modèles WhatsApp 

#### Qu’est-ce qu’un modèle WhatsApp ? 
WhatsApp exige que tous les messages initiés par l’entreprise commencent à utiliser un modèle approuvé. Le modèle inclut la copie du message, ainsi que des médias riches en option, tels que des images, des appels à action et des boutons de réponse rapide. Une fois que WhatsApp a approuvé les modèles, ceux-ci peuvent être utilisés pour composer un message WhatsApp dans Braze. 

#### Où créer, modifier et gérer mes modèles WhatsApp ? 
Vous allez créer, modifier, gérer et soumettre des modèles pour approbation directement dans WhatsApp Manager. Une fois que votre WABA est connecté à Braze, vous verrez tous vos modèles dans le tableau de bord avec un indicateur d'état. Si un modèle est rejeté, vous resterez directement via le gestionnaire WhatsApp. **Les modèles ne peuvent pas être créés ou modifiés directement dans Braze.**

#### Combien de temps faut-il que WhatsApp examine une soumission de modèle ? 
Le processus d’approbation peut prendre jusqu’à 24 heures, mais les modèles sont souvent traités en quelques heures ou minutes. 

#### Combien de modèles puis-je avoir à un moment donné ? 
La limite de votre modèle de message dépend du statut de vérification de votre entreprise. Vous pouvez vérifier votre limite sur la page **Gestionnaire WhatsApp > Modèles de messages.**  

#### Comment personnaliser le texte des modèles et les médias riches dans Braze ? 
WhatsApp permet d’insérer des paramètres variables dans des modèles de messages. Les messages ne peuvent pas démarrer ou terminer avec un paramètre variable. Les paramètres variables peuvent être renseignés avec une logique Liquid sur la plateforme Braze. Reportez-vous à la [composition d'un message WhatsApp dans Braze]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#step-2-compose-your-whatsapp-message) pour en savoir plus sur les paramètres variables. 

#### Mon modèle a été rejeté. Est-ce que Braze m’aide à l’obtenir ? 
L’équipe Braze n’a pas de visibilité sur les rejets de modèles. Vous devez travailler directement avec votre gestionnaire commercial WhatsApp pour modifier et soumettre à nouveau le modèle. Assurez-vous de fournir un modèle d’échantillon si nécessaire. Vérifiez que votre modèle respecte les politiques [professionnelles](https://www.whatsapp.com/legal/business-policy/?fbclid=IwAR2qWg6yFKdyjDMxJkbNSM38FLGsxXxffC1qStY2gaHOyp-gl_8g72rZNIw) ou [commerciales](https://www.whatsapp.com/legal/commerce-policy/?fbclid=IwAR3bzN3LTZ-7kO-wnO7X3smtPKGy0asxaFod-U1Ub8B9JUpnrfy1_y7LpAQ) de Meta.

#### Les médias riches peuvent-ils être ciblés ou personnalisés à Braze ? 
Les images peuvent être téléchargées à partir de la bibliothèque multimédia mais ne peuvent pas être ciblées de manière dynamique. Pour les URL, la dernière partie du lien peut être remplie dynamiquement en utilisant Liquide. 

### Livrabilité 

#### Pourquoi un message ne sera-t-il pas livré ? 
Il y a plusieurs raisons pour lesquelles un message ne peut pas être envoyé, y compris les problèmes réseau et l’appareil est désactivé. 

#### Si un message n’est pas livré, serai-je facturé ? 
Non. Si un message n’est pas livré, vous ne serez pas facturé. 

#### Que se passe-t-il si un utilisateur final bloque mon activité ? 
Si un utilisateur final bloque votre activité, les messages suivants que vous essayez d’envoyer ne seront pas livrés et vous ne serez pas facturé. 

#### Que se passe-t-il si un utilisateur final signale un message ? 
Si un utilisateur final signale un message, vous pouvez toujours envoyer des messages ultérieurs à cet utilisateur. Cependant, les rapports peuvent affecter votre cote de qualité sur le canal. 

#### Si un utilisateur final bloque ou signale mon entreprise, le statut de son abonnement sera-t-il mis à jour à Braze ? 
Non. Leur statut de souscription Braze ne sera pas mis à jour. 

### Divers

#### Braze soutient-t-il les cas d’utilisation du support client comme les chatbots et les chats assistés par l’homme pour WhatsApp ? 
Nous ne prenons pas en charge les chatbots ou les chats assistés par l’homme au sein de Braze ou via des intégrations directes. 

Si vous utilisez déjà WhatsApp comme canal de support client, nous vous recommandons de conserver votre configuration actuelle et de créer un nouveau WABA via Braze pour l’envoi de messages marketing. Ce WABA nécessite un nouveau numéro de téléphone. 

#### Comment puis-je « combler le fossé » entre mes messages de support client et mes messages marketing via Braze ? 
Vous pouvez utiliser les propriétés de WhatsApp Liquid pour transférer le contenu des messages WhatsApp entrants (y compris le corps du message et les URL des médias) de Braze vers d'autres plateformes, y compris tout outil de communication individualisée. Pour plus de détails, consultez nos [balises de personnalisation prises en charge]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/). 

Pour envoyer des informations dans Braze, par exemple pour indiquer qu'un utilisateur est dans une conversation d'assistance active, vous pouvez enregistrer un attribut personnalisé (tel qu'un booléen "a un chat d'assistance existant = vrai/faux") et l'utiliser comme critères de segmentation dans leurs campagnes marketing. Vous pouvez également créer un lien profond entre deux fils de discussion pour diriger les utilisateurs vers le fil d'assistance à partir du fil marketing et inversement. 

#### Braze conserve-t-il les réponses des utilisateurs ? 
Les messages ne sont stockés que le temps nécessaire à leur traitement. Pour accéder aux messages des utilisateurs, utilisez Currents. 

#### Comment les numéros de téléphone des utilisateurs doivent-ils être stockés dans Braze ? 
Les numéros de téléphone des utilisateurs doivent être enregistrés au [formatE.164.]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/#formatting)

#### Quel type de média riche est pris en charge dans les modèles WhatsApp ? 
Vous pouvez ajouter des images, des appels à l’action (URL ou numéro de téléphone) et des boutons de réponse rapide aux modèles WhatsApp. Vous pouvez ajouter ces éléments lorsque vous créez des modèles directement dans WhatsApp. 

#### Puis-je importer des numéros de téléphone utilisateur ? 
Oui. Vous pouvez [importer des numéros de téléphone d'utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/). 

#### Qu’est-ce que la vérification commerciale ? 
La vérification commerciale est un concept WhatsApp utilisé pour garantir que la marque est une entreprise légitime. Il peut être rempli dans WhatsApp Manager. La vérification des activités est également nécessaire pour faire évoluer les envois de messages. Sans vérification commerciale, les clients ne peuvent envoyer que 250 utilisateurs finaux uniques dans une période de 24 heures. 

#### Qu’est-ce qu’un compte professionnel officiel ? 
OBA vous donne la coche verte à côté de votre nom d’affichage et est facultatif. Vous pouvez demander un compte professionnel officiel après la vérification de l’entreprise. Notez que la vérification commerciale et un compte professionnel officiel sont différents des concepts WhatsApp. 

#### Quels indicateurs sont disponibles dans le tableau de bord de Braze ? 
Vous pouvez voir des destinataires uniques, des envois, des livraisons, des lectures et des échecs dans le tableau de bord de Braze. Notez que les utilisateurs finaux lisent les reçus pour que le Braze puisse suivre les lectures. Vous pouvez également configurer des événements de conversion pour surveiller les performances de la campagne, similaires à d’autres canaux. 

#### Qu’est-ce qu’une conversation WhatsApp ? 
WhatsApp est un canal axé sur l’envoi de messages bidirectionnel et donc sur les conversations (au lieu du nombre de messages individuels). Une conversation est un fil de 24 heures entre une entreprise et un utilisateur final.

- **Conversation à l'initiative de l'entreprise**: Une conversation dans laquelle commence l’entreprise en envoyant un message modèle approuvé à l’utilisateur final. Dès que l’entreprise envoie un message, elle commence la fenêtre de 24 heures.
- **Conversation initiée par l'utilisateur**: Une conversation où l’utilisateur final envoie un message à l’entreprise. Lorsque l’entreprise envoie un message en réponse, la fenêtre de 24 heures commence.

#### Quels facteurs affectent la qualité du numéro de téléphone et que se passe-t-il lorsque ma note de qualité baisse trop bas ? 
Les facteurs qui affectent la qualité de la qualité du numéro de téléphone comprennent un utilisateur final bloquant une entreprise (et les raisons qu’ils fournissent lorsqu’ils bloquent une entreprise) et un utilisateur final signalant une entreprise. 

Lorsque l'évaluation de la qualité est faible, le statut du numéro de téléphone passe de **Connecté** à **Signalé**. Si la qualité ne s'améliore pas au bout de sept jours, le statut redevient **Connecté**. Cependant, la limite d’envoi de messages diminuera au niveau supérieur. Par exemple, un numéro de téléphone utilisé pour avoir une limite d’envoi de messages de 100 000 a maintenant une limite d’envoi de messages de 10 000.
