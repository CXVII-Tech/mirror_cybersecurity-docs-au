# System security plan annex template (September 2025)

- [ISM Principles](System%20security%20plan%20annex%20template%20(September%202025)%20-%20ISM%20Principles.md)
- [ISM Controls](System%20security%20plan%20annex%20template%20(September%202025)%20-%20ISM%20Controls.md)

## Overview

The System security plan annex template is intended for use by security assessors to capture the implementation of controls from the Information security manual (ISM) by an organisation. In doing so, the SSP annex template provides indicative guidance on the scoping of security assessments, however, it should be noted that the guidance is not definitive and should be interpreted by security assessors in the context of the system being assessed.

## ISM controls

This template lists the controls from the ISM. The applicability markings can be used to filter out security classifications and essential eight maturity levels that are not applicable to the system being assessed. Note, the `NC` applicability marking is applicable to all non-classified systems while the `OS`, `P`, `S` and `TS` applicability markings represent additional controls that are only applicable to systems used by Commonwealth entities.

## Scoping considerations

The assessment boundary establishes the scope of protection for a system and must be clearly defined. Specifically, the assessment boundary is what a system owner agrees to protect, or is within the scope of their responsibilities. This includes the facilities, people, systems, software, processes and procedures that support their business functions.

All aspects of a system should be considered in scope at the commencement of a security assessment. Any aspects that are subsequently deemed out of scope should be documented in the security assessment report and accompanied by an adequate justification for their exclusion.

## Implementation of controls

### Responsibility

Select who is responsible for the implementation of the control:

- Board of Directors / Executive Committee
- Chief Information Security Officer
- System Owner
- System Manager
- Internal Service Provider
- Outsourced Service Provider
- Shared Responsibility
- Not Applicable

### Implementation

This articulates the extent of the implementation of controls within the assessment boundary.

`Not Assessed`
: **This control is yet to be assessed in the context of the environment.** Note, this serves as the default implementation status and should be changed to one of the below status following a security assessment. At the completion of the security assessment, no control should be marked as `Not Assessed`.

`Effective`
: **The system owner is effectively meeting the control's objective.** Note, where the system owner relies on an outsourced service provider to also implement this control, the control should only be marked as `Effective` if both parties effectively meet the control’s objective. For example, both the system owner and the outsourced service provider ensure that multi-factor authentication is used to authenticate users.

`Alternate Control`
: **The system owner is effectively meeting the control's objective though an alternate control.** In doing so, the alternate control meets or exceeds the objective of the original control.

`Common Control`
: **The system owner is effectively meeting the control's objective though a common control.** Common controls will typically be organisational-wide governance controls or technical controls that have been inherited from an underlying system that another system is built upon.

`Ineffective`
: **The system owner is not adequately meeting the control's objective.** Note, this includes where an alternate control was used in an attempt to meet the original control's objective but did not meet or exceed the objective of the original control.

`No Visibility`
: **The security assessor was unable to obtain adequate visibility of the control's implementation.** Note, this will commonly be the case when a system owner relies on an outsourced service provider to implement the control but was unable to provide visibility of the outsourced service provider's implementation.

`Not Implemented`
: **The system owner has decided not to implement the control.** For example, the system owner decided not to invest in the use of dedicated administrative workstations, or foreign nationals had privileged access to a service.

`Not Applicable`
: **This control does not apply to the system being assessed.** Note, a control may be marked as `Not Applicable` for a number of reasons, including: the technology is not used by the system, the control is not applicable to the security classification the system is being assessed against, or the control has been assessed as a common control rather than a system-specific control.

### Implementation Comments

Any amplifying comments relating to the implementation status of a control should be provided at this point by the security assessor.