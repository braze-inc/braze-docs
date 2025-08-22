---
nav_title: Utilisateurs dupliqués
article_title: Utilisateurs dupliqués
description: "Découvrez comment trouver et fusionner les utilisateurs dupliqués dans votre tableau de bord de Braze."
page_order: 0
---

# Utilisateurs dupliqués

> Découvrez comment trouver et fusionner les utilisateurs dupliqués afin de maximiser l'efficacité de vos campagnes et de vos canvas.

{% alert tip %}
Pour fusionner des utilisateurs dupliqués à l'aide de l'API REST de Braze, consultez [POST : Fusionner les utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/).
{% endalert %}

## Fusion individuelle

Si une recherche d'utilisateurs renvoie des profils en double, vous pouvez fusionner chaque profil individuellement à partir du profil de l'utilisateur dans le tableau de bord de Braze.

### Étape 1 : Rechercher un profil dupliqué

Dans Braze, sélectionnez **Audience** > **Recherche d'utilisateurs.**

![Vignette « Recherche d'utilisateurs » mise en évidence dans le menu de navigation.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_search_users.png %}){: style="max-width:60%;"}

Saisissez un identifiant unique, tel qu'une adresse e-mail ou un numéro de téléphone, pour le profil dupliqué, puis sélectionnez **Rechercher**.

![La page "Recherche d'utilisateurs" du tableau de bord de Braze.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:60%;"}

### Étape 2 : Fusionner les doublons

Pour lancer le processus de fusion, sélectionnez **Fusionner les doublons**.

![Un des profils de l'utilisateur dupliqué.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_duplicates.png %}){: style="max-width:50%;"}

Choisissez le profil utilisateur à conserver et celui à fusionner, puis sélectionnez **Fusionner les profils**. Répétez ce processus jusqu'à ce que vous ayez fusionné tous les profils dupliqués.

![La page de fusion individuelle pour un profil dupliqué.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_profiles.png %}){: style="max-width:80%;"}

{% alert warning %}
Les profils utilisateurs dupliqués ne peuvent pas être récupérés après la fusion.
{% endalert %}

## Fusion en bloc

Lorsque vous fusionnez en masse des utilisateurs dupliqués, Braze trouve les profils avec des identifiants correspondants (comme une adresse e-mail) et fusionne toutes leurs données dans le profil le plus récemment mis à jour avec un `external_id`. S'il n'y a pas de profil avec `external_id`, le profil le plus récemment mis à jour sans `external_id` sera utilisé.

### Étape 1 : Accéder à Gérer l'audience

Dans le tableau de bord de Braze, sélectionnez **Audience** > **Gérer l'audience**.

![Vignette « Gérer l'audience » mise en évidence dans le menu de navigation.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_manage_audience.png %}){: style="max-width:60%;"}

### Étape 2 : Prévisualiser les résultats (facultatif)

Pour prévisualiser vos résultats avant de fusionner vos doublons, sélectionnez **Générer une liste de doublons**.

![Page « Gérer l'audience » avec l'option « Générer la liste des profils dupliqués » en surbrillance.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_generate_list.png %})

Braze génère votre aperçu et l'envoie à votre adresse e-mail sous la forme d'un fichier CSV.

![Un e-mail de Braze contenant un lien vers le fichier CSV généré.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/example_email.png %}){: style="max-width:60%;"}

Dans l'exemple suivant, Braze utilise l'ID externe de l'utilisateur pour signaler les profils en double et identifier celui à conserver. Si ces profils sont fusionnés en bloc, Braze utilisera le profil avec un ID externe comme nouveau profil principal de l'utilisateur.

{% tabs local %}
{% tab exemple de fichier CSV %}
| Adresse e-mail | ID externe | Numéro de téléphone | ID Braze | Identifiant de la règle | Profil à conserver | Profil à fusionner | Profil à supprimer
| ---------------- | ----------- | -------------- | --------------------- | ------------------- | --------------- | ---------------- |
| alex@company.com | A8i3mkd99 | (555) 123-4567 | 65fcaa547f470494d1370 | e-mail | VRAI | FAUX
| alex@company.com | | (555) 987-6543 | 65fcaa547f47d004d1348 | e-mail | FAUX | VRAI | VRAI | VRAI
| alex@company.com | | (555) 321-0987 | 65fcaa547f47d0049135c | e-mail | FAUX | VRAI | Vrai | Vrai
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

#### Comportement de fusion

Braze remplit les champs vides du profil conservé avec les valeurs du profil fusionné. Pour obtenir une liste des champs qui seront remplis, reportez-vous à la section [Comportement de fusion.]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior)

