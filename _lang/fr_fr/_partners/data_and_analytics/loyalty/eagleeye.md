---
nav_title: "Œil d'aigle"
article_title: "Œil d'aigle"
description: Découvrez comment intégrer Eagle Eye à Braze.
alias: /partners/eagle_eye/
page_type: partner
search_tag: Partner
---

# Œil d'aigle

> [Eagle Eye](https://eagleeye.com/) est une société leader dans le domaine des technologies SaaS et de l'intelligence artificielle permettant aux marques de retail, de voyage et d'hôtellerie de gagner la fidélité de leurs clients finaux en alimentant leurs activités de marketing consommateur en temps réel, omnicanales et personnalisées, à l'échelle.

_Cette intégration est maintenue par Eagle Eye._

## Aperçu

L'Eagle Eye Connect est une intégration bidirectionnelle entre Braze et AIR qui permet aux marques d'activer les données de fidélisation et de promotion directement dans Braze. Les clients peuvent attribuer des récompenses dans AIR aux consommateurs qui entrent dans une audience dans AIR.  Les marketeurs peuvent ainsi personnaliser l'engagement des clients à l'aide de données en temps réel telles que les soldes de points, les promotions et les activités de récompense.

## Cas d’utilisation

- Déclenchez des campagnes de fidélisation en fonction d'événements tels que des seuils de points ou des récompenses obtenues.
- Enrichissez les profils utilisateurs de Braze avec des données en temps réel sur la fidélisation pour permettre un ciblage plus personnalisé.
- Suivez et rendez compte de l'efficacité de la campagne liée à l'utilisation des récompenses.
- Attribuez des récompenses dans AIR lorsque les utilisateurs participent à des campagnes dans Braze.

## Conditions préalables

| Condition              | Description |
|--------------------------|-------------|
| Compte AIR Eagle Eye    | Vous devez disposer d'un compte AIR Eagle Eye actif pour bénéficier de ce partenariat. Pour commencer, contactez l'équipe des partenariats d'Eagle Eye à [partnerships@eagleeye.com](mailto:partnerships@eagleeye.com). |
| Clé d'API REST Braze       | Une clé API Braze REST avec des autorisations `users.track`. <br><br>Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres > Clés API**. |
| Endpoint REST Braze      | [L'URL de votre endpoint REST.](https://www.braze.com/docs/api/basics/#endpoints) Votre endpoint dépend de l'URL Braze de votre instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Sortie ou entrée

Les tableaux suivants présentent les deux types d'intégration pris en charge entre Braze et Eagle Eye AIR. Eagle Eye Connect est le logiciel intermédiaire qui permet l'échange de données entre AIR et des systèmes partenaires comme Braze. Pour en savoir plus, consultez [la documentation d'Eagle Eye sur la Braze](https://developer.eagleeye.com/docs/braze).

{% tabs local %}
{% tab sortant %}
<table>
  <thead>
    <tr>
      <th>Direction</th>
      <th>Initiée par</th>
      <th>Flux de données</th>
      <th>Objectif</th>
      <th>Exemple</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Eagle Eye → Braze</td>
      <td>Œil d'aigle</td>
      <td>Pour Braze API</td>
      <td>
        Envoyez les données de fidélisation dans les profils utilisateurs de Braze sous forme d'attributs personnalisés via des événements personnalisés. Au sein de Braze, les données ingérées peuvent être utilisées pour :
        <ul>
          <li>segmenter les utilisateurs, déclencher des campagnes</li>
          <li>personnaliser les messages</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Envoi de points de fidélité ou de statuts dans Braze (<code>ee_loyalty.points.current</code>, <code>ee_loyalty.tier.tierId</code>)</li>
          <li>Mise à jour du profil d'un utilisateur lorsqu'il reçoit ou échange un coupon.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation"}
{% endtab %}

{% tab entrant %}
<table>
  <thead>
    <tr>
      <th>Direction</th>
      <th>Initiée par</th>
      <th>Flux de données</th>
      <th>Objectif</th>
      <th>Exemple</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Braze → Eagle Eye</td>
      <td>Braze</td>
      <td>Vers l'API d'Eagle Eye via webhook</td>
      <td>
        Lorsqu'un consommateur entre dans une audience dans Braze, quelle que soit la source, Braze peut déclencher un webhook Braze à EE Connect, ce qui permet à EE d'émettre une récompense (coupon ou points)<br><br>
        Une fois l'action terminée dans AIR, Braze reçoit un événement sortant d'AIR.
      </td>
      <td>
        <ul>
          <li>Les récompenses (coupons ou points) sont attribuées à un consommateur qui adhère au programme de fidélisation.</li>
          <li>Des récompenses sont attribuées à un consommateur qui a eu une réception/distribution tardive.</li>
          <li>Récompenses d'anniversaire</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation"}
{% endtab %}
{% endtabs %}

{% alert tip %}
Pour en savoir plus sur les données personnalisées que vous pouvez envoyer à Braze en tant qu'attributs et événements personnalisés, reportez-vous à la [documentation Braze d'Eagle Eye.](https://developer.eagleeye.com/docs/braze#data-model)
{% endalert %}

## Aperçu de l’intégration

Actuellement, les connecteurs entrants et sortants ne peuvent être mis en place que via l'API avec l'aide directe de l'équipe d'Eagle Eye. Toutefois, une option en libre-service dans le tableau de bord AIR est en cours d'élaboration !

En travaillant avec votre équipe Eagle Eye, vous accomplirez les tâches suivantes :

### Étape 1 : Fournir les détails de la configuration

Tout d'abord, vous fournirez les informations suivantes à votre équipe Eagle Eye :

| Vous fournissez            | Description |
|------------------------|-------------|
| Identifiants de l'API de Braze  | Partagez votre endpoint REST Braze, votre identifiant d'application et votre clé API en toute sécurité avec votre contact Eagle Eye. |
| Correspondance des identifiants    | Déterminez et partagez l'identifiant principal de l'utilisateur pour les mises à jour de profil qui est commun à AIR et Braze, comme l'ID externe ou l'e-mail. |
| Clé d'authentification               | Déterminez et partagez une clé d'authentification secrète pour chaque connecteur entrant et sortant. |
| Code devise          | Partagez le code de devise à 3 chiffres pour l'affichage des montants d'achat monétaires (e.g., USD). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Étape 2 : Configurer Eagle Eye Connect 

Votre équipe Eagle Eye configurera Eagle Eye Connect en utilisant les détails que vous avez fournis ainsi que les identifiants uniques de l'API AIR et les événements sortants pour les connecteurs.

### Étape 3 : Configurer les actions comportementales sociales dans AIR

Ensuite, vous mettrez en place une ou plusieurs actions comportementales sociales dans AIR avec des références d'action uniques pour délivrer des points ou des coupons.

### Étape 4 : Configurer Braze

En Braze, vous accomplirez les tâches suivantes :

- Implémenter des campagnes dans Braze pour distribuer des récompenses dans AIR  
- Mettre en place une communication avec les consommateurs en cas de réception d'un événement de DA.

### Étape 5 : Tester votre intégration

Effectuez des appels API dans AIR et observez le flux de données d'événements dans votre Braze workspace.Validate données reçues d'AIR et confirmez que les attributs sont mis à jour comme prévu.  

Ajoutez également des utilisateurs aux audiences et confirmez que les récompenses sont émises dans AIR.

### Étape 6 : Du lancement à la production

Une fois les tests réussis, l'intégration peut être mise en ligne/en production/instantanée pour envoyer des données en continu à Braze. Les mêmes étapes de configuration sont requises pour les environnements de production dans AIR et Braze

Contactez votre gestionnaire de satisfaction client Eagle Eye pour qu'une ressource vous soit attribuée, afin de mettre en place EE Connect.

## Assistance

Pour l'assistance à l'intégration ou la résolution des problèmes, veuillez contacter l'équipe d'assistance d'Eagle Eye à l'adresse [support@eagleeye.com](mailto:support@eagleeye.com).
