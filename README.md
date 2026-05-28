# smartcardfyi

[![PyPI version](https://agentgif.com/badge/pypi/smartcardfyi/version.svg)](https://pypi.org/project/smartcardfyi/)
[![Python](https://img.shields.io/pypi/pyversions/smartcardfyi)](https://pypi.org/project/smartcardfyi/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Smart card encyclopedia API client for Python. Look up card types (contact, contactless, dual-interface), chip platforms (Java Card, MULTOS, JCOP, BasicCard), ISO 7816 standards, EMV payment specifications, GlobalPlatform card management, manufacturers, form factors from ID-1 to iSIM, and security certifications from [SmartCardFYI](https://smartcardfyi.com) -- the comprehensive smart card reference with 280 records covering every major smart card technology in commercial and government use.

Extracted from [SmartCardFYI](https://smartcardfyi.com), a smart card technology platform with 280 records spanning chip platforms, international standards, security certifications, form factor specifications, and deployment guides used by payment system architects, telecom engineers, government ID program managers, and security researchers worldwide.

> **Explore smart cards at [smartcardfyi.com](https://smartcardfyi.com)** -- [Card Type Explorer](https://smartcardfyi.com/card/) | [Standards Reference](https://smartcardfyi.com/standard/) | [Platform Guide](https://smartcardfyi.com/platform/) | [Glossary](https://smartcardfyi.com/glossary/)

<p align="center">
  <img src="https://raw.githubusercontent.com/fyipedia/smartcardfyi/main/demo.gif" alt="smartcardfyi demo -- smart card type lookup, platform comparison, and standard reference in Python" width="800">
</p>

## Table of Contents

- [Install](#install)
- [Quick Start](#quick-start)
- [What You'll Find on SmartCardFYI](#what-youll-find-on-smartcardfyi)
  - [Contact vs Contactless Interface](#contact-vs-contactless-interface)
  - [Chip Platforms](#chip-platforms)
  - [EMV Payment Standards](#emv-payment-standards)
  - [ISO 7816 Standard Series](#iso-7816-standard-series)
  - [APDU Communication](#apdu-communication)
  - [GlobalPlatform Card Management](#globalplatform-card-management)
  - [Form Factors](#form-factors)
  - [Security Certifications](#security-certifications)
- [API Endpoints](#api-endpoints)
- [Command-Line Interface](#command-line-interface)
- [MCP Server (Claude, Cursor, Windsurf)](#mcp-server-claude-cursor-windsurf)
- [REST API Client](#rest-api-client)
- [Learn More About Smart Cards](#learn-more-about-smart-cards)
- [Also Available](#also-available)
- [Tag FYI Family](#tag-fyi-family)
- [FYIPedia Developer Tools](#fyipedia-developer-tools)
- [License](#license)

## Install

```bash
pip install smartcardfyi[api]     # API client (httpx)
pip install smartcardfyi[cli]     # + CLI (typer, rich)
pip install smartcardfyi[mcp]     # + MCP server
pip install smartcardfyi[all]     # Everything
```

## Quick Start

```python
from smartcardfyi.api import SmartCardFYI

with SmartCardFYI() as api:
    # Search card types, platforms, standards, glossary
    results = api.search("emv")
    print(results)

    # Look up a specific card type
    emv = api.card("emv-contact")
    print(emv["name"], emv["interface"])  # EMV Contact Card

    # Compare two card platforms
    diff = api.compare("java-card", "multos")
    print(diff)

    # Discover a random card type
    surprise = api.random()
    print(surprise["name"])
```

## What You'll Find on SmartCardFYI

SmartCardFYI is a comprehensive smart card encyclopedia covering card types, chip platforms, international standards, manufacturers, applications, form factors, and security certifications. Smart cards are tamper-resistant integrated circuit cards that provide secure data storage, cryptographic processing, and authenticated access -- the foundation of payment systems (5+ billion EMV cards active), telecommunications (8+ billion SIM cards), government identity, physical access control, and healthcare worldwide.

### Contact vs Contactless Interface

Smart cards communicate through two primary interfaces. **Contact cards** (ISO 7816-3) use an 8-pin gold pad that makes physical contact with a card reader, operating at 3.3V or 5V with clock speeds from 1 MHz to 20 MHz, using T=0 (byte-oriented) or T=1 (block-oriented) transmission protocols. **Contactless cards** (ISO 14443 Type A/B) use radio frequency at 13.56 MHz with read ranges of 4-10 cm, employing either Type A (ASK modulation, Miller encoding -- MIFARE, NTAG) or Type B (ASK modulation, NRZ-L encoding -- Calypso, CIV).

**Dual-interface cards** combine both interfaces sharing a single chip die with separate I/O paths. This is now the standard for modern EMV payment cards -- the same chip handles contact transactions at POS terminals and contactless tap-to-pay, with the card selecting the appropriate interface automatically based on the reader's field.

Learn more: [Card Type Explorer](https://smartcardfyi.com/card/) | [Glossary](https://smartcardfyi.com/glossary/)

### Chip Platforms

Smart card chip platforms provide the operating system and execution environment for card applications:

| Platform | Developer | Language | Multi-App | Cumulative Shipments | Key Feature |
|----------|-----------|----------|-----------|---------------------|-------------|
| Java Card | Oracle | Java (subset) | Yes | 30+ billion | Open ecosystem, applet isolation, firewall |
| MULTOS | MULTOS Consortium | MEL, C, Java | Yes | 500+ million | Certified secure loading, no vendor lock-in |
| JCOP | NXP | Java Card | Yes | Billions | NXP hardware optimization, DESFire integration |
| BasicCard | ZeitControl | ZC-Basic | Limited | Millions | Rapid prototyping, free dev tools |
| Native OS | Various | Assembly/C | No | Billions | Maximum performance, proprietary |

**Java Card** dominates with over 30 billion cumulative shipments. It runs a stripped-down JVM (JCVM) supporting a subset of Java -- no floats, no threads, no garbage collection, no multi-dimensional arrays, no String class. Applets are isolated via the Java Card firewall, and inter-applet communication uses Shareable Interface Objects (SIOs). Memory is persistent by default (EEPROM/Flash), and objects survive card power cycles without explicit serialization.

Learn more: [Platform Guide](https://smartcardfyi.com/platform/) | [Standards](https://smartcardfyi.com/standard/)

### EMV Payment Standards

EMV (Europay, Mastercard, Visa) defines the global standard for chip-based payment cards. The EMV specification suite includes:

| Specification | Scope | Key Concepts |
|--------------|-------|-------------|
| EMV 4.3 Book 1 | Application-independent ICC to terminal | ATR parsing, application selection (AID) |
| EMV 4.3 Book 2 | Security and key management | SDA, DDA, CDA offline authentication |
| EMV 4.3 Book 3 | Application specification | Transaction flow, card risk management |
| EMV 4.3 Book 4 | Cardholder, attendant, acquirer | PIN entry, receipt, online authorization |
| EMV Contactless Books A-D | Tap-to-pay specifications | Per-kernel specs (Visa qVSDC, Mastercard PayPass, Amex ExpressPay) |
| EMV 3-D Secure 2.0 | Online authentication | Risk-based authentication, SCA compliance |
| EMV Payment Tokenisation | Token lifecycle | Device tokens for Apple Pay, Google Pay |

**Offline Data Authentication (ODA)**: EMV cards prove their authenticity without online connectivity using three mechanisms -- Static Data Authentication (SDA, RSA signature on static data, no cloning protection), Dynamic Data Authentication (DDA, card generates unique RSA signature per transaction), and Combined DDA/Application Cryptogram (CDA, strongest -- dynamic signature covers the transaction cryptogram).

### ISO 7816 Standard Series

The ISO 7816 series defines the complete smart card communication stack from physical dimensions to application protocols:

| Part | Title | Key Content |
|------|-------|-------------|
| 7816-1 | Physical characteristics | 85.6 x 53.98 x 0.76 mm, bending (10 N), UV, X-ray resistance |
| 7816-2 | Contacts | 8-pin pad (C1-C8): VCC, RST, CLK, GND, VPP, I/O |
| 7816-3 | Electrical interface | ATR (Answer to Reset), PPS negotiation, T=0/T=1 protocols |
| 7816-4 | Commands (APDU) | CLA/INS/P1/P2/Lc/Le structure, response SW1-SW2 |
| 7816-5 | AID registration | RID (5 bytes, registered) + PIX (up to 11 bytes, proprietary) |
| 7816-6 | Data elements | BER-TLV encoding, interindustry data objects |
| 7816-8 | Security commands | VERIFY, INTERNAL AUTHENTICATE, EXTERNAL AUTHENTICATE, key management |
| 7816-9 | Card management | Life cycle states, file creation/deletion, application management |
| 7816-15 | Crypto information | PKCS#15-compatible on-card certificate/key structure |

### APDU Communication

All smart card communication follows the APDU (Application Protocol Data Unit) structure defined in ISO 7816-4:

**Command APDU**: `CLA | INS | P1 | P2 | Lc | Data | Le`

| Field | Size | Description |
|-------|------|-------------|
| CLA | 1 byte | Class byte (0x00=ISO, 0x80-0x8F=proprietary) |
| INS | 1 byte | Instruction (0xA4=SELECT, 0xB0=READ BINARY, 0x20=VERIFY) |
| P1-P2 | 2 bytes | Parameters (file ID, record number, key reference) |
| Lc | 0-3 bytes | Length of command data (absent if no data) |
| Data | Lc bytes | Command data payload |
| Le | 0-3 bytes | Expected response data length |

**Response APDU**: `Data | SW1 | SW2`

| Status Word | Meaning |
|-------------|---------|
| 90 00 | Success |
| 61 XX | SW2 bytes of response data available (use GET RESPONSE) |
| 6A 82 | File or application not found |
| 69 82 | Security condition not satisfied |
| 6A 86 | Incorrect parameters P1-P2 |

Learn more: [Standards Reference](https://smartcardfyi.com/standard/) | [Glossary](https://smartcardfyi.com/glossary/)

### GlobalPlatform Card Management

GlobalPlatform specifications define how applications are loaded, installed, and managed on multi-application smart cards:

| Component | Role | Key Function |
|-----------|------|-------------|
| Issuer Security Domain (ISD) | Card-level authority | Key management, secure channel, app lifecycle |
| Supplementary Security Domain (SSD) | Delegated authority | Third-party application management |
| OPEN (GP Environment) | Runtime | API dispatch, inter-applet firewall, registry |
| Secure Channel Protocol (SCP02/SCP03) | Session security | Mutual authentication, session keys, encrypted APDUs |
| DAP Verification | Code integrity | Data Authentication Pattern for applet loading |

**SCP03** (Secure Channel Protocol 03) provides AES-based session key derivation, mutual authentication, and command/response encryption with C-MAC/R-MAC integrity protection. It supersedes SCP02 (3DES-based) for new deployments and is mandatory for EMVCo-certified cards.

### Form Factors

| Form Factor | Dimensions (mm) | Primary Use |
|-------------|------------------|-------------|
| Full-size (ID-1) | 85.6 x 53.98 x 0.76 | Payment, identity, access |
| ID-000 (Plug-in) | 25 x 15 x 0.76 | Legacy SIM cards |
| Mini SIM (2FF) | 25 x 15 | GSM/3G phones |
| Micro SIM (3FF) | 15 x 12 | 4G smartphones |
| Nano SIM (4FF) | 12.3 x 8.8 | Modern smartphones |
| Embedded SIM (MFF2) | 6 x 5 (soldered) | IoT, M2M, wearables |
| iSIM | Integrated in SoC | Next-gen IoT (in silicon) |

Modern SIM cards ship as multi-cut ("tri-cut" or "quad-cut") carriers that snap to Mini, Micro, or Nano sizes from a single ID-1 card blank. **eSIM** (GSMA Remote SIM Provisioning) enables over-the-air profile download without physical SIM swap -- now standard in iPhone 14+ (US), Apple Watch, and Samsung Galaxy flagship devices.

### Security Certifications

| Certification | Scope | Typical Level | Evaluation Time |
|---------------|-------|---------------|-----------------|
| Common Criteria (ISO 15408) | IC + OS + applets | EAL5+ (smart cards) | 12-18 months |
| FIPS 140-2/140-3 | Cryptographic modules | Level 2-3 | 6-12 months |
| EMVCo Security Evaluation | Payment card ICs | IC, Platform, Application | 6-9 months |
| PCI PTS | Payment terminals | POI v6 | 3-6 months |
| ANSSI CSPN | French fast-track | Binary pass/fail | 2-3 months |

Learn more: [Card Type Explorer](https://smartcardfyi.com/card/) | [Platform Guide](https://smartcardfyi.com/platform/)

## API Endpoints

Free, no authentication required. JSON responses with CORS enabled.

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/card/{slug}/` | Card type detail with specs |
| GET | `/api/platform/{slug}/` | Chip platform with features |
| GET | `/api/standard/{slug}/` | Standard detail with linked cards |
| GET | `/api/manufacturer/{slug}/` | Manufacturer with product lines |
| GET | `/api/application/{slug}/` | Application with card types |
| GET | `/api/form-factor/{slug}/` | Form factor with dimensions |
| GET | `/api/certification/{slug}/` | Certification with requirements |
| GET | `/api/term/{slug}/` | Glossary term definition |
| GET | `/api/search/?q={query}` | Search across all content types |
| GET | `/api/compare/?a={slug}&b={slug}` | Compare two card types |
| GET | `/api/random/` | Random card type discovery |
| GET | `/api/openapi.json` | OpenAPI 3.1.0 specification |

### Example

```bash
# Search for EMV card types
curl -s "https://smartcardfyi.com/api/search/?q=emv" | python -m json.tool
```

Full API documentation at [smartcardfyi.com/api/](https://smartcardfyi.com/api/).
OpenAPI 3.1.0 spec: [smartcardfyi.com/api/openapi.json](https://smartcardfyi.com/api/openapi.json).

## Command-Line Interface

```bash
smartcardfyi search "java card"         # Search all content
smartcardfyi card emv-contact           # Card type detail
smartcardfyi compare java-card multos   # Side-by-side comparison
smartcardfyi random                     # Discover a random card type
```

## MCP Server (Claude, Cursor, Windsurf)

```json
{
    "mcpServers": {
        "smartcardfyi": {
            "command": "uvx",
            "args": ["--from", "smartcardfyi[mcp]", "python", "-m", "smartcardfyi.mcp_server"]
        }
    }
}
```

Tools: `smartcard_search`, `smartcard_lookup`, `smartcard_compare`

## REST API Client

```python
from smartcardfyi.api import SmartCardFYI

with SmartCardFYI() as api:
    api.search("emv")                          # Full-text search
    api.card("emv-contact")                    # Card type detail
    api.platform("java-card")                  # Chip platform
    api.standard("iso-7816")                   # Standard detail
    api.manufacturer("nxp")                    # Manufacturer
    api.application("payment")                 # Application
    api.form_factor("id-1")                    # Form factor
    api.certification("common-criteria")       # Certification
    api.glossary_term("apdu")                  # Glossary term
    api.compare("java-card", "multos")         # Compare two cards
    api.random()                               # Random discovery
    api.openapi()                              # OpenAPI 3.1.0 spec
```

## Learn More About Smart Cards

- **Browse**: [Card Type Explorer](https://smartcardfyi.com/card/) · [Platform Guide](https://smartcardfyi.com/platform/) · [Form Factors](https://smartcardfyi.com/form-factor/)
- **Reference**: [Standards](https://smartcardfyi.com/standard/) · [Certifications](https://smartcardfyi.com/certification/) · [Glossary](https://smartcardfyi.com/glossary/)
- **API**: [REST API Docs](https://smartcardfyi.com/api/) · [OpenAPI Spec](https://smartcardfyi.com/api/openapi.json)

## Also Available

| Platform | Install | Link |
|----------|---------|------|
| **npm** | `npm install smartcardfyi` | [npm](https://www.npmjs.com/package/smartcardfyi) |
| **Go** | `go get github.com/fyipedia/smartcardfyi-go` | [pkg.go.dev](https://pkg.go.dev/github.com/fyipedia/smartcardfyi-go) |
| **Rust** | `cargo add smartcardfyi` | [crates.io](https://crates.io/crates/smartcardfyi) |
| **Ruby** | `gem install smartcardfyi` | [rubygems.org](https://rubygems.org/gems/smartcardfyi) |
| **MCP** | `uvx --from "smartcardfyi[mcp]" python -m smartcardfyi.mcp_server` | [Config](#mcp-server-claude-cursor-windsurf) |

## Tag FYI Family

Part of the [FYIPedia](https://fyipedia.com) open-source developer tools ecosystem -- automatic identification and data capture technologies.

| Site | Domain | Focus |
|------|--------|-------|
| BarcodeFYI | [barcodefyi.com](https://barcodefyi.com) | 518 records -- barcode symbologies, standards, GS1 prefixes |
| QRCodeFYI | [qrcodefyi.com](https://qrcodefyi.com) | 425 records -- QR code types, versions, encoding modes |
| NFCFYI | [nfcfyi.com](https://nfcfyi.com) | 288 records -- NFC chips, NDEF records, standards |
| BLEFYI | [blefyi.com](https://blefyi.com) | 261 records -- BLE chips, GATT profiles, beacons |
| RFIDFYI | [rfidfyi.com](https://rfidfyi.com) | 318 records -- RFID tags, frequency bands, EPC schemes |
| **SmartCardFYI** | [smartcardfyi.com](https://smartcardfyi.com) | **280 records -- smart cards, EMV, Java Card, platforms** |

## FYIPedia Developer Tools

| Package | PyPI | npm | Description |
|---------|------|-----|-------------|
| barcodefyi | [PyPI](https://pypi.org/project/barcodefyi/) | [npm](https://www.npmjs.com/package/barcodefyi) | Barcode symbologies, standards -- [barcodefyi.com](https://barcodefyi.com) |
| qrcodefyi | [PyPI](https://pypi.org/project/qrcodefyi/) | [npm](https://www.npmjs.com/package/qrcodefyi) | QR code types, versions, encoding -- [qrcodefyi.com](https://qrcodefyi.com) |
| nfcfyi | [PyPI](https://pypi.org/project/nfcfyi/) | [npm](https://www.npmjs.com/package/nfcfyi) | NFC chips, NDEF, standards -- [nfcfyi.com](https://nfcfyi.com) |
| blefyi | [PyPI](https://pypi.org/project/blefyi/) | [npm](https://www.npmjs.com/package/blefyi) | BLE profiles, beacons, chips -- [blefyi.com](https://blefyi.com) |
| rfidfyi | [PyPI](https://pypi.org/project/rfidfyi/) | [npm](https://www.npmjs.com/package/rfidfyi) | RFID tags, readers, frequencies -- [rfidfyi.com](https://rfidfyi.com) |
| **smartcardfyi** | [PyPI](https://pypi.org/project/smartcardfyi/) | [npm](https://www.npmjs.com/package/smartcardfyi) | **Smart cards, EMV, platforms -- [smartcardfyi.com](https://smartcardfyi.com)** |

## Embed Widget

Embed [SmartCardFYI](https://smartcardfyi.com) widgets on any website with [smartcardfyi-embed](https://widget.smartcardfyi.com):

```html
<script src="https://cdn.jsdelivr.net/npm/smartcardfyi-embed@1/dist/embed.min.js"></script>
<div data-smartcardfyi="entity" data-slug="example"></div>
```

Zero dependencies · Shadow DOM · 4 themes (light/dark/sepia/auto) · [Widget docs](https://widget.smartcardfyi.com)

## Recently Updated (v0.1.2)

Latest content state on [https://smartcardfyi.com](https://smartcardfyi.com):
- [Homepage](https://smartcardfyi.com)
- [Developer documentation](https://smartcardfyi.com/developers/)
- [Sitemap (full content index)](https://smartcardfyi.com/sitemap.xml)

Version bumped 2026-05-27 as part of the FYIPedia [SEO recovery refresh](https://github.com/dobestan).

## License

MIT
