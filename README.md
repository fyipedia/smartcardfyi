# smartcardfyi

[![PyPI version](https://agentgif.com/badge/pypi/smartcardfyi/version.svg)](https://pypi.org/project/smartcardfyi/)
[![Python](https://img.shields.io/pypi/pyversions/smartcardfyi)](https://pypi.org/project/smartcardfyi/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Smart card encyclopedia API client for Python. Look up card types, chip platforms, ISO 7816 standards, manufacturers, form factors, and certifications from [SmartCardFYI](https://smartcardfyi.com) -- the comprehensive smart card reference covering EMV payment cards, SIM/USIM, Java Card, MULTOS, JCOP, PIV, CAC, FIDO2, and every major smart card technology in commercial and government use.

> **Explore smart cards at [smartcardfyi.com](https://smartcardfyi.com)** -- [Card Type Explorer](https://smartcardfyi.com/card/) | [Standards Reference](https://smartcardfyi.com/standard/) | [Platform Guide](https://smartcardfyi.com/platform/) | [Glossary](https://smartcardfyi.com/glossary/)

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
    print(emv["name"], emv["interface"])

    # Compare two card types
    diff = api.compare("java-card", "multos")
    print(diff)

    # Discover a random card type
    surprise = api.random()
    print(surprise["name"])
```

## What You'll Find on SmartCardFYI

SmartCardFYI is a comprehensive smart card encyclopedia covering card types, chip platforms, international standards, manufacturers, applications, form factors, and security certifications. Smart cards are tamper-resistant integrated circuit cards that provide secure data storage, cryptographic processing, and authenticated access -- the foundation of payment systems, telecommunications, government identity, physical access control, and healthcare worldwide.

### Contact vs Contactless Interface

Smart cards communicate through two primary interfaces. **Contact cards** (ISO 7816-3) use an 8-pin gold pad that makes physical contact with a card reader, operating at 3.3V or 5V with clock speeds up to 20 MHz. **Contactless cards** (ISO 14443 Type A/B) use radio frequency at 13.56 MHz with read ranges of 4-10 cm. **Dual-interface cards** combine both, sharing a single chip die with separate I/O paths -- the standard for modern EMV payment cards.

### Chip Platforms

| Platform | Developer | Language | Multi-App | Key Feature |
|----------|-----------|----------|-----------|-------------|
| Java Card | Oracle | Java (subset) | Yes | Open ecosystem, applet isolation |
| MULTOS | MULTOS Consortium | MEL, C, Java | Yes | Certified secure loading |
| JCOP | NXP | Java Card | Yes | NXP hardware optimization |
| BasicCard | ZeitControl | ZC-Basic | Limited | Rapid prototyping |
| .NET Card | Gemalto (legacy) | C# (subset) | Yes | Windows ecosystem integration |
| Native OS | Various | Assembly/C | No | Maximum performance, proprietary |

Java Card dominates the market with over 30 billion cumulative shipments. It runs a stripped-down Java Virtual Machine (JVMCDI) supporting a subset of Java -- no floats, no threads, no garbage collection, no multi-dimensional arrays. Applets are isolated via the Java Card firewall, and inter-applet communication uses Shareable Interface Objects (SIOs).

### EMV Payment Standards

EMV (Europay, Mastercard, Visa) defines the global standard for chip-based payment cards. The EMV specification suite includes contact (EMV 4.3 Book 1-4), contactless (EMV Contactless Books A-D), and tokenization (EMV Payment Tokenisation). Key concepts include the Application Identifier (AID), Card Risk Management, offline data authentication (SDA/DDA/CDA), and cardholder verification methods (PIN, signature, CDCVM).

### GlobalPlatform Card Management

GlobalPlatform specifications define how applications are loaded, installed, and managed on multi-application smart cards. The Card Specification (GP 2.3.1) introduces the Issuer Security Domain (ISD), Supplementary Security Domains (SSD), and the OPEN (GlobalPlatform Environment). Secure Channel Protocol (SCP02/SCP03) provides authenticated and encrypted communication between the card and the host for remote applet management.

### ISO 7816 Standard Series

| Part | Title | Scope |
|------|-------|-------|
| ISO 7816-1 | Physical characteristics | Card dimensions, bending, UV, X-ray |
| ISO 7816-2 | Contacts | 8-pin pad position and assignment |
| ISO 7816-3 | Electrical interface | ATR, PPS, T=0/T=1 protocols |
| ISO 7816-4 | Commands (APDU) | CLA/INS/P1/P2/Lc/Le structure |
| ISO 7816-5 | AID registration | RID + PIX application identifiers |
| ISO 7816-6 | Data elements | TLV encoding, interindustry data |
| ISO 7816-8 | Security commands | VERIFY, INT AUTH, EXT AUTH, key mgmt |
| ISO 7816-9 | Card management | Life cycle, file operations |
| ISO 7816-15 | Crypto info app | PKCS#15 on-card structure |

### Form Factors

| Form Factor | ISO Designation | Dimensions (mm) | Primary Use |
|-------------|----------------|------------------|-------------|
| Full-size (ID-1) | ISO/IEC 7810 ID-1 | 85.6 x 53.98 x 0.76 | Payment, identity, access |
| ID-000 (Plug-in) | ISO/IEC 7810 ID-000 | 25 x 15 x 0.76 | SIM cards (legacy) |
| Mini SIM (2FF) | ETSI TS 102.221 | 25 x 15 | GSM/3G phones |
| Micro SIM (3FF) | ETSI TS 102.221 | 15 x 12 | 4G smartphones |
| Nano SIM (4FF) | ETSI TS 102.221 | 12.3 x 8.8 | Modern smartphones |
| Embedded SIM (MFF2) | ETSI TS 103.383 | 6 x 5 (soldered) | IoT, M2M, wearables |
| iSIM | GSMA | Integrated in SoC | Next-gen IoT |

Modern SIM cards ship as multi-cut ("tri-cut" or "quad-cut") carriers that snap to Mini, Micro, or Nano sizes from a single ID-1 card blank.

### Security Certifications

| Certification | Scope | Levels |
|---------------|-------|--------|
| Common Criteria (ISO 15408) | IC hardware + OS + applets | EAL1-EAL7 (EAL5+ typical for cards) |
| FIPS 140-2/140-3 | Cryptographic modules | Levels 1-4 |
| EMVCo Security Evaluation | Payment card ICs | IC, Platform, Application |
| ANSSI CSPN | French fast-track | Binary assessment |
| PCI PTS | Payment terminals | POI device security |

### APDU Communication

All smart card communication follows the APDU (Application Protocol Data Unit) structure defined in ISO 7816-4. A command APDU contains: CLA (class byte), INS (instruction), P1-P2 (parameters), Lc (data length), Data, and Le (expected response length). The card returns a response APDU with optional data and a 2-byte status word (SW1-SW2), where 90 00 indicates success.

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

```bash
# Example: search for EMV card types
curl -s "https://smartcardfyi.com/api/search/?q=emv" | python -m json.tool
```

## Command-Line Interface

```bash
smartcardfyi search "java card"
smartcardfyi card emv-contact
smartcardfyi compare java-card multos
smartcardfyi random
```

## MCP Server (Claude, Cursor, Windsurf)

```json
{
    "mcpServers": {
        "smartcardfyi": {
            "command": "python",
            "args": ["-m", "smartcardfyi.mcp_server"]
        }
    }
}
```

Tools: `smartcard_search`, `smartcard_lookup`, `smartcard_compare`

## API Client

```python
from smartcardfyi.api import SmartCardFYI

with SmartCardFYI() as api:
    # All 12 endpoints
    api.search("emv")
    api.card("emv-contact")
    api.platform("java-card")
    api.standard("iso-7816")
    api.manufacturer("nxp")
    api.application("payment")
    api.form_factor("id-1")
    api.certification("common-criteria")
    api.glossary_term("apdu")
    api.compare("java-card", "multos")
    api.random()
    api.openapi()
```

## Also Available

| Language | Package | Install |
|----------|---------|---------|
| Python | [smartcardfyi](https://pypi.org/project/smartcardfyi/) | `pip install smartcardfyi` |
| TypeScript | [smartcardfyi](https://www.npmjs.com/package/smartcardfyi) | `npm install smartcardfyi` |
| Go | [smartcardfyi-go](https://pkg.go.dev/github.com/fyipedia/smartcardfyi-go) | `go get github.com/fyipedia/smartcardfyi-go` |
| Rust | [smartcardfyi](https://crates.io/crates/smartcardfyi) | `cargo add smartcardfyi` |
| Ruby | [smartcardfyi](https://rubygems.org/gems/smartcardfyi) | `gem install smartcardfyi` |

## Code FYI Family

| Site | Domain | Focus |
|------|--------|-------|
| BarcodeFYI | [barcodefyi.com](https://barcodefyi.com) | Barcode symbologies & standards |
| QRCodeFYI | [qrcodefyi.com](https://qrcodefyi.com) | QR code types & encoding |
| NFCFYI | [nfcfyi.com](https://nfcfyi.com) | NFC tags & NDEF records |
| BLEFYI | [blefyi.com](https://blefyi.com) | Bluetooth Low Energy profiles |
| RFIDFYI | [rfidfyi.com](https://rfidfyi.com) | RFID tags & frequency bands |
| SmartCardFYI | [smartcardfyi.com](https://smartcardfyi.com) | Smart card types & platforms |

## License

MIT
