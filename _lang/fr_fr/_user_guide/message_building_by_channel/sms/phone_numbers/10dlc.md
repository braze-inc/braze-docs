---
nav_title: "A2P 10DLC"
article_title: A2P 10DLC
page_order: 2.9
description: "Le présent article couvre l’A2P 10DLC, les raisons pour lesquelles l’inscription 10DLC est nécessaire pour les clients code long des États-Unis, les frais utiles et les informations de débit, et la manière de commencer avec l’inscription."
page_type: reference
channel:
  - SMS
  
---

# Codes longs à 10 chiffres application à personne

> A2P 10DLC fait référence à un système aux États-Unis qui permet aux entreprises d’envoyer des communications de type Application à personne (A2P) via un numéro de téléphone standard à 10 chiffres en code long (10DLC). Ces codes longs enregistrés bénéficient d’un débit plus élevé, d’une meilleure livrabilité et d’une conformité meilleure que celle du code long standard.

{% alert important %}
Tous les clients qui ont actuellement et/ou utilisent des codes longs américains pour envoyer aux clients américains doivent enregistrer leurs codes longs pour 10DLC ; ceux qui ne le font pas connaîtront un filtrage intensif de tous les messages. Ce processus de candidature prend 4 à 6 semaines.
{% endalert %}

## Pourquoi cela est nécessaire

Le service 10DLC a été créé pour faciliter spécifiquement l’envoi de messages A2P en utilisant des codes longs. Historiquement, les codes longs étaient destinés à l’envoi de messages personne à personne (P2P), mais lorsqu’ils sont utilisés pour des raisons marketing, ils ont créé pour les entreprises des contraintes par un débit limité et un filtrage accru. 

