---
nav_title: Implémentation avancée (facultatif)
article_title: Guide d’implémentation de la carte de contenu pour Android (facultatif) 
platform: Android
page_order: 7
description: "Ce guide d’implémentation avancé couvre les considérations du code de carte de contenu Android, trois cas d’utilisation construits par notre équipe, les extraits de code l’accompagnant et les directives sur l’enregistrement des impressions, des clics et des rejets."
channel:
  - cartes de contenu

---
<br>
{% alert important %}
Vous recherchez le guide d’intégration de base du développeur de carte de contenu ? Vous le trouverez [ici]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/integration/).
{% endalert %}

# Guide d’implémentation de carte de contenu

> Ce guide d’implémentation avancée optionnel couvre les considérations du code de carte de contenu, trois cas d’utilisation personnalisés construits par notre équipe, les extraits de code l’accompagnant et les directives sur la journalisation des impressions, des clics et des rejets. Consultez notre référentiel de démonstration Braze [ici](https://github.com/braze-inc/braze-growth-shares-android-demo-app) ! Notez que ce guide d’implémentation est centré autour d’une implémentation Kotlin, mais les extraits de code Java sont fournis aux personnes intéressées.

## Considérations du code

### Importer des relevés et des fichiers d’aide

Lors de la création de cartes de contenu, vous devez exposer le SDK Braze via un gestionnaire singleton unique. Ce modèle protège le code de votre application des détails de l’implémentation de Braze derrière une abstraction partagée qui est logique pour votre cas d’utilisation. Il facilite également la traçabilité, le débogage et les changements de code. Un exemple d’implémentation de gestionnaire est disponible [ici](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt).

### Les cartes de contenu comme objets personnalisés

Vos propres objets personnalisés déjà utilisés dans votre application peuvent être étendus pour transporter des données de carte de contenu, entraînant ainsi l’abstraction de la source des données vers un format déjà compris par le code de votre application. Les abstractions de sources de données permettent de travailler de manière flexible avec des données secondaires différentes de manière interchangeable et de concert. Dans cet exemple, nous avons défini la classe de base abstraite `ContentCardable` pour qu’elle représente à la fois nos données existantes (alimentées, dans cet exemple, à partir d’un fichier JSON local) et les nouvelles données alimentées par le SDK Braze. La classe de base expose également les données brutes de la carte de contenu pour les consommateurs qui ont besoin d’accéder à l’implémentation originale `Card`.

Lors de l’initialisation des instances `ContentCardable` du SDK Braze, nous utilisons le `class_type` supplémentaire pour mapper la carte de contenu à une sous-classe concrète. Nous utilisons ensuite les paires clé-valeur supplémentaires définies dans le tableau de bord de Braze pour renseigner les champs nécessaires.

Une fois que vous avez une compréhension approfondie de ces considérations du code, consultez nos [cas d’usage](#sample-use-cases) pour commencer à implémenter vos propres objets personnalisés.

{% tabs local %}
{% tab No Card Dependencies %}
{% subtabs global %}
{% subtab Kotlin %}
**Pas de dépendances de `Card`**<br>
`ContentCardData` représente les valeurs analysées et communes d’un `Card`.

```kotlin
abstract class ContentCardable (){

    var cardData: ContentCardData? = null

    constructor(data:Map<String, Any>):this(){
        cardData = ContentCardData(data[idString] as String,
            ContentCardClass.valueFrom(data[classType] as String),
            data[created] as Long,
            data[dismissable] as Boolean)
    }

    val isContentCard: Boolean
        get() = cardData != null

    fun logContentCardClicked() {
        BrazeManager.getInstance().logContentCardClicked(cardData?.contentCardId)
    }

    fun logContentCardDismissed() {
        BrazeManager.getInstance().logContentCardDismissed(cardData?.contentCardId)
    }

    fun logContentCardImpression() {
        BrazeManager.getInstance().logContentCardImpression(cardData?.contentCardId)
    }
}

data class ContentCardData (var contentCardId: String,
                            var contentCardClassType: ContentCardClass,
                            var createdAt: Long,
                            var dismissable: Boolean)
```
{% endsubtab %}
{% subtab Java %}
**Pas de dépendances de `Card`**<br>
`ContentCardData` représente les valeurs analysées et communes d’un `Card`.

```java
public abstract class ContentCardable{

  private ContentCardData cardData = null;

  public ContentCardable(Map<String, Object> data){
      cardData = new ContentCardData()
      cardData.contentCardId = (String) data.get(idString);
      cardData.contentCardClassType = contentCardClassType.valueOf((String)data.get(classType));
      cardData.createdAt = Long.parseLong((String)data.get(createdAt));
      cardData.dismissable = Boolean.parseBoolean((String)data.get(dismissable));
  }

  public ContentCardable(){

  }

  public boolean isContentCard(){
    return cardData != null;
  }

  public void logContentCardClicked() {
    if (isContentCard()){
      BrazeManager.getInstance().logContentCardClicked(cardData.contentCardId)
    }
  }

  public void logContentCardDismissed() {
    if(isContentCard()){
      BrazeManager.getInstance().logContentCardDismissed(cardData.contentCardId)
    }
  }

  public void logContentCardImpression() {
    if(isContentCard()){
      BrazeManager.getInstance().logContentCardImpression(cardData.contentCardId)
    }
  }
}

public class ContentCardData{
  public String contentCardId;
  public ContentCardClass contentCardClassType;
  public long createdAt;
  public boolean dismissable;
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Custom Objects %}
{% subtabs global %}
{% subtab Kotlin %}
**Initialiseur d’objet personnalisé**<br>
Les métadonnées d’un `Card` sont utilisées pour renseigner les variables de votre sous-classe concrète. Selon la sous-classe, vous devrez peut-être extraire différentes valeurs pendant l’initialisation. Les paires clé-valeur définies dans le tableau de bord de Braze sont représentées dans le dictionnaire « compléments ».

```kotlin
class Tile: ContentCardable {
    constructor(metadata:Map<String, Any>):super(metadata){
        val extras = metadata[extras] as? Map<String, Any>
        title = extras?.get(Keys.title) as? String
        image = extras?.get(Keys.image) as? String
        detail = metadata[ContentCardable.detail] as? String
        tags = (metadata[ContentCardable.tags] as? String)?.split(",")
        val priceString = extras?.get(Keys.price) as? String
        if (priceString?.isNotEmpty() == true){
            price = priceString.toDouble()
        }
        id = floor(Math.random()*1000).toInt()
    }
  }
```
{% endsubtab %}
{% subtab Java %}
**Initialiseur d’objet personnalisé**<br>
Les métadonnées d’un `Card` sont utilisées pour renseigner les variables de votre sous-classe concrète. Selon la sous-classe, vous devrez peut-être extraire différentes valeurs pendant l’initialisation. Les paires clé-valeur définies dans le tableau de bord de Braze sont représentées dans le dictionnaire « compléments ».

```java
public class Tile extends ContentCardable {

    public Tile(Map<String, Object> metadata){
        super(metadata);
        this.detail = (String) metadata.get(ContentCardable.detail);
        this.tags = ((String)metadata.get(ContentCardable.tags)).split(",");
        if (metadata.containsKey(Keys.extras)){
            Map<String, Object> extras = metadata.get(Keys.extras);
            this.title = (String)extras.get(Keys.title);
            this.price = Double.parseDouble((String)extras.get(Keys.price));
            this.image = (String)extras.get(Keys.image);

        }
    }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Identifying Types %}
{% subtabs global %}
{% subtab Kotlin %}
**Identifier des types**<br>
L’enum `ContentCardClass` représente la valeur `class_type` du tableau de bord de Braze et fournit une méthode d’initialisation de l’enum des chaînes de caractères fournies par le SDK.

```kotlin
enum class ContentCardClass{
    AD,
    COUPON,
    NONE,
    ITEM_TILE,
    ITEM_GROUP,
    MESSAGE_FULL_PAGE,
    MESSAGE_WEB_VIEW;

    companion object {
        // Il faut synchroniser cette valeur avec la valeur`class_type` configurée dans votre
        // tableau de bord de Braze ou son type sera configuré sur `ContentCardClassType.none.`
        fun valueFrom(str: String?): ContentCardClass {
            return when(str?.toLowerCase()){
                "coupon_code" -> COUPON
                "home_tile" -> ITEM_TILE
                "group" -> ITEM_GROUP
                "message_full_page" -> MESSAGE_FULL_PAGE
                "message_webview" -> MESSAGE_WEB_VIEW
                "ad_banner" -> AD
                else -> NONE
            }
        }
    }
}
```
{% endsubtab %}
{% subtab Java %}
**Identifier des types**<br>
L’enum `ContentCardClass` représente la valeur `class_type` du tableau de bord de Braze et fournit une méthode d’initialisation de l’enum des chaînes de caractères fournies par le SDK.

```java
enum ContentCardClass {
    AD,
    COUPON,
    NONE,
    ITEM_TILE,
    ITEM_GROUP,
    MESSAGE_FULL_PAGE,
    MESSAGE_WEB_VIEW

    public static valueFrom(String val){
        switch(val.toLowerCase()){
            case "coupon_code":{
                return COUPON;
            }
            case "home_tile":{
                return ITEM_TILE;
            }
            case "group":{
                return ITEM_GROUP;
            }
            case "message_full_page":{
                return MESSAGE_FULL_PAGE;
            }
            case "message_webview":{
                return MESSAGE_WEB_VIEW;
            }
            case "ad_banner":{
                return AD;
            }
            default:{
                return NONE;
            }
        }
    }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Exemples de cas d’usage

Trois exemples de cas d’usage client sont fournis. Chaque cas d’usage offre une explication détaillée, des extraits de code pertinents et un aperçu de la façon dont les variables de la carte de contenu peuvent être rassemblées et utilisées dans le tableau de bord de Braze :
- [Cartes de contenu en tant que contenu supplémentaire](#content-cards-as-supplemental-content)
- [Cartes de contenu dans un centre de messages](#content-cards-in-a-message-center)
- [Cartes de contenu interactives](#interactive-content-cards)

### Cartes de contenu en tant que contenu supplémentaire

![][1]{: style="float:right;max-width:25%;margin-left:15px;border:0;"}

Vous pouvez mélanger de façon transparente les cartes de contenu dans un flux existant, ce qui permet de charger simultanément les données de plusieurs flux. Cela crée une expérience cohésive et harmonieuse avec les cartes de contenu Braze et le contenu du flux existant.

L’exemple à droite montre un `ListView` avec une liste hybride d’éléments remplis via les données locales et les cartes de contenu alimentées par Braze. Avec cette méthode, les cartes de contenu ne peuvent pas être différenciées au regard du contenu existant.

#### Configuration du tableau de bord

Cette carte de contenu est livrée par une campagne déclenchée par API avec des paires clé-valeurs déclenchées par API. Cette option est idéale pour les campagnes où les valeurs de la carte dépendent des facteurs externes pour déterminer le contenu à afficher à l’utilisateur. Notez que `class_type` doit être connu au moment de la configuration.

![Les paires clé-valeur pour le cas d’usage des cartes de contenu supplémentaires. Dans cet exemple, différents aspects de la carte comme « tile_id », « tile_deeplink » et « tile_title » sont définis à l’aide de Liquid.][2]{: style="max-width:60%;"}

##### Prêt à enregistrer l’analytique ?
Consultez la [section suivante](#logging-impressions-clicks-and-dismissals) pour mieux comprendre à quoi le flux de données devrait ressembler.

### Cartes de contenu dans un centre de messages
<br>
Les cartes de contenu peuvent être utilisées dans un format de centre de messages dans lequel chaque message est sa propre carte. Chaque message du centre de messages est rempli via une charge utile de carte de contenu et chaque carte contient des paires clé-valeur supplémentaires qui alimentent l’interface ou expérience utilisateur lors du clic. Dans l’exemple suivant, un message vous dirige vers un affichage personnalisé arbitraire, tandis qu’un autre ouvre une vue Web qui affiche du HTML personnalisé.

![][3]{: style="border:0;"}{: style="max-width:80%;border:0"}

#### Configuration du tableau de bord

Pour les types de messages suivants, la paire clé-valeur `class_type` doit être ajoutée à la configuration de votre tableau de bord. Les valeurs assignées ici sont arbitraires, mais doivent pouvoir être distinguées entre types de classe. Ces paires clé-valeur sont les identifiants clés que l’application examine lorsqu’elle décide où aller lorsque l’utilisateur clique sur un message abrégé de la boîte de réception. 

{% tabs local %}
{% tab Arbitrary custom view message (full page) %}

Les paires clé-valeur pour ce cas d’usage comprennent :

- `message_header` défini en tant que `Full Page`
- `class_type` défini en tant que `message_full_page`

![]({% image_buster /assets/img/cc_implementation/full_page.png %}){: style="max-width:60%;"}

{% endtab %}
{% tab Webview message (HTML) %}

Les paires clé-valeur pour ce cas d’usage comprennent :

- `message_header` défini en tant que `HTML`
- `class_type` défini en tant que `message_webview`
- `message_title`

Ce message recherche également une paire clé-valeur HTML, mais si vous travaillez avec un domaine Web, une paire clé-valeur URL est également valide.

![]({% image_buster /assets/img/cc_implementation/html_webview.png %}){: style="max-width:60%;"}

{% endtab %}
{% endtabs %}

#### Explication supplémentaire

La logique du centre de messages est dirigée par le `class_type` qui est fourni par les paires clé-valeur de Braze. En utilisant le `createContentCardable` de notre exemple, vous pouvez filtrer et identifier ces types de classe.

{% tabs %}
{% tab Kotlin %}
**Utiliser `class_type` pour le comportement du clic**<br>
Lorsque nous augmentons les données de la carte de contenu dans nos classes personnalisées, nous utilisons la propriété `ContentCardClass` des données pour déterminer quelle sous-classe concrète doit être utilisée pour
stocker les données.

```kotlin
 private fun createContentCardable(metadata: Map<String, Any>, type: ContentCardClass?): ContentCardable?{
        return when(type){
            ContentCardClass.AD -> Ad(metadata)
            ContentCardClass.MESSAGE_WEB_VIEW -> WebViewMessage(metadata)
            ContentCardClass.MESSAGE_FULL_PAGE -> FullPageMessage(metadata)
            ContentCardClass.ITEM_GROUP -> Group(metadata)
            ContentCardClass.ITEM_TILE -> Tile(metadata)
            ContentCardClass.COUPON -> Coupon(metadata)
            else -> null
        }
    }
```

Ensuite, lors de la manipulation de l’interaction utilisateur avec la liste des messages, nous pouvons utiliser le type de message pour déterminer la vue à afficher à l’utilisateur.

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        //...
        listView.onItemClickListener = AdapterView.OnItemClickListener { parent, view, position, id ->
           when (val card = dataProvider[position]){
                is WebViewMessage -> {
                    val intent = Intent(this, WebViewActivity::class.java)
                    val bundle = Bundle()
                    bundle.putString(WebViewActivity.INTENT_PAYLOAD, card.contentString)
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
                is FullPageMessage -> {
                    val intent = Intent(this, FullPageContentCard::class.java)
                    val bundle = Bundle()
                    bundle.putString(FullPageContentCard.CONTENT_CARD_IMAGE, card.icon)
                    bundle.putString(FullPageContentCard.CONTENT_CARD_TITLE, card.messageTitle)
                    bundle.putString(FullPageContentCard.CONTENT_CARD_DESCRIPTION, card.cardDescription)
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
            }

        }
    }
```
{% endtab %}
{% tab Java %}
**Utiliser `class_type` pour le comportement du clic**<br>
Lorsque nous augmentons les données de la carte de contenu dans nos classes personnalisées, nous utilisons la propriété `ContentCardClass` des données pour déterminer quelle sous-classe concrète doit être utilisée pour stocker les données.

```java
private ContentCardable createContentCardable(Map<String, ?> metadata,  ContentCardClass type){
    switch(type){
        case ContentCardClass.AD:{
            return new Ad(metadata);
        }
        case ContentCardClass.MESSAGE_WEB_VIEW:{
            return new WebViewMessage(metadata);
        }
        case ContentCardClass.MESSAGE_FULL_PAGE:{
            return new FullPageMessage(metadata);
        }
        case ContentCardClass.ITEM_GROUP:{
            return new Group(metadata);
        }
        case ContentCardClass.ITEM_TILE:{
            return new Tile(metadata);
        }
        case ContentCardClass.COUPON:{
            return new Coupon(metadata);
        }
        default:{
            return null;
        }
    }
}

```

Ensuite, lors de la manipulation de l’interaction utilisateur avec la liste des messages, nous pouvons utiliser le type de message pour déterminer la vue à afficher à l’utilisateur.

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState)
        //...
        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id){
               ContentCardable card = dataProvider.get(position);
               if (card instanceof WebViewMessage){
                    Bundle intent = new Intent(this, WebViewActivity.class);
                    Bundle bundle = new Bundle();
                    bundle.putString(WebViewActivity.INTENT_PAYLOAD, card.getContentString());
                    intent.putExtras(bundle);
                    startActivity(intent);
                }
                else if (card instanceof FullPageMessage){
                    Intent intent = new Intent(this, FullPageContentCard.class);
                    Bundle bundle = Bundle();
                    bundle.putString(FullPageContentCard.CONTENT_CARD_IMAGE, card.getIcon());
                    bundle.putString(FullPageContentCard.CONTENT_CARD_TITLE, card.getMessageTitle());
                    bundle.putString(FullPageContentCard.CONTENT_CARD_DESCRIPTION, card.getCardDescription());
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
            }

        });
    }
