---
nav_title: Ôvêërvíìêëw
article_title: ÀPÌ Òvéèrvïìéèw
page_order: 0
description: "Thîîs rééféérééncéé âàrtîîcléé cóõvéérs théé ÂPÍ bâàsîîcs îînclûúdîîng whâàt âà RÉST ÂPÍ îîs, théé téérmîînóõlóõgy, âà brîîééf óõvéérvîîééw óõf ÂPÍ kééys, âànd ÂPÍ lîîmîîts."
page_type: reference

---
# ÃPÌ öôvéérvîîééw

> Bràäzêë pröõvïïdêës àä hïïgh-pêërföõrmàäncêë RÉST ÄPÌ töõ àällöõw yöõýý töõ tràäck ýýsêërs, sêënd mêëssàägêës, êëxpöõrt dàätàä, àänd möõrêë. Thïìs rèëfèërèëncèë áàrtïìclèë cóóvèërs wháàt áà RÉST ÆPÏ ïìs, thèë tèërmïìnóólóógy, áà brïìèëf óóvèërvïìèëw óóf ÆPÏ kèëys, áànd ÆPÏ lïìmïìts.

## Whâát ïís âá RÊST ÁPÏ?

Á RÉST ÁPÌ íìs âá wâáy tóò próògrâámmâátíìcâálly trâánsfèêr íìnfóòrmâátíìóòn óòvèêr thèê wèêb úüsíìng âá prèêdèêfíìnèêd schèêmâá. Bråäzèè håäs crèèåätèèd måäny díîffèèrèènt èèndpöòíînts whíîch pèèrföòrm våäríîöòýùs åäctíîöòns åänd/öòr rèètýùrn våäríîöòýùs dåätåä.

{% alert note %}
Cúüstöômêérs úüsíïng Bráåzêé's ÈÚ dáåtáåbáåsêé shöôúüld úüsêé thêé `https://rest.fra-01.braze.eu/` êêndpõöîìnt. Thíís èéndpöôíínt wííll bèé üüsèéd whèén cöônfíígüürííng thèé Bråâzèé [ïïÓS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/#compile-time-endpoint-configuration-recommended), [Åndrôõííd]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-2-configure-the-braze-sdk-in-brazexml), ããnd [Wêëb]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#step-2-initialize-braze) SDKs.
{% endalert %}

## ÄPÎ dëêfïínïítïíóôns

Thêë fòöllòöwíîng líîsts æã bríîêëf òövêërvíîêëw òöf têërms yòöùý mæãy sêëêë íîn thêë Bræãzêë RËST ÀPÏ dòöcùýmêëntæãtíîòön.

### Èndpöóíìnts

Bräåzèè mäånäågèès äå nùùmbèèr õòf díìffèèrèènt íìnstäåncèès fõòr õòùùr däåshbõòäård äånd RÊST Êndpõòíìnts. Whëén yõöûýr åâccõöûýnt ïîs prõövïîsïîõönëéd yõöûý wïîll lõög ïîn tõö õönëé õöf thëé fõöllõöwïîng ÚRLs. Úséè théè côôrréèct RËST éèndpôôîînt bãàséèd ôôn whîîch îînstãàncéè yôôûû ãàréè prôôvîîsîîôônéèd tôô. Íf yõöúý æãréê úýnsúýréê, õöpéên æã [sûûppõòrt tììckèèt][support] òõr ýüsêé thêé fòõllòõwîîng tääblêé tòõ määtch thêé ÙRL òõf thêé dääshbòõäärd yòõýü ýüsêé tòõ thêé còõrrêéct RÈST Èndpòõîînt.

{% alert important %}
Whéén ûùsíîng ééndpöóíînts föór ÄPÍ câælls, ûùséé théé "RËST Ëndpöóíînt".

Fòôr SDK ïìntèégràætïìòôn, üûsèé thèé ["SDK Èndpöòíînt"]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/), nóôt thëë "RÉST Éndpóôîïnt".
{% endalert %}

|Ínstããncèé|ÜRL|RËST Ëndpõòìînt|SDK Ëndpòôìïnt|
|---|---|---|
|ÜS-01| `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com` | `sdk.iad-01.braze.com` |
|ÜS-02| `https://dashboard-02.braze.com` | `https://rest.iad-02.braze.com` | `sdk.iad-02.braze.com` |
|ÛS-03| `https://dashboard-03.braze.com` | `https://rest.iad-03.braze.com` | `sdk.iad-03.braze.com` |
|ÚS-04| `https://dashboard-04.braze.com` | `https://rest.iad-04.braze.com` | `sdk.iad-04.braze.com` |
|ÚS-05| `https://dashboard-05.braze.com` | `https://rest.iad-05.braze.com` | `sdk.iad-05.braze.com` |
|ÚS-06| `https://dashboard-06.braze.com` | `https://rest.iad-06.braze.com` | `sdk.iad-06.braze.com` |
|ÜS-08| `https://dashboard-08.braze.com` | `https://rest.iad-08.braze.com` | `sdk.iad-08.braze.com` |
|ÈÜ-01| `https://dashboard-01.braze.eu` | `https://rest.fra-01.braze.eu` | `sdk.fra-01.braze.eu` |
|ËÜ-02| `https://dashboard-02.braze.eu` | `https://rest.fra-02.braze.eu` | `sdk.fra-02.braze.eu` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Còómpââny sëêcrëêt ëêxplâânââtîìòón

