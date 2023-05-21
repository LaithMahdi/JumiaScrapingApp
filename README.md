# JumiaScrapingApp

To run the app you need to install django to follow this steps : 

1 - Install project dependencies 


pip install -r requirements.txt
  
2 - Perform initial migrations


python manage.py migrate
  
3 - Start the development server


python manage.py runserver
  

The Django project focuses on scraping data from the Jumia Tunisia website within the phones category. This project aims to retrieve relevant information about various phone products listed on the Jumia Tunisia platform.


By leveraging web scraping techniques, the project collects data such as product names, prices, descriptions, and other details related to phones available for sale on Jumia Tunisia. This data can be used for various purposes, including price comparison, market analysis, or building a product catalog.

The project utilizes the Django framework, a powerful Python web development framework, to structure and manage the application. Django provides a convenient and efficient way to handle URL routing, database management, and rendering HTML templates.

To execute the scraping process, the project likely employs popular Python libraries such as BeautifulSoup or Scrapy. These libraries enable the extraction of specific HTML elements from the Jumia Tunisia website's pages, allowing the project to access and gather the desired phone data.

With the collected information, the Django project can offer functionality such as displaying the scraped phone data in a user-friendly format, implementing search and filtering options, and providing a seamless browsing experience for users interested in purchasing phones from Jumia Tunisia.
  
  
![jumia](https://github.com/LaithMahdi/JumiaScrapingApp/assets/109853134/337fadb5-834e-4a31-bab9-9677fb85bd10)
