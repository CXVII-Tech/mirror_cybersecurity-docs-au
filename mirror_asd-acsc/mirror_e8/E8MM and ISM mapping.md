# Essential Eight maturity model and ISM mapping

## Maturity Level One

### Patch applications

| ISM Control | Essential Eight Requirement |
| --- | --- |
| ISM-1807 | An automated method of asset discovery is used at least fortnightly to support the detection of assets for subsequent vulnerability scanning activities. |
| ISM-1808 | A vulnerability scanner with an up-to-date vulnerability database is used for vulnerability scanning activities. |
| ISM-1698 | A vulnerability scanner is used at least daily to identify missing patches or updates for vulnerabilities in online services. |
| ISM-1699 | A vulnerability scanner is used at least weekly to identify missing patches or updates for vulnerabilities in office productivity suites, web browsers and their extensions, email clients, PDF software, and security products. |
| ISM-1876 | Patches, updates or other vendor mitigations for vulnerabilities in online services are applied within 48 hours of release when vulnerabilities are assessed as critical by vendors or when working exploits exist. |
| ISM-1690 | Patches, updates or other vendor mitigations for vulnerabilities in online services are applied within two weeks of release when vulnerabilities are assessed as non-critical by vendors and no working exploits exist. |
| ISM-1691 | Patches, updates or other vendor mitigations for vulnerabilities in office productivity suites, web browsers and their extensions, email clients, PDF software, and security products are applied within two weeks of release. |
| ISM-1905 | Online services that are no longer supported by vendors are removed. |
| ISM-1704 | Office productivity suites, web browsers and their extensions, email clients, PDF software, Adobe Flash Player, and security products that are no longer supported by vendors are removed. |

### Patch operating systems

| ISM Control | Essential Eight Requirement |
| --- | --- |
| ISM-1807 | An automated method of asset discovery is used at least fortnightly to support the detection of assets for subsequent vulnerability scanning activities. |
| ISM-1808 | A vulnerability scanner with an up-to-date vulnerability database is used for vulnerability scanning activities. |
| ISM-1701 | A vulnerability scanner is used at least daily to identify missing patches or updates for vulnerabilities in operating systems of internet-facing servers and internet-facing network devices. |
| ISM-1702 | A vulnerability scanner is used at least fortnightly to identify missing patches or updates for vulnerabilities in operating systems of workstations, non-internet-facing servers and non-internet-facing network devices. |
| ISM-1877 | Patches, updates or other vendor mitigations for vulnerabilities in operating systems of internet-facing servers and internet-facing network devices are applied within 48 hours of release when vulnerabilities are assessed as critical by vendors or when working exploits exist. |
| ISM-1694 | Patches, updates or other vendor mitigations for vulnerabilities in operating systems of internet-facing servers and internet-facing network devices are applied within two weeks of release when vulnerabilities are assessed as non-critical by vendors and no working exploits exist. |
| ISM-1695 | Patches, updates or other vendor mitigations for vulnerabilities in operating systems of workstations, non-internet-facing servers and non-internet-facing network devices are applied within one month of release. |
| ISM-1501 | Operating systems that are no longer supported by vendors are replaced. |

### Multi-factor authentication

| ISM Control | Essential Eight Requirement |
| --- | --- |
| ISM-1504 | Multi-factor authentication is used to authenticate users to their organisation's online services that process, store or communicate their organisation's sensitive data. |
| ISM-1679 | Multi-factor authentication is used to authenticate users to third-party online services that process, store or communicate their organisation's sensitive data. |
| ISM-1680 | Multi-factor authentication (where available) is used to authenticate users to third-party online services that process, store or communicate their organisation's non-sensitive data. |
| ISM-1892 | Multi-factor authentication is used to authenticate users to their organisation's online customer services that process, store or communicate their organisation's sensitive customer data. |
| ISM-1893 | Multi-factor authentication is used to authenticate users to third-party online customer services that process, store or communicate their organisation's sensitive customer data. |
| ISM-1681 | Multi-factor authentication is used to authenticate customers to online customer services that process, store or communicate sensitive customer data. |
| ISM-1401 | Multi-factor authentication uses either: something users have and something users know, or something users have that is unlocked by something users know or are. |

### Restrict administrative privileges

| ISM Control | Essential Eight Requirement |
| --- | --- |
| ISM-1507 | Requests for privileged access to systems, applications and data repositories are validated when first requested. |
| ISM-0445 | Privileged users are assigned a dedicated privileged user account to be used solely for duties requiring privileged access. |
| ISM-1175 | Privileged user accounts (excluding those explicitly authorised to access online services) are prevented from accessing the internet, email and web services. |
| ISM-1883 | Privileged user accounts explicitly authorised to access online services are strictly limited to only what is required for users and services to undertake their duties. |
| ISM-1380 | Privileged users use separate privileged and unprivileged operating environments. |
| ISM-1688 | Unprivileged user accounts cannot logon to privileged operating environments. |
| ISM-1689 | Privileged user accounts (excluding local administrator accounts) cannot logon to unprivileged operating environments. |

