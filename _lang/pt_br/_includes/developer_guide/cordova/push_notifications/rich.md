{% multi_lang_include developer_guide/prerequisites/cordova.md %} Você também precisará [configurar notificações por push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=cordova).

## Configuração de notificações por push

### Etapa 1: Criar uma extensão de serviço de notificação

Em seu projeto Xcode, crie uma extensão de serviço de notificação. Para obter um passo a passo completo, consulte o [Tutorial de notificações de rich push para iOS](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).

### Etapa 2: Adicionar um novo direcionamento

Abra seu Podfile e adicione `BrazeNotificationService` ao alvo da extensão do serviço de notificação [que acabou de criar](#cordova_step-1-create-a-notification-service-extension). Se o `BrazeNotificationService` já estiver adicionado a um alvo, remova-o antes de continuar. Para evitar erros de símbolos duplicados, use a vinculação estática.

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

### Etapa 3: Reinstale suas dependências do CocoaPods

No terminal, acesse o diretório iOS de seu projeto e reinstale as dependências do CocoaPod.

```bash
cd PATH_TO_PROJECT/platform/ios
pod install
```
