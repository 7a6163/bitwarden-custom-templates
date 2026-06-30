# bitwarden-custom-templates

Ready-to-import **custom item templates** for [Bitwarden](https://bitwarden.com),
covering item types Bitwarden has no built-in type for (software licenses,
databases, passports, …). They are plain Bitwarden JSON — no tooling required.

## Why this exists (interim approach)

Bitwarden's native item types are only **Login, Card, Identity, and Secure
Note** (plus SSH Key). Password managers like 1Password have many more
(Database, Crypto Wallet, Passport, …), and Bitwarden's importer has nowhere
native to put them — they end up as plain notes with no structure.

This repo is a **stopgap**: each template is a Secure Note with pre-named custom
fields, so those item types get a consistent, searchable home today. Sensitive
fields (keys, passwords, PINs, recovery phrases) are marked **hidden**.

> If Bitwarden later adds native types or a richer import for these, this becomes
> unnecessary — you'd re-map the notes to the new native types. Until then, this
> is the practical workaround.

## How to use

**1. Import the templates (creates the "Templates" folder).**

1. Open the Bitwarden web vault → **Tools → Import data**.
2. Import destination: **My vault**.
3. File format: **Bitwarden (.json)**.
4. Choose `templates.json` (all types at once), or a single file from
   `templates/` (just one type) → **Import data**.

You now have a **Templates** folder containing one blank item per type.

> **First time:** import `templates.json` to get everything.
> **Later, when a new type is added:** import only that type's file from
> `templates/` (e.g. `templates/atm-card-pin-template.json`) so you don't
> re-create duplicates of the types you already have.

**2. Create a real entry by cloning a template.**

1. Open the template you want (e.g. *Software License (Template)*).
2. **⋮ (or Edit) → Clone**.
3. Fill in the fields, rename it, and move it to whichever folder you like.

Cloning leaves the original template untouched, so it's ready for next time.

> Importing **adds** items — it never overwrites. Re-importing creates
> duplicates, so import `templates.json` once.

## Included templates

| Template | Notable fields |
|----------|----------------|
| API Credential | api key 🔒, client secret 🔒, base url, expires |
| ATM Card PIN | bank, card number, withdrawal password 🔒 |
| Bank Account | routing/account number, SWIFT/BIC, IBAN, PIN 🔒 |
| Crypto Wallet | address, network, recovery phrase 🔒, private key 🔒 |
| Database | type, host, port, username, password 🔒, connection string 🔒 |
| Driver License | license number, class, state/country, expiry, DOB |
| Email Account | address, password 🔒, IMAP/SMTP server, port |
| Medical Record | patient, record type, provider, date, reference number |
| Membership | organization, member id, expiry, phone |
| Outdoor License | license number, valid from, expiry, issuing authority |
| Passport | passport number, nationality, DOB, issue/expiry, authority |
| Rewards Program | company, member id, PIN 🔒 |
| Server | url, hostname/IP, username, password 🔒, admin console url |
| Social Security Number | name, number 🔒 |
| Software License | license key 🔒, licensed to, registered email, version |
| Wireless Router | SSID, wireless password 🔒, admin password 🔒, server/IP |
| SSO Login | website URL + a `single sign-on` field for the provider |

🔒 = hidden field.

> **SSO Login** is a regular **Login** item (Bitwarden type 1), not a note: it
> has a URL but no password (you sign in via GitHub / Apple / Google / …). The
> `single sign-on` field records which provider — handy when a site offers
> several login methods.

## Add your own

Templates are just Bitwarden items. Copy one in `templates.json` and edit:

```json
{
  "id": "template-membership-card",
  "folderId": "templates",
  "type": 2,
  "name": "Gym Membership (Template)",
  "notes": "Template — clone this item and fill it in.",
  "favorite": false,
  "fields": [
    { "name": "member id", "value": "", "type": 0 },
    { "name": "access code", "value": "", "type": 1 }
  ],
  "secureNote": { "type": 0 },
  "collectionIds": null
}
```

Field `type`: `0` = text, `1` = hidden, `2` = boolean. Item `type` `2` is a
secure note — the right home for arbitrary key/value templates.

`templates.json` is the source of truth. After editing it, run `python3
split.py` to regenerate the per-type files in `templates/`.
