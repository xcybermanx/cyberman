#!/usr/bin/python
#>>> bismillah <<<
# Thank's to god first, to stackoverflow :p and  Syberia :D
# AUTHOR:  Skmkm
#joomla , wordpress graber
import re , urllib2 , sys , os 
from time import sleep
from platform import system
if os.name =='Linux' or os.name == "posix":
 os.system('clear')

 logo='''


 ____  _    __  __ _    __  __ 
/ ___|| | _|  \/  | | _|  \/  |  +----| Wordpress , joomla grabber |----+
\___ \| |/ / |\/| | |/ / |\/| |  |                                      |
 ___) |   <| |  | |   <| |  | |  +----|       Syberia- hackers        |----+ 
|____/|_|\_\_|  |_|_|\_\_|  |_|
                               

'''
 print (logo)

 for char in '\033[1;31m\t \t{+} Usage: \033[1;m' '\033[1;34mpython\033[1;m '+  sys.argv[0] + '\033[1;34m 127.0.0.1\033[1;m':
  sys.stdout.write(char)
  sys.stdout.flush()
  sleep(0.05)
 def unique(seq):
    seen = set()
    return [seen.add(x) or x for x in seq if x not in seen]
 try:
     lista= []
     page=1
     s=sys.argv[1]
     while page <= 100:
       bing = "http://www.bing.com/search?q=ip%3a"+s+"+&go=Rechercher&qs=ds&first="+str(page)
       openbing=urllib2.urlopen(bing)
       readbing=openbing.read()
       findsites=re.findall('<h2><a href="(.*?)"', readbing )
       for i in range(len(findsites)):
         allsites=findsites[i]
         allnoclean=re.findall("http://.*?/",allsites)
         lista.extend(allnoclean)
       page = page+50

 except (IndexError , urllib2.URLError):
	print '\n\033[1;32mPlease enter a valid ip adress or check your internet connection\033[1;m\n'
    	exit()
 print '\033[1;32m\nExtracting Websites ...\033[1;m'
 sleep(3)
 final = unique(lista)
 if len(final)==0:
   print ' \n\033[1;31mNo Websites found :/ \n \033[1;m'

 else:
  print "\nFound " , len(final) ,"sites"
  print "\n \033[1;33mWebsites Found on the server : \033[1;m"
  print "\n"
 for sites in final: 
	print '[+] '+ sites 
 	sleep(0.09)
 def unique(seq):
     seen = set()
     return [seen.add(x) or x for x in seq if x not in seen]

 try:
	 lista = []
	 s = sys.argv[1]
	 page = 1
	 print('\n')
	 while page <= 21:
		 bing = "http://www.bing.com/search?q=ip%3a"+s+"+index.php?option=com&go=Rechercher&qs=ds&first="+str(page)
		 openbing  = urllib2.urlopen(bing)
		 readbing = openbing.read()
		 findwebs = re.findall('<h2><a href="(.*?)"' , readbing)
		 for i in range(len(findwebs)):
			 jmnoclean = findwebs[i]
			 findjm = re.findall('(.*?)index.php', jmnoclean)
			 lista.extend(findjm)

		 page = page + 10

 except urllib2.URLError:
	pass            	
	
 final =  unique(lista)
 if len(final)==0:
           print '\n\033[1;31mNo Joomla Websites Found :/ \033[1;m\n'
 else:
           print '\nFound ', len(final) , ' Joomla Websites '
           print '\n\033[1;33mJoomla websites are : \033[1;m'
           print '\n'
 for sites in final:
           print '[+] ' + sites 
	   sleep(0.09)
 def unique(seq):
    seen = set()
    return [seen.add(x) or x for x in seq if x not in seen]

 try:
	lista = []
	s = sys.argv[1]
	page = 1
	print('\n')
	while page <= 21:
		bing = "http://www.bing.com/search?q=ip%3a"+s+"+?page_id=&go=Rechercher&qs=ds&first="+str(page)
		openbing  = urllib2.urlopen(bing)
		readbing = openbing.read()
		findwebs = re.findall('<h2><a href="(.*?)"' , readbing)
		for i in range(len(findwebs)):
			wpnoclean = findwebs[i]
			findwp = re.findall('(.*?)\?page_id=', wpnoclean)
			lista.extend(findwp)

		page = page + 10
 except urllib2.URLError:
            	pass
 final =  unique(lista)
 if len(final)==0:
           print '\n\033[1;31mNo Wordpress Websites Found :/ \033[1;m\n'
 else:
           print '\nFound ', len(final) , ' Wordpress Websites '
           print '\n\033[1;33mWordpress Websites are : \033[1;m'
           print '\n'
 for sites in final:
           print '[+] ' + sites 
           sleep(0.09)
 def unique(seq):
    seen = set()
    return [seen.add(x) or x for x in seq if x not in seen]


 try:
  lista=[]
  page=1
  s=sys.argv[1]
  while page <= 30:
   bing="http://www.bing.com/search?q=ip%3a"+s+"+/user/login&go=Rechercher&qs=ds&first="+str(page)
   openbing=urllib2.urlopen(bing)
   readbing=openbing.read()
   findwebs = re.findall('<h2><a href="(.*?)"' , readbing)
   for i in range(len(findwebs)):
      drp=findwebs[i]
      findrp=re.findall('(.*?)//user/login',drp)
      lista.extend(findrp)
   page=page+10
 except urllib2.URLError:
   pass
 final=unique(lista)
 final =  unique(lista)
 if len(final)==0:
           print '\n\033[1;31mNo Drupal Websites Found :/ \033[1;m\n'
 else:
           print '\nFound ', len(final) , ' Drupal Websites '
           print '\n\033[1;33mDrupal Websites are : \033[1;m'
           print '\n'
 for sites in final:
           print '[+] ' + sites 
           sleep(0.09)
   












  