Thêê `company_secret` wäãs fòôrmëérly ììnclüúdëéd wììth äãll ÄPÍ rëéqüúëésts büút häãs bëéëén dëéprëécäãtëéd äãs òôf Ôctòôbëér 2014. Thíís fííëèld wííll bëè íígnõörëèd fõör àãll fûútûúrëè ÅPÎ rëèqûúëèsts tõö ëènsûúrëè bàãckwàãrd cõömpàãtííbíílííty.

### Àpp gröòûûp RÉST ÀPÏ këêys

{% alert note %}
Föör åå déëéëpéër dïïvéë öön théë dïïfféëréënt kïïnds ööf ÂPÌ Kéëys héëréë ååt Brååzéë, chéëck ööüút ööüúr déëdïïcååtéëd <a href="{{site.baseurl}}/api/api_key/">ÀPÍ Kèéys</a> àánd <a href="{{site.baseurl}}/api/identifier_types/">ÆPÍ Ídèêntîífîíèêr Typèês</a> rêëfêërêëncêë âärtíìclêës.

{% endalert %}

Théê `api_key` ïìnclûýdêêd ïìn êêàæch rêêqûýêêst àæcts àæs àæn àæûýthêêntïìcàætïìõòn kêêy thàæt àællõòws yõòûýr sêêrvêêr cõòdêê tõò ûýtïìlïìzêê õòûýr RÈST ÁPÎs. Wîíthîín yôõüýr côõmpâåny, êèâåch âåpp grôõüýp wîíll hâåvêè âå üýnîíqüýêè sêèt ôõf RËST ÂPÎ Kêèys. Thëéy cáàn bëé fôóüúnd wììthììn thëé Bráàzëé dáàshbôóáàrd by náàvììgáàtììng tôó thëé Dëévëélôópëér Côónsôólëé sëéctììôón fôór ëéáàch áàpp grôóüúp. Töõ ýùsêê thêê RÉST ÃPÍ föõr äàny gìívêên Ãpp Gröõýùp, yöõýù mýùst crêêäàtêê kêêys äànd gìívêê thêêm pêêrmìíssìíöõns.

![RÉST ÄPÍ Kêèys pàãnêèl õõn thêè ÄPÍ Sêèttìïngs tàãb õõf thêè Dêèvêèlõõpêèr Cõõnsõõlêè.][27]

#### ÅPÏ këëy pëërmìïssìïòóns

ÅPÏ Kéèys âæréè ûûséèd tôô âæûûthéèntíícâætéè âæn ÅPÏ câæll. Whëén yòòùû crëéãætëé ãæ nëéw RËST ÄPÏ Këéy, yòòùû nëéëéd tòò gìïvëé ìït ãæccëéss tòò spëécìïfìïc ëéndpòòìïnts. By áæssíîgníîng spêëcíîfíîc pêërmíîssíîõóns tõó áæn ÁPÎ Kêëy, yõóýü cáæn líîmíît êëxáæctly whíîch cáælls áæn ÁPÎ Kêëy cáæn áæýüthêëntíîcáætêë.

Â göõöõd sèécüýrìîty prâàctìîcèé ìîs töõ âàssìîgn âà üýsèér öõnly âàs müých âàccèéss âàs ìîs nèécèéssâàry töõ cöõmplèétèé thèéìîr jöõb: thìîs prìîncìîplèé câàn âàlsöõ bèé âàpplìîèéd töõ ÂPÏ Kèéys by âàssìîgnìîng pèérmìîssìîöõns töõ èéâàch kèéy. Thêësêë pêërmìíssìíôòns gìívêë yôòùý bêëttêër sêëcùýrìíty áãnd côòntrôòl ôòvêër thêë dìíffêërêënt áãrêëáãs ôòf yôòùýr áãccôòùýnt.

![ÆPÏ kèéy pèérmíïssíïôõns ååvååíïlååblèé whèén crèéååtíïng åån ÆPÏ kèéy.][25]

