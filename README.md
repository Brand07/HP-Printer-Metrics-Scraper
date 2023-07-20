# Python---HP-Printer-Scraper
Python script that scrapes the internal web pages of HP Printers for data. 

Prerequisites:
  This script requires that you disable "Encrypt All Web Communication (not including IPP) on the printer. This can be done from the internal webpage under the Networking Tab >> Mgmt. Protocals.
  This allows the script to request the webpage, otherwise the script would fail to reach the webpage. 
  
  **Do this at your own risk as you are disabling a security feature on your printer**

  ![msedge_MiwG7D5wCM](https://github.com/Brand07/Python---HP-Printer-Scraper/assets/81128304/857f363f-b7dd-4d55-934e-ab152758a916)



What the script does:
  This script specifically scrapes the internal webpages of HP printers (that are defined in the script) and pulls the following info:
    - The Date
    - Printer Name (as defined)
    - Page Count
    - Toner Level 
    - Maintenance Kit Level

  The script will look for a .xlsx file named (AllPrinters.xlsx). If if doesn't find the .xlsx, it will create one in the directory in which you run the script from.
