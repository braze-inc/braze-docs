---
nav_title: Notificações por push
article_title: Notificações por push para o SDK do Cordova Braze
platform:
  - Cordova
  - iOS
  - Android
page_order: 1
page_type: reference
description: "Este artigo aborda a implementação de notificações por push no Cordova."
channel: push
---

# Integração de notificações por push

> Saiba como integrar notificações por push para o SDK do Cordova Braze.

{% multi_lang_include cordova/prerequisites.md %}

## Recursos básicos de push

Por padrão, os recursos básicos de notificação por push são ativados no plug-in da Braze para Cordova. Você pode desativar esses recursos [personalizando suas configurações de XML]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_setup/customizations/#customization-options). Para obter mais detalhes sobre os recursos nativos de notificação por push, consulte os guias de notificação por push para [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/) e [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/).

## Recursos de push estendidos

{% alert important %}
Sempre que você adicionar, remover ou atualizar seus plug-ins do Cordova, o Cordova substituirá o Podfile em seu projeto Xcode. Isso significa que você precisará repetir esse processo sempre que modificar seus plug-ins do Cordova.
{% endalert %}

### Notificações de Rich push

#### Etapa 1: Criar uma extensão de serviço de notificação

Em seu projeto Xcode, crie uma extensão de serviço de notificação. Para obter um passo a passo completo, consulte o [Tutorial de notificações de rich push para iOS](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).

#### Etapa 2: Adicionar um novo direcionamento

Abra seu Podfile e adicione `BrazeNotificationService` ao alvo da extensão do serviço de notificação [que acabou de criar](#step-1-create-a-notification-service-extension). Se o `BrazeNotificationService` já estiver adicionado a um alvo, remova-o antes de continuar. Para evitar erros de símbolos duplicados, use a vinculação estática.

```ruby
target 'NOTIFICATION_SERVICE_EXTENSION' do
  use_frameworks! :linkage => :static
  pod 'BrazeNotificationService'
end
```

Substitua `NOTIFICATION_SERVICE_EXTENSION` pelo nome da extensão de seu serviço de notificação. Seu Podfile deve ser semelhante ao seguinte:

```ruby
target 'MyAppRichNotificationService' do
  use_frameworks! :linkage => :static
  pod 'BrazeNotificationService'
end
```

#### Etapa 3: Reinstale suas dependências do CocoaPods

No terminal, acesse o diretório iOS de seu projeto e reinstale as dependências do CocoaPod.

```bash
cd PATH_TO_PROJECT/platform/ios
pod install
```

### Stories por push

#### Etapa 1: Criar uma extensão de conteúdo de notificação

Em seu projeto Xcode, crie uma extensão de conteúdo de notificação. Para obter um passo a passo completo, consulte [iOS Push Stories Tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories/).

#### Etapa 2: Configure seu grupo de app push

No arquivo `config.xml` do seu projeto, configure o grupo de app push [que acabou de criar](#step-1-create-a-notification-content-extension).

```xml
<preference name="com.braze.ios_push_app_group" value="NOTIFICATION_CONTENT_EXTENTION" />
```

Substitua `PUSH_APP_GROUP` pelo nome do seu grupo de app push. Seu `config.xml` deve ser semelhante ao seguinte:

```xml
<preference name="com.braze.ios_push_app_group" value="MyPushAppGroup" />
```

#### Etapa 3: Adicionar um novo direcionamento

Abra seu Podfile e adicione `BrazePushStory` ao direcionamento da extensão de conteúdo de notificação [que você criou anteriormente](#step-1-create-a-notification-content-extension). Para evitar erros de símbolos duplicados, use a vinculação estática.

```ruby
target 'NOTIFICATION_CONTENT_EXTENSION' do
  use_frameworks! :linkage => :static
  pod 'BrazePushStory'
end
```

Substitua `NOTIFICATION_CONTENT_EXTENSION` pelo nome de sua extensão de conteúdo de notificação. Seu Podfile deve ser semelhante ao seguinte:

```ruby
target 'MyAppNotificationContentExtension' do
  use_frameworks! :linkage => :static
  pod 'BrazePushStory'
end
```

#### Etapa 4: Reinstale suas dependências do CocoaPods

No terminal, acesse o diretório do iOS e reinstale as dependências do CocoaPod.

```bash
cd PATH_TO_PROJECT/platform/ios
pod install
```
