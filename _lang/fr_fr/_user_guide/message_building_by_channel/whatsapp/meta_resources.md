---
nav_title: Ressources Meta
article_title: Ressources Meta
page_order: 81
description: "Cet article fournit une documentation Meta utile, des informations et des ressources pour améliorer votre compréhension de l'intégration WhatsApp."
page_type: reference
channel:
  - WhatsApp

---

# Ressources méta

## Documentation méta

Consultez la documentation Meta suivante pour obtenir des conseils sur les noms d'affichage, les numéros de téléphone et plus encore.

- [Conseils pour le nom d'affichage](https://www.facebook.com/business/help/757569725593362) 
- [Activation des informations Meta](https://www.facebook.com/business/help/218116047387456)
- [Exigences relatives au numéro de téléphone](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers)
- [Limites d’envoi de messages](https://developers.facebook.com/docs/whatsapp/messaging-limits)
- [Évaluation de la qualité](https://www.facebook.com/business/help/896873687365001)

## Mises à jour des produits WhatsApp

### Mai 2024: lancement de l’API Cloud en Turquie
*Dernière mise à jour mai 2024*

Meta fournit désormais aux entreprises de l'API Cloud un accès à la Turquie pour la messagerie Business. Auparavant, l'API Cloud de WhatsApp était disponible pour les entreprises en Turquie, mais les utilisateurs de WhatsApp avec des numéros turcs ne pouvaient pas envoyer ou recevoir de messages envoyés via l'API Cloud. 

Meta indique toujours clairement aux utilisateurs lorsqu'ils discutent avec une entreprise hébergée par Meta, et tous les utilisateurs doivent accepter les Conditions d'utilisation et la Politique de confidentialité de WhatsApp pour continuer à envoyer des messages commerciaux. La mise à jour des conditions d'utilisation et de la politique de confidentialité de 2021 en Turquie avait été suspendue, mais est maintenant en cours de déploiement. Cela ne change pas l'engagement de Meta envers la confidentialité. Les conversations personnelles continuent d'être protégées par un chiffrement de bout en bout, ce qui signifie que seuls vous et le destinataire prévu pouvez les voir. La mise à jour permet aux utilisateurs turcs d'accéder à des fonctionnalités commerciales optionnelles s'ils choisissent de le faire et offre plus de transparence sur le fonctionnement de WhatsApp.  
 
Les entreprises d'API Cloud peuvent désormais initier des conversations avec des utilisateurs WhatsApp ayant des numéros turcs, ce qui renverra désormais un webhook comme une conversation « envoyée », au lieu du code d'erreur 131026 d'aujourd'hui.

Pour qu'un message commercial soit « livré » ou « lu », l'utilisateur doit accepter les conditions de WhatsApp. Une entreprise ne sera pas facturée à moins que le message ne soit livré.

Les utilisateurs qui reçoivent ou essaient d'envoyer un message à une entreprise Cloud API verront une notification dans l'application concernant la mise à jour des conditions, ce qui indique clairement qu'ils ne peuvent pas envoyer de message à une entreprise Cloud API tant qu'ils n'ont pas accepté la mise à jour de WhatsApp. De plus, les utilisateurs qui enregistrent ou réenregistrent l'application sur leur téléphone seront invités à accepter la mise à jour de WhatsApp.

Si un utilisateur accepte la mise à jour, il voit l'avis de message système de l’API Cloud lorsqu'il discute avec une entreprise API Cloud.

### Mai 2024: Limites de messages de modèle marketing par utilisateur
*Dernière mise à jour mai 2024*

Meta déploie de nouvelles approches pour maintenir des expériences utilisateur de haute qualité et maximiser l'engagement des messages modèles marketing sur la plateforme WhatsApp. À partir du 23 mai 2024, ils limiteront le nombre de messages de modèles marketing que chaque utilisateur individuel peut recevoir de toutes les entreprises avec lesquelles ils interagissent pendant une période donnée, en commençant par un petit nombre de conversations qui sont moins susceptibles d'être lues. Notez que la limite est déterminée en fonction du nombre de messages de modèle marketing que cette personne a déjà reçus de n'importe quelle entreprise, et n'est pas spécifiquement liée à votre marque. Cependant, cela peut affecter la délivrabilité de vos messages de modèle marketing.

La limite s'applique uniquement aux messages de modèle marketing qui ouvriraient normalement une nouvelle conversation marketing. Si une conversation marketing est déjà ouverte entre votre marque et un utilisateur WhatsApp, les messages de modèle marketing envoyés à l'utilisateur ne seront pas affectés.

Si un message de modèle marketing n'est pas distribué à un utilisateur donné en raison de la limite, l'API Cloud renvoie le code d'erreur 131026. Notez cependant que ces codes d'erreur couvrent un large éventail de problèmes pouvant entraîner la non-distribution d'un message, et pour des raisons de confidentialité, Meta ne divulguera pas si, dans les faits, le message n'a pas été distribué en raison de la limite. Reportez-vous au [document de dépannage](https://developers.facebook.com/docs/whatsapp/cloud-api/support#troubleshooting) de l'API Cloud pour obtenir des descriptions des raisons de non-distribution et ce que vous pouvez faire pour déterminer leur cause sous-jacente.

Si vous recevez l'un de ces codes d'erreur et soupçonnez qu'il est dû à la limite, évitez de renvoyer immédiatement le message modèle, car cela ne fera que générer une nouvelle erreur. 

Pour plus d'informations sur cette mise à jour de la livrabilité, y compris des détails sur la surveillance de votre livrabilité et d'autres bonnes pratiques pour la communication marketing sur WhatsApp, consultez notre récent [article de blog](https://www.braze.com/resources/articles/meta-introduces-deliverability-updates-for-whatsapp?utm_campaign=fy25-q2-global-customer-customer-meta-deliverability-updates-for-whatsapp&utm_medium=email-cdb&utm_source=braze&utm_content=blog-meta-deliverability-updates-for-wa-blog).

### Avril 2024: Modèle de rythme pour les modèles utilitaires
*Dernière mise à jour : avril 2024*

L'année dernière, WhatsApp a introduit le rythme des modèles pour les messages marketing comme un nouveau moyen d'aider les entreprises à améliorer l'engagement de leurs modèles et à créer des expériences utilisateur précieuses. À compter du 30 avril, ils étendent le cadencement des modèles aux messages utilitaires. Si un modèle d'utilitaire pour un compte est mis en pause en raison des commentaires des utilisateurs, ils ajusteront le rythme des nouveaux modèles d'utilitaires créés pour les sept prochains jours.

### Avril 2024: Les taux de lecture affecteront la note de qualité des modèles marketing 
*Dernière mise à jour : mars 2024*

WhatsApp teste de nouvelles approches, en commençant par les consommateurs en Inde, pour créer des expériences plus précieuses et maximiser l'engagement dans les conversations marketing des entreprises. Cela peut inclure la limitation du nombre de conversations marketing qu'une personne reçoit de toute entreprise dans une période donnée, en commençant par un petit nombre de conversations qui sont moins susceptibles d'être lues. Braze obtiendra un code d'erreur si un message n'est pas livré.

WhatsApp commencera à prendre en compte les taux de lecture dans notre évaluation de la qualité des modèles marketing, en plus des métriques traditionnelles telles que les blocages et les signalements. WhatsApp peut temporairement suspendre les campagnes de communication marketing avec des taux de lecture faibles, donnant aux entreprises le temps de peaufiner les modèles avec le moins d'engagement avant d'augmenter le volume à partir du 1er avril 2024. 

### Février 2024: Expérimentation des conversations marketing
*Dernière mise à jour février 2024*

À partir du 6 février 2024, WhatsApp teste de nouvelles approches, en commençant par les consommateurs en Inde, pour créer des expériences plus précieuses et maximiser l'engagement des clients avec les conversations marketing de votre marque. Cela peut inclure la limitation du nombre de conversations marketing qu'un utilisateur reçoit de votre marque dans une période donnée, en commençant par un petit nombre de conversations qui sont moins susceptibles d'être lues.

### Octobre 2023: Cadencement des modèles 
*Dernière mise à jour octobre 2023*

À partir du 12 octobre 2023, WhatsApp lance un concept appelé « cadencement des modèles » (template pacing) pour les messages marketing. Au lieu d'envoyer votre message à l'ensemble de votre audience de campagne simultanément, le « template pacing » délivre initialement le message à un plus petit sous-ensemble d'utilisateurs pour recueillir des retours en temps réel des destinataires de la campagne avant d'envoyer les messages restants. 

La « limite de rythme » (le sous-ensemble initial de messages envoyés) est variable en fonction du modèle. Après l'envoi initial, WhatsApp conservera les messages restants pendant une durée maximale de 30 minutes. Pendant cette période de rétention, ils évaluent la qualité du modèle en fonction des commentaires des clients. Si les commentaires sont positifs, signe d'un modèle de haute qualité, ils transmettent les autres messages. Si les retours sont négatifs, ils abandonnent les messages restants non livrés, empêchant ainsi d'autres retours négatifs d'une plus grande partie de vos clients et vous aidant à éviter des problèmes potentiels d'application de la qualité (tels que les impacts sur la notation de la qualité du numéro de téléphone). 

Notez que WhatsApp utilise le même système pour évaluer la qualité des modèles dans le rythme des modèles que pour la pause des modèles. Ainsi, les messages non livrés pendant le rythme du modèle (en raison de modèles de faible qualité) sont les mêmes que ceux qui auraient été mis en pause à plus grande échelle. 

En fin de compte, cette mise à jour vous offre une boucle de rétroaction plus rapide (30 minutes contre des heures ou des jours avec la pause du modèle), afin que vous puissiez ajuster vos modèles et offrir une meilleure expérience client.

**Si vous avez d'autres questions concernant cette mise à jour, veuillez contacter votre conseiller partenaire Meta.**

### Juin 2023: Expérimentation de messagerie 
*Dernière mise à jour juin 2023*

À partir du 14 juin 2023, Meta introduit de nouvelles pratiques d'expérimentation sur la plateforme WhatsApp afin d'évaluer comment les messages marketing impactent l'expérience et l'engagement des consommateurs. Cette expérience peut affecter vos messages marketing envoyés sur l'API WhatsApp Business avec Braze.

Meta a l'intention de continuer de telles expérimentations sur la plateforme WhatsApp. Pour plus d’informations, reportez-vous à la [documentation de Meta](https://developers.facebook.com/docs/whatsapp/on-premises/guides/experiments?content_id=86oue5PtwEgcBJl).

**Les expérimentations de WhatsApp n'affectent que les messages marketing.** Cette expérience a le potentiel d'impacter la livraison des messages de modèle marketing. Les modèles d'utilité et d'authentification continueront d'être livrés sans aucun impact d'expérimentation.

Dans le cadre de l'expérience, Meta choisit aléatoirement environ 1 % des consommateurs de WhatsApp comme participants. Meta ne livrera pas de modèles de messages marketing à ces consommateurs, sauf si l'une des conditions suivantes est remplie :

- Si un consommateur vous a répondu au cours des dernières 24 heures;
- Si une conversation marketing existante est ouverte ; ou
- Si une annonce WhatsApp a été cliquée par le consommateur au cours des dernières 72 heures.

## Foire aux Questions {#faq}

### Comment saurai-je si mon message marketing a été impacté par l'expérience de Meta ?

Si un message n'est pas distribué en raison de l'expérience, un code d'erreur spécifique sera affiché dans le journal des activités et dans Currents. Le message sera également compté comme un échec et intégré dans vos métriques d'échecs WhatsApp dans tous les rapports du tableau de bord Braze. Vous ne serez pas facturé pour ces messages.

Ce code d'erreur 130472 indiquera « Le numéro de l'utilisateur fait partie d'une expérience ». Pour plus d’informations sur les codes d’erreur d’API Cloud pour WhatsApp, reportez-vous à la [documentation de Meta](https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes?content_id=8SJRLBEjYGvXO9k).

### Puis-je me désinscrire de l'expérience de Meta ?

Non, Meta ne permet pas aucune désinscription de l’expérience. Tous les fournisseurs et utilisateurs de l'API WhatsApp Business sont inclus dans cette expérience Meta.

### Puis-je essayer de renvoyer un modèle plus tard ?

Il n'y a pas de temps fixe pour cette expérience. Dès lors, un consommateur peut continuer à être inclus dans l'expérience.

### Que puis-je faire si mes messages marketing ne sont pas livrés en raison de l'expérience de Meta ?

Nous recommandons d'utiliser d'autres canaux Braze, tels que l'email, le SMS, les notifications push ou les messages in-app pour envoyer un message avec un contenu similaire à vos utilisateurs ciblés.
