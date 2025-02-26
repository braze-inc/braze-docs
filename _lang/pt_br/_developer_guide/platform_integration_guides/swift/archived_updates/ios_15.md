---
nav_title: Guia de atualização do iOS 15
article_title: Guia de atualização do SDK do iOS 15
page_order: 7
platform: iOS
description: "Este artigo de referência aborda as novas atualizações do sistema operacional iOS 15, as atualizações necessárias do SDK e os novos recursos."
hidden: true
noindex: true
---

# Guia de atualização do SDK do iOS 15

> Este guia descreve as alterações introduzidas no iOS 15 (WWDC21) e as etapas de atualização necessárias para a integração de seu SDK da Braze para iOS. Para obter uma lista completa das novas atualizações do iOS 15, consulte as notas de versão do [iOS 15](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-15-release-notes) da Apple.


## Alterações de transparência nas navegações da interface do usuário

Como parte de nossos testes anuais de versões beta do iOS, identificamos uma alteração feita pela Apple que faz com que determinadas barras de navegação da interface do usuário apareçam transparentes em vez de opacas. Isso será visível no iOS 15 ao usar a interface de usuário padrão do Braze para cartões de conteúdo ou quando os deep links da Web forem abertos dentro do seu aplicativo em vez de em um aplicativo de navegador separado.

Para evitar essa mudança visual no iOS 15, recomendamos enfaticamente que você faça upgrade para o [SDK da Braze para iOS v4.3.2](https://github.com/Appboy/appboy-ios-sdk/releases/tag/4.3.2) o mais rápido possível, antes que os usuários comecem a atualizar seus telefones para o novo sistema operacional iOS 15.

## Novas configurações de notificação {#notification-settings}

O iOS 15 introduziu novos recursos de notificação para ajudar os usuários a manter o foco e evitar interrupções frequentes ao longo do dia. Estamos entusiasmados em oferecer suporte a esses novos recursos. Esses recursos não requerem atualizações adicionais do SDK e serão aplicados apenas aos usuários de dispositivos iOS 15.

### Modos de foco {#focus-mode}

Os usuários do iOS 15 agora podem criar "Modos de foco", perfis personalizados usados para determinar quais notificações eles querem que sejam exibidas com destaque.

![]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

### Níveis de interrupção {#interruption-levels}

No iOS 15, as notificações por push podem ser enviadas com um dos quatro níveis de interrupção:

* **Passivo** (novo) - Sem som, sem vibração, sem despertar da tela, sem quebra das configurações de foco.
* **Ativo** (padrão) - Permite som, vibração, ativação da tela, sem interrupção das configurações de foco.
* **Time-Sensitive** (novo) - Permite som, vibração, despertar da tela, pode romper os controles do sistema, se permitido.
* **Crítico** \- Permite som, vibração, despertar da tela, pode romper os controles do sistema e ignorar o interruptor de campainha.

Consulte [Opções de notificação do iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#interruption-level) para saber mais sobre como definir essa opção no iOS Push.

### Resumo da notificação {#notification-summary}

![]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

No iOS 15, os usuários podem (opcionalmente) escolher determinados horários ao longo do dia para receber um resumo das notificações. As notificações que não exigem atenção imediata (como as enviadas como "Passivas" ou enquanto o usuário estiver no Modo de Foco) serão agrupadas para evitar interrupções constantes ao longo do dia.

Para cada notificação enviada, em breve você poderá especificar uma "pontuação de relevância" para controlar qual notificação deve aparecer na parte superior do resumo.

Consulte [Opções de notificação do iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#relevance-score) para saber mais sobre como definir a "pontuação de relevância" de uma notificação.

## Botões de localização {#location-buttons}

O iOS 15 apresenta uma maneira nova e conveniente para os usuários concederem temporariamente acesso ao local em um app. 

O novo botão de local se baseia na permissão existente "Permitir uma vez" sem solicitar repetidamente aos usuários que clicam várias vezes na mesma sessão.

Para saber mais, assista ao vídeo [Conheça o botão de localização](https://developer.apple.com/videos/play/wwdc2021/10102/) da Apple na Worldwide Developer Conference (WWDC) deste ano.

{% alert tip %}
Esse recurso lhe dá uma chance extra de solicitar permissão aos usuários! Os usuários que recusaram anteriormente as permissões de local antes do iOS 15 receberão um aviso ao clicar no botão de local como uma oportunidade de redefinir a permissão do estado recusado uma última vez.
{% endalert %}

### Uso de botões de local com o Braze

Não é necessária nenhuma integração adicional ao usar botões de local com o Braze. Seu app deve continuar passando o local do usuário (depois que ele tiver concedido permissão) como de costume.

De acordo com a Apple, para os usuários que já compartilharam o acesso ao local em segundo plano, a opção "While Using App" continuará a conceder esse nível de permissão depois que eles fizerem upgrade para o iOS 15.

## E-mail da Apple {#mail}

Este ano, a Apple anunciou muitas atualizações para o rastreamento e a privacidade de e-mails. Para saber mais, confira nossa [postagem no blog](https://www.braze.com/resources/articles/9-ways-email-marketers-can-respond-to-apples-mail-privacy-protection-feature).

## Local do endereço IP do Safari

No iOS 15, os usuários poderão configurar o Safari para tornar anônimo ou generalizar o local determinado a partir de seus endereços IP. Tenha isso em mente ao usar o direcionamento ou a segmentação com base no local.