```

{% endtab %}
{% endtabs %}

##### Prêt à enregistrer l’analytique ?
Consultez la [section suivante](#logging-impressions-clicks-and-dismissals) pour mieux comprendre à quoi le flux de données devrait ressembler.

![Une carte de contenu interactive affichant une promotion de 50 % apparaît dans le coin en bas à gauche de l’écran. Une fois cliquée, une promotion sera appliquée au panier.][6]{: style="float:right;max-width:45%;border:0;margin-left:15px;"} 

### Cartes de contenu interactives
<br>
Les cartes de contenu peuvent être utilisées pour créer des expériences dynamiques et interactives pour vos utilisateurs. Dans l’exemple à droite, une fenêtre contextuelle de carte de contenu apparaît au moment du paiement, fournissant aux utilisateurs des promotions de dernière minute. 

Des cartes bien placées comme ceci constituent un excellent moyen d’encourager les utilisateurs à entreprendre des actions spécifiques. 
<br><br><br>
#### Configuration du tableau de bord

La configuration du tableau de bord pour les cartes de contenu interactives est rapide et simple. Les paires clé-valeur pour ce cas d’usage comprennent un ensemble `discount_percentage` défini comme montant de remise souhaité et un ensemble `class_type` défini comme `coupon_code`. Ces paires clé-valeur sont la manière dont les cartes de contenu spécifiques à un type sont filtrées et affichées sur l’écran de paiement.

![][7]{: style="max-width:70%;"} 

##### Prêt à enregistrer l’analytique ?
Consultez la [section suivante](#logging-impressions-clicks-and-dismissals) pour mieux comprendre à quoi le flux de données devrait ressembler.

## Enregistrer les impressions, les clics et les rejets

Après avoir étendu vos objets personnalisés pour qu’ils fonctionnent en tant que cartes de contenu, vous pouvez enregistrer des métriques de valeur comme les impressions, les clics et les rejets, et ce, rapidement et simplement. Cela peut être fait en utilisant une classe de base `ContentCardable` qui fait référence et fournit des données au `BrazeManager`.

#### **Composants d’implémentation**<br><br>

{% tabs %}
{% tab Kotlin %}
**Les objets personnalisés appellent les méthodes d’enregistrement**<br>
Dans votre classe de base `ContentCardable`, vous pouvez appeler directement `BrazeManager`, le cas échéant. Dans cet exemple, la propriété `cardData` sera nonnull si l’objet provenait d’une carte de contenu. 

```kotlin
override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
        val tile = currentTiles[position]
        tile.logContentCardImpression()
        ...
    }
