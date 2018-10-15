from lxml import html
import requests
loginpage = "http://bismoodle2.ucc.ie/moodle/login/index.php?"
r = requests.Session()
payload = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', 'username':'116397543', 'password':'passwordhere'}
r.post(loginpage, data = payload)
weburl = "http://pokergamelabs.gearhostpreview.com/pyplace/EconFile.php?"
page = r.get('http://bismoodle2.ucc.ie/moodle/course/view.php?id=2')
print(page)
tree = html.fromstring(page.content)
LinkData = tree.xpath('//div[@class="activityinstance"]//a')
NameData = tree.xpath('//div[@class="activityinstance"]//a//span[@class="instancename"]/text()')
for x in range (0, len(LinkData)):
    if "resource" not in LinkData[x].get("href") and "Assignment" not in NameData[x] and "Placement Offer" not in NameData[x] and "Opportunity Update" not in NameData[x]:
        print (NameData[x] + "  " + LinkData[x].get("href"))
        page2 = r.get(LinkData[x].get("href"))
        tree2 = html.fromstring(page2.content)
        Links = tree2.xpath('//a')
        for y in range(0, len(Links)):
            if "forcedownload" in Links[y].get("href") and "keane_kelly_daniel" not in Links[y].get("href"):
                print (Links[y].text.replace("Job Spec -","").replace(".pdf","") +  "   " + Links[y].get("href").replace("?forcedownload=1", ""))