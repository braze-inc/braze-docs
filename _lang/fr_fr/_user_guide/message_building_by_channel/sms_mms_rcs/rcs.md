---
nav_title: "RCS"
article_title: À propos des services de communication riches (RCS)
alias: /about_rcs/
page_type: reference
page_order: 14
description: "Cet article de référence couvre les cas d'utilisation généraux du canal RCS et les conditions requises pour que votre canal RCS soit prêt à l'emploi."
---

# À propos des services de communication riches (RCS)

> Les services de communication riches (RCS) améliorent les SMS traditionnels en permettant aux marques d'envoyer des messages non seulement informatifs, mais aussi beaucoup plus attrayants. Désormais pris en charge sur Android et iOS, RCS apporte des fonctionnalités telles que des médias de haute qualité, des boutons interactifs et des profils d'expéditeur de marque directement dans les applications d'envoi de messages préinstallées des utilisateurs, éliminant ainsi le besoin de télécharger une application distincte.

Contrairement aux applications de messagerie tierces, RCS exploite l'environnement de messagerie natif (Apple Messages et Google Messages), ce qui vous permet d'atteindre les utilisateurs là où ils passent déjà le plus clair de leur temps et d'aller au-delà des expériences SMS et MMS traditionnelles en permettant une communication plus riche et plus interactive avec les clients. 

## Avantages de l'utilisation du RCS

- **Des expériences clients plus riches :** Offrez des expériences utilisateur plus riches en intégrant de façon fluide des textes, des visuels et des éléments interactifs, ce qui stimule l'engagement et ouvre la voie à des campagnes personnalisées et basées sur des données.
- **Interactions de confiance et de marque :** Obtenez des interactions de marque fiables grâce à un ID d'expéditeur vérifié qui non seulement met en valeur les ressources de votre marque, mais respecte également les normes de confidentialité les plus strictes du secteur, renforçant ainsi la confiance et la fidélité de vos clients.
- **Réception/distribution flexible des messages :** Facilitez la réception/distribution de messages flexibles et fiables grâce à une solution de repli SMS transparente qui permet d'atteindre tous les segments de l'audience, quelles que soient les capacités de l'appareil, tout en préservant une expérience homogène pour l'utilisateur.
- **Informations exploitables :** Débloquez des informations exploitables grâce à des rapports avancés qui suivent les indicateurs clés de performance, ce qui vous permet d'optimiser les campagnes en temps réel et d'obtenir un succès mesurable.
- **Synergie omnicanale :** Intégrez de façon fluide/sans heurts/de façon homogène le RCS dans votre stratégie marketing globale pour offrir des expériences client cross-canal cohérentes, en amplifiant l'efficacité des campagnes et le retour sur investissement global.

## Cas d'utilisation

| Cas d'utilisation | Description |
| --- | --- |
| Promotions interactives des produits | Donnez vie aux promotions de produits en combinant des images attrayantes ou de courtes vidéos avec des documents détaillés sur les produits. Tirez parti des réponses suggérées (telles que "Ajouter au panier" ou "Apprendre") et des actions openURL pour favoriser l'exploration immédiate des produits et la conversion, le tout dans le cadre d'une expérience de communication enrichie. |
| Mises à jour personnalisées sur la fidélité et les récompenses | Envoyez des messages de personnalisation enrichis de visuels de haute qualité et de détails sur les récompenses. Utilisez les réponses suggérées (comme "Échangez maintenant" ou "Voir les offres") et les actions openURL pour créer un parcours client interactif, en rendant chaque mise à jour visuellement attrayante et personnalisée pour inspirer un engagement immédiat et une rétention accrue. |
| Alertes sécurisées sur les transactions et les comptes | Envoyez des alertes de compte et des notifications de transaction sécurisées en incluant des images de reçus ou de documents PDF. Les actions suggérées (telles que "Réviser maintenant" ou "Contacter le support") et les liens openURL permettent aux clients d'accéder rapidement à plus de détails ou d'initier des étapes de sécurité, renforçant à la fois la fiabilité et la confiance dans chaque interaction. |
| Itinéraire de voyage & Amélioration des réservations | Améliorez l'expérience du voyage en envoyant des itinéraires, des guides de destination ou des cartes d'embarquement visuellement riches. Grâce aux actions openURL, les clients peuvent rapidement accéder aux modifications de réservation ou aux mises à jour en temps réel (comme les changements de planification) sans quitter la fenêtre d'envoi des messages, ce qui facilite un parcours de voyage fluide et engageant du début à la fin. |
| Retour d'information sur les clients et enquêtes interactives | Obtenez un retour d'information exploitable en déployant des enquêtes interactives qui utilisent un mélange de contenu multimédia et de texte. Intégrez des suggestions de réponses pour des réponses rapides et des actions openURL pour accéder à des formulaires d'enquête plus complets, ce qui permet aux clients de partager leur opinion en toute simplicité et aide les marketeurs à affiner leurs stratégies en fonction des retours d'information en temps réel provenant de tous les secteurs verticaux. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Exigences

