---
nav_title: Adikteev
article_title: Previsão de churn do Adikteev
description: "Este artigo de referência descreve a parceria entre o Braze e a Adikteev, um mecanismo de retenção de usuários que combina a previsão de churn com o redirecionamento de aplicativos full-service."
alias: /partners/adikteev/
page_type: partner
search_tag: Partner

---

# Previsão de churn do Adikteev

> A [Adikteev](https://www.adikteev.com/churn-prediction) é um mecanismo de retenção de usuários que combina a previsão de churn com o redirecionamento de aplicativos full-service.

_Essa integração é mantida por Adikteev._

## Sobre a integração

A integração entre o Braze e a Adikteev permite aumentar a retenção de usuários, aproveitando a tecnologia de previsão de churn da Adikteev nas campanhas do Braze CRM para direcionar prioritariamente os segmentos de usuários de alto risco.

## Pré-requisitos

| Requisito | Descrição |
| --- | --- |
| Conta da Adikteev | É necessário ter uma conta Adikteev para aproveitar essa parceria. |
| Chave da API REST do Braze | Uma chave da API REST do Braze com a permissão `users.track`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **APIs e identificadores**. |
| Ponto de extremidade REST do Braze | [Sua URL de endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Seu endpoint dependerá do URL do Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

{% tabs %}
{% tab Filtragem de público %}
Refinamento de seus segmentos de público com base no risco de churn.<br> Os nomes e valores dos atributos personalizados enviados pelo Adikteev são configuráveis.

![Uma captura de tela mostrando um exemplo de como usar um atributo personalizado enviado pelo Adikteev como um filtro de segmento de público.]({% image_buster /assets/img/adikteev/audience.png %})
{% endtab %}
{% tab Direcionamento de mensagens %}
Personalização de suas campanhas de mensagens do Braze com base no risco de churn dos destinatários.

![Uma captura de tela mostrando um exemplo de como usar um atributo personalizado enviado pelo Adikteev como um filtro de direcionamento de campanha.]({% image_buster /assets/img/adikteev/campaign.png %})
{% endtab %}
{% endtabs %}

## Integração

### Etapa 1: Compartilhe o fluxo de eventos do seu app

Para começar a executar a previsão de churn no público do seu app, o Adikteev precisará que você ative os postbacks de eventos da sua plataforma de medição móvel. Siga as diretrizes no [site de suporte da Adikteev](https://help.adikteev.com/hc/en-us/sections/8185123408914-Data-stream-activation) para configurar isso.

### Etapa 2: Crie sua chave da API REST do Braze

Na Braze, navegue até **Configurações** > **APIs e identificadores**. Selecione **Criar nova chave de API**, digite o nome da chave de API de sua escolha e verifique se a permissão a seguir foi adicionada:

- `users.track`

### Etapa 3: Fornecer informações à equipe da Adikteev

Para concluir a integração, você deve fornecer sua chave de API REST e o URL do ponto de extremidade REST ao gerente de sua conta do Adikteev. A Adikteev estabelecerá a conexão e entrará em contato com você após a conclusão da configuração para validar a integração.

## Loteamento e limites de frequência

O ponto de extremidade `user.track` é usado para atualizar detalhes sobre seus usuários. Consulte a [documentação da API]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para obter detalhes completos sobre os limites de frequência do ponto de extremidade, solicitações em lote e detalhes da solicitação.

{% alert tip %}
Lembre-se de que as chamadas de API devem ser feitas apenas para atualizar dados que foram alterados, a fim de reduzir o número total de chamadas. Em outras palavras, atualize apenas os usuários cujo segmento de churn foi alterado.
{% endalert %}

## Identificadores de usuários e dispositivos

Os perfis de usuário no Braze podem ser associados a qualquer tipo de identificador de usuário ou dispositivo; a lista de opções disponíveis depende de como você integrou a coleta de dados ao Braze. Para o Adikteev, será necessário encontrar um identificador comum entre o MMP e os perfis de usuário no Braze para enviar as informações do segmento de churn corretamente.

## Retenção e exclusão de dados

Se nenhuma atualização for feita, a atribuição e seu valor serão mantidos indefinidamente nos perfis de usuário do Braze.

Para remover uma atribuição de perfil, defina-a como `null`.

## Cargas úteis de solicitação

A carga útil enviada da Adikteev para o Braze é personalizável e pode ser configurada para atender às necessidades do cliente. Isso inclui a configuração dos identificadores usados, o nome do atributo personalizado e se o Adikteev pode criar novos usuários no Braze ou apenas atualizar os usuários existentes.


## Suporte e solução de problemas

Entre em contato com o gerente de contas da Adikteev para tirar dúvidas relacionadas à integração ou para obter suporte para seus casos de uso.

