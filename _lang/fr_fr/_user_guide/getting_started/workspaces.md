---
nav_title: Espaces de travail
article_title: "Pour commencer : Espaces de travail"
page_order: 3
page_type: reference
description: "Tout ce que vous faites dans la plateforme Braze se produit au sein d'un espace de travail. Cet article décrit leur fonctionnement et les éléments importants à prendre en compte lors de la planification de vos espaces de travail dans Braze."
---

# Pour commencer : Espaces de travail

Tout ce que vous faites dans la plateforme Braze se produit au sein d'un espace de travail. Les espaces de travail agissent comme des silos de données distincts et vous permettent de séparer différentes marques ou activités. Plusieurs versions de votre site web ou de votre application mobile peuvent envoyer des données au même espace de travail. Nous désignons les différents sites et apps rassemblés au sein d'un espace de travail par le terme "instances d'apps".

## Comprendre les espaces de travail

Les espaces de travail ont deux fonctions essentielles :

- **Unifier les données des utilisateurs :** Lorsque plusieurs instances d'applis se trouvent dans un même espace de travail, vous pouvez recueillir et cibler des données utilisateur de façon fluide/sans heurts/de façon homogène sur les différentes versions de votre appli, comme iOS, Android et web. Vous êtes ainsi certain de toujours disposer d'informations actualisées sur chaque utilisateur, quelle que soit la plateforme qu'il utilise.
- **Séparer des activités distinctes :** Les espaces de travail permettent également de séparer des marques ou des activités distinctes. Par exemple, si vous avez plusieurs sous-marques avec des bases d'utilisateurs différentes, il est avantageux de créer des espaces de travail distincts pour chacune d'entre elles.

{% alert tip %}
Cette approche est particulièrement utile pour des entreprises telles que les sociétés de jeux mobiles qui peuvent gérer des espaces de travail individuels pour chacun de leurs jeux ou les sites de commerce électronique qui veulent des espaces de travail distincts pour chaque région dans laquelle ils opèrent.
{% endalert %}

## Aménagement des espaces de travail

Vous devez créer des instances d'apps distinctes pour chaque version de votre app sur chaque plateforme. Lorsque vous décidez des instances d'applications à inclure dans un espace de travail, pensez aux utilisateurs que vous souhaitez cibler et regroupez-les en conséquence.

La possibilité d'avoir plusieurs instances d'applications dans un seul espace de travail peut être séduisante, car elle vous permet de limiter le débit de l'envoi des messages dans l'ensemble de votre portefeuille d'applications. Toutefois, nous vous conseillons de ne regrouper que les différentes versions d'une même application (ou d'applications très similaires) au sein d'un même espace de travail.

### Espaces de travail partagés

Exemples courants de cas où vous souhaiteriez avoir plusieurs instances d'applications dans le même espace de travail :

- Lorsque vous avez plusieurs applications presque identiques sur différentes plates-formes
- Lorsque vous avez plusieurs versions majeures de l'application, mais que vous souhaitez continuer à attirer les mêmes utilisateurs lorsqu'ils mettent à jour leur application.
- Lorsque vous avez différentes versions de l'application auxquelles un même utilisateur peut accéder ou non (par exemple, de la version gratuite à la version premium).

#### Impact sur les filtres de segmentation

Quelles que soient les apps que vous choisissez d'avoir dans un espace de travail, leurs données seront agrégées. Cela aura un impact notable sur les filtres de segmentation suivants dans Braze (cette liste n'est pas exhaustive) :

- Dernière application utilisée
- Première application utilisée
- Nombre de sessions
- Argent dépensé dans l'application
- Abonnement en mode push (Cela devient une situation de tout ou rien : si vos utilisateurs se désabonnent d'une application, ils se désabonnent de toutes les applications de l'espace de travail).
- Abonnement aux e-mails (cela devient une situation "tout ou rien" et peut vous exposer à des problèmes de conformité).

{% alert note %}
L'agrégation des données entre les instances d'apps dans ces filtres est la raison pour laquelle nous ne recommandons pas d'héberger des apps substantiellement différentes au sein d'un même espace de travail. Cela peut rendre le ciblage difficile !
{% endalert %}

### Espaces de travail séparés

