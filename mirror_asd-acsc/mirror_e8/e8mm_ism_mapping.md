# Mapping between the *Essential Eight maturity model* and the ISM

This document presents the Essential Eight requirements mapped to ASD ISM controls with their applicable maturity levels. It is optimized for human reading, with one canonical description per control and cross-references from strategy views to avoid duplication.

## Legend

### Maturity levels

| Level | Label |
| --- | --- |
| L1 | Maturity Level 1 |
| L2 | Maturity Level 2 |
| L3 | Maturity Level 3 |

### Mitigation strategies

| Key | Strategy |
| --- | --- |
| patch_applications | Patch applications |
| patch_operating_systems | Patch operating systems |
| multi_factor_authentication | Multi-factor authentication |
| restrict_administrative_privileges | Restrict administrative privileges |
| application_control | Application control |
| restrict_microsoft_office_macros | Restrict Microsoft Office macros |
| user_application_hardening | User application hardening |
| regular_backups | Regular backups |

## Requirements catalog (canonical descriptions)

Each control is listed once. Strategy-specific sections below link back here to avoid duplicating long text.

### ISM-0123 — Cybersecurity incidents are reported to the chief information security officer, or one of their delegates, as soon as possible after they occur or are discovered.
- Applicable maturity: L2, L3
- Strategies: Multi-factor authentication; Restrict administrative privileges; Application control; User application hardening

### ISM-0140 — Cybersecurity incidents are reported to ASD as soon as possible after they occur or are discovered.
- Applicable maturity: L2, L3
- Strategies: Multi-factor authentication; Restrict administrative privileges; Application control; User application hardening

### ISM-1819 — Following the identification of a cybersecurity incident, the cybersecurity incident response plan is enacted.
- Applicable maturity: L2, L3
- Strategies: Multi-factor authentication; Restrict administrative privileges; Application control; User application hardening

### ISM-1507 — Requests for privileged access to systems and their resources are validated when first requested.
- Applicable maturity: L1, L2, L3
- Strategies: Restrict administrative privileges

### ISM-1508 — Privileged access to systems and their resources is limited to only what is required for users and services to undertake their duties.
- Applicable maturity: L3
- Strategies: Restrict administrative privileges

### ISM-1175 — Privileged user accounts (excluding those explicitly authorised to access online services) are prevented from accessing the internet, email and web services.
- Applicable maturity: L1, L2, L3
- Strategies: Restrict administrative privileges

### ISM-1883 — Privileged user accounts explicitly authorised to access online services are strictly limited to only what is required for users and services to undertake their duties.
- Applicable maturity: L1, L2, L3
- Strategies: Restrict administrative privileges

### ISM-1649 — Just-in-time administration is used for the administration of systems and their resources.
- Applicable maturity: L3
- Strategies: Restrict administrative privileges

### ISM-0445 — Privileged users are assigned a dedicated privileged user account to be used solely for duties requiring privileged access.
- Applicable maturity: L1, L2, L3
- Strategies: Restrict administrative privileges

### ISM-1509 — Privileged access events are centrally logged.
- Applicable maturity: L2, L3
- Strategies: Restrict administrative privileges

### ISM-1650 — Privileged user account and security group management events are centrally logged.
- Applicable maturity: L2, L3
- Strategies: Restrict administrative privileges

### ISM-1648 — Privileged access to systems and their resources are disabled after 45 days of inactivity.
- Applicable maturity: L2, L3
- Strategies: Restrict administrative privileges

### ISM-1647 — Privileged access to systems and their resources are disabled after 12 months unless revalidated.
- Applicable maturity: L2, L3
- Strategies: Restrict administrative privileges

### ISM-1407 — The latest release, or the previous release, of operating systems are used.
- Applicable maturity: L3
- Strategies: Patch operating systems

### ISM-1654 — Internet Explorer 11 is disabled or removed.
- Applicable maturity: L1, L2, L3
- Strategies: User application hardening

### ISM-1655 — .NET Framework 3.5 (includes .NET 2.0 and 3.0) is disabled or removed.
- Applicable maturity: L3
- Strategies: User application hardening

### ISM-0843 — Application control is implemented on workstations.
- Applicable maturity: L1, L2, L3
- Strategies: Application control

