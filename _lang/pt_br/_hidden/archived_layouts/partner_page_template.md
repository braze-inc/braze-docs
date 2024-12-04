---
nav_title: Página do parceiro

page_order: 4

#Required
description: "Esta é a descrição da Pesquisa Google. Caracteres com mais de 160 caracteres são truncados, portanto, seja breve."
page_type: partner
tool:
  - Dashboard
  - Docs
  - Canvas
  - Campaigns
  - Segments
  - Templates
  - Media
  - Location
  - Currents
  - Reports

platform:
  - iOS
  - Android
  - Web
  - API

channel:
  - Content Cards
  - Email
  - News Feed
  - In-App Messages
  - Push
  - SMS
  - Webhooks
  
noindex: true
#ATTENTION: remove noindex and this alert from template

---

# [Nome do parceiro]

> Bem-vindo ao modelo de página de parceiro! Aqui, você encontrará tudo o que precisa para criar sua própria página de parceiro. Nesta primeira seção, você deve descrever o parceiro no primeiro parágrafo em uma ou duas frases. Além disso, inclua um link para o site principal do parceiro.

No segundo parágrafo, você deve explorar e explicar o relacionamento entre a Braze e esse parceiro. Esse parágrafo deve explicar como a Braze e esse parceiro trabalham juntos para estreitar o vínculo entre o usuário Braze e seu cliente. Explique a "elevação" que ocorre quando um usuário Braze se integra ou utiliza esse parceiro e seus serviços.

## Requisitos ou pré-requisitos

Esta seção trata do que é necessário para fazer a integração com o parceiro e começar a usar os serviços dele. A melhor maneira de fornecer essas informações é com um parágrafo instrutivo rápido que descreva todos os detalhes importantes não técnicos das informações que "precisam ser conhecidas", como se a sua integração estará ou não sujeita a verificações ou autorizações de segurança adicionais. Em seguida, você deve usar um gráfico para descrever os requisitos técnicos da integração.

{% alert important %}
Os requisitos a seguir são requisitos típicos que você pode precisar do Braze. Recomendamos o uso de atribuição de título, origem, links e frases conforme listado na tabela a seguir. Certifique-se de ajustar a descrição para que você saiba para que serve cada um desses requisitos.
{% endalert %}

| Requisito | Origin | Acesso | Descrição |
|---|---|---|---|
|Chave da API REST do espaço de trabalho do Braze | Plataforma Braze | Página **Configurações** > **Chave de API**  | Essa descrição deve dizer o que fazer com a chave da API REST do espaço de trabalho. |
|Ponto de extremidade da API do Braze | Plataforma Braze | Confira nossos [endpoints listados]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) ou abra um [ticket de suporte]({{site.baseurl}}/braze_support/). | Descrição pendente. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## [Tipo de integração] Integração

É aqui que você divide a integração em etapas. Não escreva apenas parágrafos intermináveis - esses são documentos técnicos que serão usados por profissionais de marketing e desenvolvedores para colocar a integração em funcionamento. Seu único objetivo nesta seção é escrever uma documentação descritiva que ajude o usuário do Braze a realizar o trabalho. Por "Tipo de integração" no título da seção, queremos indicar se é ou não uma integração lado a lado, de servidor para servidor ou fora da caixa. Isso permite que você tenha várias seções de integração se houver mais de uma maneira de integrar com este parceiro.

Se essa for uma integração do Currents, essa página deverá estar localizada na seção Currents e deverá ser criada uma página de navegação correspondente que redirecione para esse local no Currents.

### Etapa 1: Esta é uma breve descrição da primeira etapa

Basta detalhar isso, incluindo qualquer código, conforme necessário. Lembre-se de que você pode oferecer vários conjuntos diferentes de códigos - não há necessidade de oferecer apenas uma forma de integração.

### Etapa 2: Esta etapa descreverá as imagens

Você tem a opção de colocar imagens em sua documentação, por isso recomendamos que o faça e que o faça com cuidado.

### Etapa 3: Quantas etapas

Descreva o uso da integração, especialmente se isso significar inserir o Liquid em nosso criador de mensagens.

## Personalização

Esta é uma seção **opcional**. Aqui, você pode delinear quaisquer maneiras específicas de personalizar sua integração com os dois parceiros.

## Uso dessa integração

Isso deve descrever como usar a integração - informe ao seu leitor se ele precisará pressionar alguns botões ou se não precisará fazer nada após a integração.

### Etapa 1: Esta é uma breve descrição da primeira etapa

Apenas o típico passo a passo de como fazer.

## Casos de uso

Essa pode ser uma parte essencial de sua documentação. Embora seja opcional, este é um bom lugar para detalhar casos de uso típicos ou até mesmo novos para a integração. Isso pode ser usado como uma forma de vender ou aumentar o relacionamento - ele fornece contexto, ideias e, o mais importante, uma forma de visualizar os recursos da integração.
