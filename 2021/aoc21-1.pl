#!/usr/bin/perl -w
use strict;

my $input1 = <<EOF
EOF
;

my $input2 = <<EOF
EOF
;

#################
my $input = $input1;

my $rolls = 3;
my $thre = 1000;
my $dice = 1;
my $dmax = 100;
my $max = 10;
my @pos = (4, 3);
my @score = map { 0 } @pos;
my $count = 0;

sub roll {
	++$count;
	$dice -= $dmax while $dice > $dmax;
	return $dice++;
}

sub go {
	my($pos, $score) = @_;
	my $d = 0;
	for (my $i = 0; $i < $rolls; ++$i) {
		$d += roll();
	}
	$pos += $d;
	$pos -= $max while $pos > $max;
	$score += $pos;
	my $win = ($score >= $thre) || 0;
	return ($pos, $score, $win);
}

my $end;
while (!defined($end)) {
	for (my $j = 0; $j < @pos; ++$j) {
		my $pos = $pos[$j];
		my $score = $score[$j];
		my $win = 0;
		print "$j: $pos, $score, $win -> ";
		($pos, $score, $win) = go($pos, $score);
		print "$j: $pos, $score, $win\n";
		$pos[$j] = $pos;
		$score[$j] = $score;
		$end = $j if $win;
		last if defined($end);
	}
}

my $loser_score = $score[1 - $end];
print "$loser_score, $count, ", $loser_score * $count, "\n";
