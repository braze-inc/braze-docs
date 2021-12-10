---
nav_title: Générations précédentes
article_title: Génération de messages dans l'application précédente
page_order: 20
page_type: Référence
description: "Cet article passe en revue les informations sur les messages dans l'application en Brésil."
channel: messages intégrés à l'application
noindex: vrai
---

# Générer les messages précédents dans l'application

{% alert important %}
Cette page passe en revue les informations précédentes autour de nos messages dans l'application. Pour voir les informations les plus à jour sur la génération actuelle de messages dans l'application, consultez notre documentation actuelle de [messages dans l'application]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/).
{% endalert %}

## Universel

Ceci va examiner les informations précédentes autour de nos messages dans l'application. Pour voir les informations les plus à jour sur la génération actuelle de messages dans l'application, consultez notre [documentation d'aperçu des messages dans l'application]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/).

{% details Full-Screen %}
Celles-ci sont les plus intéressantes, mais aussi les plus intrusives puisqu’elles couvrent l’écran entier de votre utilisateur. Ils sont parfaits pour afficher de grandes images riches, et peuvent être utiles pour transmettre des informations très importantes, telles que des nouvelles fonctionnalités cruciales et des promotions qui expirent. Etant donné qu'ils sont plus perturbateurs de l'expérience de l'utilisateur, utilisez-les avec parcimonie pour le contenu prioritaire.

![Message plein écran]({% image_buster /assets/img_archive/braze_fullscreen.png %}){: style="largeur-max-80%;"}

__Fonctionnalités personnalisables__

- En-tête et corps du texte
- Une grande image
- Jusqu'à deux boutons d'appel à l'action avec un comportement séparé au clic et des liens profonds
- Couleurs différentes pour l'en-tête et le corps du texte, les boutons et l'arrière-plan
- Paires clé-valeur

{% enddetails %}
{% details  Modal %}
Ces messages ne sont pas aussi intrusifs que les messages en plein écran, car ils permettent toujours aux utilisateurs de voir une partie de l'interface utilisateur de votre application. Comme ils contiennent toujours des boutons et des images, les messages modaux peuvent être une meilleure option que les slideups si vous souhaitez une campagne visuelle plus interactive. Celles-ci sont idéales pour les contenus de priorité moyenne, tels que les mises à jour des applications et les événements non urgents.

![Message modal]({% image_buster /assets/img_archive/braze_modal.png %}){: style="largeur-max-80%;"}

__Fonctionnalités personnalisables__

- En-tête et corps du texte
- Une image ou une icône de badge personnalisable
- Jusqu'à deux boutons d'appel à l'action avec un comportement séparé au clic et des liens profonds
- Couleurs différentes pour l'en-tête et le corps du texte, les boutons et l'arrière-plan
- Paires clé-valeur

{% enddetails %}

{% details Traditional Slideup %}
Il s'agit du type de message le moins intrusif, mais il peut être plus ou moins attentif en fonction de votre utilisation des couleurs et des icônes de badges. Ceci peut être le format de message à utiliser lors de l'intégration de nouveaux utilisateurs et de les diriger vers des fonctionnalités spécifiques dans l'application. puisqu'ils ne mettent pas en pause l'expérience de l'application et permettent une exploration continue.

![Message Slideup]({% image_buster /assets/img_archive/stopwatch_slideup_IAM.gif %}){: style="max-width:50%;"}

__Fonctionnalités personnalisables__

- Corps du texte
- Une image ou une icône de badge personnalisable
- Couleurs différentes pour l'arrière-plan du slideup, le texte et l'icône
- Comportement de fermeture des messages
- Position du glissement (haut ou bas de l'écran de l'application)
- Paires clé-valeur

{% enddetails %}

<br>

## Web

Ceci va examiner les informations précédentes autour de messages plus personnalisés dans l'application. Pour voir les informations les plus à jour sur la génération actuelle de messages dans l'application, consultez notre [documentation de personnalisation]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/).

{% details Email Capture Message %}
Les messages de capture de courriel vous permettent d'inviter facilement les utilisateurs de votre site à soumettre leur adresse e-mail, après quoi il sera disponible dans le système Braze pour être utilisé dans toutes vos campagnes de messagerie.

