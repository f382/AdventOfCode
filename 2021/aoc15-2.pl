#!/usr/bin/perl -w
use strict;

my @input1 = qw(
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
)
;

my @input2 = qw(
1195699269169962618115739279199143968185692172285182183566221795877116121863721498957174621167918242
9115625874265799911728162199785394821312124845672192542919338584962177612992393151111933224334135452
8131729216517615863391649615129757111193739768481218915512112595941796747611211317938536136799846916
4962593132118152776959137321183383866772192116141953231951591444941238923298442361423618911179121722
1416121522926541915424971183698194981419338198971913131598831476211215251194523121195812188825994191
1928733692818149228324516927257499752678492513169166313451293451242416536442231355632161758212412115
4991813117359923391742392452551991886811936769148871994981937912114913399457193319831421852811811411
9996916186114911181317116839536799955741529114391992149574162387517295536711111425429134625723713721
6413152742931664293329711273293938913869998819228825914291212594321245569621831111918122371115465372
6722188749914139715213996125538481197121421593279313213185899225935111987292443132111143755985119529
6141512948818315114491829781295212661954323972616128386859935554992431321714445196118173993711558124
6523752772123188989169344829152218112692618197911472748191793562881571148348812711618193873951113528
8954722416492191712173547723412144532941317659721251223481537443946222823319111777131252431841192491
1219692484677226812231612539162313962112991811497897637829997937131866442336993772931261219369261847
6829142775922131221421699171891121995314918167141731413315221751156692121198315343979568132427284418
3282913221696695997376693291956466428248818465226925182129141125458581691913172218151994115999238119
1481242274838117149188214983221621273134622411136155992499972363312217924192499321799321224791726881
8429813642119162329227799294946451917123691918196133831319435771944687143576199628949499998747162763
8395921941954153228218312412725253615739691131793212984746387117261619752267161113249561125448521573
9211772949361922111776251228119342199252233939131825891962491746149161289543191281631521191528151729
2193925127318321141244277227599184821119727813113229679251991316121821158292233491611923846717119158
9151776354929118196915775164124249829119872627219946481741131411931381997631827757831918173194985349
6977211417599781311418423893723399355128981882844795231591948241298219665711731268447885454263587381
5349135211225233128116791411544311173251931562886224132922219393288176192118214216322799827219811119
6411921773896928424585199799991923414751791199198424646119917617472278291778719919799348821419148724
1423293283117293382227124359498154229373299921865286619381116123429144636291256599612311814659899913
8759614112712881116188816992852111129273765191958918918119921831721418783293917211991846211312611119
4121196173264119196199812212192496732231752189712187319121858237158115471625725612655876196419969937
2691914257589447739711834281999184259675111522131449811913611412236532193323199936291224416611271113
9192755461112725383245113492161211415871889986712211921819194916181391316311361383794418692693182242
9891838115191983532641471156115494911242254468716132462814716618248743273323215725412773332412787352
8722272933154344722732912929122813165682321995172313631238381398582132511122695349523913886143313161
3159822492451512821177591837987711928147328462539253731373891338415277199226141921412821329159184278
1832485826993984412417721923133667113613451764133131128131243811948335992447851989136113499938359145
9257768218141712472531919121131719239231356129229915988251523772791781168121416242161919415829553784
3891717441161141299323329871161725242416786365139551955251111486128147276258118276995359131236712228
4133422437419291126239531215239841331958132171112115233199891441933618863125616385327915193131413261
3253212961163124967414171286936361495972984828192712184792123182321681413111277312139439225347179423
2377431129712475315863521829984995789655626495798679371297781315999954158181121987521157274217196321
4592394651189519271259571319178919179154163791125439916726132231168199694259881318333239193192113119
5214358557391139332181292337556917331883162955773614429133947912812152812455942531392992452114431332
7914511581243189111526812729232853912768193314111226889191115838158147643977115139839624185229333941
4522297916392638141999211949998782928492795393326383963611461431112429161915374925921922371178131735
3116117224134523616636283974197178845139981151286731829271937711211286144713973157818336923155139559
1111295511971847293991217559316561942966392155489341944819143697999114911998211431142725136499468655
1891992683454413881151161751711242395932829172221141125821463261747311911338413341127471564991439546
2197193741181151969214374311187114311245112693918122115717139181914895295849765115821395921191918468
1918812176151559923226989551718951285211227784728295345569322191532911724359295794212198411816325194
7629928961228139545143278341914339752551791925569811939691921284247551268554865938529131518711139531
9451169285941298488483155291166241622428812963136859134265217869232119571587922942764129629377832992
1139592251182689154648182495457245293152859671536169199155915935138564186622314416113812197287681293
1119816611213622645121527229154149189414321711438818453128839964994812163235717235493169348364812413
1115793714933792898281139148211541133261863761597669828999211194232712941151917141932348896263117215
7143981722811931378639626221768345837123991164575136264218371995983942221883741712166415472137721341
3996548229222449762784779391842131791294982258228583737547892351961147281221614412549284975749816744
4922438251273127318171752385192919154922976632198383111121691511461911742517115181294162921997113543
9124461637891375169892252644331692827189167199413165129676424414953458991238723712121149814131276926
1895991515343259216934519621792999914371314528811251145931177912272284392121146199117591523391341219
9857722651665692811316272199623915819118857972163473846145219143133918931463916632958839922431916911
1989949857315678686251225273677553493256129745562479491356285341113695469127148417384622949976616524
1514345992981613134238939273116925182116613291995762152229187269412797171147386143842712248985831764
1211198422698743771451111739285421716192682661858199165165495211191228411993891839117216417485154548
3112992823483168122193816192136331881279211994456269862431176427242242345281287279732441869716191389
6871134463512275644982441198617971116471544111195519491429492742222154536972116714589962192221751385
5647154259376797491331854821299242541251251831183931114992139186921418195851432419352479398994111597
9675812361251547522613219729358639431998762941185794271951111743771188822419414981869983179671393777
2421978919226813559125816133917455796932224322127431441971323952423731378977778142299338998481694621
1162339193451725659611144929116291695927663312921334958711971618293843833635911817495624438269793162
7194289631493331742577212984661271734593922149964321251891912599313222711319511212521891991121817159
9654438184931123365769111117511792284663135618911981951661785454819122411394344529179916722212292335
9381539819769183334129143827547144947273493139711946941111969166113912799186126173317111193291991275
1661334416712633888242162591491114145161623757119234215118957518411596768891927145421233553867417999
1181181172699977113144191474311313161538171364172149949927239939139973157512351741924112395453921131
9799361923512814971481384219119182861846186769934949142334471794341454911588479116988949736973762124
2171161128751829419662251657166198159119931228153262933188511412214512163914514326141175526963632415
7612147289898569864114841291891153691232511181425187711712596649484685412198253969882929227211124238
2922314329122211671657786342123242914361173382744154572623461799951676191374747944234229247999178141
2121115817128199999591441995165254392173622999611859571327239469691126169563163219128197619925629693
3182672168559637413893445199112142497191251242941619924889893728121218651239589762192385494162894121
5791512214198437118967488718672546229179875132191211294148111849597464372811229816224599419181512211
9368472118122928199893477986398229912136629381261436753252174518924581148123243335312798324878848212
9725669655831621352979534192691954118988373532149622234171911923288798911129172114513273197359582283
1942761687342938618918838525761617921731659877171691411971516121317261319199891414189574729261122229
2159398941128831167829781939514329224978191194811728234752148114537973115426731412464878529111311111
1341328878619141146339146971488879124925985158551477411318189214192111643482297176134521189678728713
1442411429315169933594843144898323461746534243341425449339893312191772326944159125121565342118732742
7652125192884993111137974796199931588271953919118334511232831498213211927598715139913123931814522156
8168233671944113286991712612511185119717139652855151332182712722616311711191945817112211499911181521
1921296996453463169619436191262787335963117656489612357751271541937729111183295281896932769447431755
7289213684237311791995281282813488592291961373748236224817633211187113123962827228325981121148847993
6751411399143943283211281437425359722729191819645784229792576159332722378196994132679121397858245431
1917169121919847115634282129154464112929199989281129417312237913972281211921149592991829981144227161
1261189974825512854988913249612121789782128611383136321941939819131669773171112589654999631741194198
3219281818175692294456827118194628339263336829122263483717216243613482232758123183171992174992388688
7222941144112654273162264136491941693974211731736147294821427975517491486839269699142111413274944943
6411899713149171347537792921413961778812778428865681922491878751412131132519154425521912118977133146
6275715225136872451189435474268927729781495997951583367145623498914931591691279272517953212593721359
2433746293145649421172128991788265173129261744194121679239172142992115883692944413244861736711569739
2824762557912419114811994741439928232182929722212597932922111769122217134615129118682941162335962156
3156739229892221111493261433466816249792951919531787792919597117721856143161391231113153218196918133
)
;

