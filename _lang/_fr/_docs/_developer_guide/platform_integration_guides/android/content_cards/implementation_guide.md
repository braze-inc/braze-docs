---
nav_title: Implémentation avancée (facultatif)
article_title: Guide d'implémentation de la carte de contenu pour Android (facultatif)
platform: Android
page_order: 7
description: "Ce guide de mise en œuvre avancé couvre les considérations de code de la carte de contenu Android, trois cas d'utilisation construits par notre équipe, accompagnant des extraits de code, et des conseils sur la journalisation des impressions, les clics et les licenciements."
channel:
  - cartes de contenu
---

{% alert important %}
Vous recherchez le guide d'intégration des développeurs de cartes de contenu ? Trouvez-le [ici]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/data_model/).
{% endalert %}

# Guide d'implémentation de la carte de contenu

> Ce guide de mise en œuvre optionnel et avancé couvre les considérations de code de la carte de contenu, trois cas d'utilisation personnalisés construits par notre équipe, accompagnant des extraits de code, et des conseils sur la journalisation des impressions, les clics et les licenciements. Visitez notre Dépôt de Démo de Braze [ici](https://github.com/braze-inc/braze-growth-shares-android-demo-app)! Veuillez noter que ce guide d'implémentation est centré sur une implémentation de Kotlin, mais des extraits de code Java sont fournis pour ceux qui sont intéressés.

## Considérations de code

### Importer des instructions et des fichiers d'aide

Lors de la création de Cartes de Contenu, vous devriez exposer le Braze SDK via un seul gestionnaire singleton. Ce motif protège le code de votre application des détails d'implémentation de Braze derrière une abstraction partagée qui a du sens pour votre cas d'utilisation. Il facilite également le suivi, le débogage et la modification du code. Un exemple d'implémentation du gestionnaire peut être trouvé [ici](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt).

### Cartes de contenu en tant qu'objets personnalisés

