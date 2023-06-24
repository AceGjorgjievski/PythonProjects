ABS
----

dominantni strategii - strategija s1 e dominantna vo odnos na strategija s2
		ako sekoja sostojba vo koja kje se najde agentot igrajkji ja
		taa strategija e podobro od strategijata s2

pareto optimality - sostojba vo koja najmalku eden od agentite bi ja podobril
		pozicijata bez da ja vloshi situacijata na drugiot



nagradata e mnogu biten koncept bidejkji tokmu vo ucenje so potiknuvanje
toa e onoj vid na koncept koj shto prepoznavame [ja prepoznavame okolinata].
Vo markovite procesi na odluchuvanje ili vo ovoj tip na problemi, agentot podobro
ja prepoznava okolinata preku feedback [ishodot] od okolinata ili koga kje deluva po 
okolinata/ prevzeme soodvetna akcija. 

Markov's Rule : slednata sostojba vo koja se preogja zavisi samo od sostojbata vo koja 
	           momentalno se naogja agentot.

Imame sostojba, akcii koi mozhat da se izvedat i koga kje se izbere akcijata, ne znaeme
vo koja sostojba kje zavrshime, megjutoa toa shto go znaeme e verojatnost na raspredelba
za nivno sluchuvanje.
Da se bide vo prozivolna sostojba i da se izbere odredena akcija od tie mozhni,
no ne znaeme kade zavrshuvame, voobichaeno se narekuva cool state.

optimalna politika -> vo dadena sostojba, koja akcija da ja prevzeme agentot [pi*: S -> A]
	[preporaka, shto akcija da odberesh]
najdobra akcija da odbereme -> e onaa koja kje go donese agentot do najdobra dobivka vo idnina
---------------------------------------------------------------------------------------------------------------------
uchenje so pottiknuvanje - mora da se proba akcijata za da se nauchish kako
		se odnesuva okolu okolinata
MDPs - znaevme odredeni pravila, gi znaeme verijatnostite, znaevme nekoj model
	na okolinata
---------------------------------------------------------------------------------------------------------------------
kolku e popustot pogolem, kako da ja potkrastuva vrednosta na nagradata vo idnina,
toa znachi agentot mozhe da bide poalchen

---------------------------------------------------------------------------------------------------------------------	

Vrednost na sostojba V*(s) - ochekuvana dobivka dokolku zapochneme vo taa sostojba 
		i se odnesuvame optimalno
* -> znachi optimalno
Q-sostojbi Q*(s, a) - zapochnuvame vo sostojba 's', prevzemame nekoja akcija megjutoa ponatamu
	pretpostavuvame se' kje bide optimalno
[Site vrednosti na Q se izrazeni preku optimalni vrednosti koi idnite sostojbi bi gi imale]

Optimalna politika - bi pomagnala [ne e so sigurnost] vo izbor na dobra akcija
Vrednostite na polinjata ni' se potrebni za da agentot ja izbere
sekvencata na akcii

V_k(s) - zapochnuvash vo sostojba megjutoa znaejkji deka igrata zavrshuva vo 'k' chekori

k - kolku vo idnina gledam za da procenam neshto
k=0 -> imash 0 potezi do kraj na igrata.

strelkite ja pokazhuvaat koja e optimalnata, preporachanata, najdobrata akcija vo dadena sostojba;
toa e celta za da izbreme optimalna politika

vrednosta na sostojbata zavisi od politikata [74:00] 
black jack MDP **

gama => pretstavuva discount

uchi od site akcii, ne znaeme kade se naogjame
da gi nauchime Q vrednostite, najdobrite
pozitivnite i loshite iskustva konvertiraat da se izbira pooptimalna politika

noise = 0.2 => izveduvanje na sekoja akcija ima 80% da se pomesti vo
	nasoka na opcijata, a so po 0.1[10%] pomestuvanjata vo drugite 
	se sluchuvaat .

Zoshto od MDP da se premina na Reinforcement Learning? => bidejkji ne e simulacija,
	tuku iskustvo direktno, ne e nekakva procenka, planirame i potoa gi izbirame
	akciite tuku naprotiv ne znaeme ona vo zhivotot shto ne' ochekuva i probuvame.
	Idejata vo uchenje so pottiknuvanje e ona shto go uchime postojano doprinesuva
	na generalnoto uchenje koe go imame za ona shto pred nas e kako problem.

