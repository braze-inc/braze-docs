---
title: "Movable Ink"
article_title: Movable Ink
alias: "/partners/movable_ink/"
description: "Cet article de référence présente le partenariat entre Braze et Movable Ink, une plateforme logicielle basée sur le cloud qui offre aux marketeurs numériques un moyen de créer des expériences visuelles convaincantes et uniques qui attirent les clients."
page_type: partner
search_tag: Partenaire

---

# Movable Ink

> [Movable Ink][1], une plateforme logicielle basée sur le cloud qui offre aux marketeurs numériques un moyen de créer des expériences visuelles convaincantes et uniques qui attirent les clients. La plateforme Movable Ink offre des options de personnalisation précieuses qui peuvent facilement être intégrées à vos campagnes. 

Développez les capacités créatives de Braze en tirant parti des fonctionnalités Intelligent Creative de Movable Ink telles que le sondage, la minuterie et le grattage. L’intégration de Movable Ink et de Braze donne une approche plus complète aux messages dynamiques axés sur les données, offrant aux utilisateurs des éléments en temps réel sur les choses qui comptent.

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Movable Ink | Un compte Movable Ink est nécessaire pour tirer parti de ce partenariat. |
| Source de données | Vous devrez connecter une source de données à Movable Ink. Cela peut être effectué via CSV, importation de site Internet ou API. Assurez-vous de transmettre des données avec un identifiant unique entre Braze et Movable Ink (p. ex., `external_id`).
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Cas d’utilisation
- Récapitulatifs mensuels ou de fin d’année personnalisés.
- Personnalisez dynamiquement les images pour les e-mails, les notifications push ou les notifications riches en fonction du dernier comportement connu.<br>
	Par exemple : 
	- Utilisez un message push riche pour créer de façon dynamique une planification des événements en extrayant des données de l’API. 
	- Utilisez la fonctionnalité Countdown Timer (Compte à rebours) pour avertir les utilisateurs lorsqu’une grosse vente approche (p. ex., Black Friday, Saint-Valentin, offres de dernière minute, etc.)
	- Utilisez la fonctionnalité Scratch Off (Grattage) comme une façon amusante et interactive de distribuer des codes promotionnels.

## Fonctions Movable Ink prises en charge

Intelligent Creative propose de nombreuses offres dont les utilisateurs de Braze peuvent profiter. La liste suivante indique les fonctions prises en charge. 

| Fonction Movable Ink | Fonctionnalité | Notification push riche | Messages in-app/Cartes de contenu | Détails |
| ---------------------- |---| ---------------------- | -------------------------------- | ------- |
| Creative Optimizer | Affichage du contenu A/B | ✗ | ✔ | |
|| Optimize | ✗ | ✔* | * Doit utiliser la solution de création de liens profonds de Branch |
| Règles de ciblage | Date | ✔* | ✔ | * Pris en charge mais non recommandé, car les notifications push sont mises en cache dès réception et ne sont pas actualisées |
|| Jour de la semaine | ✔* | ✔ | * Pris en charge mais non recommandé, car les notifications push sont mises en cache dès réception et ne sont pas actualisées |
|| Heure de la journée | ✔* | ✔ | * Pris en charge mais non recommandé, car les notifications push sont mises en cache dès réception et ne sont pas actualisées |
| Histoires/Activité de comportement | | ✔* | ✔* | * L’identifiant utilisateur unique utilisé pour Braze doit être lié à l’identifiant de votre fournisseur de services d’e-mail |
| Création de liens profonds dans l’application | | ✔* | ✔* | * Pour offrir une expérience simplifiée à vos clients, utilisez soit une solution de liens profonds établie via Branch, soit une solution validée avec l’équipe d’expérience client de Movable Ink. |
| Applications | Countdown Timer | ✔* | ✔ | * Pris en charge mais non recommandé, car les notifications push sont mises en cache dès réception et ne sont pas actualisées |
|| Polling | ✗ | ✔* | * Après le vote, l’application propose une page d’accueil mobile |
|| Scratch Off | ✔* | ✔* | * Au clic, l’application propose une expérience de grattage |
|| Vidéo | ✔* | ✔* | * GIF animés uniquement, <br>Pour Android, Braze requiert [GIF Support][GIFsupport] lors de l'implémentation |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Intégration

### Étape 1 : Créer une source de données pour Movable Ink

Les clients devront créer une source de données qui peut soit être via un CSV, une importation de site web ou une intégration API.

![Les différentes options de source de données proposées : Chargement d’un CSV, site web ou intégration API.]({% image_buster /assets/img/movable_ink/movable_ink1.png %})

{% tabs local %}
{% tab CSV Data Source %}
- **Source de données CSV** : Chaque ligne doit comporter au moins une colonne de segment et une colonne de contenu. Une fois votre CSV téléchargé, sélectionnez les colonnes qui doivent être utilisées pour cibler le contenu. [Exemple de fichier CSV]({% image_buster /assets/download_file/movable_ink_CSV.csv %})

