# AI-Powered Competitive Intelligence System

## Overview
A multi-agent AI system that monitors **HubSpot**, **Salesforce**, and **Zoho CRM** for competitive intelligence:

- **Hiring trends** – sales team growth  
- **Pricing changes** – plan adjustments and new features  
- **Strategic insights** – actionable recommendations  

The system stores historical data and outputs daily reports and a Streamlit dashboard.

## Agents

- **Hiring Agent:** Scrapes careers pages and counts sales-related mentions.  
- **Pricing Agent:** Simulates pricing changes and tracks feature additions (supports live scraping later).  
- **Strategy Agent:** Generates recommendations based on hiring and pricing signals.  
- **Report Agent:** Saves structured daily reports for all companies.

## Features

- Persistent memory for trends (`data/hiring_history.csv`, `data/{company}_pricing_history.json`)  
- Streamlit dashboard: top metrics, alerts, hiring trend charts  
- Multi-company processing in one execution

## Current Status

- Hiring agent scraping working for all 3 companies  
- Pricing agent simulating changes  
- Strategy and report agents functional  
- Dashboard displays metrics and trends

