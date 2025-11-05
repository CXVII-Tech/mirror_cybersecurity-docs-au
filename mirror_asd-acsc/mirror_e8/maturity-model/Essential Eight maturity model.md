# Essential Eight maturity model

**First published:**

30 Jun 2017

**Last updated:**

27 Nov 2023

### **Content written for**

Small & medium business

Large organisations & infrastructure

Government

### **Attachments**

- [**Essential Eight maturity model (November 2023)*1.17MB .pdf***](https://www.cyber.gov.au/sites/default/files/2025-03/Essential%20Eight%20maturity%20model%20%28November%202023%29.pdf)

## **Introduction**

The Australian Signals Directorate (ASD) has developed prioritised mitigation strategies, in the form of the [*Strategies to mitigate cybersecurity incidents*](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/mitigating-cyber-security-incidents), to help organisations protect themselves against various cyberthreats. The most effective of these mitigation strategies are the Essential Eight.

The Essential Eight has been designed to protect organisations’ internet-connected information technology networks. While the principles behind the Essential Eight may be applied to enterprise mobility and operational technology networks, it was not designed for such purposes and alternative mitigation strategies may be more appropriate to defend against unique cyberthreats to these environments.

The [*Essential Eight maturity model*](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/essential-eight), first published in June 2017 and updated regularly, supports the implementation of the Essential Eight. It is based on ASD’s experience in producing cyberthreat intelligence, responding to cybersecurity incidents, conducting penetration testing and assisting organisations to implement the Essential Eight.

## **Implementation**

When implementing the Essential Eight, organisations should identify and plan for a target maturity level suitable for their environment. Organisations should then progressively implement each maturity level until that target is achieved.

As the mitigation strategies that constitute the Essential Eight have been designed to complement each other, and to provide coverage of various cyberthreats, organisations should plan their implementation to achieve the same maturity level across all eight mitigation strategies before moving onto higher maturity levels.

Organisations should implement the Essential Eight using a risk-based approach. In doing so, organisations should seek to minimise any exceptions and their scope, for example, by implementing compensating controls and ensuring the number of systems or users impacted are minimised. In addition, any exceptions should be documented and approved through an appropriate process. Subsequently, the need for any exceptions, and associated compensating controls, should be monitored and reviewed on a regular basis. Note, the appropriate use of exceptions should not preclude an organisation from being assessed as meeting the requirements for a given maturity level.

As the Essential Eight outlines a minimum set of preventative measures, organisations need to implement additional measures to those within this maturity model where it is warranted by their environment. Further, while the Essential Eight can help to mitigate the majority of cyberthreats, it will not mitigate all cyberthreats. As such, additional mitigation strategies and controls need to be considered, including those from the [*Strategies to mitigate cybersecurity incidents*](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/mitigating-cyber-security-incidents) and the [*Information security manual*](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/ism).

Finally, there is no requirement for organisations to have their Essential Eight implementation certified by an independent party. However, Essential Eight implementations may need to be assessed by an independent party if required by a government directive or policy, by a regulatory authority, or as part of contractual arrangements.

## **Maturity levels**

To assist organisations with their implementation of the Essential Eight, four maturity levels have been defined (Maturity Level Zero through to Maturity Level Three). With the exception of Maturity Level Zero, the maturity levels are based on mitigating increasing levels of tradecraft (i.e. tools, tactics, techniques and procedures) and targeting, which are discussed in more detail below. Depending on overall capability, malicious actors may exhibit different levels of tradecraft for different operations against different targets. For example, malicious actors capable of advanced tradecraft may use it against one target while using basic tradecraft against another. As such, organisations should consider what level of tradecraft and targeting, rather than which malicious actors, they are aiming to mitigate.

Organisations need to consider that the likelihood of being targeted is influenced by their desirability to malicious actors, and the consequences of a cybersecurity incident will depend on their requirement for the confidentiality of their data, as well as their requirement for the availability and integrity of their systems and data. This, in combination with the descriptions for each maturity level, can be used to help determine a target maturity level to implement.

Finally, Maturity Level Three will not stop malicious actors that are willing and able to invest enough time, money and effort to compromise a target. As such, organisations still need to consider the remainder of the mitigation strategies from the [*Strategies to mitigate cybersecurity incidents*](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/mitigating-cyber-security-incidents) and the [*Information security manual*](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/ism).

### **Maturity Level Zero**

This maturity level signifies that there are weaknesses in an organisation’s overall cybersecurity posture. When exploited, these weaknesses could facilitate the compromise of the confidentiality of their data, or the integrity or availability of their systems and data, as described by the tradecraft and targeting in Maturity Level One below.

### **Maturity Level One**

The focus of this maturity level is malicious actors who are content to simply leverage commodity tradecraft that is widely available in order to gain access to, and likely control of, a system. For example, malicious actors opportunistically using a publicly-available exploit for a vulnerability in an online service which had not been patched, or authenticating to an online service using credentials that were stolen, reused, brute forced or guessed.

Generally, malicious actors are looking for any victim rather than a specific victim and will opportunistically seek common weaknesses in many targets rather than investing heavily in gaining access to a specific target. Malicious actors will employ common social engineering techniques to trick users into weakening the security of a system and launch malicious applications. If user accounts that malicious actors compromise have special privileges they will exploit it. Depending on their intent, malicious actors may also destroy data (including backups).

### **Maturity Level Two**

The focus of this maturity level is malicious actors operating with a modest step-up in capability from the previous maturity level. These malicious actors are willing to invest more time in a target and, perhaps more importantly, in the effectiveness of their tools. For example, these malicious actors will likely employ well-known tradecraft in order to better attempt to bypass controls implemented by a target and evade detection. This includes actively targeting credentials using phishing and employing technical and social engineering techniques to circumvent weak multi-factor authentication.

Generally, malicious actors are likely to be more selective in their targeting but still somewhat conservative in the time, money and effort they may invest in a target. Malicious actors will likely invest time to ensure their phishing is effective and employ common social engineering techniques to trick users to weaken the security of a system and launch malicious applications. If user accounts that malicious actors compromise have special privileges they will exploit it, otherwise they will seek user accounts with special privileges. Depending on their intent, malicious actors may also destroy all data (including backups) accessible to a user account with special privileges.

### **Maturity Level Three**

The focus of this maturity level is malicious actors who are more adaptive and much less reliant on public tools and techniques. These malicious actors are able to exploit the opportunities provided by weaknesses in their target’s cybersecurity posture, such as the existence of older software or inadequate logging and monitoring. Malicious actors do this to not only extend their access once initial access has been gained to a target, but to evade detection and solidify their presence. Malicious actors make swift use of exploits when they become publicly available as well as other tradecraft that can improve their chance of success.

Generally, malicious actors may be more focused on particular targets and, more importantly, are willing and able to invest some effort into circumventing the idiosyncrasies and particular policy and technical controls implemented by their targets. For example, this includes social engineering a user to not only open a malicious document but also to unknowingly assist in bypassing controls. This can also include circumventing stronger multi-factor authentication by stealing authentication token values to impersonate a user. Once a foothold is gained on a system, malicious actors will seek to gain privileged credentials or password hashes, pivot to other parts of a network, and cover their tracks. Depending on their intent, malicious actors may also destroy all data (including backups).

### **Requirements for each maturity level**

Requirements for Maturity Level One through to Maturity Level Three are outlined in Appendices A to C. A comparison of the maturity levels, with changes between maturity levels indicated via bolded text, is outlined in Appendix D.

## **Further information**

The [*Essential Eight maturity model*](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/essential-eight) is part of a suite of related publications:

- Answers to questions on this maturity model are available in the [*Essential Eight maturity model FAQ*](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/essential-eight/essential-eight-maturity-model-faq) publication.
- Additional mitigation strategies are available in the [*Strategies to mitigate cybersecurity incidents*](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/mitigating-cyber-security-incidents) publication.
- Further Information on patching activities is available in the [*Patching applications and operating systems*](https://www.cyber.gov.au/business-government/protecting-devices-systems/system-administration/patching-applications-and-operating-systems) publication.
- Further Information on implementing multi-factor authentication is available in the [*Implementing multi-factor authentication*](https://www.cyber.gov.au/business-government/protecting-devices-systems/hardening-systems-applications/system-hardening/implementing-multi-factor-authentication) publication.
- Further Information on controlling privileged user accounts is available in the [*Restricting administrator privileges*](https://www.cyber.gov.au/business-government/protecting-devices-systems/system-administration/restricting-administrative-privileges) publication.
- Further Information on implementing application control is available in the [*Implementing application control*](https://www.cyber.gov.au/business-government/protecting-devices-systems/hardening-systems-applications/system-hardening/implementing-application-control) publication.
- Further Information on controlling Microsoft Office macros is available in the [*Restricting Microsoft Office macros*](https://www.cyber.gov.au/business-government/protecting-devices-systems/hardening-systems-applications/system-hardening/restricting-microsoft-office-macros) publication.

## **Contact details**

If you have any questions regarding this guidance you can [write to us](https://www.cyber.gov.au/about-us/about-asd-acsc/contact-us) or call us on 1300 CYBER1 (1300 292 371).

## **Appendix**

- [Appendix A: Maturity Level One](e8-mm-appendix-a.md)
- [Appendix B: Maturity Level Two](e8-mm-appendix-b.md)
- [Appendix C: Maturity Level Three](e8-mm-appendix-c.md)
- [Appendix D: Comparison of maturity levels](e8-mm-appendix-d.md)