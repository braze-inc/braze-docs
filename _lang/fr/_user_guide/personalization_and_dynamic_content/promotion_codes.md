---
nav_title: Promotion Codes
article_title: Promotion Codes
page_order: 5
alias: "/promotion_codes/"
description: "Le présent article de référence explique comment créer des listes de codes de promotion et les ajouter à vos campagnes et à vos Canvas."

---

# Codes de promotion

> Les codes de promotion également appelés codes promo, sont un excellent moyen de maintenir l’engagement des utilisateurs en conduisant des interactions en soulignant les achats.

Grâce à la fonctionnalité Liquid de Braze, nous proposons un moyen de faire un usage de code de promotion étendu, ce qui permet aux messages d’utiliser la liste de promotions que vous avez fournie, automatiquement et intuitivement. La fonctionnalité de codes de promotion offre des dates d’expiration allant jusqu’à six mois et prend en charge jusqu’à 20 MM de codes individuels par liste.

{% alert important %}
Les codes de promotion ne peuvent pas être envoyés dans des messages in-app.
{% endalert %}

## Créer une liste de codes de promotion

### Étape 1 : Accédez à la section Code de promotion

![][1]{: style="float:right;max-width:30%;margin-left:15px;"}

Dans le tableau de bord, allez à **Promotion Code (Codes de promotion)**, situé dans la section **Integrations (Intégrations)** puis sélectionnez **Create Promotion Code List (Créer une liste de codes de promotion)**.

### Étape 2 : Nommer et créer votre code de promotion

Nommez votre liste de codes de promotion et ajoutez une description facultative.

![][2]{: style="max-width:90%"}

Ensuite, créez un extrait de code pour le code de promotion. Cet extrait de code correspond à ce que vous allez référencer dans Liquid pour afficher cet ensemble spécifique de codes de promotion. Assurez-vous qu’il s’agit d’un extrait de code qui n’est pas déjà utilisé dans une autre liste.

{% alert important %}
Les extraits de code sont sensibles à la casse. Par exemple « Birthday_promo » et « birthday_promo » seront reconnus comme deux extraits de code différents.
{% endalert %}

![][3]{: style="max-width:90%"}

{% alert warning %}
Vous ne pouvez pas changer l’extrait de code après avoir enregistré !
{% endalert %}

### Étape 3 : Options de code de promotion

Chaque liste de codes de promotion a une date et une heure d’expiration correspondantes définies lors de la création. La longueur maximale d’expiration est de six mois dans l’avenir, à partir du jour où vous créez ou modifiez votre liste. Dans ce délai, vous pouvez modifier et mettre à jour la date d’expiration à plusieurs reprises. Cette date d’expiration s’applique à tous les codes ajoutés à cette liste. À l’expiration, les codes sont supprimés du système Braze et tous les messages appelant l’extrait de code de cette liste ne sont pas envoyés.

![][4]{: style="max-width:90%"}

Vous avez également la possibilité de configurer des alertes de seuil facultatives et personnalisables. Si cette option est définie, ces alertes envoient un e-mail au destinataire désigné, soit lorsque la liste est en cours de fonctionnement sur les codes de promotion disponibles dans cette liste, soit lorsque votre liste de codes de promotion est proche de l’expiration. Le destinataire est notifié une fois par jour.

![][5]

### Étape 4 : Téléchargement du code de promotion

Braze ne gère pas la création et l’échange de code. Vous devrez donc générer vos codes promo dans un fichier CSV et les télécharger sur Braze. Vous pouvez utiliser notre intégration intégrée avec [Voucherify]({{site.baseurl}}/partners/channel_extensions/loyalty/voucherify/) ou [Talon.One]({{site.baseurl}}/partners/channel_extensions/loyalty/talonone/) pour créer et exporter des codes promo. Assurez-vous qu’il n’y a qu’un seul code sur chaque ligne.

{% alert note %}
La taille maximale du fichier est de 100 Mo et la taille maximale de la liste est de 20 MM de codes inutilisés. Si le fichier incorrect a été téléchargé, il suffit de télécharger un nouveau fichier et le fichier précédent sera remplacé.
{% endalert %}