![Champs affichés en sélectionnant « CSV » comme source de données.]({% image_buster /assets/img/movable_ink/movable_ink2.png %})
{% endtab %}
{% tab Website Data Source %}
- **Source de données site web** : Chaque ligne doit comporter au moins une colonne de segment et une colonne de contenu. Une fois votre CSV téléchargé, sélectionnez les colonnes qui doivent être utilisées pour cibler le contenu.
  - Dans ce processus, vous devez mapper :
    - Les champs qui seront utilisés comme segments
    - Les champs qui seront utilisés comme champs de données et qui peuvent être personnalisés dynamiquement dans la création (p. ex., attributs utilisateur ou attributs personnalisés comme prénom, nom, ville, etc.)

![Champs affichés en sélectionnant « Website » (Site Web) comme source de données.]({% image_buster /assets/img/movable_ink/movable_ink3.png %})
{% endtab %}
{% tab API Integrations %}
- **Intégrations par API** : Utilisez l’API de votre entreprise pour alimenter directement le contenu d’une réponse API.

![Champs affichés en sélectionnant « API Integration » (Intégration par API) comme source de données]({% image_buster /assets/img/movable_ink/movable_ink4.png %})
{% endtab %}
{% endtabs %}

### Étape 2 : Créer une campagne sur la plateforme Movable Ink

À partir de l’écran d’accueil de Movable Ink, créez une campagne. Les options disponibles incluent e-mails de HTML, e-mail à partir d’image ou bloc qui peut être utilisé dans n’importe quel canal, y compris les notifications push, les messages in-app et les cartes de contenu (recommandé).
Nous suggérons également de jeter un œil aux différentes options de contenu disponibles par le biais de blocs.

![Image de la plateforme Movable Ink lors de la création d’une nouvelle campagne Movable Ink.]({% image_buster /assets/img/movable_ink/movable_ink5.png %}){: style="max-width:70%"}

Movable Ink dispose d’un éditeur facile pour vous permettre de glisser et de déposer des éléments comme le texte, les images, etc. Si vous avez renseigné votre source de données, vous pouvez générer dynamiquement une image à l’aide des propriétés des données. En outre, vous pouvez également créer des solutions de repli dans ce flux pour les utilisateurs si la campagne est envoyée et qu’un utilisateur ne correspond pas aux critères de personnalisation.

![L’éditeur de blocs Movable Ink affichant les différents éléments personnalisables.]({% image_buster /assets/img/movable_ink/create_campaign2.png %})

Avant de terminer votre campagne, veillez à prévisualiser les images dynamiques et à tester les paramètres de requête pour voir à quoi ressembleront les images à l’affichage. Une fois terminé, une URL dynamique sera générée, puis insérée dans Braze !

Pour plus d’informations sur l’utilisation de la plateforme Movable Ink, visitez le [centre d’assistance de Movable Ink][support].

### Étape 3 : Obtenir l’URL du contenu de Movable Ink

Pour inclure le contenu de Movable Ink dans les messages de Braze, vous devez identifier l’URL source que Movable Ink vous a fournie. 

Pour obtenir l’URL source, vous devez avoir configuré le contenu dans le tableau de bord de Movable Ink, puis de là, terminer et exporter votre contenu. Sur la page **Finish (Terminer)**, copiez l’URL source (`img src`) à partir de la balise créative.

![La page qui apparaît une fois que vous avez terminé votre campagne Movable Ink, vous y trouvez l’URL de votre contenu.]({% image_buster /assets/img/movable_ink/obtain_url.png %}){: style="max-width:80%;"}

Ensuite, sur la plateforme Braze, collez l’URL dans le champ approprié. Les champs appropriés pour votre canal de communication sont disponibles à l’étape 4. Enfin, remplacez les balises de fusion (c.-à-d. {% raw %}```&mi_u=%%email%%```{% endraw %}) avec la variable Liquid correspondante (c.-à-d. {% raw %}```&mi_u={{${email_address}}}```{% endraw %}).

### Étape 4 : Expérience Braze

{% tabs local %}
{% tab Push notification %}

1. Dans la plateforme Braze :
	- Notification push pour Android : Collez l’URL dans les champs **Push Icon Image** (Image de l’icône de notification push) et **Expanded Notification Image** (Image de notification étendue).<br>![]({% image_buster /assets/img/movable_ink/android.png %}){: style="max-width:60%"}<br><br>
	- Notification push pour iOS : Collez l’URL dans le champ de lien **Media** et indiquez le format de fichier que vous utilisez.<br>![]({% image_buster /assets/img/movable_ink/ios.png %}){: style="max-width:60%"}<br><br>
	- Notification push pour le Web : Collez l’URL dans les champs **Push Icon Image** (Image de l’icône de notification push) et **Large Notification Image** (Image de notification grande).<br>![]({% image_buster /assets/img/movable_ink/web.png %}){: style="max-width:60%"}<br><br>
2. Pour vous assurer que les images ne sont pas mises en cache, faites précéder l’URL dans le message par des balises Liquid vides : <br>{% raw %}```{% if true %}{% endif %}https://movable-ink-image-url-goes-here```{% endraw %}

{% endtab %}
{% tab In-app message %}

