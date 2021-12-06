#!/usr/bin/perl -w
use strict;

my $duration = 7;
my $delay = 2;

my @input = (
2,4,1,5,1,3,1,1,5,2,2,5,4,2,1,2,5,3,2,4,1,3,5,3,1,3,1,3,5,4,1,1,1,1,5,1,2,5,5,5,2,3,4,1,1,1,2,1,4,1,3,2,1,4,3,1,4,1,5,4,5,1,4,1,2,2,3,1,1,1,2,5,1,1,1,2,1,1,2,2,1,4,3,3,1,1,1,2,1,2,5,4,1,4,3,1,5,5,1,3,1,5,1,5,2,4,5,1,2,1,1,5,4,1,1,4,5,3,1,4,5,1,3,2,2,1,1,1,4,5,2,2,5,1,4,5,2,1,1,5,3,1,1,1,3,1,2,3,3,1,4,3,1,2,3,1,4,2,1,2,5,4,2,5,4,1,1,2,1,2,4,3,3,1,1,5,1,1,1,1,1,3,1,4,1,4,1,2,3,5,1,2,5,4,5,4,1,3,1,4,3,1,2,2,2,1,5,1,1,1,3,2,1,3,5,2,1,1,4,4,3,5,3,5,1,4,3,1,3,5,1,3,4,1,2,5,2,1,5,4,3,4,1,3,3,5,1,1,3,5,3,3,4,3,5,5,1,4,1,1,3,5,5,1,5,4,4,1,3,1,1,1,1,3,2,1,2,3,1,5,1,1,1,4,3,1,1,1,1,1,1,1,1,1,2,1,1,2,5,3
);

my @fishes = (0,0,0,0,0,0,0,0,0);

sub eat {
	foreach my $fish (@_) {
		++$fishes[$fish];
	}
}

sub tick {
	my($fish) = @_;
	my $x = shift @fishes;
	$fishes[$duration - 1] += $x;
	push @fishes, $x;
	print join(",", @$fish), "\n";
}

sub count {
	my $result = 0;
	foreach my $fish (@_) {
		$result += $fish;
	}
	return $result;
}

eat(@input);
print scalar(@fishes), "\n";
print join(",", @fishes), "\n";

for (my $j = 0; $j < 256   ; ++$j) {
	tick(\@fishes);
}

print scalar(@fishes), "\n";
print count(@fishes), "\n";