### ISM-1490 — Application control is implemented on internet-facing servers.
- Applicable maturity: L2, L3
- Strategies: Application control

### ISM-1656 — Application control is implemented on non-internet-facing servers.
- Applicable maturity: L3
- Strategies: Application control

### ISM-1870 — Application control is applied to user profiles and temporary folders used by operating systems, web browsers and email clients.
- Applicable maturity: L1, L2, L3
- Strategies: Application control

### ISM-1871 — Application control is applied to all locations other than user profiles and temporary folders used by operating systems, web browsers and email clients.
- Applicable maturity: L2, L3
- Strategies: Application control

### ISM-1657 — Application control restricts the execution of executables, software libraries, scripts, installers, compiled HTML, HTML applications and control panel applets to an organisation-approved set.
- Applicable maturity: L1, L2, L3
- Strategies: Application control

### ISM-1658 — Application control restricts the execution of drivers to an organisation-approved set.
- Applicable maturity: L3
- Strategies: Application control

### ISM-1544 — Microsoft’s recommended application blocklist is implemented.
- Applicable maturity: L2, L3
- Strategies: Application control

### ISM-1659 — Microsoft’s vulnerable driver blocklist is implemented.
- Applicable maturity: L3
- Strategies: Application control

### ISM-1582 — Application control rulesets are validated on an annual or more frequent basis.
- Applicable maturity: L2, L3
- Strategies: Application control

### ISM-1660 — Allowed and blocked application control events are centrally logged.
- Applicable maturity: L2, L3
- Strategies: Application control

### ISM-1889 — Command line process creation events are centrally logged.
- Applicable maturity: L2, L3
- Strategies: User application hardening

### ISM-1621 — Windows PowerShell 2.0 is disabled or removed.
- Applicable maturity: L3
- Strategies: User application hardening

### ISM-1622 — PowerShell is configured to use Constrained Language Mode.
- Applicable maturity: L3
- Strategies: User application hardening

### ISM-1623 — PowerShell module logging, script block logging and transcription events are centrally logged.
- Applicable maturity: L2, L3
- Strategies: User application hardening

### ISM-1667 — Microsoft Office is blocked from creating child processes.
- Applicable maturity: L2, L3
- Strategies: User application hardening

### ISM-1668 — Microsoft Office is blocked from creating executable content.
- Applicable maturity: L2, L3
- Strategies: User application hardening

### ISM-1669 — Microsoft Office is blocked from injecting code into other processes.
- Applicable maturity: L2, L3
- Strategies: User application hardening

### ISM-1542 — Microsoft Office is configured to prevent activation of Object Linking and Embedding packages.
- Applicable maturity: L2, L3
- Strategies: User application hardening

### ISM-1859 — Office productivity suites are hardened using ASD and vendor hardening guidance, with the most restrictive guidance taking precedence when conflicts occur.
- Applicable maturity: L2, L3
- Strategies: User application hardening

### ISM-1823 — Office productivity suite security settings cannot be changed by users.
- Applicable maturity: L2, L3
- Strategies: User application hardening

### ISM-1486 — Web browsers do not process Java from the internet.
- Applicable maturity: L1, L2, L3
- Strategies: User application hardening

### ISM-1485 — Web browsers do not process web advertisements from the internet.
- Applicable maturity: L1, L2, L3
- Strategies: User application hardening

### ISM-1412 — Web browsers are hardened using ASD and vendor hardening guidance, with the most restrictive guidance taking precedence when conflicts occur.
- Applicable maturity: L2, L3
- Strategies: User application hardening

### ISM-1585 — Web browser security settings cannot be changed by users.
- Applicable maturity: L1, L2, L3
- Strategies: User application hardening

### ISM-1670 — PDF applications are blocked from creating child processes.
- Applicable maturity: L2, L3
- Strategies: User application hardening

### ISM-1860 — PDF applications are hardened using ASD and vendor hardening guidance, with the most restrictive guidance taking precedence when conflicts occur.
- Applicable maturity: L2, L3
- Strategies: User application hardening

### ISM-1824 — PDF application security settings cannot be changed by users.
- Applicable maturity: L2, L3
- Strategies: User application hardening

### ISM-1671 — Microsoft Office macros are disabled for users that do not have a demonstrated business requirement.
- Applicable maturity: L1, L2, L3
- Strategies: Restrict Microsoft Office macros

