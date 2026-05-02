## Technical Report

### Big-O Analysis

The main algorithms used in this project are:

- CSV ingestion: O(n), as each row in the CSV file is processed once using a loop. The time taken increases linearly with the number of rows as each row must be validated and inserted into the database or rejected.  

- XML parsing: O(n), as each observation element in the XML file is processed sequentially. The script loops through each observation to extract species and count data before inserting it into the database. The time taken depends on the number of elements.  

- Database queries: O(n), depending on the number of results returned meaning performance scales with the size of the result set.  

These algorithms are efficient for the dataset size used in this project as they scale linearly and avoid unnecessary complexity.

---

### SQL vs NoSQL Comparison

SQL was chosen because:

- The data is structured (species, sites, sightings)  
- Relationships between tables are important  
- Data integrity and consistency are required  

NoSQL databases are more flexible but don't enforce relationships as strictly. For this project, SQL is more suitable due to the relational nature of the data.

---

### JSON vs XML Comparison

JSON and XML were both used in this project but for different purposes.

JSON was used for the API because:

- It is lightweight and uses less data compared to XML  
- It is faster to transmit over a network  
- It is easy to parse and use in web applications 

This makes JSON suited to returning data to the frontend in the JSON report service.

XML was used for data exchange and reporting because:

- It supports structured and hierarchical data  
- It allows clearly defined nested elements  
- It can be validated using schemas such as XSD  

XML is better suited for data exchange between systems and for generating structured reports where validation is required.

---

### Sustainability Evaluation

The system was designed with efficiency in mind. The main data processing operations use linear time algorithms (O(n)), meaning that performance scales proportionally with the size of the data. This avoids unnecessary computational overhead.

The database is normalised which reduces duplication of data and improves storage efficiency. This means that less disk space is used and fewer redundant updates are required.

JSON is used for API responses which reduces data transmission size compared to XML. This lowers network usage and improves performance whilst transferring data to the frontend.

However, there are some areas where sustainability could be improved:

- There is no data lifecycle management meaning old data is never removed  
- Repeated database queries could increase resource usage over time  
- No caching is implemented for frequently accessed data  

Overall the system is efficient for its scale but could be improved with optimisation techniques in a live environment. 

---

### Time Management Reflection

The project was developed within a limited timeframe which required a change in apprach to project management. Agile principles were followed where possible. This included breaking the system into smaller components and completing them incrementally.

Due to time constraints, full sprint cycles were followed in real time. Instead, sprints were simulated by grouping tasks into short development phases that aligned with project milestones. This allowed progress to be tracked and ensured that the projet was completed in a structured way.

This approach was effective for delivering the project within the time available. However, it reduced opportunities for extensive testing and refinement.

---

## Sustainability Statement

The system was designed to be efficient by using linear time algorithms and a normalised relational database structure to reduce redundancy. JSON was used for API responses to reduce data transmission size, whilst XML was used where structured validation was required. However, sustainability could be improved by implementing data lifecycle management, reducing repeated queries and optimising resource usage.