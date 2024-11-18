---
article_title: Limitation du débit pour les campagnes et les toiles
permalink: /rate_limiting/
page_type: reference
description: "Cet article de référence décrit le comportement antérieur de limitation du débit de réception/distribution de Braze."
---

# Limitation du taux

> Cet article décrit l'ancien comportement de limitation du débit de réception/distribution de Braze. La mise à jour de la limite de débit est décrite [ici.]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting#rate-limiting)

Braze vous permet de contrôler la pression marketing en limitant le débit de vos campagnes et Canvases, en régulant la quantité de trafic sortant de votre plateforme. Vous pouvez mettre en place deux types différents de limite de débit pour vos campagnes :

1. La **réception/distribution limite de débit** prend en considération la bande passante de vos serveurs.
2. La **limite de débit centrée sur l'utilisateur** s'attache à lui offrir la meilleure expérience possible. 

Pour plus d'informations, reportez-vous à la section [À propos de la limite de débit.]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#about-rate-limiting)

## À propos de la limitation du débit de réception/distribution

Si vous prévoyez que de grandes campagnes entraîneront un pic d'activité des utilisateurs et une surcharge de vos serveurs, vous pouvez spécifier une limite de débit par minute pour l'envoi des messages, ce qui signifie que Braze n'enverra pas plus que la limite de débit définie en l'espace d'une minute. 

Lorsque vous ciblez des utilisateurs lors de la création d'une campagne, vous pouvez accéder à **Target Audiences** (pour les campagnes) ou **Send Settings** (pour Canvas) pour sélectionner une limite de débit pour la réception/distribution des messages (par incréments allant de 10 à 500 000 messages par minute). Notez que les campagnes sans limitation du taux peuvent dépasser ces limites de livraison.

Par exemple, si vous essayez d'envoyer 75 000 messages avec une limite de débit de 10 000 par minute, la réception/distribution sera étalée sur huit minutes. Votre campagne n'enverra pas plus de 10 000 messages pour chacune des sept premières minutes, et 5 000 messages au cours de la dernière minute. 

### Considérations

