---
nav_title: Réglementation sur les spams
article_title: Réglementation sur les spams
page_order: 4.2
page_type: Référence
description: "Cet article fournit des résumés et des ressources sur diverses réglementations en matière de spam qui peuvent vous affecter ou affecter vos utilisateurs."
channel:
  - Email
  - Pousser
  - SMS
---

# Règles de spam

Il existe un certain nombre de lois qui régissent les expéditeurs de communications électroniques, y compris les courriels, les notifications push et les SMS. Vous devez toujours être au courant des [réglementations locales][4] qui peuvent vous affecter ou affecter vos utilisateurs. Braze fournit des informations pertinentes basées sur nos propres recherches, mais vous devriez également vous référer au texte intégral de ces lois pour des détails complets et à jour.

- [CAN-SPAM][1]
- [Loi canadienne antispam][2]

## CAN-SPAM

La loi CAN-SPAM de 2003 réglemente les expéditeurs de courriels aux États-Unis. en envoyant "tout message électronique dont l'objectif premier est la publicité commerciale ou la promotion d'un produit ou service commercial". Vous pouvez lire plus de détails sur le site [FTC][5].

Il y a 7 exigences clés pour le CAN-SPAM :

1. N'utilisez pas d'informations d'en-tête fausses ou trompeuses (c.-à-d. "De", "À" et "Répondre à")
2. Ne pas utiliser de lignes de sujet trompeuses
3. Identifier le message comme une annonce
4. Dites aux destinataires où vous vous trouvez (c.-à-d. adresse physique)
5. Dites aux destinataires comment ne pas recevoir de futurs e-mails de votre part
6. Honorer rapidement les demandes de désinscription
7. Surveiller ce que d'autres font en votre nom

Les courriels transactionnels sont exemptés de ces règles, à l'exception du numéro 1.

## Loi canadienne antispam (CASL) {#casl}

Le 1er juillet 2014, la Loi canadienne antispam (LCSP) entrera en vigueur pour les courriels envoyés aux résidents canadiens. Vous pouvez lire le texte complet de la loi [ici][3]. La loi stipule essentiellement que les destinataires canadiens de messages électroniques et de notifications push doivent fournir un consentement « explicite ou implicite » à votre communication avec eux.

### CASL vs CAN-SPAM

Il y a quelques différences importantes entre l'ACPLS et le CAN-SPAM, notamment :

- L'ACHAT s'applique à *où* le message est reçu, donc les expéditeurs en dehors du Canada sont affectés
- Les destinataires du message doivent opt-in, au lieu de l'opt-out

### Responsabilité

Alors que l’ACPLS a une période de transition de trois ans, se terminant le 1er juillet 2017, le Conseil de la radiodiffusion et des télécommunications canadiennes (CRTC), le Bureau de la concurrence et le Commissariat à la protection de la vie privée du Canada peuvent entamer des enquêtes et des litiges au cours de cette période. À la fin de la période de transition, les personnes peuvent également se plaindre contre des entités qui, selon elles, envoient des pourriels.

### Messages exonérés

Les types de messages suivants sont exemptés des exigences de l’ACPLS :

- Messages ouverts à l'extérieur du Canada
- Messages aux membres de la famille ou à d'autres relations personnelles
- Messages aux personnes associées à votre entreprise, y compris aux employés ou aux sous-traitants
- Messages fournissant des informations sur la garantie, des informations de rappel de produit ou des informations de sécurité sur un produit ou un service que le destinataire a utilisé ou acheté
- Messages fournissant une notification d'informations factuelles sur l'abonnement, l'adhésion ou le compte
- Messages fournissant un produit ou un service, y compris des mises à jour de produits ou des mises à jour de produits

> Ce n'est pas la liste complète des exemptions. Veuillez consulter le [texte complet de la loi][3] pour plus de détails.

### Consentement du message

Les messages qui ne tombent pas sous l'une des exemptions requièrent un consentement « explicite ou implicite » de la part du destinataire.

#### Consentement implicite

Le consentement implicite est basé sur une activité antérieure avec un utilisateur dans le cadre d'une relation commerciale ou non commerciale. Les messages peuvent être envoyés en fonction du consentement implicite au cours de la période de transition. Après le 1er juillet 2017, un consentement explicite est exigé, à moins que le consentement implicite soit toujours valide (c'est-à-dire les 2 ans après l'achat).

- Le destinataire d'un message a acheté ou loué un produit, un bien, un service ou une autre entreprise avec votre organisation au cours des 2 dernières années
- L'adresse électronique a été publiée et n'interdit pas explicitement les e-mails non sollicités

Le consentement implicite n'est valide que pendant 6 mois si le destinataire ne devient pas client.

#### Consentement express

Le consentement exprès est écrit ou oral de la part du destinataire du message et n'est valide que si le message contient une description claire et simple de:

- Pourquoi demander un consentement
- La personne ou l'organisation qui sollicite le consentement

## Filtres anti-spam

