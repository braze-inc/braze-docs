---
nav_title: Stylisation de la page de test
page_order: 2
noindex: vrai
---

# Stylisation de la page de test

## Test de l'en-tête

{% tabs %}
{% tab Styling %}

# Bannière H1
Texte H1

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

## Bannière H2
Texte H2

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

### Bannière H3
Texte H3

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

#### Bannière H4
Texte H4

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

##### Bannière H5
Texte H5

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

###### Bannière H6
Texte H6

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

{% endtab %}
{% tab Markdown %}

```
# Bannière H1

## Bannière H2

### Bannière H3

#### Bannière H4

##### Bannière H5

###### Bannière H6
```
{% endtab %}
{% endtabs %}

## Ancre d'en-tête personnalisée

Pour ajouter une ancre à un en-tête, ajoutez le code suivant à la fin de la ligne sur laquelle le titre est placé. Remplacer `ancre` par l'ancre pour cette rubrique. Utilisez des lettres minuscules et mettez des traits d'union entre les mots.

```
# Texte d'en-tête {#anchor-text}
```

Vous pouvez lier à des titres avec des ancres personnalisées en créant un lien standard avec un panneau numéro `#` suivi de l'ancre personnalisée.

{% raw %}
```
Voici mon [link](#anchor-text)
```
{% endraw %}

## Font Test

{% tabs %}
{% tab Styling %}

Texte normal

*Texte de mise en valeur*

**Bold**

_**Gras Gras**_

~~Strikethrough~~

{% endtab %}
{% tab Markdown %}
```
Texte normal

*Texte de mise en évidence*

**Grand**

_**Gras d'empaquetage**_

~~Strikethrough~~
```
{% endtab %}
{% endtabs %}

## Test de devis

{% tabs %}
{% tab Styling %}
> Texte cité

#### Devis en ligne
Lorem ipsum dolor `sit amet, consectetur adipiscing elit`. Sed nec tortor at lectus tempus tempor.

#### Chunk de guillemets
```
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor.
```
{% endtab %}
{% tab Markdown %}
```
> Quoted Text

Lorem ipsum dolor ``sit amet, consectetur adipiscing elit``. Sed nec tortor at lectus tempus tempor.

``` Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. ```
```
{% endtab %}
{% endtabs %}

## Test de la table

{% tabs %}
{% tab Styling %}
| Instance | URL du tableau de bord                                                      | Point de terminaison REST       |
| -------- | --------------------------------------------------------------------------- | ------------------------------- |
| US-01    | `https://dashboard.braze.com` ou<br> `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com` |
| US-02    | `https://dashboard-02.braze.com`                                            | `https://rest.iad-02.braze.com` |
| US-03    | `https://dashboard-03.braze.com`                                            | `https://rest.iad-03.braze.com` |
| US-04    | `https://dashboard-04.braze.com`                                            | `https://rest.iad-04.braze.com` |
| US-06    | `https://dashboard-06.braze.com`                                            | `https://rest.iad-06.braze.com` |
| EU-01    | `https://dashboard.braze.eu` ou<br> `https://dashboard-01.braze.eu`   | `https://rest.fra-01.braze.eu`  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
{% endtab %}
{% tab Markdown %}
```
Instance | Dashboard URL | REST Endpoint
----------- |---------------- | --------------------
US-01 | `https://dashboard.braze.com` ou<br> `https://dashboard-01. raze.com` | `https://rest.iad-01.braze.com`
US-02 | `https://dashboard-02.braze.com` | `https://rest.iad-02.braze.com`
US-03 | `https://dashboard-03.braze. om` | `https://rest.iad-03.braze.com`
US-04 | `https://dashboard-04.braze.com` | `https://rest.iad-04.braze.com`
US-06 | `https://dashboard-06.braze.com` | `https://rest. ad-06.braze.com`
EU-01 | `https://dashboard.braze.eu` ou<br> `https://dashboard-01.braze.eu` | `https://rest.fra-01.braze.eu`
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
```
{% endtab %}
{% endtabs %}

#### Réinitialisation de la table par saut de mot par colonne
Pour les colonnes de tables dont le saut de mot doit être réinitialisé au style par défaut, utilisez les options markdown pour ajouter une classe à la table en utilisant `. eset-td-br-1`, `. eset-td-br-2`, `.reset-td-br-3` , `. eset-td-br-4`, avec le `#` correspondant à la colonne jusqu'à 4.

