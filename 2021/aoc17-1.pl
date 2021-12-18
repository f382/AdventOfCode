#!/usr/bin/perl -w
use strict;

my $input1 = 'target area: x=20..30, y=-10..-5';

my $input2 = 'target area: x=287..309, y=-76..-48';

#################
my $input = $input2;

die unless $input =~ /target area: x=([+-]?\d+)..([+-]?\d+), y=([+-]?\d+)..([+-]?\d++)/;
my($x0, $x1, $y0, $y1) = ($1, $2, $3, $4);
print "$x0, $x1, $y0, $y1\n\n";


sub run {
	my($vx, $vy, $s, $t, $yy) = @_;

	my $good = 0;
	my($x, $y) = (0, 0);
	
	while ((!$s || ($vx <= 0 && $x >= $x0 || $vx >= 0 && $x <= $x1)) && (!$t || $y >= $y0)) {
		$$yy = $y if $yy && (!defined($$yy) || $$yy < $y);
		
		# print "$x, $y | $vx, $vy\n";
		if ((!$s || $x >= $x0 && $x <= $x1) && (!$t || $y >= $y0 && $y <= $y1)) {
			++$good;
		}

		$x += $vx;
		$y += $vy;
		$vx -= ($vx <=> 0);
		$vy -= 1;
		
		last if $vx == 0 && !$t;
	}
	
	return $good;
}

my $range = 2000;

my($vy_min, $vy_max) = (-$range);
my $hot = 0;
for (my $vy = $vy_min; ; ++$vy) {
	print "$vy?\n";
	if (run(0, $vy, 0, 1)) {
		$vy_min = $vy unless $hot;
		$hot ||= 1;
		$vy_max = $vy;
	} else {
		last if $vy >= $range;
	}
	# print "\n";
}
print "-----\n";

my($vx_min, $vx_max) = (-$range);
$hot = 0;
for (my $vx = $vx_min; ; ++$vx) {
	print "$vx?\n";
	if (run($vx, 0, 1, 0)) {
		$vx_min = $vx unless $hot;
		$hot ||= 1;
		$vx_max = $vx;
	} else {
		last if $vx >= $range;
	}
	# print "\n";
}
print "-----\n";

print "$vx_min..$vx_max, $vy_min..$vy_max\n";

print "=====\n";

my $y_max;
my($vx_good, $vy_good);
for (my $vx = $vx_min; $vx <= $vx_max; ++$vx) {
	for (my $vy = $vy_min; $vy <= $vy_max; ++$vy) {
		my $y_max_tentative;
		if (run($vx, $vy, 1, 1, \$y_max_tentative)) {
			print "$vx, $vy, $y_max_tentative\n";
			if (!defined($vy_good) || $vy_good < $vy) {
				$vx_good = $vx;
				$vy_good = $vy;
			}
			if (!defined($y_max) || $y_max < $y_max_tentative) {
				$y_max = $y_max_tentative;
			}
		}
	}
}
print "-----\n";

print "$vx_good, $vy_good -> $y_max\n";
