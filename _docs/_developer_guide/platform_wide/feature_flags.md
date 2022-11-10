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

Feature Flags allow you to remotely enable or disable app functionality without spending engineering resources to release new code.

Create a new feature flag within the Braze dashboard by providing a name (`ID`), a target audience, and a percentage of traffic to allocate to this feature.Then, using that same `ID` in your app or website's code, you can restrict or gate certain parts of the business logic from running.

For example, if you've built a new profile page for your ride-sharing app, instead of releasing it (and potential bugs) directly to your entire user base, you can roll out the new profile page to a single segment. 

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