#!/usr/bin/perl -w
use strict;

my $input1 = <<EOF
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
EOF
;

my $input2 = <<EOF
OOBFPNOPBHKCCVHOBCSO

NS -> H
NN -> P
FF -> O
HF -> C
KN -> V
PO -> B
PS -> B
FB -> N
ON -> F
OK -> F
OO -> K
KS -> F
FN -> F
KC -> H
NC -> N
NB -> C
KH -> S
SV -> B
BC -> S
KB -> B
SC -> S
KP -> H
FS -> K
NK -> K
OC -> H
NH -> C
PH -> F
OS -> V
BB -> C
CC -> F
CF -> H
CP -> V
VB -> N
VC -> F
PK -> V
NV -> N
FO -> S
CK -> O
BH -> K
PN -> B
PP -> S
NF -> B
SF -> K
VF -> H
HS -> F
NP -> F
SH -> V
SK -> K
PC -> V
BO -> H
HN -> P
BK -> O
BP -> S
OP -> N
SP -> N
KK -> C
HB -> H
OF -> C
VH -> C
HO -> N
FK -> V
NO -> H
KF -> S
KO -> V
PF -> K
HV -> C
SO -> F
SS -> F
VN -> K
HH -> B
OB -> S
CH -> B
FH -> B
CO -> V
HK -> F
VK -> K
CN -> V
SB -> K
PV -> O
PB -> F
VV -> P
CS -> N
CB -> C
BS -> F
HC -> B
SN -> P
VP -> P
OV -> P
BV -> P
FC -> N
KV -> S
CV -> F
BN -> S
BF -> C
OH -> F
VO -> B
FP -> S
FV -> V
VS -> N
HP -> B
EOF
;

#################
my $input = $input2;

my $polymer = $1 if $input =~ /^(\w+)/;

my %mapping = ();
while ($input =~ /^(\w+)\s*->\s*(\w+)$/mg) {
	my($a, $b) = ($1, $2);
	$mapping{$a} = $b;
}

print join(",", %mapping), "\n";

print "$polymer\n";

for (my $i = 1; $i <= 10; ++$i) {
	my $new;
	for (my $j = 0; $j < length($polymer) - 1; ++$j) {
		my $part = substr($polymer, $j, 2);
		my $result = $mapping{$part} || "";
		# print "$part -> $result\n";
		$new .= substr($part, 0, 1) . $result;
	}
	$new .= substr($polymer, length($polymer) - 1, 1);
	$polymer = $new;
	print "$i: $polymer\n";
}

my %count = ();
my @e = split "", $polymer;
foreach my $e (@e) {
	$count{$e}++;
}

my @counts = sort { $a <=> $b } values %count;
my $high = $counts[@counts - 1];
my $low = $counts[0];
my $diff = $high - $low;

print "$high, $low, $diff\n";