1. Dans la plateforme Braze, collez l’URL dans le champ **Rich Notification Media (Média de notification enrichie)**.![]({% image_buster /assets/img/movable_ink/image.png %}){: style="max-width:60%"}<br><br>
2. Fournissez une URL unique pour éviter la mise en cache. Pour vous assurer que les images en temps réel de Movable Ink fonctionnent et ne soient pas affectées par la mise en cache, utilisez Liquid pour ajouter un horodatage à la fin de l’URL de l’image de Movable Ink.

Pour ce faire, utilisez la syntaxe suivante, remplaçant l’URL de l’image selon les besoins :
{% raw %}
```
{% assign timestamp = "now" | date: "%s" %}
{% assign img = "https://movable-ink-image-url-goes-here" | append:timestamp %}
{{img}}
```
{% endraw %}
Ce modèle prend l’heure actuelle (en secondes), l’ajoute à la fin de l’onglet d’image Movable Ink (en tant que paramètre de requête), puis affiche le résultat final. Vous pouvez le prévisualiser avec l’onglet **Test** ; cela évaluera le code et affichera un aperçu.

**3.** Enfin, réévaluez l’adhésion du segment. Pour ce faire, activez l’option `Re-evaluate audience membership and liquid at send-time` située à l’étape **Target Audiences (Audiences cibles)** d’une campagne. Si cette option n’est pas disponible, contactez votre gestionnaire du succès des clients ou l’assistance Braze. Cette option demandera aux SDK de Braze de redemander la campagne en fournissant une URL unique chaque fois qu’un message in-app est déclenché.

{% endtab %}
{% tab Content Card %}

1. Dans la plateforme Braze, collez l’URL dans le champ **Rich Notification Media (Média de notification enrichie)**.![]({% image_buster /assets/img/movable_ink/image.png %}){: style="max-width:60%"}<br><br>
2. Pour mobile : Les images des cartes de contenu sur iOS et Android sont mises en cache dès leur réception et ne sont pas actualisées. 
  - Comme solution de contournement, planifiez votre campagne en tant que message récurrent quotidien, hebdomadaire ou mensuel avec une expiration correspondante afin que la carte de contenu soit remodélisée. Par exemple, une carte de contenu qui devrait être actualisée une fois par jour doit être définie comme un envoi planifié quotidien avec une expiration de 1 jour.
3. Pour vous assurer que les images en temps réel de Movable Ink fonctionnent et ne soient pas affectées par la mise en cache lorsque la carte de contenu est remodélisée, utilisez Liquid pour ajouter un horodatage à la fin de l’URL de l’image de Movable Ink.

Pour ce faire, utilisez la syntaxe suivante, remplaçant l’URL de l’image selon les besoins :
{% raw %}
```
{% assign timestamp = "now" | date: "%s" %}
{% assign img = "https://movable-ink-image-url-goes-here" | append:timestamp %}
{{img}}
```
{% endraw %}
Ce modèle prend l’heure actuelle (en secondes), l’ajoute à la fin de l’onglet d’image Movable Ink (en tant que paramètre de requête), puis affiche le résultat final. Vous pouvez le prévisualiser avec l’onglet **Test**, ce qui évaluera le code et affichera un aperçu.

{% endtab %}
{% endtabs %}

## Résolution des problèmes

#### Les images dynamiques ne s’affichent pas correctement ? Avec quel canal rencontrez-vous des difficultés ?
- **Notification push** : Assurez-vous que vous avez une logique vide avant l’URL de votre image Movable Ink : <br>{% raw %}```{% if true %}{% endif %}https://movable-ink-image-url-goes-here```{% endraw %}
- **Messages in-app et cartes de contenu** : Assurez-vous que l’URL de l’image est unique pour chaque impression. Cela peut être fait en ajoutant la variable Liquid appropriée de sorte que chaque URL soit différente. Voir [les instructions relatives aux messages in-app et aux cartes de contenu][instructions]. 
- **L’image n’est pas chargée** : Veillez à remplacer toutes les « balises de fusion » par les champs Liquid correspondants dans le tableau de bord de Braze. Par exemple : {% raw %}```https://mi-msg.com/p/rp/image.png?mi_u=%%email%%```{% endraw %} avec {% raw %}```https://mi-msg.com/p/rp/image.png?mi_u={{${email_address}}}```{% endraw %}.

#### Vous avez des difficultés à afficher les GIF sur Android ?
- Android nécessite la prise en charge GIF dans la mise en œuvre. Reportez-vous à l’article [Personnalisation des messages in-app][GIFsupport] dans Android si vous n’avez pas cette configuration.

[1]: https://movableink.com/
[datasource]: ({% image_buster /assets/img/movable_ink/movable_ink1.png %})
[support]: https://support.movableink.com/
[GIFsupport]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/gifs/
[Instructions]: {{site.baseurl}}/partners/message_personalization/dynamic_content/movable_ink/#step-4-braze-experience
[1]: ({% image_buster /assets/img/movable_ink/android.png %})
[2]: ({% image_buster /assets/img/movable_ink/ios.png %})
[3]: ({% image_buster /assets/img/movable_ink/web.png %})