![][6]

Une fois le téléchargement terminé, cliquez sur **Save List (Enregistrer la liste)** pour enregistrer tous les détails et les codes que vous venez de saisir.

![][7]

Lorsque vous cliquez sur Enregistrer, une nouvelle ligne s’affiche dans l’**Historique des importations**. Pour actualiser le tableau pour voir si votre importation est terminée, cliquez sur <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-sync" ></span> **Sync (Synchronisation)** en haut du tableau.

![][8]

{% alert note %}
Les fichiers plus volumineux prendront quelques minutes à importer. Pendant que vous attendez, vous pouvez quitter la page et travailler à autre chose pendant que l’importation est en cours. Une fois l’importation terminée, vous verrez le statut passer à **Terminé** dans le tableau.
{% endalert %}

#### Mettre à jour une liste de codes de promotion

Pour mettre à jour une liste, ouvrez simplement l’une de vos listes existantes. Vous pouvez modifier le nom, la description, l’expiration de la liste, les alertes de seuil et ajouter d’autres codes à la liste en téléchargeant de nouveaux fichiers et en cliquant sur **Update List (Mettre à jour la liste)**.
Tous les codes de la liste auront la même expiration, quelle que soit la date d’importation.

### Étape 5 : Utiliser des codes de promotion

Pour envoyer des codes de promotion dans les messages, cliquez sur **Copy Snippet (Copier l’extrait de code)** pour copier l’extrait de code que vous avez défini lors de la création de votre liste de codes de promotion.

![][9]{: style="max-width:70%"}

À partir de là, vous pouvez coller ce code dans un message du tableau de bord.

![][10]{: style="max-width:70%"}

Avec [Liquid][11], vous pouvez insérer un des codes de promotion uniques du fichier CSV téléchargé dans un message. Ce code sera marqué comme envoyé sur le backend Braze pour s’assurer qu’aucun autre message n’envoie ce même code. Lorsqu’un extrait de code est utilisé dans une campagne multicanal ou un composant Canvas, chaque utilisateur reçoit toujours un code unique. Si un utilisateur particulier est éligible pour recevoir un code via plusieurs canaux, cet utilisateur recevra le même code dans chaque canal. 

Si l’utilisateur reçoit deux messages à partir de deux canaux, un seul code sera affiché et utilisé dans les deux messages. Ceci s’applique également aux objectifs de reporting : un code sera envoyé et reçu par l’utilisateur par les deux canaux. Par exemple, pour une étape Canvas multicanale, un seul code serait utilisé par l’utilisateur.

{% alert important %}
S’il n’y a pas de codes de promotion restants disponibles lors de l’envoi d’un test ou des messages en direct d’une campagne qui envoie des codes de promotion, le message ne sera pas envoyé.
{% endalert %}

## Déterminer le nombre de codes utilisés

Vous pouvez trouver le nombre de codes restant dans la colonne **Restant** de la liste des codes de promotion, située sur la page **Promotion Codes (Codes de promotion)**.

![][12]{: style="max-width:90%"}

Ce compte de code peut également être trouvé lorsque vous avez consulté une page de liste de codes de promotion préexistante. 

![][13]{: style="max-width:50%"}

[1]:{% image_buster /assets/img/promocodes/promocode1.png %}
[2]:{% image_buster /assets/img/promocodes/promocode2.png %}
[3]:{% image_buster /assets/img/promocodes/promocode3.png %}
[4]:{% image_buster /assets/img/promocodes/promocode4.png %}
[5]:{% image_buster /assets/img/promocodes/promocode5.png %}
[6]:{% image_buster /assets/img/promocodes/promocode6.png %}
[7]:{% image_buster /assets/img/promocodes/promocode7.png %}
[8]:{% image_buster /assets/img/promocodes/promocode8.png %}
[9]:{% image_buster /assets/img/promocodes/promocode9.png %}
[10]:{% image_buster /assets/img/promocodes/promocode10.png %}
[11]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/
[12]: {% image_buster /assets/img/promocodes/promocode11.png %}
[13]: {% image_buster /assets/img/promocodes/promocode12.png %}
