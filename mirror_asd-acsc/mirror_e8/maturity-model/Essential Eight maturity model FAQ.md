# Essential Eight maturity model FAQ

**First published:**

16 Jul 2021

**Last updated:**

28 Oct 2024

### **Content written for**

Small & medium business

Large organisations & infrastructure

Government

### **Attachments**

- [**Essential Eight maturity model FAQ (October 2024)*1.19MB .pdf***](https://www.cyber.gov.au/sites/default/files/2025-03/Essential%20Eight%20maturity%20model%20FAQ%20%28October%202024%29.pdf)

## **Introduction**

This publication was developed to answer frequently asked questions on the [*Essential Eight maturity model*](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/essential-eight) (E8MM).

## **FAQ: General questions**

### **What is the Essential Eight?**

- While no set of mitigation strategies are guaranteed to protect against all cyberthreats, organisations are recommended to implement eight essential mitigation strategies from the [*Strategies to mitigate cybersecurity incidents*](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/mitigating-cyber-security-incidents) as a baseline. This baseline, known as the Essential Eight, makes it much harder for malicious actors to compromise systems.
- The mitigation strategies that constitute the Essential Eight are: patch applications, patch operating systems, multi-factor authentication, restrict administrative privileges, application control, restrict Microsoft Office macros, user application hardening and regular backups.

### **Why should I implement the Essential Eight?**

- Implementing the Essential Eight proactively can be more cost-effective in terms of time, money and effort than having to respond to a large-scale cybersecurity incident.

### **What is the *Essential Eight maturity model*?**

- The E8MM is designed to assist organisations to implement the Essential Eight in a graduated manner based upon different levels of malicious actors’ tradecraft (i.e. tools, tactics, techniques and procedures) and targeting.
- The different maturity levels can also be used to provide a high-level indication of an organisation’s cybersecurity maturity.

### **Why update the *Essential Eight maturity model*?**

- The Australian Signals Directorate (ASD) is committed to providing cybersecurity advice that is contemporary, fit for purpose and practical. This includes regular updates to the E8MM.
- Malicious actors continually evolve their tradecraft to defeat preventative measures that organisations put in place.
- ASD continually learns of advances in malicious actors’ tradecraft through its cyberthreat intelligence and cybersecurity incident response functions.
- ASD also learns of how our cybersecurity advice is implemented within organisations as part of Essential Eight implementation assessments and uplift activities.
- Updates to the E8MM follow a thorough review by ASD, which includes consultation with government and industry partners.

### **Which version of the *Essential Eight maturity model* should be used?**

- Organisations are strongly encouraged to use the latest version of the E8MM to protect themselves against contemporary tradecraft used by malicious actors. Note, legacy versions of the E8MM will often no longer be fit for purpose due to the continual evolution of tradecraft used by malicious actors.

### **How do the *Essential Eight maturity model* and *Information security manual* relate to each other?**

- The applicability of controls within the [*Information security manual*](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/ism) (ISM) is based on the classification of data that a system will store, process or communicate whereas the E8MM is based on prioritising the implementation of controls to mitigate different levels of malicious actors’ tradecraft and targeting.
- A mapping between the E8MM and ISM is provided within the [*Essential Eight maturity model and ISM mapping*](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/essential-eight/essential-eight-maturity-model-and-ism-mapping) publication.
- The ISM also provides [OSCAL baselines for the E8MM](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/ism/ism-oscal-releases) which can be used by organisations to track their implementation of the E8MM within their governance, reporting and compliance tools.
- Organisations should consider their E8MM and ISM requirements independently. For example, an organisation contractually required to implement Maturity Level Two from the E8MM should not assume that controls within the ISM that are mapped to Maturity Level Three are out of scope when building and deploying a system. For non-corporate Commonwealth entities subject to the Department of Home Affairs’ [*Protective Security Policy Framework*](https://www.protectivesecurity.gov.au/), this means that while Maturity Level Two is considered a mandatory baseline, controls mapped to Maturity Level Three within the ISM are still applicable for their systems, however, their implementation may be risk managed.

### **Is there any training available on the *Essential Eight maturity model*?**

- ASD has developed an Essential Eight assessment course and partnered with TAFEcyber for the delivery of the course to cybersecurity professionals across Australia.
- The Essential Eight assessment course is a face-to-face three-day course that uses a blend of specialist expertise, knowledge and hands-on technical training. Further information on the [Essential Eight Assessment Course is available](https://www.tafecyber.com.au/essential-eight) from TAFEcyber.

## **FAQ: *Essential Eight maturity model* update (November 2023)**

### **What were the changes?**

- Information on changes made as part of the November 2023 update of the E8MM can be found within the associated [*Essential Eight maturity model changes*](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/essential-eight/essential-eight-maturity-model-changes) publication.

## **FAQ: Implementation questions – General**

### **Is the *Essential Eight maturity model* applicable to all systems?**

- The Essential Eight has been designed to protect organisations’ internet-connected information technology networks. While the principles behind the Essential Eight may be applied to enterprise mobility and operational technology networks, it was not designed for such purposes and alternative mitigation strategies may be more appropriate to defend against unique cyberthreats to these environments.

### **Are legacy systems out of scope?**

- It is often difficult to implement the Essential Eight, either in part or in full, on legacy systems. In such cases, ASD strongly encourages organisations to upgrade their legacy systems as a priority so that the Essential Eight can be implemented in full. While a system is in the process of being upgraded, organisations should implement compensating controls where possible to do so.

### **What maturity level should I target?**

- Generally, Maturity Level One may be suitable for small to medium enterprises, Maturity Level Two may be suitable for large enterprises, and Maturity Level Three may be suitable for critical infrastructure providers and other organisations that operate in high threat environments.
- When implementing Essential Eight requirements, organisations should identify and plan for a target maturity level suitable for their environment. Organisations should then progressively implement each maturity level until that target is achieved.
- For organisations with a target maturity level above Maturity Level One, they may choose to implement individual requirements of a higher maturity level if it is more efficient and cost-effective to do so in the long run. For example, rather than implementing physical one-time password tokens to meet Maturity Level One requirements, then later replacing them with phishing-resistant smart cards, security keys or passkeys to meet Maturity Level Two requirements, organisations may choose to implement smart cards, security keys or passkeys when implementing Maturity Level One.
- Organisations should not be penalised for implementing more robust security measures than specified for the given maturity level they are being assessed against.

### **Can I jump straight to implementing my target maturity level?**

- Organisations should progressively implement, and assess their implementation of, each maturity level until their target maturity level is achieved. Using such an approach provides organisations the opportunity to validate the correctness and robustness of their implementation of a particular maturity level before moving onto the next maturity level.
- Using a staged approach also allows organisations to:
    - assess the effectiveness of any new controls within their environment
    - monitor for any unanticipated consequences and identify any edge cases
    - address any issues identified following an assessment of their implementation
    - identify any impacted business processes, including unanticipated consequences
    - allow employees time to adjust to changes within their environment and work flows.

### **Can I implement compensating controls instead of specific Essential Eight requirements?**

- Yes. However, system owners will need to demonstrate that their compensating controls provide an equivalent level of protection to the specific Essential Eight requirements they are compensating for. This will assist in ensuring that an equivalent level of overall protection against a specified level of malicious actors’ tradecraft and targeting can be achieved and maintained.
- In cases where compensating controls are implemented, a mitigation strategy will be considered to have been fully implemented when all requirements that form that mitigation strategy have been assessed as either implemented or implemented using suitable compensating controls. However, if compensating controls are assessed as not suitable, the mitigation strategy will be assessed as either the next lowest maturity level it qualifies for or Maturity Level Zero.
- Note, system owners that seek to use risk acceptance without compensating controls, or risk transference (e.g. by sourcing cyber insurance), as justification for not implementing an entire mitigation strategy, such as application control or multi-factor authentication, will be considered to have not protected themselves against a specific class of cyberthreat and will subsequently be assessed as Maturity Level Zero for both that mitigation strategy and their overall Essential Eight implementation.

### **What is a workstation?**

- A workstation is any device that uses a desktop operating system, such as Microsoft Windows or a Linux distribution. This includes traditional desktop PCs, laptops and some tablets.

### **What is an internet-facing server?**

- An internet-facing server is any server that is directly accessible over the internet.

### **What is an online service?**

- An online service is any service that is directly accessible over the internet, including those sitting behind a perimeter firewall. For example, a web portal, a cloud service or a network device (such as a firewall or VPN concentrator).
- An example of an online service that processes, stores or communicates an organisation’s sensitive data is any cloud service that has been authorised for use with OFFICIAL: Sensitive or PROTECTED data (such as GovTeams) or any other sensitive business data.
- Examples of online services that process, store or communicate an organisation’s non-sensitive data can include web hosting services (such as GovCMS) or social media platforms (such as Facebook, Instagram, LinkedIn, YouTube and X).

### **What is a customer?**

- A customer is a person that an organisation has dealings with, typically via the consumption of goods or services. A customer does not necessarily need to purchase goods or services from the organisation.

### **What is an online customer service?**

- An online customer service is a subset of online service that is designed specifically for interaction between organisations and their customers. For example, the Australian Government’s myGov web portal.

### **What is sensitive customer data?**

- While organisations are often best placed to determine what constitutes sensitive customer data, organisations should consider the [guidance provided by the Office of the Australian Information Commissioner](https://www.oaic.gov.au/privacy/your-privacy-rights/your-personal-information/what-is-personal-information) as it relates to the [*Privacy Act 1988*](https://www.legislation.gov.au/Series/C2004A03712).

### **What is a data repository?**

- A data repository is a location in which data is stored, managed and made available to users.

### **Does ASD provide a list of approved products for implementing the Essential Eight?**

- No. Organisations should determine the suitability of particular products based on their own requirements.

### **Does ASD provide any tools to assist with assessing implementations of the Essential Eight?**

- Yes. ASD provides two tools as part of a ‘cyber toolbox’ to assist organisations with assessing implementations of the Essential Eight. These tools are the Essential Eight Maturity Verification Tool (E8MVT) and the Application Control Verification Tool (ACVT).
- Both E8MVT and ACVT are available to download via ASD’s [Partner Portal](https://partners.cyber.gov.au/).

### **Do I require a Security Information and Event Management (SIEM), Endpoint Detection and Response (EDR) or Extended Detection and Response (XDR) solution to capture, protect and monitor event logs?**

- The [*Strategies to mitigate cybersecurity incidents*](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/mitigating-cyber-security-incidents) publication recommends the use of SIEM and EDR software to centrally log and analyse system behaviour to detect compromises, while also facilitating cybersecurity incident response activities.
- MITRE’s research illustrates how various [EDR vendors can detect and respond to compromises of systems](https://attackevals.mitre-engenuity.org/enterprise/apt29/) by malicious actors.
- Recent industry advances have introduced the concept of XDR which combines SIEM and EDR functionality while adding more advanced log analysis capabilities. This often integrates cloud-based analysis of host-based sensor telemetry to link disparate alerts in order to detect compromises of systems.

### **Can I filter out events from event logs that are known to be legitimate in order to simplify event log analysis and reduce storage requirements?**

- Yes. Organisations that are comfortable that certain events have a high probability of being legitimate may choose to filter them out of event logs in order to simplify event log analysis and reduce storage requirements.

### **Do I need to perform events log analysis in real time or near real time?**

- Organisations should analyse event logs for signs of compromise in a timeframe that is reasonably practicable given the resources they have available to them.

## **FAQ: Implementation questions – Patch applications and patch operating systems**

### **My vulnerability scanning tool offers the ability to automatically detect assets on a network, can I use it as an asset discovery tool?**

- Yes. Some vulnerability scanning tools offer automatic asset discovery functionality that is equivalent to other tools developed for that sole purpose.

### **Can I perform automated asset discovery more frequently than fortnightly?**

- Yes. While automated asset discovery should be performed at least fortnightly, system owners may elect to align the frequency of asset discovery scans to more frequent timeframes used for vulnerability scans (such as daily or weekly) in order to perform both activities at the same time for optimal effect.

### **How can I find out if a vulnerability has a working exploit?**

- Vendors, ASD, news outlets and security researchers often cover exploitable vulnerabilities.
- The United States’ Cybersecurity & Infrastructure Security Agency also maintains a [*Known Exploited Vulnerabilities Catalog*](https://www.cisa.gov/known-exploited-vulnerabilities-catalog).

### **One of my vendors does not rate the criticality of vulnerabilities, what should I do?**

- ASD, news outlets and security researchers often cover critical vulnerabilities.
- Organisations may also consider the type of vulnerability, including factors such as its Common Vulnerability Scoring System score (if available), to determine if it would have likely represented a critical vulnerability.

### **Do I have 48 hours to patch from when working exploits are announced or when exploitation starts occurring?**

- The requirement to patch within 48 hours when a working exploit exists relates to the announcement of a working exploit or that exploitation is already occurring, whichever occurs first.

### **I am unable to perform rapid scanning and patching of online services, what can I do?**

- ASD encourages all organisations to consider moving their online services to mature and trustworthy cloud service providers. Depending on the type of cloud service used, this can result in significant security benefits such as the rapid identification and patching of vulnerabilities.

### **How can I remove Adobe Flash Player?**

- Information on [removing Adobe Flash Player](https://support.microsoft.com/en-au/topic/kb4577586-update-for-the-removal-of-adobe-flash-player-october-27-2020-931521b9-075a-ce54-b9af-ff3d5da047d5), if installed automatically by Microsoft Windows, is available from Microsoft.
- Information on [removing Adobe Flash Player](https://www.adobe.com/au/products/flashplayer/end-of-life.html), if installed manually, is available from Adobe.

### **What constitutes the previous release of an operating system?**

- This depends on the servicing branch being used for the operating system (i.e. Semi-Annual Channel or Long-Term Servicing Channel).
- Information on [Microsoft Windows 10](https://learn.microsoft.com/en-au/windows/release-health/release-information), [Microsoft Windows 11](https://learn.microsoft.com/en-au/windows/release-health/windows11-release-information) and [Microsoft Windows Server](https://learn.microsoft.com/en-au/windows/release-health/windows-server-release-info) operating system releases is available from Microsoft.

## **FAQ: Implementation questions – Multi-factor authentication**

### **Following multi-factor authentication to a system or online service, can I use a single factor for re-authentication?**

- No. Multi-factor authentication is required for both authentication and re-authentication activities.

### **Can I use biometrics as a primary authentication factor?**

- No. Biometrics can only be used as a secondary authenticator factor to unlock something you have.

### **Can I use Trusted Signals as a primary authentication factor?**

- No. Trusted Signals cannot be used as a primary authentication factor. However, organisations may use Trusted Signals in addition to two other suitable authentication factors for added security.
- Information on [Trusted Signals](https://learn.microsoft.com/en-au/windows/security/identity-protection/hello-for-business/feature-multifactor-unlock) is available from Microsoft.

### **Can I use Windows Hello for Business for multi-factor authentication?**

- Yes. Windows Hello for Business uses biometrics (something users are) or a PIN (something users know) to unlock access to cryptographic material that is tied to a device (something users have).
- Information on the use of [Windows Hello for Business](https://learn.microsoft.com/en-au/windows/security/identity-protection/hello-for-business/) is available from Microsoft.

### **Can I use Microsoft Authenticator for multi-factor authentication?**

- Yes. Microsoft Authenticator uses biometrics (something users are) or a PIN (something users know) to unlock access to cryptographic material that is tied to a device (something users have).
- Information on the use of [Microsoft Authenticator](https://learn.microsoft.com/en-au/entra/identity/authentication/concept-authentication-passwordless#microsoft-authenticator) is available from Microsoft.

### **Can I use passkeys for multi-factor authentication?**

- Yes. Passkeys use biometrics (something users are) or a PIN (something users know) to unlock access to cryptographic material that is tied to a device (something users have).
- Information on the use of [passkeys](https://learn.microsoft.com/en-au/windows/security/identity-protection/passkeys/) is available from Microsoft.

### **Can I go ‘passwordless’ for multi-factor authentication?**

- Yes. However, multi-factor authentication implementations will require biometrics (something users are) or a PIN (something users know) to unlock access to cryptographic material that is tied to a device (something users have). Depending upon the specific implementation, this is often referred to as either multi-factor cryptographic software or multi-factor cryptographic devices.
- Information on [planning a passwordless authentication deployment](https://learn.microsoft.com/en-au/entra/identity/authentication/howto-authentication-passwordless-deployment) is available from Microsoft.

### **What authentication types can be used for something users know?**

- The following authentication types can be used for something users know: memorised secrets.
- The use of knowledge-based authentication techniques (i.e. security questions) is not recognised as a valid form of memorised secret.
- Further information can be found in Section 5.1.1 of National Institute of Standards and Technology (NIST) Special Publication (SP) 800-63B, [*Digital Identity Guidelines: Authentication and Lifecycle Management*](https://csrc.nist.gov/pubs/sp/800/63/b/upd2/final).

### **What authentication types can be used for something users have?**

- The following authentication types can be used for something users have: look-up secrets, out-of-band devices, single-factor OTP devices, single-factor cryptographic software and single-factor cryptographic devices.
- Further information can be found in Section 5.1.2, Section 5.1.3, Section 5.1.4, Section 5.1.6 and Section 5.1.7 respectively of NIST SP 800-63B, [*Digital Identity Guidelines: Authentication and Lifecycle Management*](https://csrc.nist.gov/pubs/sp/800/63/b/upd2/final).

### **What authentication types can be used for something users have that is unlocked by something users know or are?**

- The following authentication types can be used for something users have that is unlocked by something users know or are: multi-factor OTP devices, multi-factor cryptographic software and multi-factor cryptographic devices.
- Further information can be found in Section 5.1.5, Section 5.1.8 and Section 5.1.9 respectively of NIST SP 800-63B, [*Digital Identity Guidelines: Authentication and Lifecycle Management*](https://csrc.nist.gov/pubs/sp/800/63/b/upd2/final).

### **Where can I find information on certified multi-factor authentication solutions?**

- The FIDO Alliance [certifies multi-factor authentication solutions](https://fidoalliance.org/certification/) against its UAF, U2F and FIDO2 standards.
- Organisations are encouraged to use multi-factor authentication solutions that have been [certified against the FIDO2 standard](https://fidoalliance.org/certification/fido-certified-products/) (preferably Level 2 over Level 1).

### **Some of my customers cannot use multi-factor authentication due to personal circumstances, what compensating controls can I implemented for such customers?**

- For customers that are unable to use multi-factor authentication due to personal circumstances, such as being in a vulnerable cohort, organisations should consider compensating controls that achieve the same security objective (i.e. not relying on a single authentication factor when authenticating customers to online customer services that contain sensitive personal data).
- Possible compensating controls, subject to acceptance of risk by an appropriate authority, could include the use of security questions (in addition to a passphrase) along with enhanced monitoring for potential signs of compromise of such user accounts.

## **FAQ: Implementation questions – Restrict administrative privileges**

### **What are unprivileged operating environments?**

- Unprivileged operating environments are those used for activities that do not require privileged access, such as reading emails and browsing the web.

### **What are privileged operating environments?**

- Privileged operating environments are those used for activities that require a degree of privileged access, such as system administration activities.

### **What are privileged user accounts?**

- A user account that has the capability to modify system configurations, account privileges, event logs or security configurations for applications. This also applies to user accounts that may only have limited privileges but still have the ability to bypass some of a system’s controls. A privileged user account may belong to a person or a service.

### **What are unprivileged user accounts?**

- A user account that does not have the capability to modify system configurations, account privileges, event logs or security configurations for applications. An unprivileged user account may belong to a person or a service.

### **How do Secure Admin Workstations differ from Privileged Access Workstations?**

- Secure Admin Workstations (SAWs) and Privileged Access Workstations (PAWs) are different names for the same concept.

### **Where can I find information on Secure Admin Workstations?**

- Microsoft provides a number of resources on [securing privileged access](https://learn.microsoft.com/en-au/security/privileged-access-workstations/overview), including the use of SAWs.

### **Do I need dedicated physical workstations for Secure Admin Workstations?**

- No. Dedicated physical workstations are not strictly required when implementing SAWs.
- Implementing SAWs generally represents a security philosophy of minimising the attack surface of privileged operating environments used by privileged users as much as possible rather than necessarily implementing a specific set of IT equipment requirements.

### **Where can I find information on privileged access management?**

- Microsoft provides an [overview of privileged access management (PAM)](https://www.microsoft.com/en-au/security/business/security-101/what-is-privileged-access-management-pam), including the concepts of just enough administration (JEA) and just-in-time (JIT) access.

### **What constitutes long credentials for break glass accounts, local administrator accounts and service accounts?**

- Long credentials are a minimum of 30 characters.

### **Where can I find information on memory integrity functionality?**

- Information on [memory integrity functionality](https://support.microsoft.com/en-au/windows/core-isolation-e30ed737-17d8-42f3-a2a9-87521df09b78) is available from Microsoft.
- Microsoft Windows’ memory integrity functionality may also be referred to as Hypervisor-protected Code Integrity (HVCI).

### **Where can I find information on Local System Authority protection functionality?**

- Information on [Local System Authority (LSA) protection functionality](https://learn.microsoft.com/en-au/windows-server/security/credentials-protection-and-management/configuring-additional-lsa-protection) is available from Microsoft.
- Microsoft Windows’ LSA protection functionality may also be referred to as Process Protection Light for LSASS.

### **Where can I find information on Credential Guard and Remote Credential Guard?**

- Information on [Credential Guard functionality](https://learn.microsoft.com/en-au/windows/security/identity-protection/credential-guard/) and [Remote Credential Guard functionality](https://learn.microsoft.com/en-au/windows/security/identity-protection/remote-credential-guard/) is available from Microsoft.

## **FAQ: Implementation questions – Application control**

### **What file types do I need to control with my application control solution?**

- The following in a non-exhaustive list of common file types that can be controlled by application control solutions:
    - executables: .exe and .com files
    - software libraries: .dll and .ocx files
    - scripts: .ps1, .bat, .cmd, .vbs and .js files
    - installers: .msi, .msp and .mst files
    - compiled HTML: .chm files
    - HTML applications: .hta files
    - control panel applets: .cpl files.

### **Where can I find Microsoft’s recommended application blocklist?**

- Information on Microsoft’s [recommended application blocklist](https://learn.microsoft.com/en-au/windows/security/application-security/application-control/windows-defender-application-control/design/applications-that-can-bypass-wdac) is available from Microsoft.

### **Where can I find Microsoft’s vulnerable driver blocklist?**

- Information on Microsoft’s [vulnerable driver blocklist](https://learn.microsoft.com/en-au/windows/security/application-security/application-control/windows-defender-application-control/design/microsoft-recommended-driver-block-rules) is available from Microsoft.

### **Can Microsoft’s vulnerable driver blocklist be implemented using core isolation’s memory integrity functionality?**

- Yes. Enabling core isolation’s memory integrity functionality will automatically enforce Microsoft’s vulnerable driver blocklist. This approach is preferred by Microsoft over the use of Windows Defender Application Control (WDAC) to block vulnerable or malicious drivers.
- Microsoft reviews their vulnerable driver blocklist every 6-12 months and updates it automatically for organisations that have implemented core isolation’s memory integrity functionality. In contrast, organisations using WDAC will need to manually update their application control rulesets when Microsoft releases an updated vulnerable driver blocklist.
- From Windows 11 version 22H2 onwards, the vulnerable driver blocklist is enabled by default.

## **FAQ: Implementation questions – Restrict Microsoft Office macros**

### **Can I use Application Guard for Office to execute macros in a sandboxed environment?**

- Unfortunately, no. Application Guard for Office disables the execution of macros in Microsoft Office documents.

### **Can I use Application Guard for Office to block the execution of macros?**

- Unfortunately, Application Guard for Office is limited in its ability to provide a comprehensive solution to blocking the execution of macros within organisations. Specifically, Microsoft Office documents will only be opened in Application Guard for Office when identified as originating from an untrusted source, such as the internet.
- As Application Guard for Office cannot be configured to always activate when opening Microsoft Office documents, this will not prevent the execution of macros that were developed internally to organisations (e.g. by malicious insiders) or from Microsoft Office documents that have had the Mark of the Web removed from them (e.g. due to users being convinced by malicious actors to do so as part of social engineering efforts).

## **FAQ: Implementation questions – User application hardening**

### **Does this mitigation strategy apply to servers?**

- Yes. Although some user applications, such as Microsoft Office and PDF software, may not be present on servers.

### **Does preventing web browsers from processing Java from the internet include JavaScript?**

- No. The requirement to prevent web browsers from processing Java from the internet does not include JavaScript.

### **Where can I find information on using attack surface reduction rules?**

- Information on [using attack surface reduction rules](https://learn.microsoft.com/en-au/microsoft-365/security/defender-endpoint/attack-surface-reduction?view=o365-worldwide) is available from Microsoft.
- Information on using attack surface reduction rules is also available in the [*Hardening Microsoft 365, Office 2021, Office 2019 and Office 2016*](https://www.cyber.gov.au/business-government/protecting-devices-systems/hardening-systems-applications/system-hardening/hardening-microsoft-365-office-2021-office-2019-and-office-2016) publication.

### **Where can I find information on preventing the activation of OLE packages?**

- Information on preventing the activation of OLE packages is available in the [*Hardening Microsoft 365, Office 2021, Office 2019 and Office 2016*](https://www.cyber.gov.au/business-government/protecting-devices-systems/hardening-systems-applications/system-hardening/hardening-microsoft-365-office-2021-office-2019-and-office-2016) publication.

### **Where can I find ASD hardening guidance?**

- Further [system hardening guidance](https://www.cyber.gov.au/business-government/protecting-devices-systems/hardening-systems-applications/system-hardening) is available from ASD.

### **When ASD and vendor hardening guidance differ, which do I follow?**

- In situations where ASD and vendor hardening guidance differs, each difference should be assessed on a case-by-case basis; however, preference should be given to implementing the most restrictive requirements.

## **FAQ: Implementation questions – Regular backups**

### **Can I delete backup contents to satisfy privacy or legal requirements?**

- Yes. Depending on the maturity level, this may be done with either a privileged user account, a backup administrator account or a break glass account.
- For Maturity Level Three, break glass accounts should only be used for this purpose.

## **Contact details**

If you have any questions regarding this guidance you can [write to us](https://www.cyber.gov.au/about-us/about-asd-acsc/contact-us) or call us on 1300 CYBER1 (1300 292 371).