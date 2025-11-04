# 19. ISM - Guidelines for database systems (September 2025)

**First published:**

04 Sep 2025

**Last updated:**

04 Sep 2025

### **Content written for**

Large organisations & infrastructure

Government

### **Attachments**

- [**Guidelines for database systems (September 2025)*845KB .pdf***](https://www.cyber.gov.au/sites/default/files/2025-09/19.%20ISM%20-%20Guidelines%20for%20database%20systems%20%28September%202025%29.pdf)

## **Database servers**

### **Functional separation between database servers and web servers**

Due to the higher threat environment that web servers are typically exposed to, hosting database servers and web servers within the same operating environment increases the likelihood of database servers being compromised by malicious actors. This security risk can be mitigated by ensuring that database servers are functionally separated from web servers.

***Control: ISM-1269; Revision: 3; Updated: Mar-22; Applicable: NC, OS, P, S, TS; Essential 8: N/A***

*Database servers and web servers are functionally separated.*

### **Communications between database servers and web servers**

Data communicated between database servers and web servers, especially over the internet, is susceptible to capture by malicious actors. As such, it is important that all data communicated between database servers and web servers is encrypted.

***Control: ISM-1277; Revision: 4; Updated: Mar-22; Applicable: NC, OS, P, S, TS; Essential 8: N/A***

*Data communicated between database servers and web servers is encrypted.*

### **Network environment**

Placing database servers on the same network segment as user workstations can increase the likelihood of database servers being compromised by malicious actors. Additionally, in cases where databases will only be accessed from their own database server, allowing remote access to the database server poses an unnecessary security risk.

***Control: ISM-1270; Revision: 3; Updated: Mar-22; Applicable: NC, OS, P, S, TS; Essential 8: N/A***

*Database servers are placed on a different network segment to user workstations.*

***Control: ISM-1271; Revision: 3; Updated: Mar-25; Applicable: NC, OS, P, S, TS; Essential 8: N/A***

*Network access controls are implemented to restrict database server communications to strictly defined network resources that require access to the database server.*

***Control: ISM-1272; Revision: 2; Updated: Jun-25; Applicable: NC, OS, P, S, TS; Essential 8: N/A***

*If only local access to a database is required, networking functionality of database management system applications are disabled or directed to listen solely to the localhost interface.*

### **Segregation of development, testing, staging and production database servers**

Using database servers across different environments, such as development, testing, staging and production environments, could result in accidental damage to their integrity or exposure of their hosted database contents.

***Control: ISM-1273; Revision: 4; Updated: Mar-25; Applicable: NC, OS, P, S, TS; Essential 8: N/A***

*Database servers for development, testing, staging and production environments are segregated.*

### **Further information**

Further information on the functional separation of computing environments can be found in the virtualisation hardening section of the [*Guidelines for system hardening*](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/ism/cybersecurity-guidelines/guidelines-for-system-hardening).

Further information on encrypting communications can be found in the cryptographic fundamentals section of the [*Guidelines for cryptography*](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/ism/cybersecurity-guidelines/guidelines-for-cryptography).

Further information on network segmentation and segregation can be found in the network design and configuration section of the [*Guidelines for networking*](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/ism/cybersecurity-guidelines/guidelines-for-networking).

Further information on database management system applications can be found in the server application hardening section of the [*Guidelines for system hardening*](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/ism/cybersecurity-guidelines/guidelines-for-system-hardening).

## **Databases**

### **Database register**

Without knowledge of all the databases in an organisation, and their contents, an organisation will be unable to appropriately protect their assets. As such, it is important that a database register is developed, implemented, maintained and verified on a regular basis.

***Control: ISM-1243; Revision: 6; Updated: Dec-22; Applicable: NC, OS, P, S, TS; Essential 8: N/A***

*A database register is developed, implemented, maintained and verified on a regular basis.*

### **Protecting databases**

Databases can be protected from unauthorised copying, and subsequent offline analysis, by applying file-based access controls to database files.

***Control: ISM-1256; Revision: 3; Updated: Sep-18; Applicable: NC, OS, P, S, TS; Essential 8: N/A***

*File-based access controls are applied to database files.*

### **Protecting database contents**

Database administrators and database users should know the sensitivity or classification associated with databases and their contents. In cases where all of a database’s contents are the same sensitivity or classification, an organisation should classify the entire database at this level and protect it as such. Alternatively, in cases where a database’s contents are of varying sensitivities or classifications, and database users have varying levels of access to the database’s contents, an organisation should protect the database’s contents at a more granular level.

Restricting database users’ ability to access, insert, modify or remove database contents, based on their work duties, ensures that the likelihood of unauthorised access, modification or deletion of database contents is reduced. Furthermore, where concerns exist that the aggregation of separate pieces of content from within a database could lead to malicious actors determining more sensitive or classified content, the need-to-know principle can be enforced through the use of minimum privileges, database views and database roles. Alternatively, the content of concern could be separated by implementing multiple databases, each with restricted data sets.

***Control: ISM-0393; Revision: 8; Updated: Jun-21; Applicable: NC, OS, P, S, TS; Essential 8: N/A***

*Databases and their contents are classified based on the sensitivity or classification of data that they contain.*

***Control: ISM-1255; Revision: 4; Updated: Mar-22; Applicable: NC, OS, P, S, TS; Essential 8: N/A***

*Database users’ ability to access, insert, modify and remove database contents is restricted based on their work duties.*

***Control: ISM-1268; Revision: 2; Updated: Jun-25; Applicable: NC, OS, P, S, TS; Essential 8: N/A***

*The need-to-know principle is enforced for database contents through the application of minimum privileges, database views, database roles and data tokenisation.*

### **Segregation of development, testing, staging and production databases**

Using database contents from production environments in non-production environments, such as development, testing or staging environments, could result in inadequate protection being applied to the database contents.

***Control: ISM-1274; Revision: 7; Updated: Mar-25; Applicable: NC, OS, P, S, TS; Essential 8: N/A***

*Database contents from production environments are not used in non-production environments unless the non-production environment is secured to at least the same level as the production environment.*

### **Database event logging**

Centrally logging and analysing security-relevant events, including configuration changes, for databases can assist in monitoring the security posture of databases, detecting malicious behaviour and contributing to investigations following cybersecurity incidents.

***Control: ISM-1537; Revision: 5; Updated: Sep-24; Applicable: NC, OS, P, S, TS; Essential 8: N/A***

*Security-relevant events for databases are centrally logged, including:*

- *access or modification of particularly important content*
- *addition of new users, especially privileged users*
- *changes to user roles or privileges*
- *attempts to elevate user privileges*
- *queries containing comments*
- *queries containing multiple embedded queries*
- *database and query alerts or failures*
- *database structure changes*
- *database administrator actions*
- *use of executable commands*
- *database logons and logoffs.*

### **Further information**

Further information on event logging can be found in the event logging and monitoring section of the [*Guidelines for system monitoring*](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/ism/cybersecurity-guidelines/guidelines-for-system-monitoring).