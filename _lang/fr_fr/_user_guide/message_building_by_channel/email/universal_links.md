---
nav_title: Liens universels et liens vers les applications
article_title: Liens universels et liens vers les applications
page_order: 6.4
page_type: reference
description: "Cet article d'aide vous explique comment configurer les liens universels Apple et les liens applicatifs Android."
channel: email
---

# Liens universels et liens vers les applications

Les liens universels Apple et les liens vers les applications Android sont des mécanismes conçus pour assurer une transition fluide entre les contenus web et les applications mobiles. Alors que les liens universels sont spécifiques à iOS, les liens d'application Android ont la même fonction pour les applications Android.

## Comment fonctionnent les liens universels et les liens applicatifs ?

Les liens universels (iOS) et les liens d'application (Android) sont des liens web standard (`http://mydomain.com`) qui pointent à la fois vers une page web et vers un élément de contenu à l'intérieur d'une application.

Lorsqu'un lien universel ou App Link est ouvert, le système d'exploitation vérifie si une application installée est enregistrée pour ce domaine. Si une application est trouvée, elle est lancée immédiatement sans jamais charger la page web. Si aucune application n'est trouvée, l'URL web est chargée dans le navigateur web par défaut de l'utilisateur, qui pourrait également être configuré pour rediriger vers l'App Store ou le Google Play Store respectivement.

En clair, les liens universels permettent à un site web d'associer ses pages web à des écrans d'application spécifiques. Ainsi, lorsqu'un utilisateur clique sur un lien vers une page web correspondant à un écran d'application, l'application peut être ouverte directement (si l'application est déjà installée).

Ce tableau présente les principales différences entre les liens universels et les liens profonds traditionnels :

|                        | Liens universels et liens vers les applications                                  | Liens profonds                   |
| ---------------------- | -------------------------------------------------------------- | ---------------------------- |
| Compatibilité des plateformes | iOS (à partir de la version 9) et Android (à partir de la version 6.0)  | Utilisé dans divers systèmes d'exploitation mobiles    |
| Objectif                | Reliez de façon fluide/sans heurts/de façon homogène le contenu des sites web et des applications sur les appareils iOS et Android. | Lien vers le contenu spécifique de l'application |
| Fonction               | Dirige vers des pages web ou du contenu d'application en fonction du contexte           | Ouvre des écrans spécifiques de l'application   |
| Installation de l'application       | Ouvre l'application si l'application est installée, sinon ouvre le contenu web | L'installation de l'application est nécessaire |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Cas d’utilisation

Les liens universels et les App Links sont le plus souvent utilisés pour les campagnes d'e-mail, car les e-mails peuvent être ouverts et cliqués aussi bien depuis un ordinateur de bureau que depuis un appareil mobile.

Certains canaux ne fonctionnent pas bien avec ces liens. Par exemple, les notifications push, les messages in-app et les cartes de contenu doivent utiliser des liens profonds basés sur des schémas (`mydomain://`).

{% alert note %}
Les liens vers les applications Android nécessitent une adresse `IBrazeDeeplinkHandler` personnalisée avec une logique permettant de traiter les liens de leurs domaines séparément des autres URL web. Il peut être plus facile d'utiliser des liens profonds et d'uniformiser les pratiques de création de liens pour les canaux autres que l'e-mail.
{% endalert %}

## Conditions préalables

Pour utiliser les liens universels et les liens applicatifs :

- Votre site web doit être accessible via HTTPS
- Votre application doit être disponible sur l'App Store (iOS) ou le Google Play Store (Android).

## Mise en place de liens universels et d'App Links

Pour que les apps prennent en charge les liens universels ou App Links, iOS et Android exigent qu'un fichier d'autorisations spécial soit hébergé dans le domaine du lien. Ce fichier contient les définitions des apps capables d'ouvrir les liens de ce domaine et, pour iOS, les chemins que ces apps sont autorisées à ouvrir :

- **iOS :** Dossier de l'Apple App Site Association (AASA)
- **Android :** Fichier de liens de ressources numériques

En plus de ce fichier de permissions, il existe des définitions codées en dur des domaines de liens que l'application est autorisée à ouvrir et qui sont configurées au sein de l'application :

- **iOS :** Définir comme "Domaines associés" dans Xcode
- **Android :** Défini dans le fichier `AndroidManifest.xml` de l'application

Cette association domaine-app en deux parties est nécessaire pour qu'un lien universel ou App Link fonctionne et empêche toute app de détourner les liens d'un domaine particulier ou tout domaine d'ouvrir une app particulière.

