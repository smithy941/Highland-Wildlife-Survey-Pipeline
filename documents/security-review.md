## Security Review

### Authentication and Authorisation
The system does not implement authentication or authorisation. This means that any user can access the system, including the JSON report endpoint and data ingestion processes without logging in. This presents a security risk as there is no way to verify users or restrict access. If the system was live, authentication and authorisation would be required to ensure that only authorised users can access and modify data.

---

### Access Control
There are no access controls implemented in the system. All users have the same level of access including the ability to view and insert data through scripts and endpoints. The lack of role based access control allows unauthorised users to modify and insert incorrect data. In a live system, access control would be required to restrict actions based on user roles This could include limiting data modification to administrators only.

---

### Data Anonymity
The system stores volunteer names and email addresses as plain text within the database. This means that personal information is directly associated with survey data which raises privacy concerns. There is no anonymisation or pseudonymisation of user data. In a live system, personal data would have to be anonymised or replaced with unique identifiers to protect users and comply with GDPR..

---

### Data Destruction
The system does not include processes for data deletion or archival. All data remains stored in the database which could lead to excessive data accumulation and potentially compliance issues over time. There are also no processes for removing outdated or unnecessary records. In a live system, data destruction processes would be a requirement to securely delete or archive data.

---

### Lifecycle Security
The system does not implement lifecycle security practices. Data is collected, stored and used but there are no processes for secure handling throughout its lifecycle. This includes a lack of secure data storage processes, no encryption of data and no processes for data archival or deletion. In a live system, lifecycle security would include protecting data during collection, transmission, storage and deletion to reduce security risks.

---

### SQL Injection
The system uses parameterised SQL queries (e.g. %s placeholders) which helps reduce the risk of SQL injection attacks by preventing user inputs being inserted into SQL statements. This is a positive security measure. However, input validation could be implemented to further reduce risk.

---

### Insider Threats
The system does not protect against insider threats. Any user with access to the system could modify or insert data. This could lead to accidental errors or intentional misuse of the system. In a live system, monitoring, logging and restricted access would be used to reduce the risk of insider threats.

---

### Business Vulnerability
The system relies on a single database with no redundancy or backups. If the database becomes unavailable due to failure or attack, the system would not be able to function. This represents a business vulnerability as there is no recovery plan in place. In a live system, backups and failover systems would be required to ensure availability.

---

### Safety-Critical Context
The system is not considered safety critical as it does not impact human safety. However, the data produced by the system could have an influence on wildlife conservation and environmental monitoring decisions. If the data is inaccurate or compromised it could lead to the wrong decisions being made.