| Exigence | Description |
| --- | --- |
| Crédits du message | Contactez votre gestionnaire de compte Braze pour confirmer que vous avez acheté des crédits de messages dans votre contrat. Les crédits de messages sont un élément contractuel flexible qui vous permet d'acheter et d'allouer un volume d'envoi de messages sur différents canaux, tels que les SMS, les MMS, le RCS et WhatsApp. |
| Pays éligible | Assurez-vous que vous envoyez du RCS à des utilisateurs situés dans l'un des pays pris en charge par Braze : États-Unis, Royaume-Uni, Allemagne, Mexique, Suède, Espagne, Singapour, Brésil, France, Italie, Colombie |
| Expéditeur vérifié du RCS | L'expéditeur que le destinataire voit sur son appareil pour identifier la provenance du message. Un expéditeur vérifié par RCS se compose d'un nom de société, d'une marque visuelle et d'un badge vérifié. <br><br> Braze vous aidera à postuler et à vous inscrire en tant qu'expéditeur vérifié par le RCS dans les régions éligibles. Vous devrez fournir quelques informations de base à votre conseiller Braze. |
| Liste des utilisateurs avec numéros de téléphone | Avant de pouvoir commencer à envoyer des messages, vous devez ajouter des utilisateurs à votre compte. En outre, vous devez connaître la taille approximative de votre audience. Les utilisateurs et les numéros de téléphone peuvent être ajoutés à Braze de différentes manières. Les numéros de téléphone doivent être formatés sous la forme d'un numéro à 10 chiffres, ainsi que d'un code régional pour le pays. Pour en savoir plus, consultez la rubrique [Numéros de téléphone des utilisateurs]({{site.baseurl}}/user_phone_numbers/). |
| Mots clés et réponses | Tous les mots-clés de base doivent se voir attribuer des réponses avant que vous puissiez commencer à envoyer des messages. Braze traitera automatiquement les mots-clés d'abonnement, d'exclusion et d'aide. Des options de personnalisation et des configurations supplémentaires de réponse par mot-clé sont disponibles. Pour en savoir plus, consultez les [mots-clés d'abonnement et d'exclusion.]({{site.baseurl}}/optin_optout/) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Termes à connaître

| Durée | Définition |
|----|----|
| Groupe d'abonnement | Groupe d'utilisateurs abonnés à un cas d'utilisation de messages spécifique. Chaque groupe d'abonnement est lié à un ou plusieurs "expéditeurs" de la marque, qui peuvent être des expéditeurs vérifiés par RCS, des codes SMS, ou les deux. Par exemple, si vous prévoyez d'envoyer des messages RCS transactionnels et promotionnels, vous pouvez choisir de configurer deux subscription groups avec des expéditeurs vérifiés RCS distincts dans votre tableau de bord Braze. |
| Expéditeur vérifié par le RCS | L'entité d'envoi d'un message RCS, ou ce que le destinataire du message RCS voit sur son appareil pour identifier la provenance du message. Les expéditeurs vérifiés par RCS contiennent un nom d'entreprise, une légende, une marque visuelle et un badge vérifié. Une fois que vous avez fourni à Braze les informations nécessaires à l'enregistrement de l'expéditeur RCS, nous nous chargeons de l'enregistrement et de la configuration des groupes d'abonnement. |
| Repli sur le SMS | Si un message ne peut pas être envoyé par RCS (par exemple, absence de prise en charge par l'opérateur dans la région), Braze tentera tout de même d'envoyer le message par SMS lorsqu'un code SMS existe dans le groupe d'abonnement. |
| RCS de base | Envois de messages en texte seul jusqu'à 160 caractères. Facturé comme un message unique. <br><br> Cette catégorie n'est utilisée que dans le modèle global. |
| RCS unique | Les messages en texte seul de plus de 160 caractères **ou** comprenant des éléments riches, tels que des boutons ou des médias. <br><br>Cette catégorie n'est utilisée que dans le modèle global. |
| Riche | Messages en texte seul, avec ou sans suggestions ou boutons limités. Facturation par segment (160 octets UTF-8). Par exemple, un message contenant 161 caractères de texte en clair correspond à deux segments. <br><br> Cette catégorie n'est utilisée que dans le modèle des États-Unis. |
| Médias riches | Messages comprenant un fichier multimédia (image, vidéo) ou une carte enrichie. Facturé comme un seul message, quelle que soit la longueur du message. <br><br> Cette catégorie n'est utilisée que dans le modèle des États-Unis. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
