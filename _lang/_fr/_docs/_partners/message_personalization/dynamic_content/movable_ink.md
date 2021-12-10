---
title: "Encre mobile"
article_title: Encre mobile
alias: "/fr/partners/movable_ink/"
page_order: 1
description: "Cet article décrit le partenariat entre Braze et Movable Ink, une plateforme logicielle basée sur le nuage qui offre aux marketeurs numériques un moyen de créer des expériences visuelles uniques et convaincantes qui déplacent leurs clients."
page_type: partenaire
search_tag: Partenaire
---

# Encre mobile

> [Movable Ink][1] est une plate-forme logicielle basée sur le nuage qui offre aux marketeurs numériques un moyen de créer des expériences visuelles uniques et convaincantes qui déplacent les clients. La plateforme Movable Ink vous offre de précieuses options de personnalisation qui peuvent facilement être insérées dans vos campagnes.

Développez les capacités créatives de Braze en exploitant les fonctionnalités de création intelligente de Movable Ink telles que le sondage, le compte à rebours et le grattage. L'intégration de Movable Ink et Braze permet une approche plus équilibrée des messages dynamiques basés sur les données, fournissant aux utilisateurs des éléments en temps réel sur les choses qui importent.

## Pré-requis

| Exigences             | Libellé                                                                                                                                                                                                                                                                   |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte d'encre mobile | Vous aurez besoin d'un compte d'encre mobile pour profiter de ce partenariat.                                                                                                                                                                                             |
| Source de données     | Vous devrez connecter une source de données à Movable Ink. Cela peut se faire par le biais du CSV, de l'importation de sites Web ou de l'API. Assurez-vous de passer des données avec un identifiant unificateur entre Braze et Movable Ink (par exemple, `external_id`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Cas d'utilisation
- Récapitulatifs personnalisés mensuels ou de fin d'année.
- Personnaliser dynamiquement les images pour les e-mails, les push, ou les notifications riches en fonction du dernier comportement connu.<br> Par exemple :
    - En utilisant un riche message push pour créer dynamiquement un calendrier d'événements en tirant des données de l'API.
    - Utiliser la fonction Compte à rebours pour avertir les utilisateurs quand une grosse vente approche (par exemple, Vendredi Noir, Saint Valentin, etc.)
    - Utilisez la fonction Scratch Off comme une façon amusante et interactive de débourser des codes promotionnels.

## Capacités d'encre mobile supportées

Intelligent Creative a de nombreuses offres dont les utilisateurs de Braze peuvent profiter. Voici une liste de ce qui est pris en charge.

| Capacité d'encre mobile              | Fonctionnalités         | Notification Rich Push | Messagerie In-App / Cartes de Contenu | Détails du produit                                                                                                     |
| ------------------------------------ | ----------------------- | ---------------------- | ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Optimiseur créatif                   | Afficher le contenu A/B | ✗                      | ✔                                     |                                                                                                                        |
|                                      | Optimiser               | ✗                      | ✔*                                    | * Doit utiliser la solution de plinçage en profondeur de la branche                                                    |
| Règles de ciblage                    | Date                    | ✔*                     | ✔                                     | * Supporté mais non recommandé car les notifications push sont mises en cache sur réception et ne sont pas actualisées |
|                                      | Jour de la semaine      | ✔*                     | ✔                                     | * Supporté mais non recommandé car les notifications push sont mises en cache sur réception et ne sont pas actualisées |
|                                      | Heure de la journée     | ✔*                     | ✔                                     | * Supporté mais non recommandé car les notifications push sont mises en cache sur réception et ne sont pas actualisées |
| Activité des histoires/Comportements |                         | ✔*                     | ✔*                                    | * L'identifiant utilisateur unique utilisé pour Braze doit être lié à l'identifiant de votre ESP                       |
| Liens profonds dans l'application    |                         | ✔*                     | ✔*                                    | * Vous devez utiliser la solution de liaison profonde de la branche                                                    |
| Applications                         | Compte à rebours        | ✔*                     | ✔                                     | * Supporté mais non recommandé car les notifications push sont mises en cache sur réception et ne sont pas actualisées |
|                                      | Vote                    | ✗                      | ✔*                                    | * Après le vote, quittera l'application pour être une page de destination mobile                                       |
|                                      | Scratch désactivé       | ✔*                     | ✔*                                    | * En cliquant dessus, quittera l'application pour l'expérience Scratch Off                                             |
|                                      | Vidéo                   | ✔*                     | ✔*                                    | * GIFs animés uniquement, <br>Pour Android, Braze nécessite [le support GIF][GIFsupport] en implémentation       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Intégration

### Étape 1 : Créer une source de données pour Movable Ink

Les clients devront créer une source de données qui peut être un CSV, une importation de site Web ou une intégration de l'API.

![Source de données]({% image_buster /assets/img/movable_ink/movable_ink1.png %})

{% tabs %}
{% tab CSV Data Source %}
- __Source de données CSV__: Chaque ligne doit avoir au moins une colonne de segment et une colonne de contenu. Une fois que votre CSV a été téléchargé, sélectionnez les colonnes à utiliser pour cibler le contenu. [Exemple de fichier CSV]({% image_buster /assets/download_file/movable_ink_CSV.csv %})

![Source de données]({% image_buster /assets/img/movable_ink/movable_ink2.png %})
{% endtab %}
{% tab Website Data Source %}
- __Source de données du site__: Chaque ligne doit avoir au moins une colonne de segment et une colonne de contenu. Une fois que votre CSV a été téléchargé, sélectionnez les colonnes à utiliser pour cibler le contenu.
  - Dans ce processus, vous devrez cartographier :
    - Quels champs seront utilisés comme segments
    - Quels champs vous voulez en tant que champs de données qui peuvent être dynamiquement personnalisés dans la création (ex: attributs utilisateur ou attributs personnalisés comme prénom, nom, ville, etc.)

![Source de données]({% image_buster /assets/img/movable_ink/movable_ink3.png %})
{% endtab %}
{% tab API Integrations %}
- __Intégrations d'API__: Utilisez l'API de votre entreprise pour alimenter le contenu directement à partir d'une réponse de l'API.

![Source de données]({% image_buster /assets/img/movable_ink/movable_ink4.png %})
{% endtab %}
{% endtabs %}

### Étape 2 : Créez une campagne sur la plateforme d'encre mobile

À partir de l'écran d'accueil de l'encre amovible, créez une campagne. Vous pouvez sélectionner à partir d'email à partir de HTML, d'email à partir de l'image, ou d'un bloc qui peut être utilisé dans n'importe quel canal, y compris les messages push, in-app et les cartes de contenu (suggéré). Nous vous suggérons également de consulter les différentes options de contenu disponibles via les blocs.

![Créer une campagne]({% image_buster /assets/img/movable_ink/movable_ink5.png %}){: style="largeur-max-70%"}

Movable Ink possède un éditeur facile pour vous permettre de glisser-déposer des éléments comme le texte, l'image, etc. Si vous avez rempli votre source de données, vous pouvez générer dynamiquement une image en utilisant les propriétés de données. De plus, vous pouvez également créer des replis dans ce flux pour les utilisateurs si la campagne est envoyée et qu'un utilisateur ne correspond pas aux critères de personnalisation.

![Créer une campagne 2]({% image_buster /assets/img/movable_ink/create_campaign2.png %})

Avant de terminer votre campagne, assurez-vous de prévisualiser les images dynamiques et de tester les paramètres de requête pour voir ce que les images vont regarder. Une fois terminé, une URL dynamique va générer qui peut ensuite être insérée dans Brésil!

Pour plus d'informations sur l'utilisation de la plateforme d'encre amovible, visitez le [Centre de support d'encre amovible][support]

