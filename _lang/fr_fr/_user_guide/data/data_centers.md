---
nav_title: Centres de données
article_title: Centres de données
page_order: 0.1
page_type: reference
description: "Cet article de référence fournit des informations sur les centres de données, notamment sur leur emplacement/localisation et sur la manière de s'inscrire à des centres de données spécifiques à une région."
---

# Centres de données

> Les centres de données de Braze sont créés pour vous offrir des options sur l'endroit où les données de vos utilisateurs sont traitées et stockées. Vous pouvez ainsi gérer efficacement vos risques liés à la souveraineté, à la flexibilité et à la gestion des données. Lorsque vous choisissez un centre de données Braze, vous pouvez être certain que notre plateforme répond ou dépasse toutes les exigences locales en matière de gestion des données.

## Fonctionnement

Braze exploite plusieurs centres de données situés dans différents emplacements/localisations à travers le monde. Ces centres de données permettent à nos services d'être fiables et évolutifs. Cette répartition géographique permet de minimiser le temps de latence, c'est-à-dire le temps que mettent les données à voyager entre le serveur et l'utilisateur. 

Cela signifie également que lorsqu'un utilisateur interagit avec votre appli ou votre site web, ses demandes sont dirigées vers le centre de données le plus proche, ce qui optimise les performances et réduit les temps de chargement. En se connectant au centre de données le plus proche, vos utilisateurs peuvent bénéficier de temps de chargement rapides, ce qui est particulièrement important pour l'envoi de messages en temps réel et l'importation d'utilisateurs.

Imaginons que vous ayez une application mobile qui envoie des notifications push aux utilisateurs. Si un utilisateur de Melbourne reçoit une notification, la demande d'envoi de cette notification est acheminée vers le centre de données le plus proche en Australie. Dans le cas où l'application mobile connaîtrait une recrudescence d'utilisateurs lors d'un événement promotionnel, Braze dispose d'une infrastructure évolutive avec plusieurs centres de données capables de gérer l'augmentation de la demande.

## Liste des centres de données

Consultez le tableau suivant pour obtenir la liste des centres de données disponibles.

<style>
table th:nth-child(1) {
    width: 10%;
}
table th:nth-child(2) {
    width: 33%;
}
table th:nth-child(3) {
    width: 33%;
}
table th:nth-child(4) {
    width: 24%;
}
table td {
    word-break: break-word;
}
</style>
<table>
  <thead>
    <tr>
      <th>Région du centre de données</th>
      <th>URL du tableau de bord</th>
      <th>Endpoint REST</th>
      <th>Endpoint SDK</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Australie</b></td>
      <td><code>https://dashboard.au-01.braze.com</code></td>
      <td><code>https://rest.au-01.braze.com</code></td>
      <td><code>sdk.au-01.braze.com</code></td>
    </tr>
    <tr>
      <td><b>L'Europe</b></td>
      <td>
        <ul>
          <li><code>https://dashboard-01.braze.eu</code></li>
          <li><code>https://dashboard-02.braze.eu</code></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><code>https://rest.fra-01.braze.eu</code></li>
          <li><code>https://rest.fra-02.braze.eu</code></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><code>sdk.fra-01.braze.eu</code></li>
          <li><code>sdk.fra-02.braze.eu</code></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>US</b></td>
      <td>
        <ul>
          <li><code>https://dashboard-01.braze.com</code></li>
          <li><code>https://dashboard-02.braze.com</code></li>
          <li><code>https://dashboard-03.braze.com</code></li>
          <li><code>https://dashboard-04.braze.com</code></li>
          <li><code>https://dashboard-05.braze.com</code></li>
          <li><code>https://dashboard-06.braze.com</code></li>
          <li><code>https://dashboard-07.braze.com</code></li>
          <li><code>https://dashboard-08.braze.com</code></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><code>https://rest.iad-01.braze.com</code></li>
          <li><code>https://rest.iad-02.braze.com</code></li>
          <li><code>https://rest.iad-03.braze.com</code></li>
          <li><code>https://rest.iad-04.braze.com</code></li>
          <li><code>https://rest.iad-05.braze.com</code></li>
          <li><code>https://rest.iad-06.braze.com</code></li>
          <li><code>https://rest.iad-07.braze.com</code></li>
          <li><code>https://rest.iad-08.braze.com</code></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><code>sdk.iad-01.braze.com</code></li>
          <li><code>sdk.iad-02.braze.com</code></li>
          <li><code>sdk.iad-03.braze.com</code></li>
          <li><code>sdk.iad-04.braze.com</code></li>
          <li><code>sdk.iad-05.braze.com</code></li>
          <li><code>sdk.iad-06.braze.com</code></li>
          <li><code>sdk.iad-07.braze.com</code></li>
          <li><code>sdk.iad-08.braze.com</code></li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## Inscription à des centres de données spécifiques à une région

Lors de l'inscription à votre compte Braze, vous pouvez vous inscrire à des centres de données spécifiques à une région. Contactez votre gestionnaire de compte pour obtenir des informations et des recommandations sur les centres de données qui vous conviennent le mieux en fonction des régions géographiques de vos utilisateurs.
