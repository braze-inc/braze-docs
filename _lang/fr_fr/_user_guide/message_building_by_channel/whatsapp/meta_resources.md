---
nav_title: Ressources Meta
article_title: Ressources Meta
page_order: 12
description: "Cet article fournit une documentation Meta utile, des informations et des ressources pour améliorer votre compréhension de l'intégration WhatsApp."
alias: /meta_resources/
page_type: reference
channel:
  - WhatsApp

---

# Ressources Meta

## Documentation Meta

Consultez la documentation Meta suivante pour obtenir des conseils sur les noms d'affichage, les numéros de téléphone et plus encore.

- [Conseils pour le nom d'affichage](https://www.facebook.com/business/help/757569725593362)
- [Activation de Meta Insights](https://www.facebook.com/business/help/218116047387456)
- [Exigences relatives au numéro de téléphone](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers)
- [Limites d'envoi de messages](https://developers.facebook.com/docs/whatsapp/messaging-limits)
- [Évaluation de la qualité](https://www.facebook.com/business/help/896873687365001)

## Mises à jour des produits WhatsApp

### Juin 2026 : Identifiants utilisateur au niveau du compte professionnel
*Dernière mise à jour mars 2026*

- Meta introduit des identifiants utilisateur pour remplacer le partage de numéros de téléphone afin de protéger la vie privée
- Braze travaille sur une solution en amont du déploiement
- Déploiement prévu par Meta en juin 2026

### Novembre 2025 : [API Marketing Messages pour WhatsApp](https://developers.facebook.com/documentation/business-messaging/whatsapp/marketing-messages/overview/) (anciennement Marketing Messages Lite API)
*Dernière mise à jour mars 2026*

- Remplace les limites statiques de l'API Cloud par des limites dynamiques basées sur l'engagement
- Non disponible dans la zone EMEA, au Japon ou en Corée du Sud pour la distribution optimisée
- Les messages d'utilité et d'authentification continuent automatiquement via l'API Cloud

### Octobre 2025 : Modification du processus d'approbation des comptes professionnels officiels (OBA)
*Dernière mise à jour mars 2026*

- Auparavant accessible à tous les clients via WhatsApp Manager
- Désormais réservé aux : gouvernements/grands annonceurs Meta, annonceurs directs, ou via un BSP comme Braze (jusqu'à 5 par semaine)
- Nouvelles conditions préalables : vérification de l'entreprise, vérification en deux étapes, nom d'affichage approuvé, notoriété
- Contactez votre Customer Success Manager pour obtenir de l'aide

### Octobre 2025 : Baisses de tarifs régionales
*Dernière mise à jour mars 2026*

- Tarifs d'utilité/authentification réduits en Argentine, Égypte, Mexique, Amérique du Nord
- Tarifs marketing réduits au Mexique (à compter du 1er octobre 2025)

### Octobre 2025 : Les limites d'envoi de messages passent du niveau téléphone au niveau portefeuille d'entreprise
*Dernière mise à jour mars 2026*

- Les limites sont désormais partagées entre tous les numéros de téléphone d'un portefeuille
- Les portefeuilles héritent de la limite existante la plus élevée
- Accès plus rapide aux limites supérieures (dans les 6 heures)
- Risque : les entreprises sans numéro « illimité » peuvent voir leurs limites agrégées diminuer

### 1er juillet 2025 : Refonte de la tarification
*Dernière mise à jour mars 2026*

- La facturation par message remplace la facturation par conversation
- Les messages d'utilité envoyés dans une fenêtre de service de 24 heures deviennent gratuits
- Tarifs d'utilité/authentification mis à jour sur plusieurs marchés, avec de nouveaux paliers de volume
- Nouvelles règles sur la mauvaise catégorisation des modèles d'utilité — les entreprises risquent le rejet de modèles et des restrictions de soumission

### Avril 2025 : Arrêt des envois de messages marketing aux numéros de téléphone américains
*Dernière mise à jour août 2025*

Meta mettra en pause la distribution de tous les messages de modèles marketing aux utilisateurs WhatsApp disposant d'un numéro de téléphone aux États-Unis (numéro composé d'un indicatif `+1` et d'un indicatif régional américain). Aucune date n'est actuellement prévue pour la levée de cette pause.

Toute tentative d'envoi d'un modèle à un utilisateur WhatsApp ayant un numéro de téléphone américain aboutira à l'erreur `131049`.

### Mars 2025 : Restrictions en cas de mauvaise catégorisation des modèles
*Dernière mise à jour mars 2026*

- Meta a mis en place des mesures d'application pour les entreprises qui utilisent de manière abusive la catégorisation utilité/marketing
- Cela peut entraîner des restrictions de 7 à 30 jours sur la création de modèles et les vérifications de catégorie

### Mars 2025 : Limites de messages de modèle marketing par utilisateur
*Dernière mise à jour août 2025*

Meta limitera le nombre de messages de modèles marketing qu'un utilisateur peut recevoir de l'ensemble des entreprises au cours d'une période donnée, en commençant par les messages les moins susceptibles d'être lus.

Il existe une exception : si une personne répond à un message marketing, cela ouvre une fenêtre de service client de 24 heures. Les messages marketing envoyés dans cette fenêtre ne sont pas comptabilisés dans la limite de cette personne.

La limite spécifique varie selon l'utilisateur, en fonction de son niveau d'engagement. Pour en savoir plus sur les limites de messages de modèles marketing par utilisateur de WhatsApp, [cliquez ici](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates#per-user-marketing-template-message-limits).

### Janvier 2025 : WhatsApp met en pause l'envoi de messages marketing aux utilisateurs américains à partir du 1er avril
*Dernière mise à jour janvier 2025*

WhatsApp mettra en pause l'envoi de messages marketing aux utilisateurs américains (personnes ayant un numéro de téléphone américain) à partir du 1er avril 2025. [Les messages d'utilité, de service et d'authentification](https://developers.facebook.com/docs/whatsapp/pricing/) ainsi que les [messages de réponse]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#response-messages) resteront autorisés aux États-Unis.

L'envoi de messages marketing (ainsi que tous les autres types de messages) vers tous les autres pays ou régions reste autorisé et ne sera pas affecté.

Meta nous a informés que cette mise à jour vise à préserver la santé de l'écosystème WhatsApp aux États-Unis, où WhatsApp se développe rapidement mais en est encore à un stade précoce (par exemple, les messages marketing génèrent un engagement plus faible que dans d'autres régions). Ils continueront à évaluer le moment où le marché américain sera prêt à reprendre les messages marketing.

La distribution de messages marketing à des numéros de téléphone avec des indicatifs régionaux américains sera rejetée par WhatsApp et renverra un code d'erreur 131049.

### Novembre 2024 : Modifications de la politique d'abonnement WhatsApp
*Dernière mise à jour janvier 2025*

Meta a récemment mis à jour sa [politique d'abonnement](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). Au lieu d'exiger un consentement spécifique à chaque canal, les entreprises peuvent désormais envoyer des messages aux utilisateurs sur la plateforme si :

1. La personne a communiqué son numéro de téléphone.
2. La personne a donné son consentement pour recevoir des messages en général, et pas uniquement via WhatsApp.

Les entreprises doivent toujours se conformer à toutes les lois locales et respecter les exigences ci-dessous lors de la collecte des abonnements :

- Les entreprises doivent clairement indiquer que la personne accepte de recevoir des communications de leur part.
- Les entreprises doivent indiquer clairement le nom de l'entreprise dont la personne accepte de recevoir des messages.
- Les entreprises doivent se conformer à la législation en vigueur.

Bien que WhatsApp ait assoupli sa politique, Braze recommande toujours de collecter des abonnements spécifiques au canal WhatsApp afin de favoriser la meilleure expérience client et les meilleurs taux d'engagement. Comme toujours, vérifiez auprès de votre équipe juridique ce qui convient le mieux à votre marque.

### Novembre 2024 : Mise à jour de la limite de modèles marketing par utilisateur pour les personnes résidant aux États-Unis, à l'approche des fêtes de fin d'année
*Dernière mise à jour décembre 2024*

Depuis le déploiement de la limite de modèles marketing par utilisateur, Meta a constaté des améliorations significatives des taux de lecture et du ressenti des utilisateurs.
 
À partir de maintenant, avant les fêtes de fin d'année, les personnes aux États-Unis recevront moins de nouvelles conversations marketing. Meta s'attend à ce que ce changement génère des audiences plus engagées, ce qui se traduit en fin de compte par de meilleurs résultats pour les entreprises. Cela peut entraîner des taux de distribution plus faibles pour votre entreprise si vous envoyez des messages marketing à des numéros de téléphone américains. Vous pouvez suivre cette évolution grâce au code d'erreur `131049` via Braze Currents et le journal d'activité des messages.

Les entreprises aux États-Unis peuvent toujours diffuser des messages marketing dans d'autres zones géographiques. Les messages d'utilité, d'authentification ou de service ne sont pas concernés, tout comme les messages de modèles marketing envoyés dans une fenêtre de conversation initiée par l'utilisateur (par exemple, une publicité cliquable vers WhatsApp, un carrousel de produits ou un modèle de coupon envoyé dans le cadre d'une conversation).

### Novembre 2024 : WhatsApp étend les mesures de qualité au niveau des comptes pour inclure les taux de lecture
*Dernière mise à jour décembre 2024*

WhatsApp investit en permanence dans de nouveaux moyens d'aider les entreprises à créer des expériences de qualité pour leurs clients, notamment en réduisant les comportements de type spam sur sa plateforme.

Le 22 novembre, WhatsApp a commencé à étendre ses mesures d'application de la qualité au niveau des comptes pour les comptes professionnels WhatsApp (WABA) dont le taux de lecture est extrêmement bas. Ce changement sera déployé à l'échelle mondiale.

Lorsque le taux de lecture d'un compte chute de manière significative (par exemple, la majorité des messages envoyés par le compte ne sont pas lus), des blocages d'envoi de messages seront appliqués au compte. La sévérité du blocage augmentera si les taux de lecture restent constamment faibles à grande échelle.

Si le taux de lecture du compte est extrêmement bas, les mesures suivantes seront prises :

- Le compte sera bloqué pour l'envoi de messages à l'initiative de l'entreprise. Il pourra toujours répondre aux messages envoyés par les clients. Ce blocage initial est un « verrouillage souple » qui peut être levé en sélectionnant le bouton d'acquittement dans la page Qualité du compte pour reprendre l'envoi de messages.
- Si le taux de lecture continue de baisser ou reste faible après le verrouillage souple, les entreprises peuvent faire face à une augmentation progressive des mesures d'application (par exemple, quelques jours de restrictions sur l'envoi de messages).
- Les entreprises devront attendre la fin de la restriction imposée pour recommencer à envoyer des messages. Si le taux de lecture reste faible après plusieurs verrouillages souples, le compte sera finalement radié.

#### Comment rester informé de ces avertissements et mesures d'application

Comme pour les mesures d'application existantes sur la plateforme, les entreprises seront informées de ces actions et pourront en accuser réception via la page Qualité du compte dans le WhatsApp Business Manager. Vérifiez que les coordonnées correctes sont bien renseignées dans le WhatsApp Business Manager pour tous les administrateurs concernés, car les e-mails de notification seront envoyés sur la base de ces informations.

Les notifications concernant les violations graves liées au spam seront :

- Affichées dans le centre de notifications du WhatsApp Business Manager
- Affichées dans une bannière dans le WhatsApp Manager
- Envoyées par e-mail à tous les administrateurs définis dans le WhatsApp Business Manager

### Mai 2024 : Lancement de l'API Cloud en Türkiye
*Dernière mise à jour mai 2024*

Meta donne désormais aux entreprises utilisant l'API Cloud un accès à la Türkiye pour la messagerie professionnelle. Auparavant, l'API Cloud de WhatsApp était disponible pour les entreprises en Türkiye, mais les utilisateurs WhatsApp disposant de numéros turcs ne pouvaient pas envoyer ni recevoir de messages via l'API Cloud.

Meta indique toujours clairement aux utilisateurs lorsqu'ils discutent avec une entreprise hébergée par Meta, et tous les utilisateurs doivent accepter les Conditions d'utilisation et la Politique de confidentialité de WhatsApp pour pouvoir utiliser la messagerie professionnelle. La mise à jour des Conditions d'utilisation et de la Politique de confidentialité de 2021 en Türkiye avait été suspendue, mais est maintenant en cours de déploiement. Cela ne change pas l'engagement de Meta envers la confidentialité — les conversations personnelles continuent d'être protégées par un chiffrement de bout en bout, ce qui signifie que seuls vous et le destinataire prévu pouvez les voir. La mise à jour permet aux utilisateurs turcs d'accéder à des fonctionnalités professionnelles optionnelles s'ils le souhaitent et offre plus de transparence sur le fonctionnement de WhatsApp.  
 
Les entreprises utilisant l'API Cloud peuvent désormais initier des conversations avec des utilisateurs WhatsApp ayant des numéros turcs, ce qui renverra désormais un webhook de conversation « envoyée », au lieu du code d'erreur 131026 actuel.

Pour qu'un message professionnel soit marqué comme « distribué » ou « lu », l'utilisateur doit accepter les conditions de WhatsApp. Une entreprise ne sera facturée que si le message est effectivement distribué.

Les utilisateurs qui reçoivent ou essaient d'envoyer un message à une entreprise API Cloud verront une notification in-app concernant la mise à jour des conditions, indiquant clairement qu'ils ne peuvent pas envoyer de message à une entreprise API Cloud tant qu'ils n'ont pas accepté la mise à jour de WhatsApp. De plus, les utilisateurs qui enregistrent ou réenregistrent l'application sur leur téléphone seront invités à accepter la mise à jour de WhatsApp.

Lorsqu'un utilisateur accepte la mise à jour, il verra l'avis de message système de l'API Cloud lorsqu'il discutera avec une entreprise API Cloud.

### Mai 2024 : Limites de messages de modèle marketing par utilisateur
*Dernière mise à jour mai 2024*

Meta déploie de nouvelles approches pour maintenir des expériences utilisateur de haute qualité et maximiser l'engagement des messages de modèles marketing sur la plateforme WhatsApp. À partir du 23 mai 2024, le nombre de messages de modèles marketing que chaque utilisateur peut recevoir de l'ensemble des entreprises avec lesquelles il interagit sera limité sur une période donnée, en commençant par un petit nombre de conversations moins susceptibles d'être lues. Notez que la limite est déterminée en fonction du nombre de messages de modèle marketing que cette personne a déjà reçus de n'importe quelle entreprise, et n'est pas spécifiquement liée à votre marque. Cependant, cela peut affecter la livrabilité de vos messages de modèle marketing.

La limite s'applique uniquement aux messages de modèle marketing qui ouvriraient normalement une nouvelle conversation marketing. Si une conversation marketing est déjà ouverte entre votre marque et un utilisateur WhatsApp, les messages de modèle marketing envoyés à cet utilisateur ne seront pas affectés.

Si un message de modèle marketing n'est pas distribué à un utilisateur donné en raison de la limite, l'API Cloud renverra le code d'erreur 131026. Notez cependant que ces codes d'erreur couvrent un large éventail de problèmes pouvant entraîner la non-distribution d'un message, et pour des raisons de confidentialité, Meta ne divulguera pas si le message n'a effectivement pas été distribué en raison de la limite. Reportez-vous au [document de résolution des problèmes](https://developers.facebook.com/docs/whatsapp/cloud-api/support#troubleshooting) de l'API Cloud pour obtenir des descriptions des raisons de non-distribution et savoir comment en déterminer la cause sous-jacente.

Si vous recevez l'un de ces codes d'erreur et soupçonnez qu'il est dû à la limite, évitez de renvoyer immédiatement le message de modèle, car cela ne fera que générer une nouvelle erreur.

Pour plus d'informations sur cette mise à jour de la livrabilité, y compris des détails sur le suivi de votre livrabilité et d'autres bonnes pratiques pour la communication marketing sur WhatsApp, consultez notre récent [article de blog](https://www.braze.com/resources/articles/meta-introduces-deliverability-updates-for-whatsapp?utm_campaign=fy25-q2-global-customer-customer-meta-deliverability-updates-for-whatsapp&utm_medium=email-cdb&utm_source=braze&utm_content=blog-meta-deliverability-updates-for-wa-blog).

### Avril 2024 : Cadencement des modèles pour les modèles d'utilité
*Dernière mise à jour avril 2024*

L'année dernière, WhatsApp a introduit le cadencement des modèles pour les messages marketing comme un nouveau moyen d'aider les entreprises à améliorer l'engagement de leurs modèles et à créer des expériences utilisateur de qualité. À compter du 30 avril, ce cadencement est étendu aux messages d'utilité. Si un modèle d'utilité pour un compte est mis en pause en raison des retours des utilisateurs, le rythme des nouveaux modèles d'utilité créés sera ajusté pour les sept jours suivants.

### Avril 2024 : Les taux de lecture affecteront la note de qualité des modèles marketing
*Dernière mise à jour mars 2024*

WhatsApp teste de nouvelles approches, en commençant par les consommateurs en Inde, pour créer des expériences plus enrichissantes et maximiser l'engagement dans les conversations marketing des entreprises. Cela peut inclure la limitation du nombre de conversations marketing qu'une personne reçoit de toute entreprise dans une période donnée, en commençant par un petit nombre de conversations moins susceptibles d'être lues. Braze recevra un code d'erreur si un message n'est pas distribué.

WhatsApp commencera à prendre en compte les taux de lecture dans l'évaluation de la qualité des modèles marketing, en plus des indicateurs traditionnels tels que les blocages et les signalements. WhatsApp pourra temporairement suspendre les campagnes de messages marketing avec des taux de lecture faibles, donnant aux entreprises le temps de peaufiner les modèles les moins performants avant d'augmenter le volume, à partir du 1er avril 2024.

### Février 2024 : Expérimentation des conversations marketing
*Dernière mise à jour février 2024*

À partir du 6 février 2024, WhatsApp teste de nouvelles approches, en commençant par les consommateurs en Inde, pour créer des expériences plus enrichissantes et maximiser l'engagement des clients avec les conversations marketing de votre marque. Cela peut inclure la limitation du nombre de conversations marketing qu'un utilisateur reçoit de votre marque dans une période donnée, en commençant par un petit nombre de conversations moins susceptibles d'être lues.

### Octobre 2023 : Cadencement des modèles
*Dernière mise à jour octobre 2023*

À partir du 12 octobre 2023, WhatsApp lance un concept appelé « cadencement des modèles » (template pacing) pour les messages marketing. Au lieu d'envoyer votre message à l'ensemble de l'audience de votre campagne simultanément, le « cadencement des modèles » distribue initialement le message à un sous-ensemble plus restreint d'utilisateurs pour recueillir des retours en temps réel des destinataires avant d'envoyer les messages restants.

La « limite de rythme » (le sous-ensemble initial de messages envoyés) varie en fonction du modèle. Après l'envoi initial, WhatsApp conserve les messages restants pendant une durée maximale de 30 minutes. Pendant cette période de rétention, la qualité du modèle est évaluée en fonction des retours des clients. Si les retours sont positifs, signe d'un modèle de haute qualité, les messages restants sont distribués. Si les retours sont négatifs, les messages restants non distribués sont abandonnés, ce qui évite d'autres retours négatifs d'une plus grande partie de vos clients et vous aide à prévenir d'éventuels problèmes liés à l'application des règles de qualité (tels que les impacts sur la notation de la qualité du numéro de téléphone).

Notez que WhatsApp utilise le même système pour évaluer la qualité des modèles dans le cadencement que dans la mise en pause des modèles. Ainsi, les messages non distribués pendant le cadencement (en raison de modèles de faible qualité) sont les mêmes que ceux qui auraient été mis en pause à plus grande échelle.

En définitive, cette mise à jour vous offre une boucle de rétroaction plus rapide (30 minutes contre des heures ou des jours avec la mise en pause des modèles), ce qui vous permet d'ajuster vos modèles et d'offrir une meilleure expérience client.

**Si vous avez d'autres questions concernant cette mise à jour, contactez votre conseiller partenaire Meta.**

### Juin 2023 : Expérimentation de messagerie
*Dernière mise à jour juin 2023*

À partir du 14 juin 2023, Meta introduit de nouvelles pratiques d'expérimentation sur la plateforme WhatsApp afin d'évaluer l'impact des messages marketing sur l'expérience et l'engagement des consommateurs. Cette expérience peut affecter vos messages marketing envoyés via l'API WhatsApp Business avec Braze.

Meta a l'intention de poursuivre ce type d'expérimentations sur la plateforme WhatsApp. Pour plus d'informations, reportez-vous à la [documentation de Meta](https://developers.facebook.com/docs/whatsapp/on-premises/guides/experiments?content_id=86oue5PtwEgcBJl).

**Les expérimentations de WhatsApp n'affectent que les messages marketing.** Cette expérience peut impacter la distribution des messages de modèle marketing. Les modèles d'utilité et d'authentification continueront d'être distribués sans aucun impact.

Dans le cadre de l'expérience, Meta sélectionne aléatoirement environ 1 % des consommateurs WhatsApp comme participants. Si ces consommateurs sont sélectionnés, Meta ne leur distribuera pas de messages de modèle marketing, sauf si l'une des conditions suivantes est remplie :

- Le consommateur vous a répondu au cours des dernières 24 heures ;
- Une conversation marketing existante est ouverte ; ou
- Le consommateur a cliqué sur une publicité WhatsApp au cours des dernières 72 heures.

## Foire aux questions {#faq}

### Comment saurai-je si mon message marketing a été impacté par l'expérience de Meta ?

Si un message n'est pas distribué en raison de l'expérience, un code d'erreur spécifique sera affiché dans le journal des activités et dans Currents. Le message sera également comptabilisé comme un échec et intégré dans vos indicateurs d'échecs WhatsApp dans tous les rapports du tableau de bord de Braze. Vous ne serez pas facturé pour ces messages.

Ce code d'erreur 130472 indiquera « User's number is part of an experiment ». Pour plus d'informations sur les codes d'erreur de l'API Cloud WhatsApp, reportez-vous à la [documentation de Meta](https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes?content_id=8SJRLBEjYGvXO9k).

### Puis-je me désinscrire de l'expérience de Meta ?

Non, Meta ne permet aucune désinscription. Tous les fournisseurs et utilisateurs de l'API WhatsApp Business sont soumis à cette expérience.

### Puis-je essayer de renvoyer un modèle plus tard ?

Il n'y a pas de durée fixe pour cette expérience. Un consommateur peut donc continuer à y être inclus.

### Que puis-je faire si mes messages marketing ne sont pas distribués en raison de l'expérience de Meta ?

Nous vous recommandons d'utiliser d'autres canaux Braze, tels que l'e-mail, le SMS, les notifications push ou les messages in-app, pour envoyer un message au contenu similaire à vos utilisateurs ciblés.