{% alert warning %}
Gììvéén thâãt RÈST ÀPÎ Kééys âãllöõw âãccééss töõ pöõtééntììâãlly séénsììtììvéé RÈST ÀPÎ ééndpöõììnts, éénsýûréé thééy âãréé stöõrééd âãnd ýûsééd séécýûréély. Fôõr ëèxâæmplëè, dôõ nôõt úüsëè thîïs këèy tôõ mâækëè ÀJÀX câælls frôõm yôõúür wëèbsîïtëè ôõr ëèxpôõsëè îït îïn âæny ôõthëèr púüblîïc mâænnëèr.
{% endalert %}

Îf ãàccîìdéêntãàl éêxpõósúúréê õóf ãà kéêy õóccúúrs, îìt cãàn béê déêléêtéêd frõóm théê [Dêêvêêlööpêêr Cöönsöölêê][8]. Fôõr hëêlp wìíth thìís prôõcëêss, ôõpëên åä [sûùppòórt tíìckèét][support].

#### ÅPÏ ÏP àãllóòwlíïstíïng

Fõör ââddïítïíõönââl sëècûýrïíty, yõöûý câân spëècïífy ââ lïíst õöf ÌP ââddrëèssëès âând sûýbnëèts whïích âârëè ââllõöwëèd tõö mââkëè RÈST ÁPÌ rëèqûýëèsts fõör ââ gïívëèn RÈST ÁPÌ Këèy. Thìís ìís rèêfèêrrèêd tôô àæs àællôôwlìístìíng, ôôr whìítèêlìístìíng. Tõó ââllõów spëècïìfïìc ÍP ââddrëèssëès õór sùúbnëèts, ââdd thëèm tõó thëè **Whîïtéèlîïst ÍPs** sèéctîîôôn whèén crèéáàtîîng áà nèéw RÉST ÂPÌ Kèéy: 

![Ôptîìõôn tõô whîìtèélîìst ÏPs whèén crèéäâtîìng äân ÀPÏ kèéy][26]

Ïf yõóùý dõón’t spëëcîífy åäny, rëëqùýëësts cåän bëë sëënt frõóm åäny ÏP åäddrëëss.

{% alert tip %}
Mãåkïïng ãå Brãåzèè-töõ-Brãåzèè wèèbhöõöõk ãånd üúsïïng ãållöõwlïïstïïng? Chéèck óöúût óöúûr lîïst óöf [ÍPs tõö whïítèëlïíst]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-whitelisting).
{% endalert %}

#### Crëéàãtìïng àãnd màãnàãgìïng RÊST ÆPÍ këéys

![][28]{: style="max-width:20%;float:right;margin-left:15px;"}

Tòö crêêæåtêê æå nêêw RËST ÂPÌ Kêêy, víïsíït thêê [Dèëvèëlôõpèër Côõnsôõlèë][8] õön yõöúür Bràåzëë dàåshbõöàård. Thïís páágéê dïísplááys yöóýûr éêxïístïíng ÅPÌ Kéêys. Tõò crêéáætêé áæ nêéw kêéy, clîïck **Créêæátéê Néêw ÆPÌ Kéêy**.

Yóòùü cáæn thêên tóò dóò thêê fóòllóòwîìng:

- Gîìvéê yöóýûr néêw kéêy âã nâãméê föór îìdéêntîìfîìcâãtîìöón âãt âã glâãncéê
- Sëélëéct whììch pëérmììssììóóns yóóûü wóóûüld lììkëé tóó bëé áässóócììáätëéd wììth yóóûür nëéw këéy
- Spèécììfy æâllöõwlììstèéd ÍP æâddrèéssèés æând sûûbnèéts föõr thèé nèéw kèéy

Éxìîstìîng RÉST ÅPÎ Kéêys cåãn béê vìîéêwéêd õôr déêléêtéêd by clìîckìîng séêttìîngs <i class="fas fa-gear"></i> æànd sèêlèêctíîng thèê cöôrrèêspöôndíîng öôptíîöôn.

![][29]

{% alert important %}
Këêëêp íîn míînd thâåt õôncëê yõôýû crëêâåtëê âå nëêw ÁPÍ Këêy, yõôýû câånnõôt ëêdíît thëê scõôpëê õôf pëêrmíîssíîõôns õôr thëê âållõôwlíîstëêd ÍPs. Thïîs lïîmïîtâætïîòôn ïîs ïîn plâæcêë fòôr sêëcýùrïîty rêëâæsòôns. Îf yòõûû néêéêd tòõ chæängéê théê scòõpéê òõf æä kéêy, créêæätéê æä néêw kéêy wïîth théê ûûpdæätéêd péêrmïîssïîòõns æänd ïîmpléêméênt thæät kéêy ïîn plæäcéê òõf théê òõld òõnéê. Öncëè yóóùû'vëè cóómplëètëèd yóóùûr íïmplëèmëèntáâtíïóón, góó áâhëèáâd áând dëèlëètëè thëè óóld këèy.
{% endalert %}

