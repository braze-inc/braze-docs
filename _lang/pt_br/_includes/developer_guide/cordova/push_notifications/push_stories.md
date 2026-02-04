{% multi_lang_include developer_guide/prerequisites/cordova.md %} Você também precisará [configurar notificações por push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=cordova).

## Configuração de stories por push

### Etapa 1: Criar uma extensão de conteúdo de notificação

Em seu projeto Xcode, crie uma extensão de conteúdo de notificação. Para obter um passo a passo completo, consulte [iOS Push Stories Tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories/).

### Etapa 2: Configure seu grupo de app push

No arquivo `config.xml` do seu projeto, configure o grupo de app push [que acabou de criar](#cordova_step-1-create-a-notification-content-extension).

```xml
<preference name="com.braze.ios_push_app_group" value="NOTIFICATION_CONTENT_EXTENTION" />
```

Substitua `PUSH_APP_GROUP` pelo nome do seu grupo de app push. Seu `config.xml` deve ser semelhante ao seguinte:

```xml
<preference name="com.braze.ios_push_app_group" value="MyPushAppGroup" />
```

### Etapa 3: Adicionar um novo direcionamento

Abra seu Podfile e adicione `BrazePushStory` ao direcionamento da extensão de conteúdo de notificação [que você criou anteriormente](#cordova_step-1-create-a-notification-content-extension). Para evitar erros de símbolos duplicados, use a vinculação estática.

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

### Etapa 4: Reinstale suas dependências do CocoaPods

No terminal, acesse o diretório do iOS e reinstale as dependências do CocoaPod.

```bash
cd PATH_TO_PROJECT/platform/ios
pod install
```
