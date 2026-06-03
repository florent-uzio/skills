---
name: rc-version
description: Fetch the app version of a Ripple Custody (RC) instance from its OpenAPI/Swagger spec. Use when user asks about the version of a custody instance, RC version, custody app version, or mentions "version of custody instance".
---

# RC Version

Fetch and return the app version of a Ripple Custody instance.

## Quick start

User invokes `/rc-version <instance-url>` where the URL is either a bare hostname (e.g. `unseuzbe.7kbgnu.m3t4c0.services`) or a full base URL for non-standard instances like devboxes (e.g. `https://api-harmonize-devbox-xrpl-batch-3am8g5.m3t4c0.cloud/`).

## Steps

1. **Detect URL type**:
   - If the input starts with `https://` or `http://`, treat it as a full base URL
   - Otherwise treat it as a bare hostname following the `api.<hostname>` convention
2. **Construct the OpenAPI URL**:
   - Bare hostname: strip any `api.` prefix and trailing slashes → `https://api.<hostname>/api/OpenAPI?scope=&layout=`
   - Full base URL: strip trailing slash → `<base-url>/api/OpenAPI?scope=&layout=`
3. **Fetch** using WebFetch with prompt: `Extract the value of info.x-app-version`
4. **Return** the version string to the user in the format: `Version: <x-app-version>`

## Examples

Bare hostname: `unseuzbe.7kbgnu.m3t4c0.services`
→ `https://api.unseuzbe.7kbgnu.m3t4c0.services/api/OpenAPI?scope=&layout=`

Devbox full URL: `https://api-harmonize-devbox-xrpl-batch-3am8g5.m3t4c0.cloud/`
→ `https://api-harmonize-devbox-xrpl-batch-3am8g5.m3t4c0.cloud/api/OpenAPI?scope=&layout=`
