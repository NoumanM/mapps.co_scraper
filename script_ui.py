import csv
import os
import time
from glob import glob
import requests
from lxml.html import fromstring
# import seleniumwire.undetected_chromedriver as uc_wire
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

working_dir = os.getcwd()
download_dir_path = os.path.join(working_dir, 'downloaded_pdfs')
firefox_driver_path = os.path.join(working_dir, 'geckodriver.exe')
done_urls_csv_path = os.path.join(working_dir, 'done_url.csv')


def select_from_option(driver, xpath, option_text):
    dropdown_element = driver.find_element(By.XPATH, xpath)
    select = Select(dropdown_element)
    select.select_by_visible_text(option_text)
    selected_option = select.first_selected_option
    print(f'Selected option: {selected_option.text}')


def create_firefox_driver(healdess=False):
    try:
        firefox_options = Options()
        firefox_options.set_preference("browser.download.folderList", 2)
        firefox_options.set_preference("browser.download.dir", download_dir_path)
        firefox_options.set_preference("browser.helperApps.alwaysAsk.force", False)
        firefox_options.set_preference("browser.download.manager.showWhenStarting", False)
        firefox_options.set_preference("services.sync.prefs.sync.browser.download.manager.showWhenStarting", False)
        firefox_options.set_preference("browser.download.useDownloadDir", True)
        firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
        firefox_options.set_preference("pdfjs.disabled", True)

        driver = webdriver.Firefox(service=Service(executable_path=firefox_driver_path), options=firefox_options)

        driver.maximize_window()
        time.sleep(3)
        driver.get("https://mapps.co.maui.hi.us/EnerGov_Prod/SelfService#/search?m=2&ps=100&pn=101&em=true")
        return driver
    except Exception as e:
        print(e)
        print("----Got Exception----")

driver = create_firefox_driver()
time.sleep(25)
select_from_option(driver, "(//select[@aria-label='Sort'])[1]", 'Finalized Date')
time.sleep(30)
select_from_option(driver, "(//select[@id='SortAscending'])[1]", 'Descending')
time.sleep(30)
for page_number in range(2, 110):
    time.sleep(15)
    page = driver.page_source
    data = fromstring(page)
    all_fields = data.xpath('//div[contains(@id, "entityRecordDiv")]')
    for field in all_fields:
        try:
            PermitNo = field.xpath('.//label[contains(text(), "Permit Number")]/parent::*//span/text()')[0].strip()
        except:
            PermitNo = ''
        try:
            Type = field.xpath('.//label[contains(text(), "Type")]/parent::*//span/text()')[0].strip()
        except:
            Type = ''
        try:
            ProjectName = field.xpath('.//label[contains(text(), "Project Name")]/parent::*//span/text()')[0].strip()
        except:
            ProjectName = ''
        try:
            Status = field.xpath('.//label[contains(text(), "Status")]/parent::*//span/text()')[0].strip()
        except:
            Status = ''
        try:
            MainParcel = field.xpath('.//label[contains(text(), "Main Parcel")]/parent::*//span/text()')[0].strip()
        except:
            MainParcel = ''
        try:
            Address = field.xpath('.//label[contains(text(), "Address")]/parent::*//span/text()')[0].strip()
        except:
            Address = ''
        try:
            Description = field.xpath('.//label[contains(text(), "Description")]/parent::*//span/text()')[0].strip()
        except:
            Description = ''
        try:
            AppliedDate = field.xpath('.//label[contains(text(), "Applied Date")]/parent::*//span/text()')[0].strip()
        except:
            AppliedDate = ''
        try:
            IssuedDate = field.xpath('.//label[contains(text(), "Issued Date")]/parent::*//span/text()')[0].strip()
        except:
            IssuedDate = ''
        try:
            ExpirationDate = field.xpath('.//label[contains(text(), "Expiration Date")]/parent::*//span/text()')[0].strip()
        except:
            ExpirationDate = ''
        try:
            FinalizedDate = field.xpath('.//label[contains(text(), "Finalized Date")]/parent::*//span/text()')[0].strip()
        except:
            FinalizedDate = ''
        try:
            PermitURL = field.xpath('.//label[contains(text(), "Permit Number")]/parent::*//a/@href')[0].strip()
            PermitURL = f"https://mapps.co.maui.hi.us/EnerGov_Prod/SelfService" + PermitURL
        except:
            PermitURL = ''
        print(PermitNo, Type, ProjectName, Status, MainParcel, Address, Description, AppliedDate, IssuedDate, ExpirationDate, FinalizedDate)

        exists = False
        if os.path.exists('data.csv'):
            exists = True
        with open('data.csv', 'a+', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            if not exists:
                writer.writerow(['PermitNo', 'Type', 'ProjectName', 'Status', 'MainParcel', 'Address', 'Description', 'AppliedDate', 'IssuedDate', 'ExpirationDate', 'FinalizedDate', 'PermitURL'])
            writer.writerow([PermitNo, Type, ProjectName, Status, MainParcel, Address, Description, AppliedDate, IssuedDate, ExpirationDate, FinalizedDate, PermitURL])
    driver.find_element(By.XPATH, f'//a[@id="link-NextPage"]').click()
    print(f'Page {page_number}')
    time.sleep(10)