### Étape 3 : Fusionner vos doublons

Si vous êtes satisfait des résultats de votre aperçu, sélectionnez **Fusionner tous les profils dupliqués**.

{% alert warning %}
Les profils utilisateurs dupliqués ne peuvent pas être récupérés après la fusion.
{% endalert %}

![Page « Gérer l’audience » avec l'option « Fusionner tous les profils dupliqués » en surbrillance.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_merge_profiles.png %}){: style="max-width:70%;"}

## Fusion basée sur des règles

Vous pouvez utiliser des règles pour contrôler la manière dont les profils en double sont résolus lors de l'exécution d'une fusion, afin que le profil utilisateur le plus pertinent soit conservé. Lorsque des règles sont définies, Braze conserve les profils qui correspondent à vos critères.

### Étape 1 : Définir vos règles

1. Sélectionnez **Audience** > **Gérer l'audience** > **Modifier les règles**.
2. Dans la section **Profil à conserver** du panneau **Modifier les règles**, sélectionnez l'**identifiant** des profils qui seront conservés lors de la fusion des doublons. Il peut s'agir de l'adresse e-mail ou du numéro de téléphone.
3. Dans la section **Résoudre les liens**, sélectionnez les critères pour déterminer comment résoudre les liens entre les profils avec des critères correspondants de **Profil à conserver.** Vous pouvez sélectionner les éléments suivants :<br>
- **Résolvez les égalités en utilisant** : Date de création, Date de mise à jour, Dernière session
- **Établissement de priorités**: Le plus récent, le plus ancien

![Le panneau "Modifier les règles" avec des sections permettant de sélectionner des options pour "Profil à conserver" et "Résoudre les liens".]({% image_buster /assets/img/audience_management/duplicate_users/edit_rules.png %}){: style="max-width:40%;"}

Par exemple, vous pouvez conserver le profil qui comporte un numéro de téléphone. Si plusieurs utilisateurs ont le même numéro de téléphone, vous pouvez résoudre les problèmes d'égalité à l'aide du champ **Date de mise à jour** et donner la priorité à l'utilisateur dont le numéro a été mis à jour le plus récemment.

### Étape 2 : Prévisualiser les résultats (facultatif)

Après avoir enregistré vos règles, vous pouvez avoir un aperçu de leur fonctionnement en sélectionnant **Générer une liste de doublons.** Braze génère votre aperçu et l'envoie à votre adresse e-mail sous la forme d'un fichier CSV qui indique quels utilisateurs seraient conservés et fusionnés si vos règles étaient appliquées. 

### Étape 3 : Fusionner les doublons

Si vous êtes satisfait des résultats de votre aperçu, revenez à la page **Gérer l'audience** et sélectionnez **Fusionner tous les profils dupliqués**.

{% alert warning %}
Les profils utilisateurs dupliqués ne peuvent pas être récupérés après la fusion.
{% endalert %}

## Fusion planifiée

Similaire à la fusion basée sur des règles, la fusion planifiée vous permet d'automatiser la fusion des profils utilisateurs sur une base quotidienne à l'aide de règles préconfigurées.

![La page "Gestion de l'audience" avec le bouton "planification".]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_scheduled_merge_rules.png %})

Une fois la fonctionnalité activée, Braze attribue automatiquement un créneau horaire pour effectuer le processus de fusion tous les jours vers 12 heures dans le fuseau horaire de l'entreprise de l'utilisateur. Vous pouvez désactiver la fusion planifiée à tout moment. Braze informera les administrateurs de votre espace de travail 24 heures avant la fusion planifiée, afin de leur rappeler et de leur donner le temps de revoir la configuration.

{% alert warning %}
Les profils utilisateurs dupliqués ne peuvent pas être récupérés après la fusion.
{% endalert %}