{% tabs %}
<!--iOS instructions-->
{% tab iOS %}

Ces étapes sont adaptées de la documentation destinée aux développeurs d'Apple. Pour plus d'informations, reportez-vous à la section [Autoriser les applications et les sites web à créer des liens vers votre contenu](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content?language=objc).

### Étape 1 : Configurez les droits de votre application

{% alert note %}
[Dans Xcode 13 et les versions ultérieures](https://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities/), Xcode peut gérer automatiquement le provisionnement des droits pour vous. Vous pouvez probablement passer à l'[étape 1c](#step-1c) et vous référer à ces instructions si vous avez des problèmes.
{% endalert %}

#### Étape 1a : Enregistrer votre application {#step-1a}

1. Allez sur developer.apple.com et connectez-vous.
2. Cliquez sur **Certificats, Identifiants et Profils.**
3. Cliquez sur **Identifiants**.
4. Si vous n'avez pas encore d'identifiant d'application enregistré, cliquez sur + pour en créer un.
   a. Saisissez un **nom**. Il peut s'agir de tout ce que vous voulez.
   b. Saisissez l'**ID de l'offre groupée**. Vous pouvez trouver votre ID de bundle à partir de l'onglet **Général** de votre projet Xcode pour la cible de création appropriée.

#### Étape 1b : Activez les domaines associés dans l'identifiant de votre application.

1. Dans votre identifiant d'application existant ou nouvellement créé, localisez la section **Services d'application**.
2. Sélectionnez **Domaines associés**.
3. Cliquez sur **Enregistrer**.

![]({% image_buster /assets/img_archive/universal_links_1b.png %}){: style="max-width:75%;"}

#### Étape 1c : Activez les domaines associés dans votre projet Xcode {#step-1c}

Avant de poursuivre, assurez-vous que votre projet Xcode a la même équipe sélectionnée que celle où vous venez d'enregistrer votre identifiant d'application. 

1. Dans Xcode, accédez à l'onglet **Capacités** de votre fichier de projet.
2. Activez les **domaines associés**.

##### Résolution des problèmes

Si vous voyez l'erreur "Un ID d'application avec l'identifiant 'votre-app-id' n'est pas disponible. Veuillez saisir une chaîne de caractères différente", procédez comme suit :

1. Vérifiez que vous avez sélectionné la bonne équipe.
2. Vérifiez que votre ID d'ensemble[(étape 1a](#step-1a)) de votre projet Xcode correspond à celui utilisé pour enregistrer l'identifiant d'application.

#### Étape 1d : Ajouter le droit au domaine

Dans la section des domaines, ajoutez l'étiquette de domaine appropriée. Vous devez le faire précéder de `applinks:`. Dans ce cas, vous pouvez voir que nous avons ajouté `applinks:yourdomain.com`.

![]({% image_buster /assets/img_archive/universal_links_1d.png %})

#### Étape 1e : Confirmez que le fichier des droits est inclus lors de la création du logiciel

Dans le navigateur de projet, assurez-vous que votre nouveau fichier de droits est sélectionné sous **Adhésion cible.**

Xcode devrait s'en charger automatiquement.

### Étape 2 : Configurez votre site web pour héberger le fichier de l'AASA

Pour associer le domaine de votre site web à votre app native sur iOS, vous devez héberger le fichier Apple App Site Association (AASA) sur votre site web. Ce fichier sert de moyen sécurisé pour vérifier la propriété du domaine auprès d'iOS. Avant iOS 9, les développeurs pouvaient enregistrer n'importe quel schéma URI pour ouvrir leurs apps, sans aucune vérification. Toutefois, grâce à l'AASA, ce processus est devenu beaucoup plus sûr et fiable.

Le fichier AASA contient un objet JSON avec une liste d'apps et les chemins d'URL sur le domaine qui doivent être inclus ou exclus en tant que liens universels. Voici un exemple de fichier AASA :

```json
{
  "applinks": {
    "apps": [],
    "details": [
      {
        "appID": “JHGFJHHYX.com.facebook.ios",
        "paths": [
          "*"
        ]
      }
    ]
  }
}
```

- `appID` : Créé en combinant l'**ID d'équipe** de votre application (allez sur `https://developer.apple.com/account/#/membership/` pour obtenir l'ID d'équipe) et l'**identifiant de l'offre groupée**. Dans l'exemple ci-dessus, "JHGFJHHYX" est l'ID de l'équipe et "com.facebook.ios" est l'ID de l'offre groupée.
- `paths` : Tableau de chaînes de caractères indiquant quels chemins sont inclus ou exclus de l'association. Vous pouvez utiliser `NOT` avant le chemin d'accès pour désactiver les chemins d'accès. Dans cet exemple, tous les liens de ce chemin iront sur le web au lieu d'ouvrir l'application. Vous pouvez utiliser `*` comme caractère générique pour activer tous les chemins d'accès d'un répertoire et `?` pour correspondre à un seul caractère (tel que /archives/201?/ pour correspondre à tous les numéros compris entre 2010 et 2019).

{% alert note %}
Ces chaînes sont sensibles à la casse et les chaînes de requête et les identificateurs de fragments sont ignorés.
{% endalert %}

### Étape 3 : Hébergez le fichier AASA sur votre domaine

Lorsque votre fichier AASA est prêt, vous pouvez maintenant l'héberger sur votre domaine, soit à l'adresse `https://<<yourdomain>>/apple-app-site-association`, soit à l'adresse `https://<<yourdomain>>/.well-known/apple-app-site-association`.

Téléchargez le fichier `apple-app-site-association` sur votre serveur web HTTPS. Vous pouvez placer le fichier à la racine de votre serveur ou dans le sous-répertoire `.well-known`. N'ajoutez pas `.json` au nom du fichier.

{% alert important %}
iOS ne tentera de récupérer le fichier AASA que par le biais d'une connexion sécurisée (HTTPS).
{% endalert %}

Lorsque vous hébergez le fichier de l'AASA, veillez à ce qu'il suive ces lignes directrices :

- est servi par HTTPS.
- Utilise le type MIME `application/json`.
- Ne dépasse pas 128 KB (exigence dans iOS 9.3.1 et plus)

### Étape 4 : Préparez votre application à gérer les liens universels

Lorsqu'un utilisateur tape sur un lien universel sur un appareil iOS, l'appareil lance l'appli et lui envoie un objet [NSUserActivity.](https://developer.apple.com/documentation/foundation/nsuseractivity)  L'application peut alors interroger l'objet NSUserActivity pour déterminer comment elle a été lancée.

Pour prendre en charge les liens universels dans votre application, procédez comme suit :

1. Ajoutez un droit qui spécifie les domaines pris en charge par votre application.
2. Mettez à jour le délégué de votre application pour qu'il réponde de manière appropriée lorsqu'il reçoit l'objet NSUserActivity.

Dans Xcode, ouvrez la section **Domaines associés** dans l'onglet **Capacités** et ajoutez une entrée pour chaque domaine pris en charge par votre app, préfixée par `applinks:`. Par exemple, `applinks:www.mywebsite.com`.

{% alert note %}
Apple recommande de limiter cette liste à 20 ou 30 domaines au maximum.
{% endalert %}

### Étape 5 : Testez votre lien universel

Ajoutez le lien universel à un e-mail et envoyez-le à un appareil de test. Le fait de coller un lien universel directement dans le champ URL de Safari n'entraînera pas l'ouverture automatique de l'application. Dans ce cas, vous devrez manuellement tirer le site web vers le bas afin qu'une invite apparaisse en haut et vous demande d'ouvrir l'application correspondante.

{% endtab %}

<!--Android instructions-->
{% tab Android %}

Ces étapes sont adaptées de la documentation destinée aux développeurs Android. Pour plus d'informations, reportez-vous aux sections [Ajouter des liens vers des applications Android](https://developer.android.com/training/app-links#add-app-links) et [Créer des liens profonds vers le contenu d'une application](https://developer.android.com/training/app-links/deep-linking).

{% alert note %}
Les liens vers les applications Android nécessitent une adresse `IBrazeDeeplinkHandler` personnalisée avec une logique permettant de traiter les liens de leurs domaines séparément des autres URL web. Il peut être plus facile d'utiliser des liens profonds et d'uniformiser les pratiques de création de liens pour les canaux autres que l'e-mail.
{% endalert %}

### Étape 1 : Création de liens profonds

Tout d'abord, vous devez créer des liens profonds pour votre application Android. Pour ce faire, ajoutez des [filtres d'intention](https://developer.android.com/guide/components/intents-filters) dans votre fichier `AndroidManifest.xml`. Le filtre d'intention doit inclure l'action `VIEW` et la catégorie `BROWSABLE`, ainsi que l'URL de votre site web dans l'élément de données.

### Étape 2 : Associez votre application à votre site web

Vous devez associer votre application à votre site web. Pour ce faire, vous pouvez créer un fichier de liens de ressources numériques. Ce fichier doit être au format JSON et contient des informations sur les applications Android qui peuvent ouvrir des liens vers votre site web. Il doit être placé dans le répertoire `.well-known` de votre site web.

### Étape 3 : Mettez à jour le fichier manifeste de votre application

Dans votre fichier `AndroidManifest.xml`, ajoutez un élément de méta-données à l'intérieur de l'élément d'application. L'élément meta-data doit avoir un attribut `android:name` de "asset_statements" et un attribut `android:resource` qui pointe vers un fichier de ressources avec une chaîne de caractères qui inclut l'URL de votre site web.

### Étape 4 : Préparez votre application à gérer les liens profonds

Dans votre application Android, vous devez gérer les liens profonds entrants. Pour ce faire, vous pouvez obtenir l'intention qui a déclenché votre activité et en extraire les données.

### Étape 5 : Test de vos liens profonds

Enfin, vous pouvez tester vos liens profonds. S'envoyer un lien par le biais d'une appli de messages ou d'un e-mail et cliquer dessus. Si tout est configuré correctement, votre application devrait s'ouvrir.

{% endtab %}
{% endtabs %}

## Liens universels, App Links et suivi des clics

{% alert note %}
Les liens de suivi des clics sont généralement mis en place dans le cadre de votre onboarding pour l'e-mail. Si cela n'a pas été fait lors de l'onboarding du client, contactez votre gestionnaire de compte pour obtenir de l'aide.
{% endalert %}

Nos partenaires d'envoi d'e-mails, SendGrid et SparkPost, utilisent des domaines de suivi des clics pour envelopper tous les liens et inclure des paramètres d'URL pour le suivi des clics dans les e-mails de Braze.

Par exemple, un lien comme `https://www.example.com` devient quelque chose comme `https://links.email.example.com/uni/wf/click?upn=abcdef123456…`.

Pour permettre aux liens d'e-mail avec suivi des clics de fonctionner comme des liens universels ou des App Links, vous devrez effectuer quelques configurations supplémentaires. Veillez à ajouter le domaine de suivi des clics (`links.email.example.com`) en tant que domaine que l'application est autorisée à ouvrir. En outre, le domaine de suivi des clics doit servir les fichiers AASA (iOS) ou Digital Asset Links (Android). Cela vous permettra de vous assurer que les liens d'e-mail avec suivi des clics fonctionnent de façon fluide/sans heurts/de façon homogène.

Si vous ne souhaitez pas que chaque lien de suivi des clics soit un lien universel ou un App Link, vous pouvez spécifier quels liens doivent être des liens universels en fonction du partenaire d'envoi de l'e-mail. Reportez-vous aux sections suivantes pour plus de détails.

### SendGrid

Pour traiter un lien de suivi des clics Sendgrid comme un lien universel :

1. Configurez vos valeurs pathPrefix AASA ou AndroidManifest pour ne traiter que les liens avec `/uni/` dans le chemin URL comme des liens universels.
2. Ajoutez l'attribut `universal="true"` à l'étiquette d'ancrage de votre lien (`<a>`). Cette opération modifie le chemin d'accès à l'URL du lien enveloppé pour y inclure `/uni/`.

{% alert note %}
Pour les e-mails AMP, cet attribut doit être data-universal="true".
{% endalert %}

Par exemple :

```html
<a href=”https://www.example.com” universal="true">
```

{:start="3"}
3\. Assurez-vous que votre application est configurée pour gérer correctement les liens enveloppés. Reportez-vous à l'article de SendGrid sur la [résolution des liens de suivi des clics SendGrid](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-sendgrid-click-tracking-links) et suivez les étapes correspondant à votre système d'exploitation. Cet article contient des exemples de code pour [iOS](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-ios) et [Android](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-android).

Avec cette configuration, les liens avec `/uni/` dans le chemin URL fonctionneront comme des liens universels, tandis que tous les autres liens fonctionneront comme des liens web.

### SparkPost

Pour traiter un lien de suivi des clics SparkPost comme un lien universel, ajoutez l'attribut suivant à la section Attributs de l'éditeur par glisser-déposer pour l'e-mail, ou modifiez manuellement le code HTML du lien pour inclure l'attribut suivant dans l'étiquette d'ancrage de votre lien : `data-msys-sublink="custom_path"`.

Ce chemin personnalisé vous permet de traiter sélectivement les URLs ayant cette valeur comme un lien universel.

Par exemple :

```html
<a href=”https://www.example.com” data-msys-sublink="open-in-app">
```

Ensuite, assurez-vous que votre application est configurée pour gérer correctement le chemin personnalisé. Consultez l'article de SparkPost sur l' [utilisation du suivi des clics de SparkPost sur les liens profonds.](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#preferred-solution-using-sparkpost-click-tracking-on-deep-links) Cet article contient des exemples de code pour [iOS](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#ios-swift-forwarding-clicks-to-sparkpost) et [Android](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#forwarding-clicks-from-android-to-sparkpost).

### Désactiver le suivi des clics pour chaque lien

Vous pouvez désactiver le suivi des clics pour des liens spécifiques en ajoutant un code HTML à votre message e-mail pour l'éditeur HTML ou à un bloc HTML pour l'éditeur glisser-déposer.

#### SendGrid

Si votre fournisseur de services d'e-mailing est SendGrid, utilisez le code HTML `clicktracking=off` comme suit :

```HTML
<a clicktracking=off href="[INSERT https LINK HERE]">click here</a>
```

#### SparkPost 

Si votre fournisseur de services d'e-mailing est SparkPost, utilisez le code HTML `data-msys-clicktrack="0"` comme suit :

```HTML
<a data-msys-clicktrack="0" href="[INSERT https LINK HERE]">click here</a>
```

#### Amazon SES

Si votre fournisseur de services d'e-mailing est Amazon SES, utilisez le code HTML `ses:no-track` comme suit :

```HTML
<a ses:no-track href="[INSERT https LINK HERE]">click here</a>
```

#### Éditeur par glisser-déposer

Lorsque vous utilisez l'éditeur glisser-déposer d'e-mails, saisissez votre code HTML en tant qu'attribut personnalisé si votre lien est attaché à un texte, un bouton ou une image.

##### Attribut personnalisé pour un lien de texte

#### SendGrid

Sélectionnez les éléments suivants pour l'attribut personnalisé :

- **Nom :** `clicktracking`
- **Valeur :** `off`

#### SparkPost

Sélectionnez les éléments suivants pour l'attribut personnalisé :

- **Nom :** `data-msys-clicktrack`
- **Valeur :** `0`

![Un attribut personnalisé pour un lien de texte.]({% image_buster /assets/img/text_click_tracking_off.png %}){: style="max-width:60%;"}

##### Attribut personnalisé pour un bouton ou une image

#### SendGrid

Sélectionnez les éléments suivants pour l'attribut personnalisé :

- **Nom :** `clicktracking`
- **Valeur :** `off`
- **Type :** Lien

#### SparkPost

Sélectionnez les éléments suivants pour l'attribut personnalisé :

- **Nom :** `data-msys-clicktrack`
- **Valeur :** `0`
- **Type :** Lien

![Un attribut personnalisé pour un bouton.]({% image_buster /assets/img/button_click_tracking_off.png %}){: style="max-width:60%;"}

### Résolution des problèmes des liens universels avec le suivi des clics

Si vos liens universels ne fonctionnent pas comme prévu dans vos e-mails, par exemple en faisant passer le destinataire de son application e-mail au navigateur web avant de le rediriger finalement vers l'application, consultez ces conseils pour résoudre les problèmes liés à la configuration de votre lien universel.

#### Vérifier l'emplacement/localisation du fichier de liaison

Assurez-vous que le fichier AASA (iOS) ou le fichier Digital Asset Links (Android) se trouve au bon emplacement/localisation :

- **iOS :** `https://click.tracking.domain/.well-known/apple-app-site-association`
- **Android :** `https://click.tracking.domain/.well-known/assetlinks.json`

Il est important de veiller à ce que ces fichiers soient toujours accessibles au public. Si vous ne pouvez pas y accéder, il se peut que vous ayez oublié une étape dans la configuration des liens universels pour l'e-mail.

#### Vérifier la définition des domaines

Assurez-vous que les définitions des domaines que votre application est autorisée à ouvrir sont correctes.

- **iOS :** Passez en revue les domaines associés configurés dans Xcode pour votre app[(étape 1c)]({{site.baseurl}}/help/help_articles/email/universal_links/?tab=ios#step-1c). Vérifiez que le domaine de suivi des clics est inclus dans cette liste.
- **Android :** Ouvrez la page d'information de l'application (appuyez longuement sur l'icône de l'application et cliquez sur ⓘ). Dans le menu d'information sur l'application, repérez l'**option Ouvrir par défaut** et appuyez dessus. Un écran devrait s'afficher avec tous les liens vérifiés que l'application est autorisée à ouvrir. Vérifiez que le domaine de suivi des clics est inclus dans cette liste.

