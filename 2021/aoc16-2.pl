#!/usr/bin/perl -w
use strict;

my $input1 = <<EOF
CE00C43D881120
EOF
;

my $input2 = <<EOF
E058F79802FA00A4C1C496E5C738D860094BDF5F3ED004277DD87BB36C8EA800BDC3891D4AFA212012B64FE21801AB80021712E3CC771006A3E47B8811E4C01900043A1D41686E200DC4B8DB06C001098411C22B30085B2D6B743A6277CF719B28C9EA11AEABB6D200C9E6C6F801F493C7FE13278FFC26467C869BC802839E489C19934D935C984B88460085002F931F7D978740668A8C0139279C00D40401E8D1082318002111CE0F460500BE462F3350CD20AF339A7BB4599DA7B755B9E6B6007D25E87F3D2977543F00016A2DCB029009193D6842A754015CCAF652D6609D2F1EE27B28200C0A4B1DFCC9AC0109F82C4FC17880485E00D4C0010F8D110E118803F0DA1845A932B82E200D41E94AD7977699FED38C0169DD53B986BEE7E00A49A2CE554A73D5A6ED2F64B4804419508B00584019877142180803715224C613009E795E58FA45EA7C04C012D004E7E3FE64C27E3FE64C24FA5D331CFB024E0064DEEB49D0CC401A2004363AC6C8344008641B8351B08010882917E3D1801D2C7CA0124AE32DD3DDE86CF52BBFAAC2420099AC01496269FD65FA583A5A9ECD781A20094CE10A73F5F4EB450200D326D270021A9F8A349F7F897E85A4020CF802F238AEAA8D22D1397BF27A97FD220898600C4926CBAFCD1180087738FD353ECB7FDE94A6FBCAA0C3794875708032D8A1A0084AE378B994AE378B9A8007CD370A6F36C17C9BFCAEF18A73B2028C0A004CBC7D695773FAF1006E52539D2CFD800D24B577E1398C259802D3D23AB00540010A8611260D0002130D23645D3004A6791F22D802931FA4E46B31FA4E4686004A8014805AE0801AC050C38010600580109EC03CC200DD40031F100B166005200898A00690061860072801CE007B001573B5493004248EA553E462EC401A64EE2F6C7E23740094C952AFF031401A95A7192475CACF5E3F988E29627600E724DBA14CBE710C2C4E72302C91D12B0063F2BBFFC6A586A763B89C4DC9A0
EOF
;

#################
my $input = $input2;

chomp $input;
my $binary = join("", map { sprintf("%04b", hex($_)) } split "", $input);

#print "$binary\n";

my %table = (
	0 => sub { my $z = 0; $z += shift while @_; return $z; },
	1 => sub { my $z = 1; $z *= shift while @_; return $z; },
	2 => sub { @_ = sort { $a <=> $b } @_; return shift; },
	3 => sub { @_ = sort { $a <=> $b } @_; return pop; },
	5 => sub { return $_[0] > $_[1] ? 1 : 0; },
	6 => sub { return $_[0] < $_[1] ? 1 : 0; },
	7 => sub { return $_[0] == $_[1] ? 1 : 0; },
);

my $sum = 0;

sub bin {
	my($b) = @_;
	return oct('0b' . $b);
}

sub crack {
	my($x, $l) = @_;
	my $t = substr($$x, $l);
	my $v = substr($$x, 0, $l);
	# print "$v $t\n";
	$$x = $t;
	return $v;
}

sub literal {
	my($x) = @_;
	my $pp = "";
	my $repeat = '1';
	while ($repeat eq '1') {
		my $ppp = crack($x, 5);
		$repeat = crack(\$ppp, 1);
		$pp .= $ppp;
	};
	my $p = bin($pp);
	print "Literal $p\n";
	return $p;
}

sub operator {
	my($x, $y) = @_;
	my $l = crack($x, 1);
	my @op = ();
	if (!$l) {
		my $b = bin(crack($x, 15));
		print "Operator with $b bits\n";
		my $p = crack($x, $b);
		while (length($p)) {
			push @op, parse(\$p);
		}
	} else {
		my $n = bin(crack($x, 11));
		print "Operator with $n packets\n";
		for (my $i = 0; $i < $n; ++$i) {
			push @op, parse($x);
		}
	}
	my $sub = $table{$y};
	my $r = $sub->(@op);
	print "Operator $y (@op) result: $r\n";
	return $r;
}

sub parse {
	my($x) = @_;
	print "?$$x\n";
	my $v = bin(crack($x, 3));
	my $y = bin(crack($x, 3));
	print "-> Packet version $v, type $y\n";
	$sum += $v;
	if ($y == 4) {
		return literal($x);
	} else {
		return operator($x, $y);
	}
	print "<-\n";
}

my $result = parse(\$binary);

print "$sum\n";
print "$result\n";