---
nav_title: Aperçu de la personnalisation
article_title: Aperçu de la personnalisation
page_order: 10
description: "Cet article de référence aborde les concepts essentiels de la personnalisation et de l'extension des canaux de communication du SDK."
hidden: true
layout: redirect
redirect_to: /docs/developer_guide/getting_started/
---

# Aperçu de la personnalisation

> Chez Braze, presque tout est entièrement personnalisable ! Les articles de ce guide de personnalisation vous montrent comment affiner votre expérience Braze grâce à un mélange de configuration et de personnalisation. Au cours de ce processus, les équipes de marketing et d'ingénierie doivent travailler en étroite collaboration pour coordonner exactement la manière de personnaliser les canaux d'envoi des messages de Braze.

{% alert note %}
Le SDK de Braze est une boîte à outils puissante, mais à un niveau élevé, il fournit deux fonctionnalités importantes : il aide à collecter et à synchroniser les données des utilisateurs entre les plateformes vers un profil utilisateur consolidé, et gère également les canaux d'envoi de messages tels que les messages in-app, les notifications push et les cartes de contenu. Les articles du guide de personnalisation partent du principe que vous avez déjà suivi le [processus d’implémentation du SDK]({{site.baseurl}}/developer_guide/home).
{% endalert %}

Tous les composants de Braze sont conçus pour être accessibles, adaptables et personnalisables. À ce titre, nous vous recommandons de commencer par les composants par défaut de `BrazeUI` et de les personnaliser en fonction des besoins de votre marque et de votre cas d'utilisation. Chez Braze, nous avons défini trois approches de personnalisation en fonction de leur niveau d’effort et de flexibilité. Ces approches sont appelées « Crawl (ramper) », « Walk (Marcher) » et « Run (Courir) ».

- **Crawl (ramper) :** Tirez parti des options de style de base pour une mise en œuvre rapide et sans effort.
- **Walk (marcher) :** Ajoutez un style personnalisé aux modèles par défaut pour qu'ils correspondent mieux à votre expérience client.
- **Run (courir) :** Personnalisez chaque partie de votre message, du style au comportement en passant par les connexions cross-canal.

<style>
table {
  width: 60%;
}
table td {
    word-break: break-word;
}
</style>

{% tabs %}
{% tab Crawl (ramper) %}