#### Usage
```
| Nom de l'événement | Type de flux | Description | Attributs personnalisés
| ------------------------------------ | ---------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| UNBROKENWORDTHATISVERYLONGUNBROKENWORDTHATISVERYLONG | Flux non lié | Un email a été envoyé avec succès au serveur de messagerie d'un utilisateur.                              | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id` |
| `UNBROKENHIGHLIGHTTHATISVERYLONGUNBROKENHIGHLIGHTTHATISVERYLONG` | Flux non lié | L'utilisateur a ouvert un e-mail.                                                                     | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id` |
| In-App Message Impression | Flux spécifique à la plate-forme | L'utilisateur a consulté un message In-App.                                                            | `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

```
{% tabs local %}
{% tab Before %}

| Nom de l'événement                                                         | Type de flux                    | Libellé                                                                       | Attributs personnalisés                                                       |
| -------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| format@@0 UNBROKENWORDTHATISVERYLONGUNBROKENWORDTHATISVERYLONG             | Flux non lié                    | Un e-mail a été envoyé avec succès au serveur de messagerie d'un utilisateur. | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| `format@@0 UNBROKENHIGHLIGHTTHATISVERYLONGUNBROKENHIGHLIGHTTHATISVERYLONG` | Flux non lié                    | L'utilisateur a ouvert un e-mail.                                             | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| Impression de message dans l'application                                   | Flux spécifique à la plateforme | L'utilisateur a consulté un message dans l'application.                       | `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id` |

{% endtab %}
{% tab After %}

| Nom de l'événement                                                         | Type de flux                    | Libellé                                                                       | Attributs personnalisés                                                       |
| -------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| format@@0 UNBROKENWORDTHATISVERYLONGUNBROKENWORDTHATISVERYLONG             | Flux non lié                    | Un e-mail a été envoyé avec succès au serveur de messagerie d'un utilisateur. | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| `format@@0 UNBROKENHIGHLIGHTTHATISVERYLONGUNBROKENHIGHLIGHTTHATISVERYLONG` | Flux non lié                    | L'utilisateur a ouvert un e-mail.                                             | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| Impression de message dans l'application                                   | Flux spécifique à la plateforme | L'utilisateur a consulté un message dans l'application.                       | `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}
{% endtab %}
{% endtabs %}