### ISM-1488 — Microsoft Office macros in files originating from the internet are blocked.
- Applicable maturity: L1, L2, L3
- Strategies: Restrict Microsoft Office macros

### ISM-1672 — Microsoft Office macro antivirus scanning is enabled.
- Applicable maturity: L1, L2, L3
- Strategies: Restrict Microsoft Office macros

### ISM-1673 — Microsoft Office macros are blocked from making Win32 API calls.
- Applicable maturity: L2, L3
- Strategies: Restrict Microsoft Office macros

### ISM-1674 — Only Microsoft Office macros running from within a sandboxed environment, a Trusted Location or that are digitally signed by a trusted publisher are allowed to execute.
- Applicable maturity: L3
- Strategies: Restrict Microsoft Office macros

### ISM-1890 — Microsoft Office macros are checked to ensure they are free of malicious code before being digitally signed or placed within Trusted Locations.
- Applicable maturity: L3
- Strategies: Restrict Microsoft Office macros

### ISM-1487 — Only privileged users responsible for checking that Microsoft Office macros are free of malicious code can write to and modify content within Trusted Locations.
- Applicable maturity: L3
- Strategies: Restrict Microsoft Office macros

### ISM-1675 — Microsoft Office macros digitally signed by an untrusted publisher cannot be enabled via the Message Bar or Backstage View.
- Applicable maturity: L3
- Strategies: Restrict Microsoft Office macros

### ISM-1891 — Microsoft Office macros digitally signed by signatures other than V3 signatures cannot be enabled via the Message Bar or Backstage View.
- Applicable maturity: L3
- Strategies: Restrict Microsoft Office macros

### ISM-1676 — Microsoft Office’s list of trusted publishers is validated on an annual or more frequent basis.
- Applicable maturity: L3
- Strategies: Restrict Microsoft Office macros

### ISM-1489 — Microsoft Office macro security settings cannot be changed by users.
- Applicable maturity: L1, L2, L3
- Strategies: Restrict Microsoft Office macros

### ISM-1504 — Multi-factor authentication is used to authenticate users to their organisation’s online services that process, store or communicate their organisation’s sensitive data.
- Applicable maturity: L1, L2, L3
- Strategies: Multi-factor authentication

### ISM-1679 — Multi-factor authentication is used to authenticate users to third-party online services that process, store or communicate their organisation’s sensitive data.
- Applicable maturity: L1, L2, L3
- Strategies: Multi-factor authentication

### ISM-1680 — Multi-factor authentication (where available) is used to authenticate users to third-party online services that process, store or communicate their organisation’s non-sensitive data.
- Applicable maturity: L1, L2, L3
- Strategies: Multi-factor authentication

### ISM-1892 — Multi-factor authentication is used to authenticate users to their organisation’s online customer services that process, store or communicate their organisation’s sensitive customer data.
- Applicable maturity: L1, L2, L3
- Strategies: Multi-factor authentication

### ISM-1893 — Multi-factor authentication is used to authenticate users to third-party online customer services that process, store or communicate their organisation’s sensitive customer data.
- Applicable maturity: L1, L2, L3
- Strategies: Multi-factor authentication

### ISM-1681 — Multi-factor authentication is used to authenticate customers to online customer services that process, store or communicate sensitive customer data.
- Applicable maturity: L1, L2, L3
- Strategies: Multi-factor authentication

### ISM-1173 — Multi-factor authentication is used to authenticate privileged users of systems.
- Applicable maturity: L2, L3
- Strategies: Multi-factor authentication

### ISM-0974 — Multi-factor authentication is used to authenticate unprivileged users of systems.
- Applicable maturity: L2, L3
- Strategies: Multi-factor authentication

### ISM-1505 — Multi-factor authentication is used to authenticate users of data repositories.
- Applicable maturity: L3
- Strategies: Multi-factor authentication

### ISM-1401 — Multi-factor authentication uses either: something users have and something users know, or something users have that is unlocked by something users know or are.
- Applicable maturity: L1, L2, L3
- Strategies: Multi-factor authentication

### ISM-1872 — Multi-factor authentication used for authenticating users of online services is phishing-resistant.
- Applicable maturity: L2, L3
- Strategies: Multi-factor authentication