### Application control

| ISM Control | Essential Eight Requirement |
| --- | --- |
| ISM-0843 | Application control is implemented on workstations. |
| ISM-1870 | Application control is applied to user profiles and temporary folders used by operating systems, web browsers and email clients. |
| ISM-1657 | Application control restricts the execution of executables, software libraries, scripts, installers, compiled HTML, HTML applications and control panel applets to an organisation-approved set. |

### Restrict Microsoft Office macros

| ISM Control | Essential Eight Requirement |
| --- | --- |
| ISM-1671 | Microsoft Office macros are disabled for users that do not have a demonstrated business requirement. |
| ISM-1488 | Microsoft Office macros in files originating from the internet are blocked. |
| ISM-1672 | Microsoft Office macro antivirus scanning is enabled. |
| ISM-1489 | Microsoft Office macro security settings cannot be changed by users. |

### User application hardening

| ISM Control | Essential Eight Requirement |
| --- | --- |
| ISM-1654 | Internet Explorer 11 is disabled or removed. |
| ISM-1486 | Web browsers do not process Java from the internet. |
| ISM-1485 | Web browsers do not process web advertisements from the internet. |
| ISM-1585 | Web browser security settings cannot be changed by users. |

### Regular backups

| ISM Control | Essential Eight Requirement |
| --- | --- |
| ISM-1511 | Backups of data, applications and settings are performed and retained in accordance with business criticality and business continuity requirements. |
| ISM-1810 | Backups of data, applications and settings are synchronised to enable restoration to a common point in time. |
| ISM-1811 | Backups of data, applications and settings are retained in a secure and resilient manner. |
| ISM-1515 | Restoration of data, applications and settings from backups to a common point in time is tested as part of disaster recovery exercises. |
| ISM-1812 | Unprivileged user accounts cannot access backups belonging to other user accounts. |
| ISM-1814 | Unprivileged user accounts are prevented from modifying and deleting backups. |

## Maturity Level Two

### Patch applications

| ISM Control | Essential Eight Requirement |
| --- | --- |
| ISM-1807 | An automated method of asset discovery is used at least fortnightly to support the detection of assets for subsequent vulnerability scanning activities. |
| ISM-1808 | A vulnerability scanner with an up-to-date vulnerability database is used for vulnerability scanning activities. |
| ISM-1698 | A vulnerability scanner is used at least daily to identify missing patches or updates for vulnerabilities in online services. |
| ISM-1699 | A vulnerability scanner is used at least weekly to identify missing patches or updates for vulnerabilities in office productivity suites, web browsers and their extensions, email clients, PDF software, and security products. |
| ISM-1700 | A vulnerability scanner is used at least fortnightly to identify missing patches or updates for vulnerabilities in applications other than office productivity suites, web browsers and their extensions, email clients, PDF software, and security products. |
| ISM-1876 | Patches, updates or other vendor mitigations for vulnerabilities in online services are applied within 48 hours of release when vulnerabilities are assessed as critical by vendors or when working exploits exist. |
| ISM-1690 | Patches, updates or other vendor mitigations for vulnerabilities in online services are applied within two weeks of release when vulnerabilities are assessed as non-critical by vendors and no working exploits exist. |
| ISM-1691 | Patches, updates or other vendor mitigations for vulnerabilities in office productivity suites, web browsers and their extensions, email clients, PDF software, and security products are applied within two weeks of release. |
| ISM-1693 | Patches, updates or other vendor mitigations for vulnerabilities in applications other than office productivity suites, web browsers and their extensions, email clients, PDF software, and security products are applied within one month of release. |
| ISM-1905 | Online services that are no longer supported by vendors are removed. |
| ISM-1704 | Office productivity suites, web browsers and their extensions, email clients, PDF software, Adobe Flash Player, and security products that are no longer supported by vendors are removed. |

### Patch operating systems

