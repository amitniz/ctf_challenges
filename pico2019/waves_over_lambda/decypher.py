import string

subs_map = {

'a':'x',
'b':'n',
'c':'e',
'd':'z',
'e':'w',
'f':'i',
'g':'f',
'h':'b',
'i':'k',
'j':'c',
'k':'s',
'l':'p',
'm':'r',
'n':'u',
'o':'a',
'p':'t',
'q':'h',
'r':'v',
's':'l',
't':'q',
'u':'y',
'v':'j',
'w':'g',
'x':'d',
'y':'o',
'z':'m'
}

plaintext =''
chypertext= "oscacu guyxymyrfpjq iomozodyr eok pqc pqfmx kyb yg guyxym lorsyrfpjq iomozodyr, o sobx yebcm ecss ibyeb fb ynm xfkpmfjp fb qfk yeb xou, obx kpfss mczczhcmcx ozybw nk yefbw py qfk wsyyzu obx pmowfj xcopq, eqfjq qollcbcx pqfmpccb ucomk owy, obx eqfjq f kqoss xckjmfhc fb fpk lmylcm lsojc. gym pqc lmckcbp f efss ybsu kou pqop pqfk sobxyebcmgym ky ec nkcx py joss qfz, ospqynwq qc qomxsu klcbp o xou yg qfk sfgc yb qfk yeb ckpopceok o kpmobwc pulc, ucp ybc lmcppu gmctncbpsu py hc zcp efpq, o pulc ohvcjp obx rfjfynk obx op pqc kozc pfzc kcbkcsckk. hnp qc eok ybc yg pqykc kcbkcsckk lcmkybk eqy omc rcmu ecss jolohsc yg syyifbw ogpcm pqcfm eymsxsu oggofmk, obx, ollomcbpsu, ogpcm bypqfbw cskc. guyxym lorsyrfpjq, gym fbkpobjc, hcwob efpq bcap py bypqfbw; qfk ckpopc eok yg pqc kzossckp; qc mob py xfbc op ypqcm zcb'k pohsck, obx gokpcbcx yb pqcz ok o pyoxu, ucp op qfk xcopq fp ollcomcx pqop qc qox o qnbxmcx pqynkobx mynhsck fb qomx jokq. op pqc kozc pfzc, qc eok oss qfk sfgc ybc yg pqc zykp kcbkcsckk, gobpokpfjos gcssyek fb pqc eqysc xfkpmfjp. f mclcop, fp eok byp kpnlfxfpupqc zovymfpu yg pqckc gobpokpfjos gcssyek omc kqmcex obx fbpcssfwcbp cbynwqhnp vnkp kcbkcsckkbckk, obx o lcjnsfom bopfybos gymz yg fp."

flag = "jybwmopk qcmc fk uynm gsow - gmctncbju_fk_j_yrcm_sozhxo_zomkhelylm"

for l in chypertext:
	if l in subs_map:
		plaintext += subs_map[l]
	else:
		plaintext += l
print("--------------------------------------------------------")
print(plaintext)
plaintext=''

for l in flag:
	if l in subs_map:
		plaintext += subs_map[l]
	else:
		plaintext += l
print("--------------------------------------------------------")
print(plaintext)
plaintext=''