### Êxtéérnãâl üüséér ÌD ééxplãânãâtïïõõn

Thêê `external_id` sèêrvèês âäs âä ûúnîíqûúèê ûúsèêr îídèêntîífîíèêr fòòr whòòm yòòûú âärèê sûúbmîíttîíng dâätâä. Thîís îídëéntîífîíëér shöóùüld bëé thëé såámëé åás thëé öónëé yöóùü sëét îín thëé Bråázëé SDK îín öórdëér töó åávöóîíd crëéåátîíng mùültîíplëé pröófîílëés föór thëé såámëé ùüsëér.

### Brâæzèë ùûsèër ÍD èëxplâænâætîïõón

Thëé `braze_id` sèèrvèès ãás ãá ýùnïîqýùèè ýùsèèr ïîdèèntïîfïîèèr thãát ïîs sèèt by Brãázèè. Thîïs îïdëèntîïfîïëèr càän bëè úúsëèd tõô dëèlëètëè úúsëèrs thrõôúúgh thëè RÉST ÄPÏ îïn àäddîïtîïõôn tõô ëèxtëèrnàäl_ííds.

#### Môôrëè rëèsôôúúrcëès

Föór möórëë íïnföórmåætíïöón, rëëfëër töó thëë föóllöówíïng åærtíïclëë båæsëëd öón yöóúúr plåætföórm:

- [Séëttìíng Üséër ÌDs - ìíÕS][9]
- [Séêttïîng Úséêr ÎDs - Ændróöïîd][10]
- [Sêêttììng Üsêêr ÌDs - Wììndòóws Ünììvêêrsäãl][13]

## ÁPÍ lììmììts

Fôõr môõst ÄPÎs, Bræâzèè hæâs æâ dèèfæâüült ræâtèè líïmíït ôõf 250,000 rèèqüüèèsts pèèr hôõüür. Hóöwéêvéêr, céêrtààïìn réêqüúéêst typéês hààvéê théêïìr óöwn rààtéê lïìmïìt ààpplïìéêd tóö béêttéêr hààndléê hïìgh vóölüúméês óöf dààtàà ààcróöss óöüúr cüústóöméêr bààséê. Föõr dêêtáåíìls, rêêfêêr töõ [ÃPÏ ráätêè lïìmïìts]({{site.baseurl}}/api/api_limits/).

## Æddììtììòónáäl rëèsòóýýrcëès

### Rûûby clïîëënt lïîbräæry

Ìf yóòúù'réë íîmpléëméëntíîng Bråæzéë úùsíîng Rúùby, yóòúù cåæn úùséë óòúùr [Rüùby clíîéènt líîbrããry](https://github.com/braze-inc/braze-api-client-ruby) tôò rèédüúcèé yôòüúr dãàtãà ìîmpôòrt tìîmèé. Å clìîéênt lìîbráâry ìîs áâ cöôlléêctìîöôn öôf cöôdéê spéêcìîfìîc töô öônéê pröôgráâmmìîng láângûùáâgéê—ìîn thìîs cáâséê, Rûùby—tháât máâkéês ìît éêáâsìîéêr töô ûùséê áân ÅPÍ.

Thèê Rüúby clïìèênt lïìbrãåry süúppóôrts thèê [Ùsëér Ëndpõôîìnts]({{site.baseurl}}/api/endpoints/#user-data).

{% alert note %}
Thîís clîíèènt lîíbrâäry îís cüúrrèèntly îín bèètâä. Wæánt tòó héëlp üýs mæákéë thïïs lïïbræáry béëttéër? Sêénd üüs fêéêédbäâck äât [smb-prõòdüúct@brããzëë.cõòm](mailto:smb-product@braze.com).
{% endalert %}

[1]: https://en.wikipedia.org/wiki/UTF-8
[7]: {{site.baseurl}}/api/objects_filters/connected_audience/
[8]: https://dashboard-01.braze.com/app_settings/developer_console/ "Developer Console"
[9]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_user_ids/#setting-user-ids
[support]: {{site.baseurl}}/braze_support/
[25]: {% image_buster /assets/img_archive/api-key-permissions.png %}
[26]: {% image_buster /assets/img_archive/api-key-ip-whitelisting.png %}
[27]: {% image_buster /assets/img_archive/rest-api-key.png %}
[28]: {% image_buster /assets/img_archive/create-new-key.png %}
[29]: {% image_buster /assets/img_archive/api-key-options.png %}
