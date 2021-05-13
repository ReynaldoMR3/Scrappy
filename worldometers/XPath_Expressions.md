### XPATH expressions

Select elements from a HTML page with
`//`

Select all H1 expressions
`//h1`

Select element with a specific attribute

`//div[@class='intro']`

`//div[@class='intro']/p`

`//div[@class='intro' or @class='outro']/p`

`//div[@class='intro']/p/text()`

`//a/@href`

`//a[starts-with(@href, 'https')]`

`//a[ends-with(@href, 'mx')]`

`//a[contains(@href, 'google')]`

`//a[contains(text(), 'Mexico')]`

`//ul[@id='items']/li[1 or 4]`

`//ul[@id='items']/li[position() = 1 or position() = last()]`

`//ul[@id='items']/li[position() > 1]`


Look for a parent element

`//p[@id='unique']/parent::div`

`//p[@id='unique']/parent::node()`

`//p[@id='unique']/ancestor::node()`

`//p[@id='unique']/ancestor-or-self::node()`

`//p[@id='unique']/preceding::node()`

`//p[@id='outside']/preceding-sibling::node()`


Look for a children element

`//div[@class='intro']/child::p`

`//div[@class='intro']/child::node()`

`//div[@class='intro']/following::node()`

`//div[@class='intro']/following-sibling::node()`

`//div[@class='intro']/descendant::node()`













