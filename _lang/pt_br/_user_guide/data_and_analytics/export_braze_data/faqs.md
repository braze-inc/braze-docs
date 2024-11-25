---
nav_title: Perguntas frequentes
article_title: Exportar FAQ
page_order: 11
page_type: FAQ
description: "Este artigo cobre algumas perguntas frequentes sobre API e exportações CSV."

---

# Perguntas frequentes

> Esta página fornece respostas para algumas perguntas comuns sobre API e exportações CSV.

### Você pode fazer com que certas exportações apareçam no seu bucket S3 e outras não?

Não. Se você forneceu credenciais do bucket S3, todas as suas exportações aparecerão no seu bucket S3; caso contrário, se nenhuma credencial for fornecida, todas as exportações aparecerão em um bucket S3 pertencente à Braze.

### Preciso adicionar credenciais S3 à Braze para exportar dados?

Não. Se você não adicionar credenciais S3, suas exportações aparecerão em um bucket S3 pertencente ao Braze.

### O que acontece se você configurar as credenciais do S3 no dashboard, mas não selecionar "Tornar este o destino padrão de exportação de dados"?

A caixa de seleção **Tornar este o destino padrão de exportação de dados** afeta o fato de as exportações irem para o S3 ou para o Azure, supondo que você tenha adicionado credenciais para ambos.

### Por que recebi vários arquivos ao exportar perfis de usuários para o S3?

Este é o comportamento esperado para espaços de trabalho com muitos usuários. Braze dividirá sua exportação em vários arquivos com base no número de usuários em seu espaço de trabalho. Geralmente, há um arquivo de saída para cada 5.000 usuários. Nota que se você estiver exportando um pequeno segmento dentro de um grande espaço de trabalho, ainda poderá receber vários arquivos.

### Por que vejo duplicatas quando exporto usuários por segmento por meio da API REST?

Essa é uma ocorrência muito rara causada pela arquitetura subjacente do provedor de banco de dados. Os duplicados são limpos toda semana; no entanto, na maioria das semanas, nenhum duplicado é removido.