```

**Récupérer la carte de contenu de la `ContentCardId`**<br>
La classe de base `ContentCardable` gère la partie ardue de l’appel de `BrazeManager` et du transfert de l’identifiant unique à partir de la carte de contenu associée à l’objet personnalisé.

```kotlin
    fun logContentCardImpression() {
        cardData?.let { BrazeManager.getInstance().logContentCardImpression(it.contentCardId) }
    }
```

**Fonctions des appels de `Card`**<br>
Le [`BrazeManager`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt) peut faire référence aux dépendances du SDK Braze, telles que la liste du tableau d'objets de carte de contenu pour obtenir le `Card` pour appeler nos méthodes d’enregistrement.

```kotlin
    fun logContentCardClicked(idString: String?) {
        getContentCard(idString)?.logClick()
    }

    fun logContentCardImpression(idString: String?) {
        getContentCard(idString)?.logImpression()
    }

    private fun getContentCard(idString: String?): Card? {
        return cardList.find { it.id == idString }.takeIf { it != null }
    }
```
{% endtab %}
{% tab Java %}
**Les objets personnalisés appellent les méthodes d’enregistrement**<br>
Dans votre classe de base `ContentCardable`, vous pouvez appeler directement `BrazeManager`, le cas échéant. Souvenez-vous que, dans cet exemple, la propriété `cardData` sera nonnull si l’objet provenait d’une carte de contenu. 
```java
@Override
public View getView(int position, View convertView, ViewGroup parent) {
        Tile tile = currentTiles.get(position);
        tile.logContentCardImpression();
        ...
    }