| ISM Control | Essential Eight Requirement |
| --- | --- |
| ISM-1807 | An automated method of asset discovery is used at least fortnightly to support the detection of assets for subsequent vulnerability scanning activities. |
| ISM-1808 | A vulnerability scanner with an up-to-date vulnerability database is used for vulnerability scanning activities. |
| ISM-1701 | A vulnerability scanner is used at least daily to identify missing patches or updates for vulnerabilities in operating systems of internet-facing servers and internet-facing network devices. |
| ISM-1702 | A vulnerability scanner is used at least fortnightly to identify missing patches or updates for vulnerabilities in operating systems of workstations, non-internet-facing servers and non-internet-facing network devices. |
| ISM-1877 | Patches, updates or other vendor mitigations for vulnerabilities in operating systems of internet-facing servers and internet-facing network devices are applied within 48 hours of release when vulnerabilities are assessed as critical by vendors or when working exploits exist. |
| ISM-1694 | Patches, updates or other vendor mitigations for vulnerabilities in operating systems of internet-facing servers and internet-facing network devices are applied within two weeks of release when vulnerabilities are assessed as non-critical by vendors and no working exploits exist. |
| ISM-1695 | Patches, updates or other vendor mitigations for vulnerabilities in operating systems of workstations, non-internet-facing servers and non-internet-facing network devices are applied within one month of release. |
| ISM-1501 | Operating systems that are no longer supported by vendors are replaced. |

### Multi-factor authentication

| ISM Control | Essential Eight Requirement |
| --- | --- |
| ISM-1504 | Multi-factor authentication is used to authenticate users to their organisation's online services that process, store or communicate their organisation's sensitive data. |
| ISM-1679 | Multi-factor authentication is used to authenticate users to third-party online services that process, store or communicate their organisation's sensitive data. |
| ISM-1680 | Multi-factor authentication (where available) is used to authenticate users to third-party online services that process, store or communicate their organisation's non-sensitive data. |
| ISM-1892 | Multi-factor authentication is used to authenticate users to their organisation's online customer services that process, store or communicate their organisation's sensitive customer data. |
| ISM-1893 | Multi-factor authentication is used to authenticate users to third-party online customer services that process, store or communicate their organisation's sensitive customer data. |
| ISM-1681 | Multi-factor authentication is used to authenticate customers to online customer services that process, store or communicate sensitive customer data. |
| ISM-1173 | Multi-factor authentication is used to authenticate privileged users of systems. |
| ISM-0974 | Multi-factor authentication is used to authenticate unprivileged users of systems. |
| ISM-1401 | Multi-factor authentication uses either: something users have and something users know, or something users have that is unlocked by something users know or are. |
| ISM-1872 | Multi-factor authentication used for authenticating users of online services is phishing-resistant. |
| ISM-1873 | Multi-factor authentication used for authenticating customers of online customer services provides a phishing-resistant option. |
| ISM-1682 | Multi-factor authentication used for authenticating users of systems is phishing-resistant. |
| ISM-1683 | Successful and unsuccessful multi-factor authentication events are centrally logged. |
| ISM-1815 | Event logs are protected from unauthorised modification and deletion. |
| ISM-1906 | Event logs from internet-facing servers are analysed in a timely manner to detect cybersecurity events. |
| ISM-1228 | Cybersecurity events are analysed in a timely manner to identify cybersecurity incidents. |
| ISM-0123 | Cybersecurity incidents are reported to the chief information security officer, or one of their delegates, as soon as possible after they occur or are discovered. |
| ISM-0140 | Cybersecurity incidents are reported to ASD as soon as possible after they occur or are discovered. |
| ISM-1819 | Following the identification of a cybersecurity incident, the cybersecurity incident response plan is enacted. |

### Restrict administrative privileges

| ISM Control | Essential Eight Requirement |
| --- | --- |
| ISM-1507 | Requests for privileged access to systems, applications and data repositories are validated when first requested. |
| ISM-1647 | Privileged access to systems, applications and data repositories is disabled after 12 months unless revalidated. |
| ISM-1648 | Privileged access to systems and applications is disabled after 45 days of inactivity. |
| ISM-0445 | Privileged users are assigned a dedicated privileged user account to be used solely for duties requiring privileged access. |
| ISM-1175 | Privileged user accounts (excluding those explicitly authorised to access online services) are prevented from accessing the internet, email and web services. |
| ISM-1883 | Privileged user accounts explicitly authorised to access online services are strictly limited to only what is required for users and services to undertake their duties. |
| ISM-1380 | Privileged users use separate privileged and unprivileged operating environments. |
| ISM-1687 | Privileged operating environments are not virtualised within unprivileged operating environments. |
| ISM-1688 | Unprivileged user accounts cannot logon to privileged operating environments. |
| ISM-1689 | Privileged user accounts (excluding local administrator accounts) cannot logon to unprivileged operating environments. |
| ISM-1387 | Administrative activities are conducted through jump servers. |
| ISM-1685 | Credentials for break glass accounts, local administrator accounts and service accounts are long, unique, unpredictable and managed. |
| ISM-1509 | Privileged access events are centrally logged. |
| ISM-1650 | Privileged user account and security group management events are centrally logged. |
| ISM-1815 | Event logs are protected from unauthorised modification and deletion. |
| ISM-1906 | Event logs from internet-facing servers are analysed in a timely manner to detect cybersecurity events. |
| ISM-1228 | Cybersecurity events are analysed in a timely manner to identify cybersecurity incidents. |
| ISM-0123 | Cybersecurity incidents are reported to the chief information security officer, or one of their delegates, as soon as possible after they occur or are discovered. |
| ISM-0140 | Cybersecurity incidents are reported to ASD as soon as possible after they occur or are discovered. |
| ISM-1819 | Following the identification of a cybersecurity incident, the cybersecurity incident response plan is enacted. |