![Exemple d'application financière montrant des cartes de contenu de type image légendée et de type image seule]({% image_buster/assets/img_archive/cc_pyrite_crawl.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

L'approche Crawl (ramper) permet aux marketeurs de prendre le contrôle direct de la personnalisation. Bien qu'un petit travail de développement soit nécessaire en amont pour intégrer les canaux de communication Braze à votre application ou à votre site, cette approche vous permet d'être opérationnel plus rapidement. 

Les marketeurs déterminent le contenu, l'audience et le calendrier des messages à partir du tableau de bord. Les options de style sont toutefois limitées. Cette approche convient mieux aux équipes dont les ressources en développeurs sont limitées ou qui souhaitent partager rapidement un contenu simple. 

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
    <td>Faible</td>
  </tr>
    <tr>
    <td><b>Travail du développeur</b></td>
    <td>0-1 heures</td>
  </tr>
  <tr>
    <td><b>Style de carte</b></td>
    <td>Utilisez les modèles par défaut de Braze.</td>
  </tr>
  <tr>
    <td><b>Comportement</b></td>
    <td>Choisissez parmi les options de comportement par défaut.</td>
  </tr>
  <tr>
    <td><b>Suivi des analyses</b></td>
    <td>Les analyses sont capturées dans Braze.</td>
  </tr>
  <tr>
    <td><b>Paires clé-valeur</b></td>
    <td>Facultatif, permet une personnalisation optimisée de l’UI/UX.</td>
  </tr>
</tbody>
</table>

{% endtab %}
{% tab Walk (marcher) %}

![Exemple d'application financière montrant des cartes de contenu avec personnalisation]({% image_buster/assets/img_archive/cc_pyrite_walk.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

L’approche « Walk (marcher) » est une approche hybride dans laquelle le service marketing et les équipes de développement collaborent pour les faire correspondre à l’image de marque de votre appli ou site. 

Au cours du processus de mise en œuvre, les développeurs écrivent un code personnalisé pour mettre à jour l'aspect et la convivialité d'un canal de communication, afin qu'il corresponde mieux à votre marque. Vous pouvez notamment modifier le type et la taille des polices, les coins arrondis et les couleurs. Cette approche utilise toujours les options par défaut, mais avec un style de modèle programmatique.

Les marketeurs conservent le contrôle de l’audience, de contenu, du comportement lors du clic et de l’expiration directement dans le tableau de bord de Braze.

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
    <td>Faible</td>
  </tr>
    <tr>
    <td><b>Travail du développeur</b></td>
    <td>0-4 heures</td>
  </tr>
  <tr>
    <td><b>Interface utilisateur</b></td>
    <td>Utilisez les modèles de Braze ou ceux créés par vos propres développeurs.</td>
  </tr>
  <tr>
    <td><b>Comportement</b></td>
    <td>Choisissez parmi les options de comportement par défaut.</td>
  </tr>
  <tr>
    <td><b>Suivi des analyses</b></td>
    <td>Les analyses par défaut sont saisies dans Braze.</td>
  </tr>
  <tr>
    <td><b>Paires clé-valeur</b></td>
    <td>Facultatif, permet une personnalisation optimisée de l’UI/UX.</td>
  </tr>
</tbody>
</table>

{% endtab %}
{% tab Run (courir) %}

![Exemple d'application financière montrant des cartes de contenu personnalisées avec capture d'e-mail]({% image_buster/assets/img_archive/cc_pyrite_run.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Avec l’approche Run, les développeurs ont un contrôle total sur l’expérience des utilisateurs. Le code personnalisé dicte l'aspect des messages, leur comportement et leur interaction avec d'autres canaux d'envoi de messages (par exemple, le déclenchement d'une carte de contenu sur la base d'une notification push).

Lorsque vous créez un contenu personnalisé entièrement nouveau, comme de nouveaux types de cartes de contenu ou des messages in-app avec une interface utilisateur sur mesure, le SDK de Braze [ne suivra pas automatiquement les analyses]({{site.baseurl}}/developer_guide/analytics/). Vous devez gérer les analyses de manière programmatique afin que les marketeurs continuent d'avoir accès à des indicateurs tels que les impressions, les clics et les rejets dans le tableau de bord de Braze. Appelez les méthodes d'analyse du SDK de Braze pour que le SDK retransmette ces données à Braze. Chaque canal de communication dispose d'un article d'analyses pour faciliter cette démarche.

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
    <td><b>Travail du développeur</b></td>
    <td>Peu d'efforts : 1-4 heures<br>Effort moyen : 4-8 heures<br>Effort important : plus de 8 heures</td>
  </tr>
  <tr>
    <td><b>Interface utilisateur</b></td>
    <td>Personnalisé</td>
  </tr>
  <tr>
    <td><b>Comportement</b></td>
    <td>Personnalisé</td>
  </tr>
  <tr>
    <td><b>Suivi des analyses</b></td>
    <td>Personnalisé</td>
  </tr>
  <tr>
    <td><b>Paires clé-valeur</b></td>
    <td>Requis</td>
  </tr>
</tbody>
</table>
{% endtab %}
{% endtabs %}

{% alert tip %}
Lorsque les développeurs et les responsables de l’implémentation créent du contenu personnalisé pour Braze, ils ont l'occasion de collaborer avec les marketeurs. Par exemple, si vous développez une nouvelle interface utilisateur ou une nouvelle fonctionnalité pour un composant particulier, préparez votre équipe à réussir en documentant le nouveau comportement et la façon dont il s'intègre à votre backend.
{% endalert %}