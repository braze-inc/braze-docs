---
nav_title: Test de page de style
page_order: 2
noindex: true
---

# Test de page de style

## Test d’en-tête

{% tabs %}
{% tab Styling %}

# Bannière H1
Texte H1

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

## Bannière H2
Texte H2

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

### Bannière H3
Texte H3

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

#### Bannière H4
Texte H4

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

##### Bannière H5
Texte H5

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

###### Bannière H6
Texte H6

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

{% endtab %}
{% tab Markdown %}

```
# H1 Banner

## H2 Banner

### H3 Banner

#### H4 Banner

##### H5 Banner

###### H6 Banner
```
{% endtab %}
{% endtabs %}

## Ancrage d’en-tête personnalisé

Pour ajouter un ancrage à un en-tête, ajoutez le code suivant à la fin de la ligne sur laquelle se trouve l’en-tête. Remplacez `anchor-text` par l’ancrage pour cet en-tête. Utilisez des lettres en minuscule et séparez les mots par des traits d’union.

```
# Heading Text {#anchor-text}
```

Vous pouvez créer un lien vers les en-têtes avec des ancrages personnalisés en créant un lien standard avec un croisillon `#` suivi de l’ancrage personnalisé.

{% raw %}
```
Here is my [link](#anchor-text)
```
{% endraw %}

## Test de police

{% tabs %}
{% tab Styling %}

Texte normal

*Accentuer le texte*

**Gras**

_**Mise en gras**_

~~Barré~~

{% endtab %}
{% tab Markdown %}
```
Normal Text

*Emphasize Text*

**Bold**

_**Bold Emphasize**_

~~Strikethrough~~
```
{% endtab %}
{% endtabs %}

## Citation de test

{% tabs %}
{% tab Styling %}
> Texte cité

#### Citation alignée avec le texte
Lorem ipsum dolor ``sit amet, consectetur adipiscing elit``. Sed nec tortor at lectus tempus tempor.

#### Partie de citation
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

## Tableau de test

{% tabs %}
{% tab Styling %}
Instance    | URL du tableau de bord   | Endpoint REST
----------- |---------------- | --------------------
US-01 | `https://dashboard.braze.com` ou<br> `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com`
US-02 | `https://dashboard-02.braze.com` | `https://rest.iad-02.braze.com`
US-03 | `https://dashboard-03.braze.com` | `https://rest.iad-03.braze.com`
US-04 | `https://dashboard-04.braze.com` | `https://rest.iad-04.braze.com`
US-06 | `https://dashboard-06.braze.com` | `https://rest.iad-06.braze.com`
EU-01 | `https://dashboard.braze.eu` ou<br> `https://dashboard-01.braze.eu` | `https://rest.fra-01.braze.eu`
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
{% endtab %}
{% tab Markdown %}
```
Instance    | Dashboard URL   | REST Endpoint
----------- |---------------- | --------------------
US-01 | `https://dashboard.braze.com` or<br> `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com`
US-02 | `https://dashboard-02.braze.com` | `https://rest.iad-02.braze.com`
US-03 | `https://dashboard-03.braze.com` | `https://rest.iad-03.braze.com`
US-04 | `https://dashboard-04.braze.com` | `https://rest.iad-04.braze.com`
US-06 | `https://dashboard-06.braze.com` | `https://rest.iad-06.braze.com`
EU-01 | `https://dashboard.braze.eu` or<br> `https://dashboard-01.braze.eu` | `https://rest.fra-01.braze.eu`
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
```
{% endtab %}
{% endtabs %}

#### Réinitialiser le word-break du tableau par colonne
Pour les colonnes de tableaux dont le word-break doit être rétabli au style par défaut, servez-vous des options Markdown pour ajouter une classe dans le tableau en utilisant `.reset-td-br-1`, `.reset-td-br-2`, `.reset-td-br-3` et `.reset-td-br-4`, où le `#` correspond aux 4 premières colonnes.