### Application control

| ISM Control | Essential Eight Requirement |
| --- | --- |
| ISM-0843 | Application control is implemented on workstations. |
| ISM-1490 | Application control is implemented on internet-facing servers. |
| ISM-1870 | Application control is applied to user profiles and temporary folders used by operating systems, web browsers and email clients. |
| ISM-1871 | Application control is applied to all locations other than user profiles and temporary folders used by operating systems, web browsers and email clients. |
| ISM-1657 | Application control restricts the execution of executables, software libraries, scripts, installers, compiled HTML, HTML applications and control panel applets to an organisation-approved set. |
| ISM-1544 | Microsoft's recommended application blocklist is implemented. |
| ISM-1582 | Application control rulesets are validated on an annual or more frequent basis. |
| ISM-1660 | Allowed and blocked application control events are centrally logged. |
| ISM-1815 | Event logs are protected from unauthorised modification and deletion. |
| ISM-1906 | Event logs from internet-facing servers are analysed in a timely manner to detect cybersecurity events. |
| ISM-1228 | Cybersecurity events are analysed in a timely manner to identify cybersecurity incidents. |
| ISM-0123 | Cybersecurity incidents are reported to the chief information security officer, or one of their delegates, as soon as possible after they occur or are discovered. |
| ISM-0140 | Cybersecurity incidents are reported to ASD as soon as possible after they occur or are discovered. |
| ISM-1819 | Following the identification of a cybersecurity incident, the cybersecurity incident response plan is enacted. |

### Restrict Microsoft Office macros

| ISM Control | Essential Eight Requirement |
| --- | --- |
| ISM-1671 | Microsoft Office macros are disabled for users that do not have a demonstrated business requirement. |
| ISM-1488 | Microsoft Office macros in files originating from the internet are blocked. |
| ISM-1672 | Microsoft Office macro antivirus scanning is enabled. |
| ISM-1673 | Microsoft Office macros are blocked from making Win32 API calls. |
| ISM-1489 | Microsoft Office macro security settings cannot be changed by users. |

### User application hardening

| ISM Control | Essential Eight Requirement |
| --- | --- |
| ISM-1654 | Internet Explorer 11 is disabled or removed. |
| ISM-1486 | Web browsers do not process Java from the internet. |
| ISM-1485 | Web browsers do not process web advertisements from the internet. |
| ISM-1412 | Web browsers are hardened using ASD and vendor hardening guidance, with the most restrictive guidance taking precedence when conflicts occur. |
| ISM-1585 | Web browser security settings cannot be changed by users. |
| ISM-1667 | Microsoft Office is blocked from creating child processes. |
| ISM-1668 | Microsoft Office is blocked from creating executable content. |
| ISM-1669 | Microsoft Office is blocked from injecting code into other processes. |
| ISM-1542 | Microsoft Office is configured to prevent activation of Object Linking and Embedding packages. |
| ISM-1859 | Office productivity suites are hardened using ASD and vendor hardening guidance, with the most restrictive guidance taking precedence when conflicts occur. |
| ISM-1823 | Office productivity suite security settings cannot be changed by users. |
| ISM-1670 | PDF software is blocked from creating child processes. |
| ISM-1860 | PDF software is hardened using ASD and vendor hardening guidance, with the most restrictive guidance taking precedence when conflicts occur. |
| ISM-1824 | PDF software security settings cannot be changed by users. |
| ISM-1623 | PowerShell module logging, script block logging and transcription events are centrally logged. |
| ISM-1889 | Command line process creation events are centrally logged. |
| ISM-1815 | Event logs are protected from unauthorised modification and deletion. |
| ISM-1906 | Event logs from internet-facing servers are analysed in a timely manner to detect cybersecurity events. |
| ISM-1228 | Cybersecurity events are analysed in a timely manner to identify cybersecurity incidents. |
| ISM-0123 | Cybersecurity incidents are reported to the chief information security officer, or one of their delegates, as soon as possible after they occur or are discovered. |
| ISM-0140 | Cybersecurity incidents are reported to ASD as soon as possible after they occur or are discovered. |
| ISM-1819 | Following the identification of a cybersecurity incident, the cybersecurity incident response plan is enacted. |

### Regular backups

