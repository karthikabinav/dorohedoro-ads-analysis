# Dorohedoro Advertising Analysis

This repository contains analysis of advertising spend for campaigns that started the day after the anime *Dorohedoro* premiered.

## Background

- **Dorohedoro** premiered on: **January 12, 2020**
- **Target analysis date**: January 13, 2020 (the day after premiere)
- **Data source**: Notion Advertising database
- **Database ID**: `21b97551-844e-8068-b387-fe7a56b04348`

## Objective

Calculate the average amount spent on advertisements that started on January 13, 2020, using data from the cloud-based Advertising database.

## Methodology

1. Identify Dorohedoro's premiere date (2020-01-12)
2. Calculate the target date (2020-01-13, day after premiere)
3. Query the Advertising database filtering by StartDate = 2020-01-13
4. Extract SpentAmount values from matching advertisements
5. Calculate the average spend

## Notion Database Schema

The Advertising database contains the following relevant properties:
- **CampaignID** (title): Unique campaign identifier
- **StartDate** (date): Campaign start date
- **SpentAmount** (number): Total amount spent on the campaign
- Additional metrics: Impressions, Clicks, Conversions, ROI, etc.

## Usage

Run the analysis script:
```bash
python analysis.py
```

## Current Status

Due to Notion API rate limiting, the actual data retrieval is temporarily unavailable. The repository contains:
- `analysis.py`: Script demonstrating the analysis logic
- This README: Documentation of the methodology

When API access is restored, the script will successfully query the database and calculate the average spend.

## Expected Output

When run with successful API access, the script will output:
- Number of advertisements found for 2020-01-13
- List of SpentAmount values
- Calculated average spend (e.g., "$1,250.00")

## Files

- `analysis.py`: Main analysis script
- `README.md`: This documentation file
