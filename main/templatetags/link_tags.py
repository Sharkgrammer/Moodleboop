from django import template
register = template.Library()

@register.simple_tag
def get_links(LinkFull, r):
    from lxml import html
    import requests
    data = ""
    Link = split_link(LinkFull, 1)
    #return Link
    page2 = r.get(Link)
    tree2 = html.fromstring(page2.content)
    Links = tree2.xpath('//a')
    for y in range(0, len(Links)):
        if "forcedownload" in Links[y].get("href"):
            data += ("<p><a href='" + Links[y].get("href").replace("?forcedownload=1", "") + "'>" + Links[y].text  + "</a></p>")
            #print (Links[y].text.replace("Job Spec -","").replace("Job Spec ","").replace(".pdf","") +  "   " + Links[y].get("href").replace("?forcedownload=1", ""))
    return data

@register.simple_tag
def get_name(LinkFull):
    data = "https://logo.clearbit.com/" + LinkFull.split("-")[0].replace("<h3><b>", "").replace(" ","") + ".com?size=50"
    return data

@register.simple_tag
def split_link(LinkFull, mode):
    data = ""
    if (mode == 0):
        data = LinkFull.split("-----")[1]
    else:
        data = LinkFull.split("-----")[0]
    if (mode == 3):
        data = data.split("-")[0] + " has no image on the server"
    return data