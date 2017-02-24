# Spider test
This is a test project of Spider using python.

***
### test 1 2 3 0221
First learning python and simple Spider realization.</br>
Meaningless projects

### sina
My first small spider for Weibo.cn.</br>

	Attention:
		cookie.txt is removed from the project, 
		considering the security of my own information
		you can create it by yourself.

Words following  are my logs ...or my comments just for myself.

####2.22
Simple log on to Weibo.cn and it can get HTML information from it. No other function.
	
	Way to Realize:
		Cookie appended to URL.

#### 2.23
Be able to search microblog depending on keyword.</br>

	Way to Realize:
		Append params in URL since we use GET to get the message.
		
Unfortunately, it is found that Weibo.cn dont provide LOCATION information *(actually it does provide, but you can`t open the URL, seems that something goes wrong in Weibo.cn)*, which is severely needed in our requirements.
</br>Maybe I should still go back to Weibo.com ...</br>
What a bad day!!!

#### 2.24
Create a list with info. just name and twitter context *(whole twitter, solve the problem of not showing completely----"...", like this)*.</br>
Complete simple file operation.</br>

	Way to Realize:
		Python File Operation:
			encode&decode to write&read binary information in txt.
			(avoid Spidering all the time while debugging)
		BeautifulSoup Learning:
			simple operation, really similar to XPath, which I`ve used before.

I find that Weibo.cn provide LOCATION information, but the rule is complicated. Anyway, I can go back on Weibo.cn.</br>
Cookies changes frequently, so it is not a good idea to use it in long-term project.</br>
Twitter context havent been analysized, now it is just a 'span' div.