Vos propres objets personnalisés déjà utilisés dans votre application peuvent être étendus pour transporter des données de carte de contenu, abstraction de la source des données dans un format déjà compris par le code de votre application. Les abstractions de la source de données telles que cela permettent de travailler avec différents backends de données de manière interchangeable et concertée. Dans cet exemple, nous avons défini la classe de base abstraite `ContentCardable` pour représenter à la fois nos données existantes (fed, dans cet exemple, à partir d'un fichier JSON local) et les nouvelles données, fournies depuis le SDK Braze. La classe de base expose également les données de la carte de contenu brute pour les consommateurs qui ont besoin d'accéder à l'implémentation de la `carte` originale.

Lors de l'initialisation d'instances `ContentCardable` à partir du Braze SDK, nous utilisons le `class_type` supplémentaire pour associer la Carte de Contenu à une sous-classe concrète. Nous utilisons ensuite les paires de valeurs clés additionnelles définies dans le tableau de bord de Braze pour remplir les champs nécessaires.

Une fois que vous avez une bonne compréhension de ces considérations de code, consultez nos [cas d'utilisation](#sample-use-cases) ci-dessous pour commencer à implémenter vos propres objets personnalisés.

{% tabs local %}
{% tab No Card Dependencies %}
{% subtabs global %}
{% subtab Kotlin %}
__Aucune `Carte` Dépendances__<br> `ContentCardData` représente les valeurs communes d'une `Carte`.

```kotlin
abstract class ContentCardable (){

    var cardData: ContentCardData ? = null

    constructor(data:Map<String, Any>):this(){
        cardData = ContentCardData(data[idString] as String,
            ContentCardClass. alueFrom(data[classType] as String),
            data[created] as Long,
            data[dismissable] as Boolean)
    }

    val isContentCard : Boolean
        get() = cardData ! null

    fun logContentCardClicked() {
        BrazeManager. etInstance().logContentCardClicked(cardData?. ontentCardId)
    }

    fun logContentCardDismissed() {
        BrazeManager.getInstance().logContentCardDismissed(cardData?. ontentCardId)
    }

    fun logContentCardImpression() {
        BrazeManager.getInstance().logContentCardImpression(cardData?. ontentCardId)
    }
}

data class ContentCardData (var contentCardId: String,
                            var contentCardClassType: ContentCardClass,
                            var créé : Long,
                            var renvoyable : Booléen)
```
{% endsubtab %}
{% subtab Java %}
__Aucune `Carte` Dépendances__<br> `ContentCardData` représente les valeurs communes d'une `Carte`.

```java
public abstrait classe ContentCardable{

  ContentCardData privé cardData = null;

  public ContentCardable(Map<String, Object> data){
      cardData = new ContentCardData()
      cardData. ontentCardId = (String) data.get(idString);
      cardData.contentCardClassType = contentCardClassType.valueOf((String)data.get(classType));
      cardData.createdAt = Long. arseLong((String)data.get(createdAt));
      cardData.dismissable = Boolean.parseBoolean((String)data. et(rejetable));
  }

  public ContentCardable(){

  }

  public boolean isContentCard(){
    return cardData ! null ;
  }

  public void logContentCardClicked() {
    if (isContentCard()){
      BrazeManager. etInstance().logContentCardClicked(cardData. ontentCardId)
    }
  }

  public void logContentCardDismissed() {
    if(isContentCard()){
      BrazeManager. etInstance().logContentCardDismissed(cardData. ontentCardId)
    }
  }

  public void logContentCardImpression() {
    if(isContentCard()){
      BrazeManager. etInstance().logContentCardImpression(cardData. ontentCardId)
    }
  }
}

ContentCardData{
  public String contentCardId;
  ContentCardClass contentCardClassType;
  public long createdAt;
  public booléen rejetable;
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Custom Objects %}
{% subtabs global %}
{% subtab Kotlin %}
__Initiateur d'objet personnalisé__<br>MetaData d'une carte `` est utilisée pour remplir les variables de votre sous-classe en béton. Selon la sous-classe, vous devrez peut-être extraire des valeurs différentes lors de l'initialisation. Les paires clé-valeur installées dans le tableau de bord Braze sont représentées dans le dictionnaire « extras ».

```kotlin
class Tile: ContentCardable {
    constructor(metadata:Map<String, Any>):super(metadata){
        val extras = metadata[extras] comme? Map<String, Any>
        title = extras?.get(Keys.title) comme? String
        image = extras?.get(Keys.image) comme? La chaîne
        détail = métadonnées[ContentCardable.detail] comme ? Chaîne
        balises = (métadonnées[ContentCardable.tags] comme? String)?.split(",")
        val priceString = extras?.get(Keys.price) comme? Chaîne
        if (priceString?.isNotEmpty() == true){
            price = priceString.toDouble()
        }
        id = floor(Math.random()*1000).toInt()
    }
}
```
{% endsubtab %}
{% subtab Java %}
__Initiateur d'objet personnalisé__<br>MetaData d'une carte `` est utilisée pour remplir les variables de votre sous-classe en béton. Selon la sous-classe, vous devrez peut-être extraire des valeurs différentes lors de l'initialisation. Les paires clé-valeur installées dans le tableau de bord Braze sont représentées dans le dictionnaire « extras ».

```java
la classe publique Tile extends ContentCardable {

    public Tile(Map<String, Object> metadata){
        super(metadata);
        ceci. métadonnées etail = (chaîne de caractères). et(ContentCardable.detail);
        this.tags = ((String)metadata.get(ContentCardable.tags)).split(",");
        if (metadata.containsKey(Keys. xtras){
            Carte<String, Object> extras = metadata.get(Keys. xtras);
            this.title = (String)extras. et(Keys.title);
            ceci. riz = Double.parseDouble((String)extras.get(Keys.price));
            ceci. mage = (String)extras.get(Keys.image);

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
__Identifying Types__<br> L'énumération `ContentCardClass` représente la valeur `class_type` dans le tableau de bord Braze et fournit une méthode pour initialiser l'énumération à partir des chaînes fournies par le SDK.

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
        // This value must be synced with the `class_type` value that has been set up in your
        // Braze dashboard or its type will be set to `ContentCardClassType.none.`
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
__Identifying Types__<br> L'énumération `ContentCardClass` représente la valeur `class_type` dans le tableau de bord Braze et fournit une méthode pour initialiser l'énumération à partir des chaînes fournies par le SDK.

```java
enum ContentCardClass {
    AD,
    COUPON,
    NONE,
    ITEM_TILE,
    ITEM_GROUP,
    MESSAGE_FULL_PAGE,
    MESSAGE_WEB_VIEW

    valeur statique publique From(String val){
        switch(val. oLowerCase()){
            case "coupon_code":{
                return COUPON;
            }
            cas "home_tile":{
                return ITEM_TILE;
            }
            cas "group":{
                return ITEM_GROUP;
            }
            cas "message_full_page":{
                return MESSAGE_FULL_PAGE ;
            }
            cas "message_webview":{
                return MESSAGE_WEB_VIEW;
            }
            cas "ad_banner":{
                return AD;
            }
            par défaut :{
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

## Exemple de cas d'utilisation

Il y a trois exemples de cas d'utilisation des clients fournis. Chaque cas d'utilisation offre une explication détaillée, des extraits de code pertinents, et voir comment les variables de la carte de contenu peuvent être utilisées dans le tableau de bord Braze :
- [Cartes de Contenu comme Contenu Supplémentaire](#content-cards-as-supplemental-content)
- [Cartes de contenu dans un centre de messages](#content-cards-in-a-message-center)
- [Cartes de contenu interactives](#interactive-content-cards)

### Cartes de contenu en tant que contenu complémentaire

!\[Supplementary Content PNG\]\[1\]{: style="float:right;max-width:25%;margin-left:15px;border:0;"}

Vous pouvez combiner de façon transparente les cartes de contenu dans un flux existant, permettant aux données provenant de plusieurs flux de se charger simultanément. Cela crée une expérience cohésive et harmonieuse avec les cartes de contenu Braze et le contenu de flux existant.

L'exemple à droite montre une `ListView` avec une liste hybride d'éléments qui sont peuplés via des données locales et des cartes de contenu propulsées par Braze. Grâce à cela, les cartes de contenu peuvent être indissociables du contenu existant.

#### Configuration du tableau de bord

Cette carte de contenu est délivrée par une campagne déclenchée par l'API, avec des paires clé-valeur déclenchées par l'API. Ceci est idéal pour les campagnes où les valeurs de la carte dépendent de facteurs externes pour déterminer le contenu à afficher à l'utilisateur. Notez que `class_type` doit être connu lors de la configuration.

!\[Supplementary Content PNG\]\[2\]{: style="max-width:60%;"}

##### Prêt à enregistrer des analyses ?
Visitez la section [suivante](#logging-impressions-clicks-and-dismissals) pour mieux comprendre à quoi devrait ressembler le flux de données.

### Cartes de contenu dans un centre de messages
<br>
Les cartes de contenu peuvent être utilisées dans un format de centre de messages où chaque message est sa propre carte. Chaque message dans le centre de messages est rempli via une charge utile de la carte de contenu et chaque carte contient des paires de valeur clé supplémentaires qui allument l'UI/UX sur le clic. Dans l'exemple ci-dessous, un message vous dirige vers une vue personnalisée arbitraire, tandis qu'un autre s'ouvre sur un webview qui affiche du HTML personnalisé.

!\[Message Center PNG\]\[3\]{: style="border:0;"}{: style="max-width:80%;border:0"}

#### Configuration du tableau de bord

Pour les types de messages suivants, la paire clé-valeur `class_type` doit être ajoutée à la configuration de votre tableau de bord. Les valeurs assignées ici sont arbitraires, mais doivent être distinguées entre les types de classe. Ces paires de valeurs clés sont les identifiants clés que l'application regarde quand elle décide où aller lorsque l'utilisateur clique sur un message de boîte de réception abrégée.

| Message de vue personnalisée arbitraire (page pleine)                                                                                                                                                                                                                                  | Message Webview (HTML)                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>Les paires clé-valeur pour ce cas d'utilisation incluent :<br><br>- `message_header` défini comme `Page Pleine`<br>- `class_type` défini comme `message_full_page`<br><br><br>! Centre de messages JPG1][4]{: style="largeur-max-100%;"} | Les paires clé-valeur pour ce cas d'utilisation incluent :<br><br>- `message_header` défini comme `HTML`<br>- `class_type` défini comme `message_webview`<br>- `message_title`<br><br>Ce message recherche également une paire clé-valeur HTML, mais si vous travaillez avec un domaine web, une paire clé-valeur d'URL est également valide.<br><br>!\[Message Center JPG2\]\[5\] |
{: .reset-td-br-1 .reset-td-br-2}

#### Explication supplémentaire

La logique du centre de messages est dictée par la `class_type` qui est fournie par les paires clé-valeur de Braze. En utilisant la méthode `createContentCardable` de notre exemple, vous pouvez filtrer et identifier ces types de classe.

{% tabs %}
{% tab Kotlin %}
__En utilisant `class_type` pour On Click Behavior__<br> Lorsque nous gonflons les données de la fiche de contenu dans nos classes personnalisées, nous utilisons la propriété `ContentCardClass` des données pour déterminer quelle sous-classe de béton doit être utilisée pour stocker les données.

```kotlin
 private fun createContentCardable(metadata: Map<String, Any>, type: ContentCardClass? : ContentCardable ?
        retourne quand(type){
            ContentCardClass. D -> Ad(métadonnées)
            ContentCardClass. ESSAGE_WEB_VIEW -> WebViewMessage(metadata)
            ContentCardClass. ESSAGE_FULL_PAGE -> FullPageMessage(métadonnées)
            ContentCardClass. TEM_GROUP -> Groupe(métadonnées)
            ContentCardClass. TEM_TILE -> Tile(métadonnées)
            ContentCardClass. OUPON -> Coupon (métadonnées)
            else -> null
        }
}
```

Ensuite, lorsque vous gérez l'interaction de l'utilisateur avec la liste de messages, nous pouvons utiliser le type de message pour déterminer la vue à afficher à l'utilisateur.

```kotlin
outrepasser le fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        //...
        ListView.onItemClickListener = AdapterView. nItemClickListener { parent, vue, position, id ->
           when (val card = dataProvider[position]){
                is WebViewMessage -> {
                    val intent = Intent(this, classe WebViewActivity::. ava)
                    bundle val = Bundle()
                    bundle. utString(WebViewActivity.INTENT_PAYLOAD, card.contentString)
                    intention. utExtras(bundle)
                    startActivity(intent)
                }
                est FullPageMessage -> {
                    intention val = Intent(this, classe FullPageContentCard::classe. ava)
                    paquets valables = Bundle()
                    bundle. utString(FullPageContentCard.CONTENT_CARD_IMAGE, carte. con)
                    bundle.putString(FullPageContentCard. ONTENT_CARD_TITLE, card.messageTitle)
                    bundle. utString(FullPageContentCard.CONTENT_CARD_DESCRIPTION, card.cardDescription)
                    intention. utExtras(bundle)
                    startActivity(intent)
                }
            }

        }
}
```
{% endtab %}
{% tab Java %}
__En utilisant `class_type` pour On Click Behavior__<br> Lorsque nous gonflons les données de la fiche de contenu dans nos classes personnalisées, nous utilisons la propriété `ContentCardClass` des données pour déterminer quelle sous-classe de béton doit être utilisée pour stocker les données.

```java
ContentCardable privéeContentCardable(Metadonnées de la carte<String, ?> , Type ContentCardClasse){
    switch(type){
        case ContentCardClass. D:{
            retourne un nouvel Ad(métadonnées) ;
        }
        case ContentCardClass. ESSAGE_WEB_VIEW:{
            retourne un nouveau WebViewMessage(métadonnées) ;
        }
        case ContentCardClass. ESSAGE_FULL_PAGE :{
            retourne un nouveau FullPageMessage(métadonnées) ;
        }
        case ContentCardClass. TEM_GROUP:{
            retourne un nouveau groupe(métadonnées) ;
        }
        coffres ContentCardClass. TEM_TILE:{
            retourne une nouvelle tuile(métadonnées);
        }
        coffres ContentCardClass. OUPON:{
            return new Coupon(metadata);
        }
        par défaut :{
            return null;
        }
    }
}

```

Ensuite, lorsque vous gérez l'interaction de l'utilisateur avec la liste de messages, nous pouvons utiliser le type de message pour déterminer la vue à afficher à l'utilisateur.

```java
@Override
annulé onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState)
        //...
        ListView.setOnItemClickListener(new AdapterView. nItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, vue vue, position d'int id){
               ContentCardable card = dataProvider. et(position);
               if (carte instance WebViewMessage){
                    Bundle intent = new Intent(ceci, Activité WebView. laiton);
                    Lot Bundle = nouveau Bundle(); Paquet
                    . utString(WebViewActivity.INTENT_PAYLOAD, card.getContentString());
                    intention. utExtras(bundle);
                    startActivity(intention);
                }
                sinon if (carte Instanceof FullPageMessage){
                    Intention = new Intent(ceci, Carte de contenu de la page complète. laiton);
                    Lot de Lot = Lot ();
                    bundle. utString(FullPageContentCard.CONTENT_CARD_IMAGE, carte. etIcon());
                    bundle.putString(FullPageContentCard.CONTENT_CARD_TITLE, carte. etMessageTitle());
                    bundle.putString(FullPageContentCard.CONTENT_CARD_DESCRIPTION, carte. etCardDescription());
                    intention. utExtras(bundle)
                    startActivity(intent)
                }
            }

        });
}
```

{% endtab %}
{% endtabs %}

##### Prêt à enregistrer des analyses ?
Visitez la section [suivante](#logging-impressions-clicks-and-dismissals) pour mieux comprendre à quoi devrait ressembler le flux de données.

!\[Interactive Content PNG\]\[6\]{: style="border:0;"}{: style="float:right;max-width:45%;border:0;margin-left:15px;"}

### Cartes de contenu interactives
<br>
Les cartes de contenu peuvent être exploitées pour créer des expériences dynamiques et interactives pour vos utilisateurs. Dans l'exemple à droite, nous avons un pop-up de carte de contenu apparaît à la caisse fournissant aux utilisateurs des promotions de dernière minute.

De telles cartes bien placées sont un excellent moyen de donner aux utilisateurs un "coup de pouce" vers des actions spécifiques de l'utilisateur. <br><br><br>
#### Configuration du tableau de bord

La configuration du tableau de bord pour les cartes de contenu interactives est rapide et simple. Les paires clé-valeur pour ce cas d'utilisation incluent un `discount_percentage` défini comme le montant de la remise désirée et `class_type` défini comme `coupon_code`. Ces paires de valeurs clés sont la façon dont les cartes de contenu spécifiques à chaque type sont filtrées et affichées sur l'écran de paiement.

!\[Interactive Content JPG\]\[7\]{: style="max-width:70%;"}

##### Prêt à enregistrer des analyses ?
Visitez la section [suivante](#logging-impressions-clicks-and-dismissals) pour mieux comprendre à quoi devrait ressembler le flux de données.

## Logs d'impressions, de clics et de licenciements

Après avoir élargi vos objets personnalisés pour fonctionner comme des Cartes de Contenu, la journalisation de précieuses métriques comme des impressions, des clics et des licenciements est rapide et simple. Cela peut être fait en utilisant une classe de base `ContentCardable` qui référence et fournit des données au `BrazeManager`.

#### __Composants d'implémentation__<br><br>

{% tabs %}
{% tab Kotlin %}
__Objets personnalisés Appelez les méthodes de journalisation__<br> Dans votre classe de base `ContentCardable` , vous pouvez appeler directement le `BrazeManager` si nécessaire. Rappelez-vous que, dans cet exemple, la propriété `cardData` sera nonnull si l'objet provient d'une carte de contenu.

```kotlin
override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
        val tile = currentTiles[position]
        tile.logContentCardImpression()
...
    }