```

**Récupérer la carte de contenu de la `ContentCardId`**<br>
La classe de base `ContentCardable` gère la partie ardue de l’appel de `BrazeManager` et du transfert de l’identifiant unique à partir de la carte de contenu associée à l’objet personnalisé.

```java
    public void logContentCardImpression() {
        if (cardData != null){
            BrazeManager.getInstance().logContentCardImpression(cardData.getContentCardId());
        }
    }
```

**Fonctions des appels de `Card`**<br>
Le [`BrazeManager`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt) peut faire référence aux dépendances du SDK Braze, telles que la liste du tableau d'objets de carte de contenu pour obtenir le `Card` pour appeler nos méthodes d’enregistrement.

```java
    public void logContentCardClicked(String idString) {
        getContentCard(idString).ifPresent(Card::logClick);
    }

    public void logContentCardImpression(String idString) {
        getContentCard(idString).ifPresent(Card::logImpression);
    }

    private Optional<Card> getContentCard(String idString) {
        return cardList.filter(c -> c.id.equals(idString)).findAny();
    }
```
{% endtab %}
{% endtabs %}

{% alert important %}
Pour une carte de contenu de variante de contrôle, un objet personnalisé doit toujours être instancié et la logique de l’interface graphique doit définir la vue correspondante de l’objet comme masquée. L’objet peut ensuite enregistrer une impression pour informer notre analytique du moment où l’utilisateur devrait avoir vu la carte de contrôle.
{% endalert %}

## Fichiers d’aide

{% details ContentCardKey Helper File %}
{% tabs %}
{% tab Kotlin %}
```kotlin
companion object Keys{
        const val idString = "idString"
        const val created = "created"
        const val classType = "class_type"
        const val dismissable = "dismissable"
        //...
    }
```
{% endtab %}
{% tab Java %}
```java
public static final String IDSTRING = "idString";
public static final String CREATED = "created";
public static final String CLASSTYPE = "class_type";
public static final String DISMISSABLE = "dismissable";
...
```
{% endtab %}
{% endtabs %}
{% enddetails %}

[1]: {% image_buster /assets/img/cc_implementation/android_supplemental_content.png %}
[2]: {% image_buster /assets/img/cc_implementation/supplementary_content.png %}
[3]: {% image_buster /assets/img/cc_implementation/android_message_center.png %}
[4]: {% image_buster /assets/img/cc_implementation/full_page.png %}
[5]: {% image_buster /assets/img/cc_implementation/html_webview.png %}
[6]: {% image_buster /assets/img/cc_implementation/android_discount2.png %}
[7]: {% image_buster /assets/img/cc_implementation/discount.png %}
