---
nav_title: "A2P 10DLC"
article_title: A2P 10DLC
page_order: 2.9
description: "Cet article couvre A2P 10DLC, pourquoi l'enregistrement 10DLC est nécessaire pour les clients de code long aux États-Unis des coûts utiles et des informations de débit, et comment commencer avec l'inscription."
page_type: Référence
channel:
  - SMS
---

# Codes longs à 10 chiffres de l'application à personne (A2P 10DLC)

> A2P 10DLC fait référence à un système aux États-Unis qui permet aux entreprises d'envoyer des messages de type Application-to-Person (A2P) via un numéro de téléphone standard à 10 chiffres long code (10DLC). Ces codes longs enregistrés reçoivent un débit plus élevé, une meilleure délivrabilité et une meilleure conformité par rapport au code standard long.

{% alert important %}
Tous les clients qui ont et/ou utilisent actuellement des codes longs américains pour envoyer aux clients américains sont tenus d'enregistrer leurs codes longs pour 10DLC ; ceux qui ne le font pas connaîtront un filtrage intensif de tous les messages.
{% endalert %}

## Pourquoi c'est nécessaire

Le service 10DLC a été créé pour faciliter spécifiquement la messagerie A2P en utilisant des codes longs. Historiquement, de longs codes étaient destinés aux messages de personne à personne (P2P) mais utilisés pour des raisons de marketing. elles ont fait que les entreprises sont contraintes par un débit limité et un filtrage plus important.

