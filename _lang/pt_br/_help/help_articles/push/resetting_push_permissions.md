---
nav_title: Redefinição das permissões de push
article_title: Redefinição das permissões de push
page_type: solution
description: "Este artigo de ajuda aborda como redefinir as permissões e os dados do push do navegador."
channel: push
---

# Redefinição das permissões push

Se estiver tendo problemas com notificações por push no navegador, talvez seja necessário redefinir as permissões de notificação do site e limpar o armazenamento do site. Consulte estas etapas para obter ajuda.

## Redefinir o Chrome no desktop

1. Ao lado do seu URL no navegador Chrome, clique no ícone do controle deslizante **Exibir informações do site**.
2. Em **Notificações**, clique em **Redefinir permissão**.
3. Abra o Chrome DevTools. Veja a seguir os atalhos relevantes por sistema operacional.

<style> 
table {
    max-width: 50%;
}
</style>

| SO      | Atalhos de teclado                                                  |
| ------- | ------------------------------------------------------------------- |
| Mac      | `Fn` + `F12`<br>`Ctrl` + `Shift` + `I` |
| Windows | `F12`<br>`Ctrl` + `Shift` + `I` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{:start="4"}
4\. No DevTools, navegue até a guia **Aplicativo**.
5\. Na barra lateral, selecione **Armazenamento**.
6\. Clique em **Limpar dados do site**.
7\. O Chrome solicitará que você recarregue a página para aplicar as configurações atualizadas. Clique em **Recarregar**.

Suas permissões push foram redefinidas. Abra uma nova guia em seu site e experimente.

## Redefinir o Chrome no Android

Se houver uma notificação do seu site visível na gaveta de notificações do Android:

1. Na notificação por push, toque em <i class="fas fa-cog" title="Configurações"></i> e selecione **Configurações do site**.
2. Nas **configurações do Site**, toque em **Limpar e redefinir**.

Se você não tiver uma notificação de seu site aberta:

1. Abra o Chrome no Android.
2. Toque no menu <i class="fas fa-ellipsis-vertical"></i>.
3. Acesse **Configurações** > **Configurações do site** > **Notificações**.
4. Verifique se as notificações estão definidas como "Perguntar antes de enviar (recomendado)".
5. Encontre seu site na lista.
6. Selecione a entrada e toque em **Limpar e redefinir**.

Suas permissões push foram redefinidas. Abra uma nova guia em seu site e experimente.

## Redefinir o Firefox na área de trabalho

1. Ao lado do URL do seu site, clique em <i class="fa-solid fa-circle-info" alt="info icon"></i> ou <i class="fas fa-lock" alt="lock icon"></i>.
2. Em **Permissões**, ao lado de **Receber notificações**, selecione <i class="fa-solid fa-circle-xmark" title="Limpar essa permissão e perguntar novamente"></i> para limpar as permissões de notificação.
3. No mesmo menu, selecione **Limpar cookies e dados do site**.
4. Será exibida uma caixa de diálogo para confirmar sua escolha. Clique em **OK**.

Suas permissões push foram redefinidas. Abra uma nova guia em seu site e experimente.

## Redefinir o Firefox no Android

Para redefinir as permissões push no Android, consulte este [artigo de suporte da Mozilla](https://support.mozilla.org/en-US/kb/clear-your-browsing-history-and-other-personal-data#w_clear-specific-items-from-your-browser).

## Redefinir o Safari no MacOS

{% alert note %}
Essas etapas são apenas para o MacOS, pois a Apple não oferece suporte ao Web Push para o Safari no Windows.
{% endalert %}

1. Abra o Safari.
2. Na [barra de menus do Mac](https://support.apple.com/guide/mac-help/whats-in-the-menu-bar-mchlp1446/mac), acesse **Safari** > **Configurações** > **Sites** > **Notificações**.
3. Selecione seu site na lista.
4. Clique em **Remove (Remover** ) para excluir as permissões de notificação do site.
5. Em seguida, acesse **Privacy** > **Manage Website Data (** **Privacidade** > **Gerenciar dados do site**).
6. Selecione seu site na lista.
7. Clique em **Remove (Remover**) ou, para remover todos os dados do site, clique em **Remove All (Remover tudo**).
8. Clique em **Done (Concluído**).

Suas permissões push foram redefinidas. Abra uma nova guia em seu site e experimente.


*Última atualização em 12 de fevereiro de 2024*