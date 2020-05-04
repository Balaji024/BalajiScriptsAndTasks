import requests
import bs4

#https://www.amazon.in/s?k=phone&ref=nb_sb_noss_2
##soldByThirdParty > span
#<span class="a-size-medium a-color-price inlineBlock-display offer-price a-text-normal price3P">₹&nbsp;2,299.00</span>
def price(url):
   res = requests.get(url)
   res.raise_for_status()
   print('Hi')
   soup = bs4.BeautifulSoup(res.text,'html.parser')
   elems=soup.select('html.a-js.a-audio.a-video.a-canvas.a-svg.a-drag-drop.a-geolocation.a-history.a-webworker.a-autofocus.a-input-placeholder.a-textarea-placeholder.a-local-storage.a-gradients.a-transform3d.-scrolling.a-text-shadow.a-text-stroke.a-box-shadow.a-border-radius.a-border-image.a-opacity.a-transform.a-transition.a-ember body.a-aui_72554-c.a-aui_dropdown_187959-c.a-aui_pci_risk_banner_210084-c.a-aui_perf_130093-c.a-aui_preload_261698-c.a-aui_tnr_v2_180836-c.a-aui_ux_145937-c.a-meter-animate div#a-page div#dp.ebooks.en_IN div#dp-container.a-container div#rightCol div#CombinedBuybox.feature div#combinedBuyBox.a-section.a-spacing-medium div#buybox.a-box.a-spacing-micro div.a-box-inner.a-padding-base table.a-lineitem.a-spacing-micro tbody tr.kindle-price td.a-color-price.a-size-medium.a-align-bottom span.a-size-medium.a-color-price')
   #elems=soup.select('html.a-ws.a-js.a-audio.a-video.a-canvas.a-svg.a-drag-drop.a-geolocation.a-history.a-webworker.a-autofocus.a-input-placeholder.a-textarea-placeholder.a-local-storage.a-gradients.a-transform3d.-scrolling.a-text-shadow.a-text-stroke.a-box-shadow.a-border-radius.a-border-image.a-opacity.a-transform.a-transition.a-ember body.a-aui_72554-c.a-aui_dropdown_187959-c.a-aui_pci_risk_banner_210084-c.a-aui_perf_130093-c.a-aui_preload_261698-c.a-aui_tnr_v2_180836-c.a-aui_ux_145937-c.a-meter-animate div#a-page div#dp.ebooks.en_IN div#dp-container.a-container div#rightCol div#CombinedBuybox.feature div#combinedBuyBox.a-section.a-spacing-medium div#buybox.a-box.a-spacing-micro div.a-box-inner.a-padding-base table.a-lineitem.a-spacing-micro tbody tr.kindle-price td.a-color-price.a-size-medium.a-align-bottom span.a-size-medium.a-color-price')
   return elems[0].text.strip()
price1=price('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming-ebook/dp')
#price1= price('https://www.amazon.in/Automate-Boring-Stuff-Python-2nd/dp/1593279922/ref=sr_1_1?crid=1DLNWEG0RZ4S9&dchild=1&keywords=automate+boring+stuff+with+python&qid=1588603678&sprefix=automate+borin%2Caps%2C1130&sr=8-1')
print('The Price is ' + price1)
