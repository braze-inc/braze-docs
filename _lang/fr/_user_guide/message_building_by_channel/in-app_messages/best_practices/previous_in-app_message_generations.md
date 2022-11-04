---
nav_title: Générations précédentes
article_title: Générations précédentes de messages In-App
page_order: 20
page_type: reference
description: "Le présent article analyse des informations précédentes sur les messages In-App dans Braze."
channel: messages In-App
noindex: true

---

# Générations précédentes de messages In-App

{% alert important %}
Cette page analyse des informations précédentes sur nos messages In-App. Pour voir les informations les plus récentes sur notre génération de messages In-App, consultez notre documentation sur les [messages In-App]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/).
{% endalert %}

## Universel

Ceci analyse des informations précédentes sur nos messages In-App. Pour voir les informations les plus récentes sur notre génération de messages In-App, consultez notre [documentation de présentation des messages In-App]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/).

{% details Full-Screen %}
Ils sont les plus attrayants, mais aussi les plus intrusifs, car ils occupent tout l’écran de votre utilisateur. Ils sont parfaits pour afficher de grandes images riches, et ils s’avèrent utiles pour transmettre des informations cruciales, telles que de nouvelles fonctionnalités clés et des promotions arrivant à terme. Sachant qu’ils perturbent davantage l’expérience utilisateur, utilisez-les avec modération pour le contenu prioritaire.

![Message plein écran]({% image_buster /assets/img_archive/braze_fullscreen.png %}){: style="max-width:80%;"}

**Fonctions personnalisables**

- En-tête et texte du corps
- Une grande image
- Jusqu’à deux boutons d’appel à l’action avec un comportement différent en cas de clic et des liens profonds
- Des couleurs différentes pour l’en-tête et le texte du corps, les boutons et l’arrière-plan
- Paires clé-valeur

{% enddetails %}
{% details  Modal %}
Ces messages ne sont pas aussi intrusifs que ceux plein écran, car ils permettent toujours aux utilisateurs de voir une partie de l’interface de votre application. Comme ils contiennent toujours des boutons et des images, les messages modaux peuvent constituer une option preferable aux slideups pour une campagne visuelle plus interactive. Ils sont parfaits pour le contenu de priorité moyenne, comme les mises à jour d’applications et les offres et événements non urgents.

![Message modal]({% image_buster /assets/img_archive/braze_modal.png %}){: style="max-width:80%;"}

**Fonctions personnalisables**

- En-tête et texte du corps
- Une icône d’image ou de badge personnalisable
- Jusqu’à deux boutons d’appel à l’action avec un comportement différent en cas de clic et des liens profonds
- Des couleurs différentes pour l’en-tête et le texte du corps, les boutons et l’arrière-plan
- Paires clé-valeur

{% enddetails %}

{% details Traditional Slideup %}
Il s’agit du type de message le moins intrusif, bien qu’il puisse attirer l’attention selon les couleurs et les icônes de badge employées. Ce format de message peut être adapté lors de l’onboarding de nouveaux utilisateurs, pour les orienter vers des fonctionnalités spécifiques dans l’application, sachant qu’ils n’interrompent pas l’expérience sur l'application et permettent une navigation continue.

![Message slideup]({% image_buster /assets/img_archive/stopwatch_slideup_IAM.gif %}){: style="max-width:50%;"}

**Fonctions personnalisables**

- Texte du corps
- Une icône d’image ou de badge personnalisable
- Couleurs différentes pour l’arrière-plan, le texte et l’icône du slideup
- Comportement de fermeture du message
- Position du slideup (haut ou bas de l’écran de l’application)
- Paires clé-valeur

{% enddetails %}

<br>

## Web

Ceci analyse des informations précédentes sur des messages In-App plus personnalisés. Pour voir les informations les plus récentes sur notre génération de messages In-App, consultez notre [documentation sur la personnalisation]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/).

{% details Email capture message %}
Les messages de capture d’e-mail vous permettent d’inviter facilement les utilisateurs de votre site à soumettre leur adresse e-mail, après quoi vous en disposerez dans le système Braze pour l’ensemble de vos campagnes de messagerie.

![Message de capture d’e-mail]({% image_buster /assets/img_archive/web-email-capture.png %}){: style="max-width:60%;"}

>  Pour activer les messages in-app de capture d'e-mails, votre intégration SDK doit fournir l'option `allowUserSuppliedJavascript` d'initialisation à Braze, par exemple, `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Pour des raisons de sécurité, les messages In-App HTML peuvent en effet exécuter du JavaScript, d’où le besoin d’un responsable de site pour les activer.

**Fonctions personnalisables**

- Texte de l’en-tête, du corps et du bouton Soumettre
- Une image facultative
- Un lien facultatif aux conditions de service
- Des couleurs différentes pour l’en-tête et le texte du corps, les boutons et l’arrière-plan
- Paires clé-valeur

{% enddetails %}

{% details Custom HTML Message %}

Bien que les messages In-App Braze soient personnalisés de diverses façons, vous pouvez contrôler encore davantage l’apparence et l’impression de vos campagnes à l’aide de messages conçus et élaborés avec HTML, CSS et Javascript. Via une composition simple, vous pouvez débloquer des fonctionnalités et des marques personnalisées pour répondre à vos besoins. Les messages In-App HTML offrent un contrôle accru de l’apparence et de l’impression d’un message, et tout ce qui est pris en charge par HTML5 l’est également par Braze.

