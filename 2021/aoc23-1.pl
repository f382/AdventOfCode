#!/usr/bin/perl -w
use strict;
use bigint;

my @input0 = ([1, 0], [0, 1]);

my @input1 = ([1, 0], [2, 3], [1, 2], [3, 0]);
<<EOF
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
EOF
;

my @input2 = ([0, 1], [2, 0], [1, 3], [3, 2]);
<<EOF
#############
#...........#
###A#C#B#D###
  #B#A#D#C#
  #########
EOF
;

##########
my @input = @input2;

my $roomcount = @input;
my $roomsize = 2;
my $sidesize = 2;
my $min = 1 - $sidesize;
my $max = $roomcount - 1 + $sidesize;
my @cost = (1, 10, 100, 1000);
my %cached = ();

sub domoveout {
	my($i, $d, $rroom, $rpark) = @_;
	my $j = 0;
	while (!defined($rroom->[$i][$j])) {
		if (++$j >= $roomsize) {
			do { print "\troom empty"; return };
		}
	}
	my $a = $rroom->[$i][$j];
	for (my $y = $j; defined($rroom->[$i][$y]) && $rroom->[$i][$y] == $i; ) {
		do { print "\tmove unnecessary"; return } if ++$y >= $roomsize;
	}
	my $p = $i + $d;
	if ($p < $min || $p > $max) {
		return;
	}
	do { print "\tspace full"; return } if defined($rpark->[$p]);
	my($k, $s, $l);
	if ($d > 0) {
		$k = $i + 1;
		$s = 1;
	} else {
		$k = $i;
		$s = -1;
	}
	$l = $j + 2;
	while ($k != $p) {
		do { print "\tspace blocked: $k"; return } if defined($rpark->[$k]);
		++$l;
		++$l unless $k <= 0 || $k >= $roomcount;
		$k += $s;
	}
	undef $rroom->[$i][$j];
	$rpark->[$p] = $a;
	return $l * $cost[$a];
}

sub domovein {
	my($p, $i, $rroom, $rpark) = @_;
	do { print "\tundefined"; return } unless defined($rpark->[$p]);
	my $a = $rpark->[$p];
	do { print "\twrong target"; return } if $i != $a;
	my $j = $roomsize - 1;
	while (defined($rroom->[$i][$j])) {
		return if $rroom->[$i][$j] != $i;
		if (--$j < 0) {
			do { print "\troom occupied"; return };
		}
	}
	my $d = $i - $p;
	my($t, $s, $l);
	if ($d >= 0) {
		$t = $i;
		$s = 1;
	} else {
		$t = $i + 1;
		$s = -1;
	}
	$l = $j + 2;
	my $k = $p;
	while ($k != $t) {
		$k += $s;
		do { print "\tway blocked: $k"; return } if defined($rpark->[$k]);
		++$l;
		++$l unless $k <= 0 || $k >= $roomcount;
	};
	undef $rpark->[$p];
	$rroom->[$i][$j] = $a;
	return $l * $cost[$a];
}

sub moveout {
	my($i, $d, $rroom, $rpark) = @_;
	print visualize($rroom, $rpark), " out $i : ", visnum($d);
	my @newroom = map { [ @$_ ] } @$rroom;
	my @newpark = @$rpark;
	my $cost = domoveout($i, $d, \@newroom, \@newpark);
	print defined($cost) ? " $cost\t" : "\n";
	return unless defined($cost);
	my $calc = calculate(\@newroom, \@newpark);
	return unless defined($calc);
	return $cost + $calc;
}

sub movein {
	my($p, $i, $rroom, $rpark) = @_;
	print visualize($rroom, $rpark), " in ", visnum($p), " -> $i";
	my @newroom = map { [ @$_ ] } @$rroom;
	my @newpark = @$rpark;
	my $cost = domovein($p, $i, \@newroom, \@newpark);
	print defined($cost) ? " $cost\t" : "\n";
	return unless defined($cost);
	my $calc = calculate(\@newroom, \@newpark);
	return unless defined($calc);
	return $cost + $calc;
}

sub isfinished {
	my($rroom, $rpark) = @_;
	print visualize($rroom, $rpark), " ";
	for (my $i = 0; $i < $roomcount; ++$i) {
		for (my $j = 0; $j < $roomsize; ++$j) {
			do { print "room incomplete: $i\n"; return } unless defined($rroom->[$i][$j]);
			do { print "room mismatch: $i\n"; return } if $rroom->[$i][$j] != $i;
		}
	}
	print "OK\n";
	return 0;
}

sub calculate {
	my($rroom, $rpark) = @_;
	my $key = visualize($rroom, $rpark);
	my $best = $cached{$key};
	if (defined($best)) {
		do { print "$key no (cached)\n"; return } if $best < 0;
		do { print "$key $best (cached)\n"; return $best } if defined($best);
	}
	$best = isfinished($rroom, $rpark);
	unless (defined($best)) {
		for (my $i = 0; $i < $roomcount; ++$i) {
			for (my $d = $min - $i; $d <= $max - $i; ++$d) {
				my $cost = moveout($i, $d, $rroom, $rpark);
				next unless defined($cost);
				$best = $cost if !defined($best) || $cost < $best;
			}
		}
		for (my $p = $min; $p <= $max; ++$p) {
			for (my $i = 0; $i < $roomcount; ++$i) {
				my $cost = movein($p, $i, $rroom, $rpark);
				next unless defined($cost);
				$best = $cost if !defined($best) || $cost < $best;
			}
		}
	}
	$cached{$key} = defined($best) ? $best : -1;
	return $best;
}

sub vis {
	return map { defined($_) ? $_ : '.' } @_;
}

sub visnum {
	return map { $_ > 0 ? "+$_" : $_ == 0 ? "-$_" : "$_" } @_;
}

sub visualize {
	my($rroom, $rpark) = @_;
	my @res = ();
	for (my $p = $min; $p <= $max; ++$p) {
		push @res, vis($rpark->[$p]);
		if ($p >= 0 && $p < $roomcount) {
			push @res, '[', vis(@{$rroom->[$p]}), ']';
		}
	}
	return join "", @res;
}

my @park;
$#park = $max - $min;
my @room = @input;
my $cost = calculate(\@room, \@park);
print defined($cost) ? $cost : "no solution", "\n";
