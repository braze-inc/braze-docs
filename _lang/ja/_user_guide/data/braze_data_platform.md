---
nav_title: Braze データプラットフォーム
article_title: Brazeデータプラットフォームの概要
page_order: 0
page_type: reference
description: "ここでは、Brazeデータプラットフォームに関連する記事について説明します。" 
---

# Brazeデータプラットフォームの概要

> Braze データプラットフォームは、包括的で構成可能な一連のデータ機能とパートナー連携で、実行する3 つのデータ関連ジョブに基づいて、カスタマーライフサイクル全体にパーソナライズされたでインパクトのあるエクスペリエンスを作成できます。[データ統合]({{site.baseurl}}/user_guide/data/unification)、[データアクティベーション]({{site.baseurl}}/user_guide/data/activation)、および[データ分散]({{site.baseurl}}/user_guide/data/distribution)。

Braze データプラットフォームの機能を組み合わせることで、データを活用して、顧客がリアルタイムで行うことに対応する、意味のあるターゲットメッセージを作成できます。

## データの統一 

[API]と[SDK s]を使用して、任意のソースからファーストパーティデータを収集し、統合します。[Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) などの組み込みの取り込みツールを使用して、データウェアハウスまたはファイルストレージソリューションからBraze への直接統合を作成したり、[Data Transformation]({{site.baseurl}}/user_guide/data/unification/data_transformation) を使用して、Braze にデータを転送するためのWebhook統合を構築および管理したりすることもできます。

## データを有効にする

データのクリーンアップ、整理、および使用準備を行います。これには、顧客の振る舞いや好みをユーザープロファイルs とSegments でリアルタイムに把握することが含まれます。ターゲットメッセージを作成するときに、[メトリクス用語集]({{site.baseurl}}/user_guide/data/activation/report_metrics)をレポートして、顧客がこれらのパーソナライズされたエクスペリエンスにどのように対応しているかを確認します。

## データを配布する

データをストリーミングして外部システムにエクスポートし、ネクストステップ インサイトのs および決定を行います。[Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)を使用して、Brazeのイベントデータをデータウェアハウスにストリーミングし、ビジネスインテリジェンスに電力を供給します。
