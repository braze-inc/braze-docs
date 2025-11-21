---
nav_title: Utilisateurs
article_title: Gestion des utilisateurs de Braze
page_order: 0
page_type: reference
description: "Cet article de référence explique comment gérer les utilisateurs dans le compte de votre entreprise, y compris l'ajout, la suspension et la suppression d'utilisateurs."

---

# Gérer les utilisateurs de Braze

> Apprenez à gérer les utilisateurs dans le compte de votre entreprise, y compris l'ajout, la suspension et la suppression d'utilisateurs.

{% alert note %}
Plusieurs sections de cette page renvoient à la page **Utilisateurs de l'entreprise**. Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/), la rubrique **Utilisateurs de l'entreprise** s'appelle **Gérer les utilisateurs** et se trouve sous l'icône de votre compte.
{% endalert %}

## Ajouter des utilisateurs à Braze

Vous devez disposer d'autorisations d'administrateur pour ajouter des utilisateurs à votre compte Braze. 

Pour ajouter un nouvel utilisateur :

1. Allez dans **Paramètres** > **Utilisateurs de l'entreprise**.
2. Cliquez sur **\+ Ajouter un nouvel utilisateur**.
3. Saisissez les informations qui vous sont demandées, notamment leur e-mail, leur département et leur [rôle d'utilisateur]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#creating-a-role).

{% alert tip %}
Le service indiqué dans le profil d'un utilisateur détermine les types de communications qu'il reçoit de Braze. Ainsi, chacun ne reçoit que les communications et les alertes qui correspondent à la manière dont il utilise Braze.
{% endalert %}

\![Champs de détails de l'utilisateur.]({% image_buster /assets/img/add_new_user_2.png %}){: style="max-width:60%;"}

{:start="4"}

4. Pour les utilisateurs qui ne sont pas des administrateurs, sélectionnez les [autorisations]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#editing-a-users-permissions) au niveau de l'entreprise et de l'espace de travail dont vous souhaitez que cet utilisateur dispose.

Autorisations au niveau de l'espace de travail avec une section pour les champs d'autorisations personnalisés.]({% image_buster /assets/img/add_new_user_3.png %})

### Exigences en matière d'adresse e-mail

Chaque adresse e-mail utilisée dans une [instance]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) doit être unique. Cela signifie que si vous essayez d'ajouter une adresse e-mail déjà associée à un utilisateur qui avait ou a toujours accès à un espace de travail de l'entreprise dans cette instance, vous verrez apparaître un message d'erreur. 

Si votre équipe utilise Gmail et que vous rencontrez des difficultés pour ajouter une adresse e-mail, vous pouvez créer un alias en ajoutant un signe plus (+) comme "+1" ou "+test" à l'adresse e-mail. Par exemple, `contractor@braze.com` peut avoir pour alias `contractor+1@braze.com`. Les e-mails adressés à `contractor+1@braze.com` seront toujours délivrés à `contractor@braze.com`, mais l'alias sera reconnu comme une adresse e-mail unique.

### Puis-je modifier l'adresse e-mail de mon compte Braze ?

Pour des raisons de sécurité, les utilisateurs ne peuvent pas modifier l'adresse e-mail associée à leur compte Braze. Si un utilisateur souhaite mettre à jour son adresse e-mail, un administrateur doit lui [créer un nouveau compte](#adding-braze-users) avec son adresse e-mail préférée.

## Suspension des utilisateurs de Braze

La suspension d'un utilisateur met son compte dans un état inactif, où l'utilisateur ne peut plus se connecter, mais où les données associées à son compte sont conservées. Seuls les administrateurs peuvent suspendre ou annuler la suspension des utilisateurs de Braze.

Pour suspendre un utilisateur, allez dans **Paramètres** > **Utilisateurs de l'entreprise**, recherchez son nom d'utilisateur et sélectionnez <i class="fa-solid fa-user-lock"></i> **Suspendre**.

\![Option permettant de suspendre un utilisateur.]({% image_buster /assets/img_archive/suspend_user.png %})

Les administrateurs peuvent également suspendre un utilisateur en sélectionnant son nom dans la liste et en cliquant sur **Suspendre l'utilisateur** dans le pied de page.

Suspendez un utilisateur lorsque vous modifiez ses coordonnées.]({% image_buster /assets/img_archive/suspend_user2.png %}){: style="max-width:70%;"}

## Attribution de l'accès et des responsabilités des utilisateurs

{% multi_lang_include permissions.md content="Differences" %}

## Suppression d'utilisateurs de Braze

Pour supprimer un utilisateur, allez dans **Paramètres** > **Utilisateurs de l'entreprise**, recherchez son nom d'utilisateur et sélectionnez <i class="fa fa-trash-can"></i> **Supprimer l'utilisateur**.

\![Supprimer un utilisateur]({% image_buster /assets/img_archive/delete_user_new.png %})

Après la suppression d'un utilisateur, Braze ne conserve aucune des données de compte suivantes :

- Tous les attributs que l'utilisateur avait
- Adresse e-mail
- Numéro de téléphone
- ID externe
- Genre
- Pays
- Langue
- Autres données similaires

Braze conservera les données de compte suivantes :

- Attributs personnalisés ou données de test associés à leur compte
- les campagnes ou les toiles qu'ils ont créées (mais le nom de l'utilisateur n'y apparaîtra pas, par exemple dans la colonne **Dernière modification par** ).

### Impact de la suppression d'un utilisateur du tableau de bord

Lorsqu'un utilisateur de tableau de bord est supprimé, il n'y aura pas d'impact significatif sur les ressources qu'il a créées dans le tableau de bord, telles que les campagnes, les segments et les Canevas. Toutefois, il est important de noter que le champ **Created By (Créé par)** de ces ressources affichera une valeur "null" au lieu de l'adresse e-mail de l'utilisateur supprimé.

Si un nouvel utilisateur du tableau de bord est créé par la suite avec la même adresse e-mail que l'utilisateur supprimé, Braze ne réassociera pas les ressources créées par l'utilisateur supprimé au nouvel utilisateur. Le nouvel utilisateur du tableau de bord fera table rase du passé et ne sera pas crédité en tant que créateur des ressources existantes dans le tableau de bord.

## Résolution des problèmes

### "L'e-mail est déjà pris" lors de l'ajout d'un utilisateur

Si vous essayez d'ajouter un nouvel utilisateur et que vous recevez un message d'erreur indiquant que l'e-mail est déjà pris, mais que vous ne le trouvez pas dans votre liste d'utilisateurs, il est fort probable que cet utilisateur existe dans une autre instance du même groupe de tableaux de bord de Braze.

Pour créer ce nouvel utilisateur, vous pouvez effectuer l'une des opérations suivantes :

1. Supprimez l'utilisateur de l'autre instance avant de pouvoir le créer dans la nouvelle, ou
2. Créez l'utilisateur avec une chaîne de caractères d'e-mail différente (telle que `testing+01@braze.com`) ou un autre alias d'utilisateur. 

Si vous ne recevez pas l'activation du message dans votre boîte de réception lorsque vous utilisez `testing+01@braze.com`, vérifiez auprès de votre équipe informatique que vous pouvez accepter des messages provenant de ce type d'adresse e-mail. Certains administrateurs filtrent les messages envoyés à des adresses e-mail comportant un `+`.