#################
my @input = @input2;

my @risk = map { [ split "", $_ ] } @input;

my $p = @risk;
my $q = @{$risk[0]};

for (my $i = 0; $i < 5; ++$i) {
	for (my $j = 0; $j < 5; ++$j) {
		next if $i == 0 && $j == 0;
		for (my $x = 0; $x < $p; ++$x) {
			for (my $y = 0; $y < $q; ++$y) {
				my $a = $p * $i + $x;
				my $b = $q * $j + $y;
				my $v = $risk[$x][$y] + $i + $j;
				$v -= 9 while $v > 9;
				push @{$risk[$a]}, $v;
			}
		}
	}
}
	
$p = @risk;
$q = @{$risk[0]};

my @dijk = map { [ map { undef } (1..$q) ] } (1..$p);
my %visited = ();
my @queue = ();

print "risk:\n", join("\n", map { join(",", @$_) } @risk), "\n";

sub dijk {
	my($x, $y) = @_;
	for (my $i = -1; $i <= 1; ++$i) {
		my $a = $x + $i;
		next if $a < 0 || $a >= $p;
		for (my $j = -1; $j <= 1; ++$j) {
			my $b = $y + $j;
			next if $b < 0 || $b >= $q;
			next if $a == $x && $b == $y;
			next if $a != $x && $b != $y;
			next if $visited{$a}{$b};
			my $new = $dijk[$x][$y] + $risk[$a][$b];
			if (!defined($dijk[$a][$b]) || $new < $dijk[$a][$b]) {
				$dijk[$a][$b] = $new;
				# print "$a, $b <- $new\n";
				my $k = 0;
				++$k while $k < @queue and $queue[$k][0] <= $new;
				splice @queue, $k, 0, [$new, $a, $b];
			}
		}
	}
	$visited{$x}{$y} = 1;
	return $x == $p - 1 && $y == $q - 1;
}

$dijk[0][0] = 0;
@queue = ([0, 0, 0]);

print "dijk:\n", join("\n", map { join(",", map { $_ // "" } @$_) } @dijk), "\n";

while (@queue) {
	my($v, $x, $y) = @{shift @queue};
	print "($x, $y) ", scalar(@queue), "\n";
	my $result = dijk($x, $y);
	# print join("\;", map { join(",", map { $_ // "" } @$_) } @queue), "\n";
	# print join("\n", map { join(",", map { $_ // "" } @$_) } @dijk), "\n";
	last if $result;
}

print "dijk:\n", join("\n", map { join(",", map { $_ // "" } @$_) } @dijk), "\n";