### Étape 3 : Obtenir l'URL du contenu de l'encre mobile

Pour inclure le contenu de l'encre mobile dans les messages de Braze, vous devez localiser l'URL source que Movable Ink vous a fournie.

Pour obtenir l'URL source, vous devez avoir configuré le contenu dans le tableau de bord de l'encre amovible, puis de là, terminez et exportez votre contenu. Sur la page **Terminer** , copiez l'URL source (`img src`) de la balise créative.

![Obtenir une URL]({% image_buster /assets/img/movable_ink/obtain_url.png %}){: style="largeur-max-80%;"}

Ensuite, dans la plate-forme de Braze, collez l'URL dans le champ approprié. Des champs appropriés pour votre canal de messagerie peuvent être trouvés à l'étape 4. Enfin, remplacez toutes les balises de fusion (c'est-à-dire {% raw %}`&mi_u=%%email%%`{% endraw %}) par la variable Liquid correspondante (i. . {% raw %}`&mi_u={{${email_address}}}`{% endraw %}).

### Étape 4 : Expérience de Braze

#### Notifications push

1. Dans la plateforme de Braze :
    - Android Push: Collez l'URL dans les champs __Push Icon Image__ et __Extended Notification Image__.
    - iOS Push: Coller l'URL dans le champ de lien __Rich Notification Media__ et directement au-dessous, indiquez le format de fichier que vous utilisez.
    - Push Web : Collez l'URL dans les champs __Push Icon Image__ et __Large Notification Image__.<br><br>
2. Pour vous assurer que les images ne sont pas mises en cache, préfixez l'URL dans le message avec des balises Liquid vides : <br>{% raw %}`{% if true %}{% endif %}https://movable-ink-image-url-goes-here`{% endraw %}

#### Messages dans l'application et cartes de contenu

1. Dans la plateforme Braze, collez l'URL dans le champ __Rich Notification Media__.<br><br>
2. Fournir une URL unique pour aider à prévenir la mise en cache. Pour s'assurer que les images en temps réel de Movable Ink fonctionnent et ne seront pas affectées par la mise en cache, utilisez Liquid pour ajouter un timestamp à la fin de l'URL de l'image Movable Ink. <br> Pour cela, utilisez la syntaxe suivante, remplacement de l'URL de l'image si nécessaire :<br>{% raw %} `{% assigner timestamp = "maintenant" | date: "%s" %}` <br> `{% assigner img = "https://movable-ink-image-url-goes-here" | append:timestamp %} {{img}}` {% endraw %} <br>Ce modèle prendra le temps actuel (en secondes), ajoutez-la à la fin de l'onglet image de l'encre mobile (en tant que paramètre de requête), puis affichez le résultat final. Vous pouvez l'afficher avec l'onglet **Tester** - cela évaluera le code et affichera un aperçu.<br><br>
3. Enfin, réévaluer l'adhésion au segment. Pour ce faire, activez l'option `Ré-évaluer l'adhésion à un segment` située à l'étape « Utilisateurs cibles » d'une campagne. Si cette option n'est pas disponible, contactez votre Customer Success Manager ou le support de Braze. Cette option demandera à Braze SDKs de redemander la campagne en fournissant une URL unique chaque fois qu'un message est déclenché.

## Dépannage

#### Des images dynamiques ne s'affichent pas correctement ? Avec quel canal éprouvez-vous des difficultés ?
- __Push__: Assurez-vous que vous avez une logique vide avant l'URL de votre image d'encre mobile : <br>{% raw %}`{% if true %}{% endif %}https://movable-ink-image-url-here`{% endraw %}
- __Messages dans l'application et Cartes de Contenu__: Assurez-vous que l'URL de l'image est unique pour chaque impression. Cela peut être fait en ajoutant le liquide approprié afin que chaque URL soit différente. Consultez les instructions [In-App et Content Card Messages][Instructions].
- __Image non chargée__: Assurez-vous de remplacer n'importe quelle "balise de fusion" par les champs Liquid correspondants dans le tableau de bord Braze. Par exemple : {% raw %}`https://mi-msg.com/p/rp/image.png?mi_u=%%email%%`{% endraw %} avec {% raw %}`https://mi-msg.com/p/rp/image.png?mi_u={{${email_address}}}`{% endraw %}.

#### Vous avez des difficultés à afficher les GIFs sur Android?
- Android nécessite le support GIF dans l'implémentation. Suivez l'article [de personnalisation des messages dans l'application][GIFsupport] si vous n'avez pas cette configuration.
[datasource]: ({% image_buster /assets/img/movable_ink/movable_ink1.png %})

[1]: https://movableink.com/
[support]: https://support.movableink.com/
[GIFsupport]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/#gifs-IAMs
[GIFsupport]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/#gifs-IAMs
[Instructions]: {{site.baseurl}}/partners/message_personalization/dynamic_content/movable_ink/#step-4-braze-experience