| ISM Control | Essential Eight Requirement |
| --- | --- |
| ISM-1511 | Backups of data, applications and settings are performed and retained in accordance with business criticality and business continuity requirements. |
| ISM-1810 | Backups of data, applications and settings are synchronised to enable restoration to a common point in time. |
| ISM-1811 | Backups of data, applications and settings are retained in a secure and resilient manner. |
| ISM-1515 | Restoration of data, applications and settings from backups to a common point in time is tested as part of disaster recovery exercises. |
| ISM-1812 | Unprivileged user accounts cannot access backups belonging to other user accounts. |
| ISM-1705 | Privileged user accounts (excluding backup administrator accounts) cannot access backups belonging to other user accounts. |
| ISM-1814 | Unprivileged user accounts are prevented from modifying and deleting backups. |
| ISM-1707 | Privileged user accounts (excluding backup administrator accounts) are prevented from modifying and deleting backups. |

## Maturity Level Three

### Patch applications

| ISM Control | Essential Eight Requirement |
| --- | --- |
| ISM-1807 | An automated method of asset discovery is used at least fortnightly to support the detection of assets for subsequent vulnerability scanning activities. |
| ISM-1808 | A vulnerability scanner with an up-to-date vulnerability database is used for vulnerability scanning activities. |
| ISM-1698 | A vulnerability scanner is used at least daily to identify missing patches or updates for vulnerabilities in online services. |
| ISM-1699 | A vulnerability scanner is used at least weekly to identify missing patches or updates for vulnerabilities in office productivity suites, web browsers and their extensions, email clients, PDF software, and security products. |
| ISM-1700 | A vulnerability scanner is used at least fortnightly to identify missing patches or updates for vulnerabilities in applications other than office productivity suites, web browsers and their extensions, email clients, PDF software, and security products. |
| ISM-1876 | Patches, updates or other vendor mitigations for vulnerabilities in online services are applied within 48 hours of release when vulnerabilities are assessed as critical by vendors or when working exploits exist. |
| ISM-1690 | Patches, updates or other vendor mitigations for vulnerabilities in online services are applied within two weeks of release when vulnerabilities are assessed as non-critical by vendors and no working exploits exist. |
| ISM-1692 | Patches, updates or other vendor mitigations for vulnerabilities in office productivity suites, web browsers and their extensions, email clients, PDF software, and security products are applied within 48 hours of release when vulnerabilities are assessed as critical by vendors or when working exploits exist. |
| ISM-1901 | Patches, updates or other vendor mitigations for vulnerabilities in office productivity suites, web browsers and their extensions, email clients, PDF software, and security products are applied within two weeks of release when vulnerabilities are assessed as non-critical by vendors and no working exploits exist. |
| ISM-1693 | Patches, updates or other vendor mitigations for vulnerabilities in applications other than office productivity suites, web browsers and their extensions, email clients, PDF software, and security products are applied within one month of release. |
| ISM-1905 | Online services that are no longer supported by vendors are removed. |
| ISM-1704 | Office productivity suites, web browsers and their extensions, email clients, PDF software, Adobe Flash Player, and security products that are no longer supported by vendors are removed. |
| ISM-0304 | Applications other than office productivity suites, web browsers and their extensions, email clients, PDF software, Adobe Flash Player, and security products that are no longer supported by vendors are removed. |

### Patch operating systems

