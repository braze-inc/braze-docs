---
nav_title: Types de messages
article_title: Types de messages LINE
page_order: 0
description: "Cet article présente les différents types d'envois de messages LINE."
page_type: reference
tool:
 - Campaigns
channel:
 - LINE
alias: /line/create/message_types/
---

# Types de messages LINE

> Cet article présente les types de messages LINE que vous pouvez composer, ainsi que leurs aspects et leurs limites.

Lorsque vous composez un message LINE, vous pouvez glisser-déposer des types de messages dans le compositeur et les personnaliser.

Panneau des types de messages avec les types de messages à glisser dans l'éditeur du compositeur, y compris le texte, l'image, le message riche et le message basé sur une carte.]({% image_buster /assets/img/line/line_message_types.png %}){: style="max-width:40%;"}

## Texte

Un message texte LINE peut contenir jusqu'à 5 000 caractères et inclure des emojis et la personnalisation du liquide.

Les cas d'utilisation sont les suivants :
- Annoncez une promotion limitée dans le temps sur les stocks en déstockage
- Envoyez des vœux d'anniversaire personnalisés avec des cartes de promotion uniques
- Partagez des mises à jour rapides sur les événements à venir

Un message textuel rappelant à l'utilisateur qu'il ne doit pas oublier la fête du vendredi noir et la possibilité d'enregistrer jusqu'à 80 % d'économies avant minuit.]({% image_buster /assets/img/line/line_text_message.png %}){: style="max-width:40%;"}

## Image

Un message image LINE peut être ajouté par l'intermédiaire de la [bibliothèque multimédia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/), d'une URL ou de Liquid. Ces images sont indépendantes et ne contiennent pas de liens cliquables.

Les cas d'utilisation sont les suivants :
- Présentez une destination de vacances pour inciter les utilisateurs à acheter des billets d'avion.
- Mettez en avant les promotions de fin de saison pour inciter les utilisateurs à s'approvisionner en vêtements d'hiver pour l'année prochaine grâce à de bonnes affaires.
- Lancez un compte à rebours visuel pour une vente annuelle dans tout le magasin

\![Un message d'image envoyant des messages pour la vente d'un grille-pain.]({% image_buster /assets/img/line/line_image_message.png %}){: style="max-width:40%;"}

### Image URL

Utilisez des images URL pour les cas d'utilisation qui les intègrent :
- Les images dynamiques Liquid en incluant le Liquid dans l'attribut source de votre image. Par exemple, vous pouvez insérer {% raw %} `https://example.com/images/?imageBanner={{first_name}}` {% endraw %} comme URL de l'image pour inclure le prénom d'un utilisateur dans l'image
- [Contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) en tirant des images directement de votre serveur web ou d'API accessibles au public.
- [Braze établit des catalogues]({{site.baseurl}}/user_guide/data/activation/catalogs/) en accédant à des images à partir de fichiers CSV importés et d'endpoints API.

| **Spécifications** | **Propriétés recommandées** |
|--------------------------|----------------------------|
| Longueur de l'URL du fichier image | 2 000 caractères maximum  |
| Format de l'image          | PNG, JPEG             |
| Taille du fichier     |  10 Mo maximum |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Messages riches (carte image)

Un message riche en LIGNE est une image qui contient un ou plusieurs liens qui s'ouvrent en sélectionnant des zones spécifiques de l'image. Sélectionnez un modèle de message riche pour choisir la manière dont les liens sont mappés sur l'image.

Les cas d'utilisation sont les suivants :
- Affichez une grille des sacs à main nouvellement arrivés avec des liens vers la page produit de chaque sac.
- Présentez un menu interactif qui permet de lancer une commande combo en sélectionnant un article.
- Présentez plusieurs promotions que les utilisateurs peuvent choisir en sélectionnant un carré de la grille.

Un message riche de six cases avec une photo d'une grille en noir et blanc sur laquelle les utilisateurs peuvent appuyer pour recevoir une offre aléatoire.]({% image_buster /assets/img/line/line_rich_message.png %})

### Mappage de l'image 

| **Spécifications** | **Propriétés recommandées** |
|--------------------------|----------------------------|
| Longueur de l'URL du fichier image | 2 000 caractères maximum  |
| Format de l'image          | PNG (peut être transparent), JPEG             |
| Rapport hauteur/largeur          | 1:1 (largeur:hauteur)
| Taille du fichier     |  10 Mo maximum |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Lien URI 

| **Spécifications** | **Propriétés recommandées** |
|--------------------------|----------------------------|
| Nombre de caractères      | 1 000 maximum |
| Régimes              | HTTP, HTTPS, LINE, tel |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Texte 

Un message riche en texte peut contenir jusqu'à 400 caractères.

## À base de cartes (carrousel)

Un message basé sur une carte LINE permet aux utilisateurs de faire défiler plusieurs messages, comme dans un carrousel, et de prendre des mesures sur les messages les plus pertinents pour eux en sélectionnant une carte ou les boutons d'une carte.

Les cas d'utilisation sont les suivants :
- Afficher des promotions pour des produits spécifiques du menu
- Mettez en avant les vestes les plus vendues de la saison
- Présenter un échantillon d'outils et de gadgets de cuisine inclus dans un kit.

!Un message à base de cartes avec au moins deux cartes qui font la promotion des sandwichs dans l'éditeur du compositeur.]({% image_buster /assets/img/line/line_card_message.png %})

### Message

| **Spécifications** | **Propriétés recommandées** |
|--------------------------|----------------------------|
| Colonnes                  | 10 maximum |
| Rapport hauteur/largeur             | Rectangle : 1.51:1 <br> Carré : 1:1  |
| Titre                    | 40 caractères maximum
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


### Image

| **Spécifications** | **Propriétés recommandées** |
|--------------------------|----------------------------|
| URL de l'image                 | 2 000 caractères maximum |
| Format de l'image              | JPEG ou PNG |
| Largeur                     | 1 024 pixels  |
| Taille du fichier                 | 1 MB |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


### Texte

| **Spécifications** | **Propriétés recommandées** |
|-------------------------|----------------------------|
| Personnages              | 120 maximum (sans image ni titre) <br> 60 maximum (message avec une image ou un titre)  |
| Actions                 | 3 maximum |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


