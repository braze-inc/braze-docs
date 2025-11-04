---
nav_title: Stylitics
article_title: Stylitics
description: "Este artigo de referência descreve a parceria entre a Braze e a Stylitics, uma plataforma SaaS baseada em nuvem que permite aprimorar suas campanhas de e-mail existentes com conteúdo agrupado envolvente e relevante, criando uma experiência personalizada para o cliente."
alias: /partners/stylitics/
page_type: partner
search_tag: Partner

---

# Stylitics

> A [Stylitics](https://stylitics.com/) é uma plataforma SaaS baseada em nuvem para varejistas automatizarem e distribuírem conteúdo visual em escala. Os pacotes da Stylitics inspiram ao contextualizar produtos, aumentando a confiança na compra e elevando o engajamento. Isso gera um maior valor médio de pedido e taxas de conversão mais elevadas.

_Essa integração é mantida pela Stylitics._

## Sobre a integração

Sua integração entre a Braze e a Stylitics permite melhorar suas campanhas de e-mail existentes com conteúdo envolvente e relevante, criando uma experiência personalizada para o cliente.

![]({% image_buster /assets/img/stylitics.png %}){: style="max-width:60%;"}

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Stylitics | Uma conta [Stylitics](https://stylitics.com/) é necessária para aproveitar esta parceria. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

A seguir estão alguns exemplos comuns de programas de e-mail acionados:
- Emails de carrinho abandonado 
- Emails de navegação abandonados 
- E-mails de confirmação de envio
- E-mails pós-compra 

## Integração

Stylitics fornece dados de pacote para esta integração. Seu prestador de serviço de e-mail pode criar ou atualizar o modelo de e-mail para incluir pacotes Stylitics. A Stylitics não pode alterar o layout ou o design dos e-mails. 

1. Integre o pacote ao e-mail. ESP determina a posição e a personalização.
2. O provedor de serviços de e-mail atualiza o código de disparo de e-mails para incluir o conteúdo da Stylitics.
3. O provedor de serviços de e-mail testará, fará a prévia e lançará a série de atualizações acionadas. 

A Stylitics fornecerá apenas os dados do pacote para os itens. Entre você e seu ESP, você terá dados de usuários e poderá conectar dados do pacote Stylitics para enviar aos usuários.

## Troca de dados

As três abordagens a seguir permitem incluir pacotes da Stylitics nos seus e-mails acionados.

### 1\. abordagem de API (recomendada)

Você ou seu ESP podem fazer uma chamada de API por item para preencher os dados do pacote no seu e-mail. A Stylitics recomenda usar a API dela para fazer chamadas de API, pois está pronta para uso imediato.

{% alert note %}
Se você executar um teste A/B gerenciado pelo Stylitics, os parâmetros `styliticsCID` e `styliticsoverride` devem ser anexados aos URLs do PDP dos itens do Stylitics em que o usuário clica no e-mail.
<br><br>
Por exemplo, {% raw %}`&styliticsoverride=001?styliticsCID=email[clientname]`{% endraw %}
{% endalert %}

### 2\. Abordagem de arquivo plano
Você ou seu ESP podem referenciar os dados do pacote de um item em um arquivo plano para preencher os dados do pacote em seu e-mail. A Stylitics pode mesclar dados de pacotes em formato CSV, TXT ou XML e enviá-los para você diariamente. Eles também podem ajudar a ajustar o formato do arquivo conforme as necessidades do seu ESP. Note que a criação do arquivo leva de duas a três semanas.

#### Requisitos:
- **Local**: a Stylitics pode disponibilizar o arquivo no SFTP da Stylitics para você baixá-lo diariamente, ou você pode enviar suas credenciais de SFTP para eles fazerem upload do arquivo. 
- **Tempo**: a Stylitics disponibiliza o arquivo de manhã diariamente. Avise-os caso precise do arquivo em um horário específico do dia. 
- **Chave do arquivo**: Você e a Stylitics precisam concordar sobre qual string de dados do item usar como chave do arquivo para que seu ESP possa referenciar os dados. SKU, `item_group_id`, ou `item_number` são comumente usados. 

### 3\. Abordagem de extração de dados do site
Os fornecedores podem raspar a interface do seu site para conteúdo da Stylitics e inserir dados de pacotes em e-mails. Nenhum trabalho adicional da Stylitics é necessário. 

## Melhores práticas de modelo de e-mail 

Você e seu ESP criarão um modelo de e-mail HTML para inserir dados e pacotes do Stylitics. Aqui estão algumas melhores práticas e recomendações. 
- Exibir 2-4 pacotes no e-mail para o item mais caro ou primeiro item a preço cheio que o usuário comprou ou interagiu 
- Chame vários `item_numbers` e mostre a primeira resposta do pacote 
- Tenha uma opção de fallback se não houver pacotes disponíveis para o item 
	- Oculte a seção onde os pacotes da Stylitics ficam 
	- Mostrar pacotes para o próximo item que o usuário visualizou 
- Exibir imagens do pacote e uma lista de títulos de produtos e imagens em miniatura para garantir que o usuário tenha cliques claros

{% alert note %}
O JavaScript do widget da Stylitics não pode ser inserido em e-mails, pois os e-mails não suportam JavaScript.
{% endalert %}

## Análise de dados

A Stylitics fornece os dados do pacote para este tipo de programa de e-mail. Portanto, pedimos um compartilhamento de dados aberto entre você, seu provedor de serviços de e-mail e a Stylitics. Se possível, esperamos receber as seguintes métricas de você para entender o aumento e melhorar o programa:
- Emails enviados 
- Emails abertos 
- Visualizações e engajamentos 
- Taxa de cliques 
- Adição aos carrinhos 
- Compras

## Próximos passos 

Entre em contato com o gerente de conta da Stylitics para coordenar os próximos passos e prazos para o programa de e-mail. Alguns próximos passos incluem: 
- Decida quais e-mails você gostaria de usar
- Conecte a Stylitics com seu ESP para discutir a troca de dados e decidir entre a opção de API ou a opção de arquivo flat 
- Crie mockups com seu ESP 
- Alinhar na análise de dados 
- Obter alinhamento em relação ao cronograma de lançamento 