Ce n’est pas parce que vos courriels ont été envoyés avec succès qu’ils ont été nécessairement vus. Il n'y a pas de solution pour éviter tous les filtres anti-spam car chaque filtre est unique dans la façon dont ils évaluent le « score de la mine de spam » d'un courriel. Cependant, voici quelques conseils pour éviter que vos e-mails ne soient étiquetés comme « spam » :

- Get Permission: Un processus double opt-in consiste à envoyer un e-mail de suivi avec un lien de confirmation après un premier opt-in. Utiliser ceci fournit la validation que les destinataires veulent recevoir votre contenu. Vous pouvez également aller plus loin encore en demandant aux utilisateurs de vous ajouter à leur carnet d'adresses. Assurez-vous également de faire croître vos listes de courriels de façon organique: les listes achetées ont souvent tendance à être obsolètes!

- Construire votre réputation : Assurez-vous de définir les attentes lorsque des personnes s'inscrivent pour recevoir vos e-mails. Soyez explicite sur ce que vous allez envoyer et à quelle fréquence vous allez l'envoyer. Ensuite, encouragez les utilisateurs à interagir avec vos campagnes de courriel en fournissant un contenu précieux. Avoir un contenu personnalisé et pertinent réduit la probabilité que vos destinataires marquent les messages comme du spam.

- Maintenez votre réputation : soyez en contact permanent avec vos utilisateurs pour éviter que vos listes de courriels ne deviennent obsolètes. En attendant trop longtemps pour envoyer un message, le destinataire peut oublier vous et vous marquer comme indésirable. Gardez vos listes de courriels à jour en implémentant une politique de couperet pour supprimer les adresses e-mail qui rebondissent. Les taux de rebond sont un facteur clé utilisé par les FSI pour évaluer la réputation d’un expéditeur.

- Vérifiez et testez : assurez-vous que votre message ne contient rien qui puisse déclencher des filtres anti-spam. Cela inclut des balises superflues provenant d'éditeurs de texte externes comme Microsoft Word, mise en forme de texte anormale, surutilisation de ! et ? sous forme de ponctuation, d'écriture dans TOUTES les majuscules, et de spam les mots déclencheurs (voir [ici][7] pour une liste de mots de déclenchement courants). Envoyez des courriels avec du contenu varié en utilisant les capacités de test multivariées de Braze pour vous assurer que vos courriels ne vont pas spammer.

## Chaîne de messagerie

### Courriel {#spam-email}

La qualité de votre liste de courriels est particulièrement importante.  Une poignée de mauvais courriels sur votre liste peut ruiner votre livraison pour un million de bons utilisateurs. La collecte d'une liste de mauvais e-mails génère des rebondissements, des listes noires, des attaques de spams et des tanks vos taux de réponse. La première étape consiste à abattre les courriels qui n'ont pas d'activité régulière, et à supprimer les rebonds évidents. Si vous implémentez un opt-in (cochez la boîte), opt-out (décochez la boîte), confirmez opt-in (un email qui dit merci de vous inscrire, et donne un lien de désinscription), ou double opt-in (un email qui nécessite un clic pour confirmer), ce que vous voulez penser est la qualité de la liste.

### iOS et Windows {#spam-ios-windows}

Dans iOS, vos utilisateurs ont toujours été invités à opter pour les notifications push. La boîte de dialogue iOS apparaît simplement à l'entrée de l'application et demande à l'utilisateur d'opter pour les notifications à votre application. L'utilisateur de l'application voit apparaître le même message au moment où il ouvre une application pour la première fois ainsi tous ceux qui sont sur votre liste iOS pour les notifications push ont, par définition, opté-in. Windows requiert également des opt-ins explicites de la part de l'utilisateur.

### Android {#spam-android}

Dans Android, vos utilisateurs peuvent supposer être optés par l'opt-in implicite qui est indiqué dans votre politique de confidentialité ou votre contrat de licence d'utilisateur final. Vous pouvez implémenter un processus opt-in exprimé peut-être dans un écran initial, au moment où l'utilisateur lance l'application pour la première fois. Visitez l'article [Push Best Practices][6] pour plus de détails. Vous pouvez également orienter l'utilisateur vers les types de notifications push qu'il va recevoir, augmentant ainsi le taux d'opt-in.

[1]: #can-spam
[2]: #casl
[3]: http://laws-lois.justice.gc.ca/eng/annualstatutes/2010_23/FullText.html
[3]: http://laws-lois.justice.gc.ca/eng/annualstatutes/2010_23/FullText.html
[4]: https://en.wikipedia.org/wiki/Email_spam_legislation_by_country
[5]: http://www.business.ftc.gov/documents/bus61-can-spam-act-compliance-guide-business
[6]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
[7]: http://blog.hubspot.com/blog/tabid/6307/bid/30684/The-Ultimate-List-of-Email-SPAM-Trigger-Words.aspx#sm.00001wbela64xddnmppa99vp1xa8j
