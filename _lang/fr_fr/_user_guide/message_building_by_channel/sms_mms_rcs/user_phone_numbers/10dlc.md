---
nav_title: "A2P 10DLC"
article_title: A2P 10DLC
page_order: 2.9
description: "Cet article traite de l'A2P 10DLC, des raisons pour lesquelles l'enregistrement 10DLC est nécessaire pour les clients américains à code long, des informations utiles sur les coûts et le débit, et de la manière de commencer l'enregistrement."
page_type: reference
channel:
  - SMS
  
---

# Application aux personnes des codes longs à 10 chiffres

> A2P 10DLC désigne un système aux États-Unis qui permet aux entreprises d'envoyer des messages de type Application-to-Person (A2P) via un numéro de téléphone standard à 10 codes longs (10DLC). Ces codes longs enregistrés bénéficient d'un débit plus élevé, d'une meilleure livrabilité et d'une meilleure conformité que le code long standard.

{% alert important %}
Tous les clients qui possèdent et/ou utilisent actuellement des codes longs américains pour envoyer des messages à des clients américains sont tenus d'enregistrer leurs codes longs pour 10DLC ; ceux qui ne le font pas seront confrontés à un filtrage important de tous les messages. Cette procédure de demande prend de 4 à 6 semaines.
{% endalert %}

## Pourquoi c'est nécessaire

Le service 10DLC a été créé pour faciliter spécifiquement l'envoi de messages A2P à l'aide de codes longs. Historiquement, les codes longs étaient destinés à l'envoi de messages de personne à personne (P2P), mais lorsqu'ils étaient utilisés à des fins de marketing, ils entraînaient des contraintes pour les entreprises en raison d'un débit limité et d'un filtrage accru. 

Le 10DLC contribue à atténuer ces problèmes en offrant : 
- **Débit plus élevé**: Les numéros 10DLC prennent en charge un volume d'envois plus important que les codes longs ordinaires.
- **Meilleure livrabilité**: Les numéros 10DLC sont destinés au trafic A2P. Les messages envoyés avec ces numéros ont donc plus de chances d'atteindre le destinataire et risquent moins d'être filtrés ou rejetés par l'opérateur que les messages envoyés avec des codes longs locaux ordinaires. 
- **Amélioration de la conformité**: L'utilisation d'un code long local pour l'envoi de messages commerciaux est contraire aux lignes directrices de [la CTIA](https://api.ctia.org/wp-content/uploads/2019/07/190719-CTIA-Messaging-Principles-and-Best-Practices-FINAL.pdf). Les numéros 10DLC ont été conçus pour l'envoi de messages en masse et permettent aux marques de se conformer aux réglementations du secteur sans avoir recours aux codes courts.
- **Un budget raisonnable**: 10DLC est une excellente option pour les entreprises qui souhaitent commencer à envoyer des SMS ou envoyer des SMS à faible volume. Pour les marques qui envoient des volumes de messages plus importants, supérieurs à 100 000 messages par jour, nous recommandons d'utiliser un code court. 

Depuis 2019, les opérateurs ont commencé à adopter 10DLC pour les messages commerciaux, Verizon et AT&T prenant actuellement en charge 10DLC, et nous nous attendons à ce que tous les principaux opérateurs suivent bientôt. Si cela peut entraîner des désagréments à court terme, à long terme, les clients bénéficieront de meilleurs taux de livrabilité tout en protégeant leurs consommateurs des envois non désirés. 

## Ce que vous devez savoir

### Accès

L'enregistrement des codes longs auprès d'A2P 10DLC prendra de 4 à 6 semaines.

### Coûts 

L'enregistrement auprès d'A2P 10DLC peut donner lieu à plusieurs types de frais :

