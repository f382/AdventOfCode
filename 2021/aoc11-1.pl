#!/usr/bin/perl -w
use strict;

my @input = qw(
8261344656
7773351175
7527856852
1763614673
8674556743
6853382153
4135852388
2846715522
7477425863
4723888888
);

my $levels = [ map { [ split //, $_ ] } @input ];

my $p = @{$levels};
my $q = @{$levels->[0]};

print "$p,$q\n";

sub pulse {
	my($x, $y) = @_;
	return if $x < 0 || $x >= $p || $y < 0 || $y >= $q;
	my $v = $levels->[$x][$y];
	if (++$levels->[$x][$y] == 10) {
		pulse($x - 1, $y - 1);
		pulse($x - 1, $y);
		pulse($x - 1, $y + 1);
		pulse($x, $y - 1);
		pulse($x, $y + 1);
		pulse($x + 1, $y - 1);
		pulse($x + 1, $y);
		pulse($x + 1, $y + 1);
	}
}

sub renew {
	my $n = 0;
	for (my $x = 0; $x < $p; ++$x) {
		for (my $y = 0; $y < $q; ++$y) {
			if ($levels->[$x][$y] > 9) {
				$levels->[$x][$y] = 0;
				++$n;
			}
		}
	}
	return $n;
}

sub step {
	my $count = 0;
	for (my $x = 0; $x < $p; ++$x) {
		for (my $y = 0; $y < $q; ++$y) {
			pulse($x, $y);
		}
	}
	for (my $x = 0; $x < $p; ++$x) {
		for (my $y = 0; $y < $q; ++$y) {
			$count += renew($x, $y);
		}
	}
	return $count;
}

my $total = 0;

for (my $k = 0; $k < 100; ++$k) {
	print "$k:\n";
	my $count = step();
	$total += $count;
	print "$count -> $total\n";
}
