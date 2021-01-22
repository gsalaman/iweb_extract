# iweb_extract

## page extract thoughts
Want to crawl through the xml for a page, and extract text and images into an HTML file.

Pointer to directory for source images.
Pointer to directory for "output"
"filename" for html file (page)

Start by dropping HTML base tags.

Crawl the xml file:
* When you see paragraph text, drop it into our HTML file.
* When you see an image, see if it exists in our "source" directory.
  * If so, copy that image into our output dir and append the html file with a link pointer.