### ISM-1873 — Multi-factor authentication used for authenticating customers of online customer services provides a phishing-resistant option.
- Applicable maturity: L2
- Strategies: Multi-factor authentication

### ISM-1874 — Multi-factor authentication used for authenticating customers of online customer services is phishing-resistant.
- Applicable maturity: L3
- Strategies: Multi-factor authentication

### ISM-1682 — Multi-factor authentication used for authenticating users of systems is phishing-resistant.
- Applicable maturity: L2, L3
- Strategies: Multi-factor authentication

### ISM-1894 — Multi-factor authentication used for authenticating users of data repositories is phishing-resistant.
- Applicable maturity: L3
- Strategies: Multi-factor authentication

### ISM-1683 — Successful and unsuccessful multi-factor authentication events are centrally logged.
- Applicable maturity: L2, L3
- Strategies: Multi-factor authentication

### ISM-1685 — Credentials for break glass accounts, local administrator accounts and service accounts are long, unique, unpredictable and managed.
- Applicable maturity: L2, L3
- Strategies: Restrict administrative privileges

### ISM-1896 — Memory integrity functionality is enabled.
- Applicable maturity: L3
- Strategies: Restrict administrative privileges

### ISM-1861 — Local Security Authority protection functionality is enabled.
- Applicable maturity: L3
- Strategies: Restrict administrative privileges

### ISM-1686 — Credential Guard functionality is enabled.
- Applicable maturity: L3
- Strategies: Restrict administrative privileges

### ISM-1897 — Remote Credential Guard functionality is enabled.
- Applicable maturity: L3
- Strategies: Restrict administrative privileges

### ISM-1898 — Secure Admin Workstations are used in the performance of administrative activities.
- Applicable maturity: L3
- Strategies: Restrict administrative privileges

### ISM-1380 — Privileged users use separate privileged and unprivileged operating environments.
- Applicable maturity: L1, L2, L3
- Strategies: Restrict administrative privileges

### ISM-1687 — Privileged operating environments are not virtualised within unprivileged operating environments.
- Applicable maturity: L2, L3
- Strategies: Restrict administrative privileges

### ISM-1688 — Unprivileged user accounts cannot logon to privileged operating environments.
- Applicable maturity: L1, L2, L3
- Strategies: Restrict administrative privileges

### ISM-1689 — Privileged user accounts (excluding local administrator accounts) cannot logon to unprivileged operating environments.
- Applicable maturity: L1, L2, L3
- Strategies: Restrict administrative privileges

### ISM-1387 — Administrative activities are conducted through jump servers.
- Applicable maturity: L2, L3
- Strategies: Restrict administrative privileges

### ISM-1807 — An automated method of asset discovery is used at least fortnightly to support the detection of assets for subsequent vulnerability scanning activities.
- Applicable maturity: L1, L2, L3
- Strategies: Patch applications; Patch operating systems

### ISM-1808 — A vulnerability scanner with an up-to-date vulnerability database is used for vulnerability scanning activities.
- Applicable maturity: L1, L2, L3
- Strategies: Patch applications; Patch operating systems

### ISM-1698 — A vulnerability scanner is used at least daily to identify missing patches or updates for vulnerabilities in online services.
- Applicable maturity: L1, L2, L3
- Strategies: Patch applications

### ISM-1699 — A vulnerability scanner is used at least weekly to identify missing patches or updates for vulnerabilities in office productivity suites, web browsers and their extensions, email clients, PDF applications, and security products.
- Applicable maturity: L1, L2, L3
- Strategies: Patch applications

### ISM-1700 — A vulnerability scanner is used at least fortnightly to identify missing patches or updates for vulnerabilities in applications other than office productivity suites, web browsers and their extensions, email clients, PDF applications, and security products.
- Applicable maturity: L2, L3
- Strategies: Patch applications

### ISM-1701 — A vulnerability scanner is used at least daily to identify missing patches or updates for vulnerabilities in operating systems of internet-facing servers and internet-facing network devices.
- Applicable maturity: L1, L2, L3
- Strategies: Patch operating systems

### ISM-1702 — A vulnerability scanner is used at least fortnightly to identify missing patches or updates for vulnerabilities in operating systems of workstations, non-internet-facing servers and non-internet-facing network devices.
- Applicable maturity: L1, L2, L3
- Strategies: Patch operating systems

