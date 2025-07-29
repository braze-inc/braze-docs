---
nav_title: Suporte da Braze
article_title: Suporte
description: "Esta página ajudará você a localizar o portal de suporte da Braze para enviar feedback sobre o produto Braze. Esta página será acessível apenas para clientes Braze."
alias: /braze_support/
page_type: reference
search_rank: 7
---

# [![curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/the-braze-support-portal/){: style="float:right;width:120px;border:0;" class="noimgborder"}suporte da Braze

## Acesse o portal de suporte

Para entrar em contato com a equipe de suporte da Braze, navegue até o dashboard da Braze. No dashboard, selecione **Suporte** > **Obter ajuda**.

![O menu suspenso "Support" (Suporte) com a opção de obter ajuda.]({% image_buster /assets/img_archive/get_help.png %}){: style="max-width:60%;"}

Dependendo das suas permissões no Braze e se você for um contato de suporte designado (premium), você será levado ao portal de suporte do Braze, onde poderá enviar e rastrear casos, ou ao nosso formulário de suporte padrão. Se não tiver certeza se é um contato de suporte da Braze, entre em contato com o administrador da Braze, o gerente de sucesso da Braze ou o proprietário da conta da sua empresa.

## Adição de contatos de suporte designados

Os contatos de suporte designados podem acessar todos os casos de suporte da sua empresa, independentemente de quem os enviou. É possível definir usuários como contatos de suporte designados diretamente na página **Editar usuário**. 

1. Acesse **Configurações** > **Usuários da empresa** e, em seguida, procure o usuário pelo nome ou endereço de e-mail.
2. Selecione o nome do usuário ou passe o mouse sobre a linha do nome do usuário para exibir um menu. 
3. No menu, selecione **Editar** para ser redirecionado para a página **Editar usuário**.
4. Marque a caixa de seleção **Definir este usuário como um Contato de Suporte Designado para o Portal de Suporte da Braze**.

![A caixa de seleção para definir um usuário como um contato de suporte designado.]({% image_buster /assets/img_archive/designated_support_contact.png %}){: style="max-width:70%;"}

O número de contatos de suporte designados que você pode definir depende do seu limite de contatos. Entre em contato com o gerente de sucesso do cliente para saber mais.

### Obtenção de acesso

Depois que um usuário for designado como um contato de suporte, o portal de suporte da Braze enviará a esse usuário um e-mail de boas-vindas com instruções para configurar seu acesso.

## Forneça capturas de tela do console de desenvolvedor

Ao se comunicar com o suporte, você pode descobrir que precisa acessar seu console de desenvolvedor para fornecer informações adicionais:
- Chrome
  1. Clique com o botão direito do mouse na página da Web e selecione **Inspecionar**.
  2. Selecione a guia **Console** na janela que se abre.
  3. Tire uma captura de tela da guia do console.<br><br>
- Firefox
  1. Clique com o botão direito do mouse na página da Web e selecione **Inspecionar elemento**.
  2. Selecione a guia **Console** na janela que se abre.
  3. Tire uma captura de tela da guia do console.<br><br>
- Safari
  1. Acessar Safari na barra de menu no topo do seu canva e então selecionar **Preferências**.
  2. Selecione **Advanced** e marque a caixa de seleção ao lado de **Show Develop menu in menu bar**. Você pode então sair da janela.
  3. Clique com o botão direito do mouse na página da Web e selecione **Inspecionar elemento**.
  4. Selecione a guia **Console** na janela que se abre.
  5. Tire uma captura de tela da guia do console.

## Melhores práticas para enviar um caso de suporte

### Forneça o máximo de informações possível

Quanto mais insights você puder oferecer, melhor. Inclua detalhes como o espaço de trabalho, o URL para a campanha ou segmento, e quaisquer IDs externos relevantes. Isso pode nos ajudar a resolver seu problema de forma mais eficiente.

### Forneça uma amostra de usuários

Compartilhe uma amostra de usuários em vez de todo o segmento afetado. O fornecimento de um número menor de usuários nos ajuda a restringir nosso escopo e acelerar nossas investigações.

### Anexe os registros de rede (registros HAR)

Se entrar em contato com o Suporte, será útil que o usuário afetado colete registros de rede (registros HAR) do navegador enquanto o problema ocorre. Isso exibirá as solicitações de rede entre o navegador e o servidor para os componentes individuais de uma página da Web, bem como o dashboard do Braze que o usuário está tentando abrir.

Peça para o usuário afetado fazer o seguinte:

1. Abra suas ferramentas de desenvolvedor. Se estiver usando o Chrome, isso pode ser feito usando o atalho de teclado `option` + `⌘` + `J` (no MacOS). Se estiver usando o Windows ou o Linux, isso pode ser feito usando o atalho `shift` + `CTRL` + `J`.
2. Selecione **Rede** > **Fetch/XHR** ou **XHR**.
3. Faça uma gravação ou captura de tela mostrando o **nome**, o **status**, o **tamanho** e **a hora** dos elementos.<br><br>![A guia "Fetch/XHR" em um navegador Chrome.]({% image_buster /assets/img/network_xhr.png %}){: style="max-width:60%;"}

Em seguida, anexe a gravação ou a captura de tela do usuário ao tíquete de suporte. Essas informações podem ajudar na investigação do Support.

### Esclarecer o comportamento esperado versus o real

Deixe-nos saber o que você esperava e o que realmente aconteceu. Isso pode nos ajudar a restringir as possíveis causas do problema.

### Anexar imagens relevantes

Considere anexar uma captura de tela para ilustrar o problema. Fornecer essas imagens pode ajudar significativamente nossa compreensão do problema e acelerar o processo de resolução.

### Avaliar o impacto

Selecione o nível de severidade apropriado para nos ajudar a atribuir os recursos certos para resolver o problema. 

{% alert important %}
Marcar um problema como "Crítico" significa que sua instância de produção está inativa e todo o trabalho no Braze foi interrompido.
{% endalert %}

