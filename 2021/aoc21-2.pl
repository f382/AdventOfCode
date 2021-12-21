#!/usr/bin/perl -w
use strict;
use bigint;

my $rolls = 3;
my $thre = 21;
my $dmax = 3;
my $high = 10;
# my @pos = (4, 8);
my @pos = (4, 3);

my @weight = (0, 0, 0, 1, 3, 3 + 3, 1 + 6, 3 + 3, 3, 1);
my %cache;

sub count {
	my $t = shift;
	my @pos = @{shift()};
	my @score = @{shift()};
	my @count = map { 0 } @pos;
	for (my $j = 0; $j < @score; ++$j) {
		if ($score[$j] >= $thre) {
			$count[$j] = 1;
			return @count;
		}
	}
	my $k = join(",", $t, @pos, @score);
	my $c = $cache{$k};
	return @$c if $c;
	for (my $d = $rolls * 1; $d <= $rolls * $dmax; ++$d) {
		my $w = $weight[$d];
		my $p = ($pos[$t] + $d - 1) % $high + 1;
		my @newpos = @pos;
		my @newscore = @score;
		$newpos[$t] = $p;
		$newscore[$t] = $score[$t] + $p;
		my @subcount = count(($t + 1) % 2, \@newpos, \@newscore);
		for (my $j = 0; $j < @pos; ++$j) {
			$count[$j] += $w * $subcount[$j];
		}
	}
	$cache{$k} = \@count;
	return @count;
}

my @count = count(0, \@pos, [ map { 0 } @pos ]);
print join("\n", @count), "\n";
