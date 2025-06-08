# 🏥 Healthcare Claims ETL Pipeline using DBT & PostgreSQL

This project demonstrates a complete Data Engineering workflow for transforming healthcare claims data using **dbt** and **PostgreSQL**. Built to highlight my skills in data modeling, testing, and SQL-based transformations.

## 👨‍💻 Developer
**Yaswanth Nissankara** — Data Engineer  
📧 yaswanthnissankara99@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/yaswanthnissankara99)

## 🚀 Tech Stack
- **DBT (v1.9.6)** – transformation and testing
- **PostgreSQL** – database and raw table storage
- **YAML, SQL, Bash** – configuration and scripting
- **macOS, VS Code, Terminal** – local dev environment

## 🛠 Features Implemented
- ✅ Source setup using `sources:` block and schema.yml
- ✅ DBT models for staging and transformation
- ✅ Data quality checks (`not_null`, `unique`)
- ✅ Full CI-style pipeline with build + test
- ✅ Validated database connectivity and model execution

## 🧪 Data Tests
- `claim_id` is unique and not null
- `patient_id` is not null

## 📂 Project Structure


## 🗂 Sample Data
The `claims` table includes:
- `claim_id`
- `patient_id`
- `procedure_code`
- `amount`
- `claim_date`

## 🏁 How to Run
1. Clone the repo and install dbt
2. Set up PostgreSQL and load the `claims` table
3. Run:
   ```bash
   dbt run
   dbt test
