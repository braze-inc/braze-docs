---
nav_title: Règlement sur le spam
article_title: Règlement sur le pollupostage
page_order: 4.2
page_type: reference
description: "Cet article fournit des résumés et des ressources sur les différentes réglementations en matière de spam qui peuvent vous concerner ou concerner vos utilisateurs."
channel:
- email
- push
- SMS

---

# Règlement sur le spam

> Plusieurs lois réglementent les expéditeurs de communications électroniques, notamment les e-mails, les notifications push et les SMS. Vous devez toujours être au courant des [réglementations locales](https://en.wikipedia.org/wiki/Email_spam_legislation_by_country) qui peuvent vous concerner ou concerner vos utilisateurs. 

Braze fournit des informations pertinentes basées sur nos propres recherches, mais vous devriez également vous référer au texte intégral de ces lois pour obtenir des détails complets et actualisés.

- [CAN-SPAM](#can-spam)
- [Loi canadienne anti-pourriel](#casl)

## CAN-SPAM

La loi CAN-SPAM de 2003 réglemente les expéditeurs d'e-mails à l'adresse U.S. L'envoi de "tout message électronique dont l'objet principal est la publicité commerciale ou la promotion d'un produit ou d'un service commercial". Vous trouverez plus d'informations sur le site officiel de [la Federal Trade Commission.](http://www.business.ftc.gov/documents/bus61-can-spam-act-compliance-guide-business) 

Le CAN-SPAM comporte sept exigences essentielles :

1. N'utilisez pas d'informations d'en-tête fausses ou trompeuses (telles que "From", "To" et "Reply-To").
2. N'utilisez pas de lignes d'objet trompeuses
3. Identifier le message comme étant une publicité
4. Indiquez aux destinataires votre emplacement/localisation (adresse physique, par exemple).
5. Indiquer aux destinataires comment refuser de recevoir d'autres e-mails de votre part.
6. Respecter les demandes d'abonnement dans les plus brefs délais
7. Surveiller ce que les autres font en votre nom

Les e-mails transactionnels ne sont pas soumis à ces règles, à l'exception du point 1.

## Loi canadienne anti-pourriel (CASL) {#casl}

Le 1er juillet 2014, la loi canadienne anti-pourriel (CASL) entre en vigueur pour les e-mails envoyés aux résidents canadiens. Vous pouvez lire le texte intégral de la loi sur le [site Web du](http://laws-lois.justice.gc.ca/eng/annualstatutes/2010_23/FullText.html) gouvernement du Canada consacré [aux lois sur la justice](http://laws-lois.justice.gc.ca/eng/annualstatutes/2010_23/FullText.html). La loi dit essentiellement que les destinataires canadiens des e-mails et des notifications push doivent fournir un consentement "explicite ou implicite" à votre communication avec eux.

### CASL contre CAN-SPAM

Il existe quelques différences essentielles entre la CASL et le CAN-SPAM, notamment :

- La CASL s'applique à l'endroit où le message est reçu, de sorte que les expéditeurs à l'étranger sont concernés.
- Les destinataires des messages doivent opter pour l'opt-in, au lieu de l'opt-out.

### Responsabilité

Bien que la CASL soit assortie d'une période de transition de trois ans, qui prendra fin le 1er juillet 2017, le Conseil de la radiodiffusion et des télécommunications canadiennes (CRTC), le Bureau de la concurrence et le Commissariat à la protection de la vie privée du Canada peuvent entamer des enquêtes et des litiges au cours de cette période. À la fin de la période de transition, les particuliers pourront également intenter une action en justice contre les entités qu'ils soupçonnent d'envoyer des pourriels.

### Envois de messages exemptés

Les types de messages suivants sont exemptés des exigences de la CASL :

- Messages ouverts à l'étranger
- Messages aux membres de la famille ou à d'autres relations personnelles
- les messages adressés à des personnes associées à votre entreprise, y compris des employés ou des sous-traitants
- Messages fournissant des informations sur la garantie, le rappel de produits ou la sécurité d'un produit ou d'un service que le destinataire a utilisé ou acheté.
- Messages de notification d'informations factuelles concernant l'abonnement, l'adhésion ou le compte.
- Messages d'envoi d'un produit ou d'un service, y compris les mises à jour ou les mises à niveau de produits.

>  Cette liste d'exemptions n'est pas exhaustive. Consultez le [texte complet de la loi](http://laws-lois.justice.gc.ca/eng/annualstatutes/2010_23/FullText.html) pour plus de détails.

### Envoi de messages

Braze demande un consentement explicite pour tous les e-mails et les envois de SMS/MMS.

#### Consentement implicite

Le consentement implicite peut être légalement autorisé dans certaines juridictions, mais n'est pas suffisant pour l'envoi d'e-mails par l'intermédiaire de Braze. Notre politique d'utilisation acceptable va au-delà des exigences légales.

#### Consentement explicite

Le consentement explicite est une confirmation écrite ou orale du destinataire du message et n'est valable que si le message comporte une description claire et simple :

- Raison pour laquelle le consentement est demandé
- La personne ou l'organisation qui demande le consentement

## Filtres anti-spam

Ce n'est pas parce que vos e-mails ont été envoyés avec succès qu'ils ont nécessairement été vus. Il n'existe pas de solution miracle pour éviter tous les filtres anti-spam, car chaque filtre est unique dans sa manière d'évaluer le "score de spam" d'un e-mail. Cependant, voici quelques conseils pour éviter que vos e-mails soient qualifiés de "spam".

### Obtenir une autorisation

Un processus de double abonnement consiste à envoyer un e-mail de suivi avec un lien de confirmation après un premier abonnement. Cela permet de valider le fait que les destinataires souhaitent recevoir votre contenu. Vous pouvez également aller plus loin en demandant aux utilisateurs de vous ajouter à leur carnet d'adresses. Veillez également à développer vos listes d'e-mails de manière organique - les listes achetées ont tendance à être périmées !


### Créez votre réputation

Veillez à définir les attentes des personnes qui s'inscrivent pour recevoir vos e-mails. Soyez explicite sur ce que vous allez envoyer et sur la fréquence de vos envois. Ensuite, encouragez les utilisateurs à interagir avec vos campagnes d'e-mail en leur fournissant un contenu de valeur. Un contenu personnalisé et pertinent réduit la probabilité que vos destinataires considèrent les messages comme du spam.

### Maintenir votre réputation

Restez en contact permanent avec vos utilisateurs pour éviter que vos listes d'e-mails ne deviennent obsolètes. Si vous attendez trop longtemps pour envoyer un message, le destinataire risque de vous oublier et de vous marquer comme spam. Maintenez vos listes d'e-mails à jour en mettant en œuvre une politique de temporisation pour supprimer les adresses e-mail qui rebondissent. Le taux de rebond est un facteur clé utilisé par les FAI pour évaluer la réputation d'un expéditeur.

### Vérifier et tester

Veillez à ce que votre message ne contienne aucun élément susceptible de déclencher des filtres anti-spam. Il s'agit notamment des étiquettes superflues provenant d'éditeurs de texte externes tels que Microsoft Word, d'une mise en forme anormale du texte, d'une utilisation excessive des points d'exclamation ( !) et d'interrogation ( ?) comme ponctuation, de l'écriture en TOUTES CAPS et des mots déclencheurs de spam. Envoyez des e-mails au contenu variable en utilisant les fonctionnalités de test multivarié pour vous assurer que vos e-mails n'iront pas dans le courrier indésirable.

## Canal de communication

### e-mail {#spam-email}

La qualité de votre liste d'e-mails est particulièrement importante.  Une poignée de mauvais e-mails sur votre liste peut ruiner votre réception/distribution pour un million de bons utilisateurs. La collecte d'une liste de mauvais e-mails génère des rebonds, une mise en liste bloquée, des visites dans les pièges à spam et réduit vos taux de réponse. La première étape consiste à éliminer les e-mails qui n'ont pas d'activité régulière et à supprimer les rebonds évidents. Que vous mettiez en œuvre un système d'opt-in (cocher la case), d'opt-out (décocher la case), d'opt-in de confirmation (un e-mail qui remercie pour l'inscription et fournit un lien de désabonnement) ou de double opt-in (un e-mail qui nécessite un clic pour confirmer), ce à quoi vous devez penser est la qualité de la liste.

### iOS {#spam-ios-windows}

Dans iOS, il a toujours été demandé à vos utilisateurs d'accepter les notifications push. La boîte de dialogue iOS s'affiche simplement à l'entrée de l'application et demande à l'utilisateur d'opter pour les notifications de votre application. L'utilisateur de l'application voit le même message s'afficher lorsqu'il ouvre l'application pour la première fois, de sorte que toutes les personnes figurant sur votre liste iOS pour les notifications push ont, par définition, opté pour l'abonnement.

### Android {#spam-android}

Dans Android, vos utilisateurs finaux peuvent supposer qu'ils bénéficient d'un abonnement implicite indiqué dans votre politique de confidentialité ou dans votre contrat de licence d'utilisateur final. Vous pouvez mettre en place un processus d'abonnement explicite, par exemple dans un écran initial lorsque l'utilisateur démarre l'application pour la première fois. Consultez l'article sur les [meilleures pratiques de Push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/) pour plus de détails. Vous pouvez également orienter l'utilisateur sur les types de notifications push qu'il recevra, ce qui augmente le taux d'abonnement.