#### Utilisation
```
| Event Name                           | Feed Type              | Description                                                                               | Custom Attributes
| ------------------------------------ | ---------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| UNBROKENWORDTHATISVERYLONGUNBROKENWORDTHATISVERYLONG | Unbound Feed           | An email was successfully delivered to a User's mail server.                              | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`                      |
| `UNBROKENHIGHLIGHTTHATISVERYLONGUNBROKENHIGHLIGHTTHATISVERYLONG`                       | Unbound Feed           | User opened an email.                                                                     | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`                      |
| In-App Message Impression            | Platform-specific Feed | User viewed an In-App Message.                                                            | `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

```
{% tabs local %}
{% tab Before %}

| Nom de l’événement                           | Type de fil d’actualité              | Description                                                                               | Attributs personnalisés
| ------------------------------------ | ---------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| TRÈSLONGMOTSANSESPACETRÈSLONGMOTSANSESPACE | Flux indépendant           | Un e-mail a été envoyé avec succès au serveur de messagerie d’un utilisateur.                              | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`                      |
| `UNBROKENHIGHLIGHTTHATISVERYLONGUNBROKENHIGHLIGHTTHATISVERYLONG`                         | Flux indépendant           | L’utilisateur a ouvert un e-mail.                                                                     | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`                      |
| In-App-Message-Impression            | Fil spécifique à la plateforme | L’utilisateur a consulté un message in-app.                                                            | `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`             |

{% endtab %}
{% tab After %}

| Nom de l’événement                           | Type de fil d’actualité              | Description                                                                               | Attributs personnalisés
| ------------------------------------ | ---------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| TRÈSLONGMOTSANSESPACETRÈSLONGMOTSANSESPACE | Flux indépendant           | Un e-mail a été envoyé avec succès au serveur de messagerie d’un utilisateur.                              | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`                      |
| `UNBROKENHIGHLIGHTTHATISVERYLONGUNBROKENHIGHLIGHTTHATISVERYLONG`                       | Flux indépendant           | L’utilisateur a ouvert un e-mail.                                                                     | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`                      |
| In-App-Message-Impression            | Fil spécifique à la plateforme | L’utilisateur a consulté un message in-app.                                                            | `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}
{% endtab %}
{% endtabs %}

