---
nav_title: suporte da Braze
article_title: Suporte
page_order: 7
description: "Esta página ajudará você a localizar o portal de suporte da Braze para enviar feedback sobre o produto Braze. Esta página será acessível apenas para clientes Braze."
alias: /braze_support/
page_type: reference
search_rank: 7
---

# [![curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/the-braze-support-portal/){: style="float:right;width:120px;border:0;" class="noimgborder"}suporte da Braze

## Acesse o portal de suporte

Para entrar em contato com a equipe de suporte da Braze, navegue até o dashboard da Braze. No dashboard, selecione **Suporte** > **Obter ajuda**.

![O dropdown "Suporte" com a opção de obter ajuda.]({% image_buster /assets/img_archive/get_help.png %}){: style="max-width:60%;"}

Dependendo das suas permissões no Braze e se você é um contato de suporte designado, você será direcionado para o portal de suporte da Braze, onde pode enviar e acompanhar casos, ou nosso formulário de suporte padrão. Se você não tiver certeza se é um contato de suporte da Braze, entre em contato com o administrador da Braze da sua empresa, o gerente de sucesso da Braze ou o proprietário da conta.

## Adicionando contatos de suporte designados

Contatos de suporte designados podem acessar todos os casos de suporte da sua empresa, independentemente de quem os enviou. Você pode definir usuários como contatos de suporte designados diretamente na página **Editar usuário**. 

1. Acesse **Configurações** > **Usuários da Empresa**, e então pesquise o usuário pelo nome ou endereço de e-mail.
2. Selecione o nome do usuário ou passe o mouse sobre a linha do nome do usuário para exibir um menu. 
3. No menu, selecione **Editar** para ser redirecionado para a página **Editar usuário**.
4. Marque a caixa de seleção para **Definir este usuário como um Contato de Suporte Designado para o Portal de Suporte da Braze**.

![A caixa de seleção para definir um usuário como um contato de suporte designado.]({% image_buster /assets/img_archive/designated_support_contact.png %}){: style="max-width:70%;"}

### Obtendo acesso

Após um usuário ser designado como um contato de suporte, o portal de suporte da Braze enviará a esse usuário um e-mail de boas-vindas com instruções para configurar seu acesso.

## Forneça capturas de tela do console de desenvolvedor

Ao se comunicar com o suporte, você pode descobrir que precisa acessar seu console de desenvolvedor para fornecer informações adicionais:
- Chrome
  1. Clique com o botão direito na página da web e selecione **Inspecionar**.
  2. Selecione a aba **Console** na janela que se abre.
  3. Tire uma captura de tela da guia do console.<br><br>
- Firefox
  1. Clique com o botão direito na página da web e selecione **Inspecionar Elemento**.
  2. Selecione a aba **Console** na janela que se abre.
  3. Tire uma captura de tela da guia do console.<br><br>
- Safari
  1. Acessar Safari na barra de menu no topo do seu canva e então selecionar **Preferências**.
  2. Selecione **Avançado** e então marque a caixa de seleção ao lado de **Mostrar menu de Desenvolvimento na barra de menu**. Você pode então sair da janela.
  3. Clique com o botão direito na página da web e selecione **Inspecionar Elemento**.
  4. Selecione a aba **Console** na janela que se abre.
  5. Tire uma captura de tela da guia do console.

## Melhores práticas para enviar um caso de suporte

### Forneça o máximo de informações possível

Quanto mais insights você puder oferecer, melhor. Inclua detalhes como o espaço de trabalho, o URL para a campanha ou segmento, e quaisquer IDs externos relevantes. Isso pode nos ajudar a resolver seu problema de forma mais eficiente.

### Forneça uma amostra de usuários

Compartilhe uma amostra de usuários em vez de todo o segmento afetado. Fornecer um número menor de usuários nos ajuda a restringir nosso escopo e acelerar nossas investigações.

### Anexar registros de rede (registros HAR)

Se você entrar em contato com o Suporte, será útil que o usuário impactado colete registros de rede (registros HAR) de seu navegador enquanto o problema ocorre. Isso exibirá as solicitações de rede entre o navegador e o servidor para os componentes individuais de uma página da web, assim como o dashboard da Braze que o usuário está tentando abrir.

Peça ao usuário afetado para fazer o seguinte:

1. Abra suas ferramentas de desenvolvedor. Se estiver usando o Chrome, isso pode ser feito usando o atalho de teclado `option` + `⌘` + `J` (no macOS). Se estiver usando Windows ou Linux, isso pode ser feito usando o atalho `shift` + `CTRL` + `J`.
2. Selecione **Rede** > **Buscar/XHR** ou **XHR**.
3. Capture uma gravação de tela ou uma captura de tela mostrando o **Nome**, **Status**, **Tamanho** e **Tempo** para os elementos.<br><br>![A aba "Buscar/XHR" em um navegador Chrome.]({% image_buster /assets/img/network_xhr.png %}){: style="max-width:60%;"}

Em seguida, anexe a gravação ou captura de tela do usuário ao ticket de Suporte. Essas informações podem ajudar na investigação do Suporte.

### Esclarecer o comportamento esperado versus o real

Deixe-nos saber o que você esperava e o que realmente aconteceu. Isso pode nos ajudar a restringir as possíveis causas do problema.

### Anexar imagens relevantes

Considere anexar uma captura de tela para ilustrar o problema. Fornecer essas imagens pode ajudar significativamente nossa compreensão do problema e acelerar o processo de resolução.

### Avaliar o impacto

Selecione o nível de severidade apropriado para nos ajudar a atribuir os recursos certos para resolver o problema. 

{% alert important %}
Marcar um problema como "Crítico" significa que sua instância de produção está fora do ar, e todo o trabalho dentro da Braze parou.
{% endalert %}

## Solução de problemas de acesso

Se você receber um erro ao fazer login no Portal de Suporte da Braze, como `Check your entry`, certifique-se de que seguiu o link no seu e-mail de boas-vindas para definir uma senha para o portal. Se você já fez isso ou conseguiu fazer login no portal anteriormente, crie um ticket de Suporte.