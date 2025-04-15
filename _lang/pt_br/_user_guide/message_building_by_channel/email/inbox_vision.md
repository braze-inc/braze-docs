---
nav_title: Inbox Vision
article_title: Inbox Vision
page_order: 9
description: "Esta página cobre como configurar o Inbox Vision, um recurso que permite aos profissionais de marketing visualizar seus e-mails a partir da perspectiva de vários clientes de e-mail e dispositivos móveis."
tool:
  - Dashboard
channel:
  - email

---

# Inbox Vision

> O Inbox Vision permite visualizar seus e-mails a partir da perspectiva de vários clientes de e-mail e dispositivos móveis. Por exemplo, você pode usar o Inbox Vision para testar as diferenças entre os modos escuro e claro para confirmar que seus e-mails estão exatamente certos.

{% alert important %}
Em geral, seu e-mail não funcionará com o Inbox Vision se o conteúdo do seu e-mail depender de informações de modelagem, como informações do perfil do usuário. Isso ocorre porque o Braze cria modelos em um usuário vazio quando enviamos e-mails usando esse recurso.
{% endalert %}

## Teste seu envio de e-mail no Inbox Vision

Seu e-mail deve incluir uma linha de assunto e um domínio de envio válido para que possa ver essas prévias. Lembre-se de como seu e-mail pode ser renderizado de forma diferente no desktop e nos dispositivos móveis. Ao visualizar essas prévias, é possível revisar o conteúdo e garantir que o e-mail esteja sendo exibido como pretendido.

Para testar sua mensagem de e-mail no Inbox Vision, faça o seguinte:

1. Acesse o editor de arrastar e soltar ou o editor de e-mail HTML.
2. No seu editor, selecione **Ver prévia e testar**.
3. Selecione **Inbox Vision**. 
4. Selecione **Executar Inbox Vision**. Isso pode levar entre dois a dez minutos para ser concluído.
5. Em seguida, selecione um tile para visualizar a prévia com mais detalhes. Essas prévias estão agrupadas nessas seções: **Clientes Web**, **Clientes de Aplicativo** e **Clientes Móveis**.

![Visão geral do Inbox Vision para o editor de HTML.][1]

{: start="6"}
6\. Faça alterações em um modelo, se necessário.
7\. Selecione **Refazer teste** para ver as prévias atualizadas.

### Visualizando como um usuário

Quando você faz uma prévia do e-mail como um usuário aleatório, quaisquer configurações ou atributos específicos associados a um usuário, como seu nome ou preferências, não são salvos para prévias atuais ou futuras. Quando você seleciona um usuário personalizado, a prévia exibida no Inbox Vision pode diferir da prévia da mensagem em outros lugares, uma vez que esta opção utiliza dados de usuários específicos para criar a prévia.

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

Para verificar os resultados do seu teste de spam, faça o seguinte:

1. Selecione a guia de **Teste de spam** na seção **Inbox Vision**. A tabela **Spam Test Result (Resultado do teste de spam** ) lista o nome, o status e o tipo do filtro de spam.

![Tabela "Spam Test Result" com três colunas: Nome, status e tipo. Há uma lista de filtros de spam e de provedores de acesso à internet que foram aprovados nos testes de spam, indicando que a campanha de e-mail não cairá na pasta de spam.][4]

{: start="2"}
2\. Revise esses resultados e faça os ajustes necessários na sua e-mail campanha.
3\. Selecione **Refazer teste** para recarregar os resultados do seu teste de spam.

## Precisão do teste

Todos os nossos testes são executados em clientes de e-mail reais. A Braze trabalha arduamente para verificar se todas as renderizações são as mais precisas possíveis. Se você sempre encontrar um problema com um cliente de e-mail, abra um [tíquete de suporte]({{site.baseurl}}/braze_support/).

[1]: {% image_buster /assets/img_archive/inboxvision1.png %}
[2]: {% image_buster /assets/img_archive/inboxvision2.png %}
[3]: {% image_buster /assets/img_archive/inboxvision4.png %}
[4]: {% image_buster /assets/img_archive/email_spam_testing.png %}