10DLC aide à soulager ces problèmes en offrant :
- __Débit supérieur__: Les nombres 10DLC supportent un volume de messages supérieur à des codes longs réguliers.
- __Une meilleure livrabilité__: les numéros 10DLC sont désignés pour le trafic A2P, de sorte que les messages envoyés avec ces numéros sont plus susceptibles d'atteindre le destinataire et sont moins susceptibles d'être filtrés ou rejetés par le transporteur que les messages envoyés via des codes locaux réguliers.
- __Conformité améliorée__: L'utilisation d'un code local long pour la messagerie texte commerciale est contraire aux lignes directrices [CTIA](https://api.ctia.org/wp-content/uploads/2019/07/190719-CTIA-Messaging-Principles-and-Best-Practices-FINAL.pdf). Les numéros 10DLC ont été désignés pour la messagerie de masse et permettent aux marques de se conformer à la réglementation de l'industrie sans compter sur des codes courts.
- __Budget Friendly__: 10DLC est une excellente option pour les entreprises qui veulent commencer à envoyer des SMS ou envoyer des SMS en petits volumes. Pour les marques envoyant à des volumes de messagerie plus importants de plus de 100 000 messages par jour, Braze recommanderait d’utiliser un code court.

Depuis 2019, les transporteurs ont commencé à adopter 10DLC pour les messages commerciaux, avec Verizon et AT&T prenant actuellement en charge 10DLC, et nous attendons de tous les principaux transporteurs de suivre bientôt. Même si cela peut causer des inconvénients à court terme, à long terme, les clients bénéficieront de meilleurs taux de délivrabilité tout en protégeant leurs consommateurs contre les messages indésirables.

## Ce que vous avez besoin de savoir

### Coûts

L'inscription à A2P 10DLC peut inclure plusieurs types de frais :

| Type de frais                   | Libellé                                                                                                                                                                                                                                                                                                       |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Frais d'inscription             | Frais nominaux appliqués lors de l'enregistrement de votre marque et de votre cas d'utilisation sur tous les principaux réseaux américains.                                                                                                                                                                   |
| Frais de prélèvement secondaire | Les marques peuvent faire appel à leur [Score de la marque](#trust-score) et demander un processus de contrôle secondaire pour améliorer leur débit global ; il y a des frais associés à ce processus.                                                                                                        |
| Frais de transporteur           | Frais facturés par les transporteurs pour les messages SMS sortants et MMS envoyés aux utilisateurs une fois enregistrés pour 10DLC. À compter du 1er octobre 2021, les frais de transporteur seront plus élevés pour le trafic non enregistré (codes standards longs) que pour le trafic enregistré (10DLC). |
{: .reset-td-br-1 .reset-td-br-2}

Visitez l'article Twilio 10DLC pour consulter les [estimations des frais](https://support.twilio.com/hc/en-us/articles/1260803965530-What-pricing-and-fees-are-associated-with-the-A2P-10DLC-service-) mises à jour.

### Débit

Le débit de vos messages pour votre 10dlc dépend de plusieurs facteurs, dont le score de confiance de la marque, les limites quotidiennes des messages et les cas d'utilisation de vos messageries.

#### Score de confiance de la marque {#trust-score}

Le Registre de campagne (TCR) est une agence tierce qui utilise un algorithme de réputation pour examiner des critères spécifiques relatifs à votre entreprise et attribuer une note de confiance qui détermine le débit de la messagerie pour chaque marque. Ce score de confiance sera attribué lorsqu'un client s'inscrit pour la messagerie US 10DLC. Plus le score de confiance est élevé, plus les messages par seconde (MPS) seront élevés.

|         | Score de confiance | AT&T   | T-Mobile | Verizon |
| ------- | ------------------ | ------ | -------- | ------- |
| Élevé   | 76-100             | 60 MPS | 60 MPS   | 60 MPS  |
| Moyenne | 51-75              | 10 MPS | 10 MPS   | 10 MPS  |
| Bas     | 16-50              | 1 MPS  | 1 MPS    | 1 MPS   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert tip %}
Les entreprises inscrites à l’indice Russel 3000 recevront un résultat de confiance et de rendement élevé après l’enregistrement et l’examen de 10DLC.
{% endalert %}

#### Limites de messages quotidiens

Les limites journalières varient de 2 000 à 200 000 messages selon le score de votre marque et s'appliquent à tous les codes longs. Alors que les scores élevés de la marque en fiducie sont fournis avec un débit de 60 messages par seconde, toutes les limites de messages quotidiens fixées par le transporteur s'appliqueront toujours. Cela signifie que les codes courts seraient une meilleure option si les messages de pointe quotidiens d'une marque sont plus élevés que la limite quotidienne imposée.

#### Cas d'utilisation des messages

Le débit est également affecté par le type de cas d'utilisation de la messagerie que vous choisissez. La plupart des clients seront dans le cadre du marketing standard ou du marketing mixte. D'autres cas d'utilisation moins courants seront susceptibles de différer les valeurs de débit.

Selon votre cas d'utilisation, le score de confiance nécessaire pour atteindre le débit maximum variera. Les tableaux ci-dessous listent les cas d'utilisation standard et les plages de scores de confiance en cas d'utilisation courante. Pour des cas d'utilisation spéciale, tels que les services d'urgence ou les organismes de bienfaisance, veuillez consulter les [documentation Twilio](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US).

| Cas d'utilisation standard    | Libellé                                                                                 |
| ----------------------------- | --------------------------------------------------------------------------------------- |
| Marketing                     | Contenu promotionnel comme les ventes et les offres à durée limitée.                    |
| Mixte                         | Campagne qui couvre des cas d'utilisation multiples tels que le service à la clientèle. |
| Enseignement supérieur        | Campagnes pour les établissements d'enseignement supérieur.                             |
| Vote & Vote                   | Les sondages et les votes non politiques tels que les enquêtes auprès des clients.      |
| PPS                           | Les ASP pour sensibiliser la population à un sujet donné.                               |
| Service à la clientèle        | Support, gestion de compte et autres interactions avec les clients.                     |
| Notifications de distribution | Statut de l'envoi des messages.                                                         |
| Notifications du compte       | Notifications sur l'état d'un compte.                                                   |
| A2F                           | Toute authentification de la vérification de compte telle que l'OTP.                    |
| Alertes de sécurité           | Notification d'un système compromis.                                                    |
| Alertes de fraude             | Messagerie au sujet d'une activité potentiellement frauduleuse.                         |
{: .reset-td-br-1 .reset-td-br-2}

{% tabs %}
{% tab Declared Use Case %}
Un cas d'utilisation déclarée signifie que vous avez choisi un cas spécifique d'utilisation non commerciale (par exemple, 2FA ou avis de compte).

| Score de confiance | Débit total vers les principaux réseaux américains | AT&T   | T-Mobile | Verizon |
| ------------------ | -------------------------------------------------- | ------ | -------- | ------- |
| 76-100             | 180 MPS                                            | 60 MPS | 60 MPS   | 60 MPS  |
| 51-75              | 30 MPS                                             | 10 MPS | 10 MPS   | 10 MPS  |
| 16-50              | 3 MPS                                              | 1 MPS  | 1 MPS    | 1 MPS   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% endtab %}
{% tab Mixed/Marketing Utilisation Cas %}

Les cas d'utilisation mixte/marketing peuvent être enregistrés pour les clients qui veulent envoyer des messages pour des cas d'utilisation multiple à partir du même jeu de chiffres ou pour le marketing.

| Score de confiance | Débit total vers les principaux réseaux américains | AT&T    | T-Mobile | Verizon |
| ------------------ | -------------------------------------------------- | ------- | -------- | ------- |
| 86-100             | 180 MPS                                            | 60 MPS  | 60 MPS   | 60 MPS  |
| 66-85              | 30 MPS                                             | 10 MPS  | 10 MPS   | 10 MPS  |
| 26-65              | 3 MPS                                              | 1 MPS   | 1 MPS    | 1 MPS   |
| 15-25              | 2.2 MPS                                            | 0.2 MPS | 1 MPS    | 1 MPS   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% endtab %}
{% endtabs %}

Visitez l'article Twilio 10DLC pour consulter les [estimations de débit](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US) mises à jour.

## Étapes suivantes

Les clients qui ne sont pas encore inscrits à 10DLC doivent travailler avec leur COM ou CSM pour enregistrer leurs codes longs. __Si les clients ne parviennent pas à enregistrer leurs codes longs, à partir du 1er octobre 2021, tout expéditeur A2P utilisant des codes longs connaîtra un filtrage lourd de tous les messages.__ Atteignez votre CSM pour commencer votre enregistrement 10DLC. 
