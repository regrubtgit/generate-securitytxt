# 🔐 `generate-securitytxt.sh` Generator and Explanation

Usage: generate_securitytxt.sh --help

Don't forget to chmod +x to make is executable.


---

# 🔐 `security.txt` Generator and Explanation

This documentation provides:

- An example `security.txt` file in English and Dutch
- Explanation of the `Expires:` field and why it uses the `Z` (Zulu time) notation
- A Bash script to generate a `security.txt` file interactively
- Recommended file permissions for `.well-known` and `security.txt`
- A suggested open source license (MIT)
- All formatted in English for international use

---

## 📄 Example `security.txt` File (Bilingual - Dutch and English)

```txt
# security.txt
# This file contains contact information for reporting security issues.
# Dit bestand bevat contactinformatie voor het melden van beveiligingsproblemen.

Contact: mailto:security@example.com
Expires: 2025-12-31T23:59:00Z
Encryption: https://example.com/pgp-key.txt
Acknowledgments: https://example.com/hall-of-fame
Preferred-Languages: en, nl
Canonical: https://example.com/.well-known/security.txt
Policy: https://example.com/security-policy
Hiring: https://example.com/jobs

# Dutch:
# We waarderen het als beveiligingsonderzoekers kwetsbaarheden op een
# verantwoorde manier melden. Neem contact met ons op via de bovenstaande
# contactinformatie.

# English:
# We appreciate responsible disclosure of security vulnerabilities.
# Please contact us using the information provided above.

---
 
## Why Use `Z` Instead of `UTC` in `Expires:` Fields?

When writing `Expires:` fields in a `security.txt` file (or any ISO 8601 timestamp), it’s important to use the letter `Z` to indicate **UTC time**, rather than writing "UTC". Here's why:

### ✅ 1. ISO 8601 Standard Compliance

The ISO 8601 standard specifies that timestamps **must** use:
- `Z` to represent UTC (also known as Zulu time), or
- An explicit offset like `+00:00` or `-04:00`

Using `"UTC"` is **not valid** in ISO 8601 format, and will be rejected by parsers expecting standardized time formats.

---

### ✅ 2. Machine Readability

The `Z` character is:
- **Short and unambiguous**
- **Consistently understood by machines and libraries** parsing ISO 8601
- Automatically recognized as UTC without confusion

In contrast, `"UTC"` is ambiguous in ISO 8601 context and **not parseable** by strict date/time parsers.

---

### ✅ 3. Origin of `Z` = Zulu Time

The letter `Z` comes from **Zulu Time**, a term used in:
- **Aviation**
- **Military**
- **Maritime industries**

In the NATO phonetic alphabet, **"Z" = Zulu**, and Zulu Time refers to **UTC without any local offset**. This convention has been adopted by the ISO 8601 standard.

---

### 🔍 Comparison Table

| Notation   | Meaning             | ISO 8601 Valid   | Valid in `security.txt`  |
| :----------- | :------------------- | :-----------------: | :-------------------------:| 
| `Z`        | UTC (Zulu Time)     | ✅              | ✅                       |
| `UTC`      | UTC (literal string)| ❌              | ❌                       |
| `+00:00`   | UTC (numeric offset)| ✅              | ✅                       |

---

### 📌 For `security.txt` Specifically

According to [RFC 9116](https://www.rfc-editor.org/rfc/rfc9116#section-2.5):

> The `Expires:` directive MUST use the format defined in [RFC3339], which is a profile of ISO 8601. This includes using **"Z"** to indicate UTC.

---

### ✅ Conclusion

Always use `Z` when specifying UTC time in the `Expires:` field to ensure:

- Standards compliance
- Machine readability
- Compatibility with security.txt scanners

Avoid using `"UTC"` in ISO 8601 timestamps — it is **not valid**.

