#!/usr/bin/python3.7
import string
import sys

def hist(str):
	for l in str:
		if l in hist_list:
			hist_list[l]+=1


hist_list = dict([[x,0] for x in string.ascii_lowercase])

chypertext = "emujuw pwdzdcdxlnhr becefekdx gea nru nrlcz ads dp pwdzdc texmdxlnhr becefekdx, e mesz dgsuc gumm bsdgs ls dqc zlanclhn ls rla dgs zew, esz anlmm cufufyucuz efdso qa dglso nd rla omddfw esz nceolh zuenr, grlhr rettusuz nrlcnuus wueca eod, esz grlhr l aremm zuahclyu ls lna tcdtuc tmehu. pdc nru tcuausn l glmm dsmw aew nren nrla meszdgsucpdc ad gu qauz nd hemm rlf, emnrdqor ru reczmw atusn e zew dp rla mlpu ds rla dgs uanenugea e ancesou nwtu, wun dsu tcunnw pcuiqusnmw nd yu fun glnr, e nwtu eyvuhn esz xlhldqa esz en nru aefu nlfu ausaumuaa. yqn ru gea dsu dp nrdau ausaumuaa tucadsa grd ecu xucw gumm heteymu dp mddblso epnuc nrulc gdcmzmw eppelca, esz, ettecusnmw, epnuc sdnrlso umau. pwdzdc texmdxlnhr, pdc lsaneshu, yuoes glnr sujn nd sdnrlso; rla uanenu gea dp nru afemmuan; ru ces nd zlsu en dnruc fus'a neymua, esz peanusuz ds nruf ea e ndezw, wun en rla zuenr ln ettuecuz nren ru rez e rqszcuz nrdqaesz cdqymua ls recz hear. en nru aefu nlfu, ru gea emm rla mlpu dsu dp nru fdan ausaumuaa, pesneanlhem pummdga ls nru grdmu zlanclhn. l cutuen, ln gea sdn anqtlzlnwnru fevdclnw dp nruau pesneanlhem pummdga ecu arcugz esz lsnummlousn usdqoryqn vqan ausaumuaasuaa, esz e tuhqmlec senldsem pdcf dp ln."

hist(chypertext)

print(hist_list)
