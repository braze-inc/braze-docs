---
nav_title: Feature Flags
article_title: Feature Flags
page_order: 3
description: "Learn how to coordinate new feature rollouts with Braze Feature Flags"
platform:
  - iOS
  - Android
  - Web
---

# Feature Flags

Feature Flags allow you to remotely enable or disable app functionality without spending additional engineering resources to release new code.

Create a new feature flag within the Braze dashboard by providing an `ID` (a name), a target audience, and a percentage of traffic to allocate to this feature. Then, using that same `ID` in your app or website's code, you can restrict certain parts of the business logic from running.

For example, if you've built a new profile page for your ride-sharing app, instead of releasing it (and potential bugs) directly to your entire user base, you can roll out the new profile page to only a single segment. 

## SDK Support

To use Feature Flags, ensure your SDKs are up to date with at least these minimum versions:
<!-- TODO -->
{% sdk_min_versions android:9999 web:9999 swift:9999 %}

## Quick Start Guide

### 1. Define a new Feature Flag

### 2. Check for the Feature Flag in your application

### 3. Enable the Feature Flag to a percentage of your audience

## Examples

### Soft launch new features to VIP users first

### Migrate internal API endpoints

### Change homepage links or banners on the fly

## Use cases

**Release new features safely, with confidence**
* Easily turn new features on or off without a code release
* Avoid incidents with a kill-switch for every new feature
* Test features on a smaller audience before rolling out globally

**Remotely control app variables**
* Modify functionality on-the-fly
* Swap out content without waiting for an app store release
* Dynamically personalize content using Braze profile attributes

**Coordinate feature rollout with marketing communication**
* Send messaging to users testing out a new feature
* Understand the impact of a feature rollout on conversions
* Automatically optimize conversions with Experiment Paths

Feature flags have two different strategic uses:

### Gradual Rollouts
Feature flags allow teams to gradually enable features to a sample population. This strategy helps to catch bugs early, to remove the risk of shipping new features to everyone at once. This also allows teams to roll back feature enablement without requiring an additional code release.

Example: Our E-commerce product finally comes in multiple colors. We have added a new color selector so customers can specify which color to purchase.

Without Feature Flags: We release this new feature and it goes live to the app stores. If there's a bug, users might not be able to make a purchase and we'll have to release a new version to the app store with a fix.

With Feature Flags: We release this new feature but only enable it for 5% of our users in Braze. If all goes well we gradually increase to 20%, 50%, and eventually 100%. If there's a bug we simply decrease down to 0% and examine what went wrong without losing additional revenue.

### Feature Experimentation

Experimenting with feature flags lets you confirm a hypothesis around a new feature. By splitting traffic into two or more groups, you can compare the impact of a feature flag across groups, and determine the best course of action based on the results.

Example: Our E-commerce team has a new product checkout page design that we believe will improve purchase conversion rates.

Without Feature Flags: We release the new checkout page, and if next month's revenue is lower, we have to release a new app version to revert the changes, which can take 1-2 weeks.

With Feature Flags: We show the new checkout page to 50% of users and make a decision in 1 month to either enable it to 100% or turn it completely off and revisit the designs. In either case we won't risk a poor experience for 50% of our users.