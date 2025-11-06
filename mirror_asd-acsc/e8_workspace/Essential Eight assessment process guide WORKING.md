# Essential Eight assessment process guide

**First published:**

24 Nov 2022

**Last updated:**

02 Oct 2024

### **Content written for**

Small & medium business

Large organisations & infrastructure

Government

### **Attachments**

- [**Essential Eight assessment process guide (October 2024)*1.3MB .pdf***](https://www.cyber.gov.au/sites/default/files/2025-03/Essential%20Eight%20assessment%20process%20guide%20%28October%202024%29.pdf)
- [**Example Essential Eight assessment test plan: Maturity Level One (August 2024)*815KB .docx***](https://www.cyber.gov.au/sites/default/files/2025-03/Example%20Essential%20Eight%20assessment%20test%20plan%20%E2%80%93%20Maturity%20Level%20One%20%28August%202024%29.docx)
- [**Example Essential Eight assessment test plan: Maturity Level Two (November 2023)*821KB .docx***](https://www.cyber.gov.au/sites/default/files/2025-03/Example%20Essential%20Eight%20assessment%20test%20plan%20%E2%80%93%20Maturity%20Level%20Two%20%28November%202023%29.docx)
- [**Example Essential Eight assessment test plan: Maturity Level Three (November 2023)*815KB .docx***](https://www.cyber.gov.au/sites/default/files/2025-03/Example%20Essential%20Eight%20assessment%20test%20plan%20%E2%80%93%20Maturity%20Level%20Three%20%28November%202023%29.docx)
- [**Essential Eight assessment report template (November 2023)*2.91MB .docx***](https://www.cyber.gov.au/sites/default/files/2025-03/Essential%20Eight%20assessment%20report%20template%20%28November%202023%29.docx)

## **Introduction**

The Australian Signals Directorate (ASD) has developed prioritised mitigation strategies, in the form of the [*Strategies to mitigate cybersecurity incidents*](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/mitigating-cyber-security-incidents), to help organisations protect themselves against various cyberthreats. The most effective of these mitigation strategies are the Essential Eight.

This publication details a process for undertaking assessments of the Essential Eight. In doing so, it includes guidance on assessment methods that can be used for assessing both the implementation and effectiveness of controls that underpin the Essential Eight – as articulated within the [*Essential Eight maturity model*](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/essential-eight) (November 2023 release).

This publication should be read and used in conjunction with other ASD guidance and tools. This includes the:

- [*Essential Eight maturity model*](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/essential-eight)
- [*Essential Eight maturity model FAQ*](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/essential-eight/essential-eight-maturity-model-faq)
- [*Essential Eight assessment report template*](https://www.cyber.gov.au/sites/default/files/2023-03/Essential%20Eight%20Assessment%20Report%20Template.docx)
- [Essential Eight assessment toolkit](https://partners.cyber.gov.au/).

Note, all vendor products mentioned within this publication are for illustrative purposes only and should not be interpreted as an explicit endorsement by ASD.

## **Overview**

Assessments against the Essential Eight are conducted using the [*Essential Eight maturity model*](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/essential-eight). This maturity model describes three target maturity levels (Maturity Level One through to Maturity Level Three) which are based on mitigating increasing levels of tradecraft (i.e. tools, tactics, techniques and procedures) and targeting. The maturity model also includes Maturity Level Zero which exists for capturing instances in which the requirements of Maturity Level One are not met.

Although the approach to conducting an assessment depends on the size and complexity of a system, there are foundational principles that are common to each assessment. As such, the guidance in this publication should be incorporated by assessors, noting that assessors should still use their own judgement and expertise.

Finally, in determining compensating control effectiveness, assessors should ensure that any compensating controls that have been implemented provide an equivalent level of protection to those recommended under the Essential Eight. This will assist in ensuring that an equivalent level of overall protection against a specific level of tradecraft and targeting can be achieved and maintained.

## **Evidence quality**

In conducting an assessment, assessors need to gather and review credible evidence to support conclusions they draw on the effectiveness of controls. In general terms, the evidence used to determine the effectiveness of controls will vary in quality depending on the approach taken. As such, when conducting an assessment, assessors should seek to gather and use the highest quality evidence where reasonably practicable. This guide defines four levels of evidence quality:

- **Excellent evidence:** Testing a control with a simulated activity designed to confirm it is in place and effective (e.g. attempting to run a test application to check application control rulesets).
- **Good evidence:** Reviewing the configuration of a system through the system’s interface to determine whether it should enforce an expected policy.
- **Fair evidence:** Reviewing a copy of a system’s configuration (e.g. using reports or screenshots) to determine whether it should enforce an expected policy.
- **Poor evidence:** A policy or verbal statement of intent (e.g. sighting mention of controls within documentation or controls being discussing during interviews with personnel administering or managing system security).

### **Determining effective implementation of mitigation strategies**

Upon concluding assessment activities, assessors will need to determine whether mitigation strategies were implemented effectively or not. This determination requires a combination of judgement and consideration of the following factors:

- adoption of a risk-based approach to the implementation of mitigation strategies
- ability to test the mitigation strategies across an accurate representative sample of workstations (including laptops), servers and network devices
- level of assurance gained from assessment activities and any evidence provided (noting the quality of evidence)
- any exceptions, including associated compensating controls, and whether they have been accepted by an appropriate authority as part of a formal exception process.

Assessors should use ASD’s standardised assessment outcomes which are:

- **Not assessed:** The control has not yet been assessed.
- **Effective:** The organisation is effectively meeting the control’s objective.
- **Alternate control:** The organisation is effectively meeting the control’s objective through an alternate control.
- **Ineffective:** The organisation is not adequately meeting the control’s objective.
- **No visibility:** The assessor was unable to obtain adequate visibility of a control’s implementation.
- **Not implemented:** The organisation has decided not to implement the control.
- **Not applicable:** The control does not apply to the system or environment.

It is important that assessors do not allow risk acceptance as a justification for not implementing an entire mitigation strategy (e.g. a system owner has risk accepted not implementing application control or multi-factor authentication). In these cases, without adequate compensating controls, the mitigation strategy is considered to be not implemented.

For a system owner to claim they have implemented a mitigation strategy, all controls specified within the mitigation strategy must be assessed as ‘effective’ or ‘alternate control’. If one of the controls specified for a mitigation strategy is assessed as ‘ineffective’, the system owner cannot claim to have met the requirements for that maturity level. In turn, this applies to the determination of whether a system owner has met the target maturity level for their system (i.e. if one or more mitigation strategies are deemed to have not been implemented then the target maturity level for the system cannot be claimed to have been met).

Where exceptions to a mitigation strategy’s controls have been identified, the assessor should review and evaluate any compensating controls that are in place to determine whether they address the intent of the original controls and are implemented effectively. Two examples have been provided below.

> Example: During an internal review, an organisation identified a low-risk Microsoft Windows server that could not be patched. As a result, the organisation implemented a plan to decommission the server within two months.
> 
> 
> In this situation, it was still important for the organisation to apply compensating controls to reduce the identified risk to an acceptable level, and to align with the requirements of the Essential Eight’s exception process. As a result, a risk owner was assigned and strong compensating controls were put in place.
> 
> In this instance, as the exception was being effectively managed and strong compensating controls had been put in place, an assessor determined that the exception should not preclude the organisation from reaching their target maturity level. Conversely, if the organisation had not applied strong compensating controls, it would not have aligned with the requirements of the Essential Eight’s exception process and should have been precluded from reaching their target maturity level.
> 

> Example: During an internal review, an organisation identified a cloud service that did not have multi-factor authentication functionality enabled. In assessing the situation, the organisation decided it was not worth the time and effort to enable such functionality, not to mention the complaints they expected they would receive from users. As such, the organisation chose to simply accept the risk of not implementing a control rather than implementing strong compensating controls.
> 
> 
> In this instance, as the exception was not being effectively managed, nor were strong compensating controls in place, an assessor determined that the organisation should be precluded from reaching their target maturity level.
> 

It is important that the use of exceptions for a system are documented and approved by an appropriate authority through a formal process. Documentation for exceptions should include the following:

- detail, scope and justification for exceptions
- detail of compensating controls associated with exceptions, including:
    - detail, scope and justification for compensating controls
    - expected lifetime of compensating controls
    - when compensating controls will next be reviewed
- system risk rating before and after the implementation of compensating controls
- any caveats placed on the use of the system as a result of exceptions
- acceptance by an appropriate authority of the residual risk for the system
- when the necessity of exceptions will next be considered by an appropriate authority (noting exceptions should not be approved beyond one year).

The appropriate use of a formal exception process, along with compensating controls, should not preclude an organisation from being assessed as meeting the requirements for their target maturity level.

## **Stages of an assessment**

At a high-level, assessments are comprised of four stages:

- **Stage 1:** The assessor plans and prepares for the assessment.
- **Stage 2:** The assessor determines the scope (i.e. assessment boundary) and approach for the assessment.
- **Stage 3:** The assessor assesses the controls associated with each of the mitigation strategies.
- **Stage 4:** The assessor develops the security assessment report.

The activities and considerations for each stage of an assessment are discussed in further detail below.

## **Stage 1: Assessment planning and preparation**

### **Assessment planning**

Prior to commencing an assessment, the assessor should conduct assessment planning activities. These activities require the assessor to discuss with the system owner:

- assessment scope (i.e. assessment boundary) and assessment approach (see further detail below)
- access to unprivileged and privileged user accounts, devices, documentation, personnel, and facilities
- any approvals required to run scripts and tools on the system (see further detail below)
- evidence collection and protection, including any requirements following the conclusion of the assessment
- where the security assessment report will be developed (e.g. on an assessor’s device or on an alternative device)
- approach to stakeholder engagement and consultation (including key points of contact)
- whether any service providers manage aspects of the system (including appropriate points of contact)
- access to any relevant prior security assessment reports for the system
- appropriate use, retention and marketing of the security assessment report by both parties.

Assessors may also develop an assessment test plan and share it with the system owner.

## **Stage 2: Determination of assessment scope and approach**

### **Determine assessment scope**

In determining the assessment scope (i.e. assessment boundary), assessors should first clarify the target maturity level with the system owner, noting that the Essential Eight is required to be implemented and assessed as a package. For example, if a system owner has not previously had an assessment demonstrating that they have implemented Maturity Level One, they should not begin an assessment against Maturity Level Two until they have done so, and likewise for Maturity Level Two before being assessed against Maturity Level Three.

Having identified a suitable target maturity level, the assessor should familiarise themselves with the requirements for that maturity level as it will impact the components or aspects of the system within scope of the assessment.

Once the scope of the assessment has been identified, and agreed upon with the system owner, a more accurate determination of the assessment’s duration and any milestones will likely be possible.

The scope of the assessment should be documented within the security assessment report. Any components or aspects of a system deemed out of scope should also be documented and accompanied by a justification for their exclusion.

### **Determine assessment approach**

In determining a suitable assessment approach, both qualitative and quantitative testing techniques should be considered. For example, qualitative testing techniques include documentation reviews and interviews with personnel administering or managing system security, while quantitative testing techniques include system configuration reviews and the use of scripts and tools. Sample sizes for testing should also be determined in consultation with the system owner, with the aim of assessing a reasonable representative sample of workstations (including laptops), servers and network devices.

Conducting assessments using interviews, reports and screenshots will always be inferior to conducting assessments using scripts and tools. Particularly as scripts and tools often assess many workstations and servers on a network, rather than a single sample workstation or server, and often identify issues that may be missed in interviews or overlooked by human analysis of reports and configuration settings. If adequate assessment scripts and tools are not already present on a system, assessors may seek to use their own scripts and tools following approval by the system owner.

Any assessment limitations, including sample sizes and constraints on technical testing, should be documented within the security assessment report.

## **Stage 3: Assessment of controls**

The assessment of each mitigation strategy is performed by reviewing and testing the effectiveness of controls. This section provides guidance on the approach to assessing each mitigation strategy at a given maturity level, along with relevant assessment considerations. Guidance on determining the effectiveness of controls within each mitigation strategy is also provided within this section.

Assessment guidance for maturity levels in this section is cumulative. For example, the guidance provided in the Maturity Level Two section is focused on unique requirements above those of Maturity Level One. Likewise, the guidance provided in the Maturity Level Three section is focused on unique requirements above those of Maturity Level Two. This aligns with the manner in which assessments should be conducted against target maturity levels.

### **Maturity Level One**

### **Maturity Level Two**

### **Maturity Level Three**

## **Stage 4: Development of the security assessment report**

In developing the security assessment report, assessors should use the [*Essential Eight assessment report template*](https://www.cyber.gov.au/sites/default/files/2023-03/Essential%20Eight%20Assessment%20Report%20Template.docx). However, assessors can use their own report templates for branding purposes if all sections from the template are included.

## **Further information**

The [*Information security manual*](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/ism) is a cybersecurity framework that organisations can apply to protect their systems and data from cyberthreats. The advice in the [*Strategies to mitigate cybersecurity incidents*](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/mitigating-cyber-security-incidents), along with its [Essential Eight](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/essential-eight), complements this framework.

A mapping between the requirements of the [*Essential Eight maturity model*](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/essential-eight) and the [*Information security manual*](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/ism) can be found in the [*Essential Eight maturity model and ISM mapping*](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/essential-eight/essential-eight-maturity-model-and-ism-mapping) publication.

## **Contact details**

If you have any questions regarding this guidance you can [write to us](https://www.cyber.gov.au/about-us/about-asd-acsc/contact-us) or call us on 1300 CYBER1 (1300 292 371).