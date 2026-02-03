---
nav_title: Landing pages
article_title: Landing pages
page_order: 31
guide_top_header: "Landing pages"
description: "Este artigo contém recursos sobre como criar e personalizar as landing pages do Braze."
alias: /landing_pages/
---

# Sobre landing pages

> As páginas de destino do Braze são páginas da web independentes que podem impulsionar sua estratégia de aquisição e engajamento de usuários.

Use páginas de destino para aumentar seu público, capturar dados de usuários, promover ofertas especiais e apoiar campanhas multicanal.

{% alert note %}
A disponibilidade de páginas de destino e domínios personalizados depende do seu pacote Braze. Entre em contato com seu gerente de conta ou gerente de sucesso do cliente para começar.
{% endalert %}

{% multi_lang_include video.html id="eg4r7agod1" source="wistia" %}

## Pré-requisitos

Antes que você possa acessar, criar e publicar páginas de destino, você precisa de permissões de administrador [permissions]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) ou de todas as seguintes permissões:

- Acessar landing page
- Criar rascunhos de landing page
- Publicar landing page

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='dnd editors' %}

## Níveis de planos

O número de landing pages publicadas e domínios personalizados que você pode usar depende do seu tipo de plano: gratuito ou pago (incremental).

| Recurso                                                                                                   | Nível gratuito     | Nível pago (incremental)     |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| Landing pages publicadas                                                                 | Cinco por empresa | 20 adicionais |
| Domínios personalizados          | Um por empresa | Cinco adicionais |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Adicionando o Google Tag Manager a uma página de destino

Para adicionar o Google Tag Manager às suas páginas de destino, adicione um bloco **Custom Code** à sua página de destino no editor de arrastar e soltar, e insira o código do Tag Manager no bloco. Certifique-se de adicionar uma camada de dados antes do código do Tag Manager, como neste exemplo:

```
<script>
window.dataLayer = window.dataLayer || [];
</script>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXX');</script>
<!-- End Google Tag Manager -->
```

Para detalhes sobre a implementação do Google Tag Manager, consulte [Google's documentation](https://developers.google.com/tag-platform/tag-manager/datalayer#installation).

## Perguntas frequentes

### Qual é o tamanho máximo das landing pages?

O tamanho do corpo da página de destino pode ser de até 500 KB.

### Há algum requisito técnico para publicar uma landing page?

Não, não há requisitos técnicos.

### Existe um editor de HTML para landing pages?

Sim. Use o bloco **Custom Code** no editor de arrastar e soltar para adicionar ou editar HTML.

### Posso criar um webhook dentro de uma landing page?

Não, isso não é suportado no momento.
