---
nav_title: Overview
article_title: Braze Pilot Overview
page_order: 1
page_type: reference
description: "This reference article briefly covers the integration steps required from your engineers or developers."
---

# Braze Pilot overview

> This page introduces the core concepts you’ll need to know when working with Braze Pilot.

Braze Pilot is a mobile app that is designed to connect seamlessly with your Braze dashboard. This allows you to launch campaigns and Canvases to the app to see Braze messages come to life on your own phone. Pilot includes a library of app simulations for fictional brands representing different industries, which allows you to experience how your messaging might look from your consumers’ perspective.

## Pilot app simulations

The core of Braze Pilot is its library of app simulations. Each app is a realistic simulation of an industry-specific fictional brand, instrumented to log a rich assortment of events and attributes that create endless opportunities for powering common Braze use cases.

### Steppington

Steppington is a fitness app with workouts, exercise goals, and a Steppington+ premium service. It offers several places to demonstrate Content Cards, a section that can be revealed with Feature Flags, and a robust library of custom event logging that make it possible to illustrate many customer journeys for this industry.

### PantsLabyrinth

PantsLabyrinth is an eCommerce app that sells (you guessed it) pants! The PantsLabyrinth app includes full shopping cart checkout experience, an optional wishlist feature that can be enabled with a feature flag, and many opportunities for sly jokes with friends from the UK.

### MovieCanon 

MovieCanon is a streaming service perfectly designed to illustrate common Braze use cases around content engagement. 

## How Pilot connects with your Braze dashboard

The Braze SDK is a package of code that collects data from your users once integrated with your app or website. When you connect Pilot to your dashboard, you initialize this connection between the Pilot app on your phone and the Braze SDK, as well as establish a unique connection with your Braze instance by giving Pilot your API key identifier for your dashboard.