```

__Récupérez la Carte de Contenu du ContentCardId__<br> La classe de base `ContentCardable` gère la lourde levée de l'appel au `BrazeManager` et en passant l'identifiant unique de la Carte de Contenu associée à l'objet personnalisé.

```kotlin
    fun logContentCardImpression() {
        cardData?.let { BrazeManager.getInstance().logContentCardImpression(it.contentCardId) }
    }
```

__Appelez les fonctions de la carte `` Fonctions__<br> Le [BrazeManager](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt) peut référencer les dépendances de Braze SDK telles que la liste d'objets de la carte de contenu pour obtenir la `carte` pour appeler nos méthodes de journalisation.

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
__Objets personnalisés Appelez les méthodes de journalisation__<br> Dans votre classe de base `ContentCardable` , vous pouvez appeler directement le `BrazeManager` si nécessaire. Rappelez-vous que, dans cet exemple, la propriété `cardData` sera nonnull si l'objet provient d'une carte de contenu.
```java
@Override
public View getView(int position, View convertView, ViewGroup parent) {
        Tuile = currentTiles.get(position);
        tile.logContentCardImpression();

    }
```

__Récupérez la Carte de Contenu à partir de la `ContentCardId`__<br> La classe de base `ContentCardable` gère la lourde levée d'appeler le `BrazeManager` et de passer l'identifiant unique de la Carte de Contenu associée à l'objet personnalisé.

```java
    public void logContentCardImpression() {
        if (cardData != null){
            BrazeManager.getInstance().logContentCardImpression(cardData.getContentCardId());
        }
}
```

__Call `Carte` Fonctions__<br> Les `[BrazeManager](insert)` peuvent référencer les dépendances Braze SDK telles que la liste d'objets Carte de contenu tableau pour obtenir la `Carte` pour appeler nos méthodes de journalisation.

```java
    public void logContentCardClicked(String idString) {
        getContentCard(idString). fPresent(Card::logClick);
    }

    public void logContentCardImpression(String idString) {
        getContentCard(idString). fPresent(Card::logImpression);
    }

    private Optional<Card> getContentCard(String idString) {
        return cardList. ilter(c -> c.id.equals(idString)).findAny();
}
```
{% endtab %}
{% endtabs %}

{% alert important %}
Pour une carte de contenu de variante de contrôle, un objet personnalisé doit toujours être instancié et la logique de l'interface utilisateur doit définir la vue correspondante de l'objet comme masquée. L'objet peut alors enregistrer une impression pour informer nos analytiques de quand un utilisateur aurait vu la carte de contrôle.
{% endalert %}

## Fichiers d'aide

{% details ContentCardKey Helper File %}
{% tabs %}
{% tab Kotlin %}
```kotlin
clés{
        const val idString = "idString"
        const val créé = "created"
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
[1]: {% image_buster /assets/img/cc_implementation/android_supplemental_content.png %} [2]: {% image_buster /assets/img/cc_implementation/supplementary_content.png %} [3]: {% image_buster /assets/img/cc_implementation/android_message_center. ng %} [4]: {% image_buster /assets/img/cc_implementation/full_page.png %} [5]: {% image_buster /assets/img/cc_implementation/html_webview. ng %} [6]: {% image_buster /assets/img/cc_implementation/android_discount2.png %} [7]: {% image_buster /assets/img/cc_implementation/discount.png %}
