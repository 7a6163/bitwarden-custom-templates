# bitwarden-custom-templates

Ready-to-import **custom item templates** for [Bitwarden](https://bitwarden.com),
covering item types Bitwarden has no built-in type for (software licenses, API
credentials, …). They are plain Bitwarden JSON — no tooling required.

These pair well with
[1password-linux-to-bitwarden](https://github.com/MatejLach/1password-linux-to-bitwarden),
which maps such 1Password items to secure notes with custom fields; these
templates give you a blank starting point for new ones.

## Import

1. Web vault → **Tools → Import data**.
2. File format: **Bitwarden (.json)**.
3. Choose `templates.json` and import.

You'll get a **Templates** folder containing blank template items. To create a
real entry, open a template, **Clone** it, and fill it in.

> Importing adds items; it never overwrites. Re-importing creates duplicates, so
> import each file once.

## What's included

| Item | Fields |
|------|--------|
| Software License (Template) | license key (hidden), licensed to, registered email, version, purchase date, order number |
| API Credential (Template) | api key (hidden), username / client id, client secret (hidden), base url, expires |

## Add your own

Templates are just Bitwarden items. Copy one in `templates.json` and edit:

```json
{
  "id": "template-database",
  "folderId": "templates",
  "type": 2,
  "name": "Database (Template)",
  "notes": "Template — duplicate this item and fill it in.",
  "favorite": false,
  "fields": [
    { "name": "host", "value": "", "type": 0 },
    { "name": "port", "value": "", "type": 0 },
    { "name": "username", "value": "", "type": 0 },
    { "name": "password", "value": "", "type": 1 }
  ],
  "secureNote": { "type": 0 },
  "collectionIds": null
}
```

Field `type`: `0` = text, `1` = hidden, `2` = boolean. Item `type` `2` is a
secure note (the right home for arbitrary key/value templates).
