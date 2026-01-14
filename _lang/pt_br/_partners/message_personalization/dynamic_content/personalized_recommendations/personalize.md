---
nav_title: Personalize.AI
article_title: Personalize.AI
description: "Este artigo de referência descreve a parceria entre a Braze e a Personalize.AI, uma plataforma de negócios SaaS baseada em IA que impulsiona o crescimento da receita a partir de recomendações personalizadas."
alias: /partners/personalize_ai/
page_type: partner
search_tag: Partner
---

# Personalize.AI

> A [Personalize.AI](https://www.zs.com/solutions/artificial-intelligence-and-analytics/personalize-ai/) faz parceria com a Braze para gerar receita incremental ao entregar mensagens e ofertas personalizadas enviadas através da Braze. 

A integração entre a Braze e a Personalize.AI permite exportar dados da Personalize.AI para a plataforma Braze para personalização e direcionamento de mensagens.

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Personalize.AI instância | Uma Personalize.AI instância é necessária para aproveitar esta parceria. |
| Chave da API REST do Braze | Uma chave da API REST do Braze com todas as permissões. <br><br>Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Ponto de extremidade REST do Braze | Sua URL de endpoint REST. Seu endpoint dependerá da [URL do Braze para sua instância]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

* Implantar testes, incluindo estratificação flexível, para obter resultados a partir do feedback do cliente
* Forneça recomendações personalizadas para itens e ofertas, incluindo tratamento, tempo e conteúdo
* Identifique objetivos prioritários e direcione seu público ideal através do Braze
* Identificar oportunidades para reengajar usuários inativos
* Aproveite os dados de geolocalização para encontrar o público certo para os novos locais abertos
* Use a modelagem de sósias para construir com base nos dados limitados disponíveis para novos usuários, combinando-os com as recomendações mais relevantes
* Identifique as maneiras corretas de engajar os clientes ao longo de seu ciclo de vida 
* Avalie proativamente os clientes quanto à probabilidade de churn e atribua uma pontuação de risco para encontrar indicadores precoces de churn
* Alvo clientes com intervenções personalizadas para evitar que se tornem inativos

## Integração

### Configure uma conexão com a Braze em Personalize.AI

1. Em Personalize.AI, navegue até a guia **Integrações**, localizada em **Operacionalização**, na sua instância de Personalize.AI.
2. Clique em **Braze**. 
3. Configure sua integração com a Braze.
    * **Nome da conexão (Nome da conexão):** dê um nome para sua conexão. É assim que sua integração será referida na Personalize.AI.
    * **Frequência de Sincronização:** a frequência de sincronização controla com que frequência a Personalize.AI exporta dados para a Braze. Selecione **Diariamente**, **Semanalmente**, ou **Mensalmente**. 
    * **chave de API:** Adicione sua chave de API da Braze.
    * **URL DA API:** Adicione seu URL de endpoint REST do Braze.
4. Clique em **EXPORTAR** para exportar dados para a Braze.

Depois que seus dados forem exportados, Personalize.AI continuará a passar dados para a Braze nos intervalos determinados pela frequência de sincronização que você definiu durante a integração.

## Usando essa integração

Personalize.AI exporta identificadores usados para direcionamento personalizado no Braze. Esses atributos personalizados indicam tempo, conteúdo, tratamento e ofertas para cada cliente. Dependendo da integração, os campos podem ser passados como um evento ou puxados para as [APIs de Conteúdo Conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/public_apis/) em vez de armazenados no perfil do cliente. Personalize.AI suporta o uso de `external_id` como um identificador.

Os atributos de dados importados para a Braze são intuitivamente nomeados para uso em canvas, seguindo uma terminologia consistente. Por exemplo, o atributo `C402_Target_Variant` em Personalize.AI seria exportado para a Braze como `"P.AI_Model_Treatment"`. Os atributos exportados de Personalize.AI são projetados para não interferir com quaisquer atributos existentes ou rastreamento do seu uso. Esses atributos são validados continuamente para confirmar que você pode referenciá-los com confiança. 

Por exemplo, aqui está um conjunto de atributos de clientes conforme eles se relacionam a um exemplo de canva focado em churn.

| Personalize.AI atributo | Valor |
| ----------- | ------------- | 
| `Customer_ID` | 12345 |
| `Target_Canvas` | C4 |
| `Target_Objective` |  "Churn_Mitigation" |
| `C4_Target_Date` | 01/03/2023 |
| `C4_Target_Variant` | Tratamento |
| `C4_Treatment` | P.IA_Model |
| `C4_Offer_Value` | R$ 8 |
| `C4_Item_Recom` | Salada caesar |
| `C4_Subject_Line` | Sentimos sua falta |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


