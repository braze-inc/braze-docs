---
nav_title: Personnaliser
article_title: Personnaliser les cartes de contenu
page_order: 2
description: "Cet article de référence explique comment personnaliser les cartes de contenu."
channel:
  - cartes de contenu
  
---

# Personnaliser les cartes de contenu

> Le présent article décrit les différentes options de personnalisation disponibles lors de la mise en œuvre de votre carte de contenu. Pour obtenir des détails techniques, consultez notre documentation Développeur pour [Android][1], [iOS][2], ou le [Web][3].

La personnalisation des cartes de contenu et de leur flux ne peut être effectuée lors de la création de la campagne. Vous devez travailler avec vos ingénieurs et développeurs pour créer et personnaliser vos cartes.

## Approches de personnalisation

Les cartes de contenu sont entièrement personnalisables ! Chez Braze, nous avons défini trois approches de personnalisation en fonction de leur niveau d’effort et de flexibilité. Ces approches sont appelées « Crawl (ramper) », « Walk (Marcher) » et « Run (Courir) ».

- **Crawl (Ramper) :** Profitez des options de style de carte de contenu de base de Braze pour une mise en œuvre rapide nécessitant peu d’efforts.
- **Walk (Marcher) :** Ajoutez un style personnalisé aux cartes de contenu par défaut pour mieux correspondre à votre expérience de marque.
- **Run (Courir) :** Personnalisez chaque partie de vos campagnes de carte de contenu, du style au comportement en passant par les connexions cross-canal.

<style>
table {
  width: 60%;
}
table td {
    word-break: break-word;
}
</style>

{% tabs %}
{% tab Crawl %}

