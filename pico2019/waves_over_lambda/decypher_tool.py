import string

chypertext =" emujuw pwdzdcdxlnhr becefekdx gea nru nrlcz ads dp pwdzdc texmdxlnhr becefekdx, e mesz dgsuc gumm bsdgs ls dqc zlanclhn ls rla dgs zew, esz anlmm cufufyucuz efdso qa dglso nd rla omddfw esz nceolh zuenr, grlhr rettusuz nrlcnuus wueca eod, esz grlhr l aremm zuahclyu ls lna tcdtuc tmehu. pdc nru tcuausn l glmm dsmw aew nren nrla meszdgsucpdc ad gu qauz nd hemm rlf, emnrdqor ru reczmw atusn e zew dp rla mlpu ds rla dgs uanenugea e ancesou nwtu, wun dsu tcunnw pcuiqusnmw nd yu fun glnr, e nwtu eyvuhn esz xlhldqa esz en nru aefu nlfu ausaumuaa. yqn ru gea dsu dp nrdau ausaumuaa tucadsa grd ecu xucw gumm heteymu dp mddblso epnuc nrulc gdcmzmw eppelca, esz, ettecusnmw, epnuc sdnrlso umau. pwdzdc texmdxlnhr, pdc lsaneshu, yuoes glnr sujn nd sdnrlso; rla uanenu gea dp nru afemmuan; ru ces nd zlsu en dnruc fus'a neymua, esz peanusuz ds nruf ea e ndezw, wun en rla zuenr ln ettuecuz nren ru rez e rqszcuz nrdqaesz cdqymua ls recz hear. en nru aefu nlfu, ru gea emm rla mlpu dsu dp nru fdan ausaumuaa, pesneanlhem pummdga ls nru grdmu zlanclhn. l cutuen, ln gea sdn anqtlzlnwnru fevdclnw dp nruau pesneanlhem pummdga ecu arcugz esz lsnummlousn usdqoryqn vqan ausaumuaasuaa, esz e tuhqmlec senldsem pdcf dp ln.".upper()



subs_map = dict([[x,x] for x in string.ascii_uppercase])
plaintext =''

while 1:
	print("plaintext:\n-------------------------------------------------------")
	for l in chypertext:
		if l in subs_map:
			plaintext += subs_map[l]
		else:
			plaintext += l
	print(plaintext)
	print("--------------------------------------------------------")
	letter, sub = input("letter,sub: ").split(',')
	if letter.upper() in subs_map: 
		subs_map[letter.upper()] = sub.lower()
	
	plaintext = ''
