
def square(a):
  """item_exporters.py contains Scrapy item exporters.

Once you have scraped your items, you often want to persist or export those items, to use the data in some other
application. That is, after all, the whole purpose of the scraping process.

For this purpose Scrapy provides a collection of Item Exporters for different output formats, such as XML, CSV or JSON.

More Info:
    https://doc.scrapy.org/en/latest/topics/exporters.html

"""
  return a**a


x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")
