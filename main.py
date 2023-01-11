import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Scatter
from pyecharts.charts import Page
from pyecharts.charts import WordCloud
import jieba
import numpy as np