## Test du lien
{% tabs %}
{% tab Styling %}
Lien ici : [Braze.com](https://www.braze.com){: height="36px" width="36px"}
{% endtab %}
{% tab Markdown %}
```
[Braze.com](https://www.braze.com)
```
{% endtab %}
{% endtabs %}

## Test de l'image
{% tabs %}
{% tab Styling %}
Image: ![Logo]({{site.baseurl}}/assets/img/braze-logo-mark.png){: style="max-width:30%;"}

#### Test de l'image liée

Image liée: [![Braze]({{site.baseurl}}/assets/img/braze-logo-mark.png){: style="max-width:30%;"}](https://www.braze.com)

#### Style de l'image

![Texte du texte]({% image_buster /assets/img/logo-braze-fa.svg %}){: style="largeur-max:30%; couleur: vert" }

#### Images d'ancrage

![Texte du texte]({% image_buster /assets/img/logo-braze-fa.svg %}){: style="float:right;max-width:30%; color: vert" }
<br><br><br><br><br>
{% endtab %}
{% tab Markdown %}

```
![Logo]({{site.baseurl}}/assets/img/braze-logo-mark.png)

[![Braze]({{site.baseurl}}/assets/img/braze-logo-mark.png)](https://www.braze.com)

![Text]({% image_buster /assets/img/logo-braze-fa. vg %}){: style="max-width:30%; color: vert" }

![Text]({% image_buster /assets/img/logo-braze-fa.svg %}){: style="float:right;max-width:30%;" }
```
{% endtab %}
{% endtabs %}

## Test de la galerie
{% tabs %}
{% tab Styling %}
{% gallery %}
{{site.baseurl}}/assets/img_archive/EBTH_Email.png?bf892368baf287cba5ab9a6e3b09431d  <br> Ceci est un [lien](https://www.braze.com).
{{site.baseurl}}/assets/img_archive/iHeartRadio_Email.png?ecd2c8fe148939b7de957fe85cd6317e  <br> Ceci est un autre `commentaire`.
{{site.baseurl}}/assets/img_archive/Saucey_Email.png?b9768937a1cc12d4c08e55a52e700d68  <br> Ceci est encore un autre __commentaire__.
{{site.baseurl}}/assets/img/schellman_iso27001_seal_grey_CMYK_300dpi_jpg.png?1b1fb9dbb80b0332c62512dcf9c83258 <br> **IMAGE TITLE** <br> Ceci est un test pour voir s'il va se briser la ligne.
{{site.baseurl}}/assets/img/SOC2.png?6338040be8e98c4c9abe1f35b3e43e3a  <br> Ceci est un commentaire régulier.
{% endgallery %}
{% endtab %}
{% tab Markdown %}
{% raw %}
```
{% gallery %}
{{site.baseurl}}/assets/img_archive/EBTH_Email.png?bf892368baf287cba5ab9a6e3b09431d  <br> Ceci est un [link](https://www.braze.com).
{{site.baseurl}}/assets/img_archive/iHeartRadio_Email.png?ecd2c8fe148939b7de957fe85cd6317e  <br> Ceci est un autre `comment`.
{{site.baseurl}}/assets/img_archive/Saucey_Email.png?b9768937a1cc12d4c08e55a52e700d68  <br> Ceci est encore un autre __comment__.
{{site.baseurl}}/assets/img/schellman_iso27001_seal_grey_CMYK_300dpi_jpg.png?1b1fb9dbb80b0332c62512dcf9c83258 <br> **TITLE IMAGE** <br> C'est un test pour voir s'il va s'infiltrer à la ligne.
{{site.baseurl}}/assets/img/SOC2.png?6338040be8e98c4c9abe1f35b3e43e3a  <br> Ceci est un commentaire régulier.
{% endgallery %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Test de l'image interactive
{% tabs %}
{% tab Styling %}
<div class="iactiveImg" data-ii="6967"></div><script src="https://interactive-img.com/js/include.js"></script>
{% endtab %}
{% tab Markdown %}
```


<div class="iactiveImg" data-ii="6967"></div>

<script src="https://interactive-img.com/js/include.js"></script>
```
{% endtab %}
{% endtabs %}

<!--- Leaving formatting here just in case it's important...
<div style="position: relative; padding-bottom: 83%; padding-top: 0; height: 0;"><iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border-width:0px; max-width:100%; overflow-y:auto;" width="100%" height="100%" src="https://interactive-img.com/view?id=6967&iframe=true"></iframe></div>
-->

## Test de Snippet de Code

{% tabs %}
{% tab Styling %}
#### Objectif de test de code C
```objc
- ((void)submitFeedback:(ABKFeedback * )feedback
 withCompletionHandler:(nullable void (^)(ABKFeedbackSentResult feedbackSentResult))completionHandler;
```

#### Test de code Swift
```swift
Appboy.sharedInstance()?.submitFeedback(feedback) { (feedbackSentResult) in
      print("Feedback sent : (feedbackSentResult))
}
```

#### Test de code Java
```java
@Override
public void onResume() {
  super.onResume();
  // Enregistre le BrazeInAppMessageManager pour l'Activité courante. Cette activité va maintenant écouter les messages
  // dans l'application de Braze.
  BrazeInAppMessageManager.getInstance().registerInAppMessageManager(activity);
}
```

#### Code test json
```json
{
   "attributes" : "Attributes" ,
   "events" : ["Tableau", "Of", "Objet"],
   "achats" : ["Tableau" ,"Of" ,"Achat" ,"Objet"]
}
```

#### JavaScript de test de code
```javascript
appboy.subscribeToFeedUpdates(function(feed) {
  var cards = feed.cards;
  appboy.display.showFeed(undefined, cards);
});
appboy.requestFeedRefresh();
```

#### Test des Pygments
```python
#!/usr/bin/python3

depuis le moteur d'import RunForrestRun

"""Test code for syntax highlighting!"""

class Foo:
    def __init__(self, var):
        self.var = var
        self.run()

    def run(self) :
        RunForrestRun() # tourne avec eux !

```
{% endtab %}
{% tab Markdown %}
![Exemple de Markdown]({% image_buster /assets/img_archive/code_snippet.png %})
{% endtab %}
{% endtabs %}

## Test d'alerte

{% tabs %}
{% tab Styling %}

{% alert tip %}Ceci est une astuce{% endalert %}

{% alert note %}Ceci est une note{% endalert %}

{% alert important %}Ceci est une alerte importante{% endalert %}

{% alert warning %}Ceci est un avertissement{% endalert %}

{% alert update %}Ceci est une mise à jour{% endalert %}

{% endtab %}
{% tab Markdown %}
{% raw %}
```
{% alert tip %}
Ceci est une astuce
{% endalert %}

{% alert note %}
Ceci est une note
{% endalert %}

{% alert important %}
Ceci est une alerte importante
{% endalert %}

{% alert warning %}
Ceci est un avertissement
{% endalert %}

{% alert update %}
Ceci est une mise à jour
{% endalert %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Test vidéo intégré
{% tabs %}
{% tab Styling %}
#### Vidéo/YouTube embarqués
Par défaut sur youtube intégré.
{% include video.html id="XY5uXoKIvFY" %}

#### Alignement à droite de la vidéo intégrée
{% include video.html id="XY5uXoKIvFY" align="right" %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

#### Embedded Video Left Align
{% include video.html id="XY5uXoKIvFY" align="left" %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

{% endtab %}
{% tab Markdown %}

{% raw %}
```html
{% include video.html id="[youtubeid]" %}
```
{% endraw  %}

Aligner à droite ou à gauche, et limiter la largeur max à 50% utiliser le paramètre `aligner` = `gauche` ou `droite`:
{% raw  %}
```html
{% include video.html id="[youtubeid]" align="left" %}

{% include video.html id="[youtubeid]" align="right" %}
```
{% endraw  %}
{% endtab %}
{% endtabs %}

#### Mise en page vidéo vedette avec placement de statut pour une résolution plus élevée
Pour utiliser la mise en page vidéo en vedette qui place une vidéo statique sur le côté gauche pour un affichage de résolution plus élevée, ajouter un video_id et un video_type ie `youtube` à l'en-tête yaml de la page. video_source par défaut à `youtube`

{% raw  %}
```yaml
layout: featured_video
video_id: [video_id]
video_source: youtube
```
{% endraw  %}

## Test de la liste
{% tabs %}
{% tab Styling %}
#### Balle
* Liste 1
  * Sous-liste 1
* Liste 2
  * Sous-liste 2a
    * Sous-liste 2
* Liste 3

#### Numérotation
1. Liste 1
  * Sous-liste 1
2. Liste 2
3. Liste 3
  * Sous-liste 3a
  * Sous-liste 3b
    * Sous-liste 3
4. Liste 4
    1. Sous-liste 4a
        1. Sous-liste 4
    2. Sous liste 4b
        1. sous-liste 4

{% endtab %}
{% tab Markdown %}
```
#### Puce
* Liste 1
  * Sous-liste 1
* Liste 2
  * Sous-liste 2a
    * Sous-liste 2
* Liste 2 * Liste 3

#### Numéroté
1. Liste 1
  * Sous-liste 1
2. Liste 2
3. Liste 3
  * Sous-liste 3a
  * Sous-liste 3b
    * Sous-liste 3
4. Liste 4
    1. Sous liste 4a
        1. Sous-liste 4
    2. Sous liste 4b
        1. sous-liste 4
```
{% endtab %}
{% endtabs %}

## Test de contenu refermable
{% tabs %}
{% tab Styling %}
{% details Click me to Expand %}
#### Regardez un bloc de code caché !

```python
print("Bonjour le monde !")
```
{% enddetails %}
{% endtab %}
{% tab Markdown %}
{% raw %}
```liquid
{% details Click me to Expand %}
...
{% enddetails %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Test des onglets

#### Onglets personnalisés

{% tabs local %}
{% tab OBJECTIVE-C %}

Ajoute la ligne de code suivante à ton fichier `AppDelegate.m`:

```objc
{% if include.platform == 'iOS' %}#import "Appboy-iOS-SDK/AppboyKit.h"{% else %}#import <AppboyTVOSKit/AppboyKit.h>{% endif %}
```

Dans votre fichier `AppDelegate.m` , ajoutez le snippet suivant dans votre application `: didFinishLaunchingWithOptions`:

```objc
[Appboy startWithApiKey:@"VOTRE API-KEY"
         inApplication:application
     withLaunchOptions:launchOptions];
```

{% endtab %}
{% tab swift %}

Si vous intégrez le SDK Braze avec CocoaPods ou Carthage, ajoutez la ligne de code suivante à votre fichier `AppDelegate.swift`:

```swift
{% if include.platform == 'iOS' %}#import Appboy_iOS_SDK{% else %}#import AppboyTVOSKit{% endif %}
```

Pour plus d'informations sur l'utilisation du code Objective-C dans les projets Swift, consultez la \[Documentation des développeurs d'Apple\]\[apple_initial_setup_19\].

Dans `AppDelegate.swift`, ajoutez un snippet suivant à votre application `(application : UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`:

```swift
Appboy.start(withApiKey: "VOTRE-API-KEY", dans:application, withLaunchOptions:launchOptions)
```
{% endtab %}
{% endtabs %}

#### Usage
{% raw %}
Enfermer __onglets__ dans un `{% tabs %}` et `{% endtabs %}` Fermer un onglet ____ avec le code Liquide et le nom de l'onglet `{% tab [Nom de l'onglet] %}` et `{% endtab %}`
{% endraw %}

{% alert important %}
 Le nombre d'onglets sur la page devrait être cohérent, sinon le contenu des onglets pourrait être masqué. Par exemple si un jeu d'onglets a `C++`,`C-Sharp` et `JS`, et un autre ensemble d'onglets a `C-Sharp` et `JS`, puis lorsque quelqu'un clique sur `C++`, l'autre section ne montrera rien. Voir ci-dessous l'option des onglets locaux pour une solution de contournement.
{% endalert %}

{% raw %}
```liquid
{% tabs %}
{% tab objective-c %}
Contenu de objective-c
{% endtab %}
{% tab swift %}
Contenu rapide
{% endtab %}
{% endtabs %}
```
{% endraw %}

#### Onglets locaux
Pour les onglets autonomes, c'est-à-dire les onglets qui ne changent que le contenu de l'onglet de la section spécifique, puis utilisez le paramètre local dans le bloc des onglets parent.

{% raw %}
```liquid
{% tabs local %}
...
{% endtabs %}
```
{% endraw %}

#### Sous-onglets
Pour les onglets dans les onglets, `sous-onglets` et `sous-onglet` peuvent être utilisés. Le paramètre par défaut est `local`. Pour les `sous-onglets globaux`, utilisez l'option `globale` : {% raw %}`{% subtabs global %}`{% endraw %}

{% tabs local %}
{% tab Tab 1 %}
tab content 1
{% subtabs %}
{% subtab Subtab 1a %}
Subtab 1a content
{% endsubtab %}
{% subtab Subtab 2a %}
Subtab 2a content
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Tab 2 %}
tab content 2
{% subtabs %}
{% subtab Subtab 1b %}
Subtab 1a content
{% endsubtab %}
{% subtab Subtab 2b %}
Subtab 2a content
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

##### Markdown
{% raw %}
```
{% tabs %}
{% tab Tab 1 %}
{% subtabs %}
{% subtab Subtab 1 %}
Subtab 1 content
{% endsubtab %}
{% subtab Subtab 2 %}
Subtab 2 content
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}
```
{% endraw %}
[1]: {% image_buster /assets/img_archive/code_snippet.png %}
