---
nav_title: Méta ressources
article_title: Ressources méta
page_order: 11
description: "Cet article fournit une documentation, des informations et des ressources Meta utiles pour améliorer votre compréhension de l'intégration WhatsApp."
page_type: reference
channel:
  - WhatsApp

---

# Méta ressources

## Méta documentation

Consultez la documentation Meta suivante pour obtenir des conseils sur les noms d'affichage, les numéros de téléphone, etc.

- [Conseils sur le nom d'affichage](https://www.facebook.com/business/help/757569725593362) 
- [Activation des méta-informations](https://www.facebook.com/business/help/218116047387456)
- [Exigences en matière de numéro de téléphone](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers)
- [Limites de l'envoi de messages](https://developers.facebook.com/docs/whatsapp/messaging-limits)
- [Classement de la qualité](https://www.facebook.com/business/help/896873687365001)

## Mises à jour des produits WhatsApp

### Avril 2025 : Arrêt des envois de messages marketing aux numéros de téléphone américains
*Dernière mise à jour août 2025*

Meta mettra en pause la réception/distribution de tous les messages de modèles marketing aux utilisateurs de WhatsApp qui ont un numéro de téléphone aux États-Unis (numéro composé d'un code de composition `+1` et d'un indicatif régional américain). Il n'y a pas de date planifiée pour la levée de cette pause. 

Toute tentative d'envoi d'un modèle à un utilisateur de WhatsApp ayant un numéro de téléphone américain aboutira à l'erreur `131049`.

### Mars 2025 : Limites des messages des modèles d'envoi de messages marketing par utilisateur
*Dernière mise à jour août 2025*

Meta limitera le nombre d'envois de messages marketeurs qu'un utilisateur peut recevoir dans toutes les entreprises au cours d'une période donnée, en commençant par les messages les moins susceptibles d'être lus. 

Il existe une exception : si une personne répond à un message marketeur, cela déclenchera une fenêtre de service à la clientèle de 24 heures. Les messages marketing envoyés dans cette fenêtre ne sont pas pris en compte dans le calcul de la limite d'une personne.

La limite spécifique varie selon l'utilisateur, en fonction de son niveau d'engagement. Pour en savoir plus sur les limites de messages des modèles de marketing par utilisateur de WhatsApp, [cliquez ici.](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates#per-user-marketing-template-message-limits) 

### Janvier 2025 : WhatsApp met en pause l'envoi de messages marketing aux utilisateurs américains à partir du 1er avril.
*Dernière mise à jour janvier 2025*

WhatsApp mettra en pause l'envoi de messages marketing aux utilisateurs américains (personnes ayant un numéro de téléphone américain) à partir du 1er avril 2025. Les [messages d']({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#response-messages) [utilité, de service, d'authentification](https://developers.facebook.com/docs/whatsapp/pricing/) et de [réponse]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#response-messages) seront toujours autorisés aux États-Unis. 

L'envoi de messages marketing (ainsi que tous les autres types de messages) vers tous les autres pays ou régions reste autorisé et ne sera pas affecté.

Meta nous a informés qu'ils font cette mise à jour pour maintenir la santé de l'écosystème WhatsApp aux États-Unis, où WhatsApp se développe rapidement, mais est encore à un stade précoce (par exemple, les messages marketeurs voient un engagement plus faible que dans d'autres régions). Ils continueront à évaluer le moment où le marché américain sera prêt à reprendre les messages marketing.

La réception/distribution de messages marketing à des numéros de téléphone avec des codes régionaux américains sera rejetée par WhatsApp et renverra un code d'erreur de 131049. 

### novembre 2024 : Changements apportés à la politique d'abonnement de WhatsApp
*Dernière mise à jour janvier 2025*

Meta a récemment mis à jour sa [politique d'abonnement](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). Au lieu d'exiger un consentement spécifique à chaque canal, les entreprises peuvent désormais envoyer des messages aux utilisateurs sur la plateforme si.. :

1. La personne a donné son numéro de téléphone.
2. La personne a fourni une autorisation d'abonnement pour l'envoi de messages en général, et pas seulement pour WhatsApp. 

Les entreprises doivent toujours se conformer à toutes les lois locales et suivre les exigences ci-dessous lorsqu'elles obtiennent un abonnement :

- Les entreprises doivent clairement indiquer qu'une personne accepte de recevoir des communications de la part de l'entreprise.
- Les entreprises doivent indiquer clairement le nom de l'entreprise à laquelle la personne s'est abonnée pour recevoir des messages.
- Les entreprises doivent se conformer à la législation en vigueur

Bien que WhatsApp ait assoupli sa politique, Braze recommande toujours de collecter des abonnements personnalisés spécifiques au canal WhatsApp afin de favoriser la meilleure expérience client et les meilleurs taux d'engagement. Comme toujours, vérifiez avec votre équipe juridique ce qui est judicieux pour votre marque.

### novembre 2024 : Mise à jour de la limite de modèles marketing par utilisateur pour les personnes résidant aux États-Unis, à l'approche des fêtes de fin d'année.
*Dernière mise à jour : décembre 2024*

Depuis que Meta a déployé la limite des modèles marketing par utilisateur, Meta a constaté des améliorations significatives dans les taux de lecture et le sentiment des utilisateurs.
 
À partir de maintenant, avant les fêtes de fin d'année, les Américains recevront moins de nouvelles conversations marketeurs. Meta s'attend à ce que ce changement crée des audiences plus engagées, ce qui, en fin de compte, se traduit par de meilleurs résultats pour les entreprises. Cela peut se traduire par des taux de réception/distribution plus faibles pour votre entreprise si vous envoyez des messages marketing à des numéros de téléphone américains, ce qui peut être contrôlé avec le code d'erreur `131049` par l'intermédiaire de Braze Currents et du Message Activity Log (journal d'activité des messages).

Les entreprises aux États-Unis peuvent toujours diffuser des messages marketing dans d'autres zones géographiques, et il n'y a pas d'impact sur les messages d'utilité, d'authentification ou de service, ou sur les messages de modèles marketing envoyés dans une fenêtre de conversation initiée par l'utilisateur (par exemple, une publicité ou un carrousel de produits ou un modèle de coupon cliquable vers WhhatsApp qui est envoyé dans le cadre d'une conversation). 

### novembre 2024 : WhatsApp étend l'application des règles de qualité des comptes aux taux de lecture
*Dernière mise à jour : décembre 2024*

WhatsApp investit en permanence dans de nouveaux moyens d'aider les entreprises à créer des expériences de qualité pour leurs clients, notamment en réduisant les comportements de type spam sur sa plateforme. 

Le 22 novembre, WhatsApp a commencé à étendre ses mesures d'application de la qualité au niveau des comptes existants pour les comptes professionnels WhatsApp (WABA) dont le taux de lecture est extrêmement bas. Cette modification sera mise en œuvre à l'échelle mondiale.

Lorsque le taux de lecture d'un compte chute de manière significative (par exemple, la majorité des messages envoyés par le compte ne sont pas lus), des blocages d'envoi de messages seront appliqués au compte. La gravité du bloc augmentera si les taux de lecture à l'échelle sont constamment faibles. 

Si le taux de lecture du compte est extrêmement bas, les mesures suivantes seront prises :

- Le compte sera bloqué pour l'envoi de messages à l'initiative de l'entreprise. Ils peuvent toujours répondre aux messages envoyés par les clients. Ce blocage initial est un "verrouillage doux" et peut être acquitté en sélectionnant le bouton d'acquittement dans la qualité du compte pour recommencer l'envoi des messages.
- Si le taux de lecture continue à baisser ou reste faible après le verrouillage progressif, les entreprises peuvent être confrontées à une augmentation progressive des mesures d'application (par exemple, quelques jours de restrictions sur les envois de messages).
- Les entreprises devront attendre la limite imposée pour recommencer à envoyer des messages. Si le taux de lecture reste faible après plusieurs verrouillages progressifs, le compte sera finalement radié.

#### Comment se tenir au courant de ces avertissements et de ces mesures d'exécution ?

À l'instar de l'application de la plateforme existante, les entreprises seront informées de ces mesures et pourront en accuser réception en utilisant la page Qualité du compte dans le gestionnaire WhatsApp. Confirmez que vous disposez des coordonnées correctes répertoriées dans le gestionnaire WhatsApp pour tous les administrateurs nécessaires, car les e-mails de notification d'application seront envoyés sur la base de ces informations.

Les notifications concernant les violations graves de la législation sur le spam seront envoyées :

- Apparaît dans le centre de notifications du gestionnaire d'entreprise de WhatsApp.
- Affiché dans une bannière dans le gestionnaire WhatsApp
- Envoyé sous forme d'e-mail à tous les administrateurs définis dans le WhatsApp Business Manager.

### mai 2024 : L'API en ligne/en production/instantanée en Turquie
*Dernière mise à jour : mai 2024*

Meta offre désormais aux entreprises l'accès à l'API Cloud de Türkiye pour l'envoi de messages d'affaires. Auparavant, les entreprises de Turquie pouvaient utiliser WhatsApp Cloud API, mais les utilisateurs de WhatsApp disposant d'un numéro turc ne pouvaient pas envoyer ou recevoir des messages envoyés via Cloud API. 

Meta indique toujours clairement aux utilisateurs lorsqu'ils discutent avec une entreprise hébergée par Meta, et tous les utilisateurs sont tenus d'accepter les conditions d'utilisation de WhatsApp et la politique de confidentialité correspondantes pour procéder à l'envoi de messages professionnels. La mise à jour des conditions de service et de la politique de confidentialité de 2021 en Turquie avait été mise en pause, mais elle est maintenant déployée. Cela ne change rien à l'engagement de Meta en matière de protection de la vie privée : les conversations personnelles continuent d'être protégées par un cryptage de bout en bout, ce qui signifie que seuls vous et le destinataire pouvez les voir. La mise à jour permet aux utilisateurs turcs d'accéder à des fonctionnalités professionnelles facultatives s'ils le souhaitent et offre plus de transparence sur le fonctionnement de WhatsApp.  
 
Les entreprises de l'API Cloud peuvent désormais initier des conversations avec les utilisateurs de WhatsApp avec des numéros turcs, qui renverront désormais un webhook en tant que conversation "envoyée", au lieu du code d'erreur 131026 d'aujourd'hui.

Pour qu'un message professionnel soit "livré" ou "lu", il faut que l'utilisateur accepte les conditions de WhatsApp. Une entreprise ne sera pas facturée si le message n'est pas envoyé.

Les utilisateurs qui reçoivent ou essaient d'envoyer un message à une entreprise de l'API Cloud recevront une notification in-app concernant la mise à jour des conditions, qui indique clairement qu'ils ne peuvent pas envoyer de message à une entreprise de l'API Cloud tant qu'ils n'ont pas accepté la mise à jour de WhatsApp. En outre, les utilisateurs qui enregistrent ou réenregistrent l'application sur leur téléphone seront invités à accepter la mise à jour de WhatsApp.

Lorsqu'un utilisateur accepte la mise à jour, il verra l'envoi message existant du système API Cloud lorsqu'il discutera avec un Business API Cloud.

### mai 2024 : Limites des messages des modèles d'envoi de messages marketing par utilisateur
*Dernière mise à jour : mai 2024*

Meta déploie de nouvelles approches pour maintenir des expériences utilisateur de haute qualité et maximiser l'engagement des messages des modèles marketing sur la plateforme WhatsApp. À partir du 23 mai 2024, ils limiteront le nombre d'envois de messages de modèles marketing que chaque utilisateur individuel peut recevoir de toutes les entreprises avec lesquelles il interagit au cours d'une période donnée, en commençant par un petit nombre de conversations moins susceptibles d'être lues. Notez que la limite est déterminée en fonction du nombre d'envois de messages marketing que cette personne a déjà reçus de la part de n'importe quelle entreprise, et qu'elle n'est pas liée à votre marque en particulier. Toutefois, cela peut avoir une incidence sur la livrabilité de vos messages marketing.

Cette limite ne s'applique qu'aux messages du modèle marketing qui ouvriraient normalement une nouvelle conversation marketing. Si une conversation marketing est déjà ouverte entre votre marque et un utilisateur de WhatsApp, les messages de modèles marketing envoyés à l'utilisateur ne seront pas affectés.

Si un message de modèle marketing n'est pas envoyé à un utilisateur donné en raison de la limite, l'API Cloud renvoie le code d'erreur 131026. Notez toutefois que ces codes d'erreur couvrent un large éventail de problèmes pouvant entraîner la non réception/distribution d'un message et, pour des raisons de confidentialité, Meta ne divulguera pas si le message n'a pas été livré en raison de la limite. Reportez-vous au [document de résolution des problèmes de](https://developers.facebook.com/docs/whatsapp/cloud-api/support#troubleshooting) l'API Cloud pour obtenir une description des raisons de non réception/distribution et savoir ce que vous pouvez faire pour déterminer leur cause sous-jacente.

Si vous recevez l'un de ces codes d'erreur et que vous pensez qu'il est dû à la limite, évitez de renvoyer immédiatement le message du modèle, car cela ne fera qu'entraîner une autre réponse d'erreur. 

Pour plus d'informations sur cette mise à jour de la livrabilité, y compris des détails sur la surveillance de votre livrabilité et d'autres bonnes pratiques pour l'envoi de messages marketing sur WhatsApp, consultez notre récent [article de blog.](https://www.braze.com/resources/articles/meta-introduces-deliverability-updates-for-whatsapp?utm_campaign=fy25-q2-global-customer-customer-meta-deliverability-updates-for-whatsapp&utm_medium=email-cdb&utm_source=braze&utm_content=blog-meta-deliverability-updates-for-wa-blog)

### avril 2024 : Cadencement des gabarits pour les modèles d'utilité
*Dernière mise à jour avril 2024*

L'année dernière, WhatsApp a introduit le template pacing pour les messages marketing comme un nouveau moyen d'aider les entreprises à améliorer l'engagement de leurs modèles et à créer des expériences utilisateur précieuses. À partir du 30 avril, ils étendent la cadence des modèles aux messages des services publics. Si un modèle d'utilité pour un compte est mis en pause en raison des commentaires des utilisateurs, les nouveaux modèles d'utilité créés pendant les sept jours suivants seront mis en place.

### avril 2024 : Les taux de lecture auront une incidence sur l'évaluation de la qualité des modèles de marketing 
*Dernière mise à jour : mars 2024*

WhatsApp teste de nouvelles approches, en commençant par les consommateurs en Inde, pour créer des expériences plus utiles et maximiser l'engagement dans les conversations marketing des entreprises. Il peut s'agir de limiter le nombre de conversations marketing qu'une personne reçoit de la part d'une entreprise au cours d'une période donnée, en commençant par un petit nombre de conversations qui sont moins susceptibles d'être lues. Braze obtient un code d'erreur si un message n'est pas envoyé.

WhatsApp va commencer à prendre en compte les taux de lecture dans le cadre de notre évaluation de la qualité des modèles marketing, aux côtés des indicateurs traditionnels tels que les blocs et les rapports. WhatsApp peut temporairement mettre en pause les campagnes de messages marketing dont le taux de lecture est faible, ce qui donne aux entreprises le temps d'itérer sur les modèles dont l'engagement est le plus faible avant d'augmenter le volume à partir du 1er avril 2024. 

### février 2024 : Conversations marketeurs Expérimentation
*Dernière mise à jour : février 2024*

À partir du 6 février 2024, WhatsApp teste de nouvelles approches, en commençant par les consommateurs en Inde, pour créer des expériences plus précieuses et maximiser l'engagement des clients avec les conversations marketing de votre marque. Il peut s'agir de limiter le nombre de conversations marketing qu'un utilisateur reçoit de votre marque au cours d'une période donnée, en commençant par un petit nombre de conversations moins susceptibles d'être lues.

### octobre 2023 : Modèles de rythme 
*Dernière mise à jour octobre 2023*

À partir du 12 octobre 2023, WhatsApp introduit un concept appelé "template pacing" pour les messages marketing. Au lieu d'envoyer votre message à toute l'audience de votre campagne simultanément, le "template pacing" diffuse d'abord le message à un sous-ensemble plus restreint d'utilisateurs afin de recueillir les réactions en temps réel des destinataires de la campagne avant d'envoyer les autres messages. 

La "limite de rythme" (le sous-ensemble initial de messages envoyés) est variable en fonction du modèle. Après l'envoi initial, WhatsApp conserve les messages restants pendant un maximum de 30 minutes. Pendant cette période d'attente, ils évaluent la qualité du modèle sur la base des commentaires des clients. Si le retour d'information est positif, signe d'un modèle de haute qualité, ils transmettent les autres messages. Si les commentaires sont négatifs, ils abandonnent les messages restants non délivrés, ce qui évite d'autres commentaires négatifs de la part d'une plus grande partie de vos clients et vous aide à éviter les problèmes potentiels liés à l'application de la qualité (tels que l'impact de l'évaluation de la qualité d'un numéro de téléphone). 

Notez que WhatsApp utilise le même système d'évaluation de la qualité des modèles pour l'accélération des modèles que pour la mise en pause des modèles. Ainsi, les messages non délivrés pendant le template pacing (en raison de modèles de mauvaise qualité) sont les mêmes que ceux qui auraient été mis en pause à plus grande échelle. 

En fin de compte, cette mise à jour vous offre une boucle de rétroaction plus rapide (30 minutes contre des heures ou des jours avec la mise en pause des modèles), afin que vous puissiez ajuster vos modèles et offrir une meilleure expérience client.

**Si vous avez d'autres questions concernant cette mise à jour, n'hésitez pas à contacter votre conseiller partenaire Meta.**

### juin 2023 : Expérimentation de l'envoi de messages 
*Dernière mise à jour juin 2023*

À partir du 14 juin 2023, Meta introduit de nouvelles pratiques d'expérimentation sur la plateforme WhatsApp afin d'évaluer l'impact des messages marketing sur l'expérience et l'engagement des consommateurs. Cette expérience peut avoir une incidence sur vos messages marketing envoyés sur l'API WhatsApp Business avec Braze.

Meta a l'intention de poursuivre cette expérience sur la plateforme WhatsApp. Veuillez consulter la [documentation de Meta](https://developers.facebook.com/docs/whatsapp/on-premises/guides/experiments?content_id=86oue5PtwEgcBJl) pour plus d'informations.

**L'expérimentation de WhatsApp ne concerne que les messages marketing.** Cette expérience pourrait avoir un impact sur la réception/distribution des messages marketeurs. Les modèles d'utilité et d'authentification continueront d'être fournis sans impact sur l'expérimentation.

Dans le cadre de l'expérience, Meta choisit au hasard environ 1 % des consommateurs de WhatsApp comme participants. S'il est choisi, Meta n'enverra pas de modèles de messages marketing à ces consommateurs, sauf si l'une des conditions suivantes est remplie :

- Si un consommateur vous a répondu au cours des dernières 24 heures ;
- Si une conversation marketing existante est ouverte ; ou
- Si le consommateur a cliqué sur une publicité WhatsApp au cours des 72 dernières heures.

## Questions fréquemment posées {#faq}

### Comment saurai-je si mon message marketeur a été affecté par l'expérience de Meta ?

Si un message n'est pas envoyé en raison de l'expérience, un code d'erreur spécifique apparaîtra dans le journal d'activité et dans Currents. Le message sera également comptabilisé comme un échec et incorporé dans vos indicateurs d'échecs WhatsApp dans tous les rapports du tableau de bord de Braze. Ces messages ne vous seront pas facturés.

Ce code d'erreur 130472 indiquera "Le numéro de l'utilisateur fait partie d'une expérience". Veuillez consulter la [documentation de Meta](https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes?content_id=8SJRLBEjYGvXO9k) pour plus d'informations sur les codes d'erreur de l'API WhatsApp Cloud.

### Puis-je m'abonner à l'expérience Meta ?

Non, Meta n'autorise aucun abonnement à l'expérience. Tous les fournisseurs et utilisateurs de l'API WhatsApp Business sont soumis à cette méta-expérience.

### Puis-je essayer de renvoyer un modèle plus tard ?

Il n'y a pas de durée fixe pour cette expérience. Ainsi, un consommateur peut continuer à être soumis à l'expérience.

### Que puis-je faire si mes messages marketeurs ne sont pas délivrés en raison de l'expérience de Meta ?

Nous vous recommandons d'utiliser d'autres canaux de Braze, tels que les e-mails, les SMS, les notifications push ou les messages in-app pour envoyer un message au contenu similaire aux utilisateurs auxquels vous vous adressez.