| ISM Control | Essential Eight Requirement |
| --- | --- |
| ISM-1807 | An automated method of asset discovery is used at least fortnightly to support the detection of assets for subsequent vulnerability scanning activities. |
| ISM-1808 | A vulnerability scanner with an up-to-date vulnerability database is used for vulnerability scanning activities. |
| ISM-1701 | A vulnerability scanner is used at least daily to identify missing patches or updates for vulnerabilities in operating systems of internet-facing servers and internet-facing network devices. |
| ISM-1702 | A vulnerability scanner is used at least fortnightly to identify missing patches or updates for vulnerabilities in operating systems of workstations, non-internet-facing servers and non-internet-facing network devices. |
| ISM-1703 | A vulnerability scanner is used at least fortnightly to identify missing patches or updates for vulnerabilities in drivers. |
| ISM-1900 | A vulnerability scanner is used at least fortnightly to identify missing patches or updates for vulnerabilities in firmware. |
| ISM-1877 | Patches, updates or other vendor mitigations for vulnerabilities in operating systems of internet-facing servers and internet-facing network devices are applied within 48 hours of release when vulnerabilities are assessed as critical by vendors or when working exploits exist. |
| ISM-1694 | Patches, updates or other vendor mitigations for vulnerabilities in operating systems of internet-facing servers and internet-facing network devices are applied within two weeks of release when vulnerabilities are assessed as non-critical by vendors and no working exploits exist. |
| ISM-1696 | Patches, updates or other vendor mitigations for vulnerabilities in operating systems of workstations, non-internet-facing servers and non-internet-facing network devices are applied within 48 hours of release when vulnerabilities are assessed as critical by vendors or when working exploits exist. |
| ISM-1902 | Patches, updates or other vendor mitigations for vulnerabilities in operating systems of workstations, non-internet-facing servers and non-internet-facing network devices are applied within one month of release when vulnerabilities are assessed as non-critical by vendors and no working exploits exist. |
| ISM-1879 | Patches, updates or other vendor mitigations for vulnerabilities in drivers are applied within 48 hours of release when vulnerabilities are assessed as critical by vendors or when working exploits exist. |
| ISM-1697 | Patches, updates or other vendor mitigations for vulnerabilities in drivers are applied within one month of release when vulnerabilities are assessed as non-critical by vendors and no working exploits exist. |
| ISM-1903 | Patches, updates or other vendor mitigations for vulnerabilities in firmware are applied within 48 hours of release when vulnerabilities are assessed as critical by vendors or when working exploits exist. |
| ISM-1904 | Patches, updates or other vendor mitigations for vulnerabilities in firmware are applied within one month of release when vulnerabilities are assessed as non-critical by vendors and no working exploits exist. |
| ISM-1407 | The latest release, or the previous release, of operating systems are used. |
| ISM-1501 | Operating systems that are no longer supported by vendors are replaced. |

### Multi-factor authentication

| ISM Control | Essential Eight Requirement |
| --- | --- |
| ISM-1504 | Multi-factor authentication is used to authenticate users to their organisation's online services that process, store or communicate their organisation's sensitive data. |
| ISM-1679 | Multi-factor authentication is used to authenticate users to third-party online services that process, store or communicate their organisation's sensitive data. |
| ISM-1680 | Multi-factor authentication (where available) is used to authenticate users to third-party online services that process, store or communicate their organisation's non-sensitive data. |
| ISM-1892 | Multi-factor authentication is used to authenticate users to their organisation's online customer services that process, store or communicate their organisation's sensitive customer data. |
| ISM-1893 | Multi-factor authentication is used to authenticate users to third-party online customer services that process, store or communicate their organisation's sensitive customer data. |
| ISM-1681 | Multi-factor authentication is used to authenticate customers to online customer services that process, store or communicate sensitive customer data. |
| ISM-1173 | Multi-factor authentication is used to authenticate privileged users of systems. |
| ISM-0974 | Multi-factor authentication is used to authenticate unprivileged users of systems. |
| ISM-1505 | Multi-factor authentication is used to authenticate users of data repositories. |
| ISM-1401 | Multi-factor authentication uses either: something users have and something users know, or something users have that is unlocked by something users know or are. |
| ISM-1872 | Multi-factor authentication used for authenticating users of online services is phishing-resistant. |
| ISM-1874 | Multi-factor authentication used for authenticating customers of online customer services is phishing-resistant. |
| ISM-1682 | Multi-factor authentication used for authenticating users of systems is phishing-resistant. |
| ISM-1894 | Multi-factor authentication used for authenticating users of data repositories is phishing-resistant. |
| ISM-1683 | Successful and unsuccessful multi-factor authentication events are centrally logged. |
| ISM-1815 | Event logs are protected from unauthorised modification and deletion. |
| ISM-1906 | Event logs from internet-facing servers are analysed in a timely manner to detect cybersecurity events. |
| ISM-1907 | Event logs from non-internet-facing servers are analysed in a timely manner to detect cybersecurity events. |
| ISM-0109 | Event logs from workstations are analysed in a timely manner to detect cybersecurity events. |
| ISM-1228 | Cybersecurity events are analysed in a timely manner to identify cybersecurity incidents. |
| ISM-0123 | Cybersecurity incidents are reported to the chief information security officer, or one of their delegates, as soon as possible after they occur or are discovered. |
| ISM-0140 | Cybersecurity incidents are reported to ASD as soon as possible after they occur or are discovered. |
| ISM-1819 | Following the identification of a cybersecurity incident, the cybersecurity incident response plan is enacted. |

### Restrict administrative privileges

