---
page_order: 1.1
nav_title: Guide sur la création de liens profonds iOS
article_title: Guide sur la création de liens profonds iOS
description: "Découvrez quel type de lien profond utiliser pour votre application iOS, quand vous avez besoin d'un fichier AASA et quelles méthodes de délégation d'application mettre en œuvre."
channel:
  - push notifications
  - in-app messages
  - content cards
  - email
---

# Guide sur la création de liens profonds iOS

> Ce guide vous aide à choisir la stratégie de création de liens profonds la mieux adaptée à votre application iOS, en fonction du canal de communication que vous utilisez et de votre recours ou non à un fournisseur de liens tiers tel que Branch.

Pour plus de détails sur la mise en œuvre, veuillez consulter [la section Création de liens profonds]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift). Pour la résolution des problèmes, veuillez consulter [la section Résolution des problèmes de création de liens profonds]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting).

## Choix d'un type de lien

Il existe trois méthodes pour gérer les liens provenant des messages Braze dans votre application iOS. Chacun fonctionne différemment et convient à différents canaux et cas d'utilisation.

| Type de lien | Exemple | Meilleur pour | S'ouvre-t-il sans application installée ? |
|---|---|---|---|
| **Schéma personnalisé** | `myapp://products/123` | Notifications push, messages in-app, cartes de contenu | Non — le lien ne fonctionne pas |
| **Lien universel** | `https://myapp.com/products/123` | E-mails, SMS, canaux avec suivi des clics | Oui — revient au site web |
| **Ouvrir l’URL Web dans l’application** | Toute`https://`URL | Affichage de contenu Web dans une WebView modale | N/A — s'affiche dans WebView |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Liens profonds personnalisés

Les liens profonds personnalisés (par exemple, `myapp://products/123`) ouvrent votre application directement sur un écran spécifique. Il s'agit de l'option la plus simple pour les canaux où les liens ne sont pas modifiés par un tiers.

**Veuillez utiliser des liens profonds personnalisés lorsque :**
- Envoi de notifications push, de messages in-app ou de cartes de contenu
- Le lien ne doit pas nécessairement fonctionner si l'application n'est pas installée.
- Vous n'avez pas besoin du suivi des clics (encapsulation des liens ESP dans les e-mails).

**Veuillez ne pas utiliser de liens profonds personnalisés dans les cas suivants :**
- Envoi d'e-mails — Les ESP encapsulent les liens pour le suivi des clics, ce qui perturbe les schémas personnalisés.
- Il est nécessaire de disposer d'un lien redirigeant vers une page web si l'application n'est pas installée.

### Liens universels

Les liens universels (par exemple, `https://myapp.com/products/123`) sont des URL HTTPS standard que iOS peut rediriger vers votre application au lieu de les ouvrir dans un navigateur. Ils nécessitent une configuration côté serveur (un fichier AASA) et une configuration côté application (autorisation de domaines associés).

**Veuillez utiliser les liens universels dans les cas suivants :**
- Envoi d'e-mails. Votre ESP encapsule les liens pour le suivi des clics, par conséquent, les liens doivent être en HTTPS.
- Envoi de SMS ou d'autres canaux où les liens sont encapsulés ou raccourcis.
- Il est nécessaire que le lien redirige vers une page Web lorsque l'application n'est pas installée.
- Vous utilisez un fournisseur de liens tiers tel que Branch ou Appsflyer.

**Veuillez ne pas utiliser de liens universels dans les cas suivants :**
- Vous n'avez besoin que de liens profonds provenant de notifications push, de messages in-app ou de cartes de contenu. Les schémas personnalisés sont plus simples.

### Ouvrir l'URL Web dans l'application

Cette option ouvre une page Web dans une fenêtre WebView modale au sein de votre application. Tout est géré par le SDK Braze à l'aide de`Braze.WebViewController`  — vous n'avez pas besoin d'écrire de code de gestion des URL.