### ISM-1703 — A vulnerability scanner is used at least fortnightly to identify missing patches or updates for vulnerabilities in drivers.
- Applicable maturity: L3
- Strategies: Patch operating systems

### ISM-1900 — A vulnerability scanner is used at least fortnightly to identify missing patches or updates for vulnerabilities in firmware.
- Applicable maturity: L3
- Strategies: Patch operating systems

### ISM-1876 — Patches, updates or other vendor mitigations for vulnerabilities in online services are applied within 48 hours of release when vulnerabilities are assessed as critical by vendors or when working exploits exist.
- Applicable maturity: L1, L2, L3
- Strategies: Patch applications

### ISM-1690 — Patches, updates or other vendor mitigations for vulnerabilities in online services are applied within two weeks of release when vulnerabilities are assessed as non-critical by vendors and no working exploits exist.
- Applicable maturity: L1, L2, L3
- Strategies: Patch applications

### ISM-1691 — Patches, updates or other vendor mitigations for vulnerabilities in office productivity suites, web browsers and their extensions, email clients, PDF applications, and security products are applied within two weeks of release.
- Applicable maturity: L1, L2
- Strategies: Patch applications

### ISM-1692 — Patches, updates or other vendor mitigations for vulnerabilities in office productivity suites, web browsers and their extensions, email clients, PDF applications, and security products are applied within 48 hours of release when vulnerabilities are assessed as critical by vendors or when working exploits exist.
- Applicable maturity: L3
- Strategies: Patch applications

### ISM-1901 — Patches, updates or other vendor mitigations for vulnerabilities in office productivity suites, web browsers and their extensions, email clients, PDF applications, and security products are applied within two weeks of release when vulnerabilities are assessed as non-critical by vendors and no working exploits exist.
- Applicable maturity: L3
- Strategies: Patch applications

### ISM-1693 — Patches, updates or other vendor mitigations for vulnerabilities in applications other than office productivity suites, web browsers and their extensions, email clients, PDF applications, and security products are applied within one month of release.
- Applicable maturity: L2, L3
- Strategies: Patch applications

### ISM-1877 — Patches, updates or other vendor mitigations for vulnerabilities in operating systems of internet-facing servers and internet-facing network devices are applied within 48 hours of release when vulnerabilities are assessed as critical by vendors or when working exploits exist.
- Applicable maturity: L1, L2, L3
- Strategies: Patch operating systems

### ISM-1694 — Patches, updates or other vendor mitigations for vulnerabilities in operating systems of internet-facing servers and internet-facing network devices are applied within two weeks of release when vulnerabilities are assessed as non-critical by vendors and no working exploits exist.
- Applicable maturity: L1, L2, L3
- Strategies: Patch operating systems

### ISM-1695 — Patches, updates or other vendor mitigations for vulnerabilities in operating systems of workstations, non-internet-facing servers and non-internet-facing network devices are applied within one month of release.
- Applicable maturity: L1, L2
- Strategies: Patch operating systems

### ISM-1696 — Patches, updates or other vendor mitigations for vulnerabilities in operating systems of workstations, non-internet-facing servers and non-internet-facing network devices are applied within 48 hours of release when vulnerabilities are assessed as critical by vendors or when working exploits exist.
- Applicable maturity: L3
- Strategies: Patch operating systems

### ISM-1902 — Patches, updates or other vendor mitigations for vulnerabilities in operating systems of workstations, non-internet-facing servers and non-internet-facing network devices are applied within one month of release when vulnerabilities are assessed as non-critical by vendors and no working exploits exist.
- Applicable maturity: L3
- Strategies: Patch operating systems

### ISM-1879 — Patches, updates or other vendor mitigations for vulnerabilities in drivers are applied within 48 hours of release when vulnerabilities are assessed as critical by vendors or when working exploits exist.
- Applicable maturity: L3
- Strategies: Patch operating systems

### ISM-1697 — Patches, updates or other vendor mitigations for vulnerabilities in drivers are applied within one month of release when vulnerabilities are assessed as non-critical by vendors and no working exploits exist.
- Applicable maturity: L3
- Strategies: Patch operating systems

### ISM-1903 — Patches, updates or other vendor mitigations for vulnerabilities in firmware are applied within 48 hours of release when vulnerabilities are assessed as critical by vendors or when working exploits exist.
- Applicable maturity: L3
- Strategies: Patch operating systems