Dans d'autres cas, vous pouvez souhaiter disposer de plusieurs espaces de travail distincts. Les exemples les plus courants sont les suivants :

- Espaces de travail séparés pour les environnements de développement et de production d'une même application.
- Différentes sous-marques, par exemple, une société de jeux mobiles qui propose plusieurs jeux.
- Différentes localisations d'une même appli ou d'un même site web qui fonctionnent dans différents pays ou ciblent différentes langues.

### Considérations importantes

N'oubliez pas que les espaces de travail agissent comme des silos de données distincts. Toutes les données, qu'il s'agisse de données utilisateur ou de ressources marketing, sont stockées au sein d'un espace de travail. Ces données ne peuvent pas être facilement partagées en dehors de cet espace de travail. 

Les éléments suivants sont tous des éléments clés qui sont configurés dans un espace de travail :

- [Instances de l'application](#app-instances)
- [Teams](#teams)
- [Permissions des utilisateurs de Braze](#braze-user-permissions) (mais pas des utilisateurs de Braze)
- [Connecteurs de courant](#currents-connectors)
- [Les profils utilisateurs](#user-profiles) et les données utilisateurs associées
- [Segments, campagnes et canevas](#segments-campaigns-and-canvases)

#### Instances de l'application

Vous devez créer des instances d'apps distinctes pour chaque version de votre app sur chaque plateforme. Par exemple, si vous avez des versions Free et Pro de votre app sur iOS et Android, créez quatre instances d'app au sein de votre espace de travail (app iOS gratuite, app Android gratuite, app iOS pro et app Android pro). Vous obtiendrez ainsi quatre clés API à utiliser, une pour chaque instance d'application.

#### Teams

Les [équipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) peuvent être constituées en fonction de l'emplacement/localisation de la base de clients, de la langue et d'attributs personnalisés, de sorte que les membres de l'équipe et les non-membres aient un accès différent aux fonctionnalités d'envoi de messages et aux données des clients.

#### Autorisations pour les utilisateurs de Braze

Les espaces de travail ont des définitions d'accès et d'autorisation utilisateur indépendantes. Les [autorisations utilisateur]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) vous permettent de créer des contrôles granulaires concernant l'accès d'un utilisateur ou d'une équipe au tableau de bord au sein d'un espace de travail unique.

#### Connecteurs de courant

L'outil Braze [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) est un flux de données en temps réel de vos événements d'engagement qui constitue l'exportation la plus robuste mais aussi la plus granulaire de la plateforme Braze. Les connecteurs Braze Currents sont inclus dans certains paquets Braze, et vous en avez peut-être reçu un au départ, dans l'hypothèse d'un espace de travail unique.

Lorsque vous décidez de créer des espaces de travail séparés ou combinés, il est important de tenir compte du nombre de connecteurs Currents dont vous disposez, car les connecteurs Currents ne sont pas partagés entre les espaces de travail. 

Par exemple, si vous disposez d'espaces de travail distincts pour les environnements de développement et de production de la même appli, activez votre connecteur Currents dans l'espace de travail de production. Pour activer Currents dans les deux espaces de travail, vous devrez acheter un connecteur Currents supplémentaire.

#### Profils utilisateurs

Toutes les données persistantes associées à un utilisateur sont stockées dans son [profil utilisateur]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/). Cependant, les profils d'utilisateurs sont également une ressource formidable pour la résolution des problèmes et les tests, car vous pouvez facilement accéder à des informations sur l'historique d'engagement d'un utilisateur, son appartenance à un segment, son appareil et son système d'exploitation.

#### Segments, campagnes et canevas

Un segment, une campagne ou un Canvas ne peut pas faire référence ou accéder à des données hébergées dans un autre espace de travail. À l'inverse, lorsque plusieurs apps se trouvent dans le même espace de travail, toutes les apps verront leurs données agrégées. Cela aura un [impact sur les filtres à Braze](#impact-on-segmentation-filters).

### Aperçu de chaque approche

Le tableau suivant décrit les avantages et les inconvénients de ces deux approches de la planification de l'espace de travail :

- **Séparez les espaces de travail et les profils utilisateurs :** Un espace de travail a une instance d'application et une personne a un profil utilisateur pour cette instance d'application.
- **Espaces de travail partagés et profils utilisateurs :** Un espace de travail comporte plusieurs instances d'applications et une personne dispose d'un profil utilisateur pour toutes ces instances d'applications.

<style type="text/css">
  table {
    width: 100%;
  }
  th, td {
    padding: 8px;
    text-align: left;
    border: 1px solid black;
    word-break: break-word !important;
  }
  th {
    background-color: #f4f4f7;
    font-size: 12px;
    font-weight: bold;
    text-transform: uppercase;
    color: #212123;
    font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;
  }
  th[colspan="2"] {
    background-color: #fffae6;
  }
  th:last-child[colspan="2"] {
    background-color: #deebff;
  }
  td:nth-child(2), td:nth-child(3) {
    background-color: #fffae6;
  }
  td:nth-child(4), td:nth-child(5) {
    background-color: #deebff;
  }
  th:nth-child(2), th:nth-child(3) {
    background-color: #fffae6;
  }
  th:nth-child(4), th:nth-child(5) {
    background-color: #deebff;
  }
  th:first-child, td:first-child {
    min-width: 150px;
    background-color: #f4f4f7;
    font-size: 12px;
    font-weight: bold;
    text-transform: uppercase;
    color: #212123;
    font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;
  }
</style>

<table>
    <tr>
        <th></th>
        <th colspan="2">Espaces de travail séparés</th>
        <th colspan="2">Espaces de travail partagés</th>
    </tr>
    <tr>
        <th></th>
        <th>Avantages</th>
        <th>Inconvénients</th>
        <th>Avantages</th>
        <th>Inconvénients</th>
    </tr>
    <tr>
        <td>Le ciblage</td>
        <td>C'est le moyen le plus sûr de séparer les communications. Les campagnes sont assurées de ne cibler que des profils utilisateurs spécifiques.</td>
        <td>Impossible d'envoyer des messages promotionnels croisés même si vous savez qu'un utilisateur a un autre profil utilisateur dans un espace de travail différent.</td>
        <td>Possibilité d'envoyer des messages in-app si vous savez qu'un utilisateur utilise plusieurs applications dans votre espace de travail.<br><br>Peut référencer les données de l'utilisateur à partir de plusieurs applications. Par exemple, Jean a un attribut X pertinent pour l'application 1, et un attribut Y pertinent pour l'application 2, qui peuvent tous deux être référencés dans une campagne.</td>
        <td>Plus de place pour l'erreur humaine - vous pourriez accidentellement cibler des utilisateurs à travers plusieurs instances d'applications.<br><br>Pour envoyer des messages in-app, vous devez disposer d'événements personnalisés spécifiques à l'application afin qu'une campagne ne s'affiche pas par hasard sur une autre application. Par exemple, <code>app_1_action</code> versus <code>app_2_action</code>.</td>
    </tr>
    <tr>
        <td>Événements et attributs personnalisés</td>
        <td>Les attributs et les événements personnalisés sont garantis comme étant spécifiques à une instance d'application.</td>
        <td>Impossible de suivre le comportement des utilisateurs dans les espaces de travail.<br><br><b>Conseil :</b> Pour ce faire, vous pouvez utiliser plusieurs connecteurs Currents.</td>
        <td>Peut suivre le comportement de l'utilisateur dans toutes les instances d'applications de l'espace de travail.</td>
        <td>Les attributs et attributs personnalisés s'appliqueraient à toutes les instances de l'application, ce qui pourrait rendre difficile de déterminer quelles données d'un profil utilisateur sont pertinentes pour telle ou telle instance de l'application. Par exemple, "date_of_parking" est-il pertinent pour l'application 1 ou l'application 2 ? Pour y remédier, veillez à utiliser des conventions de dénomination bien structurées.</td>
    </tr>
    <tr>
        <td>Limitation de fréquence</td>
        <td>La limite de fréquence peut être définie séparément pour chaque instance d'application (en fonction de l'espace de travail).</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>La limite de fréquence s'applique à toutes les campagnes, et non à chaque application, ce qui rend plus difficile la prévention de l'envoi excessif de messages aux clients.</td>
    </tr>
    <tr>
        <td>Statut de l'abonnement pour les profils utilisateurs</td>
        <td>L'état de l'abonnement de chaque profil utilisateur est unique pour chaque instance d'application.</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>Les statuts d'abonnement d'un profil utilisateur sont combinés entre les instances de l'application.<br><br><b>Conseil :</b> Vous pouvez utiliser des <a href='/docs/user_guide/data/custom_data/custom_attributes'>attributs personnalisés</a> pour gérer les abonnements de vos utilisateurs.</td>
    </tr>
    <tr>
        <td>Autorisations pour les utilisateurs de Braze</td>
        <td>N/A</td>
        <td>La mise à jour des <a href='/docs/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/'>autorisations d'</a> un utilisateur de tableau de bord doit être effectuée séparément pour chaque espace de travail auquel l'utilisateur doit avoir accès.</td>
        <td>Les <a href='/docs/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/'>autorisations de l'</a> utilisateur peuvent être définies une seule fois pour un utilisateur du tableau de bord, et il disposera des mêmes autorisations pour toutes les instances d'applications dans l'espace de travail.</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>Duplication de contenu</td>
        <td>N/A</td>
        <td>Vous ne pouvez pas dupliquer des segments, des campagnes de cartes de contenu ou de push, ou des canevas dans les espaces de travail.</td>
        <td>Vous pouvez [dupliquer des campagnes sur workspaces]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/copying_across_workspaces/) pour les canaux pris en charge suivants : SMS, messages in-app, e-mails, modèles d'e-mails et blocs de contenu. <br><br>Peut dupliquer les segments, les campagnes et les Canvases pour réutiliser le contenu d'une instance d'appli à l'autre.</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>Analyse/analytique (si utilisé comme adjectif)</td>
        <td>Les statistiques globales seront précises sur la page d'accueil.</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>Les statistiques globales seront agrégées pour toutes les instances de l'application dans l'espace de travail sur la page d'accueil.</td>
    </tr>
</table>

## Meilleures pratiques

### Mettre en place un espace de travail pour les tests

En guise de bonne pratique, lorsque vous prévoyez de mettre en place un espace de travail de production (un espace de travail qui enverra des messages à des utilisateurs réels), vous devez également mettre en place un espace de travail de test. Un espace de travail de test est une copie de votre espace de travail de production sans aucune donnée utilisateur réelle. 

Cette pratique est considérée comme la meilleure pour plusieurs raisons :

- **Isolement des changements :** Il vous permet de tester de nouvelles fonctionnalités, configurations ou mises à jour dans un environnement isolé sans affecter votre environnement de production en ligne/en production/instantané. Ainsi, en cas de problème lors des tests, votre environnement de production n'est pas affecté.
- **Des tests précis :** Il permet des tests plus précis puisque les données de l'environnement de test peuvent être contrôlées et manipulées sans se soucier des données du monde réel.
- **Débogage :** Il est plus facile de déboguer les problèmes dans un environnement de test, car vous pouvez manipuler librement l'environnement sans craindre d'avoir un impact sur l'environnement de production.
- **Formation :** Les nouveaux membres de l'équipe peuvent se familiariser avec l'espace de travail dans un environnement sûr où les erreurs n'auront pas de conséquences dans le monde réel.

{% alert tip %}
L'ordre dans lequel vous mettez en place un espace de travail de test et un espace de travail de production peut dépendre de vos besoins et circonstances spécifiques. Toutefois, il est généralement conseillé de commencer par mettre en place un espace de travail de test. Cela vous permet de tester les fonctionnalités, les configurations et les mises à jour avant qu'elles ne soient mises en œuvre dans l'espace de travail de production. Une fois que vous êtes satisfait des tests et des résultats, vous pouvez établir votre espace de travail de production.
{% endalert %}

### Ajouter des administrateurs

Vous devez avoir plus d'un utilisateur Braze avec des droits d'administration pour un même espace de travail. Cela permet de s'assurer qu'il y a suffisamment de personnes dans votre organisation pour gérer les autorisations des autres utilisateurs.

## Prochaines étapes

Après avoir déterminé votre plan d'espace de travail, il est temps de créer votre espace de travail et d'ajouter des instances d'apps. Pour connaître la marche à suivre, consultez la rubrique [Création et gestion des espaces de travail]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/).