if system()=='Windows':
 os.system('cls')
 logo='''


 ____  _    __  __ _    __  __ 
/ ___|| | _|  \/  | | _|  \/  |  +----| Wordpress , joomla grabber |----+
\___ \| |/ / |\/| | |/ / |\/| |  |                                      |
 ___) |   <| |  | |   <| |  | |  +----|       Syberia - hackers        |----+ 
|____/|_|\_\_|  |_|_|\_\_|  |_|
                               



'''
 print (logo)

 print '\t \t{+} Usage: python '+  sys.argv[0] + ' 127.0.0.1'
 def unique(seq):
    seen = set()
    return [seen.add(x) or x for x in seq if x not in seen]
 try:
     lista= []
     page=1
     s=sys.argv[1]
     while page <= 100:
       bing="http://www.bing.com/search?q=ip%3a"+s+"+&go=Rechercher&qs=ds&first="+str(page)
       openbing=urllib2.urlopen(bing)
       readbing=openbing.read()
       findsites=re.findall('<h2><a href="(.*?)"', readbing )
       for i in range(len(findsites)):
         allsites=findsites[i]
         allnoclean=re.findall("http://.*?/",allsites)
         lista.extend(allnoclean)
       page = page+50

 except (IndexError , urllib2.URLError):
	print '\nPlease enter a valid ip adress or check your internet connection\\n'
    	exit()
 print '\nExtracting Websites ...'
 sleep(3)
 final = unique(lista)
 if len(final)==0:
   print ' \nNo Websites found :/ \n '

 else:
  print "\nFound " , len(final) ,"sites"
  print "\n Websites Found on the server : "
  print "\n"
 for sites in final: 
	print '[+] '+ sites 
 	sleep(0.09)
 def unique(seq):
     seen = set()
     return [seen.add(x) or x for x in seq if x not in seen]

 try:
	 lista = []
	 s = sys.argv[1]
	 page = 1
	 print('\n')
	 while page <= 21:
		 bing = "http://www.bing.com/search?q=ip%3A"+s+"+index.php?option=com&go=Rechercher&qs=ds&first="+str(page)
		 openbing  = urllib2.urlopen(bing)
		 readbing = openbing.read()
		 findwebs = re.findall('<h2><a href="(.*?)"' , readbing)
		 for i in range(len(findwebs)):
			 jmnoclean = findwebs[i]
			 findjm = re.findall('(.*?)index.php', jmnoclean)
			 lista.extend(findjm)

		 page = page + 10

 except urllib2.URLError:
	pass            	
	
 final =  unique(lista)
 if len(final)==0:
           print '\nNo Joomla Websites Found :/ \n'
 else:
           print '\nFound ', len(final) , ' Joomla Websites '
           print '\nJoomla websites are : '
           print '\n'
 for sites in final:
           print '[+] ' + sites 
	   sleep(0.09)
 def unique(seq):
    seen = set()
    return [seen.add(x) or x for x in seq if x not in seen]

 try:
	lista = []
	s = sys.argv[1]
	page = 1
	print('\n')
	while page <= 21:
		bing = "http://www.bing.com/search?q=ip%3A"+s+"+?page_id=&go=Rechercher&qs=ds&first="+str(page)
		openbing  = urllib2.urlopen(bing)
		readbing = openbing.read()
		findwebs = re.findall('<h2><a href="(.*?)"' , readbing)
		for i in range(len(findwebs)):
			wpnoclean = findwebs[i]
			findwp = re.findall('(.*?)\?page_id=', wpnoclean)
			lista.extend(findwp)

		page = page + 10
 except urllib2.URLError:
            	pass
 final =  unique(lista)
 if len(final)==0:
           print '\nNo Wordpress Websites Found :/ \n'
 else:
           print '\nFound ', len(final) , ' Wordpress Websites '
           print '\nWordpress Websites are : '
           print '\n'
 for sites in final:
           print '[+] ' + sites 
           sleep(0.09)
 
 def unique(seq):
    seen = set()
    return [seen.add(x) or x for x in seq if x not in seen]


 try:
  lista=[]
  page=1
  s=sys.argv[1]
  while page <= 30:
   bing="http://www.bing.com/search?q=ip%3A"+s+"+/user/login&go=Rechercher&qs=ds&first="+str(page)
   openbing=urllib2.urlopen(bing)
   readbing=openbing.read()
   findwebs = re.findall('<h2><a href="(.*?)"' , readbing)
   for i in range(len(findwebs)):
      drp=findwebs[i]
      findrp=re.findall('(.*?)//user/login',drp)
      lista.extend(findrp)
   page=page+10
 except urllib2.URLError:
   pass
 final=unique(lista)
 final =  unique(lista)
 if len(final)==0:
           print '\nNo Drupal Websites Found :/ \n'
 else:
           print '\nFound ', len(final) , ' Drupal Websites '
           print '\n\Drupal Websites are : \ '
           print '\n'
 for sites in final:
           print '[+] ' + sites 
           sleep(0.09)
   