### ISM-1904 — Patches, updates or other vendor mitigations for vulnerabilities in firmware are applied within one month of release when vulnerabilities are assessed as non-critical by vendors and no working exploits exist.
- Applicable maturity: L3
- Strategies: Patch operating systems

### ISM-1905 — Online services that are no longer supported by vendors are removed.
- Applicable maturity: L1, L2, L3
- Strategies: Patch applications

### ISM-1704 — Office productivity suites, web browsers and their extensions, email clients, PDF applications, Adobe Flash Player, and security products that are no longer supported by vendors are removed.
- Applicable maturity: L1, L2, L3
- Strategies: Patch applications

### ISM-0304 — Applications other than office productivity suites, web browsers and their extensions, email clients, PDF applications, Adobe Flash Player, and security products that are no longer supported by vendors are removed.
- Applicable maturity: L3
- Strategies: Patch applications

### ISM-1501 — Operating systems that are no longer supported by vendors are replaced.
- Applicable maturity: L1, L2, L3
- Strategies: Patch operating systems

### ISM-1511 — Backups of data, applications and settings are performed and retained in accordance with business criticality and business continuity requirements.
- Applicable maturity: L1, L2, L3
- Strategies: Regular backups

### ISM-1810 — Backups of data, applications and settings are synchronised to enable restoration to a common point in time.
- Applicable maturity: L1, L2, L3
- Strategies: Regular backups

### ISM-1811 — Backups of data, applications and settings are retained in a secure and resilient manner.
- Applicable maturity: L1, L2, L3
- Strategies: Regular backups

### ISM-1812 — Unprivileged user accounts cannot access backups belonging to other user accounts.
- Applicable maturity: L1, L2, L3
- Strategies: Regular backups

### ISM-1813 — Unprivileged user accounts cannot access their own backups.
- Applicable maturity: L3
- Strategies: Regular backups

### ISM-1705 — Privileged user accounts (excluding backup administrator accounts) cannot access backups belonging to other user accounts.
- Applicable maturity: L2, L3
- Strategies: Regular backups

### ISM-1706 — Privileged user accounts (excluding backup administrator accounts) cannot access their own backups.
- Applicable maturity: L3
- Strategies: Regular backups

### ISM-1814 — Unprivileged user accounts are prevented from modifying and deleting backups.
- Applicable maturity: L1, L2, L3
- Strategies: Regular backups

### ISM-1707 — Privileged user accounts (excluding backup administrator accounts) are prevented from modifying and deleting backups.
- Applicable maturity: L2, L3
- Strategies: Regular backups

### ISM-1708 — Backup administrator accounts are prevented from modifying and deleting backups during their retention period.
- Applicable maturity: L3
- Strategies: Regular backups

### ISM-1515 — Restoration of data, applications and settings from backups to a common point in time is tested as part of disaster recovery exercises.
- Applicable maturity: L1, L2, L3
- Strategies: Regular backups

### ISM-1815 — Event logs are protected from unauthorised modification and deletion.
- Applicable maturity: L2, L3
- Strategies: Multi-factor authentication; Restrict administrative privileges; Application control; User application hardening

### ISM-1906 — Event logs from internet-facing servers are analysed in a timely manner to detect cybersecurity events.
- Applicable maturity: L2, L3
- Strategies: Multi-factor authentication; Restrict administrative privileges; Application control; User application hardening

### ISM-1907 — Event logs from non-internet-facing servers are analysed in a timely manner to detect cybersecurity events.
- Applicable maturity: L3
- Strategies: Multi-factor authentication; Restrict administrative privileges; Application control; User application hardening

### ISM-0109 — Event logs from workstations are analysed in a timely manner to detect cybersecurity events.
- Applicable maturity: L3
- Strategies: Multi-factor authentication; Restrict administrative privileges; Application control; User application hardening

### ISM-1228 — Cybersecurity events are analysed in a timely manner to identify cybersecurity incidents.
- Applicable maturity: L2, L3
- Strategies: Multi-factor authentication; Restrict administrative privileges; Application control; User application hardening

## Views by mitigation strategy (links only)

Links below reference the canonical requirement descriptions above. Maturity levels are shown inline to avoid repeating long text.

