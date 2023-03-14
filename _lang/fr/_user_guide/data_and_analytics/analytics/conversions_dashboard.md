---
nav_title: Tableau de bord de conversions
article_title: Tableau de bord de conversions
page_order: 3
page_type: reference
description: "Cet article de référence couvre le tableau de bord de conversions, qui vous permet d’analyser les conversions entre les campagnes, les Canvas et les canaux en utilisant des méthodes d’attribution différentes."
tool: 
  - Rapports

---

# Tableau de bord de conversions

Le tableau de bord de conversions vous permet d’analyser les conversions entre les campagnes, les Canvas et les canaux en utilisant des méthodes d’attribution différentes. Vous pouvez suivre ces méthodes d’attribution spécifiquement :

- **Conversions d’ouverture :** Les conversions qui se sont produites après qu’un utilisateur a ouvert le message
- **Conversions de clic :** Les conversions qui se sont produites après qu’un utilisateur a cliqué le message
- **Conversions reçues :** Les conversions qui se sont produites après qu’un utilisateur a reçu le message
- **Conversions au dernier clic :** Les conversions qui se sont produites après qu’un utilisateur a cliqué le message, si ce message était le plus récent cliqué par l’utilisateur (cette fonctionnalité est actuellement testée par un petit groupe de clients en accès anticipé)

Lorsque vous mesurez vos conversions, vous pouvez spécifier la période, l’événement de conversion et la fenêtre de conversion.

{% alert important %}
Cette fonctionnalité est en accès anticipé et est en développement actif. Si vous souhaitez participer à l’accès anticipé, contactez votre gestionnaire du succès des clients.
{% endalert %}

## Mettre en place votre rapport

