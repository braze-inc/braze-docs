---
nav_title: Storyly
article_title: Storyly
description: "Este artigo de referência descreve a parceria entre a Braze e a Storyly, um SDK leve, que permite aos proprietários de aplicativos direcionar seus segmentos e alimentar a Braze com mais dados primários."
alias: /partners/storyly/
page_type: partner
search_tag: Partner

---

# Storyly

> A [Storyly](https://www.storyly.io/) é um SDK leve que leva histórias para seu app ou site. Com um estúdio de design intuitivo, análises relevantes e conectividade prática, o Storyly é uma ferramenta poderosa para enriquecer a experiência do público. 

_Essa integração é mantida pela Storyly._

## Sobre a integração

A integração entre o Braze e o Storyly permite que você use seus segmentos no Braze como um público na plataforma Storyly. Com essa integração, você pode:
- Direcionamento de seus segmentos com histórias específicas
- Use as atribuições do usuário para personalizar o conteúdo do seu story

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Storyly | É necessário ter uma conta no Storyly para aproveitar essa parceria. |
| Storyly SDK | Você deve instalar o [Storyly SDK](https://integration.storyly.io/). |
| Chave da API REST do Braze | Uma chave da API REST do Braze com as seguintes permissões <br><br> `users.export.ids`<br> `users.export.segments`<br> `segments.list`<br> `segments.details` <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST do Braze | [Sua URL de endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Seu endpoint dependerá do URL do Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

Com a integração do Braze e do Storyly, os proprietários de aplicativos podem mostrar histórias para todos os segmentos no Braze e personalizar as histórias com atribuições do usuário.

Alguns casos de uso comuns incluem:

__Direcione segmentos da Braze na Storyly__<br>Após a conclusão da integração, você poderá criar um público do Storyly com base em seus segmentos do Braze. Esse pode ser um segmento demográfico ou comportamental. Por exemplo, direcione os usuários que moram em um local específico, aqueles que realizam uma ação específica em seu app ou aqueles interessados em produtos específicos com histórias específicas para aumentar a conversão.<br>
__Histórias personalizadas com atribuições do usuário__<br>As atribuições do usuário do Braze também podem ser usadas no Storyly para gerar histórias dinâmicas. Isso pode incluir o nome de um usuário, produtos em uma cesta ou até mesmo produtos favoritos, fornecendo aos usuários histórias personalizadas exclusivas. A personalização ajuda a aumentar as taxas de conversão nas histórias e a taxa geral de engajamento nas histórias.

## Integração de exportação de dados

A integração entre a Braze e a Storyly é explicada no vídeo a seguir:

{% multi_lang_include video.html id="3-OEqQs48Zw" source="youtube" %}

Certifique-se de que sua integração com o Storyly contenha parâmetros personalizados. Esses parâmetros serão combinados com a propriedade do usuário `external id` da Braze. A implementação de parâmetros personalizados é explicada aqui para [iOS](https://integration.storyly.io/ios/personalization-customaudience.html), [Android](https://integration.storyly.io/android/personalization-customaudience.html), [React Native](https://integration.storyly.io/react-native/personalization-customaudience.html), [Flutter](https://integration.storyly.io/flutter/personalization-customaudience.html) e [Web](https://integration.storyly.io/web/personalization-customaudience.html).

Você também pode consultar a documentação [do Storyly](https://docs.storyly.io/page/connect-your-braze-audiences-with-storyly) para obter mais informações.

### Etapa 1: Defina a integração no dashboard do Storyly

Uma integração pode ser criada no **Storyly Dashboard > Configurações > Integrações > Conectar com o Braze**. Aqui você precisará da sua chave da API REST da Braze e do endpoint REST da Braze. 

### Etapa 2: Obtenha seus segmentos 

Em seguida, você pode usar os segmentos da Braze para criar um público da Storyly. Isso pode ser criado em **Storyly Dashboard > Settings > Audiences > New Audience > Create Audience with Braze** (Dashboard da Storyly > Configurações > Públicos > Novo público > Criar público com Braze).

Aqui, haverá duas opções de sincronização. Selecione **One-time sync (Sincronização única** ) para histórias de campanhas específicas ou **Daily Sync (Sincronização diária** ) para histórias de longo prazo.