### Application control
- [ISM-0843](#ism-0843) — L1, L2, L3
- [ISM-1490](#ism-1490) — L2, L3
- [ISM-1656](#ism-1656) — L3
- [ISM-1870](#ism-1870) — L1, L2, L3
- [ISM-1871](#ism-1871) — L2, L3
- [ISM-1657](#ism-1657) — L1, L2, L3
- [ISM-1658](#ism-1658) — L3
- [ISM-1544](#ism-1544) — L2, L3
- [ISM-1659](#ism-1659) — L3
- [ISM-1582](#ism-1582) — L2, L3
- [ISM-1660](#ism-1660) — L2, L3
- [ISM-1815](#ism-1815) — L2, L3
- [ISM-1906](#ism-1906) — L2, L3
- [ISM-1907](#ism-1907) — L3
- [ISM-0109](#ism-0109) — L3
- [ISM-1228](#ism-1228) — L2, L3

### Multi-factor authentication
- [ISM-1504](#ism-1504) — L1, L2, L3
- [ISM-1679](#ism-1679) — L1, L2, L3
- [ISM-1680](#ism-1680) — L1, L2, L3
- [ISM-1892](#ism-1892) — L1, L2, L3
- [ISM-1893](#ism-1893) — L1, L2, L3
- [ISM-1681](#ism-1681) — L1, L2, L3
- [ISM-1173](#ism-1173) — L2, L3
- [ISM-0974](#ism-0974) — L2, L3
- [ISM-1505](#ism-1505) — L3
- [ISM-1401](#ism-1401) — L1, L2, L3
- [ISM-1872](#ism-1872) — L2, L3
- [ISM-1873](#ism-1873) — L2
- [ISM-1874](#ism-1874) — L3
- [ISM-1682](#ism-1682) — L2, L3
- [ISM-1894](#ism-1894) — L3
- [ISM-1683](#ism-1683) — L2, L3
- [ISM-0123](#ism-0123) — L2, L3
- [ISM-0140](#ism-0140) — L2, L3
- [ISM-1819](#ism-1819) — L2, L3
- [ISM-1815](#ism-1815) — L2, L3
- [ISM-1906](#ism-1906) — L2, L3
- [ISM-1907](#ism-1907) — L3
- [ISM-0109](#ism-0109) — L3
- [ISM-1228](#ism-1228) — L2, L3

### Patch applications
- [ISM-1807](#ism-1807) — L1, L2, L3
- [ISM-1808](#ism-1808) — L1, L2, L3
- [ISM-1698](#ism-1698) — L1, L2, L3
- [ISM-1699](#ism-1699) — L1, L2, L3
- [ISM-1700](#ism-1700) — L2, L3
- [ISM-1876](#ism-1876) — L1, L2, L3
- [ISM-1690](#ism-1690) — L1, L2, L3
- [ISM-1691](#ism-1691) — L1, L2
- [ISM-1692](#ism-1692) — L3
- [ISM-1901](#ism-1901) — L3
- [ISM-1693](#ism-1693) — L2, L3
- [ISM-1905](#ism-1905) — L1, L2, L3
- [ISM-1704](#ism-1704) — L1, L2, L3
- [ISM-0304](#ism-0304) — L3

### Patch operating systems
- [ISM-1807](#ism-1807) — L1, L2, L3
- [ISM-1808](#ism-1808) — L1, L2, L3
- [ISM-1701](#ism-1701) — L1, L2, L3
- [ISM-1702](#ism-1702) — L1, L2, L3
- [ISM-1703](#ism-1703) — L3
- [ISM-1900](#ism-1900) — L3
- [ISM-1694](#ism-1694) — L1, L2, L3
- [ISM-1877](#ism-1877) — L1, L2, L3
- [ISM-1695](#ism-1695) — L1, L2
- [ISM-1696](#ism-1696) — L3
- [ISM-1902](#ism-1902) — L3
- [ISM-1879](#ism-1879) — L3
- [ISM-1697](#ism-1697) — L3
- [ISM-1903](#ism-1903) — L3
- [ISM-1904](#ism-1904) — L3
- [ISM-1501](#ism-1501) — L1, L2, L3
- [ISM-1407](#ism-1407) — L3

### Regular backups
- [ISM-1511](#ism-1511) — L1, L2, L3
- [ISM-1810](#ism-1810) — L1, L2, L3
- [ISM-1811](#ism-1811) — L1, L2, L3
- [ISM-1812](#ism-1812) — L1, L2, L3
- [ISM-1813](#ism-1813) — L3
- [ISM-1705](#ism-1705) — L2, L3
- [ISM-1706](#ism-1706) — L3
- [ISM-1814](#ism-1814) — L1, L2, L3
- [ISM-1707](#ism-1707) — L2, L3
- [ISM-1708](#ism-1708) — L3
- [ISM-1515](#ism-1515) — L1, L2, L3

### Restrict administrative privileges
- [ISM-1507](#ism-1507) — L1, L2, L3
- [ISM-1508](#ism-1508) — L3
- [ISM-1175](#ism-1175) — L1, L2, L3
- [ISM-1883](#ism-1883) — L1, L2, L3
- [ISM-1649](#ism-1649) — L3
- [ISM-0445](#ism-0445) — L1, L2, L3
- [ISM-1509](#ism-1509) — L2, L3
- [ISM-1650](#ism-1650) — L2, L3
- [ISM-1648](#ism-1648) — L2, L3
- [ISM-1647](#ism-1647) — L2, L3
- [ISM-1896](#ism-1896) — L3
- [ISM-1861](#ism-1861) — L3
- [ISM-1686](#ism-1686) — L3
- [ISM-1897](#ism-1897) — L3
- [ISM-1898](#ism-1898) — L3
- [ISM-1380](#ism-1380) — L1, L2, L3
- [ISM-1687](#ism-1687) — L2, L3
- [ISM-1688](#ism-1688) — L1, L2, L3
- [ISM-1689](#ism-1689) — L1, L2, L3
- [ISM-1387](#ism-1387) — L2, L3
- [ISM-1815](#ism-1815) — L2, L3
- [ISM-1906](#ism-1906) — L2, L3
- [ISM-1907](#ism-1907) — L3
- [ISM-0109](#ism-0109) — L3
- [ISM-1228](#ism-1228) — L2, L3
- [ISM-0123](#ism-0123) — L2, L3
- [ISM-0140](#ism-0140) — L2, L3
- [ISM-1819](#ism-1819) — L2, L3

### Restrict Microsoft Office macros
- [ISM-1671](#ism-1671) — L1, L2, L3
- [ISM-1488](#ism-1488) — L1, L2, L3
- [ISM-1672](#ism-1672) — L1, L2, L3
- [ISM-1673](#ism-1673) — L2, L3
- [ISM-1674](#ism-1674) — L3
- [ISM-1890](#ism-1890) — L3
- [ISM-1487](#ism-1487) — L3
- [ISM-1675](#ism-1675) — L3
- [ISM-1891](#ism-1891) — L3
- [ISM-1676](#ism-1676) — L3
- [ISM-1489](#ism-1489) — L1, L2, L3

### User application hardening
- [ISM-1654](#ism-1654) — L1, L2, L3
- [ISM-1486](#ism-1486) — L1, L2, L3
- [ISM-1485](#ism-1485) — L1, L2, L3
- [ISM-1585](#ism-1585) — L1, L2, L3
- [ISM-1412](#ism-1412) — L2, L3
- [ISM-1670](#ism-1670) — L2, L3
- [ISM-1860](#ism-1860) — L2, L3
- [ISM-1824](#ism-1824) — L2, L3
- [ISM-1889](#ism-1889) — L2, L3
- [ISM-1621](#ism-1621) — L3
- [ISM-1622](#ism-1622) — L3
- [ISM-1623](#ism-1623) — L2, L3
- [ISM-1667](#ism-1667) — L2, L3
- [ISM-1668](#ism-1668) — L2, L3
- [ISM-1669](#ism-1669) — L2, L3
- [ISM-1542](#ism-1542) — L2, L3
- [ISM-1859](#ism-1859) — L2, L3
- [ISM-1823](#ism-1823) — L2, L3
- [ISM-1815](#ism-1815) — L2, L3
- [ISM-1906](#ism-1906) — L2, L3
- [ISM-1907](#ism-1907) — L3
- [ISM-0109](#ism-0109) — L3
- [ISM-1228](#ism-1228) — L2, L3