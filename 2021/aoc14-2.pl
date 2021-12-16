#!/usr/bin/perl -w
use strict;
use bigint;

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

my %pairs = ();

for (my $j = 0; $j < length($polymer) - 1; ++$j) {
	my $part = substr($polymer, $j, 2);
	# my $result = $mapping{$part} || "";
	++$pairs{$part}; # = [  ];
}

print join(",", %pairs), "\n";

for (my $i = 1; $i <= 40; ++$i) {
	print "$i:\n";
	my %copy = ();
	for my $part (keys %pairs) {
		my $result = $mapping{$part};
		next unless $result;
		my $x = substr($part, 0, 1) . $result;
		my $y = $result . substr($part, 1, 1);
		my $count = $pairs{$part};
		$copy{$x} += $count;
		$copy{$y} += $count;
		print "$part -> $x, $y: $count\n";
	}
	%pairs = %copy;
	print join(",", %pairs), "\n";
}

my %elems = ();
foreach my $part (keys %pairs) {
	my $x = substr($part, 0, 1);
	my $y = substr($part, 1, 1);
	$elems{$x} += $pairs{$part};
	$elems{$y} += $pairs{$part};
}

my @counts = sort { $a <=> $b } values %elems;
my $high = $counts[@counts - 1];
my $low = $counts[0];
my $diff = $high - $low;

print "$high, $low, $diff\n";
print(($diff - 1) / 2, "\n");
