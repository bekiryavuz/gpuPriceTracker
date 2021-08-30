from os import link
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from list import *
from getData import *









"""
products = {
    1: {'title': 'GeForce VD7552 RTX 3060 GAMING X 12G Graphics Board','ASIN': 'B08WPJ5P4R', 'price':85555},
    2: {'title': 'MSI GeForce VD7112 GTX 1660 SUPER AERO ITX OC Graphics Board','ASIN': 'B07ZHC95FP', 'price':60000},
    3: {'title': 'MSI GeForce VD7626 RTX 2060 VENTUS GP OC Graphics Board','ASIN': 'B091PVFYXM', 'price':74444},
    4: {'title': 'PowerColor Hellhound Spectral White AMD Radeon RX 6700XT','ASIN': 'B094MM9X6S', 'price':103333},
    5: {'title': 'MSI Radeon RX 6800 GAMING X TRIO 16G Graphics Board VD7459','ASIN': 'B08RHQC4KQ', 'price':157619} 
}
"""