from behave import *
from selenium import webdriver
import time
from os import *
import os

from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.page_model.home_page import HomePage
from tests.acceptance.page_model.new_post_page import NewPostPage

use_step_matcher('re')


@given('I am on the homepage')
def step_impl(context):
    basepath = os.getcwd().split('\\venv\\Lib\\site-packages')
    filepath = basepath[0] + '\\webdriver\\chromedriver.exe'
    print("Chrome driver path: "+filepath)
    context.browser = webdriver.Chrome(filepath)
    page = HomePage(context.browser)
    context.browser.get(page.url)


@given('I am on the blog page')
def step_impl(context):
    basepath = os.getcwd().split('\\venv\\Lib\\site-packages')
    filepath = basepath[0] + '\\webdriver\\chromedriver.exe'
    context.browser = webdriver.Chrome(filepath)
    page = BlogPage(context.browser)
    context.browser.get(page.url)


@given('I am on the new post page')
def step_impl(context):
    basepath = os.getcwd().split('\\venv\\Lib\\site-packages')
    filepath = basepath[0] + '\\webdriver\\chromedriver.exe'
    context.browser = webdriver.Chrome(filepath)
    page = NewPostPage(context.browser)
    context.browser.get(page.url)


@then('I am on the blog page')
def step_impl(context):
    expected_url = BlogPage(context.browser).url
    assert context.browser.current_url == expected_url
    time.sleep(2)


@then('I am on the home page')
def step_impl(context):
    expected_url = HomePage(context.browser).url
    print('Expected Url: ', expected_url)
    print('Actual Url: ', context.browser.current_url)
    assert context.browser.current_url == expected_url
    time.sleep(2)
