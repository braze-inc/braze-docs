---
nav_title: Google Tag Manager
article_title: Google Tag Manager para iOS
platform: iOS
page_order: 7
description: "Este artigo aborda como inicializar, configurar e implementar o Google Tag Manager em seu app para iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Google Tag Manager para iOS

## Inicialização do SDK {#initializing-ios-google-tag-provider}

O SDK iOS do Braze pode ser inicializado e controlado por tags configuradas dentro do [Google Tag Manager](https://tagmanager.google.com/).

Antes de usar o Google Tag Manager, certifique-se de seguir nossa [configuração inicial do SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/).

## Configuração do Google Tag Manager {#configuring-ios-google-tag-manager}

Neste exemplo, vamos fingir que somos um app de streaming de música que deseja fazer o registro de diferentes eventos à medida que os usuários ouvem as músicas. Usando o Google Tag Manager para iOS, podemos controlar quais de nossos fornecedores terceirizados recebem esse evento e criar tags específicas para o Braze.

### Eventos personalizados

Os eventos personalizados são registrados com `actionType` definido como `logEvent`. O provedor de tag personalizada do Braze em nosso exemplo está esperando que o nome do evento personalizado seja definido usando `eventName`.

Para começar, crie um disparador que procure um "Nome do evento" igual a `played song`

![Um gatilho personalizado no Google Tag Manager configurado para disparar para alguns eventos quando "nome do evento" é igual a "música tocada".]({% image_buster /assets/img/android_google_tag_manager/gtm_android_trigger.png %})

Em seguida, crie uma nova tag ("Function Call") e insira a jornada da classe de seu [provedor de tag personalizado](#adding-ios-google-tag-provider) descrito mais adiante neste artigo. 

Essa tag será disparada quando for registrado o evento `played song` que acabamos de criar. 

Nos parâmetros personalizados (pares de valores-chave) da nossa tag de exemplo, definimos `eventName` como `played song` \- que será o nome do evento personalizado registrado no Braze.

{% alert important %}
Ao enviar um evento personalizado, defina `actionType` como `logEvent` e defina um valor para `eventName`, conforme mostrado no exemplo a seguir. 

O provedor de tag personalizado em nosso exemplo usará essas chaves para determinar qual ação tomar e qual nome de evento enviar à Braze quando receber dados do Google Tag Manager.
{% endalert %}

![Uma tag no Google Tag Manager com classpath e campos de par de valores chave. Esta tag está configurada para disparar com o gatilho "música tocada" criado anteriormente.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_function_call_tag.png %})

Você também pode incluir argumentos adicionais de pares de valores-chave na tag, que serão enviados como propriedades de eventos personalizados para o Braze. `eventName` e `actionType` não serão ignorados nas propriedades de eventos personalizados. No exemplo de tag a seguir, passaremos `genre`, que foi definido usando uma variável de tag no Google Tag Manager, proveniente do evento personalizado que registramos em nosso app.

A propriedade do evento `genre` é enviada ao Google Tag Manager como uma variável "Firebase - Event Parameter", pois o Google Tag Manager para iOS usa o Firebase como camada de dados.

![Uma variável no Google Tag Manager onde "genre" é adicionado como um parâmetro de evento para a tag "Braze - Evento de Música Tocada".]({% image_buster /assets/img/android_google_tag_manager/gtm_android_eventname_variable.png %})

Por fim, quando um usuário reproduzir uma música em nosso app, registraremos um evento por meio do Firebase e do Google Tag Manager usando o nome do evento de análise de dados do Firebase que corresponde ao nome do disparo da nossa tag, `played song`:

{% tabs %}
{% tab OBJECTIVE C %}

```obj-c
NSDictionary *parameters = @{@"genre" : @"pop",
                             @"number of times listened" : @42};
[FIRAnalytics logEventWithName:@"played song" parameters:parameters];
```

{% endtab %}
{% endtabs %}

### Registro de atributos personalizados

Os atributos personalizados são definidos por meio de um `actionType` definido como `customAttribute`. O provedor de tag personalizada da Braze está esperando que o atributo personalizado chave-valor seja definido por meio de `customAttributeKey` e `customAttributeValue`:

{% tabs %}
{% tab OBJECTIVE C %}

```obj-c
NSDictionary *parameters = @{@"customAttributeKey" : @"favorite song",
                             @"customAttributeValue" : @"Private Eyes"};
[FIRAnalytics logEventWithName:@"customAttribute" parameters:parameters];
```

{% endtab %}
{% endtabs %}

### Chamada de changeUser

As chamadas para `changeUser()` são feitas por meio de um `actionType` definido como `changeUser`. O provedor de tags personalizadas do Braze espera que o ID de usuário do Braze seja definido por meio de um par de valores-chave `externalUserId` dentro da sua tag:

{% tabs %}
{% tab OBJECTIVE C %}

```obj-c
NSDictionary *parameters = @{@"externalUserId" : userId};
[FIRAnalytics logEventWithName:@"changeUser" parameters:parameters];
```

{% endtab %}
{% endtabs %}

## Provedor de tags personalizadas do Braze SDK {#adding-ios-google-tag-provider}

Com as tags e os disparadores configurados, você também precisará implementar o Google Tag Manager em seu app para iOS, o que pode ser encontrado na [documentação](https://developers.google.com/tag-manager/ios/v5/) do Google.

Depois que o Google Tag Manager estiver instalado em seu app, adicione um provedor de tag personalizado para chamar os métodos do Braze SDK com base nas tags que você configurou no Google Tag Manager. 

Certifique-se de anotar o "Caminho da Classe" para o arquivo - é isso que você irá inserir ao configurar uma tag no [Google Tag Manager](https://tagmanager.google.com/) console.

Este exemplo mostra uma das muitas maneiras de estruturar seu provedor de tag personalizado, em que determinamos qual método do Braze SDK deve ser chamado com base no par de valores-chave `actionType` enviado pela tag GTM.

Os `actionType` suportados em nosso exemplo são `logEvent`, `customAttribute` e `changeUser`, mas você pode preferir alterar a forma como seu provedor de tag trata os dados do Google Tag Manager.

Adicione o seguinte código ao seu arquivo `BrazeGTMTagManager.h`:

{% tabs %}
{% tab OBJECTIVE C %}

```obj-c
@import Firebase;
@import GoogleTagManager;

@interface BrazeGTMTagManager : NSObject <TAGCustomFunction>

@end
```

{% endtab %}
{% endtabs %}

E adicione o seguinte código ao seu arquivo `BrazeGTMTagManager.m`:

{% tabs %}
{% tab OBJECTIVE C %}

```obj-c
#import <Foundation/Foundation.h>
#import "BrazeGTMTagManager.h"
#import "Appboy-iOS-SDK/AppboyKit.h"

static NSString *const ActionTypeKey = @"actionType";

// Custom Events
static NSString *const LogEventActionType = @"logEvent";
static NSString *const LogEventEventName = @"eventName";

// Custom Attributes
static NSString *const CustomAttributeActionType = @"customAttribute";
static NSString *const CustomAttributeKey = @"customAttributeKey";
static NSString *const CustomAttributeValueKey = @"customAttributeValue";

// Change User
static NSString *const ChangeUserActionType = @"changeUser";
static NSString *const ChangeUserExternalUserId = @"externalUserId";

@implementation BrazeGTMTagManager

- (NSObject *)executeWithParameters:(NSDictionary *)parameters {
  NSMutableDictionary *mutableParameters = [parameters mutableCopy];
  
  NSString *actionType = mutableParameters[ActionTypeKey];
  if (!actionType) {
    NSLog(@"There is no Braze action type key in this call. Doing nothing.", nil);
    return nil;
  }
  
  [mutableParameters removeObjectForKey:ActionTypeKey];
  
  if ([actionType isEqualToString:LogEventActionType]) {
    [self logEvent:mutableParameters];
  } else if ([actionType isEqualToString:CustomAttributeActionType]) {
    [self logCustomAttribute:mutableParameters];
  } else if ([actionType isEqualToString:ChangeUserActionType]) {
    [self changeUser:mutableParameters];
  } else {
    NSLog(@"Invalid action type. Doing nothing.");
  }
  return nil;
}

- (void)logEvent:(NSMutableDictionary *)parameters {
  NSString *eventName = parameters[LogEventEventName];
  [parameters removeObjectForKey:LogEventEventName];
  [[Appboy sharedInstance] logCustomEvent:eventName withProperties:parameters];
}

- (void)logCustomAttribute:(NSMutableDictionary *)parameters {
  NSString *customAttributeKey = parameters[CustomAttributeKey];
  id customAttributeValue = parameters[CustomAttributeValueKey];
  
  if ([customAttributeValue isKindOfClass:[NSString class]]) {
    [[Appboy sharedInstance].user setCustomAttributeWithKey:customAttributeKey
                                             andStringValue:customAttributeValue];
  } else if ([customAttributeValue isKindOfClass:[NSDate class]]) {
    [[Appboy sharedInstance].user setCustomAttributeWithKey:customAttributeKey
                                               andDateValue:customAttributeValue];
  } else if ([customAttributeValue isKindOfClass:[NSNumber class]]) {
    if (strcmp([customAttributeValue objCType], [@(YES) objCType]) == 0) {
      [[Appboy sharedInstance].user setCustomAttributeWithKey:customAttributeKey
                                                 andBOOLValue:[(NSNumber *)customAttributeValue boolValue]];
    } else if (strcmp([customAttributeValue objCType], @encode(short)) == 0 ||
               strcmp([customAttributeValue objCType], @encode(int)) == 0 ||
               strcmp([customAttributeValue objCType], @encode(long)) == 0) {
      [[Appboy sharedInstance].user setCustomAttributeWithKey:customAttributeKey
                                              andIntegerValue:[(NSNumber *)customAttributeValue integerValue]];
    } else if (strcmp([customAttributeValue objCType], @encode(float)) == 0 ||
               strcmp([customAttributeValue objCType], @encode(double)) == 0) {
      [[Appboy sharedInstance].user setCustomAttributeWithKey:customAttributeKey
                                               andDoubleValue:[(NSNumber *)customAttributeValue doubleValue]];
    } else {
      NSLog(@"Could not map NSNumber value to Appboy custom attribute:%@", customAttributeValue);
    }
  } else if ([customAttributeValue isKindOfClass:[NSArray class]]) {
    [[Appboy sharedInstance].user setCustomAttributeArrayWithKey:customAttributeKey
                                                           array:customAttributeValue];
  }
}

- (void)changeUser:(NSMutableDictionary *)parameters {
  NSString *userId = parameters[ChangeUserExternalUserId];
  [[Appboy sharedInstance] changeUser:userId];
}

@end
```

{% endtab %}
{% endtabs %}

