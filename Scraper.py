import requests
import pandas as pd
import re
import time

# --------------------------
# Helper: Extract email from website
# --------------------------
def extract_email_from_website(url, retries=2):
    if not url:
        return None
    for attempt in range(retries):
        try:
            if not url.startswith("http"):
                url = "http://" + url
            r = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
            emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", r.text)
            if emails:
                return emails[0]
        except Exception:
            time.sleep(2)
    return None

# --------------------------
# Main script
# --------------------------
if __name__ == "__main__":
    api_key = input("Enter your SerpApi API key: ").strip()
    country = input("Enter country (e.g., United States): ").strip()
    city = input("Enter city or state (e.g., Kansas City or Missouri): ").strip()
    categories = input("Enter business categories (comma separated, e.g., electronics, restaurants): ").split(",")
    output_file = input("Enter output Excel filename (e.g., businesses.xlsx): ").strip()
    if not output_file.endswith(".xlsx"):
        output_file += ".xlsx"

    data = []
    for category in categories:
        query = f"{category.strip()} in {city}, {country}"
        print(f"\n🔍 Searching Google Maps for '{query}'...")

        url = "https://serpapi.com/search.json"
        params = {
            "engine": "google_maps",
            "q": query,
            "hl": "en",
            "type": "search",
            "api_key": api_key
        }

        try:
            res = requests.get(url, params=params)
            res.raise_for_status()
            results = res.json().get("local_results", [])
        except Exception as e:
            print(f"❌ API error for {query}: {e}")
            continue

        print(f"Found {len(results)} businesses for '{category.strip()}'.")

        for r in results:
            name = r.get("title")
            website = r.get("website")
            phone = r.get("phone")
            address = r.get("address")
            business_category = category.strip()

            email = extract_email_from_website(website)

            if name and email:  # ✅ only keep if email found
                data.append({
                    "Business Name": name,
                    "Email": email,
                    "Phone": phone or "N/A",
                    "Website": website or "N/A",
                    "Address": address or "N/A",
                    "Category": business_category
                })
                print(f"✅ Added: {name} | {email}")

    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)
    print(f"\n✅ Data saved to {output_file}, total records: {len(df)}")
