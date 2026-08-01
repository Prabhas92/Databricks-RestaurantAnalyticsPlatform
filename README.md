# 🍽️ Restaurant Analytics Platform on Azure Databricks

<p align="center">

![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=for-the-badge&logo=databricks&logoColor=white)
![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)
![Delta Lake](https://img.shields.io/badge/Delta_Lake-00ADD8?style=for-the-badge)
![Unity Catalog](https://img.shields.io/badge/Unity_Catalog-1F77B4?style=for-the-badge)
![Lakeflow](https://img.shields.io/badge/Lakeflow-Pipelines-orange?style=for-the-badge)
![Azure Event Hub](https://img.shields.io/badge/Azure_Event_Hub-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

</p>

> **A production-style end-to-end Restaurant Analytics Platform built on Azure Databricks using the Medallion Architecture, Delta Lake, Unity Catalog, Lakeflow Declarative Pipelines, and Azure Event Hub for real-time data ingestion.**

---

# 📖 Project Overview

Modern restaurants generate enormous volumes of operational data every day—from customer orders and menu selections to restaurant reviews and customer interactions.

Simply storing this data is not enough.

Businesses need an intelligent analytics platform capable of:

- Processing streaming and batch data
- Maintaining high-quality datasets
- Performing scalable transformations
- Building analytical data models
- Delivering business-ready insights

This project demonstrates how these challenges can be solved using the modern Databricks Lakehouse Platform.

The pipeline ingests raw restaurant data, validates it, transforms it through the Bronze, Silver, and Gold layers, and produces curated datasets that power business dashboards and analytical reporting.

---

# 🚀 Key Features

✅ End-to-End Lakehouse Architecture

✅ Medallion Architecture (Bronze → Silver → Gold)

✅ Unity Catalog Governance

✅ Lakeflow Declarative Pipelines

✅ Delta Lake Storage

✅ Structured Streaming

✅ Azure Event Hub Integration

✅ Data Quality Expectations

✅ Real-Time Order Processing

✅ Customer 360 Analytics

✅ Restaurant Performance Analytics

✅ Sales Summary Aggregations

---

# 🏗️ Architecture

<p align="center">
<img src="project_architecture.png" width="900">
</p>

The platform follows the industry-standard **Medallion Architecture**, where data progressively becomes cleaner, richer, and more business-friendly.

```
                        Azure Event Hub
                              │
                              ▼
                    Lakeflow Pipeline
                              │
                Bronze (Raw Ingestion)
                              │
                              ▼
              Silver (Validated & Cleaned)
                              │
                              ▼
          Gold (Business Ready Data Models)
                              │
                              ▼
                   Dashboards & Analytics
```

---

# 📂 Repository Structure

```
Databricks-RestaurantAnalyticsPlatform

│
├── Data
│   ├── customers.csv
│   ├── restaurants.csv
│   ├── menu_items.csv
│   ├── customer_reviews.csv
│   ├── historical_orders.csv
│
├── Data Ingestion
│   ├── Ingestion_to_Bronze.ipynb
│   └── Ingestion_to_Silver.ipynb
│
├── EventHubDataIngestion
│   ├── transformations
│   └── explorations
│
├── Silver_Level_Transformations
│   ├── transformations
│   └── explorations
│
├── Gold_Level_Transformations
│   ├── transformations
│   └── explorations
│
├── Dashboard Images
│
├── project_architecture.png
│
└── README.md
```

---

# 🛠️ Technology Stack

| Layer | Technology |
|---------|------------|
| Cloud Platform | Azure |
| Data Platform | Databricks |
| Storage | Delta Lake |
| Data Processing | PySpark |
| Streaming | Structured Streaming |
| Messaging | Azure Event Hub |
| Governance | Unity Catalog |
| Pipeline | Lakeflow Declarative Pipelines |
| Language | Python |
| SQL Engine | Spark SQL |

---

# 📥 Data Sources

The project processes both historical and streaming datasets.

### Batch Data

- Customers
- Restaurants
- Menu Items
- Customer Reviews
- Historical Orders

### Streaming Data

Restaurant Orders are streamed through **Azure Event Hub**, simulating a real-world online ordering system.

---

# 🥉 Bronze Layer

The Bronze layer serves as the raw landing zone.

### Responsibilities

- Ingest streaming events
- Preserve original data
- Minimal transformations
- Schema enforcement
- Store immutable raw records

Streaming ingestion is implemented using:

- Azure Event Hub
- Kafka API
- Structured Streaming
- Lakeflow Declarative Pipelines

Example Bronze table:

```
01_bronze.orders
```

---

# 🥈 Silver Layer

The Silver layer performs data cleansing, enrichment, and validation.

Implemented transformations include:

- Timestamp conversion
- Date extraction
- Weekend identification
- Hour extraction
- JSON parsing
- Item count calculation
- Business rule validation

Data quality expectations ensure records with invalid values are automatically removed.

Examples include:

- Null Order IDs
- Invalid Order Status
- Invalid Payment Method
- Negative Revenue
- Missing Customer IDs

Example Silver tables

```
02_silver.fact_orders

02_silver.fact_order_items

02_silver.fact_reviews
```

---

# 🥇 Gold Layer

The Gold layer contains business-ready datasets designed for reporting and dashboarding.

Current Gold models include:

### 📊 Sales Summary

Daily KPIs including

- Total Revenue
- Average Order Value
- Total Orders
- Delivery Orders
- Dine-In Orders
- Takeaway Orders
- Active Restaurants
- Unique Customers

---

### 👥 Customer 360

Customer-centric analytical dataset including

- Customer Profile
- Lifetime Spend
- Ordering Behaviour
- Customer Segmentation

---

### ⭐ Restaurant Reviews

Aggregated review metrics including

- Average Rating
- Total Reviews
- Restaurant Performance

---

# ⚡ Lakeflow Declarative Pipelines

The project uses **Lakeflow Declarative Pipelines** to define scalable data pipelines.

Benefits include:

- Simplified ETL
- Automatic dependency management
- Incremental processing
- Built-in monitoring
- Streaming support
- Declarative transformations

---

# 📈 Data Quality

Data quality is enforced directly inside the pipeline using expectations.

Examples include validating:

- Order IDs
- Customer IDs
- Restaurant IDs
- Order Status
- Payment Method
- Positive Revenue
- Valid Item Count

Invalid records are automatically dropped before reaching downstream layers.

---

# 📊 Business Insights

The platform enables several analytical use cases.

### Sales Analytics

- Daily Revenue
- Revenue Trend
- Average Basket Size
- Peak Ordering Hours

### Customer Analytics

- Customer Lifetime Value
- Repeat Customers
- Customer Behaviour
- Spending Patterns

### Restaurant Analytics

- Restaurant Ratings
- Order Volume
- Revenue Contribution
- Restaurant Performance

---

# 📸 Dashboards

The repository includes sample dashboards demonstrating:

- Restaurant Analytics
- Customer Analytics
- Customer Reviews
- Sales Performance

Dashboard assets are available under:

```
Dashboard Images/
```

---

# ▶️ Running the Project

1. Create an Azure Databricks Workspace

2. Configure Unity Catalog

3. Create Catalogs and Schemas

4. Upload source datasets

5. Configure Azure Event Hub

6. Deploy Lakeflow Pipelines

7. Execute Bronze Layer

8. Execute Silver Layer

9. Execute Gold Layer

10. Connect Power BI or Databricks Dashboards

---

# 📚 Learning Outcomes

Through this project, I gained practical experience with:

- Azure Databricks
- Unity Catalog
- Lakehouse Architecture
- Delta Lake
- Structured Streaming
- Azure Event Hub
- Data Quality Expectations
- Lakeflow Declarative Pipelines
- PySpark Transformations
- Real-time Analytics

---

# 🚀 Future Improvements

- CI/CD using Azure DevOps
- Infrastructure as Code with Terraform
- Workflow orchestration
- Data lineage visualization
- Machine Learning for demand forecasting
- Customer recommendation engine
- Real-time alerting
- Data observability
- Cost optimization dashboards

---

# 🙏 Acknowledgements

This project was built by following and learning from the excellent **End-to-End Databricks Project** by **Afaq Ahmed**.

The implementation has been recreated, explored, and documented as a hands-on learning project to deepen my understanding of modern Azure Data Engineering concepts and Databricks best practices.

Special thanks to **Afaq Ahmed** for creating practical and industry-oriented learning content.

---

# 👨‍💻 Author

**Chethan**

Azure Data Engineer | Databricks | PySpark | Azure Data Factory | SQL

If you found this repository useful, consider giving it a ⭐ to support the project.
