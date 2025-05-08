---
nav_title: Ada
article_title: Ada
description: "Este artigo de referência descreve a parceria entre a Braze e a Ada, uma plataforma baseada em IA que automatiza e personaliza as interações com os clientes. Essa integração permite aumentar os perfis de usuários com dados coletados de suas conversas automatizadas com a Ada."
alias: /partners/ada/
page_type: partner
search_tag: Partner

---

# Ada

> [A Ada](https://ada.cx) é uma plataforma de interação com a marca que automatiza e personaliza a experiência do cliente usando IA conversacional. Use a Ada para adaptar seu envio de mensagens e segmentar campanhas com base em dados de usuários, medir e analisar conversas para descobrir novas oportunidades e usar insights de bate-papo com clientes para enriquecer seus perfis de usuários.  

A integração do Braze e da Ada permite aumentar os perfis de usuários com dados coletados de suas conversas automatizadas com a Ada. É possível definir atributos personalizados do usuário com base nas informações coletadas durante um chat Ada e registrar eventos personalizados no Braze em pontos específicos de uma conversa Ada. Ao conectar seu chatbot Ada ao Braze, você pode saber mais sobre seus consumidores com base nas perguntas que eles fazem sobre sua marca ou iniciando proativamente conversas com eles, fazendo perguntas que lhe permitam saber mais sobre seus interesses e preferências.

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Ada | É necessário ter uma conta [Ada](https://ada.cx) com os aplicativos Braze e Answer Utilities ativados para aproveitar essa parceria. |
| Chave da API REST do Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST do Braze | [Seu URL do ponto de extremidade REST][1]. Seu endpoint dependerá do URL do Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

Os casos de uso comuns para a integração da Braze e da Ada incluem:
- Rastreamento de diferentes interações que seus consumidores têm com o bot Ada como eventos personalizados no Braze, para que você saiba quais clientes se engajaram com campanhas proativas na Ada, foram entregues a agentes de suporte, fizeram perguntas específicas ou concluíram determinadas ações.
- Perguntar aos seus consumidores sobre seus interesses, preferências, dados demográficos e muito mais. Atualize seu perfil no Braze automaticamente com essas novas informações usando atributos personalizados.

## Integração

Para integrar a Braze e a Ada, primeiro é necessário configurar o aplicativo Braze no dashboard da Ada e trabalhar com a equipe da Ada para configurar uma metavariável de ID de usuário no script de incorporação da Ada. Em seguida, você arrastará o bloco da Braze para o local do editor de respostas de onde quer enviar informações, como um evento ou uma atribuição, de volta à Braze.

### Etapa 1: Configure o app Braze no Ada

No dashboard da Ada, acesse **Settings > Integrations > Handoff Integrations** (Configurações > Integrações > Integrações de Handoff).

Ao lado de Braze, clique em **Connect (Conectar** ) e forneça as seguintes informações:
- **Ponto de extremidade REST**: digite o URL do ponto de extremidade REST do Braze. 
- **Chave da API**: digite sua chave da API REST do Braze. 
- **ID do** app: digite o ID do app ao qual deseja associar os Ada chatters.

### Etapa 2: Passar um identificador do Braze para o Ada

Para confirmar que está atualizando o usuário correto, será necessário entrar em contato com a equipe da Ada, que poderá ajudá-lo a fazer as modificações necessárias no script de incorporação da Ada para receber um identificador do Braze. Essa integração foi projetada para aceitar um ID externo, mas é possível passar outros identificadores, como um alias de usuário. 

### Etapa 3: Coloque o bloco Braze nas respostas relevantes

Para usar o bloco da Braze, arraste-o da gaveta de blocos para a resposta apropriada e selecione uma ação. Com o bloco da Braze, você pode realizar duas ações:
* Evento de rastreamento
* Atualizar atribuição

{% tabs local %}
{% tab evento de rastreamento %}

#### Resposta Bloco de utilidades

1. Arraste o bloco de utilidades de resposta da gaveta de blocos para a posição diretamente acima do bloco da Braze. 
2. Selecione a ação **Formatar data** e digite `today` no campo **Data**.
3. Digite `iso` no campo **Output Format (Formato de saída** ). Em **Save Response As Variable (Salvar resposta como variável**), crie uma variável para **Formatted Date (Data formatada)** chamada `iso_time`.

![O bloco de utilidades de resposta com campos preenchidos conforme descrito no texto anterior.]({% image_buster /assets/img/ada/ada-braze-2.png %})

#### Bloco da Braze

**4\.** No bloco Braze, digite a metavariável `external_id` configurada pela Ada na etapa anterior no campo **External ID**.<br>
**5\.** No campo **Event Name** (Nome do evento), digite o nome do evento da Braze que deseja rastrear.<br>
**6\.** No campo **Time of Event (Hora do evento** ), digite a variável `iso_time` que você criou no bloco Answer Utilities (Utilitários de resposta).<br>
**7\.** Selecione uma resposta fallback para aparecer se ocorrer um problema ao publicar o evento no Braze.

![O bloco Braze com campos preenchidos conforme descrito no texto anterior.]({% image_buster /assets/img/ada/ada-braze-3.png %})

{% endtab %}
{% tab atributo de atualização %}

#### Bloco da Braze

1. No bloco Braze, digite a metavariável `external_id` configurada pela Ada na etapa anterior no campo **External ID**. 
2. No campo **Attribute Name** (Nome do atributo), digite o nome do atributo da Braze que deseja rastrear. 
3. No campo **Attribute Value (Valor da atribuição** ), digite o valor que deseja definir, que pode ser um texto, uma variável ou uma combinação de texto e variáveis. 
4. Selecione uma resposta fallback para aparecer se ocorrer um problema ao postar o atributo no Braze.

![O bloco Braze com campos preenchidos conforme descrito no texto anterior.]({% image_buster /assets/img/ada/ada-braze-4.png %})

{% endtab %}
{% endtabs %}

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/ada/ada-braze-1.png %}
[3]: {% image_buster /assets/img/ada/ada-braze-2.png %}
[4]: {% image_buster /assets/img/ada/ada-braze-3.png %}
[5]: {% image_buster /assets/img/ada/ada-braze-4.png %}