![Exemple d’application financière avec Content Card bannière et Image avec Légende ]({% image_buster/assets/img_archive/cc_pyrite_crawl.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Idéal pour les équipes qui ont des ressources de développement limitées, l’approche Crawl repose uniquement les [modèles de carte de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/) qui vous permettent de mettre en œuvre des cartes de contenu avec moins de 5 lignes de code.

Avec cette approche, la personnalisation est l’affaire des marketeurs, qui vont définir directement dans Braze le contenu, l’audience et le moment de chaque carte de contenu. Un petit développement est nécessaire en amont pour décider où les cartes de contenu apparaitront dans votre appli ou sur votre site, et les options de style sont limitées.

<table>
<thead>
  <tr>
    <th>Personnalisation</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><b>Effort</b></td>
    <td>Bas</td>
  </tr>
  <tr>
    <td><b>Style de carte</b></td>
    <td>Choisissez parmi trois modèles Braze.</td>
  </tr>
  <tr>
    <td><b>Comportement de la carte</b></td>
    <td>Choisissez parmi trois options de comportement lors du clic.</td>
  </tr>
  <tr>
    <td><b>Ordre des cartes</b></td>
    <td>Les cartes de contenu plus récentes apparaissent en haut du flux. Les cartes épinglées restent tout en haut.</td> 
  </tr>
  <tr>
    <td><b>Suivi analytique</b></td>
    <td>Les métriques des performances des cartes de contenu sont capturées dans Braze.</td>
  </tr>
  <tr>
    <td><b>Paires clé-valeur</b></td>
    <td>Facultatif, permet une personnalisation optimisée de l’UI/UX.</td>
  </tr>
</tbody>
</table>

{% alert tip %}
La vue en tableau du SDK Braze affiche l’expérience de la carte de contenu par défaut. Si vous souhaitez intégrer des cartes de contenu n’importe où dans votre application ou votre site, ou si vous avez besoin de fonctionnalités supplémentaires non mentionnées dans cette section, envisagez plutôt une approche Walk ou Run.
{% endalert %}

{% endtab %}
{% tab Walk %}

![Exemple d’application financière avec des cartes de contenu personnalisées]({% image_buster/assets/img_archive/cc_pyrite_walk.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

L’approche « Walk (marcher) » est une approche hybride dans laquelle le service marketing et les équipes de développement collaborent pour les faire correspondre à l’image de marque de votre appli ou site. 

Pendant la mise en œuvre, les développeurs écrivent du code personnalisé pour donner aux cartes de contenu le style et l’aspect de votre marque. Cela concerne le type et la taille de la police, les coins arrondis et les couleurs. Cette approche utilise toujours les cartes de contenu par défaut, mais ce sont vos développeurs qui gèrent le style de modèle.

Les marketeurs ont toujours la main sur l’audience, le contenu, le comportement lors du clic, l’expiration et l’épinglage directement sur le tableau de bord de Braze.

<table>
<thead>
  <tr>
    <th>Personnalisation</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><b>Effort</b></td>
    <td>Bas</td>
  </tr>
  <tr>
    <td><b>Style de carte</b></td>
    <td>Choisissez parmi trois modèles Braze ou utilisez vos propres modèles créés par vos développeurs.</td>
  </tr>
  <tr>
    <td><b>Comportement de la carte</b></td>
    <td>Choisissez parmi trois options de comportement lors du clic.</td>
  </tr>
  <tr>
    <td><b>Ordre des cartes</b></td>
    <td>Les cartes de contenu plus récentes apparaissent en haut du flux. Les cartes épinglées restent tout en haut.</td>
  </tr>
  <tr>
    <td><b>Suivi analytique</b></td>
    <td>Les métriques des performances des cartes de contenu sont capturées dans Braze.</td>
  </tr>
  <tr>
    <td><b>Paires clé-valeur</b></td>
    <td>Facultatif, permet une personnalisation optimisée de l’UI/UX.</td>
  </tr>
</tbody>
</table>

{% endtab %}
{% tab Run %}

![Exemple d’application financière montrant des cartes de contenu personnalisées avec capture d’e-mail]({% image_buster/assets/img_archive/cc_pyrite_run.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Avec l’approche Run, les développeurs ont un contrôle total sur l’expérience des utilisateurs des cartes de contenu. Le code personnalisé définit l’aspect des cartes, leur comportement et comment elles interagissent avec les autres canaux de communication (par ex. déclenchement d’une carte de contenu basé sur notification push). 

Le SDK Braze ne gère pas le comportement lors du clic, l’ordre ou l’analytique. Ces caractéristiques doivent être gérées de manière programmatique par le développeur pour permettre aux marketeurs d’accéder, via le tableau de bord de Braze, à des indicateurs précieux concernant la carte de contenu, comme les impressions, les clics et les fermetures.

<table>
<thead>
  <tr>
    <th>Personnalisation</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><b>Effort</b></td>
    <td>Dépend du cas d’utilisation.</td>
  </tr>
  <tr>
    <td><b>Style de carte</b></td>
    <td>Personnalisé</td>
  </tr>
  <tr>
    <td><b>Comportement de la carte</b></td>
    <td>Personnalisé</td>
  </tr>
  <tr>
    <td><b>Ordre des cartes</b></td>
    <td>Personnalisé</td>
  </tr>
  <tr>
    <td><b>Suivi analytique</b></td>
    <td>Personnalisé</td>
  </tr>
  <tr>
    <td><b>Paires clé-valeur</b></td>
    <td>Required</td>
  </tr>
</tbody>
</table>

### Cas d’utilisation

- Des flux de cartes de contenu multiples, comme l’ajout d’un onglet d’actualités, d’un centre de notification ou d’une promotion.
- Afficher les cartes de contenu dans un flux existant.
- Afficher les cartes de contenu dans une vue carrousel.
- Utiliser une carte de contenu pour capturer les informations utilisateur.
- Déclencher les cartes de contenu en fonction des autres canaux de communication.

{% alert tip %}
Consultez les exemples d’utilisation pour [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/implementation_guide/#sample-use-cases) et [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/implementation_guide/#sample-use-cases) décrits dans nos guides de mise en œuvre avancée des Carte de contenu pour vous faire une idée ce qui est possible avec cette approche.
{% endalert %}

{% endtab %}
{% endtabs %}

## Modifier la langue du « flux vide ».

Vous pouvez modifier la langue qui apparaît automatiquement dans les flux de carte de contenu en [redéfinissant les strings de cartes de contenu localisables](https://github.com/Appboy/appboy-ios-sdk/blob/3cca65b06f66085f5bc7c8e1ad267bf8bb1f0da7/AppboyUI/ABKContentCards/Resources/en.lproj/AppboyContentCardsLocalizable.strings) dans le fichier de strings localisables de votre application : 
```
"Appboy.content-cards.no-card.text" = "No Cards!!!!";
"Appboy.content-cards.done-button.title" = "Done";
"Appboy.content-cards.no-card.text" = "We have no updates.\nCheck again later.";
"Appboy.content-cards.no-connection.title" = "Connection Error";
"Appboy.content-cards.no-connection.message" = "Cannot establish network connection.\nPlease try again later.";
```
{% alert note %}
Si vous souhaitez la mettre à jour pour différentes langues, trouvez la langue correspondante dans la [Structure des dossiers des ressources](https://github.com/Appboy/appboy-ios-sdk/tree/3cca65b06f66085f5bc7c8e1ad267bf8bb1f0da7/AppboyUI/ABKContentCards/Resources) avec le même string `Appboy.content-cards.no-card.text`.
{% endalert %}


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/customization/custom_styling/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/customization/custom_styling/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/customization/custom_ui/