# Microsoft-Fabric-ETL-Pipeline-Weekly-Credit-Card-Report

📌 Project Overview

This project demonstrates a real-world end-to-end data analytics architecture built using Microsoft Fabric, following the Medallion Architecture (Bronze, Silver, Gold) pattern.

The solution processes weekly credit card transaction data along with customer master data, applies secure transformations, and delivers business-ready insights through Power BI dashboards.

The architecture is designed to be scalable, secure, event-driven, and production-ready, closely aligning with enterprise analytics implementations.

🏗️ Architecture Diagram

![Fabric ETL Project](./images/Fabric_ETL_Pipeline.png)

📌 The diagram illustrates data ingestion, transformation, storage, security boundaries, and reporting using Microsoft Fabric and OneLake.

🧱 Architecture Layers
🟫 Bronze Layer (Raw Data)

Stores raw credit card transaction data (CSV)

Event-driven ingestion using:

Azure Data Lake Gen2

Event Hub

EventStream

Fabric Pipeline (Copy Data)

Acts as a source of truth for reprocessing and auditing

🪙 Silver Layer (Clean & Transformed)

Data cleaning, validation, and transformation

Technologies used:

Fabric Notebooks (PySpark / SQL) for credit card data

Dataflow Gen2 for customer data from Azure SQL

Column-level filtering applied to secure sensitive customer data

🥇 Gold Layer (Business-Ready)

Aggregated and curated datasets

Optimized for analytics and reporting

Serves as the single source for Power BI dashboards

🔄 Data Sources
Source	Type	Ingestion Method
Credit Card Transactions	CSV	Event-driven (Event Hub + Pipeline)
Customer Data	Azure SQL	Scheduled refresh (Dataflow Gen2)
🔐 Security & Access Control

Separate workspaces for:

Bronze & Silver (Data Engineering)

Gold (Analytics & Reporting)

Role-based access:

Data Engineer – Admin access to pipelines, notebooks, lakehouse

Data Analyst – Contributor access only to Gold layer

Implements least-privilege access principle

Column-level security for personal data

📈 Reporting & Analytics

Power BI dashboards built on Gold Layer

Enables:

Weekly revenue analysis

Week-over-week trends

Credit card transaction insights

Optimized for performance and governed access

☁️ OneLake Integration

All layers stored in OneLake

Benefits:

Centralized storage

No data duplication

Cross-workspace data access

Simplified governance

🛠️ Tools & Technologies Used

Microsoft Fabric

OneLake

Event Hub & EventStream

Fabric Pipelines

Dataflow Gen2

Fabric Notebooks (PySpark, SQL)

Delta Lake tables

Power BI

🎯 Key Learnings

Designing medallion architecture in Microsoft Fabric

Implementing event-driven and batch ingestion together

Applying enterprise-level security and workspace separation

Building analytics-ready Gold datasets for Power BI

📌 Use Cases

Banking & Financial analytics

Credit card transaction monitoring

Enterprise reporting platforms

Fabric Data Engineering reference architecture

🚀 Future Enhancements

Incremental loading optimizations

Real-time dashboarding

CI/CD using Fabric deployment pipelines

Data quality checks and monitoring

👤 Author

Shubham Gagare
Fabric Data Engineer | Power BI | Analytics Engineering
📍 Pune, India

📌 How to add the image correctly

Save your diagram image as:
architecture.png

Place it in the root folder of the GitHub repo

The README will automatically render it

If you want, next I can:

Optimize this README for recruiters

Add badges (Fabric, Power BI, Azure)

Write a LinkedIn post + GitHub description

Make a project explanation for interviews