10DLC aide à atténuer ces problèmes en offrant : 
- **Débit plus élevé**: Les numéros 10DLC prennent en charge un volume de messages plus élevé que les codes longs ordinaires.
- **Meilleure livrabilité** : Les numéros 10DLC sont conçus pour le trafic A2P. Les messages envoyés avec ces numéros sont plus susceptibles d’atteindre le destinataire et sont moins susceptibles d’être filtrés ou rejetés par l’opérateur que les messages envoyés par le biais de codes longs locaux ordinaires. 
- **Conformité améliorée**: L'utilisation d'un code long local pour les messages texte commerciaux est contraire aux directives [CTIA](https://api.ctia.org/wp-content/uploads/2019/07/190719-CTIA-Messaging-Principles-and-Best-Practices-FINAL.pdf). Les numéros 10DLC ont été conçus pour la communication de masse et permettent aux marques de se conformer aux réglementations du secteur sans s’appuyer sur les codes courts.
- **Abordable** : 10DLC est une excellente option pour les entreprises qui souhaitent commencer à envoyer des SMS ou envoyer des SMS en petits volumes. Pour les marques envoyant des volumes de plus de 100 000 messages par jour, nous recommandons d'utiliser un code court. 

Depuis 2019, les opérateurs ont commencé à adopter 10DLC pour la communication commerciale ; Verizon et AT&T prennent actuellement en charge 10DLC, et nous nous attendons à ce que tous les principaux opérateurs fassent de même. Bien qu’il puisse entraîner des inconvénients à court terme, les clients bénéficieront de meilleurs taux de livrabilité tout en protégeant leurs consommateurs contre les messages indésirables. 

## Ce que vous devez savoir

### Accès

L’enregistrement de codes longs avec A2P 10DLC prendra 4 à 6 semaines.

### Coûts 

L’enregistrement avec A2P 10DLC peut inclure plusieurs types de frais :

| Type de frais | Description |
| -------- | ---------- |
| Frais d’inscription | Des frais minimes s’appliquent lors de l’enregistrement de votre marque et de votre cas d’utilisation sur tous les principaux réseaux américains. |
| Frais de deuxième vérification | Les marques peuvent faire appel de leur [Brand Trust Score](#trust-score) et demander un processus de vérification secondaire pour améliorer leur rendement global ; il y a des frais associés à ce processus. |
| Frais d’opérateur | Frais facturés par les opérateurs pour les messages SMS et MMS sortants envoyés aux utilisateurs après l'enregistrement 10DLC. À compter du 1er octobre 2021, les frais d’opérateur seront plus élevés sur le trafic non enregistré (codes longs standard) que sur le trafic enregistré (10DLC). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Consultez l'article 10DLC de Twilio pour connaître les [estimations de frais](https://support.twilio.com/hc/en-us/articles/1260803965530-What-pricing-and-fees-are-associated-with-the-A2P-10DLC-service-) actualisées.

### Débit

Le débit de messages pour votre 10DLC dépend de plusieurs facteurs, notamment le score de confiance de la marque, les limites quotidiennes de messagerie et vos cas d’utilisation d’envoi de messages.

#### Score de confiance de la marque {#trust-score}

Le registre de campagne (TCR) est une agence tierce qui utilise un algorithme de réputation pour examiner les critères spécifiques liés à votre entreprise et attribuer un score de confiance qui détermine le débit d’envoi de messages pour chaque marque. Ce score de confiance est attribué quand un client s’inscrit pour l’envoi de messages 10DLC aux États-Unis. Plus le score de confiance est élevé, plus le nombre de messages par seconde (MPS) s’améliore. 

|     | Score de confiance | AT&T | T-Mobile | Verizon |
| --- | ----------- | ---- | -------- | ------- |
| Élevée | 75-100 | 75 MPS | 75 MPS | 75 MPS |
| Moyen | 50-74 | 40 MPS | 40 MPS | 40 MPS |
| Faible | 1-49 | 4 MPS | 4 MPS | 4 MPS | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert tip %}
Les sociétés répertoriées dans l’indice Russel 3000 bénéficieront d’un débit élevé et d’un score de confiance de marque après l’inscription 10DLC et sa revue.
{% endalert %} 

#### Maxima quotidiens de messages

Les limites quotidiennes sont de 2 000 à 200 000 messages en fonction du score de confiance de votre marque et s’appliquent à tous les codes longs. Alors que les scores de confiance de marque élevés correspondent à un débit de 60 messages par seconde, toute limite quotidienne de messages définie par l’opérateur s’applique toujours. Cela signifie que les codes courts sont une meilleure option quand les maxima quotidiens de la marque dépassent la limite imposée. 

#### Cas d’utilisation de l’envoi de messages

Le débit est également affecté par le type de cas d’utilisation d’envoi de messages que vous choisissez. La plupart des clients se trouvent dans le cas d’utilisation du marketing standard ou du marketing mixte. D’autres cas d’utilisation moins courants peuvent avoir des valeurs de débit différentes.

Selon votre cas d’utilisation, le score de confiance nécessaire pour atteindre le débit maximal varie. Les tableaux suivants répertorient les cas d’utilisation standard et les plages de score de confiance pour les cas d’utilisation courants. Pour des cas d'utilisation spéciaux tels que les services d'urgence ou les œuvres de charité, consultez la [documentation Twilio](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US).

| Cas d’utilisation standard | Description |
| ------------------ | ----------- |
| Marketing | Contenu promotionnel tel que des ventes et des offres à durée limitée. |
| Mixte | Campagne qui couvre plusieurs cas d'utilisation, tels que le service client. | 
| Enseignement supérieur | Campagnes destinées aux établissements d’enseignement supérieur. |
| Sondage et vote | Sondages et votes non politiques, tels que les enquêtes auprès des clients. |
| Annonce de service public (PSA) | Des annonces pour sensibiliser à un sujet donné. |
| Service client | Assistance, gestion de compte et autres interactions avec la clientèle. |
| Notifications de livraison | Statut des messages de livraison. |
| Notifications de compte | Notifications concernant l’état d’un compte. |
| 2FA | Toute authentification de vérification de compte, telle qu'OTP. | 
| Alertes de sécurité | Notification de compromission d’un système. |
| Alertes de fraude | Envoi de messages au sujet d’une activité potentiellement frauduleuse. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% tabs %}
{% tab Cas d'utilisation déclaré %}
Un cas d’utilisation déclaré signifie que vous avez choisi un cas d’utilisation non marketing spécifique (par exemple, 2FA ou Notifications de compte).

| Score de confiance | Débit total vers les principaux réseaux américains | AT&T | T-Mobile | Verizon |
| --- | ----------- | ---- | -------- | ------- |
| 75-100 | 225 MPS | 75 MPS | 75 MPS | 75 MPS |
| 50-74	 | 120 MPS | 40 MPS | 40 MPS | 40 MPS |
| 1-49 | 12 MPS | 4 MPS | 4 MPS | 4 MPS| 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endtab %}
{% tab Cas d'utilisation marketing mixte %}

Des cas d'utilisation marketing mixtes peuvent être enregistrés pour les clients qui souhaitent envoyer des messages pour plusieurs cas d'utilisation à partir du même ensemble de numéros ou à des fins de marketing.

| Score de confiance | Débit total vers les principaux réseaux américains | AT&T | T-Mobile  | Verizon |
| --- | ----------- | ---- | -------- | ------- |
| 75-100 | 225 MPS | 75 MPS | 75 MPS | 75 MPS |
| 50-74 | 120 MPS | 40 MPS | 40 MPS | 40 MPS |
| 1-49 | 12 MPS | 4 MPS | 4 MPS | 4 MPS| 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endtab %}
{% endtabs %}

Consultez l’article 10DLC de Twilio pour vérifier les dernières [estimations de débit](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US).

## Étapes suivantes

Les clients qui ne se sont pas encore inscrits pour 10DLC doivent contacter leur gestionnaire du succès des clients pour enregistrer leurs codes longs. **Si des clients ne parviennent pas à enregistrer leurs codes longs, à compter du 1er octobre 2021, tout expéditeur A2P utilisant des codes longs connaîtra un filtrage intensif de tous les messages.** Contactez votre gestionnaire du succès des clients pour commencer votre inscription à 10DLC. 