Les messages envoyés à l'aide d'une limite de débit ne verront pas la limite de débit fixée (10 000 par minute, par exemple) répartie uniformément sur 60 secondes. Au lieu de cela, Braze veille à ce qu'il n'y ait pas plus de 10 000 messages envoyés par minute (ce qui peut signifier qu'un pourcentage plus élevé des 10 000 messages est envoyé dans la première demi-minute par rapport à la dernière demi-minute). 

Attention à ne pas retarder les envois de messages sensibles au facteur temps avec cette forme de limite de débit. Si l'audience du message contient 30 millions d'utilisateurs mais que nous fixons la limite de débit à 10 000 par minute, une grande partie de votre base d'utilisateurs ne recevra pas le message avant le lendemain. 

Sachez que les messages seront interrompus s'ils sont retardés de 72 heures ou plus en raison d'une limite de débit trop basse. L’utilisateur qui a créé la campagne recevra des alertes dans le tableau de bord et par e-mail si la limitation du débit est trop basse.

## Limitation de la vitesse de réception/distribution des campagnes

### Campagnes à canal unique

Lors de l'envoi d'une campagne à canal unique avec une limite de vitesse de réception/distribution, la limite de débit est appliquée à l'ensemble des messages. Par exemple, une campagne e-mail avec une limite de débit de 10 000 messages par minute enverra un maximum de 10 000 messages au total par minute.


| Nombre maximum d'e-mails envoyés par minute | Nombre maximal de messages envoyés par minute |
|--------------------------------|----------------------------------------|
| 10,000                         | 10,000                                 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Campagnes multicanal

Lors de l'envoi d'une campagne multicanal avec une limite de débit, chaque canal est envoyé indépendamment des autres. En conséquence, les phénomènes suivants peuvent se produire :

- Le nombre total de messages envoyés par minute pourrait être supérieur à la limite de débit. Par exemple, si votre campagne a une limite de débit de 10 000 par minute et utilise l'e-mail et le SMS, Braze peut envoyer un maximum de 20 000 messages au total chaque minute (10 000 e-mails et 10 000 webhooks).

| Nombre maximum d'e-mails envoyés par minute | Nombre maximum de messages SMS envoyés par minute | Nombre maximal de messages envoyés par minute |
|--------------------------------|--------------------------------------|----------------------------------------|
| 10,000                         | 10,000                               | 20,000                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

- Les utilisateurs pourraient recevoir les différentes chaînes à des moments différents, et il n'est pas nécessairement possible de prévoir quelle chaîne ils recevront en premier. 

Par exemple, si vous envoyez une campagne contenant des e-mails et des SMS, vous pouvez avoir 10 000 utilisateurs avec des numéros de téléphone valides, mais 50 000 utilisateurs avec des adresses e-mail valides. Si vous paramétrez la campagne pour qu'elle envoie 100 messages par minute (une limite de débit pour la taille de la campagne), un utilisateur pourrait recevoir le SMS dans le premier lot d'envois et l'e-mail dans le dernier lot d'envois, soit près de neuf heures plus tard.

### Campagnes de notification push multi-plates-formes

Pour les campagnes de notification push envoyant sur plusieurs plates-formes, la limite de débit sélectionnée sera répartie de manière égale sur les plates-formes. Une campagne de notification push utilisant Android et iOS avec une limite de débit de 10 000 messages par minute distribuera en parts égales les 10 000 messages sur les deux plates-formes.

| Nombre maximal de notifications Android envoyées par minute | Maximum de notifications push iOS envoyées par minute. | Nombre maximal de notifications push envoyées par minute |
|--------------------------------|--------------------------------------|----------------------------------------|
| 10,000                         | 10,000                               | 10,000                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Limitation de la vitesse de réception/distribution des toiles

Lors de l'envoi d'un Canvas avec une limite de débit, chaque canal est envoyé indépendamment des autres. En conséquence, les phénomènes suivants peuvent se produire :

- Le nombre total de messages envoyés par minute pourrait être supérieur à la limite de débit. 
    - Par exemple, si votre Canvas a une limite de débit de 10 000 par min et utilise des e-mails et des messages in-app, Braze peut envoyer jusqu'à 20 000 messages au total chaque minute (10 000 e-mails et 10 000 messages in-app).

- Les limites de débit peuvent avoir une incidence sur l'ordre dans lequel les utilisateurs reçoivent les messages dans un canvas. 
    - Par exemple, si vous envoyez un Canvas qui contient des e-mails et des notifications push à 50 000 utilisateurs, il se peut que les 50 000 aient tous une adresse e-mail valide, mais que seuls 10 000 utilisateurs aient des jetons push valides. Dans ce cas, si vous réglez le Canvas pour qu'il envoie 1 000 messages par minute et qu'il existe une étape du Canvas multicanal qui contient à la fois de l'e-mail et du push, il est possible qu'un utilisateur passe à l'étape du Canvas suivante (et soit éligible pour recevoir cette étape suivante) après avoir reçu uniquement la notification push, mais pas encore l'e-mail. 

## Aperçu des limites de débit antérieures et nouvelles

Votre compte Braze Currents utilise actuellement l'ancien comportement de limitation du débit de réception/distribution. Les informations ci-dessous détaillent la différence globale entre l'ancien et le nouveau comportement de limitation de la vitesse de réception/distribution :

- **Campagnes à canal unique et Canvases :** Les limites de débit sont toujours appliquées à l'ensemble des messages.
- **Campagnes multicanales et Canvases (y compris push multiplateforme) :**


<style>
table td {
    word-break: normal;
}
</style>

<table>
  <tr>
    <th></th>
    <th><b>Campagnes</b></th>
    <th><b>Canvas</b></th>
  </tr>
  <tr>
    <td><b>Précédent</b></td>
    <td>Appliqué pour chaque canal séparément, les plateformes push* partageant la limite collectivement.</td>
    <td>Appliqué pour chaque canal séparément, les plateformes push* partageant la limite collectivement.</td>
  </tr>
  <tr>
    <td><b>Nouveau</b></td>
    <td>Appliqué séparément par canal et par plate-forme de poussée</td>
    <td>Partagé collectivement</td>
  </tr>
</table>

_\*Les plates-formes de poussée comprennent : Android, iOS, Web Push et Kindle._