| ISM Control | Essential Eight Requirement |
| --- | --- |
| ISM-1507 | Requests for privileged access to systems, applications and data repositories are validated when first requested. |
| ISM-1647 | Privileged access to systems, applications and data repositories is disabled after 12 months unless revalidated. |
| ISM-1648 | Privileged access to systems and applications is disabled after 45 days of inactivity. |
| ISM-0445 | Privileged users are assigned a dedicated privileged user account to be used solely for duties requiring privileged access. |
| ISM-1508 | Privileged access to systems, applications and data repositories is limited to only what is required for users and services to undertake their duties. |
| ISM-1175 | Privileged user accounts (excluding those explicitly authorised to access online services) are prevented from accessing the internet, email and web services. |
| ISM-1883 | Privileged user accounts explicitly authorised to access online services are strictly limited to only what is required for users and services to undertake their duties. |
| ISM-1898 | Secure Admin Workstations are used in the performance of administrative activities. |
| ISM-1380 | Privileged users use separate privileged and unprivileged operating environments. |
| ISM-1687 | Privileged operating environments are not virtualised within unprivileged operating environments. |
| ISM-1688 | Unprivileged user accounts cannot logon to privileged operating environments. |
| ISM-1689 | Privileged user accounts (excluding local administrator accounts) cannot logon to unprivileged operating environments. |
| ISM-1649 | Just-in-time administration is used for administering systems and applications. |
| ISM-1387 | Administrative activities are conducted through jump servers. |
| ISM-1685 | Credentials for break glass accounts, local administrator accounts and service accounts are long, unique, unpredictable and managed. |
| ISM-1896 | Memory integrity functionality is enabled. |
| ISM-1861 | Local Security Authority protection functionality is enabled. |
| ISM-1686 | Credential Guard functionality is enabled. |
| ISM-1897 | Remote Credential Guard functionality is enabled. |
| ISM-1509 | Privileged access events are centrally logged. |
| ISM-1650 | Privileged user account and security group management events are centrally logged. |
| ISM-1815 | Event logs are protected from unauthorised modification and deletion. |
| ISM-1906 | Event logs from internet-facing servers are analysed in a timely manner to detect cybersecurity events. |
| ISM-1907 | Event logs from non-internet-facing servers are analysed in a timely manner to detect cybersecurity events. |
| ISM-0109 | Event logs from workstations are analysed in a timely manner to detect cybersecurity events. |
| ISM-1228 | Cybersecurity events are analysed in a timely manner to identify cybersecurity incidents. |
| ISM-0123 | Cybersecurity incidents are reported to the chief information security officer, or one of their delegates, as soon as possible after they occur or are discovered. |
| ISM-0140 | Cybersecurity incidents are reported to ASD as soon as possible after they occur or are discovered. |
| ISM-1819 | Following the identification of a cybersecurity incident, the cybersecurity incident response plan is enacted. |

### Application control

| ISM Control | Essential Eight Requirement |
| --- | --- |
| ISM-0843 | Application control is implemented on workstations. |
| ISM-1490 | Application control is implemented on internet-facing servers. |
| ISM-1656 | Application control is implemented on non-internet-facing servers. |
| ISM-1870 | Application control is applied to user profiles and temporary folders used by operating systems, web browsers and email clients. |
| ISM-1871 | Application control is applied to all locations other than user profiles and temporary folders used by operating systems, web browsers and email clients. |
| ISM-1657 | Application control restricts the execution of executables, software libraries, scripts, installers, compiled HTML, HTML applications and control panel applets to an organisation-approved set. |
| ISM-1658 | Application control restricts the execution of drivers to an organisation-approved set. |
| ISM-1544 | Microsoft's recommended application blocklist is implemented. |
| ISM-1659 | Microsoft's vulnerable driver blocklist is implemented. |
| ISM-1582 | Application control rulesets are validated on an annual or more frequent basis. |
| ISM-1660 | Allowed and blocked application control events are centrally logged. |
| ISM-1815 | Event logs are protected from unauthorised modification and deletion. |
| ISM-1906 | Event logs from internet-facing servers are analysed in a timely manner to detect cybersecurity events. |
| ISM-1907 | Event logs from non-internet-facing servers are analysed in a timely manner to detect cybersecurity events. |
| ISM-0109 | Event logs from workstations are analysed in a timely manner to detect cybersecurity events. |
| ISM-1228 | Cybersecurity events are analysed in a timely manner to identify cybersecurity incidents. |
| ISM-0123 | Cybersecurity incidents are reported to the chief information security officer, or one of their delegates, as soon as possible after they occur or are discovered. |
| ISM-0140 | Cybersecurity incidents are reported to ASD as soon as possible after they occur or are discovered. |
| ISM-1819 | Following the identification of a cybersecurity incident, the cybersecurity incident response plan is enacted. |

### Restrict Microsoft Office macros