## Test de lien
{% tabs %}
{% tab Styling %}
Lien : [Braze.com](https://www.braze.com){: height="36px" width="36px"}
{% endtab %}
{% tab Markdown %}
```
[Braze.com](https://www.braze.com)
```
{% endtab %}
{% endtabs %}

## Test d’image
{% tabs %}
{% tab Styling %}
Image : ![Logo]({{site.baseurl}}/assets/img/braze-logo-mark.png){: style="max-width:30%;"}

#### Test d’image en lien

Image en lien : [![Braze]({{site.baseurl}}/assets/img/braze-logo-mark.png){: style="max-width:30%;"}](https://www.braze.com)

#### Style d’image

![Texte]({% image_buster /assets/img/logo-braze-fa.svg %}){: style="max-width:30%; color: green" }

#### Ancrage d’images

![Texte]({% image_buster /assets/img/logo-braze-fa.svg %}){: style="float:right;max-width:30%; color: green" }
<br><br><br><br><br>
{% endtab %}
{% tab Markdown %}

```
![Logo]({{site.baseurl}}/assets/img/braze-logo-mark.png)

[![Braze]({{site.baseurl}}/assets/img/braze-logo-mark.png)](https://www.braze.com)

![Text]({% image_buster /assets/img/logo-braze-fa.svg %}){: style="max-width:30%; color: green" }

![Text]({% image_buster /assets/img/logo-braze-fa.svg %}){: style="float:right;max-width:30%;" }
```
{% endtab %}
{% endtabs %}

## Test de galerie
{% tabs %}
{% tab Styling %}
{% gallery %}
{{site.baseurl}}/assets/img_archive/EBTH_Email.png?bf892368baf287cba5ab9a6e3b09431d  <br> Ceci est un [lien](https://www.braze.com).
{{site.baseurl}}/assets/img_archive/iHeartRadio_Email.png?ecd2c8fe148939b7de957fe85cd6317e  <br> Ceci est un autre `comment`.
{{site.baseurl}}/assets/img_archive/Saucey_Email.png?b9768937a1cc12d4c08e55a52e700d68  <br> Ceci est encore un autre **commentaire**.
{{site.baseurl}}/assets/img/schellman_iso27001_seal_grey_CMYK_300dpi_jpg.png?1b1fb9dbb80b0332c62512dcf9c83258 <br> **TITRE DE L’IMAGE** <br> Ceci est un test pour vérifier le saut de ligne.
{{site.baseurl}}/assets/img/SOC2.png?6338040be8e98c4c9abe1f35b3e43e3a  <br> Ceci est un commentaire standard.
{% endgallery %}
{% endtab %}
{% tab Markdown %}
{% raw %}
```
{% gallery %}
{{site.baseurl}}/assets/img_archive/EBTH_Email.png?bf892368baf287cba5ab9a6e3b09431d  <br> This is a [link](https://www.braze.com).
{{site.baseurl}}/assets/img_archive/iHeartRadio_Email.png?ecd2c8fe148939b7de957fe85cd6317e  <br> This is another `comment`.
{{site.baseurl}}/assets/img_archive/Saucey_Email.png?b9768937a1cc12d4c08e55a52e700d68  <br> This is yet another **comment**.
{{site.baseurl}}/assets/img/schellman_iso27001_seal_grey_CMYK_300dpi_jpg.png?1b1fb9dbb80b0332c62512dcf9c83258 <br> **IMAGE TITLE** <br> This is a test to see if it will line break.
{{site.baseurl}}/assets/img/SOC2.png?6338040be8e98c4c9abe1f35b3e43e3a  <br> This is a regular comment.
{% endgallery %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Test d’image interactive
{% tabs %}
{% tab Styling %}
<div class="iactiveImg" data-ii="6967"></div><script src="https://interactive-img.com/js/include.js"></script>
{% endtab %}
{% tab Markdown %}
```
<div class="iactiveImg" data-ii="6967"></div><script src="https://interactive-img.com/js/include.js"></script>
```
{% endtab %}
{% endtabs %}
<!--- Leaving formatting here just in case it's important...
<div style="position: relative; padding-bottom: 83%; padding-top: 0; height: 0;"><iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border-width:0px; max-width:100%; overflow-y:auto;" width="100%" height="100%" src="https://interactive-img.com/view?id=6967&iframe=true"></iframe></div>
-->

## Test d’extrait de code

{% tabs %}
{% tab Styling %}
#### Objectif C du test de code
```objc
- (void)submitFeedback:(ABKFeedback * )feedback
 withCompletionHandler:(nullable void (^)(ABKFeedbackSentResult feedbackSentResult))completionHandler;
```

#### Test de code Swift
```swift
Appboy.sharedInstance()?.submitFeedback(feedback) { (feedbackSentResult) in
      print("Feedback sent: (feedbackSentResult)")
    }
```

#### Test de code Java
```java
@Override
public void onResume() {
  super.onResume();
  // Registers the BrazeInAppMessageManager for the current Activity. This Activity will now listen for
  // in-app messages from Braze.
  BrazeInAppMessageManager.getInstance().registerInAppMessageManager(activity);
}
```

#### Test de code JSON
```json
{
   "attributes" : "Attributes" ,
   "events" : ["Array", "Of", "Object"],
   "purchases" : ["Array" ,"Of" ,"Purchase" ,"Object"]
}
```

#### Test de code JavaScript
```javascript
braze.subscribeToFeedUpdates(function(feed) {
  var cards = feed.cards;
  braze.showFeed(undefined, cards);
});
braze.requestFeedRefresh();
```

#### Test de Pygments
```python
#!/usr/bin/python3

from engine import RunForrestRun

"""Test code for syntax highlighting!"""

class Foo:
	def __init__(self, var):
		self.var = var
		self.run()

	def run(self):
		RunForrestRun()  # run along!

```
{% endtab %}
{% tab Markdown %}
![Exemple pour Markdown]({% image_buster /assets/img_archive/code_snippet.png %})
{% endtab %}
{% endtabs %}

## Test d’alerte

{% tabs %}
{% tab Styling %}

{% alert tip %}Ceci est un conseil{% endalert %}

{% alert note %}Ceci est une note{% endalert %}

{% alert important %}Ceci est une alerte importante{% endalert %}

{% alert warning %}Ceci est un avertissement{% endalert %}

{% alert update %}Ceci est une mise à jour{% endalert %}

{% endtab %}
{% tab Markdown %}
{% raw %}
```
{% alert tip %}
This is a tip
{% endalert %}

{% alert note %}
This is a note
{% endalert %}

{% alert important %}
This is a important alert
{% endalert %}

{% alert warning %}
This is a warning
{% endalert %}

{% alert update %}
This is a update
{% endalert %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Test d’intégration vidéo
{% tabs %}
{% tab Styling %}
#### Vidéo/vidéo YouTube intégrée
Intégration YouTube par défaut.
{% multi_lang_include video.html id="XY5vFY" source="youtube" %}

#### Alignement à droite de la vidéo intégrée
{% multi_lang_include video.html id="XYuXoKIvFY" align="right" source="youtube" %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

#### Alignement à gauche de la vidéo intégrée
{% multi_lang_include video.html id="XY5uXvFY" align="left" source="youtube" %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.
<br /><br />

#### Exemple pour Loom
* utiliser `source="loom"`
{% multi_lang_include video.html id="c1d3199463c448e8918f046265b54eb2" source="loom" %}

{% endtab %}
{% tab Markdown %}

{% raw %}
```html
{% multi_lang_include video.html id="[youte_id]" source="youtube" %}
```
{% endraw  %}

Pour aligner à droite ou à gauche et limiter la largeur maximale à 50 %, utilisez le paramètre `align` = `left` ou `right` :
{% raw  %}
```html
{% multi_lang_include video.html id="[ytube_id]" align="left" source="youtube" %}

{% multi_lang_include video.html id="[youe_id]" align="right" source="youtube" %}
```
{% endraw  %}

Exemple pour Loom :
{% raw %}
```html
{% multi_lang_include video.html id="[lid]" source="loom" %}
```
{% endraw  %}

{% endtab %}
{% endtabs %}

#### Mise en page vidéo avec positionnement de l’état pour une résolution plus élevée
Pour utiliser la mise en page vidéo présentée qui place une vidéo statique sur le côté gauche 
pour un affichage à haute résolution, ajoutez un video_id et un video_type, par exemple `youtube`, à 
l’en-tête yaml de la page.
video_source par défaut sur `youtube`

{% raw  %}
```yaml
layout: dev_guide_video
video_id: [video_id]
video_source: youtube
```
{% endraw  %}

## Test de liste
{% tabs %}
{% tab Styling %}
#### Liste à puce
* Liste 1
  * Sous-liste 1
* Liste 2
  * Sous-liste 2a
    * Sous sous-liste 2
* Liste 3

#### Numérotée
1. Liste 1
  * Sous-liste 1
2. Liste 2
3. Liste 3
  * Sous-liste 3a
  * Sous-liste 3b
    * Sous sous-liste 3
4. Liste 4
    1. Sous-liste 4a
        1. Sous sous-liste 4
    2. Sous-liste 4b
        1. sous sous-liste 4

{% endtab %}
{% tab Markdown %}
```
#### Bullet
* List 1
  * Sub List 1
* List 2
  * Sub List 2a
    * Sub Sub List 2
* List 3

#### Numbered
1. List 1
  * Sub List 1
2. List 2
3. List 3
  * Sub List 3a
  * Sub List 3b
    * Sub Sub List 3
4. List 4
    1. Sub list 4a
        1. Sub Sub List 4
    2. Sub list 4b
        1. sub sub list 4
```
{% endtab %}
{% endtabs %}

## Test de contenu réductible
{% tabs %}
{% tab Styling %}
{% details Cliquez pour dérouler %}
#### Regardez, un bloc de code caché !

```python
print("hello world!")
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

## Test d’onglet

#### Onglets personnalisés

{% tabs local %}
{% tab OBJECTIVE-C %}

Ajoutez la ligne de code suivante à votre fichier `AppDelegate.m` :

```objc
{% if include.platform == 'iOS' %}#import "Appboy-iOS-SDK/AppboyKit.h"{% else %}#import <AppboyTVOSKit/AppboyKit.h>{% endif %}
```

Dans votre fichier `AppDelegate.m`, ajoutez l’extrait de code suivant au sein de votre méthode `application:didFinishLaunchingWithOptions` :

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
         inApplication:application
     withLaunchOptions:launchOptions];
```

{% endtab %}
{% tab swift %}

Si vous intégrez le SDK Braze avec des CocoaPods, Carthage ou via une intégration manuelle dynamique, ajoutez la ligne de code suivante à votre fichier `AppDelegate.swift` :

```swift
{% if include.platform == 'iOS' %}#import Appboy_iOS_SDK{% else %}#import AppboyTVOSKit{% endif %}
```

Pour plus d’informations sur l’utilisation du code Objective-C dans les projets Swift, consultez la [Documentation des développeurs Apple][apple_initial_setup_19].

Dans `AppDelegate.swift`, ajoutez l’extrait de code suivant dans votre `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` :

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions)
```
{% endtab %}
{% endtabs %}

#### Utilisation
{% raw %}
Encadrer les **onglets** dans un `{% tabs %}` et `{% endtabs %}`
Encadrer chaque **onglet** avec le code Liquid et le nom de l’onglet `{% tab [Tab name] %}` et `{% endtab %}`
{% endraw %}

{% alert important %}
 Remarque : le nombre d’onglets sur la page doit être cohérent, faute de quoi le contenu de certains onglets risque d’être masqué.
 Par exemple, si un ensemble d’onglets contient `C++`,`C-Sharp` et `JS`, et un autre ensemble d’onglets contient `C-Sharp` et `JS`,
alors, lorsque quelqu’un clique sur `C++`, l’autre section n’affichera rien. Consultez l’option des onglets locaux pour contourner ce problème.
{% endalert %}

{% raw %}
```liquid
{% tabs %}
{% tab objective-c %}
Content of objective-c
{% endtab %}
{% tab swift %}
Content of swift
{% endtab %}
{% endtabs %}
```
{% endraw %}

#### Onglets locaux
Pour les onglets autonomes, c’est-à-dire les onglets qui modifient uniquement le contenu des onglets pour une section donnée, utilisez le paramètre local dans le bloc d’onglets parent.

{% raw %}
```liquid
{% tabs local %}
...
{% endtabs %}
```
{% endraw %}

#### Sous-onglets
`subtabs` et `subtab` peuvent être utilisés pour les onglets à l’intérieur d’autres onglets. Le paramètre par défaut est `local`.
Pour les `subtabs` globaux, utilisez l’option `global` :  {% raw %}`{% subtabs global %}`{% endraw %}

{% tabs local %}
{% tab Tab 1 %}
contenu de l’onglet 1
{% subtabs %}
{% subtab Subtab 1a %}
Contenu du sous-onglet 1a
{% endsubtab %}
{% subtab Subtab 2a %}
Contenu du sous-onglet 2a
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Tab 2 %}
contenu de l’onglet 2
{% subtabs %}
{% subtab Subtab 1b %}
Contenu du sous-onglet 1a
{% endsubtab %}
{% subtab Subtab 2b %}
Contenu du sous-onglet 2a
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
