# Cloud controls matrix template (September 2025)

## Overview

The Cloud controls matrix template is intended for use by security assessors to capture the implementation of controls from the Information security manual (ISM) by a Cloud Service Provider (CSP). In doing so, the CCM template provides indicative guidance on the scoping of security assessments, however, it should be noted that the guidance is not definitive and should be interpreted by security assessors in the context of the services being assessed. The CCM template also captures the ability for consumers to implement controls for services built upon a CSP's services by identifying where they are responsible for configuring their own services in accordance with the ISM.

## ISM controls

This content lists the controls from the ISM as typically found in the associated System security plan annex template. The applicability markings can be used to filter out security classifications and essential eight maturity levels that are not applicable to the service being assessed. Note, the `NC` applicability marking is applicable to non-classified services offered to all consumers while the `OS`, `P`, `S` and `TS` applicability markings represent additional controls that are only applicable to classified services offered to Commonwealth entities.

## Scoping considerations

The assessment boundary establishes the scope of protection for a service and must be clearly defined. Specifically, the assessment boundary is what a CSP agrees to protect, or is within the scope of their responsibilities. This includes the facilities, people, systems, software, processes and procedures that support their business functions.

All aspects of a CSP should be considered in scope at the commencement of a security assessment. Any environments that are subsequently deemed out of scope should be documented in the security assessment report and accompanied by an adequate justification for their exclusion. In conducting a security assessment, each environment should be assessed separately ensuring that the assessment covers each administration environment and cloud production environment. For example, noting the importance of the physical devices used for privileged access to the given security model, they will always be included in the administration environment and be within scope.

### Administration Environment

This includes controls associated with a CSP’s administration environment. In assessing a CSP’s administrative environment, this would typically include all machines located in their management offices. Broadly speaking, where these machines are on a CSP’s corporate network, they must be assessed. Alternatively, where a dedicated administrative zone and workstations are used, the scope may be restricted to this environment instead.

Note, a CSP’s corporate environment should be included in scope of the security assessment until it is proven that it is sufficiently segregated and segmented from the CSP’s cloud production environment and that the CSP performs secure administrative practices.

### Cloud Production - Common Controls

This includes controls associated with the cloud production environment that are common across all services. Typically this would include all machines located in the data centre.

### Cloud Production - System Specific

This includes controls applicable to an individual service that have not been assessed as part of the common controls assessment. For example, tenancy segmentation and segregation configuration where these vary between services, or service-specific technologies such as web conferencing.

## Provider Responsibilities

### Provider Responsibility

List the responsibility of the CSP or  any outsourced service provider that have responsibilities for the implementation of the control.

Note, similar to a consumer relying on a CSP, the CSP itself may be equally reliant on any outsourced service provider they use. To this end, it is critical that the consumer is made as aware as possible of the overall security posture of a CSP by taking into consideration these dependencies.

If performing a security assessment where an outsourced service provider is used by a CSP, the security assessor needs to determine the risk of the outsourced service. In doing so, the amount of information available will vary greatly based on the particular outsourced service provider used. As such, the security assessor will need to adapt to these circumstances. If the outsourced service provider has not already undergone an IRAP assessment themselves, or has but is unwilling to share their security assessment report, this should be explicitly noted in order to provide the consumer with visibility of this situation. Alternatively, where an existing security assessment report is available, this information should be captured and presented alongside the assessed service. Note, if the outsourced service provider was assessed using an earlier version of the ISM a gap analysis will be required.

### Implementation Status

This articulates the extent of the implementation of controls within the assessment boundary.

Not Assessed

: **This control is yet to be assessed in the context of the environment.** Note, this serves as the default implementation status and should be changed to one of the below status following a security assessment. At the completion of the security assessment, no control should be marked as `Not Assessed`.

Effective

: **The CSP is effectively meeting the control's objective.** Note, where the CSP relies on an outsourced service provider to also implement this control, the control should only be marked as `Effective` if both parties effectively meet the control’s objective. For example, both the CSP and the outsourced service provider ensure that multi-factor authentication is used to authenticate users.

Alternate Control

: **The CSP is effectively meeting the control's objective though an alternate control.** In doing so, the alternate control meets or exceeds the objective of the original control.

Ineffective

: **The CSP is not adequately meeting the control's objective.** Note, this includes where an alternate control was used in an attempt to meet the original control's objective but did not meet or exceed the objective of the original control.

No Visibility

: **The security assessor was unable to obtain adequate visibility of the control's implementation.** Note, this will commonly be the case when a CSP relies on an outsourced service provider to implement the control but was unable to provide visibility of the outsourced service provider's implementation.

Not Implemented

: **The CSP has decided not to implement the control.** For example, the CSP decided not to invest in the use of dedicated administrative workstations, or foreign nationals had privileged access to a service.

Not Applicable

: **This control does not apply to the service being assessed.** Note, a control may be marked as `Not Applicable` for a number of reasons, including: the technology is not used by the service, the control is not applicable to the security classification the service is being assessed against, or the control has been assessed as a common control rather than a service-specific control.

### Implementation Comments

Any amplifying comments relating to the implementation status of a control should be provided at this point by the security assessor.

## Consumer Responsibilities

### Consumer Responsibility

This articulates the responsibility of consumers when using the assessed service.

### Consumer Implementation Required

Whether the consumer is required to perform implementation activities associated with this control to carry out their consumer responsibility. `Not Assessed` serves as the default implementation status and should be changed to one of `Yes`/`No`/`Not Possible`/`Not Applicable` where `Not Possible` covers scenarios whereby the CSP prevents the implementation of this control in which the consumer would normally be responsible. At the completion of the security assessment, no implementation should be marked as `Not Assessed`.

### Consumer Configuration Required

Whether the consumer is required to perform configuration activities associated with this control to carry out their consumer responsibility, while the CSP manages the implementation of this control. For example, while the CSP may offer multi-factor authentication, it is the consumer’s responsibility to configure this feature for their user accounts. `Not Assessed` serves as the default configuration status and should be changed to one of `Yes`/`No`/`Not Possible`/`Not Applicable` where `Not Possible` covers scenarios whereby the CSP prevents the configuration of this control in which the consumer would normally be responsible. At the completion of the security assessment, no configuration should be marked as `Not Assessed`.

### Consumer Guidance

Any amplifying comments relating to the implementation of a control by a consumer should be provided at this point by the security assessor, including the ability for consumers to implement and/or configure controls to meet the intent of the ISM. 

## Further information

Further information on conducting security assessments of cloud services can be found within the Cloud assessment and authorisation publication and the Cloud security assessment report template.