kaj MDP mozheme da primenime iterativna presmetka na vrednostite zatoa shto vo site
ravenki uchestvuvashe i nagradata i verojatnosniot model, a kaj RL agentot uchi za vreme na 
taa simulacija, od vistinski prevzemeni akcii, no posledicite mozhe da bidat i fatalni.
============================================================================

epizodi -> treba agentot da dojde do nekoja krajna pozicija, da ja dobie nagradata, za da mozhe
	da zakluchi neshto za ona shto se ishodi od dadeni sostojbi

Passive RL -> uchime od akcii da izvlekuvame ona shto ni e potrebno da gi nauchime
	vrednostite na sostojbite [tie ni bea bitni za da ja izvlecheme politikata]
	t.e. kje prevzememe akcija i ona shto sakame da vidime kolku e vrednosta na sostojbite

exploration - da istrazhime novi neshta, da go zbogatime znaenjeto, mozhebi i ponekogash kje bide losho
exploitation - ona shto go znaeme prethodno

*Vazhen koncept vo RL => da go iskoristime znaenjeto bez razlika dali e dobro ili losho

se koristi terminot AKTIVNO bidejkji agentot prevzema akcija, znachi kje prevzeme vistinska akcija vo realnosta,
sobira informacii za okolinata i go podobrua ona znaenje go imal, za razlika od ona shto go imame koga go uchish
modelot na okolinata za da mozhesh da planirash shto e najdobro, zatoa velevme PASIVNO uchenje. Tamu ucham
za mozham pak da se svedam na MDP za da mozham da isplaniram za toa shto e najdobroto go prevzemam ili da 
sporedam edna politika so druga.


Q - beshe vrzano so akciite i site mozhni sostojbi, najdobroto od site akcii, od site sostojbi vo koi mozham da preminam
od Q mozhevme vednash da izvlecheme akcija
=========================================================================================

pasivno -  => uchime od akciite da izveduvame ona shto ni e potrebno t.e. vrednost na sostojbite. Toa se sveduvashe na toa deka 
	nekoi ni dal, ni rekol 'eve ovaa politika vodija', sme zavzemale sluchajno izbrana, no za taa izbrana politika iako ne go znaeme
	modelot nie kje ja sledime politikata i na toj nachin agentot vsushnost imal mozhnost da uchi. Kje pravi i dobri i loshi sostojbi i 
	od akciite kade i da zavrshuva i ona shto beshe karakteristichno za pasivnoto uchenje, agentot, zatoa se veli i pasivno, ne gi izbira akciite,
	tuku samo sledi fiksna strategija i vrz osnova na toa treba da mu pomogne na toa vo presmetka na vrednostite od koi podocna izvlekuvavme
	politika.
aktivno -  => ona shto e od poseben interesen beshe deka sakame da deluvame vo okolinata bidejkji gi porcenuvame vrednostite na sostojbite,
	sakavme tie primeroci ili nasheto iskustvo da bide shto poraznoliko t.e. poseben fokus beshe na toa kako birame shto e toa shto go
	posetuvame ili vo koi sostojbi sakame da gi zememe predvid pri uchenjeto i idejata beshe deka uchime od iskustvo. Toa znachi sekoj
	primerok na iskustvo ni pomaga da ja azhurirame vrednosta ili da go podobrime nasheto znaenje ili konvergiranje kon ona shto se 
	vistinski vrednosti. Bidejkji e jasno deka ne mozheme da gi presmetame vistinskite vrednosti, ne znaeme nitu model na okolina i naprotiv
	so vakov nachin se nadevame deka kje konvergiraat kon ona shto e vistinskata megjutoa.

okolinata e DETERMINISTICHKA => ako se prevzeme odredena akcija, se znae ishodot koj kje bide daden
	
Q learning - uchenje bez politika.
Approximate Q learning - funkcija koja vkluchuva vo sebe mnogu obelezja karakteristiki za da se opishe dadeno neshto.

uchime od nashite greshki za da uchte imame doverba na ona shto imame naucheno prethodno
koga e 'exit' nemame procenka
===============================================================================================
deep neural network == convoluciski nevronski? mrezhi