**Veuillez utiliser « Ouvrir l'URL Web dans l'application » lorsque :**
- Vous souhaitez afficher une page Web (telle qu'une promotion ou un article) sans quitter votre application.
- L'URL est une page Web HTTPS standard, et non un lien profond vers un écran d'application spécifique.

**Veuillez ne pas utiliser la fonction « Ouvrir l'URL Web dans l'application » dans les cas suivants :**
- Vous devez accéder à une vue spécifique dans votre application. Veuillez plutôt utiliser un schéma personnalisé ou un lien universel.
- La page Web nécessite une authentification ou comporte des en-têtes de politique de sécurité du contenu qui empêchent l'intégration.

## Ce dont vous avez besoin pour chaque type de lien

### Liens profonds personnalisés

| Condition | Détails |
|---|---|
| Dossier AASA | Non requis |
| `Info.plist` | Veuillez enregistrer votre programme sous`CFBundleURLTypes`et l'ajouter à `LSApplicationQueriesSchemes` |
| Méthode déléguée de l'application | Mettre`application(_:open:options:)`en œuvre l'analyse de l'URL et la navigation. |
| Configuration du SDK Braze | Aucun — le SDK ouvre les URL de schéma personnalisées par défaut. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Liens universels

| Condition | Détails |
|---|---|
| Dossier AASA | Obligatoire — hébergeur à `https://yourdomain.com/.well-known/apple-app-site-association` |
| Domaines associés | Veuillez ajouter`applinks:yourdomain.com`dans Xcode sous **Signing&Capabilities** |
| Méthode déléguée de l'application | Mettre en œuvre`application(_:continue:restorationHandler:)`pour gérer `NSUserActivity` |
| Configuration du SDK Braze | Définir `configuration.forwardUniversalLinks = true` |
| BrazeDelegate (facultatif) | Mettre en œuvre`braze(_:shouldOpenURL:)`pour un routage personnalisé (par exemple, Branch) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Si vous envoyez des e-mails via Braze, votre ESP (Sendgrid, SparkPost ou Amazon SES) intègre les liens dans un domaine de suivi des clics. Il est nécessaire d'héberger le fichier AASA sur votre domaine de suivi des clics également, et pas uniquement sur votre domaine principal. Pour une configuration complète, veuillez consulter [les liens universels et les liens vers les applications]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/).
{% endalert %}

### Ouvrir l'URL Web dans l'application

| Condition | Détails |
|---|---|
| Dossier AASA | Non requis |
| Méthode déléguée de l'application | Non requis — le SDK gère cela automatiquement. |
| Configuration du SDK Braze | Aucun — veuillez sélectionner **« Ouvrir l'URL Web dans l'application** » dans l'éditeur de campagne. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Lorsque vous avez besoin d'un fichier AASA {#when-aasa}

Un fichier Apple App Site Association (AASA) n'est requis que lorsque vous utilisez **des liens universels**. Il indique à iOS les URL que votre application peut traiter.

Vous avez besoin d'un fichier AASA lorsque :

- Vous envoyez des liens profonds dans des campagnes par e-mail (car les ESP encapsulent les liens dans des URL HTTPS de suivi des clics).
- Vous envoyez des liens profonds dans des campagnes SMS (car les liens peuvent être raccourcis en URL HTTPS).
- Vous utilisez Branch, Appsflyer ou un autre fournisseur de liens (car ils utilisent leurs propres domaines HTTPS).
- Vous pouvez utiliser des liens universels à partir de notifications push, de messages in-app ou de cartes de contenu (moins courant, mais possible avec `forwardUniversalLinks = true`).

Vous n'avez pas besoin d'un fichier AASA lorsque :

- Veuillez noter que vous ne devez utiliser les liens profonds personnalisés (par exemple, `myapp://`) qu'à partir de notifications push, de messages in-app ou de cartes de contenu.
- Veuillez utiliser l'option **« Ouvrir l'URL Web dans l'application** ».

Pour obtenir des instructions de configuration AASA, veuillez consulter [les liens universels et les liens vers les applications]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/#setting-up-universal-links-and-app-links).

## Lorsque vous avez besoin d'un code d'application pour gérer les liens {#when-app-code}

La méthode déléguée que vous implémentez dépend du type de lien que vous utilisez :

| Méthode déléguée | Poignées | Quand mettre en œuvre |
|---|---|---|
| `application(_:open:options:)` | Liens profonds personnalisés (`myapp://`) | Vous pouvez utiliser des liens profonds personnalisés à partir de n'importe quel canal. |
| `application(_:continue:restorationHandler:)` | Liens universels (`https://`) | Vous pouvez utiliser des liens universels à partir d'e-mails, de SMS ou avec `forwardUniversalLinks = true` |
| `BrazeDelegate.braze(_:shouldOpenURL:)` | Toutes les URL ouvertes par le SDK | Vous avez besoin d'une logique de routage personnalisée (par exemple, branche, traitement conditionnel, analyse/analytique). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Si vous utilisez un fournisseur de liens tiers tel que Branch, veuillez implémenter`BrazeDelegate.braze(_:shouldOpenURL:)`  pour intercepter les URL et les transmettre au SDK du fournisseur. Veuillez consulter [la section Branch pour la création de liens profonds]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/) afin d'obtenir un exemple complet.
{% endalert %}

## Utilisation de Branch avec Braze {#branch}

Si vous utilisez [Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/) comme fournisseur de liens, votre configuration nécessite quelques étapes supplémentaires par rapport à une configuration de lien universel standard :

1. **SDK de succursale** : Veuillez intégrer le SDK Branch conformément à [la documentation de Branch](https://help.branch.io/developers-hub/docs/native-sdks-overview).
2. **Domaines associés** : Veuillez ajouter votre domaine Branch (par exemple, `applinks:yourapp.app.link`) dans Xcode sous **Signing&Capabilities**.
3. **BrazeDelegate** : Mettre`braze(_:shouldOpenURL:)`en œuvre le routage des liens Branch vers le SDK Branch au lieu de laisser Braze les gérer directement.
4. **Veuillez transmettre les liens universels** : Veuillez définir`configuration.forwardUniversalLinks = true`dans votre configuration Braze SDK.

Pour plus de détails sur la mise en œuvre et des conseils de débogage, veuillez consulter [la branche pour la création de liens profonds]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/).