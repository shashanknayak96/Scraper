# Scraper
A scraper to scrap a placement website and send email regarding the same...

So basically I tried to scrap from [the placement page](http://www.pvppcoe.ac.in/placement-notice)

The scraper would scrap the most recent data (Provided that the scrapper keeps running continously... More on that later) and sends an email about the same. 

The script makes use of requests and bs4 to do the scraping. 

To be able to remember if the data is new or old I simply created a text file. When the script runs, the text file is checked to make sure that the data is new. If so, the mail is send else nothing happens. Yeah! Rocket science! :rocket:

A better approach to all of these would be to save the script to a cloud and run a scheduler. Thus making the script to run without your computer. :grin:
