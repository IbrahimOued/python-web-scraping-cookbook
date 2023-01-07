from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def get_upcoming_events(url):
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    driver.get(url)

    events = driver.find_elements_by_xpath('//ul[contains(@class, "list-recent-events")]/li')

    for event in events:
        event_details = dict()
        event_details['name'] = event.find_element_by_xpath('p/span[@class="event-location"]').text
        event_details['location'] = event.find_element_by_xpath('p/time').text
        print(event_details)

    driver.quit()

get_upcoming_events('https://www.python.org/events/python-events/')