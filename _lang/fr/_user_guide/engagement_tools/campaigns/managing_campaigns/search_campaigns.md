---
nav_title: Recherche de campagnes
article_title: Recherche de campagnes
page_order: 10
page_type: reference
description: "Cet article explique comment utiliser la recherche de campagne pour trouver des campagnes."
tool:
  - Campagnes

---

# Recherche de campagnes

Cette page explique comment vous pouvez utiliser le champ de recherche dans la liste des campagnes pour affiner vos résultats.

## Recherche par mot-clé

Saisissez le nom de la campagne ou recherchez des mots-clés dans les champs de nom de description ou de message de campagne. Par exemple, dans le cas présent, nous avons cherché « cette semaine », qui extrait depuis le titre et le message de cette campagne de ré-engagement.

![Recherche de campagne pour les mots-clés « cette semaine » avec des résultats à partir du titre et du corps du message.][1]

## Rechercher le texte exact

Pour trouver des correspondances exactes pour les termes recherchés, encadrez votre recherche entre crochets `[ ]`.

Par exemple, si vous recherchez `[flow]`, vous verrez des campagnes contenant le mot « flow », mais pas « flower » ou « overflow ».

## Filtres

Utilisez les filtres dans le menu latéral pour grouper les résultats par créateur, éditeur, dates d’envoi ou canal, ou bien sélectionnez **Ne montrer que les miens** pour limiter les résultats de votre recherche aux seules campagnes que vous avez créées. Vous pouvez également filtrer par statut et [balises]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/) pour affiner vos résultats encore plus.

![][2]

Étendez le menu déroulant de recherche pour filtrer par dernier éditeur, segment cible, canal de communication ou date.

![][3]

## Syntaxe de recherche

Sélectionner un filtre de campagne ajoutera automatiquement la syntaxe adéquate au champ de recherche. Vous pouvez également saisir ces filtres manuellement. Lorsque vous utilisez la recherche manuelle, la syntaxe doit être le nom du filtre, suivi par un point-virgule, suivi par votre saisie. Par exemple, pour chercher des campagnes de notification push, saisissez `channel:push`.

Voici une liste des filtres de recherche pris en charge :

| Chercher par | Filtre | Entrée |
| --- | --- | --- |
| Identifiant API de campagne | `api_id` | Un [identifiant API de campagne]({{site.baseurl}}/api/identifier_types#api-identifier-types) donné |
| Le segment ciblé par une campagne | `segment` | Nom du segment |
| Canal de communication ciblé par une campagne | `channel` | Un des éléments suivants : <br>-`content_cards` <br>- `email`<br>- `push`<br>- `sms` (renvoie à la fois les SMS et les MMS)<br>- `webhook`
| Type de statut ou de livraison | `status` | Un des éléments suivants : <br>- `one-time` <br>- `recurring` <br>- `triggered` <br>- `multivariate` <br>- `transactional` <br> - `drafts` <br> - `stopped` <br> - `archived` <br> - `all` |
| Balise | `tag` | - Un seul nom de balise <br>- Une liste de noms de balises séparés par des virgules |
| Éditeur le plus récent | `edited_by` | Adresse e-mail d’un utilisateur |
| Date à laquelle la campagne a été créée | `created` | - Une seule date au format `YYYY/MM/DD`<br> - Une plage de dates au format `YYYY/MM/DD-YYYY/MM/DD` |
| Date à laquelle la campagne a été éditée pour la dernière fois | `edited` | - Une seule date au format `YYYY/MM/DD`<br> - Une plage de dates au format `YYYY/MM/DD-YYYY/MM/DD` |
| Date à laquelle la campagne a été envoyée pour la dernière fois | `sent` | - Une seule date au format `YYYY/MM/DD`<br> - Une plage de dates au format `YYYY/MM/DD-YYYY/MM/DD` |
| Campagnes que vous avez créées | `created_by_me` | `true` |


[1]: {% image_buster /assets/img_archive/campaign_search.png %}
[2]: {% image_buster /assets/img_archive/campaign_search2.png %}
[3]: {% image_buster /assets/img_archive/campaign_search3.png %}