| ISM Control | Essential Eight Requirement |
| --- | --- |
| ISM-1671 | Microsoft Office macros are disabled for users that do not have a demonstrated business requirement. |
| ISM-1674 | Only Microsoft Office macros running from within a sandboxed environment, a Trusted Location or that are digitally signed by a trusted publisher are allowed to execute. |
| ISM-1890 | Microsoft Office macros are checked to ensure they are free of malicious code before being digitally signed or placed within Trusted Locations. |
| ISM-1487 | Only privileged users responsible for checking that Microsoft Office macros are free of malicious code can write to and modify content within Trusted Locations. |
| ISM-1675 | Microsoft Office macros digitally signed by an untrusted publisher cannot be enabled via the Message Bar or Backstage View. |
| ISM-1891 | Microsoft Office macros digitally signed by signatures other than V3 signatures cannot be enabled via the Message Bar or Backstage View. |
| ISM-1676 | Microsoft Office's list of trusted publishers is validated on an annual or more frequent basis. |
| ISM-1488 | Microsoft Office macros in files originating from the internet are blocked. |
| ISM-1672 | Microsoft Office macro antivirus scanning is enabled. |
| ISM-1673 | Microsoft Office macros are blocked from making Win32 API calls. |
| ISM-1489 | Microsoft Office macro security settings cannot be changed by users. |

### User application hardening

| ISM Control | Essential Eight Requirement |
| --- | --- |
| ISM-1654 | Internet Explorer 11 is disabled or removed. |
| ISM-1486 | Web browsers do not process Java from the internet. |
| ISM-1485 | Web browsers do not process web advertisements from the internet. |
| ISM-1412 | Web browsers are hardened using ASD and vendor hardening guidance, with the most restrictive guidance taking precedence when conflicts occur. |
| ISM-1585 | Web browser security settings cannot be changed by users. |
| ISM-1667 | Microsoft Office is blocked from creating child processes. |
| ISM-1668 | Microsoft Office is blocked from creating executable content. |
| ISM-1669 | Microsoft Office is blocked from injecting code into other processes. |
| ISM-1542 | Microsoft Office is configured to prevent activation of Object Linking and Embedding packages. |
| ISM-1859 | Office productivity suites are hardened using ASD and vendor hardening guidance, with the most restrictive guidance taking precedence when conflicts occur. |
| ISM-1823 | Office productivity suite security settings cannot be changed by users. |
| ISM-1670 | PDF software is blocked from creating child processes. |
| ISM-1860 | PDF software is hardened using ASD and vendor hardening guidance, with the most restrictive guidance taking precedence when conflicts occur. |
| ISM-1824 | PDF software security settings cannot be changed by users. |
| ISM-1655 | .NET Framework 3.5 (includes .NET 2.0 and 3.0) is disabled or removed. |
| ISM-1621 | Windows PowerShell 2.0 is disabled or removed. |
| ISM-1622 | PowerShell is configured to use Constrained Language Mode. |
| ISM-1623 | PowerShell module logging, script block logging and transcription events are centrally logged. |
| ISM-1889 | Command line process creation events are centrally logged. |
| ISM-1815 | Event logs are protected from unauthorised modification and deletion. |
| ISM-1906 | Event logs from internet-facing servers are analysed in a timely manner to detect cybersecurity events. |
| ISM-1907 | Event logs from non-internet-facing servers are analysed in a timely manner to detect cybersecurity events. |
| ISM-0109 | Event logs from workstations are analysed in a timely manner to detect cybersecurity events. |
| ISM-1228 | Cybersecurity events are analysed in a timely manner to identify cybersecurity incidents. |
| ISM-0123 | Cybersecurity incidents are reported to the chief information security officer, or one of their delegates, as soon as possible after they occur or are discovered. |
| ISM-0140 | Cybersecurity incidents are reported to ASD as soon as possible after they occur or are discovered. |
| ISM-1819 | Following the identification of a cybersecurity incident, the cybersecurity incident response plan is enacted. |

### Regular backups

| ISM Control | Essential Eight Requirement |
| --- | --- |
| ISM-1511 | Backups of data, applications and settings are performed and retained in accordance with business criticality and business continuity requirements. |
| ISM-1810 | Backups of data, applications and settings are synchronised to enable restoration to a common point in time. |
| ISM-1811 | Backups of data, applications and settings are retained in a secure and resilient manner. |
| ISM-1515 | Restoration of data, applications and settings from backups to a common point in time is tested as part of disaster recovery exercises. |
| ISM-1812 | Unprivileged user accounts cannot access backups belonging to other user accounts. |
| ISM-1813 | Unprivileged user accounts cannot access their own backups. |
| ISM-1705 | Privileged user accounts (excluding backup administrator accounts) cannot access backups belonging to other user accounts. |
| ISM-1706 | Privileged user accounts (excluding backup administrator accounts) cannot access their own backups. |
| ISM-1814 | Unprivileged user accounts are prevented from modifying and deleting backups. |
| ISM-1707 | Privileged user accounts (excluding backup administrator accounts) are prevented from modifying and deleting backups. |
| ISM-1708 | Backup administrator accounts are prevented from modifying and deleting backups during their retention period. |
