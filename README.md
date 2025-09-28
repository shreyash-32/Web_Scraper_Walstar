# Web_Scraper_Walstar
#  Google Maps Business Email Scraper  

This project scrapes business details (Name, Website, Phone, Address, and Email) from **Google Maps** using [SerpApi](https://serpapi.com/).  
It automatically visits business websites and extracts valid emails, saving results into an Excel file.  

---

##  Features  
-  Search businesses on Google Maps by **country, city, and category**.  
-  Extract details like **business name, phone, website, and address**.  
-  Scrape **emails directly from business websites**.  
-  Only businesses with a **valid email** are saved.  
-  Export results to **Excel (.xlsx)** for easy access.  

---

##  Requirements  
- Python 3.8+  
- SerpApi account & API key (879c9e99874d2041b0bdb71090bf39869e9c810422f945a32d69f6031d3e9e48)  

### Install Dependencies  
```bash
pip install requests pandas openpyxl
```

Then enter inputs:  
```
Enter your SerpApi API key: 879c9e99874d2041b0bdb71090bf39869e9c810422f945a32d69f6031d3e9e48
Enter country (e.g., United States): United States
Enter city or state (e.g., Kansas City or Missouri): Kansas City
Enter business categories (comma separated, e.g., electronics, restaurants): electronics, restaurants
Enter output Excel filename (e.g., businesses.xlsx): businesses.xlsx
---

##  Notes  
- Google Maps data comes from **SerpApi** (free tier has 100 searches/month).  
- If no emails are found, the business is skipped.  
- Some sites may hide emails in images, PDFs, or JS, which aren’t captured yet.  

---

##  Challenges Faced 
  There were multiple challenges in this project like:-

- Getting E-mails of the companies as they are not listed openly on any public platform so I had to scrape email from the companies   
  website
- The same challenge was with phone number
- I used google maps to scrape data which needed to get its API key ,I faced problems in getting it from Google cloud so I used SerpApi      
  for the key