**Pont Javascript (appboyBridge)**

Les messages In-App HTML prennent en charge une interface de pont Javascript vers le SDK Web Braze, ce qui vous permet de déclencher des actions Braze personnalisées lorsque les utilisateurs cliquent sur des éléments avec des liens ou montrent un engagement avec votre contenu. Les méthodes Javascript suivantes sont prises en charge dans les messages In-App HTML Braze :

{% multi_lang_include archive/appboyBridge.md platform="web" %}

En outre, pour le suivi analytique, tous les éléments `<a>` ou `<button>` dans votre HTML enregistrent automatiquement une action de clic sur la campagne associée au message In-App. Pour enregistrer un « clic sur bouton » au lieu d’un « clic dans le corps », entrez une valeur de chaîne de caractères abButtonId dans les href de votre lien (par ex., `<a href="http://mysite.com?abButtonId=0">click me</a>`) ou un identifiant dans l’élément HTML (par ex., `<a id="0" href="http://mysite.com">click me</a>`). Notez que seuls les identifiants de bouton « 0 » et « 1 » sont actuellement acceptés. Un lien avec un ID de bouton 0 est représenté comme « Bouton 1 » dans le tableau de bord, tandis qu’un lien avec un ID de bouton 1 est représenté comme « Bouton 2 »."

>  Pour activer les messages In-App HTML, votre intégration SDK doit fournir `allowUserSuppliedJavascript`l’option d’initialisation à Braze, par exemple, `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Pour des raisons de sécurité, les messages In-App HTML peuvent en effet exécuter du JavaScript, d’où le besoin d’un responsable de site pour les activer.

{% enddetails %}

{% details HTML In App-Message Templates %}

Nous avons conçu un ensemble de modèles de messages In-App HTML5 pour vous aider à démarrer. Découvrez notre [référentiel Github](https://github.com/braze-inc/in-app-message-templates) qui contient des instructions détaillées sur la façon d’utiliser et de personnaliser ces modèles selon vos besoins.

**Fonctions personnalisables**

- Polices
- Styles
- Images et vidéos
- Comportement en cas de clic
- Composants interactifs

{% enddetails %}

<br>

## Spécifications

Ceci analyse des informations précédentes sur les spécifications créatives des messages In-App. Pour voir les informations les plus récentes sur notre génération de messages In-App, consultez notre [documentation sur les spécifications créatives]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/).

### Limites de caractères et d’image

Pour tous les types de messages In-App répertoriés dans le tableau suivant, les directives supplémentaires suivantes s’appliquent :

- **Taille d’image recommandée :** 500 ko
- **Taille d’image max. :** 5 Mo
- **Types de fichiers pris en charge :** PNG, JPG, GIF

| Type                               | Rapport d’aspect | Nombre max. de caractères |
| :--------------------------------- | :----------: | :-----------------: |
| Portrait plein écran (image uniquement)  |    10:16     |         240         |
| Portrait plein écran (avec texte)   |     5:4      |         240         |
| Paysage Plein écran (avec texte)  |     16:5     |         240         |
| Paysage plein écran (image uniquement) |    16:10     |         240         |
| Slideup                            |     1:1      |         140         |
| Modal (Image uniquement)                 |     1:1      |         140         |
| Modal (avec texte)                  |    29:10     |         140         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Conservation de petites tailles de fichiers de messages In-App

Braze vous recommande de conserver les zips de vos images et ressources HTML aussi petits que possible pour plusieurs raisons :

- Les charges utiles HTML et d’images plus petites se téléchargent et s’affichent plus vite et de manière plus fiable pour vos clients.
- Les charges utiles HTML et d’images plus petites permettent également de réduire les coûts des données de vos clients. Les messages In-App Braze sont téléchargés en arrière-plan au début de la session pour pouvoir être déclenchés en temps réel selon les critères sélectionnés. Par conséquent, si vous avez 10 messages In-App HTML d’1 Mo chaque, vos clients supportent aussi des frais de 10 Mo de données, même s’ils n’ont jamais déclenché tous ces messages. La somme peut rapidement augmenter avec le temps, même si les messages In-App sont mis en cache et ne sont pas téléchargés à nouveau à chaque session.

Les stratégies suivantes sont utiles pour conserver de petites tailles de fichiers :

- Les polices de référence intégrées dans votre application ou site Web permettent de personnaliser vos messages In-App HTML au lieu de les inclure dans votre dossier ZIP de ressources HTML.
- Assurez-vous qu’aucun CSS ou Javascript superflu ou dupliqué ne figure dans vos zips de ressources HTML.
- Utiliser [ImageOptim][25] sur toutes les images pour les compresser à leur taille minimale sans perdre en qualité.

### Spécifications de l’iPhone 5

![Spécifications de l’iPhone 5][18]

### Spécifications de l’iPhone 6

![Spécifications de l’iPhone 6][19]


[18]: {% image_buster /assets/img_archive/In-AppMsg_Mockups+Specs_05.png %}

[19]: {% image_buster /assets/img_archive/In-AppMsg_Mockups+Specs_06.png %}

[25]: https://imageoptim.com/