1. Rendez-vous sur la page **Conversions**, dans **Data (Données)**.
2. Sélectionnez la période de temps pour votre rapport, jusqu’à 365 jours dans le passé.
3. Sélectionnez un événement de conversion, **Started session (Session démarrée)**, **Performed custom event (Événement personnalisé effectué)** ou **Made a specific purchase (Achat donné effectué)**.
4. Décidez si vous voulez que votre rapport comprenne les [événements non suivis](#untracked-events) (optional, cette fonctionnalité est actuellement testée par un petit groupe de clients en accès anticipé).
5. Sélectionnez une fenêtre de conversion, jusqu’à 7 jours. Elle représente le temps que les utilisateurs ont après avoir effectué l’action d’engagement de message pour que l’événement de conversion compte comme conversion. Les événements de conversion qui se produisent en dehors de cette fenêtre ne sont pas comptabilisés dans votre rapport.
6. Cliquez sur **Refresh (Rafraîchir)**.

### Événements non suivis

Les événements non suivis sont des événements qui ne sont pas, au départ, affectés en tant qu’événement de conversions pour les campagnes et les Canvas dans votre rapport. S’ils ne sont pas sélectionnés, votre rapport ne comprendra que les indicateurs de conversion pour les événements qui étaient compris au départ dans les événements de conversion et toutes les autres occurrences de cet événement dans cette période ne sont pas comptabilisés dans votre rapport.

Par exemple, imaginons que vous exécutiez votre rapport sur la campagne A (voir la prochaine section, [Filtrer votre rapport](#filtering-your-report), pour savoir comment filtrer les rapports pour une campagne donnée). Vous souhaitez voir le taux de conversion pour les utilisateurs qui ont reçu la campagne A et effectué l’événement personnalisé X, mais celui-ci ne faisait pas partie des quatre événements de conversion suivis pour cette campagne. Si vous choisissez de ne pas ajouter les événements non suivis, votre rapport affichera 0 conversions. Cependant, si vous ajoutez les événements non suivis, Braze générera alors un rapport des utilisateurs qui ont effectué l’événement personnalisé X après avoir reçu, ouvert ou cliqué la campagne A.

### Filtrer votre rapport

Vous pouvez filtrer par campagne, Canvas Step ou canal pour affiner les résultats de votre rapport. Vous devez sélectionner un canal pour exécuter le rapport.

- **Filtrer par campagne :** Sélectionnez jusqu’à 10 campagnes pour afficher les conversions qui se sont produites après avoir reçu, ouvert ou cliqué une des campagnes sélectionnées.
- **Filtrer par Canvas Step :** Sélectionnez jusqu’à 10 Canvas ou 10 Canvas Step pour afficher les conversions qui se sont produites après avoir reçu, ouvert ou cliqué un des Canvas ou une des étapes sélectionnés.
- **Filtrer par canal :** Sélectionnez un canal (required) pour afficher les conversions qui se sont produites après avoir reçu, ouvert ou cliqué un message envoyé par ce canal. Le canal e-mail est sélectionné par défaut.
- **Filtrer par pays :** Sélectionnez jusqu’à 10 pays pour afficher les conversions pour les utilisateurs ayant ces pays dans leur profil.

## Comprendre vos résultats

Votre rapport est divisé en trois sections : **Conversions totales**, **Conversions uniques** et **Performance des conversions par canal**.

### Conversions totales

Les conversions totales représentent le nombre total et ne sont pas dédupliquées lorsqu’un utilisateur se convertit plusieurs fois. Par exemple, si un utilisateur se convertit deux fois dans la fenêtre de conversion, alors deux conversions totales supplémentaires sont ajoutées.

Cette section comprend les panneaux d’indicateurs suivants :

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
.leftHeader{font-size: 12px; font-weight: bold; background-color: #f4f4f7; text-transform: uppercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-0pky">Nombre de conversions</th>
    <th class="tg-0pky">Nombre total de conversions par utilisateur</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="leftHeader">Conversions de réception</td>
    <td class="tg-0pky">Le nombre de fois où l’événement de conversion que vous avez sélectionné s’est produit après réception du message, pendant la fenêtre de conversion sélectionnée.</td>
    <td class="tg-0pky">Calculé comme : (Nombre total de conversions de la période) / (Nombre de destinataires uniques de la période)</td>
  </tr>
  <tr>
    <td class="leftHeader">Conversions d’ouverture</td>
    <td class="tg-0pky">Le nombre de fois où l’événement de conversion que vous avez sélectionné s’est produit après ouverture du message, pendant la fenêtre de conversion sélectionnée.</td>
    <td class="tg-0pky">Calculé comme : (Nombre de conversions de la période) / (Nombre de destinataires uniques de la période)</td>
  </tr>
  <tr>
    <td class="leftHeader">Conversions de clic</td>
    <td class="tg-0pky">Le nombre de fois où l’événement de conversion que vous avez sélectionné s’est produit après un clic de message, pendant la fenêtre de conversion sélectionnée.</td>
    <td class="tg-0pky">Calculé comme : (Nombre de conversions de la période) / (Nombre de destinataires uniques de la période)</td>
  </tr>
</tbody>
</table>

### Conversions uniques

Le décompte et le taux de conversions uniques suivent le nombre d’utilisateurs qui se sont convertis une fois ou plus. Cette section comprend les indicateurs suivants.

| Indicateur | Calcul |
| --- | --- | ---- |
| Taux de conversions de réception uniques | (Nombre d’utilisateurs qui se sont convertis au moins une fois après la réception du message durant la fenêtre de conversion sélectionnée) / (Nombre de destinataires uniques) |
| Taux de conversions d’ouverture uniques | (Nombre d’utilisateurs qui se sont convertis au moins une fois après l’ouverture du message durant la fenêtre de conversion sélectionnée) / (Nombre de destinataires uniques) |
| Taux de conversions de clic uniques | (Nombre d’utilisateurs qui se sont convertis au moins une fois après avoir cliqué le message durant la fenêtre de conversion sélectionnée) / (Nombre de destinataires uniques) |
| Taux de conversions du dernier clic (cette fonctionnalité est testée actuellement par un petit groupe de clients en accès anticipé) | (Nombre d’utilisateurs qui se sont convertis au moins une fois si leur dernier clic durant la fenêtre de conversion était pour ce message) / (Nombre de destinataires uniques)
{: .reset-td-br-1 .reset-td-br-2}

### Performances des conversions par canal

Cette section montre les résultats de conversion pour chaque canal de communication. En raison de la manière dont sont suivi les ouvertures et les clics sur les canaux, tous les indicateurs ne sont pas disponibles pour tous les canaux. 

{% alert note %}
Les événements de réception changent d’un canal à l’autre. De ce fait, l’indicateur de _destinataires uniques_ utilisé au dénominateur pour les calculs de conversions totales et uniques variera légèrement entre les canaux. Par exemple, les messages in-app suivent les impressions et non les réceptions. Ceci signifie que, pour le canal de communication in-app, le calcul des _conversions totales_ et des _conversions uniques_ utilise le nombre d’impression au dénominateur.
{% endalert %}

Le tableau suivant répertorie comment chaque méthode d’attribution est suivie pour chaque canal.

<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-0pky">Conversions de réception</th>
    <th class="tg-0pky">Conversions d’ouverture</th>
    <th class="tg-0pky">Conversions de clic</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="leftHeader">E-mail</td>
    <td class="tg-0pky">Réception des e-mails</td>
    <td class="tg-0pky">Ouverture des e-mails</td>
    <td class="tg-0pky">Clics des e-mails</td>
  </tr>
  <tr>
    <td class="leftHeader">SMS</td>
    <td class="tg-0pky">SMS envoyé</td>
    <td class="tg-0pky">S.O.</td>
    <td class="tg-0pky">S.O.</td>
  </tr>
  <tr>
    <td class="leftHeader">Notification push</td>
    <td class="tg-0pky">Notification push envoyée</td>
    <td class="tg-0pky">Ouvertures influencées de notification push</td>
    <td class="tg-0pky">Ouvertures directes de notification push</td>
  </tr>
  <tr>
    <td class="leftHeader">Message in-app</td>
    <td class="tg-0pky">Impressions des messages in-app</td>
    <td class="tg-0pky">S.O.</td>
    <td class="tg-0pky">Clics des messages in-app</td>
  </tr>
  <tr>
    <td class="leftHeader">Carte de contenu</td>
    <td class="tg-0pky">Impressions de la carte de contenu</td>
    <td class="tg-0pky">S.O.</td>
    <td class="tg-0pky">Carte de contenu cliquée</td>
  </tr>
</tbody>
</table>
