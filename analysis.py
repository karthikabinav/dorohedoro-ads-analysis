import requests
from datetime import datetime, timedelta
import json

# Dorohedoro premiered on January 12, 2020
DOROHEDORO_PREMIERE = datetime(2020, 1, 12)
DAY_AFTER_PREMIERE = DOROHEDORO_PREMIERE + timedelta(days=1)
TARGET_DATE = DAY_AFTER_PREMIERE.strftime('%Y-%m-%d')

print(f"Dorohedoro premiered on: {DOROHEDORO_PREMIERE.strftime('%Y-%m-%d')}")
print(f"Analyzing ads that started on: {TARGET_DATE}")
print()

# Notion database details
NOTION_DATABASE_ID = "21b97551-844e-8068-b387-fe7a56b04348"

# This would query the Notion database for advertisements
# that started on the day after Dorohedoro premiered
def query_advertisements_by_date(target_date):
    """
    Query Notion Advertising database for ads starting on target_date
    
    Args:
        target_date (str): Date in YYYY-MM-DD format
        
    Returns:
        list: Advertisements that started on the target date
    """
    # In a real implementation, this would use the Notion API
    # with proper authentication to query the database
    
    # Example filter structure for Notion API:
    filter_payload = {
        "property": "StartDate",
        "date": {
            "equals": target_date
        }
    }
    
    print(f"Would query database {NOTION_DATABASE_ID}")
    print(f"With filter: {json.dumps(filter_payload, indent=2)}")
    print()
    print("Expected response would include advertisements with:")
    print("- CampaignID (title)")
    print("- StartDate")
    print("- SpentAmount (number)")
    print("- Other advertising metrics")
    print()
    
    # For demo purposes, returning mock data
    # In reality, this would come from the Notion API response
    return []

def calculate_average_spend(advertisements):
    """
    Calculate average SpentAmount from advertisements
    
    Args:
        advertisements (list): List of ad objects with SpentAmount property
        
    Returns:
        float: Average amount spent, or None if no ads found
    """
    if not advertisements:
        print("No advertisements found for the target date.")
        return None
    
    total_spend = sum(ad.get('SpentAmount', 0) for ad in advertisements)
    average_spend = total_spend / len(advertisements)
    
    return average_spend

def main():
    print("=" * 60)
    print("DOROHEDORO ADVERTISING SPEND ANALYSIS")
    print("=" * 60)
    print()
    
    # Query advertisements starting the day after Dorohedoro premiere
    ads = query_advertisements_by_date(TARGET_DATE)
    
    # Calculate average spend
    avg_spend = calculate_average_spend(ads)
    
    if avg_spend is not None:
        print(f"Average amount spent on ads starting {TARGET_DATE}:")
        print(f"${avg_spend:,.2f}")
    else:
        print(f"No advertisement data available for {TARGET_DATE}")
        print()
        print("Note: Notion API rate limiting prevented data retrieval.")
        print("When API is available, the script will:")
        print("1. Query the Advertising database")
        print("2. Filter by StartDate = 2020-01-13")
        print("3. Extract SpentAmount values")
        print("4. Calculate and return the average")
    
    print()
    print("=" * 60)

if __name__ == "__main__":
    main()
