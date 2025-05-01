---
title: "Movable Ink"
article_title: Movable Ink
alias: "/partners/movable_ink/"
description: "Cet article de référence présente le partenariat entre Braze et Movable Ink, une plateforme logicielle basée sur le cloud qui permet aux marketeurs numériques de créer des expériences visuelles convaincantes et uniques pour engager les clients."
page_type: partner
search_tag: Partner

---

# Movable Ink

> [Movable Ink](https://www.movableink.com/) est une plateforme logicielle basée sur le cloud qui permet aux marketeurs numériques de créer des expériences visuelles convaincantes et uniques pour engager les clients. La plateforme Movable Ink offre de précieuses options de personnalisation qui peuvent être facilement insérées dans vos campagnes. 

_Cette intégration est maintenue par Movable Ink._

## À propos de l'intégration

Étendez vos capacités créatives en tirant parti des fonctionnalités de création intelligente de Movable Ink, telles que le sondage, le compte à rebours et le grattage. L'intégration de Movable Ink et de Braze permet une approche plus complète des messages dynamiques axés sur les données, en fournissant aux utilisateurs des éléments en temps réel sur les choses qui comptent.

## Prérequis

| Condition | Descriptif |
|---|---|
| Compte Movable Ink | Un compte Movable Ink est nécessaire pour bénéficier de ce partenariat. |
| Source des données | Vous devez connecter une source de données à Movable Ink. Cela peut se faire par le biais d'un fichier CSV, de l'importation d'un site web ou d'une API. Veillez à transmettre les données avec un identifiant commun entre Braze et Movable Ink (par exemple, `external_id`).
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d'utilisation

- Des récapitulatifs mensuels ou de fin d'année personnalisés.
- Personnalisez dynamiquement les images pour les e-mails, les notifications push ou les notifications riches en fonction du dernier comportement connu.<br>
	Par exemple : 
	- Utilisation d'un message push riche pour créer dynamiquement une planification d'événements en tirant des données de l'API. 
	- Utiliser le compte à rebours pour avertir les utilisateurs de l'imminence d'une grande vente (par exemple, le vendredi noir, la Saint-Valentin ou des offres de vacances).
	- Utilisez la fonctionnalité de grattage comme un moyen amusant et interactif de distribuer des codes de promotion.

## Capacités de l'encre mobile prises en charge

Intelligent Creative propose de nombreuses offres dont les utilisateurs de Braze peuvent profiter. La liste suivante indique les capacités prises en charge. 

| Capacité Movable Ink | Fonctionnalité | Notification push enrichie | Message in-app / cartes de contenu / e-mail | Détails |
| ---------------------- |---| ---------------------- | -------------------------------- | ------- |
| Optimiseur de création | Affichage du contenu des tests A/B | ✗ | ✔ | |
|| Optimiser | ✗ | ✔* | \* Vous devez utiliser la solution Deeplinking de Branch |
| Règles de ciblage | Date | ✔* | ✔ | \* Pris en charge mais non recommandé car les notifications push sont mises en cache dès leur réception et ne s'actualisent pas. |
|| Jour de la semaine | ✔* | ✔ | \* Pris en charge mais non recommandé car les notifications push sont mises en cache dès leur réception et ne s'actualisent pas. |
|| Heure de la journée | ✔* | ✔ | \* Pris en charge mais non recommandé car les notifications push sont mises en cache dès leur réception et ne s'actualisent pas. |
| Histoires/activités comportementales | | ✔* | ✔* | \* L'identifiant unique de l'utilisateur utilisé pour Braze doit être lié à l'identifiant de votre ESP. |
| Création de liens profonds dans l'application | | ✔* | ✔* | \* Pour offrir une expérience personnalisée à vos clients, utilisez une solution de création de liens profonds établie via Branch ou une solution validée avec l'équipe Expérience client de Movable Ink. |
| Applications | Compte à rebours | ✔* | ✔ | \* Pris en charge mais non recommandé car les notifications push sont mises en cache dès leur réception et ne s'actualisent pas. |
|| Sondage | ✗ | ✔* | \* Après avoir voté, l’utilisateur quittera l'application pour aller sur une page d'accueil mobile. |
|| Grattage | ✔* | ✔* | \* En cliquant, l’utilisateur quittera l'application pour afficher l'expérience de grattage. |
|| Vidéo | ✔* | ✔* | \* Uniquement les GIFs animés, <br>Pour Android, Braze requiert la [prise en charge des GIF][GIFsupport] dans la mise en œuvre |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Intégration

### Étape 1 : Créer une source de données pour Movable Ink

Les clients devront créer une source de données sous la forme d’un fichier CSV, d’un import de site web ou de l’intégration d'une API.

![Différentes options de sources de données apparaissent : Téléchargement CSV, site web ou intégration API.]({% image_buster /assets/img/movable_ink/movable_ink1.png %})

{% tabs local %}
{% tab Source de données CSV %}
- **Source de données CSV**: Chaque ligne doit comporter au moins une colonne de segmentation et une colonne de contenu. Une fois votre fichier CSV téléchargé, sélectionnez les colonnes à utiliser pour le ciblage du contenu. [Exemple de fichier CSV]({% image_buster /assets/download_file/movable_ink_CSV.csv %})

![Les champs qui s'affichent lorsque vous sélectionnez "CSV" comme source de données.]({% image_buster /assets/img/movable_ink/movable_ink2.png %})
{% endtab %}
{% tab Source de données du site web %}
- **Source de données du site web**: Chaque ligne doit comporter au moins une colonne de segmentation et une colonne de contenu. Une fois votre fichier CSV téléchargé, sélectionnez les colonnes à utiliser pour le ciblage du contenu.
  - Dans le cadre de ce processus, vous devez établir un mappage :
    - Quels sont les champs qui seront utilisés comme segmentations ?
    - Quels sont les champs de données que vous souhaitez voir personnalisés de manière dynamique dans la création (ex : attributs de l'utilisateur ou attributs personnalisés tels que le prénom, le nom de famille, la ville, etc.)

![Les champs qui s'affichent lorsque vous sélectionnez "Site web" comme source de données.]({% image_buster /assets/img/movable_ink/movable_ink3.png %})
{% endtab %}
{% tab Intégrations API %}
- **Intégrations API**: Utilisez l'API de votre entreprise pour alimenter le contenu directement à partir d'une réponse d'API.

![Les champs qui s'affichent lorsque vous sélectionnez "Integration d’API" comme source de données]({% image_buster /assets/img/movable_ink/movable_ink4.png %})
{% endtab %}
{% endtabs %}

### Étape 2 : Créez une campagne sur la plateforme Movable Ink

Dans l'écran d'accueil de Movable Ink, créez une campagne. Vous pouvez choisir entre des e-mails à partir de code HTML, des e-mails à partir d'une image ou d’un bloc pouvant être utilisés dans n'importe quel canal, y compris celui des notifications push, des messages in-app et des cartes de contenu (suggérées).
Nous vous suggérons également de jeter un coup d'œil aux différentes options de contenu disponibles par le biais des blocs.

![Une image de la plateforme Movable Ink lors de la création d'une nouvelle campagne Movable Ink.]({% image_buster /assets/img/movable_ink/movable_ink5.png %}){: style="max-width:70%"}

Movable Ink dispose d'un éditeur par-déposé qui vous permet de glisser-déposer des éléments tels que du texte, des images, etc. Si vous avez rempli votre source de données, vous pouvez générer dynamiquement une image à l'aide des propriétés des données. En outre, vous pouvez également créer des solutions de repli dans ce flux pour les utilisateurs si la campagne est envoyée et qu'un utilisateur ne correspond pas aux critères de personnalisation.

![L'éditeur de blocs Movable Ink montre les différents éléments personnalisables.]({% image_buster /assets/img/movable_ink/create_campaign2.png %})

Avant de terminer votre campagne, veillez à prévisualiser les images dynamiques et à tester les paramètres de requête pour voir à quoi ressembleront les images à l'affichage. Une fois l'opération terminée, une URL dynamique sera générée et pourra être insérée dans Braze !

Pour plus d'informations sur l'utilisation de la plateforme Movable Ink, visitez le [centre d'assistance Movable Ink][support]

### Étape 3 : Obtenir l'URL du contenu de Movable Ink

Pour inclure le contenu de Movable Ink dans les messages Braze, vous devez localiser l'emplacement de l'URL source que Movable Ink vous a fournie. 

Pour obtenir l'URL source, vous devez avoir configuré le contenu dans le tableau de bord Movable Ink, puis à partir de là, terminer et exporter votre contenu. Sur la page **Terminer**, copiez l'URL source (`img src`) de la balise du contenu créatif.

![La page qui s'affiche une fois que vous avez terminé votre campagne Movable Ink dans laquelle figure l'URL de votre contenu.]({% image_buster /assets/img/movable_ink/obtain_url.png %}){: style="max-width:80%;"}

Ensuite, dans la plateforme Braze, collez l'URL dans le champ approprié. Les champs appropriés pour votre canal de communication sont indiqués à l'étape 4. Enfin, remplacez toutes les balises de fusion (telles que {% raw %}```&mi_u=%%email%%```{% endraw %}) par la variable Liquid correspondante (telle que {% raw %}```&mi_u={{${email_address}}}```{% endraw %}).

### Étape 4 : Expérience de Braze

{% tabs local %}
{% tab E-mail %}
Dans la plateforme Braze, collez votre balise de contenu créatif dans le corps de votre e-mail.![]({% image_buster /assets/img/movable_ink/web2.png %}){: style="max-width:90%"}<br><br>

{% endtab %}
{% tab Notification push %}

1. Dans la plateforme Braze :
	- Notification push Android : Collez l'URL dans les champs **Image de l'icône push** et **Image de la notification étendue.** <br>![]({% image_buster /assets/img/movable_ink/android.png %}){: style="max-width:60%"}<br><br>
	- iOS Push : Collez l'URL dans le champ Lien **média** et indiquez le format de fichier que vous utilisez.<br>![]({% image_buster /assets/img/movable_ink/ios.png %}){: style="max-width:60%"}<br><br>
	- Web Push : Collez l'URL dans les champs **Image de l'icône push** et **Image de la grande notification.** <br>![]({% image_buster /assets/img/movable_ink/web.png %}){: style="max-width:60%"}<br><br>
2. Pour vous assurer que les images ne sont pas mises en cache, placez dans le message des balises Liquid vides avant l'URL : <br>{% raw %}```{% if true %}{% endif %}https://movable-ink-image-url-goes-here```{% endraw %}

{% endtab %}
{% tab Message in-app %}

1. Dans la plateforme Braze, collez l'URL dans le champ **Média de notification enrichie**.![]({% image_buster /assets/img/movable_ink/image.png %}){: style="max-width:60%"}<br><br>
2. Fournissez une URL unique pour éviter la mise en cache. Pour confirmer que les images en temps réel de Movable Ink fonctionnent et ne seront pas affectées par la mise en cache, utilisez Liquid pour ajouter un horodatage à la fin de l'URL de l'image Movable Ink.

Pour ce faire, utilisez la syntaxe suivante, en remplaçant l'URL de l'image si nécessaire :
{% raw %}
```
{% assign timestamp = "now" | date: "%s" %}
{% assign img = "https://movable-ink-image-url-goes-here" | append:timestamp %}
{{img}}
```
{% endraw %}
Ce modèle prend l'heure actuelle (en secondes), l'ajoute à la fin de l'onglet image de Movable Ink (en tant que paramètre de requête), puis affiche le résultat final. Vous pouvez le prévisualiser à l'aide de l'onglet **Test**, qui évalue le code et affiche un aperçu.

**3\.** Enfin, réévaluez l'appartenance à un segment. Pour ce faire, activez l'option `Re-evaluate audience membership and liquid at send-time` située à l'étape **Audiences cibles** d'une campagne. Si cette option n'est pas disponible, contactez votre gestionnaire de la satisfaction client ou le service d'assistance de Braze. Cette option indiquera aux SDK de Braze de redemander la campagne en fournissant une URL unique à chaque fois qu'un message in-app est déclenché.

{% endtab %}
{% tab Carte de contenu %}

1. Dans la plateforme Braze, collez l'URL dans le champ **Média de notification enrichie**.![]({% image_buster /assets/img/movable_ink/image.png %}){: style="max-width:60%"}<br><br>
2. Pour les mobiles : Les images des cartes de contenu sur iOS et Android sont mises en cache dès leur réception et ne s'actualisent pas. 
  - Pour contourner ce problème, planifiez votre campagne comme un message récurrent quotidien, hebdomadaire ou mensuel avec une date d'expiration correspondante afin que la carte de contenu soit reformatée. Par exemple, une carte de contenu qui doit être actualisée une fois par jour doit être définie comme un envoi planifié quotidien avec une expiration d'un jour.
3. Pour garantir que les images en temps réel de Movable Ink fonctionnent et ne seront pas affectées par la mise en cache lorsque la carte de contenu est reformatée, utilisez Liquid pour ajouter un horodatage à la fin de l'URL de l'image Movable Ink.

Pour ce faire, utilisez la syntaxe suivante, en remplaçant l'URL de l'image si nécessaire :
{% raw %}
```
{% assign timestamp = "now" | date: "%s" %}
{% assign img = "https://movable-ink-image-url-goes-here" | append:timestamp %}
{{img}}
```
{% endraw %}
Ce modèle prend l'heure actuelle (en secondes), l'ajoute à la fin de l'onglet image de Movable Ink (en tant que paramètre de requête), puis affiche le résultat final. Vous pouvez le prévisualiser à l'aide de l'onglet **Test**, qui évaluera le code et affichera un aperçu.

{% endtab %}
{% endtabs %}

## Résolution des problèmes

### Les images dynamiques ne s'affichent pas correctement ? Quel est le canal qui vous pose problème ?
- **Notification push** : Veillez à ce que l'URL de votre image Movable Ink soit précédée d'une logique vide : <br>{% raw %}```{% if true %}{% endif %}https://movable-ink-image-url-goes-here```{% endraw %}
- **Messages in-app et cartes de contenu**: Veillez à ce que l'URL de l'image soit unique pour chaque impression. Pour ce faire, il suffit d'ajouter la balise Liquid appropriée pour différencier toutes les URL. Voir les instructions relatives aux messages in-app et aux cartes de contenu][instructions]. 
- L**'image ne se charge pas**: Veillez à remplacer toutes les "balises de fusion" par les champs Liquid correspondants dans le tableau de bord de Braze. Par exemple : {% raw %}```https://mi-msg.com/p/rp/image.png?mi_u=%%email%%```{% endraw %} avec {% raw %}```https://mi-msg.com/p/rp/image.png?mi_u={{${email_address}}}```{% endraw %}.

### Vous avez des difficultés à afficher des GIF sur Android ?
- Android exige la prise en charge du format GIF dans la mise en œuvre. Consultez l'article Android [personnalisation des messages in-app][GIFsupport] ] si vous n'avez pas cette configuration.


[1]: https://www.movableink.com/
[datasource]: ({% image_buster /assets/img/movable_ink/movable_ink1.png %})
[support]: https://support.movableink.com/
[GIFsupport]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/gifs/
[Instructions]: {{site.baseurl}}/partners/message_personalization/dynamic_content/movable_ink/#step-4-braze-experience
[1]: ({% image_buster /assets/img/movable_ink/android.png %})
[2]: ({% image_buster /assets/img/movable_ink/ios.png %})
[3]: ({% image_buster /assets/img/movable_ink/web.png %})