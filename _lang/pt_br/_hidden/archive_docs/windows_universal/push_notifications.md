---
nav_title: Notificações por push
article_title: Notificações por push para o Windows Universal
platform: Windows Universal
page_order: 1
description: "Este artigo aborda as instruções de integração de notificações por push para a Plataforma Universal do Windows."
channel: push 
hidden: true
---

# Integração de notificações por push
{% multi_lang_include archive/windows_deprecation.md %}

![Um exemplo de push da Plataforma Universal do Windows.][10]{: style="float:right;max-width:40%;margin-left:15px;"}

Uma notificação por push é um alerta fora do aplicativo que aparece na tela do usuário quando ocorre uma atualização importante. As notificações por push são uma forma valiosa de fornecer aos usuários conteúdo relevante e oportuno ou para reengajá-los com seu app.

Consulte mais práticas recomendadas em nossa [documentação][9].

## Etapa 1: Configure seu app para push

Certifique-se de que, no arquivo `Package.appxmanifest`, as seguintes configurações estejam definidas:

Na guia **Aplicativo**, verifique se `Toast Capable` está definido como `YES`.

## Etapa 2: Configurar o dashboard do Braze

1. [Encontre seu SID e segredo do cliente][4]
2. Na página **Configurações** do dashboard da Braze, adicione o SID e o segredo do cliente em suas configurações.<br>![][6]

## Etapa 3: Atualização para registro aberto em segundo plano

Em seu método `OnLaunched`, depois de chamar `OpenSession`, adicione o seguinte snippet.

```
string campaignId = e.Arguments.Split(new[] { "_ab_pn_cid" }, StringSplitOptions.None)[0];
if (!string.IsNullOrEmpty(campaignId))
{
Appboy.SharedInstance.PushManager.LogPushNotificationOpened(campaignId);          
}
```

## Etapa 4: Criação de manipuladores de eventos

Para ouvir os eventos que são disparados quando o push é recebido e ativado (clicado pelo usuário), crie manipuladores de eventos e adicione-os aos eventos `PushManager`:

- `Appboy.SharedInstance.PushManager.PushReceivedEvent += YourPushReceivedEventHandler;`
- `Appboy.SharedInstance.PushManager.ToastActivatedEvent += YourToastActivatedEventHandler;`

Seus manipuladores de eventos devem ter as assinaturas:

- `void YourPushReceivedEventHandler(PushNotificationChannel sender, AppboyPushNotificationReceivedEventArgs args);`
- `void YourToastActivatedEventHandler(ToastNotification sender, AppboyToastActivatedEventArgs args);`

## Etapa 5: Deep linking do push para seu app

### Parte 1: Criação de deep links para seu app

Os deep links são usados para navegar com os usuários de fora do aplicativo diretamente para uma determinada tela ou página do aplicativo. Normalmente, isso é feito registrando um esquema de URL (por exemplo, myapp://mypage) com um sistema operacional e registrando o seu aplicativo para lidar com esse esquema; quando o sistema operacional é solicitado a abrir um URL desse formato, ele transfere o controle para o seu aplicativo.

O suporte a deep linking do WNS é diferente disso, pois inicia seu app com dados sobre para onde enviar o usuário. Quando o push do WNS é criado, ele pode incluir uma string de inicialização que é passada para o site `OnLaunched` do seu app quando o push é clicado e o aplicativo é aberto. Já usamos essa string de lançamento para fazer o rastreamento de campanhas e oferecemos aos usuários a capacidade de anexar seus próprios dados que podem ser analisados e usados para navegar pelo usuário quando o app é iniciado.

Se você especificar uma string de inicialização extra no dashboard ou na API REST, ela será adicionada ao final da string de inicialização que criamos, após a chave "abextras=". Portanto, um exemplo de string de inicialização pode ser semelhante a `ab_cn_id=_trackingid_abextras=page=settings`, no qual você especificou `page=settings` no parâmetro extra da string de inicialização para que possa analisá-la e levar o usuário à página de configurações.

### Parte 2: Deep links pelo dashboard

Especifique a string a ser anexada à string de inicialização no campo "Additional Launch String Configuration" (Configuração adicional da string de inicialização) nas configurações de notificação por push.

![][15]

### Parte 3: Deep links pela API REST

A Braze também permite o envio de deep links por meio da API REST. Os [objetos push do Windows Universal][13] aceitam um parâmetro opcional `extra_launch_string`.

[4]: http://msdn.microsoft.com/en-us/library/windows/apps/hh465407.aspx
[6]: {% image_buster /assets/img_archive/windows_sid.png %} "Painel de controle do Windows SID"
[9]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
[10]: {% image_buster /assets/img_archive/windows_uni_push_sample.png %}
[13]: {{site.baseurl}}/api/objects_filters/messaging/windows_objects/
[15]: {% image_buster /assets/img_archive/windows_deep_link_click_action.png %} "Ação de clique do deep linking"
