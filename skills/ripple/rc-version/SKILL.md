---
name: rc-version
description: Fetch the app version of a Ripple Custody (RC) instance from its OpenAPI/Swagger spec. Use when user asks about the version of a custody instance, RC version, custody app version, or mentions "version of custody instance".
---

# RC Version

Fetch and return the app version of a Ripple Custody instance.

## Quick start

User invokes `/rc-version <instance-url>` where the URL is the base hostname of the RC instance (e.g. `unseuzbe.7kbgnu.m3t4c0.services`).

## Steps

1. **Normalize the URL** — strip any `api.` prefix, `https://`, and trailing slashes from the input to get the bare hostname
2. **Construct the OpenAPI URL** — `https://api.<hostname>/api/OpenAPI?scope=&layout=`
3. **Fetch** using WebFetch with prompt: `Extract the value of info.x-app-version`
4. **Return** the version string to the user in the format: `Version: <x-app-version>`

## Example

Input: `unseuzbe.7kbgnu.m3t4c0.services`
Constructed URL: `https://api.unseuzbe.7kbgnu.m3t4c0.services/api/OpenAPI?scope=&layout=`
Output: `Version: 1.35.1`