| Type de frais | Description |
| -------- | ---------- |
| Frais d'inscription | Des frais nominaux sont appliqués lors de l'enregistrement de votre marque et de votre cas d'utilisation sur tous les principaux réseaux américains. |
| Frais de vérification secondaire | Les marques peuvent faire appel de leur [score de confiance](#trust-score) et demander un processus de vérification secondaire afin d'améliorer leur débit global ; ce processus est payant. |
| Frais des transporteurs | Frais facturés par les opérateurs pour les envois de SMS et MMS sortants aux utilisateurs après l'inscription au 10DLC. À partir du 1er octobre 2021, les frais des transporteurs seront plus élevés sur le trafic non enregistré (codes longs standard) que sur le trafic enregistré (10DLC). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Visitez l'article de Twilio 10DLC pour consulter les [estimations de frais](https://support.twilio.com/hc/en-us/articles/1260803965530-What-pricing-and-fees-are-associated-with-the-A2P-10DLC-service-) mises à jour.

### Débit

Le débit des messages pour votre 10DLC dépend de plusieurs facteurs, notamment du score de confiance de la marque, des limites de messages quotidiens et de vos cas d'utilisation des messages.

#### Score de confiance de la marque {#trust-score}

The Campaign Registry (TCR) est une agence tierce qui utilise un algorithme de réputation pour examiner des critères spécifiques relatifs à votre entreprise et attribuer un score de confiance qui détermine le débit d'envoi des messages pour chaque marque. Ce score de confiance est attribué lorsqu'un personnalisé s'inscrit à l'envoi de messages de l'US 10DLC. Plus le score de confiance est élevé, plus les messages par seconde (MPS) sont bons. 

|     | Score de confiance | AT&T | T-Mobile | Verizon |
| --- | ----------- | ---- | -------- | ------- |
| Haut | 75-100 | 75 MPS | 75 MPS | 75 MPS |
| Moyen | 50-74 | 40 MPS | 40 MPS | 40 MPS |
| Faible | 1-49 | 4 MPS | 4 MPS | 4 MPS | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert tip %}
Les entreprises répertoriées dans l'indice Russel 3000 se verront attribuer un score élevé de débit et de confiance dans la marque après l'enregistrement et l'examen du 10DLC.
{% endalert %} 

#### Limites de messages par jour

Les limites quotidiennes vont de 2 000 à 200 000 messages en fonction du score de confiance de votre marque et s'appliquent à tous les codes longs. Si un score de confiance élevé s'accompagne d'un débit de 60 messages par seconde, les limites de messages quotidiennes fixées par l'opérateur restent d'application. Cela signifie que les codes courts constituent une meilleure option si les pics de messages quotidiens d'une marque sont supérieurs à la limite quotidienne imposée. 

#### Cas d'utilisation de l'envoi de messages

Le débit est également influencé par le type d'envoi de messages que vous choisissez. La plupart des clients relèvent du marketing standard ou du marketing mixte. D'autres cas d'utilisation moins courants seront susceptibles de donner lieu à des valeurs de débit différentes.

Selon votre cas d'utilisation, le score de confiance nécessaire pour atteindre le débit maximal variera. Les tableaux suivants répertorient les cas d'utilisation standard et les plages de score de confiance des cas d'utilisation courants. Pour les cas d'utilisation particuliers tels que les services d'urgence ou les œuvres caritatives, reportez-vous à la [documentation de Twilio](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US).

| Cas d'utilisation standard | Description |
| ------------------ | ----------- |
| Marketeur | Contenu promotionnel tel que les ventes et les offres à durée limitée. |
| Mixte | Campagne qui couvre plusieurs cas d'utilisation, comme l'assistance à la clientèle. | 
| Enseignement supérieur | Campagnes pour les établissements d'enseignement supérieur. |
| Bureau de vote & Vote | Sondages et votes non politiques, tels que les enquêtes auprès des clients. |
| PSA | Des messages d'intérêt public pour sensibiliser le public à un sujet donné. |
| Service clientèle | Support, gestion de compte et autres interactions avec les clients. |
| Notifications de réception/distribution | État des messages de réception/distribution. |
| Notifications de compte | Notifications sur le statut d'un compte. |
| 2FA | Toute authentification de la vérification du compte, telle que l'OTP. | 
| Alertes de sécurité | Notification d'un système compromis. |
| Alertes à la fraude | Envoi de messages concernant des activités potentiellement frauduleuses. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% tabs %}
{% tab Declared Use Case %}
Un cas d'utilisation déclaré signifie que vous avez choisi un cas d'utilisation spécifique non marketing (par exemple, 2FA ou Notifications de compte).

| Score de confiance | Débit total vers les principaux réseaux américains | AT&T | T-Mobile | Verizon |
| --- | ----------- | ---- | -------- | ------- |
| 75-100 | 225 MPS | 75 MPS | 75 MPS | 75 MPS |
| 50-74	 | 120 MPS | 40 MPS | 40 MPS | 40 MPS |
| 1-49 | 12 MPS | 4 MPS | 4 MPS | 4 MPS| 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endtab %}
{% tab Mixed Marketing Use Case %}

Des cas d'utilisation marketing mixtes peuvent être enregistrés pour les clients qui souhaitent envoyer des messages pour plusieurs cas d'utilisation à partir du même ensemble de numéros ou à des fins de marketing.

| Score de confiance | Débit total vers les principaux réseaux américains | AT&T | T-Mobile  | Verizon |
| --- | ----------- | ---- | -------- | ------- |
| 75-100 | 225 MPS | 75 MPS | 75 MPS | 75 MPS |
| 50-74 | 120 MPS | 40 MPS | 40 MPS | 40 MPS |
| 1-49 | 12 MPS | 4 MPS | 4 MPS | 4 MPS| 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endtab %}
{% endtabs %}

Consultez l'article sur le 10DLC de Twilio pour vérifier les [estimations de débit](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US) mises à jour.

## Prochaines étapes

Les clients qui ne se sont pas encore inscrits à 10DLC doivent travailler avec leur gestionnaire de satisfaction client pour enregistrer leurs codes longs. **Si les clients n'enregistrent pas leurs codes longs, à partir du 1er octobre 2021, tout expéditeur A2P utilisant des codes longs subira un filtrage important de tous les messages.** Contactez votre gestionnaire satisfaction client pour commencer votre inscription au 10DLC. 
