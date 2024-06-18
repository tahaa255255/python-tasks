#make module to open favourite links
import chromelink
print("links avalaible :\n1-google.com\n2-youtube.com\n3-facebook.com")
c=int(input("enter the number of you'r choice:"))

if c==1:
    chromelink.chrome(chromelink.google_link)
elif c==2:
    chromelink.chrome(chromelink.youtube_link_link)
elif c==3:
    chromelink.chrome(chromelink.facebook_link)
else:
    print("invalid input")

    
   

