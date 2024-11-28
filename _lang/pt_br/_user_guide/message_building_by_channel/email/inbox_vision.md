---
nav_title: Inbox Vision
article_title: Inbox Vision
page_order: 9
description: "Este artigo de referência aborda como configurar o Inbox Vision, um recurso que permite que os profissionais de marketing visualizem seus e-mails a partir da perspectiva de vários clientes de e-mail e dispositivos móveis."
tool:
  - Dashboard
channel:
  - email

---

# Inbox Vision

> O Inbox Vision permite visualizar seus e-mails a partir da perspectiva de vários clientes de e-mail e dispositivos móveis. 

## Teste seu envio de e-mail no Inbox Vision

O Inbox Vision funciona quando **o Usuário aleatório** é selecionado para **Pré-visualização como usuário** e não persiste nenhum usuário personalizado ou outras configurações de usuário de pré-visualização. Isso significa que se você selecionar **Usuário personalizado** e executar o Inbox Vision, o que é mostrado no Inbox Vision pode ser diferente da prévia da mensagem em outro lugar. 

Para testar sua mensagem de e-mail no Inbox Vision, faça o seguinte:

1. Acesse o editor de arrastar e soltar ou o editor de e-mail HTML. 
2. Abra a guia **Pré-visualização e teste**.
3. Selecione **Inbox Vision** e clique em **Executar Inbox Vision**. <br><br> ![][3]{: style="max-width:80%;"} <br><br> Em seguida, o Braze envia uma versão HTML de seu e-mail para vários clientes de e-mail usados em todo o mundo, o que pode levar de dois a dez minutos para ser concluído. <br><br> As prévias HTML renderizadas serão divididas em três seções: 
- **Clientes Web** 
- **Aplicativos clientes** 
- **Clientes móveis** <br><br>
4. Selecione um bloco para ver a prévia em mais detalhes. <br><br> Seu e-mail deve incluir uma linha de assunto e um domínio de envio válido para que possa ver essas prévias. Lembre-se de como seu e-mail pode ser renderizado de forma diferente no desktop e nos dispositivos móveis. Ao visualizar essas prévias, é possível revisar o conteúdo e garantir que o e-mail esteja sendo exibido como pretendido.

{% alert tip %}
Use o Inbox Vision para testar as diferenças entre os modos escuro e claro para confirmar que seus e-mails estão corretos!
{% endalert %}

![Visão geral do Inbox Vision para o editor de HTML.][1]

{: start="5"}
5\. Faça alterações em um modelo, se necessário, e clique em **Reexecutar teste** para ver as prévias atualizadas.

{% alert important %}
Em geral, seu e-mail não funcionará com o Inbox Vision se o conteúdo do e-mail depender de informações de modelo, como informações de perfil de usuário. Isso ocorre porque o Braze cria modelos em um usuário vazio quando enviamos e-mails usando esse recurso.
{% endalert %}

## Análise de código

A análise de código é uma maneira de o Braze destacar os problemas que podem existir em seu HTML, mostrando o número de ocorrências de cada problema e fornecendo insight sobre quais elementos HTML não são suportados. 

### Exibição de informações de análise de código

Essas informações podem ser encontradas na guia **Inbox Vision**, selecionando <i class="fas fa-list"></i> **List view**. Esse modo de exibição de lista está disponível apenas para modelos de e-mail em HTML. Se estiver usando modelos de e-mail do tipo arrastar e soltar, verifique as prévias para resolver possíveis problemas.

![Exemplo de análise de código na prévia do Inbox Vision.][2]

{% alert note %}
Às vezes, a análise de código será exibida mais rapidamente do que a prévia para um cliente de e-mail específico. Isso ocorre porque o Braze espera até que o e-mail chegue à caixa de entrada antes de fazer a captura de tela.
{% endalert %}

## Teste de spam

Os testes de spam tentam prever se seu e-mail chegará às pastas de spam ou às caixas de entrada de seus clientes. Os testes de spam são executados nos principais filtros de spam, como IronPort, SpamAssassin e Barracuda, bem como nos principais filtros de provedores de acesso à internet, como Gmail.com e Outlook.com.

### Exibição dos resultados do teste de spam

Para verificar os resultados do teste de spam, clique na guia **Spam Testing (Teste de spam** ) na seção **Inbox Vision (Visão da caixa de entrada** ). A tabela **Spam Test Result (Resultado do teste de spam** ) lista o nome, o status e o tipo do filtro de spam.

![Tabela "Spam Test Result" com três colunas: Nome, status e tipo. Há uma lista de filtros de spam e de provedores de acesso à internet que foram aprovados nos testes de spam, indicando que a campanha de e-mail não cairá na pasta de spam.][4]

Depois de analisar esses resultados e fazer os ajustes necessários em sua campanha de e-mail, clique em **Reexecutar teste** para recarregar os resultados do teste de spam.

## Precisão do teste

Todos os nossos testes são executados em clientes de e-mail reais. A Braze trabalha arduamente para verificar se todas as renderizações são as mais precisas possíveis. Se você sempre encontrar um problema com um cliente de e-mail, abra um [tíquete de suporte]({{site.baseurl}}/braze_support/).

[1]: {% image_buster /assets/img_archive/inboxvision1.png %}
[2]: {% image_buster /assets/img_archive/inboxvision2.png %}
[3]: {% image_buster /assets/img_archive/inboxvision4.png %}
[4]: {% image_buster /assets/img_archive/email_spam_testing.png %}