![Message de capture d'email]({% image_buster /assets/img_archive/web-email-capture.png %}){: style="largeur-max-60%;"}

> Pour activer les messages de capture d'email dans l'application, votre intégration de SDK doit fournir l'option d'initialisation `allowUserSuppliedJavascript` à Braze, . `appboy.initialize('VOTRE API_KEY', {allowUserSuppliedJavascript: true})`. Ceci est pour des raisons de sécurité - les messages HTML dans l'application peuvent exécuter JavaScript donc nous avons besoin d'un responsable du site pour les activer.

__Fonctionnalités personnalisables__

- En-tête, corps et texte du bouton Soumettre
- Une image optionnelle
- Un lien optionnel "Conditions d'utilisation"
- Couleurs différentes pour l'en-tête et le corps du texte, les boutons et l'arrière-plan
- Paires clé-valeur

{% enddetails %}

{% details Custom HTML Message %}

Pendant que Braze est sorti de la boite de messages dans l'application peut être personnalisé de différentes manières, vous pouvez prendre encore plus de contrôle sur l'apparence de vos campagnes en utilisant des messages conçus et construits en utilisant HTML, CSS et JavaScript. Avec une composition simple, vous pouvez déverrouiller des fonctionnalités personnalisées et une image de marque pour répondre à vos besoins. Les messages HTML intégrés à l'application permettent un plus grand contrôle sur l'apparence d'un message, et tout ce qui est supporté par HTML5 est également pris en charge par Braze.

__Pont JavaScript (appboyBridge)__

Les messages HTML dans l'application prennent en charge une interface JavaScript « pont » vers le SDK Web de Braze, vous permettant de déclencher des actions personnalisées de Braze lorsque les utilisateurs cliquent sur des éléments avec des liens ou s'engagent autrement avec votre contenu. Les méthodes JavaScript suivantes sont prises en charge dans les messages HTML de Braze dans l'application:

{% include archive/appboyBridge.md platform="web" %}

De plus, pour le suivi des analytiques, tous les éléments `<a>` ou `<button>` dans votre HTML enregistreront automatiquement une action "clic" à la campagne associée au message dans l'application. Pour enregistrer un "clic de bouton" au lieu d'un "body click", indiquez soit la valeur de la chaîne de requête abButtonId sur le href de votre lien (par ex. `<a href="http://mysite.com?abButtonId=0">cliquez sur moi</a>`), ou fournissez un id sur l'élément HTML (e. . `<a id="0" href="http://mysite.com">cliquez sur moi</a>`). Notez que les seuls identifiants de bouton actuellement acceptés sont "0" et "1." Un lien avec un id de bouton de 0 sera représenté comme "Bouton 1" sur le Tableau de bord, alors qu'un lien avec un identifiant de bouton de 1 sera représenté comme "Bouton 2."

> Pour activer les messages HTML dans l'application, votre intégration SDK doit fournir l'option d'initialisation `allowUserSuppliedJavascript` au Brésil : par exemple `appboy. nitialize('VOTRE API_COUR', {allowUserSuppliedJavascript: true})`. Ceci est pour des raisons de sécurité - les messages HTML dans l'application peuvent exécuter JavaScript donc nous avons besoin d'un responsable du site pour les activer.

{% enddetails %}

{% details HTML In App-Message Templates %}

Nous avons conçu un ensemble de modèles de messages HTML5 dans l'application pour vous aider à démarrer. Consultez notre [dépôt Github](https://github.com/Appboy/appboy-custom-html5-in-app-message-templates) qui contient des instructions détaillées sur la façon d'utiliser et de personnaliser ces modèles pour vos besoins.

__Fonctionnalités personnalisables__

- Polices
- Styles
- Images + Vidéos
- Comportements du clic
- Composants interactifs

{% enddetails %}

<br>

## Caractéristiques

Ceci va examiner les informations précédentes autour des spécifications créatives de notre message dans l'application. pour voir les informations les plus à jour sur la génération de messages actuels dans l'application, consultez notre [documentation de spécification créative]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/).

### Limites de caractères et d'images

Pour tous les types de messages dans l'application listés dans le tableau ci-dessous, les directives supplémentaires suivantes s'appliquent :

- **Taille d'image recommandée :** 500 Ko
- **Taille maximale de l'image :** 5 Mo
- **Types de fichiers supportés :** PNG, JPG, GIF

| Type de texte                          | Ratio d'aspect | Nombre maximum de caractères |
|:-------------------------------------- |:--------------:|:----------------------------:|
| Portrait plein écran (Image seulement) |     10:16      |             240              |
| Portrait plein écran (avec texte)      |      5:4       |             240              |
| Paysage plein écran (avec texte)       |      16:5      |             240              |
| Paysage plein écran (Image seulement)  |     16:10      |             240              |
| Glissement vers le haut                |      1:1       |             140              |
| Modal (Image uniquement)               |      1:1       |             140              |
| Modal (Avec du texte)                  |     29:10      |             140              |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Garder la taille des fichiers de messages dans l'application petite

Braze vous recommande de garder vos images, et les assets HTML aussi petits que possible pour plusieurs raisons:

- Les petits payloads HTML et images de messages seront téléchargés plus rapidement et s'afficheront plus rapidement et de manière plus fiable pour vos clients.
- Les petits blocs HTML et de messages image réduiront également les coûts de données de votre client. Les messages Braze dans l'application sont téléchargés en arrière-plan au démarrage de la session afin qu'ils puissent être déclenchés en temps réel en fonction des critères que vous avez sélectionnés. Par conséquent, si vous avez 10 messages HTML dans l'application de 1 Mo chacun, vos clients auraient tous des frais de 10 Mo de données même s'ils n'ont jamais déclenché tous ces messages. Cela peut s'ajouter rapidement au fil du temps, même si les messages dans l'application sont mis en cache et non retéléchargés session en session.

Les stratégies suivantes sont utiles pour maintenir la taille des fichiers vers le bas :

- Polices de référence intégrées dans votre application ou votre site Web pour personnaliser vos messages HTML dans l'application plutôt que d'inclure les fichiers de police dans votre dossier ZIP de contenu HTML.
- Assurez-vous qu'aucun code source CSS ou JavaScript externe ou duplicatif ne soit inclus dans vos ZIP de l'asset HTML.
- Utilisez [ImageOptim][25] sur toutes les images pour compresser les images à leur taille minimum sans aucune réduction de la qualité.

### Spécifications de l'iPhone 5

!\[Spécifications iPhone 5\]\[18\]

### Spécifications de l'iPhone 6

!\[Spécifications iPhone 6\]\[19\]
[18]: {% image_buster /assets/img_archive/In-AppMsg_Mockups+Specs_05.png %}
[19]: {% image_buster /assets/img_archive/In-AppMsg_Mockups+Specs_06.png %}

[25]: https://imageoptim.com/
